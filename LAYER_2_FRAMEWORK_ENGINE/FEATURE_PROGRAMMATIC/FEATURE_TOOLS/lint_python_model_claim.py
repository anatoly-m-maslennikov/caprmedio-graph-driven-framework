"""Lint static Python Formal Claims against caller-supplied declarations.

Accepts Python files or Python fences under Claim / Formal Claim in Markdown.
The address list is a JSON array; the relation list can be a JSON array or the
Workbench registry object with a registered_names array. References with
complex qualifiers and instance selectors can be unsupported; the checker
validates selector Properties but does not evaluate their conditions. Callers
must provide unresolved symbolic Relation aliases explicitly.
No Claim is executed. A block reports its first problem.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys
from collections.abc import Collection, Mapping

from markdown_it import MarkdownIt
from python_model_claim import PythonModelClaimError, parse_python_model_claim
from subject_notation import (Name, Path as SubjectPath, Qualification, RelationChain, SelectionGroup, SelectionSuffix,
                              namespace_local_expression, parse_subject_expression)


_MEMBERSHIP = re.compile(
    r'/\(\.([A-Za-z_][A-Za-z_0-9. ]*)\s+in\s+'
    r'(?:\((?:[A-Za-z_][A-Za-z_0-9 ,\-]*|"[^"\n]+")\)|RMED)\)'
)
_PARTICIPANT = re.compile(r'^\$([A-Za-z_]\w*)\[<([A-Za-z_][A-Za-z_0-9 /]*)>(?:,\s*(.+))?\]$')
_PARTICIPANT_PROPERTY = re.compile(r'^\(\.([A-Za-z_][A-Za-z_0-9. ]*?)\s*=\s*[A-Za-z_][A-Za-z_0-9 -]*\)$')
_QUOTED_INSTANCE = re.compile(r'//"([A-Za-z_0-9][A-Za-z_0-9-]*)"')


def _resolve(text: str, declared: set[str], relations: Collection[str], aliases: dict[str, str]) -> bool:
    """Resolve references and the Properties used in a selector."""
    if participant := _PARTICIPANT.fullmatch(text):
        variable, kind, conditions = participant.groups()
        if kind not in declared or aliases.get(variable, kind) != kind:
            return False
        if conditions:
            for clause in conditions.split(" AND "):
                match = _PARTICIPANT_PROPERTY.fullmatch(clause)
                if match is None:
                    raise ValueError("unsupported participant condition")
                property_address = f"{kind}.{match[1]}"
                if property_address not in declared:
                    raise ValueError(f"unknown participant Property: {property_address}")
        aliases[variable] = kind
        return True
    # The Subject resolver admits a single qualifier value. For reference
    # checking a membership qualifier selects the same Property.
    text = _MEMBERSHIP.sub(lambda match: f'/(.{match[1]} := Value)', text)
    text = _QUOTED_INSTANCE.sub(r"//\1", text)
    if text.endswith(".*"):
        text += "*"
    expression = parse_subject_expression(text, subject_profile="approved").expression
    expression = namespace_local_expression(expression) or expression
    if isinstance(expression, RelationChain):
        return all(_resolve_path(endpoint, declared, relations, aliases) for endpoint in expression.endpoints)
    return _resolve_path(expression, declared, relations, aliases)


def _resolve_path(expression, declared, relations, aliases) -> bool:
    return _resolved_address(expression, declared, relations, aliases) is not None


def _resolved_address(expression, declared, relations, aliases) -> str | None:
    if not isinstance(expression, SubjectPath):
        raise ValueError("unsupported qualified reference")
    head = expression.head
    if isinstance(head, SelectionGroup) and not expression.steps:
        return "" if all(_resolve_path(member, declared, relations, aliases) for member in head.members) else None
    if isinstance(head, SubjectPath):
        address = _resolved_address(head, declared, relations, aliases)
        if address is None:
            return None
    elif isinstance(head, Name):
        address = aliases.get(head.value.lstrip("$"), head.value)
    else:
        raise ValueError("unsupported qualified reference")
    qualifiers = []
    named_instance = False
    for index, step in enumerate(expression.steps):
        if step.operator == "." and isinstance(step.operand, Name):
            address += "." + step.operand.value
            named_instance = False
        elif step.operator == "." and isinstance(step.operand, SelectionSuffix) and index == len(expression.steps) - 1:
            pass  # Wildcard selects descendants of the declared base.
        elif step.operator == "/" and isinstance(step.operand, Qualification):
            relative = step.operand.relative_path
            if not isinstance(relative.head, Name):
                raise ValueError("unsupported qualifier Property")
            property_name = relative.head.value
            for substep in relative.steps:
                if substep.operator == "." and isinstance(substep.operand, Name):
                    property_name += "." + substep.operand.value
                elif substep.operator not in (":=", ":"):
                    raise ValueError("unsupported qualifier Property")
            qualifiers.append(address + "." + property_name)
        elif step.operator == "/" and isinstance(step.operand, Name):
            address += "/" + step.operand.value
        elif step.operator == "//" and isinstance(step.operand, Name):
            instance = step.operand.value
            if instance.startswith("$"):
                if aliases.get(instance[1:], address) != address:
                    raise ValueError(f"inconsistent binding: {instance}")
                aliases[instance[1:]] = address
            elif address == "Relation" and index == len(expression.steps) - 1:
                return address if instance in relations else None
            else:
                if f"{address}//{instance}" not in declared:
                    raise ValueError(f"unknown instance: {address}//{instance}")
                named_instance = True
        elif step.operator == "//" and isinstance(step.operand, SelectionSuffix):
            continue
        else:
            raise ValueError("unsupported qualified reference")
    for qualifier in qualifiers:
        if qualifier not in declared:
            raise ValueError(f"unknown qualifier Property: {qualifier}")
    return address if named_instance or address in declared else None


def _simple_address(text: str) -> str:
    expression = parse_subject_expression(text, subject_profile="approved").expression
    expression = namespace_local_expression(expression) or expression
    if not isinstance(expression, SubjectPath) or not isinstance(expression.head, Name):
        raise ValueError(f"unsupported declared address: {text}")
    address = expression.head.value
    for step in expression.steps:
        if step.operator not in (".", "/", "//") or not isinstance(step.operand, Name):
            raise ValueError(f"unsupported declared address: {text}")
        address += step.operator + step.operand.value
    return address


def lint_python_model_claim(text: str, *, declared_addresses: Collection[str],
                            relation_names: Collection[str], path: str = "<claim>",
                            first_line: int = 1,
                            relation_aliases: Mapping[str, str] | None = None) -> tuple[str, ...]:
    """Return path-and-line diagnostics for a static Python Claim block."""
    declared = {_simple_address(address) for address in declared_addresses}
    bindings: dict[str, str] = {}
    def validate_reference(address: str) -> bool:
        return _resolve(address, declared, relation_names, bindings)
    try:
        parse_python_model_claim(text, validate_reference=validate_reference)
    except PythonModelClaimError as error:
        message = str(error)
        match = re.match(r"line (\d+), column (\d+): (.*)", message, re.DOTALL)
        if match:
            return (f"{path}:{first_line + int(match[1]) - 1}:{match[2]}: {match[3]}",)
        return (f"{path}:{first_line}: {message}",)
    # The registry supplies names, while callers may supply separately declared aliases.
    known_aliases = {"<+": "CONTAINS", ">|": "HAS_CLASSIFICATION", ";>": "IS_ORDERED_RIGHT_BEFORE"}
    known_aliases.update(relation_aliases or {})
    for item in ast.parse(text).body:
        call = item.value
        if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name):
            continue
        helper = call.func.id
        args = {kw.arg: ast.literal_eval(kw.value) for kw in call.keywords}
        name = args["name"] if helper == "relation" else None
        symbol = {"composition": "<+", "classify": ">|", "order_before": ";>", "deliver": ">>"}.get(helper)
        if helper == "classify" and args.get("notation") == "relation":
            name, symbol = "HAS_CLASSIFICATION", None
        if symbol:
            name = known_aliases.get(symbol)
            if not name:
                return (f"{path}:{first_line + call.lineno - 1}:{call.col_offset + 1}: unresolved Relation alias: {symbol}",)
        if name and name != "*" and name not in relation_names:
            return (f"{path}:{first_line + call.lineno - 1}:{call.col_offset + 1}: unknown Relation: {name}",)
    return ()


def _blocks(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".py":
        yield text, 1
        return
    headings: list[tuple[int, str]] = []
    tokens = MarkdownIt("commonmark").parse(text)
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            level = int(token.tag[1:])
            headings = [(n, name) for n, name in headings if n < level]
            headings.append((level, tokens[index + 1].content.strip().casefold()))
        elif token.type == "fence" and token.info.strip().casefold() == "python":
            if tuple(name for _, name in headings[-2:]) == ("claim", "formal claim"):
                yield token.content, token.map[0] + 2


def _names(path: Path, *, registry: bool = False) -> list[str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if registry and isinstance(value, dict):
        names = value.get("registered_names")
        aliases = value.get("inverse_aliases", [])
        if not isinstance(names, list) or not isinstance(aliases, list) or any(not isinstance(item, dict) or not isinstance(item.get("alias"), str)
                                                or item.get("canonical") not in names for item in aliases):
            raise ValueError(f"{path}: invalid inverse alias registry")
        value = names + [item["alias"] for item in aliases]
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{path}: expected a JSON array of strings" + (" or Workbench relation registry" if registry else ""))
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Python Claim files or Markdown carriers")
    parser.add_argument("--addresses", required=True, type=Path, help="JSON array of declared model addresses")
    parser.add_argument("--relations", required=True, type=Path, help="JSON array or Workbench relation registry")
    parser.add_argument("--relation-alias", action="append", default=[], metavar="TOKEN=NAME")
    args = parser.parse_args(argv)
    try:
        addresses = _names(args.addresses)
        relations = _names(args.relations, registry=True)
        aliases = {}
        for entry in args.relation_alias:
            token, separator, name = entry.partition("=")
            if not separator or not token or not name:
                raise ValueError(f"invalid Relation alias: {entry}")
            aliases[token] = name
        diagnostics = []
        for path in args.paths:
            for block, first_line in _blocks(path):
                diagnostics.extend(lint_python_model_claim(block, declared_addresses=addresses,
                                   relation_names=relations, path=str(path), first_line=first_line,
                                   relation_aliases=aliases))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 2
    for diagnostic in diagnostics:
        print(diagnostic, file=sys.stderr)
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
