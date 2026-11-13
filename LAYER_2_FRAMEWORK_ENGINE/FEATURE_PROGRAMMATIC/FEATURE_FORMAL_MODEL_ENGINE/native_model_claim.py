"""Read Python Model Declarations without importing or executing authored code."""

from __future__ import annotations

import ast
import re
from typing import Any


class NativeModelClaimError(ValueError):
    """A native Model Claim cannot be read safely."""


_DECLARATIONS = {"declare_entity": "entity", "declare_relation": "relation"}
_BUILTINS = {"str", "int", "bool", "float", "bytes", "list", "tuple", "dict", "set", "object"}
_IMPORTS = {
    "caprmedio.formal_claims": {"declare_entity", "declare_relation", "Cardinality"},
    "datetime": {"date", "datetime", "time", "timedelta"},
    "dataclasses": {"dataclass", "field"},
    "typing": {"Annotated", "ClassVar", "Literal", "Optional"},
    "__future__": {"annotations"},
}
_COUNT_KEYS = {
    "property_occurrence_cardinality", "value_cardinality",
    "dependent_property_cardinality", "dependent_property_value_cardinality",
    "recursive_dependent_property_cardinality", "instance_population_cardinality",
    "targets_per_source", "sources_per_target",
}
_ENDPOINT_KEYS = {
    "level", "entity_paths", "reference_form", "dependency", "classification_axis",
    "ephemeral", "address_form",
}
_ENDPOINT_LEVELS = {"model_entities", "instances", "model_entities_or_instances"}

_DECLARATION_KEYS = {
    "declare_entity": {
        "entity_name", "entity_class", "instance", "instance_check", "qualification_property_path", "incoming_model_relations", "structure_paths", "aspect_memberships",
        "relation_name", "base_path", "value_format", "value_cardinality", "property_occurrence_cardinality",
        "dependent_property_cardinality", "dependent_property_name_format", "dependent_property_value_format",
        "dependent_property_value_cardinality",
        "recursive_dependent_property_cardinality", "recursive_dependent_property_name_format",
        "recursive_dependent_property_value_format", "ordered_dependent_property_roles",
        "allowed_dependent_property_names", "ordered_dependent_property_pairs", "allowed_values", "minimum_value", "applies_to_entity_classes",
        "instance_population_cardinality", "instance_population_scope", "population_entity_path", "population_functional_dependencies", "population_unique_constraints", "classifications", "allowed_classification_values", "fallback_property_name", "fallback_value", "fallback_chain", "maximum_value",
        "required_instance_property_values", "instance_property_constraints", "model_relation_constraints",
        "instance_relation_constraints", "status_order_numbers", "applies_to_role", "applies_to_forms", "status_groups",
    },
    "declare_relation": {
        "relation_name", "source_endpoint", "target_endpoint", "endpoint_pairs", "inverse_alias", "written_alias",
        "reverse_written_alias", "targets_per_source", "sources_per_target", "acyclic",
        "same_immediate_bearer", "swap_endpoints", "swap_endpoint_cardinalities",
    },
}
_RELATION_CONSTRAINT_KEYS = {"target_entity_paths", "targets_per_source", "sources_per_target"}
_PROPERTY_CONSTRAINT_KEYS = {"value_cardinality"}


def _fail(node: ast.AST, message: str) -> None:
    raise NativeModelClaimError(
        f"line {getattr(node, 'lineno', 1)}, column {getattr(node, 'col_offset', 0) + 1}: {message}"
    )


def _keywords(call: ast.Call) -> dict[str, ast.AST]:
    if call.args:
        _fail(call, "only named arguments are supported")
    result: dict[str, ast.AST] = {}
    for keyword in call.keywords:
        if keyword.arg is None:
            _fail(keyword, "expanded keyword arguments are unsupported")
        if keyword.arg in result:
            _fail(keyword, f"duplicate argument: {keyword.arg}")
        result[keyword.arg] = keyword.value
    return result


