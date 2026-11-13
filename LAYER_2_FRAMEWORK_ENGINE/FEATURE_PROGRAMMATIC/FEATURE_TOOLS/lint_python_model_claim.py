"""Lint static Python Formal Claims against caller-supplied declarations.

Accepts Python files or Python fences under Claim / Formal Claim in Markdown.
The Model catalog is a JSON address array or an object with addresses and
python_classes bindings. The relation list can be a JSON array or the
Workbench registry object with a registered_names array. References with
complex qualifiers and instance selectors can be unsupported; the checker
validates selector Properties but does not evaluate their conditions. Callers
must provide unresolved symbolic Relation aliases explicitly.
No Claim is executed. A block reports its first problem.
"""
from __future__ import annotations

import argparse
from dataclasses import replace
import ast
import json
from pathlib import Path
import re
import sys
from collections.abc import Collection, Mapping

from markdown_it import MarkdownIt
from python_model_claim import PythonModelClaimError, parse_python_model_claim
from subject_notation import (Name, Path as SubjectPath, Qualification, RelationChain, SelectionGroup, SelectionSuffix,
                              namespace_local_expression, parse_subject_expression, render_subject)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import NativeModelClaimError, parse_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.native_model_lint import lint_native_model_claim


_MEMBERSHIP = re.compile(
    r'/\(\.([A-Za-z_][A-Za-z_0-9. ]*)\s+in\s+'
    r'(?:\((?:[A-Za-z_][A-Za-z_0-9 ,\-]*|"[^"\n]+")\)|RMED)\)'
)
_SINGLETON_MEMBERSHIP = re.compile(
    r'/\(\.([A-Za-z_][A-Za-z_0-9. ]*)\s+in\s+\(([A-Za-z_][A-Za-z_0-9 -]*)\)\)'
)
_PARTICIPANT = re.compile(r'^\$([A-Za-z_]\w*)\[<([A-Za-z_][A-Za-z_0-9 /]*)>(?:,\s*(.+))?\]$')
_PARTICIPANT_PROPERTY = re.compile(r'^\(\.([A-Za-z_][A-Za-z_0-9. ]*?)\s*=\s*[A-Za-z_][A-Za-z_0-9 -]*\)$')
_QUOTED_INSTANCE = re.compile(r'//"([A-Za-z_0-9][A-Za-z_0-9-]*)"')


_QUALIFIED_REQUIREMENT_FORMS = re.compile(
    r"^Atom/\(\.Header\.Context\.Role\s*(?::|:=)\s*Requirement\)"
    r"/\(\.Header\.Context\.Form\s+in\s*\((?P<forms>[^()]*)\)\)"
    r"//(?P<variable>\$[A-Za-z_]\w*)$"
)


def _requirement_form_selection(address: str, exact_addresses: set[str]) -> tuple[str, str] | None:
    """Resolve a finite Requirement Form union only through exact declarations."""
    match = _QUALIFIED_REQUIREMENT_FORMS.fullmatch(address)
    if match is None:
        return None
    forms = [item.strip() for item in match['forms'].split(',')]
    if (not forms or len(forms) != len(set(forms))
            or any(not re.fullmatch(r"[A-Za-z][A-Za-z0-9 ]*", form) for form in forms)):
        return None
    role = _canonical_address("Atom/(.Header.Context.Role := Requirement)")
    if ("Atom.Header.Context.Role" not in exact_addresses
            or role not in exact_addresses
            or role + ".Header.Context.Form" not in exact_addresses):
        return None
    branches = [_canonical_address(role + "/(.Header.Context.Form := " + form + ")")
                for form in forms]
    if any(branch not in exact_addresses for branch in branches):
        return None
    return match['variable'][1:], "union:" + "|".join(sorted(branches))


def _resolve(text: str, declared: set[str], relations: Collection[str], aliases: dict[str, str],
             address_bindings: Mapping[str, str] | None = None) -> bool:
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
        return all(_resolve_path(endpoint, declared, relations, aliases, address_bindings) for endpoint in expression.endpoints)
    return _resolve_path(expression, declared, relations, aliases, address_bindings)


def _resolve_path(expression, declared, relations, aliases, address_bindings=None) -> bool:
    return _resolved_address(expression, declared, relations, aliases, address_bindings) is not None


