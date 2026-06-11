"""Code Generator Agent — produces Python code from a design document.

Takes the design document (from the designer) and the original context.
On retries it also receives ``correction_feedback`` with the validation
failure reason so the model can self-correct.

Returns :class:`CodeGeneratorOutputSchema` with complete source, libraries,
output files, and an explanation.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from akd_ext.agents._base import PydanticAIBaseAgent, PydanticAIBaseAgentConfig
from akd_ext.agents.code_generator.validator import ALLOWED_IMPORTS
from akd_ext.agents.code_generator.schemas import (
    CodeGeneratorInputSchema,
    CodeGeneratorOutputSchema,
)

__all__ = [
    "CodeGeneratorAgent",
    "CodeGeneratorConfig",
]


# ---------------------------------------------------------------------------
# Generic system prompt
# ---------------------------------------------------------------------------

_GENERIC_GENERATOR_PROMPT = """\
## ROLE

You are the **Code Generator**. You receive a design document (a detailed \
markdown spec) and produce a **complete, self-contained Python script** \
that implements it exactly.

---

## INPUTS

1. **design_document** — A comprehensive markdown spec from the Code \
   Designer. It contains: goal & success criteria, approach, workflow, \
   constraints, I/O spec, libraries, best practices, visualisation \
   specifications (if any), and edge cases. \
   Follow it closely — the designer has already made the architectural \
   decisions.
2. **context** — The original task description for additional background.
3. **correction_feedback** — If non-empty, your previous code was rejected \
   by a validator. Fix the specific issues described.

---

## YOUR JOB

Translate the design document into a single Python file. Follow the \
WORKFLOW section step-by-step and honor every CONSTRAINT. Respect every \
best practice listed in the design document.

---

## CODE QUALITY RULES

- **Single file**. Everything in one self-contained script.
- **No external dependencies** beyond the allowed library set.
- **Type hints** on all function signatures.
- **Docstrings** on every function.
- **Descriptive names** — no single-letter variables except loop indices.
- **pathlib.Path** for all file operations. NOT ``os.path``.
- **try/except** around all I/O with informative error messages.
- **Graceful degradation** — if an input file is missing or corrupt, \
  log a warning and skip it. Don't crash.
- **Path containment** — read only inside ``--input-dir``, write only \
  inside ``--output-dir``. Paths referenced *inside* data files (e.g. a \
  binary-file path declared in a header/metadata file) must be resolved \
  relative to the file that declares them — never follow absolute \
  paths. Log a WARNING and skip anything pointing outside \
  ``--input-dir``.
- **CLI interface** — use ``argparse`` with exactly TWO arguments \
  (names and count are non-negotiable):
  - ``--input-dir`` — path to input data directory.
  - ``--output-dir`` — path to output directory for all results.
  Do NOT add any other CLI arguments. All parameters (thresholds, \
  regex patterns, window sizes, flags) must be defined as constants \
  at the top of the script. The user runs the script with only \
  ``--input-dir`` and ``--output-dir`` — nothing else.
- ``if __name__ == '__main__': main()`` entry point.

---

## COMPLETENESS — NON-NEGOTIABLE

Implement **every** figure, table, and output file listed in the design \
document. Do NOT silently drop any. The design document was produced by a \
domain expert; every artefact exists to support the hypothesis. If the \
design specifies 18 figures, the code must produce 18 figures. A long \
script is fine — an incomplete script is not.

If you cannot implement a specific figure (e.g., required data is not \
described), emit a clear ``WARNING`` log explaining why it was skipped \
so the intent checker can see it. Never skip silently.

The reverse also holds: do NOT produce outputs the design document does \
not specify — no manifests, run-log files, debug tables, or extra CSVs. \
Warnings go to the console (``warnings`` module or ``print``), not to \
log files.

---

## PLOT FORMATTING (when the design document specifies plots)

- ``matplotlib.use('Agg')`` BEFORE importing ``pyplot``
- ``dpi=150`` on all ``savefig()`` calls
- ``plt.tight_layout()`` before every save
- ``plt.close()`` after every save to free memory
- When comparing multiple datasets: ALL on the same axes with a legend
- Consistent color scheme across all plots (use a colour list or colormap)
- Grid on, clear labels with units
- **Never save an empty figure** — if none of a figure's data is \
  available at runtime, skip the figure entirely and log a WARNING. \
  A blank plot with axes and no curves must never be written to disk.

---

## CORRECTION FEEDBACK

If ``correction_feedback`` is non-empty, your previous code was rejected. \
Read the feedback carefully and fix the SPECIFIC issues described:
- **Forbidden import**: replace with an allowed alternative. \
  ``os.listdir()`` → ``pathlib.Path.iterdir()``, \
  ``os.path.join()`` → ``pathlib.Path / "child"``, \
  ``os.makedirs()`` → ``pathlib.Path.mkdir(parents=True, exist_ok=True)``.
