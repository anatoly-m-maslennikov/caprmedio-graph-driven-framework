"""Shared, profile-explicit parsing for Subject notation.

This module recognizes only the two grammar profiles accepted for ordinary
Subject Tool operations.  It deliberately does not inspect a Project, infer a
profile from a Subject string, admit native graph endpoints, or translate
between profiles.
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping


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


@dataclass(frozen=True)
class InitialAtomSelector:
    """The syntax-only initial ``atom(...)`` component of an approved Subject."""

    literal: str
    selector: Mapping[str, str]
    entity_type_term: str = "Atom"


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
        14,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md",
        "d883f1bd53ac3ea83aeff2d3d1fdfb5498641a0e5f2db5e8e79d8dfd5c5a84df",
    ),
    GrammarPin(
        "CA-R-1324",
        12,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md",
        "33cbfee9844ba4dd895ae6745121fd5db5793a20aab27eb8b8d7b4591e7fb9a3",
    ),
    GrammarPin(
        "CA-M-228",
        16,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md",
        "0f398721d7d15aaf8e0b0f69a20b1b541e8d306839073c98eea4b80f9580b40d",
    ),
    GrammarPin(
        "CA-E-383",
        16,
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md",
        "a356617c341cd1d3c723e3e3ddbf9852c720781c8f22dd31f07cf33dfa4ec512",
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

_UNSUPPORTED_EXPRESSION_MARKERS = frozenset("\\[]{}&|?*")
_NON_SELECTOR_COMPONENT_MARKERS = frozenset('(),"')
_LEGACY_UNSUPPORTED_COMPONENT_MARKERS = frozenset("(),")
_UNSUPPORTED_SELECTOR_LITERAL_MARKERS = frozenset("\\[]{}&|?*@$")
_SELECTOR_KEYWORD = "atom"
_SELECTOR_ENTITY_TYPE_TERM = "Atom"


def get_profile(name: str = "legacy") -> SubjectProfile:
    """Return one immutable named profile; no profile is inferred from text."""

    if not isinstance(name, str) or not name:
        raise SubjectNotationError("profile-invalid", "subject profile must be one non-empty string")
    try:
        return _PROFILES[name]
    except KeyError as error:
        raise SubjectNotationError("profile-unknown", f"unknown subject profile: {name}") from error


def parse_initial_atom_selector(
    component: str,
    *,
    subject_profile: str = "legacy",
) -> InitialAtomSelector | None:
    """Return one exact approved initial selector without resolving any Atom.

    The result preserves its complete selector literal and exposes the selected
    owner's existing Entity-type Term, ``Atom``.  It performs syntax validation
    only; callers must not treat it as a Term, a new Entity kind, or native
    endpoint admission.
    """

    profile = get_profile(subject_profile)
    if not isinstance(component, str):
        raise SubjectNotationError("subject-invalid", "Subject component must be text")
    literal = component.strip()
    if "@" in literal:
        raise SubjectNotationError("subject-at-unsupported", "@ is not a Subject notation operator")
    if profile.name != "approved":
        if _looks_like_selector(literal) or literal == _SELECTOR_KEYWORD:
            raise SubjectNotationError(
                "subject-form-unsupported",
                "Subject selectors are unsupported in the legacy profile",
            )
        return None
    if literal == _SELECTOR_KEYWORD:
        raise SubjectNotationError("subject-selector-invalid", "bare atom is not a Subject selector")
    if literal.startswith(f"{_SELECTOR_KEYWORD}("):
        selector, end = _parse_selector_literal(literal)
        if end != len(literal):
            raise SubjectNotationError("subject-selector-invalid", "selector must be one complete component")
        return InitialAtomSelector(
            literal=literal,
            selector=MappingProxyType(selector),
            entity_type_term=_SELECTOR_ENTITY_TYPE_TERM,
        )
    if _looks_like_selector(literal):
        raise SubjectNotationError(
            "subject-selector-invalid",
            "Subject selector keyword must be exact lowercase atom",
        )
    return None


def parse_subject(value: str, *, subject_profile: str = "legacy") -> list[tuple[str, str | None]]:
    """Parse a Subject string into component and preceding-separator tuples.

    Components are whitespace-normalized at their boundaries only.  Internal
    whitespace remains literal.  In the approved profile alone, the initial
    component can be one exact lowercase ``atom(...)`` selector.  The parser
    deliberately does not resolve that selector, determine a Subject target,
    or admit a native endpoint.
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

    if profile.name == "legacy":
        if any(marker in value for marker in _LEGACY_UNSUPPORTED_COMPONENT_MARKERS):
            raise SubjectNotationError(
                "subject-form-unsupported",
                "Subject selectors, conjunctions, wildcards, and escapes are unsupported",
            )
        return _split_subject_components(value, profile)

    selector, position = _initial_selector_prefix(value)
    if selector is None:
        if _looks_like_selector(value):
            raise SubjectNotationError(
                "subject-selector-invalid",
                "Subject selector keyword must be exact lowercase atom",
            )
        return _split_subject_components(value, profile)

    parsed: list[tuple[str, str | None]] = [(selector.literal, None)]
    if position == len(value):
        return parsed
    separator = value[position]
    if separator not in profile.separators:
        raise SubjectNotationError("subject-selector-invalid", "selector must be followed by a Subject separator")
    parsed.extend(_split_subject_components(value[position + 1 :], profile, preceding_separator=separator))
    return parsed