def _resolved_address(expression, declared, relations, aliases, address_bindings=None) -> str | None:
    if not isinstance(expression, SubjectPath):
        raise ValueError("unsupported qualified reference")
    head = expression.head
    if isinstance(head, SelectionGroup) and not expression.steps:
        return "" if all(_resolve_path(member, declared, relations, aliases, address_bindings) for member in head.members) else None
    if isinstance(head, SubjectPath):
        address = _resolved_address(head, declared, relations, aliases, address_bindings)
        if address is None:
            return None
    elif isinstance(head, Name):
        address = aliases.get(head.value.lstrip("$"), head.value)
        if address_bindings is not None:
            address = address_bindings.get(address, address)
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
            if address_bindings is not None:
                address = address_bindings.get(address, address)
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


def _canonical_address(text: str) -> str:
    expression = parse_subject_expression(text, subject_profile="approved").expression
    return render_subject(namespace_local_expression(expression) or expression)


def _validate_exact_qualifiers(text: str, declared: set[str]) -> None:
    expression = parse_subject_expression(text, subject_profile="approved").expression
    expression = namespace_local_expression(expression) or expression
    if isinstance(expression, RelationChain):
        for endpoint in expression.endpoints:
            _validate_exact_qualifiers(render_subject(endpoint), declared)
        return
    if not isinstance(expression, SubjectPath):
        return
    if isinstance(expression.head, SubjectPath):
        _validate_exact_qualifiers(render_subject(expression.head), declared)
    elif isinstance(expression.head, SelectionGroup):
        for member in expression.head.members:
            _validate_exact_qualifiers(render_subject(member), declared)
    for index, step in enumerate(expression.steps):
        if step.operator != "/" or not isinstance(step.operand, Qualification):
            continue
        relative = step.operand.relative_path
        if not isinstance(relative.head, Name):
            raise ValueError("unsupported qualifier Property")
        name = relative.head.value
        for part in relative.steps:
            if part.operator == "." and isinstance(part.operand, Name):
                name += "." + part.operand.value
            elif part.operator not in (":=", ":"):
                raise ValueError("unsupported qualifier Property")
        parent = render_subject(replace(expression, steps=expression.steps[:index]))
        qualifier = parent + "." + name
        if qualifier not in declared:
            raise ValueError(f"unknown qualifier Property: {qualifier}")


