"""Extract a deliberately small, non-evaluating CFEL constraint inventory.

This is a projection aid, not a CFEL parser or validator. Every expression
outside the few shape-stable forms below remains visible as an unsupported
diagnostic rather than being guessed or silently discarded.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import subject_notation as notation
from carrier_aliases import carrier_read_view, matches_named_value

Record = dict[str, Any]
_FENCE_LINE = re.compile(r"^[ \t]*(?P<marker>`{3,}|~{3,})(?P<label>[^\r\n]*)\r?$")
_COUNT = r"(?P<minimum>0|[1-9][0-9]*)(?P<tail>\+|\.\.(?P<maximum>0|[1-9][0-9]*))?"
_PROPERTY = re.compile(
    rf"^(?P<property>.+?)(?P<descendants>\.\*\*|\.\*)?"
    rf"(?:\[(?P<name_format>[^\]]*)\])?"
    rf"\{{::?{_COUNT}\}}"
    rf"(?:\s*::?\s*(?:\[(?P<value_format>[^\]]*)\])?\{{::?(?P<value_minimum>0|[1-9][0-9]*)(?P<value_tail>\+|\.\.(?P<value_maximum>0|[1-9][0-9]*))?\}})?$"
)
_PROPERTY_VALUE = re.compile(
    rf"^(?P<property>.+?)(?P<descendants>\.\*\*|\.\*)?\s*::?\s*(?:\[(?P<value_format>[^\]]*)\])?"
    rf"(?:\{{::?{_COUNT}\}})?$"
)
_NAMED_PROPERTY = re.compile(rf"^(?P<property>.+?)(?:\{{::?{_COUNT}\}})?\s*::?$")
_MEMBERSHIP_QUALIFIER = re.compile(r"/\(\.[A-Za-z][A-Za-z0-9_. -]*\s+in\s+[A-Za-z][A-Za-z0-9_. -]*\)(?=\.|$)")
_ORDERING = re.compile(r"^(?P<left>.+?)\s*(?P<operator>;>|<;)\s*(?P<right>.+)$")
_ORDERING_ROLE = re.compile(r"^Atom/\(\.Header\.Context\.Role in (RMED|\([A-Za-z, ]+\))\)\.")
_RMED_ROLES = ("Requirement", "Method", "Evaluation", "Delivery")
_RELATION = re.compile(
    rf"^(?P<source>.+?)\s*(?:\{{::?(?P<forward_minimum>0|[1-9][0-9]*)(?P<forward_tail>\+|\.\.(?P<forward_maximum>0|[1-9][0-9]*))?\}}\s*)?"
    rf"(?:<\(\((?P<reverse_relation>[^()]+)\)\)|\(\((?P<relation>[^()]+)\)\)|(?P<relation_notation>\+>|<\+))\s*"
    rf"(?:\{{::?(?P<reverse_minimum>0|[1-9][0-9]*)(?P<reverse_tail>\+|\.\.(?P<reverse_maximum>0|[1-9][0-9]*))?\}}\s*)?"
    rf"(?P<target>.+)$"
)
_GROUPED_INSTANCE_RELATION = re.compile(
    r"^\((?P<source>[^()]+)\)\s*\(\(INSTANCE_OF\)\)\s*(?P<target>[^()]+)$"
)
_RELATION_WITHOUT_TARGET = re.compile(
    rf"^(?P<source>.+?)\s*\{{:(?P<forward_minimum>0|[1-9][0-9]*)(?P<forward_tail>\+|\.\.(?P<forward_maximum>0|[1-9][0-9]*))?\}}\s*"
    rf"(?:\(\((?P<relation>[^()]+)\)\)|(?P<relation_notation>\+>|<\+)|(?P<bare_relation>[A-Z][A-Z0-9_]*))$"
)
_ALLOWED_CLASSIFICATION_VALUE = re.compile(
    r"^(?P<subject>[A-Za-z_][A-Za-z_0-9 .-]*)\s*>\|\s*(?P<axis>[A-Za-z_][A-Za-z_0-9 .-]*?):\s*(?P<value>[A-Za-z_][A-Za-z_0-9 .-]*)$"
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
_ALLOWED_LITERAL = re.compile(r"^(?P<property>.+?)\s*:{1,2}\s*(?P<literal>[^\[\]{}]+)$")
_QUALIFIED_ALLOWED_LITERAL = re.compile(r"^(?P<property>.+\).+?)\s*:{1,2}\s*(?P<literal>[^\[\]{}]+)$")
_PROPERTY_MINIMUM = re.compile(r"^(?P<property>.+?)\s*>=\s*(?P<value>-?\d+(?:\.\d+)?)$")
_RELATION_ALIAS = re.compile(r'^alias\(\s*(?:Relation//)?(?P<name>[A-Za-z][A-Za-z0-9_]*)\s*\)\s*==\s*"(?P<glyph>[^"\r\n]+)"$')
_OPERATOR_SYMBOL = re.compile(r'Operator//(?P<name>[A-Za-z_][A-Za-z_0-9]*)\s*==\s*(?P<symbol>"(?:[^"\\\x00-\x1f]|\\(?:["\\/bfnrt]|u[0-9a-fA-F]{4}))*")')
_OPERATOR_SUBJECT = re.compile(r'(?:^|<\+\s*)CFEL\s*<\+\s*Operator//(?P<name>[A-Za-z_][A-Za-z_0-9]*)\s*$')
_COUNTERPART = re.compile(r'^(?P<source>Relation//[A-Za-z][A-Za-z0-9_]*)\s*<-->\s*(?P<target>Relation//[A-Za-z][A-Za-z0-9_]*)$')
_UNFILTERED_UNIQUE = re.compile(r"^UNIQUE\(\s*(?P<population>[A-Za-z][A-Za-z0-9_ /.-]*)//\$[A-Za-z][A-Za-z0-9_]*\s*,\s*\(\s*\.(?P<key>[A-Za-z_][A-Za-z_0-9 .-]*)\s*\)\s*\)$")
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
    minimum = count["minimum"] if count is not None else int(bool(value_count and value_count["minimum"] > 0))
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


def _sibling_order(expression: str) -> Record | None:
    match = _ORDERING.fullmatch(expression)
    if match is None:
        return None
    left, operator, right = match.group("left", "operator", "right")
    qualifier = _ORDERING_ROLE.match(left)
    roles = ()
    if qualifier is not None:
        if not right.startswith(qualifier[0]):
            return None
        role_names = qualifier[1]
        roles = _RMED_ROLES if role_names == "RMED" else tuple(name.strip() for name in role_names[1:-1].split(","))
        if not all(roles):
            return None
        left = "Atom." + left[qualifier.end():]
        right = "Atom." + right[qualifier.end():]
    if not (_property_selector(left) and _property_selector(right)) or "." not in left or "." not in right:
        return None
    bearer, first = left.rsplit(".", 1)
    other_bearer, second = right.rsplit(".", 1)
    if bearer != other_bearer or first == second:
        return None
    source, target = (left, right) if operator == ";>" else (right, left)
    return {"bearer": bearer, "relation": "IS_ORDERED_RIGHT_BEFORE", "relation_notation": operator,
            "source_selector": source, "target_selector": target,
            "source_cardinality": None, "target_cardinality": None,
            "written_direction": "forward" if operator == ";>" else "reverse",
            **({"ordering_roles": roles} if roles else {})}


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
        elif character == ";" and depth == 0 and block[index:index + 2] != ";>" and (
            block[index - 1:index] != "<" or block[index - 2:index] == "<<"
        ):
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


def claim_python_blocks(carrier: Mapping[str, Any]) -> list[Record]:
    """Select authored Python model Claims, never Workflow or prose examples."""
    view = carrier.get("read_view")
    if not isinstance(view, Mapping):
        metadata = carrier.get("metadata")
        view = carrier_read_view(dict(metadata)) if isinstance(metadata, Mapping) else {}
    if not any(matches_named_value(view.get("content_role"), role)
               for role in ("Requirement", "Method", "Evaluation", "Delivery")):
        return []
    source, body = carrier.get("source"), carrier.get("body")
    if not isinstance(source, Mapping) or not isinstance(body, str):
        return []
    parts = _claim_parts(body)
    ranges = parts[0] if parts is not None else _claim_ranges(body)
    return [
        {"source": dict(source), "block": body[start:closing], "label": label}
        for opening, start, closing, label in _fences(body)
        if label.casefold() == "python" and closing is not None
        and any(lo <= opening < hi for lo, hi in ranges)
    ]


def python_compiler_expressions(block: str) -> list[tuple[str, str | None]]:
    """Read normalized statements without changing the legacy graph semantics."""
    from python_model_claim import parse_grouped_python_model_claim
    return [(part, group)
            for expression, group in parse_grouped_python_model_claim(block)
            for part in _split_expressions(expression)]


def native_declaration(block: str) -> dict[str, Any] | None:
    """Read the native declaration without executing its Python source."""
    import sys
    from pathlib import Path

    programmatic = str(Path(__file__).resolve().parents[2])
    if programmatic not in sys.path:
        sys.path.insert(0, programmatic)
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim

    return parse_native_model_claim(block)


def _native_count(value: Any) -> Record | None:
    if type(value) is int and value >= 0:
        return {"minimum": value, "maximum": value}
    if isinstance(value, dict) and set(value) == {"minimum", "maximum"}:
        return value
    return None


def _native_constraints(declaration: Mapping[str, Any], source: Mapping[str, Any], block: str) -> list[Record]:
    args = declaration["arguments"]
    result: list[Record] = []
    check = declaration.get("instance_check")
    if check is not None:
        scope_check = (args.get("base_path") == "Scope Unit" and args.get("entity_name") == "structural_level"
                       and check.get("name") == "check_structural_level" and check.get("parameter_type") == "ScopeUnit")
        if check.get("name") == "dependencies_are_distinct":
            from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compile_atom_dependencies_with_check
            compile_atom_dependencies_with_check(declaration)
        elif not (scope_check and args.get("relation_name") == "IS_PROPERTY_OF"
                  or args.get("entity_class") == check["parameter_type"]):
            raise ValueError("unsupported instance check")
        result.append(_record(source, f'{check["name"]}({check["parameter"]}: {check["parameter_type"]})',
                              "instance_check", group="instances", callback=check["name"]))
    if declaration["kind"] == "entity" and args.get("entity_class"):
        row = next((row for row in declaration["classes"] if row["name"] == args["entity_class"]), None)
        if row is None:
            raise ValueError("declared entity class is unavailable")
        result.append(_record(source, block, "native_class", group="model",
                              entity_name=args["entity_name"], class_name=row["name"],
                              bases=row["bases"], qualification_property_path=args.get("qualification_property_path"),
                              fields=row["fields"], arguments=args))
        classifications = args.get("classifications", {})
        if not isinstance(classifications, Mapping) or any(
            not axis.strip() or type(value) not in (str, int, float, bool)
            for axis, value in classifications.items()
        ):
            raise ValueError("classifications must map names to literal values")
        for axis, value in classifications.items():
            result.append(_record(source, block, "classification_condition", group="model",
                                  subject_selector=args["entity_name"], axis=axis, operator="==", value=str(value)))
        if args.get("qualification_property_path") == "Projection.Form" and row["bases"] == ("Projection",):
            result.append(_record(source, block, "allowed_literal", group="model",
                                  property_selector="Projection.Form", literal=args["entity_name"]))
        if "instance_population_cardinality" in args:
            result.append(_record(source, block, "native_population_constraint", group="instances",
                                  cardinality=_native_count(args["instance_population_cardinality"]),
                                  scope=args.get("instance_population_scope")))
        for path, constraint in args.get("instance_property_constraints", {}).items():
            count = _native_count(constraint.get("value_cardinality"))
            if count is not None:
                result.append(_record(source, block, "property_constraint", group="instances",
                                      property_selector=f"{args['entity_name']}//$instance.{path}",
                                      selection="values", name_format=None, occurrence_cardinality=None,
                                      effective_occurrence_cardinality=_named_property_count(None, count),
                                      value_format="" if count == {"minimum": 0, "maximum": 0} else None,
                                      value_cardinality=count))
        return result
    if declaration["kind"] == "entity" and args.get("relation_name") == "IS_PROPERTY_OF":
        if not isinstance(args.get("base_path"), str) or not args["base_path"]:
            raise ValueError("Property declaration requires a base_path")
        if forms := args.get("applies_to_forms"):
            import json
            role = args["applies_to_role"]
            role = json.dumps(role) if " " in role else role
            for form in forms:
                selector = f"Atom/(.Header.Context.Role in ({role}))/(.Header.Context.Form in ({form})).Header.State.Status"
                for value in args.get("allowed_values", ()):
                    result.append(_record(source, f"{selector} :: {value}", "allowed_literal", group="model", property_selector=selector, literal=value))
            return result
        for rule in args.get("population_unique_constraints", ()):
            result.append(_record(source, block, "population_unique_constraint", group="instances",
                                  population_selector=args.get("population_entity_path", args["base_path"]),
                                  keys=rule["keys"], **({"status": rule["status"], "single_value_paths": rule["single_value_paths"]} if "status" in rule else {})))
        for dependency in args.get("population_functional_dependencies", ()):
            result.append(_record(source, block, "population_functional_dependency", group="instances",
                                  population_selector=args.get("population_entity_path", args["base_path"]),
                                  keys=dependency["keys"], dependents=dependency["dependents"],
                                  **({"status_groups": dependency["status_groups"]} if "status_groups" in dependency else {})))
        selector = f"{args['base_path']}.{args['entity_name']}"
        occurrence = _native_count(args.get("property_occurrence_cardinality"))
        values = _native_count(args.get("value_cardinality"))
        effective = _named_property_count(occurrence, values)
        if not args.get("allowed_values") or occurrence is not None or values is not None or "value_format" in args:
            result.append(_record(source, block, "property_constraint", group="model",
                                  property_selector=selector, selection="property", name_format=None,
                                  occurrence_cardinality=occurrence, effective_occurrence_cardinality=effective,
                                  occurrence_conflict=effective is None, value_format=args.get("value_format"),
                                  value_cardinality=values,
                                  **({"model_value_format": declaration["model_value_format"]} if declaration.get("model_value_format") else {}),
                                  applicable_entity_classes=args.get("applies_to_entity_classes")))
        dependent_value_count = _native_count(args.get("dependent_property_value_cardinality"))
        dependent_value_format = args.get("dependent_property_value_format")
        if "dependent_property_cardinality" in args or (
            "dependent_property_value_format" in args and dependent_value_count is None
        ):
            result.append(_record(source, block, "property_constraint", group="model",
                                  property_selector=selector, selection="immediate_dependents",
                                  name_format=args.get("dependent_property_name_format"),
                                  occurrence_cardinality=_native_count(args.get("dependent_property_cardinality")),
                                  effective_occurrence_cardinality=_native_count(args.get("dependent_property_cardinality")),
                                  occurrence_conflict=False,
                                  value_format=dependent_value_format if dependent_value_count is None else None,
                                  value_cardinality=None,
                                  allowed_names=args.get("allowed_dependent_property_names")))
        if dependent_value_count is not None:
            result.append(_record(source, block, "property_constraint", group="model",
                                  property_selector=selector, selection="immediate_dependent_values",
                                  name_format=None, occurrence_cardinality=None,
                                  value_format=dependent_value_format, value_cardinality=dependent_value_count))
        if "recursive_dependent_property_cardinality" in args:
            count = _native_count(args["recursive_dependent_property_cardinality"])
            result.append(_record(source, block, "property_constraint", group="model",
                                  property_selector=selector, selection="recursive_dependents",
                                  name_format=args.get("recursive_dependent_property_name_format"),
                                  occurrence_cardinality=count, effective_occurrence_cardinality=count,
                                  occurrence_conflict=False, value_format=None, value_cardinality=None))
        if "recursive_dependent_property_value_format" in args:
            result.append(_record(source, block, "property_constraint", group="model",
                                  property_selector=selector, selection="recursive_dependent_values",
                                  name_format=None, occurrence_cardinality=None,
                                  value_format=args["recursive_dependent_property_value_format"], value_cardinality=None))
        for first, second in args.get("ordered_dependent_property_pairs", ()):
            result.append(_record(source, f"{selector}.{first} ;> {selector}.{second}", "relation_cardinality",
                                  group="model", bearer=selector, relation="IS_ORDERED_RIGHT_BEFORE",
                                  source_selector=f"{selector}.{first}", target_selector=f"{selector}.{second}",
                                  source_cardinality=None, target_cardinality=None, written_direction="forward",
                                  applicable_entity_classes=args.get("applies_to_entity_classes"),
                                  **({"ordering_roles": args["ordered_dependent_property_roles"]}
                                     if "ordered_dependent_property_roles" in args else {})))
        if "minimum_value" in args:
            minimum = args["minimum_value"]
            if type(minimum) not in (int, float):
                raise ValueError("minimum_value must be numeric")
            result.append(_record(source, f"{selector} >= {minimum}", "property_value_bound",
                                  group="model", property_selector=selector, operator=">=", value=minimum))
        for value in args.get("allowed_values", ()):
            result.append(_record(source, f"{selector} :: {value}", "allowed_literal",
                                  group="model", property_selector=selector, literal=value,
                                  applicable_entity_classes=args.get("applies_to_entity_classes")))
        for status, order in args.get("status_order_numbers", {}).items():
            subject = f"Atom/(.Header.State.Status := {status}).Header.State.Status"
            result.append(_record(source, f"{subject} >| (Status Order Number == {order})",
                                  "classification_condition", group="model", subject_selector=subject,
                                  axis="Status Order Number", operator="==", value=str(order)))
        for status, group in args.get("status_groups", {}).items():
            role = args["applies_to_entity_classes"][0]
            subject = f"Atom/(.Header.Context.Role := {role})/(.Header.State.Status := {status}).Header.State.Status"
            result.append(_record(source, f"{subject} >| Status Group == {group}", "classification_condition", group="model", subject_selector=subject, axis="Status Group", operator="==", value=group))
        if "maximum_value" in args:
            result.append(_record(source, f"{selector} <= {args['maximum_value']}", "property_value_bound",
                                  group="model", property_selector=selector, operator="<=", value=args["maximum_value"]))
        if "fallback_chain" in args:
            result.append(_record(source, block, "effective_value_fallback_chain", group="instances",
                                  property_selector=selector, branches=args["fallback_chain"],
                                  empty_values=("undefined", "null", ""), project_cardinality=1))
        if "fallback_value" in args:
            result.append(_record(source, f"{selector} ?== {args['fallback_value']}",
                                  "effective_value_fallback", group="instances", property_selector=selector,
                                  fallback_literal=args["fallback_value"], empty_values=("undefined", "null", "")))
        if args.get("fallback_property_name"):
            bearer = args["base_path"]
            result.append(_record(source, f"{bearer}.{args['entity_name']} ?== {bearer}.{args['fallback_property_name']}",
                                  "effective_value_fallback", group="instances",
                                  property_selector=f"{bearer}.{args['entity_name']}",
                                  fallback_property_selector=f"{bearer}.{args['fallback_property_name']}",
                                  empty_values=("undefined", "null", "")))
        return result
    if declaration["kind"] == "relation":
        name = args["relation_name"]
        result.append(_record(source, block, "native_relation_declaration", group="model",
                              relation=name, arguments=args))
        for selector, direction in ((args.get("source_endpoint"), "source"), (args.get("target_endpoint"), "target")):
            if isinstance(selector, dict):
                result.append(_record(source, block, "relation_endpoint", group="model", relation=name,
                                      direction=direction, endpoint=selector,
                                      targets_per_source=_native_count(args.get("targets_per_source")),
                                      sources_per_target=_native_count(args.get("sources_per_target"))))
        for pair in args.get("endpoint_pairs", ()):
            result.append(_record(source, block, "relation_endpoint_pair", group="model", relation=name,
                                  source_endpoint=pair["source_endpoint"], target_endpoint=pair["target_endpoint"],
                                  targets_per_source=_native_count(args.get("targets_per_source")),
                                  sources_per_target=_native_count(args.get("sources_per_target"))))
        if inverse := args.get("inverse_alias"):
            instance_levels = {"instances", "model_entities_or_instances"}
            pairs = args.get("endpoint_pairs", (args,))
            is_inverse = all(pair[endpoint]["level"] in instance_levels for pair in pairs for endpoint in ("source_endpoint", "target_endpoint"))
            result.append(_record(source, block, "relation_cardinality", group="model",
                                  source_selector=f"Relation//{name if is_inverse else inverse}",
                                  relation="HAS_INVERSE" if is_inverse else "IS_INVERSE_ALIAS_FOR",
                                  target_selector=f"Relation//{inverse if is_inverse else name}", source_cardinality=None,
                                  target_cardinality=None, written_direction="forward"))
        if alias := args.get("written_alias"):
            result.append(_record(source, block, "relation_alias", group="model", relation=name, glyph=alias))
    return result


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
    native_records: list[Record] = []
    from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements, has_dataclass_field_contracts

    for block in claim_python_blocks(carrier):
        try:
            declaration = native_declaration(block["block"])
            if declaration is None:
                expressions.extend(python_compiler_expressions(block["block"]))
            elif has_dataclass_field_contracts(declaration):
                expressions.extend((statement, "model") for statement in compiler_model_statements(declaration))
            elif "structure_paths" in declaration.get("arguments", {}):
                expressions.extend((statement, "instances") for statement in compiler_model_statements(declaration))
            elif "allowed_classification_values" in declaration.get("arguments", {}):
                expressions.extend((statement, "model") for statement in compiler_model_statements(declaration))
            elif declaration.get("arguments", {}).get("instance", {}).get("type") == "Aspect":
                expressions.extend((statement, None) for statement in compiler_model_statements(declaration))
            else:
                native_records.extend(_native_constraints(declaration, source, block["block"]))
        except ValueError as error:
            diagnostics.append({"code": "python-formal-claim-invalid", "message": str(error), "source": dict(source)})
    records: list[Record] = native_records
    subjects = carrier.get("subjects") or {}
    subject = subjects.get("governs") or subjects.get("active")
    operator = _OPERATOR_SUBJECT.search(subject) if isinstance(subject, str) else None
    for expression, group in expressions:
        record_start, diagnostic_start = len(records), len(diagnostics)
        try:
            if group == "model" and operator and (symbol := _OPERATOR_SYMBOL.fullmatch(expression)):
                if symbol["name"] == operator["name"] and (value := json.loads(symbol["symbol"])):
                    records.append(_record(source, expression, "operator_symbol", operator=symbol["name"], symbol=value))
                    continue
            uniqueness = _UNFILTERED_UNIQUE.fullmatch(expression) if group == "instances" else None
            if uniqueness is not None:
                records.append(_record(source, expression, "population_unique_constraint", group="instances",
                                       population_selector=uniqueness.group("population").strip(),
                                       keys=(uniqueness.group("key").strip(),)))
                continue
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
            if order := _sibling_order(expression):
                records.append(_record(source, expression, "relation_cardinality", **order))
                continue
            grouped_instance = _GROUPED_INSTANCE_RELATION.fullmatch(expression)
            if grouped_instance is not None:
                try:
                    grouped = notation.parse_subject_expression(grouped_instance.group("source"), subject_profile="approved").expression
                    target = notation.parse_subject_expression(grouped_instance.group("target").strip(), subject_profile="approved").expression
                except notation.SubjectNotationError:
                    grouped = target = None
                if (isinstance(grouped, notation.RelationChain) and grouped.links
                        and all(link.operator == "<+" and link.relation_type is None
                                and link.forward_cardinality is None and link.reverse_cardinality is None
                                for link in grouped.links)
                        and all(isinstance(endpoint.head, notation.Name) and not endpoint.value_format
                                and not endpoint.value_cardinality and all(
                                    step.operator in {"/", "//"} and isinstance(step.operand, notation.Name)
                                    for step in endpoint.steps) for endpoint in grouped.endpoints)
                        and isinstance(target, notation.Path) and isinstance(target.head, notation.Name)
                        and not target.steps and target.value_format is None and target.value_cardinality is None):
                    written_source = "(" + grouped_instance.group("source").strip() + ")"
                    written_target = grouped_instance.group("target").strip()
                    records.append(_record(
                        source, expression, "relation_cardinality", source_selector=written_source,
                        relation="INSTANCE_OF", relation_notation=None, target_selector=written_target,
                        source_cardinality=None, target_cardinality=None, written_direction="forward",
                        written_source_selector=written_source, written_target_selector=written_target,
                        written_source_cardinality=None, written_target_cardinality=None,
                    ))
                    continue
            relation = _RELATION.fullmatch(expression)
            if relation is not None and _balanced_parentheses(relation.group("source")) and _balanced_parentheses(relation.group("target")) and not (relation.group("source").rstrip().endswith(":")
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
            allowed_classification = _ALLOWED_CLASSIFICATION_VALUE.fullmatch(expression)
            if allowed_classification is not None:
                records.append(_record(source, expression, "classification_allowed_value",
                                       subject_selector=allowed_classification.group("subject").strip(),
                                       axis=allowed_classification.group("axis").strip(),
                                       value=allowed_classification.group("value").strip()))
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
            minimum = _PROPERTY_MINIMUM.fullmatch(expression)
            if minimum is not None and (minimum_selector := _property_selector(minimum["property"])):
                written_value = minimum["value"]
                value = float(written_value) if "." in written_value else int(written_value)
                records.append(_record(source, expression, "property_value_bound",
                                       property_selector=minimum_selector, operator=">=", value=value))
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
        read_view = carrier_read_view(parsed.metadata)
        atom_id = read_view.get("atom_id")
        version = read_view.get("version")
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
