"""Read declarative Python model Claims without executing their contents."""

from __future__ import annotations

import ast
import io
import json
from pathlib import Path
import re
import sys
import tokenize
from collections.abc import Callable


class PythonModelClaimError(ValueError):
    """A Python model Claim contains invalid or unsupported syntax."""


_COUNT = re.compile(r"(?:0|[1-9][0-9]*)(?:\+|\.\.(?:0|[1-9][0-9]*))?\Z")
_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_ -]*\Z")
_RELATION = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\Z")
_BARE_VALUE = re.compile(r"[A-Za-z_][A-Za-z0-9_ -]*\Z")
_FUNCTIONS = {
    "property_rule": ({"address"}, {"address", "value_format", "occurrences", "values"}),
    "allowed_children": ({"address", "names", "occurrences"},
                         {"address", "names", "occurrences", "name_format"}),
    "order_before": ({"first", "second"}, {"first", "second"}),
    "allowed_values": ({"address", "values"}, {"address", "values", "occurrences", "quoted"}),
    "children": ({"address", "occurrences"}, {"address", "occurrences", "name_format", "recursive"}),
    "composition": ({"container", "parts"}, {"container", "parts"}),
    "deliver": ({"source", "carrier"}, {"source", "carrier"}),
    "classify": ({"address", "axis", "value"}, {"address", "axis", "value", "grouped", "notation"}),
    "path_template": ({"address", "template"}, {"address", "template"}),
    "copy_value": ({"address", "source"}, {"address", "source"}),
    "minimum_value": ({"address", "minimum"}, {"address", "minimum"}),
    "unique": ({"population", "keys"}, {"population", "keys"}),
    "population": ({"address", "count"}, {"address", "count"}),
    "allow_roles_for_form": ({"form", "roles"}, {"form", "roles", "participant"}),
    "relation": ({"source", "name"}, {"source", "name", "target", "source_count", "target_count", "reverse"}),
    "set_value": ({"address", "value"}, {"address", "value"}),
    "subject_path": ({"address"}, {"address"}),
}


def _error(node: ast.AST, message: str) -> PythonModelClaimError:
    return PythonModelClaimError(f"line {node.lineno}, column {node.col_offset + 1}: {message}")


def _text(value: object, label: str, node: ast.AST, *, empty: bool = False) -> str:
    if not isinstance(value, str) or (not empty and not value.strip()) or value != value.strip():
        raise _error(node, f"{label} must be a {'string' if empty else 'nonempty string'}")
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise _error(node, f"{label} contains a control character")
    return value


def _reference(value: object, label: str, node: ast.AST,
               validate_reference: Callable[[str], object] | None) -> str:
    text = _text(value, label, node)
    if any(char in text for char in ";#\\{}\n\r`") or "::" in text or re.search(r"\(\s*\(", text):
        raise _error(node, f"{label} contains an unsupported character")
    if not re.fullmatch(r"[\w\s.*/():=,!'\"<>|+@$\[\]-]+", text):
        raise _error(node, f"{label} contains an unsupported character")
    _check_delimiters(text, label, node)
    if validate_reference is not None:
        try:
            valid = validate_reference(text)
        except (ValueError, LookupError) as error:
            raise _error(node, f"invalid {label}: {error}") from error
        if valid is False:
            raise _error(node, f"unknown {label}: {text}")
    return text


def _check_delimiters(text: str, label: str, node: ast.AST) -> None:
    stack: list[str] = []
    quote = None
    for char in text:
        if quote:
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack.pop() != {')': '(', ']': '['}[char]:
                raise _error(node, f"{label} has unbalanced delimiters")
    if quote or stack:
        raise _error(node, f"{label} has unbalanced delimiters")


def _count(value: object, label: str, node: ast.AST) -> str:
    text = _text(value, label, node)
    if not _COUNT.fullmatch(text):
        raise _error(node, f"{label} is not a cardinality")
    if ".." in text:
        minimum, maximum = (int(number) for number in text.split(".."))
        if minimum > maximum:
            raise _error(node, f"{label} has a reversed range")
    return text


def _name(value: object, label: str, node: ast.AST) -> str:
    text = _text(value, label, node)
    if not _NAME.fullmatch(text):
        raise _error(node, f"{label} must be a name")
    return text


