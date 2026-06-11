"""Code Designer Agent — produces a design document for code generation.

Takes free-form context and returns a comprehensive markdown design
document that gives the code generator everything it needs to produce
correct, clean code on the first attempt.

Supports one validation retry — if ``check_output`` finds structural
issues (missing sections, empty success criteria), the pipeline retries
with targeted feedback.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from akd_ext.agents._base import PydanticAIBaseAgent, PydanticAIBaseAgentConfig
from akd_ext.agents.code_generator.validator import ALLOWED_IMPORTS
from akd_ext.agents.code_generator.schemas import (
    CodeDesignerInputSchema,
    CodeDesignerOutputSchema,
)

__all__ = [
    "CodeDesignerAgent",
    "CodeDesignerConfig",
]


# ---------------------------------------------------------------------------
# Generic system prompt
# ---------------------------------------------------------------------------

_GENERIC_DESIGNER_PROMPT = """\
## ROLE

You are the **Code Designer** — a senior software architect for a code \
generation pipeline. You receive a task description and produce a \
comprehensive **design document** that enables a code-generator agent to \
write correct, clean, production-quality code on the first attempt.

You do NOT write code. You write the spec that makes code generation \
trivial.

---

## INPUT

You receive a single ``context`` field. It could be anything:
- A data processing or ETL pipeline
- A scientific analysis or experiment post-processing task
- A statistical computation or modelling job
- A file format conversion or transformation utility
- A report generation or visualisation task
- A machine learning preprocessing or evaluation script

Read it carefully and figure out what code needs to be built.

---

## YOUR JOB

Produce a **design document** (markdown) that is so thorough the code \
generator has zero ambiguity. Think of yourself as the architect handing \
a blueprint to a builder. If the blueprint is vague, the builder guesses \
wrong.

### Before you write anything, verify:
- Do you fully understand what the code needs to do?
- Is there only ONE way to interpret the requirements?
- Have you thought through edge cases?
- Do you know exactly what the inputs and outputs are?
- Can you trace through the logic mentally and confirm it's correct?

---

## DESIGN DOCUMENT FORMAT

Your ``design_document`` must be markdown with these sections:

### 1. GOAL & SUCCESS CRITERIA
Two parts:
- **Goal**: One paragraph. What problem does this code solve? Be specific \
  — not "process data" but "parse all CSV files under the input directory, \
  compute rolling 7-day averages per station, and produce one time-series \
  figure per metric."
- **Success criteria**: 3–5 concrete, verifiable statements that define \
  "done." These must be checkable by reading the code output — no \
  subjective judgments.
  - e.g., "Produces comparative AND anomaly figures for every variable \
    named in the task context"
  - e.g., "Computes the derived metrics the task asks for (rates of \
    change, differences from baseline)"
  - e.g., "Processes ALL matching datasets discovered under the input path"

**Success criteria may ONLY concern primary deliverables** — the figures, \
metrics, and outputs that answer the task's question. Do NOT write \
criteria about intermediate or bookkeeping artifacts (manifests, logs, \
debug tables, intermediate CSVs). Those belong in the WORKFLOW section, \
not in success criteria — a missing manifest must never block approval \
of scientifically complete code.

The success criteria are used downstream by a verifier agent. Make them \
specific enough that a reviewer can check yes/no.

Also populate the ``success_criteria`` structured field with these same \
criteria (one string per criterion).

### 2. APPROACH
How to solve it. The high-level strategy in 3–5 bullet points. \
What technique, what algorithm, what data flow. If there are \
alternative approaches, state which one you chose and why.

### 3. WORKFLOW
High-level flow of the script — the **what**, not the **how**. \
Think numbered steps, not function signatures. The code generator \
is a competent programmer; tell it the workflow and let it make \
implementation decisions.
- What are the main stages (discover → load → process → output)?
- What computations or transformations are needed?
- What outputs are produced at each stage?
- Any formulas or domain knowledge the generator wouldn't know.

Keep it to 10–20 bullet points max. Do NOT specify function names, \
argument lists, data structures, or control flow details — that's \
the generator's job.

### 4. CONSTRAINTS
What the code must NOT do. Anti-requirements and correctness boundaries.

Always include:
- Do NOT silently drop, fabricate, or modify input data — warn and skip
- Do NOT hardcode dataset-specific values (file counts, column names, \
  directory names) — discover them at runtime
- Do NOT assume a fixed number of input files or a fixed schema — be \
  adaptive
- **Path containment**: all reads stay inside ``--input-dir`` and all \
  writes stay inside ``--output-dir``. Paths referenced *inside* data \
  files (e.g., a binary-file path declared in a metadata/header file) \
  must be resolved relative to the file that declares them — never \
  follow absolute paths. If a reference points outside ``--input-dir``, \
  log a WARNING and skip it.

Add any task-specific constraints relevant to the context.

Constraints concern correctness, data integrity, and safety — NOT \
implementation strategy. Do NOT write constraints about performance, \
memory use, file-reading technique (whole-file vs byte-offset reads), \
or code style. The generator owns implementation choices, and the \
verifier does not enforce such constraints.

