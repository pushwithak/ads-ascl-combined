"""Pydantic schemas for the code-generation pipeline.

Intermediate data models use plain ``BaseModel``.  Agent I/O schemas inherit
from ``akd._base.InputSchema`` / ``OutputSchema`` for framework compatibility.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from akd._base import InputSchema, OutputSchema

__all__ = [
    # Intermediate
    "VettedCode",
    "AttemptRecord",
    # Designer
    "CodeDesignerInputSchema",
    "CodeDesignerOutputSchema",
    # Generator
    "CodeGeneratorInputSchema",
    "CodeGeneratorOutputSchema",
    # Intent checker
    "IntentCheckerInputSchema",
    "IntentCheckerOutputSchema",
    # Validation results
    "ValidationResult",
    # Pipeline
    "CodeGeneratorPipelineInputSchema",
    "CodeGeneratorPipelineOutputSchema",
]


# ---------------------------------------------------------------------------
# Intermediate data models
# ---------------------------------------------------------------------------


class VettedCode(BaseModel):
    """Code that passed all validators. Ready for execution."""

    code: str = Field(..., description="Complete self-contained Python source.")
    libraries: list[str] = Field(default_factory=list, description="Pip packages needed.")
    output_files: list[str] = Field(default_factory=list, description="Paths the code writes.")
    explanation: str = Field(default="", description="One-paragraph summary of what the code does.")


# ---------------------------------------------------------------------------
# Code Designer Agent
# ---------------------------------------------------------------------------


class CodeDesignerInputSchema(InputSchema):
    """Input for the Code Designer Agent.

    ``context`` is intentionally free-form — the caller decides what to
    provide (research question, dataset description, task specification,
    fine-tuning instructions, etc.).
    """

    context: str = Field(
        ...,
        description=(
            "Free-form context describing what code needs to be generated. "
            "May include any combination of: research questions, dataset "
            "descriptions, task specifications, experiment designs, etc."
        ),
    )


class CodeDesignerOutputSchema(OutputSchema):
    """Design document produced by the Code Designer Agent.

    The ``design_document`` is a comprehensive markdown spec that gives
    the code generator everything it needs to produce correct code on the
    first attempt.  ``libraries`` and ``output_files`` are extracted as
    structured fields so the pipeline can use them without parsing markdown.
    """

    __response_field__ = "design_document"

    design_document: str = Field(
        ...,
        description=(
            "Comprehensive markdown design document. Must include sections: "
            "GOAL & SUCCESS CRITERIA, APPROACH, WORKFLOW, CONSTRAINTS, "
            "INPUT/OUTPUT, LIBRARIES, and any relevant BEST PRACTICES "
            "or PLOT SPECIFICATIONS."
        ),
    )
    libraries: list[str] = Field(
        default_factory=list,
        description="Required Python libraries (from the allowed set).",
    )
    output_files: list[str] = Field(
        default_factory=list,
        description="All output file paths the code will write.",
    )
    success_criteria: list[str] = Field(
        default_factory=list,
        description=(
            "Concrete, verifiable success criteria from the GOAL & SUCCESS "
            "CRITERIA section. Each criterion must be checkable yes/no by "
            "reading the code output. Used by the intent checker downstream."
        ),
    )


# ---------------------------------------------------------------------------
# Code Generator Agent
# ---------------------------------------------------------------------------


class CodeGeneratorInputSchema(InputSchema):
    """Input for the Code Generator Agent."""

    design_document: str = Field(
        ..., description="Markdown design document from the Code Designer."
    )
    context: str = Field(
        ..., description="Original context passed to the designer."
    )
    correction_feedback: str = Field(
        default="",
        description=(
            "If non-empty, the previous code attempt was rejected by a validator. "
            "This field contains the failure reason. Fix the issues described."
        ),
    )


class CodeGeneratorOutputSchema(OutputSchema):
    """Generated analysis code plus metadata."""

    __response_field__ = "code"

    code: str = Field(..., description="Complete self-contained Python source.")
    libraries: list[str] = Field(
        default_factory=list, description="Pip packages needed."
    )
    output_files: list[str] = Field(
        default_factory=list, description="Paths the code writes."
    )
    explanation: str = Field(
        default="", description="One-paragraph summary of what the code does."
    )


# ---------------------------------------------------------------------------
# Intent Checker (LLM-as-judge)
# ---------------------------------------------------------------------------


class IntentCheckerInputSchema(InputSchema):
    """Input for the Intent Checker LLM-as-judge."""

    context: str = Field(..., description="Original context.")
    design_document: str = Field(..., description="Design document from the designer.")
    code: str = Field(..., description="Generated Python code to evaluate.")
    success_criteria: list[str] = Field(
        default_factory=list,
        description=(
            "Structured success criteria from the designer. Each criterion is "
            "a concrete, verifiable statement. The intent checker should verify "
            "the code addresses every criterion."
        ),
    )


class IntentCheckerOutputSchema(OutputSchema):
    """Verdict from the intent checker judge."""

    __response_field__ = "reasoning"

    matches_intent: bool = Field(
        ..., description="Does the code match the design document?"
    )
    is_benign: bool = Field(
        ..., description="Is the code safe and non-malicious?"
    )
    confidence: float = Field(
        ge=0.0, le=1.0, description="Confidence in this verdict."
    )
    reasoning: str = Field(
        default="", description="2-4 sentence justification."
    )
    suggested_fixes: list[str] = Field(
        default_factory=list,
        description="Concrete edits if the code should be regenerated.",
    )

    @property
    def approved(self) -> bool:
        """Single gate used by the pipeline orchestrator."""
        return self.matches_intent and self.is_benign and self.confidence >= 0.6


# ---------------------------------------------------------------------------
# Validation results (aggregated)
# ---------------------------------------------------------------------------


class ValidationResult(BaseModel):
    """Aggregated result from all three code validators."""

    passed: bool
    allowlist_passed: bool = True
    bandit_passed: bool = True
    intent_passed: bool = True
    failure_reasons: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Pipeline (top-level orchestrator)
# ---------------------------------------------------------------------------


class CodeGeneratorPipelineInputSchema(InputSchema):
    """Input for the full code-generation pipeline."""

    context: str = Field(
        ...,
        description=(
            "Free-form context for the code to be generated. "
            "The designer reads this and produces a design document; "
            "the generator implements it."
        ),
    )

    def to_designer_input(self) -> "CodeDesignerInputSchema":
        """Convert to the designer's input schema."""
        return CodeDesignerInputSchema(context=self.context)