def _literal(value: object, node: ast.AST) -> str:
    text = _text(value, "value", node)
    return text if _BARE_VALUE.fullmatch(text) else json.dumps(text, ensure_ascii=False)


def _items(value: object, label: str, node: ast.AST) -> tuple:
    if not isinstance(value, tuple) or not value:
        raise _error(node, f"{label} must be a nonempty tuple")
    if len(value) != len(set(item for item in value if isinstance(item, str))):
        raise _error(node, f"{label} must contain distinct strings")
    return value


def _optional_count(args: dict, key: str, node: ast.AST) -> str:
    value = args.get(key)
    return "" if value is None else f"{{::{_count(value, key, node)}}}"


def _render_layout(name: str, args: dict, node: ast.AST, ref: Callable[[str], str]) -> str:
    if name == "deliver":
        return f"{ref('source')} >> {ref('carrier')}"
    if name == "copy_value":
        return f"{ref('address')} == {ref('source')}"
    if name == "minimum_value":
        minimum = args["minimum"]
        if type(minimum) is not int:
            raise _error(node, "minimum must be an integer")
        return f"{ref('address')} >= {minimum}"
    if name == "population":
        return f"{ref('address')}{_optional_count(args, 'count', node)}"
    if name == "path_template":
        template = json.dumps(_text(args["template"], "template", node), ensure_ascii=False)
        return f"{ref('address')} == PATH_TEMPLATE({template})"
    if name == "children":
        name_format = args.get("name_format", "")
        if name_format not in ("", "string"):
            _reference(name_format, "name_format", node, None)
        recursive = args.get("recursive", False)
        if type(recursive) is not bool:
            raise _error(node, "recursive must be a boolean")
        wildcard = "**" if recursive else "*"
        return f"{ref('address')}.{wildcard}[{name_format}]{_optional_count(args, 'occurrences', node)}"
    axis = _name(args["axis"], "axis", node)
    value = args["value"]
    if type(value) is int:
        value = str(value)
    else:
        value = _literal(value, node)
    grouped = args.get("grouped", False)
    if type(grouped) is not bool:
        raise _error(node, "grouped must be a boolean")
    notation = args.get("notation", "assignment")
    if notation == "relation" and not grouped:
        return f"{ref('address')} ((HAS_CLASSIFICATION)) {axis} == {value}"
    if notation not in ("assignment", "allowed"):
        raise _error(node, "notation must be 'assignment', 'allowed', or 'relation' without grouping")
    assignment = f"{axis} == {value}" if notation == "assignment" else f"{axis}: {value}"
    return f"{ref('address')} >| " + (f"({assignment})" if grouped else assignment)