### 5. INPUT / OUTPUT SPECIFICATION

**Mandatory CLI contract** — every generated script MUST use ``argparse`` \
with exactly TWO arguments (no more, no less):
- ``--input-dir`` — path to the directory containing input data. The script \
  discovers what it needs inside this directory at runtime.
- ``--output-dir`` — path to the directory where ALL outputs are written.

Do NOT specify any additional CLI arguments. All parameters (thresholds, \
regex patterns, window sizes, constants, flags) must be hardcoded as \
named constants at the top of the script. The script must be runnable \
with only ``--input-dir`` and ``--output-dir``.

For this section, specify:
- **Inputs**: What files/subdirectories the script expects inside \
  ``--input-dir``, their format, and their layout.
- **Outputs**: Every file the script writes inside ``--output-dir``. \
  Filenames, format, content.

**The deliverables are figures.** Do NOT specify manifests, run-log \
files, debug tables, or summary CSVs — they add no value to the \
analysis. Warnings and skip notices go to the console, not to files. \
Specify a data-file output (CSV/JSON) ONLY if the task context \
explicitly requests one.

### 6. LIBRARIES
List every Python package the code should use, chosen from the allowed \
set (appended below). For each library, state what it's used for: \
``numpy — array operations and numerical computation``

### 7. BEST PRACTICES
Specific coding rules the generator must follow:
- Single self-contained file, no external dependencies
- Use ``pathlib.Path`` for all file operations (NOT ``os.path``)
- Wrap all I/O in try/except with informative error messages
- Use type hints on function signatures
- Use descriptive variable names
- Add docstrings to every function
- Handle missing or corrupt input files gracefully (warn + skip)
- Any task-specific practices relevant to the context

### 8. VISUALISATION SPECIFICATIONS (if the task produces plots)
Only include this section if the code needs to generate visualisations.

**Relevance over volume.** What matters is that EVERY figure helps \
answer the task's question. Before specifying a figure, ask: "how does \
this figure help accept or reject the hypothesis / answer the \
question?" If you cannot answer that in one sentence, cut the figure. \
A plot that merely describes the data without informing the question \
is noise, not thoroughness.

**Relevance sets the filter; the causal chain sets the floor.** A \
hypothesis proposes a mechanism: something was changed (the forcing), \
it propagates somehow (the mechanism), and an effect is predicted (the \
outcome). Your figures must cover ALL THREE links — with comparative \
views AND anomaly (experiment − baseline) views of each. If you only \
plot the outcome, an expert will ask "where is the evidence for the \
mechanism?" A comparative multi-experiment study that covers its \
causal chain typically needs 8–15 figures; a design with fewer than 6 \
for a multi-variable hypothesis has almost certainly cut mechanism \
evidence, not noise.

**Guidelines:**
- Cover all key variables and relationships described in the task context.
- If the task involves comparison across groups, datasets, or conditions, \
  produce both **per-group** and **comparative** figures.
- Include **derived metrics** where they add insight (rates of change, \
  differences, ratios, distributions).
- Group related metrics into **multi-panel composite figures** where it \
  aids readability.
- Think about what a domain expert reviewing the output would want to see.
- **Never save an empty figure.** If none of a figure's required data is \
  available at runtime, the script must skip that figure entirely and \
  log a WARNING explaining why — a blank plot with axes and no data is \
  worse than no plot.

For each figure, specify:
- **Filename**: e.g. ``metric_comparison.png``
- **Type**: line / scatter / bar / heatmap / histogram / contour / \
  multi-panel composite
- **What it shows**: exactly what data on each axis, which variables
- **Labels**: title, x-label, y-label, legend entries
- **Purpose**: why this figure matters for answering the task's question
- **Computation**: if a derived field is needed, specify the formula

### 9. EDGE CASES & GOTCHAS
What could go wrong? What should the code handle?
- Missing files or empty directories
- Empty or malformed datasets
- Unexpected data shapes or column names
- Division by zero in computations
- Large files that might not fit in memory
- Any task-specific pitfalls

---

## RULES

- Be **thorough on outputs, concise on boilerplate**. The visualisation \
  and I/O sections should be exhaustive. The workflow and best practices \
  sections should be brief — the generator knows how to write argparse \
  and try/except.
- Be **precise** where it counts. Data formats, file layouts, formulas, \
  and domain knowledge that the generator wouldn't know on its own.
- Be **correct**. Think through the logic. If a step would fail, \
  fix it before writing it down.
- Do NOT include code — workflow steps and plain English only. \
  The generator writes the actual Python.
- Do NOT specify matplotlib formatting details (dpi, tight_layout, \
  Agg backend, plt.close). The generator handles those. Focus on \
  **what** to plot, not **how** to configure matplotlib.
- The ``libraries`` and ``output_files`` fields must match what you \
  wrote in sections 6 and 5 respectively.
- The ``success_criteria`` field must match what you wrote in section 1.
- **Quality bar**: imagine a domain expert reviewing the output. They \
  should say "this covers everything I need" — and they should never \
  have to ask "why is this figure here?". Every figure earns its place \
  by informing the task's question.
