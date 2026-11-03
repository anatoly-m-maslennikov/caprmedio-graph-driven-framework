"""Shared, profile-explicit parsing for Subject notation.

This module recognizes only the two grammar profiles accepted for ordinary
Subject Tool operations.  It deliberately does not inspect a Project, infer a
profile from a Subject string, admit native graph endpoints, or translate
between profiles.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from types import MappingProxyType
from typing import Mapping, Sequence
import re


@dataclass(frozen=True)
class GrammarSource:
    """One stable current grammar source selector, without observed evidence."""

    atom_id: str
    path: str


@dataclass(frozen=True)
class GrammarPin:
    """One immutable source pin supporting a grammar profile."""

    atom_id: str
    version: int
    path: str
    sha256: str


@dataclass(frozen=True)
class SubjectProfile:
    """Immutable syntax and declared grammar sources for one explicit profile."""

    name: str
    separators: tuple[str, ...]
    bearer_separator: str
    grammar_pins: tuple[GrammarSource | GrammarPin, ...]


@dataclass(frozen=True)
class Span:
    """Half-open character offsets in the supplied Subject text."""

    start: int
    end: int


@dataclass(frozen=True)
class InitialAtomSelector:
    """The syntax-only initial ``atom(...)`` component of an approved Subject."""

    literal: str
    selector: Mapping[str, str]
    entity_type_term: str = "Atom"
    span: Span | None = None


@dataclass(frozen=True)
class Name:
    value: str
    span: Span


@dataclass(frozen=True)
class ValueLiteral:
    value: str
    span: Span


@dataclass(frozen=True)
class FormatReference:
    value: str
    span: Span


@dataclass(frozen=True)
class Cardinality:
    minimum: int
    maximum: int | None
    span: Span


@dataclass(frozen=True)
class Qualification:
    relative_path: Path
    span: Span


@dataclass(frozen=True)
class DeclaredReference:
    entity: Name | Path
    span: Span


@dataclass(frozen=True)
class SelectionGroup:
    members: tuple[Path | RelationChain, ...]
    span: Span


@dataclass(frozen=True)
class SelectionSuffix:
    value: str
    span: Span


@dataclass(frozen=True)
class PathStep:
    operator: str
    operand: Name | ValueLiteral | Qualification | DeclaredReference | Path | RelationChain | SelectionGroup | SelectionSuffix
    span: Span


@dataclass(frozen=True)
class Path:
    head: Name | InitialAtomSelector | DeclaredReference | Path | RelationChain | SelectionGroup
    steps: tuple[PathStep, ...]
    value_format: FormatReference | None
    value_cardinality: Cardinality | None
    span: Span


@dataclass(frozen=True)
class RelationLink:
    operator: str
    relation_type: Name | None
    forward_cardinality: Cardinality | None
    reverse_cardinality: Cardinality | None
    span: Span


@dataclass(frozen=True)
class RelationChain:
    endpoints: tuple[Path, ...]
    links: tuple[RelationLink, ...]
    span: Span


@dataclass(frozen=True)
class ParsedSubject:
    source: str
    expression: Path | RelationChain
    span: Span


def namespace_local_expression(
    expression: Path | RelationChain,
) -> Path | RelationChain | None:
    """Return the local expression below an explicit CAPRMEDIO namespace."""

    if not isinstance(expression, RelationChain) or len(expression.endpoints) < 2:
        return None
    root, namespace = expression.endpoints[:2]
    if (isinstance(root.head, Name) and root.head.value in {"CAPRMEDIO_MODEL", "CAPRMEDIO_STRUCTURE"}
            and not root.steps and expression.links[0].operator == "<+"
            and expression.links[0].relation_type is None):
        endpoints, links = expression.endpoints[1:], expression.links[1:]
        return endpoints[0] if len(endpoints) == 1 else replace(expression, endpoints=endpoints, links=links)
    if (
        not isinstance(root.head, Name) or root.head.value != "CAPRMEDIO"
        or root.steps
        or not isinstance(namespace.head, Name) or namespace.head.value not in {"MODEL", "STRUCTURE"}
        or namespace.steps
        or any(link.operator != "<+" or link.relation_type is not None
               for link in expression.links[:min(2, len(expression.links))])
    ):
        return None
    if len(expression.endpoints) == 2:
        return namespace
    endpoints, links = expression.endpoints[2:], expression.links[2:]
    if len(endpoints) == 1:
        return endpoints[0]
    return replace(expression, endpoints=endpoints, links=links)


class SubjectNotationError(ValueError):
    """A bounded Subject-notation failure with a stable machine code."""

    def __init__(self, code: str, message: str, span: Span | None = None) -> None:
        self.code = code
        self.span = span
        super().__init__(message)


# Legacy syntax deliberately names archived history, not current rule authority.
_LEGACY_PINS = (
    GrammarPin(
        "CA-R-1204",
        14,
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive/CA-R-1204-CORE_META_MODEL--use-subject-path-slash-only-for-bearer-qualification@14.md",
        "f57d56dab2cff12ea38a94900a1f146e40ead39f0af9e26e3130e9867f290dda",
    ),
    GrammarPin(
        "CA-R-1321",
        12,
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression@12.md",
        "6baf3f4179591dcc89c458dcb6503a55f24b70f9f1bd93203f4b748a9bcb1b8c",
    ),
    GrammarPin(
        "CA-R-1324",
        10,
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators@10.md",
        "f38d4cc446b04cde6958f1fe011679ff95048bdfe30f360d11a7366a572bc0b1",
    ),
    GrammarPin(
        "CA-M-228",
        14,
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/archive/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification@14.md",
        "f5a2152648b95c04af56c49118f43ac64ee46dd8183b23913cb64f335d6f26df",
    ),
    GrammarPin(
        "CA-E-383",
        13,
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/archive/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions@13.md",
        "00c3e901fbd18cdb584387386f6b04cd43905f651c4369e16a97d20b469b3274",
    ),
)

_APPROVED_SOURCES = (
    GrammarSource(
        "CA-R-1931",
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1931-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md",
    ),
    GrammarSource(
        "CA-R-1321",
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-RULE--define-subject-expression.md",
    ),
    GrammarSource(
        "CA-R-1324",
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-RULE--reserve-subject-expression-separators.md",
    ),
    GrammarSource(
        "CA-M-228",
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification.md",
    ),
    GrammarSource(
        "CA-E-383",
        ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVAL_POLICY--reject-invalid-subject-expressions.md",
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
            separators=("//", "/", ".", ":", "+>", "<+", ">|", "|<", "<-->", "<((", "(("),
            bearer_separator=".",
            grammar_pins=_APPROVED_SOURCES,
        ),
    }
)

_UNSUPPORTED_EXPRESSION_MARKERS = frozenset("\\[]{}&|?*")
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
    """Parse archived legacy syntax into its unchanged flat tuple contract.

    Approved expressions require the typed API because tuples cannot preserve
    grouping, qualification binding, or Relation cardinality slots.
    """

    profile = get_profile(subject_profile)
    if profile.name != "legacy":
        raise SubjectNotationError(
            "subject-flat-adapter-unsupported",
            "approved Subjects require parse_subject_expression and its typed expression",
        )
    if not isinstance(value, str):
        raise SubjectNotationError("subject-invalid", "subject must be text")
    if "@" in value:
        raise SubjectNotationError("subject-at-unsupported", "@ is not a legacy Subject notation operator")
    if any(marker in value for marker in _UNSUPPORTED_EXPRESSION_MARKERS | _LEGACY_UNSUPPORTED_COMPONENT_MARKERS):
        raise SubjectNotationError("subject-form-unsupported", "unsupported legacy Subject form")
    value = value.strip()
    if not value:
        raise SubjectNotationError("subject-empty", "subject must contain one non-empty component")
    return _split_subject_components(value, profile)


def _split_subject_components(
    value: str,
    profile: SubjectProfile,
    *,
    preceding_separator: str | None = None,
) -> list[tuple[str, str | None]]:
    """Split ordinary Subject components after selector handling, if any."""

    parsed: list[tuple[str, str | None]] = []
    component: list[str] = []
    position = 0
    while position < len(value):
        separator = _separator_at(value, position, profile)
        if separator is None:
            component.append(value[position])
            position += 1
            continue
        parsed.append((_ordinary_component(component, profile), preceding_separator))
        component.clear()
        preceding_separator = separator
        position += len(separator)

    parsed.append((_ordinary_component(component, profile), preceding_separator))
    return parsed


def _separator_at(value: str, position: int, profile: SubjectProfile) -> str | None:
    """Return the longest registered separator beginning at one position."""

    return next((separator for separator in profile.separators if value.startswith(separator, position)), None)


def _ordinary_component(component: list[str], profile: SubjectProfile) -> str:
    text = "".join(component).strip()
    if not text:
        raise SubjectNotationError("subject-malformed", "Subject separators require non-empty components")
    return text


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
    if keys == ("content_role",) or keys == ("content_role", "type"):
        return selector, position
    raise SubjectNotationError(
        "subject-selector-invalid",
        "selector must use content_role followed by optional type",
    )


def _skip_whitespace(value: str, position: int) -> int:
    while position < len(value) and value[position].isspace():
        position += 1
    return position


def _looks_like_selector(value: str) -> bool:
    return value[:4].casefold() == _SELECTOR_KEYWORD and (
        value == _SELECTOR_KEYWORD or (len(value) > 4 and value[4] == "(")
    )


# Every reserved character is either syntax or explicitly escaped in a name.
_RESERVED = frozenset('\\/.:@()[]{}+<>|*&?,="\'')
_RELATION_OPERATORS = ("+>", "<+", ">|", "|<", "<-->", "<((", "((")
# ``:=`` keeps the authored qualification marker.  It has the same endpoint
# shape as ``:`` in a Subject address, but callers can retain the distinction
# between an allowed value and the condition used to select the address.
_PATH_OPERATORS = ("//", "/", ".", ":=", ":")


class _ExpressionParser:
    def __init__(self, source: str) -> None:
        self.source = source
        self.position = 0
        self.depth = 0

    def whitespace(self) -> None:
        self.position = _skip_whitespace(self.source, self.position)

    def at(self, token: str) -> bool:
        return self.source.startswith(token, self.position)

    def fail(self, message: str, start: int | None = None, code: str = "subject-malformed") -> None:
        position = self.position if start is None else start
        raise SubjectNotationError(code, message, Span(position, min(len(self.source), position + 1)))

    def name(self, node_type: type = Name) -> Name | ValueLiteral | FormatReference:
        self.whitespace()
        start = self.position
        characters: list[str] = []
        literal_length = 0
        last_end = start
        while self.position < len(self.source):
            character = self.source[self.position]
            escaped = character == "\\"
            if escaped:
                self.position += 1
                if self.position == len(self.source):
                    self.fail("a name escape requires a following character", self.position - 1)
                character = self.source[self.position]
            elif character in _RESERVED:
                break
            if ord(character) < 32 or ord(character) == 127:
                self.fail("names require printable characters")
            characters.append(character)
            self.position += 1
            if escaped or not character.isspace():
                literal_length = len(characters)
                last_end = self.position
        value = "".join(characters[:literal_length])
        if not value:
            self.fail("expected a non-empty name", start)
        return node_type(value, Span(start, last_end))

    def value_literal(self) -> ValueLiteral:
        """Parse an allowed value, including its bounded quoted literal form."""

        self.whitespace()
        if not self.at('"'):
            return self.name(ValueLiteral)
        start = self.position
        self.position += 1
        literal_start = self.position
        while self.position < len(self.source) and self.source[self.position] != '"':
            character = self.source[self.position]
            if character == "\\" or ord(character) < 32 or ord(character) == 127:
                self.fail("quoted allowed values require printable unescaped characters", self.position)
            self.position += 1
        if self.position == len(self.source):
            self.fail("quoted allowed value is unterminated", start)
        value = self.source[literal_start:self.position]
        if not value.strip():
            self.fail("quoted allowed value must be non-empty", start)
        self.position += 1
        return ValueLiteral(value, Span(start, self.position))

    def cardinality(self) -> Cardinality:
        self.whitespace()
        start = self.position
        end = self.source.find("}", start + 1)
        if end < 0:
            self.fail("unterminated cardinality", start)
        literal = self.source[start + 1:end]
        match = re.fullmatch(r"(0|[1-9][0-9]*)(?:(\+)|\.\.(0|[1-9][0-9]*))?", literal)
        if match is None:
            self.fail("cardinality must be {n}, {n+}, or {n..m}", start)
        minimum = int(match[1])
        maximum = None if match[2] else int(match[3]) if match[3] else minimum
        if maximum is not None and maximum < minimum:
            self.fail("cardinality minimum exceeds its maximum", start)
        self.position = end + 1
        return Cardinality(minimum, maximum, Span(start, self.position))

    def reference(self) -> DeclaredReference:
        start = self.position
        self.position += 1
        self.whitespace()
        grouped = self.at("(")
        if grouped:
            self.position += 1
            entity = self.path()
        else:
            entity = self.name()
        self.whitespace()
        if grouped:
            if not self.at(")"):
                self.fail("declared reference requires one complete Entity path")
            self.position += 1
        return DeclaredReference(entity, Span(start, self.position))

    def head(self, *, initial: bool) -> Name | InitialAtomSelector | DeclaredReference | Path | RelationChain | SelectionGroup:
        self.whitespace()
        start = self.position
        if self.at("@"):
            return self.reference()
        if self.at("("):
            if self.depth >= 64:
                self.fail("Subject grouping exceeds the depth limit", start, "subject-limit")
            self.position += 1
            self.depth += 1
            members = [self.expression(initial=False)]
            self.whitespace()
            while self.at(","):
                self.position += 1
                members.append(self.expression(initial=False))
                self.whitespace()
            self.depth -= 1
            self.whitespace()
            if not self.at(")"):
                self.fail("unterminated logical group", start)
            self.position += 1
            return members[0] if len(members) == 1 else SelectionGroup(tuple(members), Span(start, self.position))
        if self.at("atom("):
            if not initial:
                self.fail("atom selector may occur only as the initial component", start, "subject-selector-position")
            try:
                selector, end = _parse_selector_literal(self.source[start:])
            except SubjectNotationError as error:
                if error.span is None:
                    error.span = Span(start, len(self.source))
                raise
            self.position = start + end
            return InitialAtomSelector(self.source[start:self.position], MappingProxyType(selector), span=Span(start, self.position))
        if self.source[start:start + 5].casefold() == "atom(":
            self.fail("Subject selector keyword must be exact lowercase atom", start, "subject-selector-invalid")
        name = self.name()
        if initial and name.value == _SELECTOR_KEYWORD:
            self.fail("bare atom is not a Subject selector", start, "subject-selector-invalid")
        return name

    def path(self, *, initial: bool = False, relative: bool = False) -> Path:
        self.whitespace()
        start = self.position
        if relative:
            if not self.at("."):
                self.fail("qualification requires a relative Property path")
            self.position += 1
        head = self.head(initial=initial and not relative)
        steps: list[PathStep] = []
        while True:
            self.whitespace()
            step_start = self.position
            operator = next((token for token in _PATH_OPERATORS if self.at(token)), None)
            if operator is None:
                break
            self.position += len(operator)
            self.whitespace()
            if operator == "//" and (self.position == len(self.source) or self.at(")") or self.at(",")):
                operand = SelectionSuffix("", Span(self.position, self.position))
            elif operator == "." and self.at("**"):
                operand = SelectionSuffix("**", Span(self.position, self.position + 2))
                self.position += 2
            elif operator == "/" and self.at("(") and not self.at("(("):
                after_open = _skip_whitespace(self.source, self.position + 1)
                if self.source.startswith(".", after_open):
                    qualification_start = self.position
                    self.position += 1
                    operand_path = self.path(relative=True)
                    if not isinstance(operand_path.head, Name) or not any(
                        step.operator in {":", ":="} for step in operand_path.steps
                    ):
                        self.fail("qualification requires a relative Property and its allowed value", qualification_start)
                    self.whitespace()
                    if not self.at(")"):
                        self.fail("unterminated relative qualification", qualification_start)
                    self.position += 1
                    operand = Qualification(operand_path, Span(qualification_start, self.position))
                else:
                    operand = self.head(initial=False)
            elif operator in {":", ":="}:
                operand = self.value_literal()
            else:
                operand = self.head(initial=False)
            steps.append(PathStep(operator, operand, Span(step_start, self.position)))
        value_format = None
        value_cardinality = None
        if self.at("["):
            format_start = self.position
            self.position += 1
            value_format = self.name(FormatReference)
            self.whitespace()
            if not self.at("]"):
                self.fail("unterminated value Format", format_start)
            self.position += 1
            self.whitespace()
        if self.at("{"):
            count_start = self.position
            count = self.cardinality()
            self.whitespace()
            if any(self.at(operator) for operator in _RELATION_OPERATORS):
                self.position = count_start
            else:
                value_cardinality = count
        end = self.position
        while end > start and self.source[end - 1].isspace():
            end -= 1
        return Path(head, tuple(steps), value_format, value_cardinality, Span(start, end))

    def expression(self, *, initial: bool = False) -> Path | RelationChain:
        first = self.path(initial=initial)
        endpoints = [first]
        links: list[RelationLink] = []
        while True:
            self.whitespace()
            start = self.position
            forward = self.cardinality() if self.at("{") else None
            self.whitespace()
            operator = next((token for token in _RELATION_OPERATORS if self.at(token)), None)
            if operator is None:
                if forward is not None:
                    self.fail("directional cardinality requires a Relation operator", start)
                break
            self.position += len(operator)
            relation_type = None
            if operator in {"((", "<(("}:
                relation_type = self.name()
                self.whitespace()
                if not self.at("))"):
                    self.fail("named Relation requires matching double parentheses", start)
                self.position += 2
            self.whitespace()
            reverse = self.cardinality() if self.at("{") else None
            self.whitespace()
            link_end = self.position
            endpoint = self.path()
            links.append(RelationLink(operator, relation_type, forward, reverse, Span(start, link_end)))
            endpoints.append(endpoint)
        if not links:
            return first
        return RelationChain(tuple(endpoints), tuple(links), Span(first.span.start, endpoints[-1].span.end))


def parse_subject_expression(text: str, *, subject_profile: str = "approved") -> ParsedSubject:
    """Parse syntax without resolving names, declarations, or native graph facts."""

    profile = get_profile(subject_profile)
    if not isinstance(text, str):
        raise SubjectNotationError("subject-invalid", "subject must be text")
    if profile.name == "legacy":
        components = parse_subject(text, subject_profile="legacy")
        position = 0
        nodes = []
        for value, operator in components:
            start = text.find(value, position)
            end = start + len(value)
            node = Name(value, Span(start, end))
            nodes.append((node, operator))
            position = end
        head = nodes[0][0]
        expression = Path(head, tuple(PathStep(operator, node, node.span) for node, operator in nodes[1:]), None, None, Span(head.span.start, nodes[-1][0].span.end))
        return ParsedSubject(text, expression, expression.span)
    if len(text) > 16384:
        raise SubjectNotationError("subject-limit", "Subject exceeds the length limit", Span(0, len(text)))
    parser = _ExpressionParser(text)
    parser.whitespace()
    if parser.position == len(text):
        raise SubjectNotationError("subject-empty", "subject must contain one non-empty component", Span(0, len(text)))
    expression = parser.expression(initial=True)
    parser.whitespace()
    if parser.position != len(text):
        parser.fail("unexpected reserved character or trailing expression")
    return ParsedSubject(text, expression, expression.span)


def _escaped_name(value: str) -> str:
    return "".join(
        "\\" + character if character in _RESERVED or (character.isspace() and index in (0, len(value) - 1)) else character
        for index, character in enumerate(value)
    )


def render_subject(parsed: ParsedSubject | Path | RelationChain) -> str:
    """Render a canonical, idempotent Subject while preserving written direction."""

    if isinstance(parsed, ParsedSubject):
        return render_subject(parsed.expression)
    if isinstance(parsed, RelationChain):
        result = render_subject(parsed.endpoints[0])
        for link, endpoint in zip(parsed.links, parsed.endpoints[1:], strict=True):
            operator = (
                ("<((" if link.operator == "<((" else "((")
                + _escaped_name(link.relation_type.value) + "))"
                if link.relation_type else link.operator
            )
            result += " " + _render_cardinality(link.forward_cardinality) + operator + _render_cardinality(link.reverse_cardinality) + " " + render_subject(endpoint)
        return result
    head = parsed.head
    if isinstance(head, (Path, RelationChain)):
        result = "(" + render_subject(head) + ")"
    else:
        result = _render_operand(head)
    for step in parsed.steps:
        result += step.operator + _render_operand(step.operand)
    if parsed.value_format is not None:
        result += "[" + _escaped_name(parsed.value_format.value) + "]"
    return result + _render_cardinality(parsed.value_cardinality)


def _render_operand(node: Name | ValueLiteral | InitialAtomSelector | Qualification | DeclaredReference | Path | RelationChain | SelectionGroup | SelectionSuffix) -> str:
    if isinstance(node, SelectionGroup):
        return "(" + ",".join(render_subject(member) for member in node.members) + ")"
    if isinstance(node, SelectionSuffix):
        return node.value
    if isinstance(node, InitialAtomSelector):
        return "atom(" + ",".join(key + '="' + value + '"' for key, value in node.selector.items()) + ")"
    if isinstance(node, Qualification):
        return "(." + render_subject(node.relative_path) + ")"
    if isinstance(node, DeclaredReference):
        if isinstance(node.entity, Path):
            return "@(" + render_subject(node.entity) + ")"
        return "@" + _escaped_name(node.entity.value)
    if isinstance(node, (Path, RelationChain)):
        return "(" + render_subject(node) + ")"
    if isinstance(node, ValueLiteral) and '"' not in node.value and "\\" not in node.value and any(
        character in _RESERVED for character in node.value
    ):
        return '"' + node.value + '"'
    return _escaped_name(node.value)


def _render_cardinality(cardinality: Cardinality | None) -> str:
    if cardinality is None:
        return ""
    minimum, maximum = cardinality.minimum, cardinality.maximum
    value = str(minimum) + ("+" if maximum is None else "" if minimum == maximum else ".." + str(maximum))
    return "{" + value + "}"


def profile_evidence(
    name: str = "legacy", *, grammar_pins: Sequence[GrammarPin] | None = None,
) -> dict[str, object]:
    """Project explicit current observations or the declared legacy history."""

    profile = get_profile(name)
    pins = tuple(grammar_pins) if grammar_pins is not None else profile.grammar_pins
    if any(not isinstance(pin, GrammarPin) for pin in pins):
        raise SubjectNotationError("profile-evidence-unbound", "Current grammar observations are required")
    if len(pins) != len(profile.grammar_pins) or any(
        pin.atom_id != source.atom_id
        or (isinstance(source, GrammarPin) and pin.path != source.path)
        for pin, source in zip(pins, profile.grammar_pins, strict=True)
    ):
        raise SubjectNotationError("profile-evidence-invalid", "Grammar observations must match the selected sources")
    rows = []
    for pin in pins:
        if not isinstance(pin, GrammarPin) or type(pin.version) is not int or pin.version < 1 or not isinstance(pin.sha256, str) or re.fullmatch(r"[0-9a-f]{64}", pin.sha256) is None:
            raise SubjectNotationError("profile-evidence-invalid", "Grammar observations require a Version and SHA-256")
        rows.append({"atom_id": pin.atom_id, "version": pin.version, "path": pin.path, "sha256": pin.sha256})
    return {
        "grammar_pins": rows,
        "native_admission": "not_performed",
    }


__all__ = [
    "Span", "Name", "ValueLiteral", "FormatReference", "Cardinality",
    "Qualification", "DeclaredReference", "SelectionGroup", "SelectionSuffix", "PathStep", "Path",
    "RelationLink", "RelationChain", "ParsedSubject",
    "parse_subject_expression", "render_subject",
    "GrammarSource",
    "GrammarPin",
    "InitialAtomSelector",
    "SubjectNotationError",
    "SubjectProfile",
    "get_profile",
    "parse_initial_atom_selector",
    "parse_subject",
    "profile_evidence",
]
