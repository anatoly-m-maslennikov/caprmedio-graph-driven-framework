"""Extract a deliberately small, non-evaluating CFEL constraint inventory.

This is a projection aid, not a CFEL parser or validator. Every expression
outside the few shape-stable forms below remains visible as an unsupported
diagnostic rather than being guessed or silently discarded.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import subject_notation as notation

Record = dict[str, Any]
_FENCE_LINE = re.compile(r"^[ \t]*(?P<marker>`{3,}|~{3,})(?P<label>[^\r\n]*)\r?$")
_COUNT = r"(?P<minimum>0|[1-9][0-9]*)(?P<tail>\+|\.\.(?P<maximum>0|[1-9][0-9]*))?"
_PROPERTY = re.compile(
    rf"^(?P<property>.+?)(?P<descendants>\.\*\*|\.\*)?"
    rf"(?:\[(?P<name_format>[^\]]*)\])?"
    rf"\{{:{_COUNT}\}}"
    rf"(?:\s*:\s*(?:\[(?P<value_format>[^\]]*)\])?\{{:(?P<value_minimum>0|[1-9][0-9]*)(?P<value_tail>\+|\.\.(?P<value_maximum>0|[1-9][0-9]*))?\}})?$"
)
_PROPERTY_VALUE = re.compile(
    rf"^(?P<property>.+?)(?P<descendants>\.\*\*|\.\*)?\s*:\s*(?:\[(?P<value_format>[^\]]*)\])?"
    rf"(?:\{{:{_COUNT}\}})?$"
)
_NAMED_PROPERTY = re.compile(rf"^(?P<property>.+?)(?:\{{:{_COUNT}\}})?\s*:$")
_MEMBERSHIP_QUALIFIER = re.compile(r"/\(\.[A-Za-z][A-Za-z0-9_. -]*\s+in\s+[A-Za-z][A-Za-z0-9_. -]*\)(?=\.|$)")
_RELATION = re.compile(
    rf"^(?P<source>.+?)\s*(?:\{{:(?P<forward_minimum>0|[1-9][0-9]*)(?P<forward_tail>\+|\.\.(?P<forward_maximum>0|[1-9][0-9]*))?\}}\s*)?"
    rf"(?:<\(\((?P<reverse_relation>[^()]+)\)\)|\(\((?P<relation>[^()]+)\)\)|(?P<relation_notation>\+>|<\+))\s*"
    rf"(?:\{{:(?P<reverse_minimum>0|[1-9][0-9]*)(?P<reverse_tail>\+|\.\.(?P<reverse_maximum>0|[1-9][0-9]*))?\}}\s*)?"
    rf"(?P<target>.+)$"
)
_RELATION_WITHOUT_TARGET = re.compile(
    rf"^(?P<source>.+?)\s*\{{:(?P<forward_minimum>0|[1-9][0-9]*)(?P<forward_tail>\+|\.\.(?P<forward_maximum>0|[1-9][0-9]*))?\}}\s*"
    rf"(?:\(\((?P<relation>[^()]+)\)\)|(?P<relation_notation>\+>|<\+)|(?P<bare_relation>[A-Z][A-Z0-9_]*))$"
)
_FORWARD_CLASSIFICATION = re.compile(
    r"^(?P<subject>.+?)\s*>\|\s*(?P<axis>.+?)\s*(?P<operator>==|=)\s*(?P<value>.+)$"
)
_REVERSE_CLASSIFICATION = re.compile(
    r"^(?P<axis>.+?)\s*\|<\s*(?P<subject>.+?)\s*(?P<operator>==|=)\s*(?P<value>.+)$"
)
_FORWARD_GROUPED_CLASSIFICATION = re.compile(
    r"^(?P<subject>.+?)\s*>\|\s*\(\s*(?P<axis>.+?)\s*(?P<operator>==|=)\s*(?P<value>.+?)\s*\)$"
)
_REVERSE_GROUPED_CLASSIFICATION = re.compile(
    r"^\(\s*(?P<axis>.+?)\s*(?P<operator>==|=)\s*(?P<value>.+?)\s*\)\s*\|<\s*(?P<subject>.+)$"
)
_ALLOWED_LITERAL = re.compile(r"^(?P<property>.+?)\s*:\s*(?P<literal>[^\[\]{}]+)$")
_QUALIFIED_ALLOWED_LITERAL = re.compile(r"^(?P<property>.+\).+?)\s*:\s*(?P<literal>[^\[\]{}]+)$")
_RELATION_ALIAS = re.compile(r'^alias\(\s*(?:Relation//)?(?P<name>[A-Za-z][A-Za-z0-9_]*)\s*\)\s*==\s*"(?P<glyph>[^"\r\n]+)"$')
_COUNTERPART = re.compile(r'^(?P<source>Relation//[A-Za-z][A-Za-z0-9_]*)\s*<-->\s*(?P<target>Relation//[A-Za-z][A-Za-z0-9_]*)$')
_INSTANCE_BINDING = re.compile(r'^(?P<kind>[A-Za-z][A-Za-z0-9_ /.-]*)//\$(?P<variable>[A-Za-z][A-Za-z0-9_]*)$')
_SCOPED_INSTANCE_BINDING = re.compile(r'^(?P<kind>.+)//\$(?P<variable>[A-Za-z][A-Za-z0-9_]*)$')
_INSTANCE_POPULATION = re.compile(rf'^(?P<kind>[A-Za-z][A-Za-z0-9_ /.-]*)//\$(?P<variable>[A-Za-z][A-Za-z0-9_]*)\{{:{_COUNT}\}}$')
_PROPERTY_INSTANCE_POPULATION = re.compile(rf'^(?P<bearer>[A-Za-z][A-Za-z0-9_ /.-]*)\.\*\*//\{{:{_COUNT}\}}$')
_MODEL_BINDING = re.compile(r'^IF\s+\$(?P<variable>[A-Za-z][A-Za-z0-9_]*)\s+in\s*\((?P<selection>[^()]*)\)\s+THEN\s*\(', re.I)
_CONTROL = re.compile(r"\b(?:IF|THEN|AND|OR)\b")
_HEADING = re.compile(r"^(?P<hashes>#{1,6})[ \t]+(?P<name>[^\n#][^\n]*?)[ \t]*$", re.M)


def _count(minimum: str | None, tail: str | None, maximum: str | None) -> Record | None:
    if minimum is None:
        return None
    return {
        "minimum": int(minimum),
        "maximum": None if tail == "+" else int(maximum) if maximum else int(minimum),
    }


def _named_property_count(count: Record | None, value_count: Record | None = None) -> Record | None:
    minimum = max(count["minimum"] if count else 0, 1 if value_count and value_count["minimum"] > 0 else 0)
    maximum = min(1, count["maximum"]) if count and count["maximum"] is not None else 1
    if minimum > maximum:
        return None
    return {"minimum": minimum, "maximum": maximum}


def _record(source: Mapping[str, Any], expression: str, kind: str, **fields: Any) -> Record:
    return {"kind": kind, "expression": expression, "source": dict(source), **fields}


def _property_selector(value: str) -> str | None:
    """Accept only a plain Property path; functions and expressions stay opaque."""

    selector = value.strip()
    plain = _MEMBERSHIP_QUALIFIER.sub("", selector)
    if not plain or any(token in plain for token in ("(", ")", "+", "=", "<", ">", "|", "@", "*", ";", ":", "[", "]", "{", "}", "'", '"')):
        try:
            parsed = notation.parse_subject_expression(selector, subject_profile="approved").expression
        except notation.SubjectNotationError:
            return None
        if (not isinstance(parsed, notation.Path) or parsed.value_format is not None or parsed.value_cardinality is not None
                or not isinstance(parsed.head, notation.Name)
                or not any(isinstance(step.operand, notation.Qualification) for step in parsed.steps)
                or any(step.operator not in {"/", "."} or not isinstance(step.operand, (notation.Name, notation.Qualification)) for step in parsed.steps)):
            return None
    return selector


def _fences(body: str) -> list[tuple[int, int, int | None, str]]:
    """Read top-level backtick/tilde fences with their actual marker width."""

    result: list[tuple[int, int, int | None, str]] = []
    active: tuple[str, int, int, int, str] | None = None
    offset = 0
    for line in body.splitlines(keepends=True):
        match = _FENCE_LINE.match(line)
        if active is None:
            if match is not None:
                marker = match.group("marker")
                active = (marker[0], len(marker), offset, offset + len(line), match.group("label").strip())
        elif match is not None:
            marker = match.group("marker")
            character, width, opening, content_start, label = active
            if marker[0] == character and len(marker) >= width and not match.group("label").strip():
                result.append((opening, content_start, offset, label))
                active = None
        offset += len(line)
    if active is not None:
        _, _, opening, content_start, label = active
        result.append((opening, content_start, None, label))
    return result


def _section_ranges(body: str, section_name: str) -> list[tuple[int, int]]:
    """Return named Markdown-section bodies, ignoring headings inside fences."""

    headings: list[tuple[int, int, int, str]] = []
    fenced = [(opening, closing if closing is not None else len(body)) for opening, _, closing, _ in _fences(body)]
    offset = 0
    for line in body.splitlines(keepends=True):
        if not any(opening <= offset < closing for opening, closing in fenced):
            match = _HEADING.match(line)
            if match is not None:
                headings.append((offset, offset + len(line), len(match.group("hashes")), match.group("name").strip()))
        offset += len(line)
    ranges = []
    for index, (_, content_start, level, heading_name) in enumerate(headings):
        if heading_name.casefold() != section_name.casefold():
            continue
        end = len(body)
        for next_start, _, next_level, _ in headings[index + 1:]:
            if next_level <= level:
                end = next_start
                break
        ranges.append((content_start, end))
    return ranges


def _claim_ranges(body: str) -> list[tuple[int, int]]:
    """Return Markdown Claim bodies, ignoring headings written inside fences."""

    return _section_ranges(body, "claim")


def _claim_parts(body: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]] | None:
    """Find named direct Claim children, leaving legacy Claims readable."""
    formal, prose = [], []
    headings = []
    fenced = [(a, c if c is not None else len(body)) for a, _, c, _ in _fences(body)]
    offset = 0
    for line in body.splitlines(keepends=True):
        match = _HEADING.match(line) if not any(a <= offset < c for a, c in fenced) else None
        if match:
            headings.append((offset, offset + len(line), len(match.group("hashes")), match.group("name").strip().casefold()))
        offset += len(line)
    for index, (_, _, level, name) in enumerate(headings):
        if name != "claim":
            continue
        end_index = next((i for i in range(index + 1, len(headings))
                          if headings[i][2] == level and headings[i][3] in {"summary", "claim", "semantics", "details"}), len(headings))
        children = [row for row in headings[index + 1:end_index]
                    if row[2] == level + 1 and row[3] in {"formal claim", "prose claim"}]
        end = headings[end_index][0] if end_index < len(headings) else len(body)
        for position, (_, start, _, child_name) in enumerate(children):
            child_end = children[position + 1][0] if position + 1 < len(children) else end
            (formal if child_name == "formal claim" else prose).append((start, child_end))
    return (formal, prose) if formal or prose else None


def section_text(carrier: Mapping[str, Any], name: str) -> str:
    """Return exact named-section text; this does not interpret its Markdown."""

    body = carrier.get("body")
    if not isinstance(body, str):
        return ""
    return "\n".join(body[start:end].strip() for start, end in _section_ranges(body, name) if body[start:end].strip())


def _split_expressions(block: str) -> list[str]:
    """Split only unquoted semicolons; unsupported quoted syntax stays whole."""

    values: list[str] = []
    start = 0
    quote: str | None = None
    escaped = False
    depth = 0
    for index, character in enumerate(block):
        if quote is not None:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote:
                quote = None
            continue
        if character in {"'", '"'}:
            quote = character
        elif character == "(":
            depth += 1
        elif character == ")":
            depth = max(0, depth - 1)
        elif character == ";" and depth == 0:
            value = block[start:index].strip()
            if value:
                values.append(value)
            start = index + 1
    value = block[start:].strip()
    if value:
        values.append(value)
    return values


def _grouped_expressions(block: str) -> list[tuple[str, str | None]]:
    groups: list[tuple[str, str | None]] = []
    pending: list[str] = []
    group = None
    quote = None
    escaped = False
    for line in block.splitlines(keepends=True):
        if quote is None and line.lstrip().startswith('#'):
            groups.extend((value, group) for value in _split_expressions(''.join(pending)))
            pending = []
            marker = line.strip().casefold()
            if marker in {'# model', '# instances'}:
                group = marker[2:]
            continue
        pending.append(line)
        for character in line:
            if quote is not None:
                if escaped:
                    escaped = False
                elif character == '\\':
                    escaped = True
                elif character == quote:
                    quote = None
            elif character in {'"', "'"}:
                quote = character
    groups.extend((value, group) for value in _split_expressions(''.join(pending)))
    return groups


def _balanced_parentheses(value: str) -> bool:
    depth = 0
    quote = None
    escaped = False
    for character in value:
        if quote:
            if escaped:
                escaped = False
            elif character == '\\':
                escaped = True
            elif character == quote:
                quote = None
        elif character in {'"', "'"}:
            quote = character
        elif character == '(':
            depth += 1
        elif character == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0 and quote is None


def _expressions(body: str) -> tuple[list[tuple[str, str | None]], list[Record]]:
    """Read CFEL fences inside Claim; retain skipped fences as diagnostics."""

    values: list[tuple[str, str | None]] = []
    diagnostics: list[Record] = []
    parts = _claim_parts(body)
    claim_ranges = parts[0] if parts is not None else _claim_ranges(body)
    for opening, content_start, closing, label in _fences(body):
        if label.casefold() != "cfel":
            continue
        if parts is not None and any(start <= opening < end for start, end in parts[1]):
            continue
        in_claim = any(start <= opening < end for start, end in claim_ranges)
        if closing is None:
            diagnostics.append({
                "code": "cfel-fence-unclosed" if in_claim else "cfel-fence-outside-claim",
                "message": (
                    "CFEL fence has no closing fence; its contents were not interpreted."
                    if in_claim else "CFEL fence is outside Claim; its contents were not interpreted."
                ),
                "offset": opening,
            })
            continue
        if in_claim:
            values.extend(_grouped_expressions(body[content_start:closing]))
        else:
            diagnostics.append({
                "code": "cfel-fence-outside-claim",
                "message": "CFEL fence is outside Claim; its contents were not interpreted.",
                "offset": opening,
            })
    return values, diagnostics


def claim_cfel_blocks(carrier: Mapping[str, Any]) -> list[Record]:
    """Return complete CFEL Claim blocks without interpreting their clauses."""

    source, body = carrier.get("source"), carrier.get("body")
    if not isinstance(source, Mapping) or not isinstance(body, str):
        return []
    parts = _claim_parts(body)
    ranges = parts[0] if parts is not None else _claim_ranges(body)
    return [
        {"source": dict(source), "block": body[content_start:closing]}
        for opening, content_start, closing, label in _fences(body)
        if label.casefold() == "cfel" and closing is not None and any(start <= opening < end for start, end in ranges)
    ]


def claim_fenced_blocks(carrier: Mapping[str, Any]) -> list[Record]:
    """Return every fenced Claim block with its original language label.

    Only blocks labelled ``CFEL`` are structurally extracted elsewhere.  Other
    labels, including no label, remain source evidence rather than being
    relabelled or interpreted as CFEL.
    """

    source, body = carrier.get("source"), carrier.get("body")
    if not isinstance(source, Mapping) or not isinstance(body, str):
        return []
    ranges = _claim_ranges(body)
    return [
        {"source": dict(source), "block": body[content_start:closing if closing is not None else len(body)],
         "label": label, "closed": closing is not None}
        for opening, content_start, closing, label in _fences(body)
        if any(start <= opening < end for start, end in ranges)
    ]


def claim_prose(carrier: Mapping[str, Any]) -> str:
    """Return Claim text after removing fenced blocks, without parsing prose."""

    body = carrier.get("body")
    if not isinstance(body, str):
        return ""
    parts = _claim_parts(body)
    if parts is not None:
        return "\n".join(body[start:end].strip() for start, end in parts[1] if body[start:end].strip())
    pieces = []
    for start, end in _claim_ranges(body):
        removed = []
        for opening, _, closing, _ in _fences(body):
            if not start <= opening < end:
                continue
            if closing is None:
                removed.append((opening, end))
                continue
            newline = body.find("\n", closing)
            removed.append((opening, len(body) if newline < 0 else newline + 1))
        cursor = start
        for opening, closing in removed:
            pieces.append(body[cursor:opening])
            cursor = closing
        pieces.append(body[cursor:end])
    return "\n".join(piece.strip() for piece in pieces if piece.strip())


def has_prose_claim(carrier: Mapping[str, Any]) -> bool:
    body = carrier.get("body")
    parts = _claim_parts(body) if isinstance(body, str) else None
    return parts is not None and bool(parts[1])


def extract_claim_constraints(carrier: Mapping[str, Any]) -> tuple[list[Record], list[Record]]:
    """Return recognized constraints and explicit unsupported CFEL diagnostics."""

    source = carrier.get("source")
    body = carrier.get("body")
    if not isinstance(source, Mapping) or not isinstance(body, str):
        return [], []
    expressions, diagnostics = _expressions(body)
    records: list[Record] = []
    for expression, group in expressions:
        record_start, diagnostic_start = len(records), len(diagnostics)
        try:
            binder = _MODEL_BINDING.match(expression) if group == 'model' else None
            if binder is not None and expression.rstrip().endswith(')') and _balanced_parentheses(expression):
                records.append(_record(source, expression, "model_binding", variable=binder.group("variable"),
                                       selection=binder.group("selection"), interpretation="opaque"))
                continue
            population = _INSTANCE_POPULATION.fullmatch(expression) if group == 'instances' else None
            if population is not None:
                records.append(_record(source, expression, "instance_population_constraint",
                                       kind_selector=population.group("kind").strip(), variable=population.group("variable"),
                                       scope="project",
                                       population_cardinality=_count(population.group("minimum"), population.group("tail"), population.group("maximum"))))
                continue
            property_population = _PROPERTY_INSTANCE_POPULATION.fullmatch(expression)
            if property_population is not None:
                records.append(_record(source, expression, "property_instance_population_constraint",
                                       bearer_selector=property_population.group("bearer").strip(),
                                       property_selection="recursive_dependents", scope="per_bearer_each_schema",
                                       population_cardinality=_count(property_population.group("minimum"), property_population.group("tail"), property_population.group("maximum"))))
                continue
            binding = _INSTANCE_BINDING.fullmatch(expression) if group == 'instances' else None
            if binding is None and group == 'instances':
                scoped_binding = _SCOPED_INSTANCE_BINDING.fullmatch(expression)
                if scoped_binding is not None:
                    try:
                        kind = notation.parse_subject_expression(scoped_binding.group("kind"), subject_profile="approved").expression
                    except notation.SubjectNotationError:
                        kind = None
                    if (isinstance(kind, notation.Path) and isinstance(kind.head, notation.Name)
                            and kind.value_format is None and kind.value_cardinality is None
                            and any(isinstance(step.operand, notation.Qualification) for step in kind.steps)
                            and all(step.operator in {"/", "."} and isinstance(step.operand, (notation.Name, notation.Qualification)) for step in kind.steps)):
                        binding = scoped_binding
            if binding is not None:
                records.append(_record(source, expression, "instance_binding", kind_selector=binding.group("kind").strip(), variable=binding.group("variable")))
                continue
            alias = _RELATION_ALIAS.fullmatch(expression)
            if alias is not None:
                records.append(_record(source, expression, "relation_alias", relation=alias.group("name"), glyph=alias.group("glyph")))
                continue
            counterpart = _COUNTERPART.fullmatch(expression)
            if counterpart is not None:
                records.append(_record(source, expression, "relation_cardinality", source_selector=counterpart.group("source"),
                                       relation="HAS_INVERSE", relation_notation="<-->", target_selector=counterpart.group("target"),
                                       source_cardinality=None, target_cardinality=None, written_direction="forward"))
                continue
            if _CONTROL.search(expression):
                diagnostics.append({
                    "code": "cfel-expression-unsupported",
                    "message": "CFEL control expression is outside the bounded projection extractor.",
                    "expression": expression,
                    "source": dict(source),
                })
                continue
            relation = _RELATION.fullmatch(expression)
            if relation is not None and not (relation.group("source").rstrip().endswith(":")
                                             or relation.group("target").lstrip().startswith(":")):
                reverse_named = relation.group("reverse_relation") is not None
                written_source = relation.group("source").strip()
                written_target = relation.group("target").strip()
                written_forward = _count(
                    relation.group("forward_minimum"), relation.group("forward_tail"), relation.group("forward_maximum"),
                )
                written_reverse = _count(
                    relation.group("reverse_minimum"), relation.group("reverse_tail"), relation.group("reverse_maximum"),
                )
                records.append(_record(
                    source, expression, "relation_cardinality",
                    source_selector=written_target if reverse_named else written_source,
                    relation=(relation.group("reverse_relation") or relation.group("relation")).strip()
                    if (relation.group("reverse_relation") or relation.group("relation")) else None,
                    relation_notation=relation.group("relation_notation"),
                    target_selector=written_source if reverse_named else written_target,
                    source_cardinality=written_reverse if reverse_named else written_forward,
                    target_cardinality=written_forward if reverse_named else written_reverse,
                    written_direction="reverse" if reverse_named else "forward",
                    written_source_selector=written_source,
                    written_target_selector=written_target,
                    written_source_cardinality=written_forward,
                    written_target_cardinality=written_reverse,
                ))
                continue
            relation_without_target = _RELATION_WITHOUT_TARGET.fullmatch(expression)
            if relation_without_target is not None:
                relation_name = (
                    relation_without_target.group("relation")
                    or relation_without_target.group("bare_relation")
                )
                records.append(_record(
                    source, expression, "relation_cardinality",
                    source_selector=relation_without_target.group("source").strip(),
                    relation=relation_name,
                    relation_notation=relation_without_target.group("relation_notation"),
                    target_selector=None,
                    source_cardinality=_count(
                        relation_without_target.group("forward_minimum"),
                        relation_without_target.group("forward_tail"),
                        relation_without_target.group("forward_maximum"),
                    ),
                    target_cardinality=None,
                    selection="all_relations" if relation_name == "*" else "named_relation",
                    written_direction="forward",
                    target_domain="unresolved",
                ))
                continue
            classification = (
                _FORWARD_GROUPED_CLASSIFICATION.fullmatch(expression)
                or _REVERSE_GROUPED_CLASSIFICATION.fullmatch(expression)
                or _FORWARD_CLASSIFICATION.fullmatch(expression)
                or _REVERSE_CLASSIFICATION.fullmatch(expression)
            )
            if classification is not None:
                records.append(_record(
                    source, expression, "classification_condition",
                    subject_selector=classification.group("subject").strip(),
                    axis=classification.group("axis").strip(),
                    operator=classification.group("operator"),
                    value=classification.group("value").strip(),
                ))
                continue
            named_property = _NAMED_PROPERTY.fullmatch(expression)
            named_selector = _property_selector(named_property.group("property")) if named_property is not None else None
            if named_property is not None and named_selector is not None:
                occurrence = _count(named_property.group("minimum"), named_property.group("tail"), named_property.group("maximum"))
                effective = _named_property_count(occurrence)
                records.append(_record(source, expression, "property_constraint", property_selector=named_selector,
                                       selection="property", name_format=None, occurrence_cardinality=occurrence,
                                       effective_occurrence_cardinality=effective, occurrence_conflict=effective is None,
                                       value_format=None, value_cardinality=None))
                continue
            property_constraint = _PROPERTY.fullmatch(expression)
            # The direct-value form is a different constraint: the count applies
            # to values per Property, not to Property occurrences.  Keep it out
            # of the broader Property matcher, whose path token may otherwise
            # absorb the colon.
            property_selector = _property_selector(property_constraint.group("property")) if property_constraint is not None else None
            if property_constraint is not None and property_selector is not None and not (
                property_constraint.group("descendants") is None
                and property_constraint.group("property").rstrip().endswith(":")
            ):
                selection = {None: "property", ".*": "immediate_dependents", ".**": "recursive_dependents"}[
                    property_constraint.group("descendants")
                ]
                occurrence = _count(property_constraint.group("minimum"), property_constraint.group("tail"), property_constraint.group("maximum"))
                named = selection == "property" and property_constraint.group("name_format") is None
                value_count = _count(property_constraint.group("value_minimum"), property_constraint.group("value_tail"), property_constraint.group("value_maximum"))
                effective = _named_property_count(occurrence, value_count) if named else occurrence
                records.append(_record(
                    source, expression, "property_constraint",
                    property_selector=property_selector,
                    selection=selection,
                    name_format=property_constraint.group("name_format"),
                    occurrence_cardinality=occurrence,
                    effective_occurrence_cardinality=effective,
                    occurrence_conflict=named and effective is None,
                    value_format=property_constraint.group("value_format"),
                    value_cardinality=value_count,
                ))
                continue
            property_value = _PROPERTY_VALUE.fullmatch(expression)
            value_selector = _property_selector(property_value.group("property")) if property_value is not None else None
            if (property_value is not None and value_selector is not None
                    and (property_value.group("value_format") is not None or property_value.group("minimum") is not None)):
                value_count = _count(property_value.group("minimum"), property_value.group("tail"), property_value.group("maximum"))
                descendants = property_value.group("descendants")
                records.append(_record(
                    source, expression, "property_constraint",
                    property_selector=value_selector,
                    selection={None: "values", ".*": "immediate_dependent_values", ".**": "recursive_dependent_values"}[descendants],
                    name_format=None,
                    occurrence_cardinality=None,
                    **({"effective_occurrence_cardinality": _named_property_count(None, value_count)} if descendants is None else {}),
                    value_format=property_value.group("value_format"),
                    value_cardinality=value_count,
                ))
                continue
            allowed_literal = _ALLOWED_LITERAL.fullmatch(expression)
            literal_selector = _property_selector(allowed_literal.group("property")) if allowed_literal is not None else None
            if literal_selector is None:
                allowed_literal = _QUALIFIED_ALLOWED_LITERAL.fullmatch(expression)
                literal_selector = _property_selector(allowed_literal.group("property")) if allowed_literal is not None else None
            if allowed_literal is not None and literal_selector is not None and not any(
                token in expression for token in (":=", ": =", "'", '"', ">|", "|<", "((")
            ) and not any(token in allowed_literal.group("literal") for token in ("(", ")")):
                records.append(_record(
                    source, expression, "allowed_literal",
                    property_selector=literal_selector,
                    literal=allowed_literal.group("literal").strip(),
                ))
                continue
            if group in {None, "model"}:
                try:
                    subject = notation.parse_subject_expression(expression, subject_profile="approved").expression
                except notation.SubjectNotationError:
                    subject = None
                if (isinstance(subject, notation.Path) and isinstance(subject.head, notation.Name)
                        and subject.value_format is None and subject.value_cardinality is None
                        and all(step.operator in {"/", "."} and isinstance(step.operand, (notation.Name, notation.Qualification)) for step in subject.steps)):
                    records.append(_record(source, expression, "subject_expression", selector=notation.render_subject(subject)))
                    continue
            diagnostics.append({
                "code": "cfel-expression-unsupported",
                "message": "CFEL expression is outside the bounded projection extractor.",
                "expression": expression,
                "source": dict(source),
            })
        finally:
            if group is not None:
                for row in records[record_start:] + diagnostics[diagnostic_start:]:
                    row["group"] = group
    return records, diagnostics


def constraints_for(carriers: Iterable[Mapping[str, Any]]) -> tuple[list[Record], list[Record]]:
    """Collect deterministic records from supplied Carriers without writing them."""

    records: list[Record] = []
    diagnostics: list[Record] = []
    for carrier in carriers:
        selected, unresolved = extract_claim_constraints(carrier)
        records.extend(selected)
        diagnostics.extend(unresolved)
    key = lambda row: (str(row.get("kind", "")), str(row.get("expression", "")), str(row.get("source", {})))
    return sorted(records, key=key), sorted(diagnostics, key=key)


def preview_constraints_from_paths(
    paths: Iterable[Path], *, repository: Path | None = None,
) -> tuple[list[Record], list[Record]]:
    """Read exactly supplied Markdown Carriers for a no-write CFEL preview.

    Unlike the current-source reader, this deliberately does not filter Draft
    or Archived paths. Callers choose the exact preview frontier; this helper
    only reads it and returns the same records/diagnostics as ``constraints_for``.
    """

    from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

    base = repository.absolute() if repository is not None else None
    carriers: list[Record] = []
    for path in paths:
        raw = path.read_bytes()
        parsed = parse_carrier(raw, path)
        atom_id = parsed.metadata.get("atom_id")
        version = parsed.metadata.get("version")
        if not isinstance(atom_id, str) or not atom_id.strip() or isinstance(version, bool) or not isinstance(version, int):
            raise ValueError(f"{path}: CFEL preview requires text atom_id and integer version")
        display_path = path.relative_to(base).as_posix() if base is not None else path.as_posix()
        carriers.append({
            "source": {
                "atom_id": atom_id,
                "version": version,
                "path": display_path,
                "sha256": hashlib.sha256(raw).hexdigest(),
            },
            "body": parsed.body,
        })
    return constraints_for(carriers)