"""


# ---------------------------------------------------------------------------
# Shared prompt assembly & validation
# ---------------------------------------------------------------------------

_REQUIRED_SECTIONS = (
    "GOAL",
    "APPROACH",
    "WORKFLOW",
    "CONSTRAINTS",
    "INPUT",       # matches INPUT / OUTPUT or INPUT/OUTPUT
    "LIBRARIES",
)

_DATA_FORMAT_CONTEXT_DESC = (
    "Domain-specific data format description appended to the system "
    "prompt. Describes file formats, variable inventories, directory "
    "structure, and reading patterns."
)

_ANALYSIS_METHODOLOGY_DESC = (
    "Domain-specific analysis methodology appended to the system prompt. "
    "Teaches the designer how to think about the task domain: what "
    "metrics matter, what derived computations to include, what makes "
    "an output thorough vs superficial."
)


def _assemble_designer_prompt(config: "CodeDesignerConfig") -> str:
    """Build the full system prompt from config fields."""
    parts = [config.system_prompt]

    libs_sorted = sorted(ALLOWED_IMPORTS)
    parts.append(
        "\n\n---\n\n## ALLOWED LIBRARIES\n\n"
        + ", ".join(libs_sorted)
        + "\n\nForbidden: networking (requests, urllib, socket, http), "
        "system access (os, sys, subprocess, shutil), "
        "serialisation (pickle, shelve, marshal), "
        "dynamic execution (eval, exec, compile, __import__), "
        "low-level (ctypes, cffi), concurrency (multiprocessing, threading)."
    )

    if config.data_format_context.strip():
        parts.append(
            "\n\n---\n\n## DATA FORMAT REFERENCE\n\n"
            + config.data_format_context.strip()
        )

    if config.analysis_methodology.strip():
        parts.append(
            "\n\n---\n\n## SCIENTIFIC ANALYSIS METHODOLOGY\n\n"
            + config.analysis_methodology.strip()
        )

    return "".join(parts)


def _validate_designer_output(output: Any) -> str | None:
    """Domain-specific validation for designer output."""
    if not isinstance(output, CodeDesignerOutputSchema):
        return None

    doc = output.design_document.strip()
    if not doc:
        return "design_document is empty — produce a comprehensive design spec."
    if len(doc) < 200:
        return (
            "design_document is too short. Include all required sections: "
            "GOAL & SUCCESS CRITERIA, APPROACH, WORKFLOW, CONSTRAINTS, "
            "INPUT/OUTPUT, LIBRARIES, BEST PRACTICES, and EDGE CASES."
        )

    doc_upper = doc.upper()
    missing = [s for s in _REQUIRED_SECTIONS if s not in doc_upper]
    if missing:
        return (
            f"design_document is missing required sections: {', '.join(missing)}. "
            "Include all sections: GOAL & SUCCESS CRITERIA, APPROACH, "
            "WORKFLOW, CONSTRAINTS, INPUT/OUTPUT, LIBRARIES, "
            "BEST PRACTICES, and EDGE CASES."
        )

    if not output.libraries:
        return "libraries list is empty — the code needs at least one library."

    if not output.success_criteria:
        return (
            "success_criteria list is empty — provide 3-5 concrete, "
            "verifiable criteria that define when the code is 'done'."
        )

    disallowed = set(output.libraries) - ALLOWED_IMPORTS
    if disallowed:
        return (
            f"libraries not in allowed set: {disallowed}. "
            f"Choose only from: {', '.join(sorted(ALLOWED_IMPORTS))}"
        )
    return None


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


class CodeDesignerConfig(PydanticAIBaseAgentConfig):
    """Configuration for the Code Designer Agent."""

    system_prompt: str = Field(
        default=_GENERIC_DESIGNER_PROMPT,
        description=(
            "Base system prompt. The allowed-library list, "
            "data_format_context, and analysis_methodology are appended "
            "at construction time."
        ),
    )
    model_name: str = Field(default="openai:gpt-5.2")
    data_format_context: str = Field(default="", description=_DATA_FORMAT_CONTEXT_DESC)
    analysis_methodology: str = Field(default="", description=_ANALYSIS_METHODOLOGY_DESC)


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------


class CodeDesignerAgent(
    PydanticAIBaseAgent[CodeDesignerInputSchema, CodeDesignerOutputSchema],
):
    """Produces a comprehensive design document for code generation.

    The design document is a markdown spec that covers goal & success
    criteria, approach, workflow, constraints, I/O spec, libraries, best
    practices, plot specs (if applicable), and edge cases. The code
    generator follows it to produce correct code on the first attempt.
    """

    input_schema = CodeDesignerInputSchema
    output_schema = CodeDesignerOutputSchema
    config_schema = CodeDesignerConfig

    def __init__(self, config: CodeDesignerConfig | None = None) -> None:
        config = config or self.config_schema()
        assembled = _assemble_designer_prompt(config)
        config = config.model_copy(update={"system_prompt": assembled})
        super().__init__(config)

    def check_output(self, output) -> str | None:
        return _validate_designer_output(output) or super().check_output(output)