- **Intent mismatch**: re-read the design document and implement what \
  it actually asks for.
- **Missing library**: add it to the ``libraries`` list.
- Do NOT rewrite from scratch — fix the specific issues.
"""


# ---------------------------------------------------------------------------
# Prompt assembly & validation
# ---------------------------------------------------------------------------

_DATA_FORMAT_CONTEXT_DESC = (
    "Domain-specific data format description appended to the system "
    "prompt. Code examples for reading specific file formats, etc."
)

_FORBIDDEN_EXAMPLES = [
    "os", "sys", "subprocess", "shutil", "socket", "ssl",
    "urllib", "requests", "httpx", "http", "ftplib", "smtplib",
    "pickle", "shelve", "marshal", "ctypes", "cffi",
    "multiprocessing", "threading", "importlib",
]


def _assemble_generator_prompt(config: Any) -> str:
    """Build the full system prompt from config fields."""
    parts = [config.system_prompt]

    allowed = sorted(ALLOWED_IMPORTS)
    parts.append(
        "\n\n---\n\n## ALLOWED LIBRARIES\n\n"
        + ", ".join(allowed)
        + "\n\n**FORBIDDEN** (the validator will reject your code):\n"
        + ", ".join(_FORBIDDEN_EXAMPLES)
        + "\n\nAlso forbidden: eval(), exec(), compile(), __import__()."
    )

    if getattr(config, "data_format_context", "").strip():
        parts.append(
            "\n\n---\n\n## DATA FORMAT REFERENCE\n\n"
            + config.data_format_context.strip()
        )

    return "".join(parts)


def _validate_generator_output(output: Any) -> str | None:
    """Domain-specific validation for generator output."""
    if not isinstance(output, CodeGeneratorOutputSchema):
        return None

    code = output.code.strip()
    if not code:
        return "code field is empty — generate complete Python source."
    if len(code.splitlines()) < 10:
        return (
            "code is too short (< 10 lines). Generate a complete, "
            "self-contained script."
        )

    disallowed = set(output.libraries) - ALLOWED_IMPORTS
    if disallowed:
        return (
            f"libraries not in allowed set: {disallowed}. "
            f"Choose only from: {', '.join(sorted(ALLOWED_IMPORTS))}"
        )

    if "--input-dir" not in code:
        return (
            "code is missing mandatory --input-dir argument. "
            "Every script must accept --input-dir and --output-dir."
        )
    if "--output-dir" not in code:
        return (
            "code is missing mandatory --output-dir argument. "
            "Every script must accept --input-dir and --output-dir."
        )

    # Enforce exactly 2 CLI arguments — no extras allowed
    add_arg_count = code.count("add_argument(")
    if add_arg_count > 2:
        return (
            f"code defines {add_arg_count} CLI arguments but only 2 are "
            "allowed (--input-dir and --output-dir). All other parameters "
            "must be defined as constants at the top of the script, not "
            "as CLI arguments."
        )

    if "def " not in code:
        return (
            "code has no function definitions. Generate modular code "
            "with functions, not a bare script."
        )

    if 'if __name__' not in code:
        return (
            "code is missing `if __name__ == '__main__':` entry point. "
            "Every script must have a guarded main entry point."
        )
    return None


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


class CodeGeneratorConfig(PydanticAIBaseAgentConfig):
    """Configuration for the Code Generator Agent."""

    system_prompt: str = Field(
        default=_GENERIC_GENERATOR_PROMPT,
        description="Base system prompt. data_format_context is appended at runtime.",
    )
    model_name: str = Field(default="openai:gpt-5.2")
    data_format_context: str = Field(default="", description=_DATA_FORMAT_CONTEXT_DESC)


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------


class CodeGeneratorAgent(
    PydanticAIBaseAgent[CodeGeneratorInputSchema, CodeGeneratorOutputSchema],
):
    """Produces Python code from a design document.

    Takes the design document (from the designer) plus the original
    context, and returns a complete, self-contained Python script with
    CLI interface, type hints, and graceful error handling.
    """

    input_schema = CodeGeneratorInputSchema
    output_schema = CodeGeneratorOutputSchema
    config_schema = CodeGeneratorConfig

    def __init__(self, config: CodeGeneratorConfig | None = None) -> None:
        config = config or self.config_schema()
        assembled = _assemble_generator_prompt(config)
        config = config.model_copy(update={"system_prompt": assembled})
        super().__init__(config)

    def check_output(self, output) -> str | None:
        return _validate_generator_output(output) or super().check_output(output)
