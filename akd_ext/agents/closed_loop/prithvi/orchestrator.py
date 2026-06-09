"""Prithvi pipeline orchestrator — called by Temporal worker on HPC.

Receives a config dict from ``job_submit``, patches it with server-side
values (paths, checkpoints, credentials), validates it, and writes a
SLURM script for execution.

Public API:
    setup_job(job_id, config) -> dict
"""

from __future__ import annotations

import copy
import os
from pathlib import Path

import yaml
from loguru import logger

# ---------------------------------------------------------------------------
# HPC constants — edit here if server paths change
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path("/rhome/vkolluru/AKD/CLSW_new")
WORKSPACE_ROOT = PROJECT_ROOT / "workspace"
CONDA_ENV = "r2o_crop"

PATHS_DEFAULTS = {
    "download_script": str(PROJECT_ROOT / "scripts" / "download_all_datasets.py"),
    "statistical_tests": str(PROJECT_ROOT / "statistical_tests"),
    "prithvi_modules": str(PROJECT_ROOT / "prithvi"),
    "flood_validation": str(PROJECT_ROOT / "scripts" / "flood_validation_v26.py"),
}

CHECKPOINT_DEFAULTS = {
    "flood_checkpoint": "/rhome/vkolluru/r2o/r2o_flood/Prithvi-EO-2.0-300M-TL-Sen1Floods11/Prithvi-EO-V2-600-Sen1Floods11.pt",
    "crop_checkpoint": "/rhome/vkolluru/r2o/r2o_crop/scripts/best-epoch=117_ep120.ckpt",
    "burn_checkpoint": "/rhome/rshinde/r2o/burnscars/burn_scar_v2/ckpt/mr01eo-workshop.ckpt",
    "burn_config": "/rhome/rshinde/r2o/burnscars/burn_scar_v2/ckpt/mr01eo_config.yaml",
}

CATALOG_PATHS = {
    "flood": str(PROJECT_ROOT / "event_database" / "flood_events_catalog.csv"),
    "burn": str(PROJECT_ROOT / "event_database" / "burn_events_catalog.csv"),
}


# ---------------------------------------------------------------------------
# 1. patch_config — inject server-side values Stage 3 doesn't know
# ---------------------------------------------------------------------------


def patch_config(config: dict) -> dict:
    """Add HPC paths, checkpoints, and GFM credentials to a Stage-3 config.

    Stage 3 only produces scientific intent (rq, events flags, analysis).
    This fills in everything the pipeline scripts need to actually run.
    """
    cfg = copy.deepcopy(config)

    # Paths
    paths = cfg.setdefault("paths", {})
    for k, v in PATHS_DEFAULTS.items():
        paths.setdefault(k, v)

    # Checkpoints
    prithvi = cfg.setdefault("prithvi", {})
    for k, v in CHECKPOINT_DEFAULTS.items():
        prithvi.setdefault(k, v)

    # GFM credentials from env vars (flood only)
    if prithvi.get("flood"):
        gfm = cfg.setdefault("gfm", {})
        gfm.setdefault("date_range_days", 5)
        email = os.environ.get("GFM_JRC_EMAIL", "")
        pwd = os.environ.get("GFM_JRC_PASSWORD", "")
        if email and pwd:
            gfm["jrc_email"] = email
            gfm["jrc_password"] = pwd

    # Catalog path for screening
    events = cfg.get("events", {})
    if events.get("source") == "pending_screening":
        screening = events.setdefault("screening", {})
        hazard = screening.get("hazard_type", "flood")
        screening.setdefault("catalog_path", CATALOG_PATHS.get(hazard, CATALOG_PATHS["flood"]))

    # Resolve relative output.dir against PROJECT_ROOT
    output = cfg.get("output", {})
    out_dir = output.get("dir", "")
    if out_dir and not os.path.isabs(out_dir):
        output["dir"] = str(PROJECT_ROOT / out_dir)

    return cfg


# ---------------------------------------------------------------------------
# 2. validate_config — quick sanity checks
# ---------------------------------------------------------------------------


def validate_config(config: dict) -> list[str]:
    """Check config has required sections. Returns list of error strings."""
    errors: list[str] = []

    # Required sections
    for section in ("rq", "events", "prithvi", "output"):
        if not isinstance(config.get(section), dict):
            errors.append(f"Missing section: {section}")

    if errors:
        return errors

    # RQ fields
    for field in ("text", "h0", "h1"):
        if not config["rq"].get(field, "").strip():
            errors.append(f"rq.{field} is empty")

    # At least one prithvi task
    p = config["prithvi"]
    if not any(p.get(t) for t in ("flood", "burn", "crop")):
        errors.append("No prithvi task enabled (flood/burn/crop all false)")

    # Events
    source = config["events"].get("source", "")
    if source == "custom" and not config["events"].get("custom_events"):
        errors.append("events.source=custom but no custom_events")
    elif source == "pending_screening" and not config["events"].get("screening"):
        errors.append("events.source=pending_screening but no screening config")

    # Output
    if not config["output"].get("dir", "").strip():
        errors.append("output.dir is empty")

    return errors


