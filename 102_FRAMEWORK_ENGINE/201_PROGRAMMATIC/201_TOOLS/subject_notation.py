"""Shared, profile-explicit parsing for Subject notation.

This module recognizes only the two grammar profiles accepted for ordinary
Subject Tool operations.  It deliberately does not inspect a Project, infer a
profile from a Subject string, admit native graph endpoints, or translate
between profiles.
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True)
class GrammarPin:
    """One immutable source pin supporting a grammar profile."""

    atom_id: str
    version: int
    path: str
    sha256: str


@dataclass(frozen=True)
class SubjectProfile:
    """Immutable syntax and evidence for one explicit Subject profile."""

    name: str
    separators: tuple[str, ...]
    bearer_separator: str
    grammar_pins: tuple[GrammarPin, ...]


class SubjectNotationError(ValueError):
    """A bounded Subject-notation failure with a stable machine code."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


_LEGACY_PINS = (
    GrammarPin(
        "CA-R-1204",
        14,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/archive/CA-R-1204-CORE_META_MODEL--use-subject-path-slash-only-for-bearer-qualification@14.md",
        "f57d56dab2cff12ea38a94900a1f146e40ead39f0af9e26e3130e9867f290dda",
    ),
    GrammarPin(
        "CA-R-1321",
        12,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/archive/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression@12.md",
        "6baf3f4179591dcc89c458dcb6503a55f24b70f9f1bd93203f4b748a9bcb1b8c",
    ),
    GrammarPin(
        "CA-R-1324",
        10,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/archive/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators@10.md",
        "f38d4cc446b04cde6958f1fe011679ff95048bdfe30f360d11a7366a572bc0b1",
    ),
    GrammarPin(
        "CA-M-228",
        14,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/archive/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification@14.md",
        "f5a2152648b95c04af56c49118f43ac64ee46dd8183b23913cb64f335d6f26df",
    ),
    GrammarPin(
        "CA-E-383",
        13,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/archive/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions@13.md",
        "00c3e901fbd18cdb584387386f6b04cd43905f651c4369e16a97d20b469b3274",
    ),
)

_APPROVED_PINS = (
    GrammarPin(
        "CA-R-1931",
        1,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1931-CORE_META_MODEL--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md",
        "f11bc913a0f7b31abc746a86599eaeaa76db8be412568ef4c34f68c7d01525c8",
    ),
    GrammarPin(
        "CA-R-1321",
        13,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md",
        "e70433376c3c1fdda8189e90f31a2d9b7cfd740a2c23e7f9c91ad9a3de81be5f",
    ),
    GrammarPin(
        "CA-R-1324",
        11,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md",
        "b672d509190b0e87d5ff839721da9a5b05e52a572cc845450f2a7f1a96fa21f7",
    ),
    GrammarPin(
        "CA-M-228",
        15,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md",
        "f3febddbb9edf1776b7fd6d8680f46b69b735a7eb1a311bea844b0fbb74bcd70",
    ),
    GrammarPin(
        "CA-E-383",
        14,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md",
        "6e17caba7c5dac4bce187bdd79084bd49d316abc393ebb564280364fee39f143",
    ),
)

_PROFILES = MappingProxyType(
    {
        "legacy": SubjectProfile(
            name="legacy",
            separators=("/", ":"),
            bearer_separator="/",
            grammar_pins=_LEGACY_PINS,
        ),
        "approved": SubjectProfile(
            name="approved",
            separators=("/", ".", ":"),
            bearer_separator=".",
            grammar_pins=_APPROVED_PINS,
        ),
    }
)

_UNSUPPORTED_EXPRESSION_MARKERS = frozenset("\\[]{}(),&|?*")


def get_profile(name: str = "legacy") -> SubjectProfile:
    """Return one immutable named profile; no profile is inferred from text."""

    if not isinstance(name, str) or not name:
        raise SubjectNotationError("profile-invalid", "subject profile must be one non-empty string")
    try:
        return _PROFILES[name]
    except KeyError as error:
        raise SubjectNotationError("profile-unknown", f"unknown subject profile: {name}") from error


def parse_subject(value: str, *, subject_profile: str = "legacy") -> list[tuple[str, str | None]]:
    """Parse a Subject string into component and preceding-separator tuples.

    Components are whitespace-normalized at their boundaries only.  Internal
    whitespace remains literal.  The parser deliberately accepts no grammar
    beyond separators: it does not determine whether a component is an Atom,
    Property, allowed value, or admitted native endpoint.
    """

    profile = get_profile(subject_profile)
    if not isinstance(value, str):
        raise SubjectNotationError("subject-invalid", "subject must be text")
    if "@" in value:
        raise SubjectNotationError("subject-at-unsupported", "@ is not a Subject notation operator")
    if any(marker in value for marker in _UNSUPPORTED_EXPRESSION_MARKERS):
        raise SubjectNotationError(
            "subject-form-unsupported",
            "Subject selectors, conjunctions, wildcards, and escapes are unsupported",
        )

    value = value.strip()
    if not value:
        raise SubjectNotationError("subject-empty", "subject must contain one non-empty component")

    parsed: list[tuple[str, str | None]] = []
    component: list[str] = []
    preceding_separator: str | None = None
    for character in value:
        if character not in profile.separators:
            component.append(character)
            continue
        text = "".join(component).strip()
        if not text:
            raise SubjectNotationError("subject-malformed", "Subject separators require non-empty components")
        parsed.append((text, preceding_separator))
        component.clear()
        preceding_separator = character

    text = "".join(component).strip()
    if not text:
        raise SubjectNotationError("subject-malformed", "Subject separators require non-empty components")
    parsed.append((text, preceding_separator))
    return parsed


def profile_evidence(name: str = "legacy") -> dict[str, object]:
    """Return new JSON-compatible grammar evidence for the named profile."""

    profile = get_profile(name)
    return {
        "grammar_pins": [
            {
                "atom_id": pin.atom_id,
                "version": pin.version,
                "path": pin.path,
                "sha256": pin.sha256,
            }
            for pin in profile.grammar_pins
        ],
        "native_admission": "not_performed",
    }


__all__ = [
    "GrammarPin",
    "SubjectNotationError",
    "SubjectProfile",
    "get_profile",
    "parse_subject",
    "profile_evidence",
]