def _dictionary(node: ast.Dict, names: set[str]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in zip(node.keys, node.values, strict=True):
        if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
            _fail(node, "dictionary keys must be literal strings")
        if key.value in result:
            _fail(key, f"duplicate dictionary key: {key.value}")
        result[key.value] = _value(value, names)
    return result


def _cardinality(node: ast.Call, names: set[str]) -> dict[str, int | None]:
    if "Cardinality" not in names:
        _fail(node, "Cardinality must be imported")
    arguments = _keywords(node)
    if set(arguments) != {"minimum", "maximum"}:
        _fail(node, "Cardinality requires minimum and maximum")
    minimum = _value(arguments["minimum"], names)
    maximum = _value(arguments["maximum"], names)
    if type(minimum) is not int or minimum < 0:
        _fail(node, "Cardinality minimum must be a nonnegative integer")
    if maximum is not None and (type(maximum) is not int or maximum < minimum):
        _fail(node, "Cardinality maximum must be at least minimum or None")
    return {"minimum": minimum, "maximum": maximum}


def _validate_cardinalities(value: Any, node: ast.AST) -> None:
    if isinstance(value, (tuple, list)):
        for item in value:
            _validate_cardinalities(item, node)
    elif isinstance(value, dict):
        for key, item in value.items():
            if key in _COUNT_KEYS:
                exact = type(item) is int and item >= 0
                bounded = (
                    isinstance(item, dict) and set(item) == {"minimum", "maximum"}
                    and type(item["minimum"]) is int and item["minimum"] >= 0
                    and (item["maximum"] is None or (
                        type(item["maximum"]) is int and item["maximum"] >= item["minimum"]
                    ))
                )
                if not (exact or bounded):
                    _fail(node, f"invalid {key} cardinality")
            else:
                _validate_cardinalities(item, node)


def _validate_endpoint(value: Any, label: str, node: ast.AST) -> None:
    if not isinstance(value, dict) or set(value) - _ENDPOINT_KEYS:
        _fail(node, f"{label} must be a supported endpoint mapping")
    if value.get("level") not in _ENDPOINT_LEVELS:
        _fail(node, f"{label} requires an admitted level")
    if "entity_paths" in value:
        paths = value["entity_paths"]
        if (not isinstance(paths, (list, tuple)) or not paths
                or any(not isinstance(path, str) or not path.strip() or path != path.strip()
                       for path in paths)):
            _fail(node, f"{label} entity_paths must be nonempty paths")
    for key in ("reference_form", "dependency", "address_form"):
        if key in value and (not isinstance(value[key], str) or not value[key].strip()):
            _fail(node, f"{label} {key} must be a nonempty string")
    for key in ("classification_axis", "ephemeral"):
        if key in value and type(value[key]) is not bool:
            _fail(node, f"{label} {key} must be a boolean")


def _value(node: ast.AST, names: set[str]) -> Any:  # noqa: C901
    if isinstance(node, ast.Constant):
        if node.value is None or type(node.value) in {str, int, float, bool}:
            return node.value
    if isinstance(node, ast.Name):
        if node.id in names or node.id in _BUILTINS:
            return node.id
        _fail(node, f"unbound symbol: {node.id}")
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        number = _value(node.operand, names)
        if type(number) in {int, float}:
            return -number
    if isinstance(node, (ast.Tuple, ast.List)):
        values = [_value(value, names) for value in node.elts]
        return tuple(values) if isinstance(node, ast.Tuple) else values
    if isinstance(node, ast.Dict):
        return _dictionary(node, names)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "Cardinality":
        return _cardinality(node, names)
    _fail(node, "unsupported expression")


def _annotation(node: ast.AST, names: set[str]) -> str:
    """Validate and preserve an annotation without evaluating forward references."""
    if isinstance(node, ast.Name):
        if node.id not in names and node.id not in _BUILTINS:
            _fail(node, f"unbound annotation: {node.id}")
    elif isinstance(node, ast.Constant):
        if node.value is not None and not isinstance(node.value, (str, int, bool)):
            _fail(node, "unsupported annotation literal")
    elif isinstance(node, ast.Subscript):
        _annotation(node.value, names)
        _annotation(node.slice, names)
    elif isinstance(node, ast.Tuple):
        for part in node.elts:
            _annotation(part, names)
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        _annotation(node.left, names)
        _annotation(node.right, names)
    else:
        _fail(node, "unsupported annotation")
    return ast.unparse(node)


def _field(node: ast.AnnAssign, names: set[str]) -> dict[str, Any]:
    if not isinstance(node.target, ast.Name) or node.simple != 1:
        _fail(node, "field must be a simple annotated name")
    result: dict[str, Any] = {"name": node.target.id, "annotation": _annotation(node.annotation, names)}
    if node.value is None:
        return result
    if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "field":
        if "field" not in names:
            _fail(node, "field must be imported")
        options = _keywords(node.value)
        if set(options) - {"default", "default_factory", "metadata", "kw_only"}:
            _fail(node, "unsupported field argument")
        if "default" in options and "default_factory" in options:
            _fail(node, "field has both default and default_factory")
        if "default_factory" in options:
            factory = options["default_factory"]
            if not isinstance(factory, ast.Name) or factory.id not in {"list", "dict", "set", "tuple"}:
                _fail(factory, "default_factory must be a collection type")
        result["field"] = {key: _value(value, names) for key, value in options.items()}
    else:
        result["default"] = _value(node.value, names)
    return result


def _class(node: ast.ClassDef, names: set[str]) -> dict[str, Any]:  # noqa: C901
    if node.keywords:
        _fail(node, "class keyword arguments are unsupported")
    bases = []
    for base in node.bases:
        if not isinstance(base, ast.Name) or base.id not in names | _BUILTINS:
            _fail(base, "class base must be an imported or declared class")
        bases.append(base.id)
    decorators = []
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Name) and decorator.id == "dataclass" and "dataclass" in names:
            decorators.append({})
        elif (isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name)
              and decorator.func.id == "dataclass" and "dataclass" in names):
            options = _keywords(decorator)
            if set(options) - {"frozen", "kw_only", "slots"}:
                _fail(decorator, "unsupported dataclass option")
            values = {key: _value(value, names) for key, value in options.items()}
            if any(type(value) is not bool for value in values.values()):
                _fail(decorator, "dataclass options must be booleans")
            decorators.append(values)
        else:
            _fail(decorator, "unsupported class decorator")
    if len(decorators) > 1:
        _fail(node, "duplicate dataclass decorator")
    fields = []
    for item in node.body:
        if isinstance(item, ast.Pass):
            continue
        if isinstance(item, ast.AnnAssign):
            fields.append(_field(item, names | {node.name}))
            continue
        _fail(item, "class body supports annotated fields and pass")
    if len({field["name"] for field in fields}) != len(fields):
        _fail(node, "duplicate class field")
    return {"name": node.name, "bases": tuple(bases), "fields": tuple(fields),
            "dataclass": decorators[0] if decorators else None}