def _render(name: str, args: dict, node: ast.AST,
            validate_reference: Callable[[str], object] | None,
            validate_relation_endpoint: Callable[[str, object, str], object] | None = None) -> tuple[str, ...]:
    def ref(key: str) -> str:
        return _reference(args[key], key, node, validate_reference)

    if name == "composition":
        parts = args["parts"]
        if not isinstance(parts, tuple) or not parts:
            raise _error(node, "parts must be a nonempty tuple")
        return (" <+ ".join([ref("container"), *(
            _reference(part, "part", node, validate_reference) for part in parts
        )]),)

    if name == "unique":
        keys = ", ".join(_reference(key, "key", node, None) for key in _items(args["keys"], "keys", node))
        return (f"UNIQUE({ref('population')}, ({keys}))",)

    if name == "allow_roles_for_form":
        participant = _text(args.get("participant", "a"), "participant", node)
        if not _RELATION.fullmatch(participant):
            raise _error(node, "participant must be an identifier")
        form = _name(args["form"], "form", node)
        roles = ", ".join(_name(role, "role", node) for role in _items(args["roles"], "roles", node))
        for address in ("Atom", "Atom.Header.Context.Form", "Atom.Header.Context.Role"):
            _reference(address, "address", node, validate_reference)
        return (f"FOR EACH ${participant}[<Atom>, (.Header.Context.Form = {form})]: "
                f"(${participant}.Header.Context.Role:: [in ({roles})]{{::1}})",)

    if name in {"children", "copy_value", "deliver", "classify", "path_template", "minimum_value", "population"}:
        return (_render_layout(name, args, node, ref),)

    if name == "property_rule":
        address = ref("address")
        occurrence = _optional_count(args, "occurrences", node)
        value_count = _optional_count(args, "values", node)
        raw_format = args.get("value_format")
        if raw_format is None and not value_count:
            if occurrence:
                return (f"{address}{occurrence}",)
            raise _error(node, "property_rule requires a constraint")
        if raw_format is None:
            format_text = ""
        else:
            format_text = _text(raw_format, "value_format", node, empty=True)
            if format_text and not re.fullmatch(r"[A-Za-z0-9_,. +()/$-]+", format_text):
                raise _error(node, "value_format contains an unsupported character")
            format_text = f" [{format_text}]"
        return (f"{address}{occurrence}::{format_text}{value_count}",)

    if name == "allowed_children":
        address = ref("address")
        names = tuple(_name(item, "child name", node) for item in _items(args["names"], "names", node))
        name_format = args.get("name_format")
        if name_format is not None and name_format != "string":
            raise _error(node, "name_format must be 'string'")
        prefix = "string, " if name_format else ""
        return (f"{address}.*[{prefix}in ({', '.join(names)})]{{::{_count(args['occurrences'], 'occurrences', node)}}}",)

    if name == "order_before":
        return (f"{ref('first')} ;> {ref('second')}",)

    if name == "allowed_values":
        address = ref("address")
        quoted = args.get("quoted", False)
        if type(quoted) is not bool:
            raise _error(node, "quoted must be a boolean")
        values = tuple(
            json.dumps(_text(item, "value", node), ensure_ascii=False) if quoted else _literal(item, node)
            for item in _items(args["values"], "values", node)
        )
        count = _optional_count(args, "occurrences", node)
        if count:
            return (f"{address}:: [in ({', '.join(values)})]{count}",)
        return tuple(f"{address} :: {value}" for value in values)

    if name == "subject_path":
        return (ref("address"),)

    if name == "set_value":
        address = _text(args["address"], "address", node)
        if re.match(r"alias\s*\(", address):
            match = re.fullmatch(r"alias\(Relation//([A-Za-z_][A-Za-z0-9_]*)\)", address)
            if match is None:
                raise _error(node, "invalid Relation alias address")
            _reference("Relation//" + match[1], "address", node, validate_reference)
            value = args["value"]
            if not isinstance(value, str):
                raise _error(node, "Relation alias must be a nonempty string")
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except (ValueError, TypeError) as error:
                    raise _error(node, "value must be a valid quoted string") from error
            literal = json.dumps(_text(value, "Relation alias", node), ensure_ascii=False)
            return (f"{address} == {literal}",)
        address = ref("address")
        value = args["value"]
        if type(value) is bool:
            literal = str(value).lower()
        elif type(value) is int:
            literal = str(value)
        elif isinstance(value, str):
            if value.startswith('"'):
                try:
                    decoded = json.loads(value)
                except (ValueError, TypeError) as error:
                    raise _error(node, "value must be a valid quoted string") from error
                literal = json.dumps(_text(decoded, "value", node, empty=True), ensure_ascii=False)
            else:
                literal = _literal(value, node)
        else:
            raise _error(node, "value must be a string, integer, or boolean")
        return (f"{address} == {literal}",)

    def endpoint(key):
        if validate_relation_endpoint is None:
            check = validate_reference
        else:
            check = lambda value: validate_relation_endpoint(value, args.get("name"), key)
        return _reference(args[key], key, node, check)

    source = endpoint("source")
    relation_name = _text(args["name"], "name", node)
    if relation_name != "*" and not _RELATION.fullmatch(relation_name):
        raise _error(node, "name must be a Relation name")
    source_count = _optional_count(args, "source_count", node)
    target_count = _optional_count(args, "target_count", node)
    target = f" {endpoint('target')}" if args.get("target") is not None else ""
    if target_count and not target:
        raise _error(node, "target_count requires target")
    reverse = args.get("reverse", False)
    if type(reverse) is not bool:
        raise _error(node, "reverse must be a boolean")
    operator = "<" if reverse else ""
    return (f"{source} {source_count}{operator}(({relation_name})){target_count}{target}",)