def lint_python_model_claim(text: str, *, declared_addresses: Collection[str],
                            relation_names: Collection[str], path: str = "<claim>",
                            first_line: int = 1,
                            relation_aliases: Mapping[str, str] | None = None,
                            python_class_bindings: Mapping[str, Collection[str]] | None = None,
                            operator_catalog: Mapping[str, Collection[str]] | None = None,
                            require_declared_aliases: bool = False,
                            address_bindings: Mapping[str, str] | None = None,
                            relation_declaration: str | None = None) -> tuple[str, ...]:
    """Return path-and-line diagnostics for a static Python Claim block.

    Address bindings are caller-proven unique aliases to exact declared or
    explicitly projected inherited addresses; they do not create declarations.
    """
    try:
        native = parse_native_model_claim(text)
    except NativeModelClaimError as error:
        message = str(error)
        match = re.match(r"line (\d+), column (\d+): (.*)", message, re.DOTALL)
        if match:
            return (f"{path}:{first_line + int(match[1]) - 1}:{match[2]}: {match[3]}",)
        return (f"{path}:{first_line}: {message}",)
    if native is not None:
        return lint_native_model_claim(native, declared_addresses=declared_addresses,
                                       relation_names=relation_names, path=path, first_line=first_line,
                                       resolve_address=_resolve, simple_address=_simple_address,
                                       canonical_address=_canonical_address,
                                       python_class_bindings=python_class_bindings)
    from ATOM_LIFECYCLE.placement_claim import parse_placement_rules
    try:
        if parse_placement_rules(text) is not None:
            return ()
    except ValueError as error:
        return (f"{path}:{first_line}: {error}",)
    declared = set()
    for address in declared_addresses:
        try:
            declared.add(_simple_address(address))
        except ValueError:
            if python_class_bindings is None and address_bindings is None:
                raise
            _canonical_address(address)
    exact_addresses: set[str] = set()
    if address_bindings is not None:
        if not isinstance(address_bindings, Mapping):
            return (f"{path}:{first_line}: invalid address bindings",)
        exact_addresses = {_canonical_address(address) for address in declared_addresses}
        bound_names: dict[str, str] = {}
        for alias, target in address_bindings.items():
            if not isinstance(alias, str) or not isinstance(target, str):
                return (f"{path}:{first_line}: invalid address binding",)
            try:
                name = _simple_address(alias)
                canonical_target = _canonical_address(target)
            except ValueError:
                return (f"{path}:{first_line}: invalid address binding: {alias}",)
            if (canonical_target not in exact_addresses
                    or (name in exact_addresses and name != canonical_target)
                    or (name in bound_names and bound_names[name] != canonical_target)):
                return (f"{path}:{first_line}: missing or ambiguous address binding: {alias}",)
            try:
                _validate_exact_qualifiers(canonical_target, declared | exact_addresses)
            except ValueError as error:
                return (f"{path}:{first_line}: {error}",)
            bound_names[name] = canonical_target
        for name, target in tuple(bound_names.items()):
            for address in exact_addresses:
                if not address.startswith(target + "."):
                    continue
                projected = name + address[len(target):]
                if projected in exact_addresses or (projected in bound_names and bound_names[projected] != address):
                    continue
                bound_names[projected] = address
        declared.update(bound_names)
        declared.update(exact_addresses)
    bindings: dict[str, str] = {}
    generic = set()
    def validate_reference(address: str) -> bool:
        if any(
            re.search(r"(?<![A-Za-z0-9_])" + re.escape(var) + r"(?![A-Za-z0-9_])", address)
            for var in generic
        ):
            raise ValueError("generic endpoint is scoped to its Relation signature")
        if address_bindings is not None:
            participant = re.fullmatch(r"\$([A-Za-z_]\w*)(\.[A-Za-z_][A-Za-z_0-9. ]*)?", address)
            if participant and bindings.get(participant[1], "").startswith("union:"):
                suffix = participant[2] or ""
                branches = bindings[participant[1]][len("union:"):].split("|")
                return all(branch + suffix in exact_addresses for branch in branches)
            normalized = _SINGLETON_MEMBERSHIP.sub(lambda m: f'/(.{m[1]} := {m[2]})', address)
            try:
                expression = parse_subject_expression(normalized, subject_profile="approved").expression
                local = namespace_local_expression(expression)
                if local is not None and isinstance(expression, RelationChain):
                    local_text = render_subject(local)
                    local_base = re.sub(r'//\$[A-Za-z_]\w*$', '', local_text)
                    if ("/" in local_base and local_base in bound_names
                            and render_subject(expression.endpoints[0]) not in exact_addresses):
                        return False
            except ValueError:
                pass
            if '$' not in normalized:
                try:
                    exact = _canonical_address(normalized) in exact_addresses
                except ValueError:
                    exact = False
                if exact:
                    _validate_exact_qualifiers(normalized, declared)
                    return True
            if ')/' in normalized:
                variable = re.search(r'//(\$[A-Za-z_]\w*)$', normalized)
                base = normalized[:variable.start()] if variable else normalized
                try:
                    canonical = _canonical_address(base)
                except ValueError:
                    return False
                if canonical not in exact_addresses:
                    return False
                _validate_exact_qualifiers(base, declared)
                if variable:
                    name = variable.group(1)[1:]
                    if bindings.get(name, canonical) != canonical:
                        raise ValueError(f"inconsistent binding: ${name}")
                    bindings[name] = canonical
                return True
            try:
                bound_target = bound_names.get(_simple_address(normalized))
            except ValueError:
                bound_target = None
            if bound_target is not None:
                _validate_exact_qualifiers(bound_target, declared)
        return _resolve(address, declared, relation_names, bindings, bound_names if address_bindings is not None else None)
    def validate_relation_endpoint(address: str, name: object, side: str) -> bool:
        if (side == "target" and name == "IS_DECLARED_BY"
                and relation_declaration == "IS_DECLARED_BY" and name in relation_names
                and address_bindings is not None):
            selection = _requirement_form_selection(address, exact_addresses)
            if selection is not None:
                variable, identity = selection
                if f"${variable}" in generic or bindings.get(variable, identity) != identity:
                    raise ValueError(f"inconsistent binding: ${variable}")
                bindings[variable] = identity
                return True
            if (re.fullmatch(r"\$[A-Za-z_]\w*", address)
                    and bindings.get(address[1:], "").startswith("union:")):
                return validate_reference(address)
        if (isinstance(address, str) and re.fullmatch(r"\$[A-Za-z_]\w*", address)
                and name == relation_declaration and name in relation_names):
            if address in generic or address[1:] in bindings:
                raise ValueError("generic endpoint cannot shadow another participant")
            generic.add(address)
            return True
        return validate_reference(address)
    try:
        parse_python_model_claim(text, validate_reference=validate_reference,
                                 validate_relation_endpoint=validate_relation_endpoint)
    except PythonModelClaimError as error:
        message = str(error)
        match = re.match(r"line (\d+), column (\d+): (.*)", message, re.DOTALL)
        if match:
            return (f"{path}:{first_line + int(match[1]) - 1}:{match[2]}: {match[3]}",)
        return (f"{path}:{first_line}: {message}",)
    # The registry supplies names, while callers may supply separately declared aliases.
    known_aliases = {} if require_declared_aliases else {
        "<+": "CONTAINS", ">|": "HAS_CLASSIFICATION", ";>": "IS_ORDERED_RIGHT_BEFORE",
    }
    known_aliases.update(relation_aliases or {})
    for item in ast.parse(text).body:
        call = item.value
        if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name):
            continue
        helper = call.func.id
        args = {kw.arg: ast.literal_eval(kw.value) for kw in call.keywords}
        name = args["name"] if helper == "relation" else None
        if helper == "deliver":
            symbols = (operator_catalog or {}).get("Delivery", ())
            if not isinstance(symbols, (list, tuple)) or tuple(symbols) != (">>",):
                return (f"{path}:{first_line + call.lineno - 1}:{call.col_offset + 1}: missing or ambiguous Delivery operator: >>",)
            continue
        symbol = {"composition": "<+", "classify": ">|", "order_before": ";>"}.get(helper)
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
    yield from _markdown_blocks(text)