# ---------------------------------------------------------------------------
# 3. setup_job — write config + SLURM script, return metadata
# ---------------------------------------------------------------------------


def setup_job(job_id: str, config: dict) -> dict:
    """Patch config, validate, write YAML + SLURM script.

    Called by Temporal worker after ``job_submit``.

    Returns dict with job_id, paths, and metadata.
    Raises ValueError if validation fails.
    """
    patched = patch_config(config)

    errors = validate_config(patched)
    if errors:
        raise ValueError("Config validation failed:\n" + "\n".join(errors))

    # Write config
    job_dir = WORKSPACE_ROOT / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    config_path = job_dir / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(patched, f, default_flow_style=False, sort_keys=False)

    # Write SLURM script
    slurm_content = _build_slurm_script(job_id, config_path, job_dir, patched)
    slurm_path = job_dir / "run.slurm"
    slurm_path.write_text(slurm_content)

    output_dir = patched.get("output", {}).get("dir", str(job_dir / "output"))
    logger.info(f"[{job_id}] Setup complete: output={output_dir}")

    return {
        "job_id": job_id,
        "job_dir": str(job_dir),
        "config_path": str(config_path),
        "slurm_path": str(slurm_path),
        "output_dir": output_dir,
    }


# ---------------------------------------------------------------------------
# SLURM script generation
# ---------------------------------------------------------------------------


def _build_slurm_script(
    job_id: str, config_path: Path, job_dir: Path, config: dict
) -> str:
    """Generate SLURM script: screen events (if needed) → run pipeline."""
    needs_gpu = any(config.get("prithvi", {}).get(t) for t in ("flood", "burn", "crop"))
    gpu_line = "#SBATCH --gres=gpu:1" if needs_gpu else "# no GPU"
    skip_screening = config.get("events", {}).get("source") == "custom"

    # Build screen_events.py args
    screen_args = f"--config {config_path}"
    if not skip_screening:
        screening = config.get("events", {}).get("screening", {})
        mode = screening.get("mode", "auto")
        screen_args += f" --mode {mode} --parallel 4"
        if screening.get("hazard_type"):
            screen_args += f" --hazard_type {screening['hazard_type']}"
        max_ev = config.get("events", {}).get("max_events")
        if max_ev:
            screen_args += f" --max_events {max_ev}"

        # Manual mode: screen_events.py reads bbox/date from CLI, not config
        if mode == "manual":
            bbox = screening.get("bbox")
            if bbox and len(bbox) == 4:
                screen_args += f" --bbox {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}"
            flood_date = screening.get("flood_date")
            if flood_date:
                screen_args += f" --flood_date {flood_date}"
            event_id = screening.get("event_id")
            if event_id:
                screen_args += f" --event_id {event_id}"

        # Catalog mode: pass specific event IDs if provided
        elif mode == "catalog":
            event_ids = screening.get("event_ids")
            if event_ids:
                screen_args += " --event_ids " + " ".join(str(eid) for eid in event_ids)

    # Estimate walltime
    n = config.get("events", {}).get("max_events", 10)
    if skip_screening:
        n = len(config.get("events", {}).get("custom_events", []))
    hours = min(12, max(1, (30 + n * 20 + 15) // 60 + 1))

    screening_block = f"""
echo "=== Phase 0: Event Screening ==="
python -u scripts/screen_events.py {screen_args} 2>&1 | tee -a "$LOG"
if [ $? -ne 0 ]; then echo "Screening failed" >> "$LOG"; exit 1; fi
""" if not skip_screening else """
echo "Phase 0 skipped (events pre-verified)"
"""

    return f"""#!/bin/bash
#SBATCH --job-name=prithvi_{job_id}
#SBATCH --partition=gpu
#SBATCH --output={job_dir}/slurm_%j.out
#SBATCH --error={job_dir}/slurm_%j.err
#SBATCH --time={hours:02d}:00:00
#SBATCH --mem=32G
{gpu_line}

set -uo pipefail
cd {PROJECT_ROOT}
source activate {CONDA_ENV}
export CUDA_VISIBLE_DEVICES=${{SLURM_LOCALID:-0}}

LOG="{job_dir}/pipeline.log"
echo "Job {job_id} started $(date)" | tee "$LOG"
{screening_block}
echo "=== Phases 1-5: Pipeline ==="
python -u prithvi/pipeline_executor.py --config {config_path} --no_pause 2>&1 | tee -a "$LOG"
if [ $? -ne 0 ]; then echo "Pipeline failed" >> "$LOG"; exit 1; fi

echo "Job {job_id} finished $(date)" | tee -a "$LOG"
"""