def parse_grouped_python_model_claim(
    text: str, *, validate_reference: Callable[[str], object] | None = None,
    validate_relation_endpoint: Callable[[str, object, str], object] | None = None,
) -> tuple[tuple[str, str | None], ...]:
    """Return statements with their preceding top-level model/instances marker."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if validate_reference is not None and not callable(validate_reference):
        raise TypeError("validate_reference must be callable")
    try:
        tree = ast.parse(text, mode="exec")
    except SyntaxError as error:
        raise PythonModelClaimError(f"line {error.lineno}, column {error.offset}: {error.msg}") from error
    markers: list[tuple[int, str]] = []
    depth = 0
    for token in tokenize.generate_tokens(io.StringIO(text).readline):
        if token.type == tokenize.OP and token.string in "([{":
            depth += 1
        elif token.type == tokenize.OP and token.string in ")]}":
            depth -= 1
        elif token.type == tokenize.COMMENT and depth == 0 and token.line.lstrip().startswith("#"):
            label = token.string[1:].strip().casefold()
            if label in {"model", "instances"}:
                markers.append((token.start[0], label))
    statements: list[tuple[str, str | None]] = []
    for item in tree.body:
        if not isinstance(item, ast.Expr) or not isinstance(item.value, ast.Call):
            raise _error(item, "expected a declarative function call")
        call = item.value
        if not isinstance(call.func, ast.Name) or call.func.id not in _FUNCTIONS:
            raise _error(item, "unknown declarative function")
        name = call.func.id
        if call.args or any(keyword.arg is None for keyword in call.keywords):
            raise _error(item, "only named literal arguments are supported")
        args = {}
        for keyword in call.keywords:
            if keyword.arg in args:
                raise _error(keyword, f"duplicate argument: {keyword.arg}")
            try:
                args[keyword.arg] = ast.literal_eval(keyword.value)
            except (ValueError, TypeError, SyntaxError, RecursionError) as error:
                raise _error(keyword, f"{keyword.arg} must be a literal") from error
        required, allowed = _FUNCTIONS[name]
        missing = required - args.keys()
        unexpected = args.keys() - allowed
        if missing:
            raise _error(item, f"missing arguments: {', '.join(sorted(missing))}")
        if unexpected:
            raise _error(item, f"unexpected arguments: {', '.join(sorted(unexpected))}")
        group = next((label for line, label in reversed(markers) if line < item.lineno), None)
        statements.extend((statement, group) for statement in _render(name, args, item, validate_reference, validate_relation_endpoint))
    if not statements:
        raise PythonModelClaimError("line 1, column 1: expected a declarative function call")
    return tuple(statements)


def parse_python_model_claim(
    text: str, *, validate_reference: Callable[[str], object] | None = None,
    validate_relation_endpoint: Callable[[str, object, str], object] | None = None,
) -> tuple[str, ...]:
    """Return compatible statements without evaluating the source text.

    The optional callback checks each address and may return False or raise
    ValueError/LookupError to reject an unknown reference.
    """
    return tuple(statement for statement, _group in
                 parse_grouped_python_model_claim(text, validate_reference=validate_reference, validate_relation_endpoint=validate_relation_endpoint))


def compile_python_model_claim(text: str, *, model_class_bindings=None) -> tuple[str, ...]:
    """Read either Python declaration format for the existing schema compilers."""
    programmatic = str(Path(__file__).resolve().parents[1])
    if programmatic not in sys.path:
        sys.path.insert(0, programmatic)
    from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import (
        compiler_model_statements, compile_atom_dependencies_with_check, compile_scope_level_with_check,
    )
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim

    native = parse_native_model_claim(text)
    if native is None:
        return parse_python_model_claim(text)
    if native.get("instance_check") is not None:
        if native["instance_check"]["name"] == "dependencies_are_distinct":
            statements, _metadata = compile_atom_dependencies_with_check(native, model_class_bindings=model_class_bindings)
        else:
            statements, _metadata = compile_scope_level_with_check(native)
        return statements
    return compiler_model_statements(native, model_class_bindings=model_class_bindings)


def compile_atom_dependencies_claim_with_check(text: str, *, model_class_bindings=None):
    """Compile the explicit Atom Dependencies consumer's reviewed-callback input."""
    programmatic = str(Path(__file__).resolve().parents[1])
    if programmatic not in sys.path:
        sys.path.insert(0, programmatic)
    from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compile_atom_dependencies_with_check
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim

    native = parse_native_model_claim(text)
    if native is None:
        raise ValueError("Atom Dependencies requires a native declaration")
    return compile_atom_dependencies_with_check(native, model_class_bindings=model_class_bindings)