def _instance_check(node: ast.FunctionDef, names: set[str], text: str) -> dict[str, Any]:
    args = node.args
    if (node.decorator_list or node.type_comment or args.posonlyargs or args.vararg or args.kwarg
            or args.kwonlyargs or args.defaults or args.kw_defaults or len(args.args) != 1):
        _fail(node, "instance check requires one typed argument without defaults or decorators")
    parameter = args.args[0]
    if (not isinstance(parameter.annotation, ast.Name) or parameter.annotation.id not in names
            or not isinstance(node.returns, ast.Name) or node.returns.id != "bool"):
        _fail(node, "instance check requires a bound Model type and bool return")
    return {
        "name": node.name,
        "parameter": parameter.arg,
        "parameter_type": parameter.annotation.id,
        "source": ast.get_source_segment(text, node),
        "line": node.lineno,
    }


def validate_aspect_instance(args: dict[str, Any]) -> str:
    """Return the canonical full address of a bounded Aspect declaration."""
    import subject_notation as notation

    message = "Aspect instance requires only entity_name and a matching full Project Structure address"
    if not isinstance(args, dict) or set(args) != {"entity_name", "instance"}:
        raise ValueError(message)
    instance = args["instance"]
    if not isinstance(instance, dict) or set(instance) != {"type", "fields"} or instance["type"] != "Aspect":
        raise ValueError(message)
    fields = instance["fields"]
    if not isinstance(fields, dict) or set(fields) != {"address"} or not isinstance(fields["address"], str):
        raise ValueError(message)
    try:
        tree = notation.parse_subject_expression(fields["address"], subject_profile="approved").expression
        if not isinstance(tree, notation.RelationChain) or len(tree.endpoints) < 3:
            raise ValueError
        root, *rest = tree.endpoints
        if (not isinstance(root.head, notation.Name) or root.head.value != "PROJECT STRUCTURE"
                or root.value_format is not None or root.value_cardinality is not None
                or len(root.steps) != 1 or root.steps[0].operator != "//"
                or not isinstance(root.steps[0].operand, notation.Name)):
            raise ValueError
        if any(not isinstance(part.head, notation.Name) or part.steps or part.value_format is not None
               or part.value_cardinality is not None for part in rest):
            raise ValueError
        if rest[0].head.value != "Aspects" or rest[-1].head.value != args["entity_name"]:
            raise ValueError
        if any(link.operator != "<+" or link.relation_type is not None
               or link.forward_cardinality is not None or link.reverse_cardinality is not None
               for link in tree.links):
            raise ValueError
        return notation.render_subject(tree)
    except (notation.SubjectNotationError, ValueError):
        raise ValueError(message) from None