def _split_subject_components(
    value: str,
    profile: SubjectProfile,
    *,
    preceding_separator: str | None = None,
) -> list[tuple[str, str | None]]:
    """Split ordinary Subject components after selector handling, if any."""

    parsed: list[tuple[str, str | None]] = []
    component: list[str] = []
    for character in value:
        if character not in profile.separators:
            component.append(character)
            continue
        parsed.append((_ordinary_component(component, profile), preceding_separator))
        component.clear()
        preceding_separator = character

    parsed.append((_ordinary_component(component, profile), preceding_separator))
    return parsed


def _ordinary_component(component: list[str], profile: SubjectProfile) -> str:
    text = "".join(component).strip()
    if not text:
        raise SubjectNotationError("subject-malformed", "Subject separators require non-empty components")
    if profile.name == "approved" and (_looks_like_selector(text) or text == _SELECTOR_KEYWORD):
        raise SubjectNotationError("subject-selector-position", "atom selector may occur only as the initial component")
    if profile.name == "approved" and any(marker in text for marker in _NON_SELECTOR_COMPONENT_MARKERS):
        raise SubjectNotationError("subject-form-unsupported", "selector punctuation is unsupported outside atom(...)")
    return text


def _initial_selector_prefix(value: str) -> tuple[InitialAtomSelector | None, int]:
    """Parse an approved selector at byte zero and return its separator index."""

    if value == _SELECTOR_KEYWORD:
        raise SubjectNotationError("subject-selector-invalid", "bare atom is not a Subject selector")
    if not value.startswith(f"{_SELECTOR_KEYWORD}("):
        return None, 0
    selector, end = _parse_selector_literal(value)
    literal = value[:end]
    position = end
    while position < len(value) and value[position].isspace():
        position += 1
    if position < len(value) and value[position] not in get_profile("approved").separators:
        raise SubjectNotationError("subject-selector-invalid", "selector must be followed by a Subject separator")
    return (
        InitialAtomSelector(
            literal=literal,
            selector=MappingProxyType(selector),
            entity_type_term=_SELECTOR_ENTITY_TYPE_TERM,
        ),
        position,
    )


def _parse_selector_literal(value: str) -> tuple[dict[str, str], int]:
    """Parse exactly one lowercase selector and return its map plus end index."""

    position = len(_SELECTOR_KEYWORD) + 1
    selector: dict[str, str] = {}
    while True:
        position = _skip_whitespace(value, position)
        key_start = position
        while position < len(value) and (value[position].isalnum() or value[position] == "_"):
            position += 1
        key = value[key_start:position]
        if not key:
            raise SubjectNotationError("subject-selector-invalid", "selector requires a named key")
        position = _skip_whitespace(value, position)
        if position >= len(value) or value[position] != "=":
            raise SubjectNotationError("subject-selector-invalid", "selector key requires one quoted value")
        position = _skip_whitespace(value, position + 1)
        if position >= len(value) or value[position] != '"':
            raise SubjectNotationError("subject-selector-invalid", "selector values must be double-quoted")
        position += 1
        literal_start = position
        while position < len(value) and value[position] != '"':
            if value[position] == "\\":
                raise SubjectNotationError("subject-selector-invalid", "selector escaping is unsupported")
            position += 1
        if position >= len(value):
            raise SubjectNotationError("subject-selector-invalid", "selector value is unterminated")
        literal = value[literal_start:position]
        if not literal.strip() or any(ord(character) < 32 or ord(character) == 127 for character in literal):
            raise SubjectNotationError("subject-selector-invalid", "selector values must be non-empty printable literals")
        if any(marker in literal for marker in _UNSUPPORTED_SELECTOR_LITERAL_MARKERS):
            raise SubjectNotationError(
                "subject-selector-invalid",
                "selector literals do not support escaping, wildcards, or expansion",
            )
        if key in selector:
            raise SubjectNotationError("subject-selector-invalid", "selector keys must not repeat")
        selector[key] = literal
        position = _skip_whitespace(value, position + 1)
        if position >= len(value):
            raise SubjectNotationError("subject-selector-invalid", "selector is unterminated")
        if value[position] == ")":
            position += 1
            break
        if value[position] != ",":
            raise SubjectNotationError("subject-selector-invalid", "selector entries require commas")
        position += 1

    keys = tuple(selector)
    if keys == ("atom_id",) or keys == ("content_role",) or keys == ("content_role", "type"):
        return selector, position
    raise SubjectNotationError(
        "subject-selector-invalid",
        "selector must use atom_id or content_role followed by optional type",
    )


def _skip_whitespace(value: str, position: int) -> int:
    while position < len(value) and value[position].isspace():
        position += 1
    return position


def _looks_like_selector(value: str) -> bool:
    return value[:4].casefold() == _SELECTOR_KEYWORD and (
        value == _SELECTOR_KEYWORD or (len(value) > 4 and value[4] == "(")
    )


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
    "InitialAtomSelector",
    "SubjectNotationError",
    "SubjectProfile",
    "get_profile",
    "parse_initial_atom_selector",
    "parse_subject",
    "profile_evidence",
]