def _markdown_blocks(text: str):
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


def _address_catalog(path: Path) -> tuple[list[str], dict[str, list[str]] | None]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value, None
    if not isinstance(value, dict) or set(value) != {"addresses", "python_classes"}:
        raise ValueError(f"{path}: expected an address array or a Model catalog")
    addresses, bindings = value["addresses"], value["python_classes"]
    if (not isinstance(addresses, list) or any(not isinstance(item, str) for item in addresses)
            or not isinstance(bindings, dict)
            or any(not isinstance(name, str) or not name.isidentifier() or not isinstance(targets, list)
                   or not targets or any(not isinstance(target, str) or not target for target in targets)
                   for name, targets in bindings.items())):
        raise ValueError(f"{path}: invalid Model catalog")
    return addresses, bindings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Python Claim files or Markdown carriers")
    parser.add_argument("--addresses", required=True, type=Path, help="JSON address array or Model catalog")
    parser.add_argument("--relations", required=True, type=Path, help="JSON array or Workbench relation registry")
    parser.add_argument("--relation-alias", action="append", default=[], metavar="TOKEN=NAME")
    parser.add_argument("--operators", type=Path, help="JSON operator descriptor-to-symbols catalog")
    args = parser.parse_args(argv)
    try:
        addresses, class_bindings = _address_catalog(args.addresses)
        relations = _names(args.relations, registry=True)
        operators = json.loads(args.operators.read_text(encoding="utf-8")) if args.operators else {}
        if not isinstance(operators, dict) or any(
            not isinstance(name, str) or not isinstance(symbols, list)
            or any(not isinstance(symbol, str) for symbol in symbols)
            for name, symbols in operators.items()
        ):
            raise ValueError("invalid operator catalog")
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
                                   relation_aliases=aliases, python_class_bindings=class_bindings,
                                   operator_catalog=operators))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 2
    for diagnostic in diagnostics:
        print(diagnostic, file=sys.stderr)
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