def validate_aspect_hierarchy(args: dict) -> tuple[tuple[str, ...], tuple[str, ...]]:
    import subject_notation as notation
    if not isinstance(args, dict) or set(args) != {"entity_name", "structure_paths", "aspect_memberships"} or args.get("entity_name") != "Project Structure":
        raise ValueError("invalid Aspect hierarchy")
    result = []
    for key in ("structure_paths", "aspect_memberships"):
        paths = args[key]
        if (not isinstance(paths, tuple) or any(not isinstance(x, str) for x in paths)
                or len(set(paths)) != len(paths)):
            raise ValueError("Aspect hierarchy paths must be distinct tuples of text")
        normalized = []
        for address in paths:
            try:
                tree = notation.parse_subject_expression(address, subject_profile="approved").expression
                if (not isinstance(tree, notation.RelationChain) or not tree.endpoints
                        or not isinstance(tree.endpoints[-1].head, notation.Name)):
                    raise ValueError("invalid Aspect hierarchy address")
                leaf = tree.endpoints[-1].head.value
                normalized.append(validate_aspect_instance({"entity_name": leaf, "instance": {"type": "Aspect", "fields": {"address": address}}}))
            except (notation.SubjectNotationError, ValueError, TypeError, AttributeError, IndexError):
                raise ValueError("invalid Aspect hierarchy address") from None
        result.append(tuple(normalized))
    return tuple(result)