class AttemptRecord(BaseModel):
    """Record of a single generator attempt within the pipeline."""

    attempt: int = Field(..., description="1-indexed attempt number.")
    stage_failed: str = Field(
        default="",
        description=(
            "Which stage caused the failure: 'generator', 'allowlist', "
            "'bandit', 'intent', or '' if this attempt succeeded."
        ),
    )
    failure_reason: str = Field(
        default="",
        description="Short description of why this attempt failed.",
    )
    passed: bool = Field(
        default=False, description="True if all validators passed on this attempt."
    )


class CodeGeneratorPipelineOutputSchema(OutputSchema):
    """Output from the code-generation pipeline."""

    __response_field__ = "report"

    vetted_code: VettedCode | None = Field(
        default=None,
        description="Validated code, or None if rejected.",
    )
    rejected: bool = Field(
        default=False, description="True if all retries exhausted."
    )
    rejection_reason: str = Field(
        default="", description="Why the code was rejected, if applicable."
    )
    report: str = Field(
        default="", description="Markdown summary of the pipeline run."
    )
    design_document: str = Field(
        default="",
        description="Designer output for traceability.",
    )
    attempt_history: list[AttemptRecord] = Field(
        default_factory=list,
        description=(
            "Ordered list of attempt records. Each entry records which "
            "stage failed (if any) and why. Useful for debugging and "
            "understanding pipeline convergence."
        ),
    )
    total_attempts: int = Field(
        default=0,
        description="Total number of generator attempts used.",
    )