def parse_native_model_claim(text: str) -> dict[str, Any] | None:  # noqa: C901
    """Parse one authored Declaration into data, or return None for older Claims.

    The returned mapping contains kind, arguments, classes, imports and line.
    Python symbols are represented by their written names and Cardinality by
    minimum/maximum mappings. No Claim code or annotation is evaluated.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    try:
        tree = ast.parse(text, mode="exec")
    except SyntaxError as error:
        raise NativeModelClaimError(
            f"line {error.lineno}, column {error.offset}: {error.msg}"
        ) from error
    candidates = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                  and isinstance(node.func, ast.Name) and node.func.id in _DECLARATIONS]
    if not candidates:
        return None
    if len(candidates) != 1:
        raise NativeModelClaimError("a Model Claim must contain exactly one declaration")

    imports: dict[str, str] = {}
    names: set[str] = set()
    classes = []
    functions = []
    declaration: ast.Call | None = None
    for item in tree.body:
        if isinstance(item, ast.ImportFrom) and item.level == 0 and item.module:
            allowed = _IMPORTS.get(item.module)
            if allowed is None and item.module != "caprmedio.model":
                _fail(item, f"unsupported import: {item.module}")
            for alias in item.names:
                if alias.asname or alias.name == "*" or (allowed is not None and alias.name not in allowed):
                    _fail(item, f"unsupported import: {alias.name}")
                if alias.name in names:
                    _fail(item, f"duplicate symbol: {alias.name}")
                names.add(alias.name)
                imports[alias.name] = item.module
        elif isinstance(item, ast.ClassDef):
            if item.name in names:
                _fail(item, f"duplicate symbol: {item.name}")
            classes.append(_class(item, names))
            names.add(item.name)
        elif isinstance(item, ast.FunctionDef):
            if item.name in names:
                _fail(item, f"duplicate symbol: {item.name}")
            functions.append(_instance_check(item, names, text))
            names.add(item.name)
        elif (isinstance(item, ast.Expr) and isinstance(item.value, ast.Call)
              and isinstance(item.value.func, ast.Name) and item.value.func.id in _DECLARATIONS):
            if declaration is not None:
                _fail(item, "a Model Claim must contain exactly one declaration")
            declaration = item.value
        else:
            _fail(item, "unsupported top-level statement")
    if declaration is None:
        raise NativeModelClaimError("declaration must be a top-level call")
    function = declaration.func.id
    if imports.get(function) != "caprmedio.formal_claims":
        _fail(declaration, f"{function} must be imported")
    keywords = _keywords(declaration)
    if unknown := keywords.keys() - _DECLARATION_KEYS[function]:
        _fail(declaration, f"unsupported {function} arguments: {', '.join(sorted(unknown))}")
    arguments = {}
    for key, value in keywords.items():
        if key != "instance":
            arguments[key] = _value(value, names)
            continue
        if (function != "declare_entity" or not isinstance(value, ast.Call)
                or not isinstance(value.func, ast.Name)
                or value.func.id not in {"ScopeUnit", "Project", "Aspect"}
                or imports.get(value.func.id) != "caprmedio.model"):
            _fail(value, "instance requires an imported ScopeUnit, Project, or Aspect")
        fields = {}
        for field, field_value in _keywords(value).items():
            try:
                literal = ast.literal_eval(field_value)
            except (ValueError, TypeError, SyntaxError, RecursionError):
                _fail(field_value, "instance fields must be literals")
            if literal is not None and type(literal) not in {str, int, bool}:
                _fail(field_value, "instance fields must be scalar literals")
            fields[field] = literal
        arguments[key] = {"type": value.func.id, "fields": fields}
    if "allowed_classification_values" in arguments:
        values = arguments["allowed_classification_values"]
        if (set(arguments) != {"entity_name", "allowed_classification_values"}
                or not isinstance(values, dict) or not values
                or any(not isinstance(axis, str) or not axis.strip() or not isinstance(items, tuple)
                       or not items or any(not isinstance(item, str) or not item.strip() for item in items)
                       or len(set(items)) != len(items) for axis, items in values.items())):
            _fail(declaration, "allowed_classification_values requires named nonempty tuples of distinct text values")
    if "structure_paths" in arguments or "aspect_memberships" in arguments:
        try:
            validate_aspect_hierarchy(arguments)
        except ValueError as error:
            _fail(declaration, str(error))
    if "incoming_model_relations" in arguments:
        if (function != "declare_entity" or set(arguments) != {"entity_name", "entity_class", "incoming_model_relations"}
                or len(classes) != 1 or classes[0]["name"] != arguments.get("entity_class")
                or classes[0]["dataclass"] is None or classes[0]["bases"]
                or not any(isinstance(field.get("field", {}).get("metadata"), dict)
                           and {"property_occurrence_cardinality", "value_cardinality"}.intersection(field["field"]["metadata"])
                           for field in classes[0]["fields"])):
            _fail(declaration, "incoming model relations require a dataclass field contract")
    if arguments.get("instance", {}).get("type") == "Aspect":
        try:
            validate_aspect_instance(arguments)
        except ValueError as error:
            _fail(declaration, str(error))
    if "maximum_value" in arguments or "fallback_value" in arguments:
        if (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"
                or arguments.get("value_format") != "int"):
            _fail(declaration, "numeric bounds and literal fallback require an integer Property")
        for key in ("minimum_value", "maximum_value", "fallback_value"):
            if key in arguments and type(arguments[key]) is not int:
                _fail(declaration, f"{key} must be an integer")
        if arguments.get("minimum_value", float("-inf")) > arguments.get("maximum_value", float("inf")):
            _fail(declaration, "minimum_value exceeds maximum_value")
        if ("fallback_value" in arguments and not arguments.get("minimum_value", float("-inf")) <= arguments["fallback_value"] <= arguments.get("maximum_value", float("inf"))):
            _fail(declaration, "fallback_value violates numeric bounds")
        if "fallback_property_name" in arguments and "fallback_value" in arguments:
            _fail(declaration, "only one fallback is supported")
    if "fallback_chain" in arguments:
        chain = arguments["fallback_chain"]
        if (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"
                or "fallback_property_name" in arguments or "fallback_value" in arguments
                or not isinstance(chain, (tuple, list)) or len(chain) != 2
                or not isinstance(chain[0], dict) or set(chain[0]) != {"lookup_relation", "lookup_property"}
                or not isinstance(chain[1], dict) or set(chain[1]) != {"project_entity", "project_property"}
                or any(not isinstance(v, str) or not v.strip() or v != v.strip() for item in chain for v in item.values())
                or chain[1]["project_entity"] != "Project" or not chain[1]["project_property"].startswith("Project.")):
            _fail(declaration, "fallback_chain requires an ordered lookup and Project Property")
    if "fallback_property_name" in arguments:
        fallback = arguments["fallback_property_name"]
        if (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"
                or not isinstance(fallback, str) or not fallback.strip() or fallback != fallback.strip()
                or any(c in fallback for c in "./()[]{}")
                or fallback == arguments.get("entity_name")):
            _fail(declaration, "fallback_property_name requires a distinct simple Property name")
    if "instance" in arguments and ("entity_class" in arguments or functions or classes):
        _fail(declaration, "instance cannot be combined with class or instance-check declarations")
    check = next((keyword.value for keyword in declaration.keywords if keyword.arg == "instance_check"), None)
    if check is not None:
        if (function != "declare_entity" or not isinstance(check, ast.Name)
                or check.id not in {item["name"] for item in functions}):
            _fail(check, "instance_check must name a function declared in this Claim")
        model_types = {item["name"] for item in classes} | {
            name for name, module in imports.items() if module == "caprmedio.model"
        }
        callback = next(item for item in functions if item["name"] == check.id)
        if callback["parameter_type"] not in model_types:
            _fail(check, "instance check argument must be a Model class")
        if "entity_class" in arguments and callback["parameter_type"] != arguments["entity_class"]:
            _fail(check, "instance check argument must match entity_class")
    if functions and (check is None or len(functions) != 1):
        _fail(declaration, "each function must be the declared instance_check")
    required = {"entity_name"} if function == "declare_entity" else {"relation_name"}
    if missing := required - arguments.keys():
        _fail(declaration, f"missing arguments: {', '.join(sorted(missing))}")
    if not isinstance(arguments[next(iter(required))], str) or not arguments[next(iter(required))]:
        _fail(declaration, "declaration name must be a nonempty string")
    if "entity_class" in arguments and arguments["entity_class"] not in {row["name"] for row in classes}:
        _fail(declaration, "entity_class must name a class declared in the Claim")
    if any(key in arguments for key in ("applies_to_role", "applies_to_forms", "status_groups")) and (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"):
        _fail(declaration, "Status qualifiers require a Property Declaration")
    if "dependent_property_value_cardinality" in arguments and (
        arguments.get("relation_name") != "IS_PROPERTY_OF" or not arguments.get("dependent_property_value_format")
    ):
        _fail(declaration, "dependent Property value cardinality requires a Property Declaration and value format")
    if function == "declare_entity" and arguments.get("relation_name") == "IS_PROPERTY_OF":
        base = arguments.get("base_path")
        if not isinstance(base, str) or not base.strip() or base != base.strip():
            _fail(declaration, "IS_PROPERTY_OF requires a nonempty base_path")
        allowed = arguments.get("allowed_values", ())
        if (not isinstance(allowed, (list, tuple)) or any(not isinstance(value, str) or not value.strip()
                                                          for value in allowed)
                or len(allowed) != len(set(allowed))):
            _fail(declaration, "allowed_values requires distinct nonempty names")
        forms = arguments.get("applies_to_forms")
        role = arguments.get("applies_to_role")
        groups = arguments.get("status_groups")
        if any(key in arguments for key in ("applies_to_forms", "applies_to_role", "status_groups")):
            if base != "Atom.Header.State" or arguments.get("entity_name") != "Status":
                _fail(declaration, "Status qualifiers require Atom Header Status")
            if "applies_to_forms" in arguments or "applies_to_role" in arguments:
                permitted = {"entity_name", "relation_name", "base_path", "applies_to_role", "applies_to_forms", "allowed_values"}
                if (not isinstance(role, str) or not role.strip() or role != role.strip()
                        or not isinstance(forms, tuple) or not forms or not allowed
                        or any(not isinstance(form, str) or not form.strip() or form != form.strip() for form in forms)
                        or len(forms) != len(set(forms)) or set(arguments) - permitted):
                    _fail(declaration, "Form-qualified Status requires one Role and distinct Forms")
            if "status_groups" in arguments:
                classes = arguments.get("applies_to_entity_classes")
                if (not isinstance(groups, dict) or not groups or not isinstance(classes, (tuple, list)) or len(classes) != 1
                        or any(status not in allowed or not isinstance(group, str) or not group.strip() or group != group.strip()
                               for status, group in groups.items())):
                    _fail(declaration, "Status Groups require allowed values and one Role")
        if "status_order_numbers" in arguments:
            orders = arguments["status_order_numbers"]
            if (base != "Atom.Header.State" or arguments.get("entity_name") != "Status"
                    or not isinstance(orders, dict)
                    or any(name not in allowed or type(order) is not int or not 0 <= order <= 999
                           for name, order in orders.items())
                    or len(orders) != len(set(orders.values()))):
                _fail(declaration, "invalid base Status Order Numbers")
    if "population_entity_path" in arguments and not ({"population_functional_dependencies", "population_unique_constraints"} & arguments.keys()):
        _fail(declaration, "population_entity_path requires a population constraint")
    if "population_unique_constraints" in arguments:
        population = arguments.get("population_entity_path", arguments.get("base_path"))
        base = arguments.get("base_path")
        rules = arguments["population_unique_constraints"]
        if (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"
                or not isinstance(population, str) or not population.strip() or population != population.strip()
                or not isinstance(base, str) or not (base == population or base.startswith(population + "."))
                or not isinstance(rules, (tuple, list)) or not rules):
            _fail(declaration, "population uniqueness requires a Property and its population")
        seen = set()
        for rule in rules:
            if (not isinstance(rule, dict) or set(rule) not in ({"keys"}, {"keys", "status", "single_value_paths"})
                    or ("status" in rule and rule["status"] != "Active")):
                _fail(declaration, "population uniqueness requires keys, optionally with Active status and single-value paths")
            keys, present = rule["keys"], rule.get("single_value_paths", rule["keys"])
            for part in (keys, present):
                if (not isinstance(part, (tuple, list)) or not part
                        or any(not isinstance(path, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z_0-9 -]*(?:\.[A-Za-z_][A-Za-z_0-9 -]*)*", path)
                               or path != path.strip() or any(segment != segment.strip() for segment in path.split(".")) for path in part)
                        or len(part) != len(set(part))):
                    _fail(declaration, "population uniqueness paths must be distinct relative Property paths")
            if set(keys) != set(present):
                _fail(declaration, "every unique key requires exactly one value")
            signature = tuple(keys)
            if signature in seen:
                _fail(declaration, "duplicate population uniqueness rule")
            seen.add(signature)
    if "population_functional_dependencies" in arguments:
        population = arguments.get("population_entity_path", arguments.get("base_path"))
        base = arguments.get("base_path")
        if (not isinstance(population, str) or not population.strip() or population != population.strip()
                or not isinstance(base, str) or not (base == population or base.startswith(population + "."))):
            _fail(declaration, "population must be the Property bearer or an ancestor")
        dependencies = arguments["population_functional_dependencies"]
        if (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"
                or not isinstance(dependencies, (tuple, list)) or not dependencies):
            _fail(declaration, "population functional dependencies require a Property declaration")
        seen = set()
        for dependency in dependencies:
            if (not isinstance(dependency, dict) or not {"keys", "dependents"} <= set(dependency)
                    or set(dependency) - {"keys", "dependents", "status_groups"}):
                _fail(declaration, "functional dependency requires keys and dependents")
            if "status_groups" in dependency:
                groups = dependency["status_groups"]
                if (population != "Atom" or not isinstance(groups, (tuple, list)) or not groups
                        or any(not isinstance(group, str) or group not in {"Current", "Backlog", "Archived", "Draft"} for group in groups)
                        or len(groups) != len(set(groups))):
                    _fail(declaration, "status_groups requires distinct admitted Atom Status Groups")
            for part in (dependency["keys"], dependency["dependents"]):
                if (not isinstance(part, (tuple, list)) or not part
                        or any(not isinstance(path, str) or not re.fullmatch(r"[A-Za-z_][A-Za-z_0-9 -]*(?:\.[A-Za-z_][A-Za-z_0-9 -]*)*", path)
                               or path != path.strip() or any(segment != segment.strip() for segment in path.split(".")) for path in part)
                        or len(part) != len(set(part))):
                    _fail(declaration, "functional dependency paths must be distinct nonempty relative Property paths")
            signature = (tuple(dependency["keys"]), tuple(dependency["dependents"]), tuple(dependency.get("status_groups", ())))
            if signature in seen:
                _fail(declaration, "duplicate functional dependency")
            seen.add(signature)
    recursive_fields = {"recursive_dependent_property_cardinality", "recursive_dependent_property_name_format",
                        "recursive_dependent_property_value_format"}
    if recursive_fields & arguments.keys():
        if function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF":
            _fail(declaration, "recursive dependent Properties require a Property declaration")
        if ("recursive_dependent_property_name_format" in arguments
                and "recursive_dependent_property_cardinality" not in arguments):
            _fail(declaration, "recursive dependent Property name format requires cardinality")
    if "ordered_dependent_property_pairs" in arguments:
        pairs = arguments["ordered_dependent_property_pairs"]
        names = arguments.get("allowed_dependent_property_names")
        if (function != "declare_entity" or arguments.get("relation_name") != "IS_PROPERTY_OF"
                or (names is not None and (not isinstance(names, (tuple, list)) or not names))
                or not isinstance(pairs, (tuple, list)) or not pairs):
            _fail(declaration, "ordered dependent Property pairs require a Property declaration")
        if any(not isinstance(pair, (tuple, list)) or len(pair) != 2
               or any(not isinstance(name, str) or not name.strip() or (names is not None and name not in names) for name in pair)
               or pair[0] == pair[1] for pair in pairs):
            _fail(declaration, "ordered dependent Property pairs must name distinct allowed children")
        edges = [tuple(pair) for pair in pairs]
        if (len({left for left, _ in edges}) != len(edges)
                or len({right for _, right in edges}) != len(edges)):
            _fail(declaration, "ordered dependent Properties require unique adjacent neighbors")
        following = dict(edges)
        for start in following:
            seen = set()
            current = start
            while current in following:
                if current in seen:
                    _fail(declaration, "ordered dependent Property pairs must be acyclic")
                seen.add(current)
                current = following[current]
    if "ordered_dependent_property_roles" in arguments:
        roles = arguments["ordered_dependent_property_roles"]
        if ("ordered_dependent_property_pairs" not in arguments or not isinstance(roles, (tuple, list))
                or not roles or any(not isinstance(role, str) or not role.strip() for role in roles)):
            _fail(declaration, "ordered dependent Property roles require ordering pairs and nonempty Roles")
    if function == "declare_relation":
        if "endpoint_pairs" in arguments:
            pairs = arguments["endpoint_pairs"]
            if (not isinstance(pairs, (tuple, list)) or not pairs
                    or "source_endpoint" in arguments or "target_endpoint" in arguments):
                _fail(declaration, "endpoint_pairs requires a nonempty collection and excludes single endpoints")
            for pair in pairs:
                if not isinstance(pair, dict) or set(pair) != {"source_endpoint", "target_endpoint"}:
                    _fail(declaration, "endpoint pair requires source_endpoint and target_endpoint")
                for key in ("source_endpoint", "target_endpoint"):
                    _validate_endpoint(pair[key], key, declaration)
        else:
            for key in ("source_endpoint", "target_endpoint"):
                _validate_endpoint(arguments.get(key), key, declaration)
    for field, allowed in (("model_relation_constraints", _RELATION_CONSTRAINT_KEYS),
                           ("instance_relation_constraints", _RELATION_CONSTRAINT_KEYS),
                           ("instance_property_constraints", _PROPERTY_CONSTRAINT_KEYS)):
        if field not in arguments:
            continue
        constraints = arguments[field]
        if not isinstance(constraints, dict) or any(not isinstance(value, dict) for value in constraints.values()):
            target = "Property paths" if field == "instance_property_constraints" else "Relation names"
            _fail(declaration, f"{field} must map {target} to constraint mappings")
        for constraint in constraints.values():
            if unknown := constraint.keys() - allowed:
                _fail(declaration, f"unsupported {field} keys: {', '.join(sorted(unknown))}")
    _validate_cardinalities(arguments, declaration)
    result = {"kind": _DECLARATIONS[function], "arguments": arguments, "classes": tuple(classes),
              "imports": imports, "line": declaration.lineno}
    value_format_node = keywords.get("value_format")
    if isinstance(value_format_node, ast.Name) and imports.get(value_format_node.id) == "caprmedio.model":
        result["model_value_format"] = value_format_node.id
    if functions:
        result["instance_check"] = functions[0]
    return result
