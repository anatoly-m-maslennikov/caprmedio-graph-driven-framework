"""Translate native declarations into statements understood by existing compilers.

Only the compiler inputs represented here are translated. Consumers of the
other native contracts must use the structured declaration directly.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any


_PATH = re.compile(r"[A-Za-z_][A-Za-z_0-9 .-]*\Z")
_RELATION = re.compile(r"[A-Za-z_][A-Za-z_0-9]*\Z")
_FORMATS = {"str": "string", "int": "int", "float": "float", "bool": "bool", "datetime": "datetime",
            "markdown": "markdown", "atom_id": "atom id"}


def _name(value: Any, *, relation: bool = False) -> str:
    pattern = _RELATION if relation else _PATH
    if not isinstance(value, str) or not pattern.fullmatch(value) or value != value.strip():
        raise ValueError(f"unsupported compiler name: {value!r}")
    return value


def _model_base_path(value: Any) -> str:
    """Accept bounded Model paths, including a qualified narrowing step."""
    try:
        return _name(value)
    except ValueError:
        pass
    if not isinstance(value, str) or value != value.strip():
        raise ValueError(f"unsupported compiler name: {value!r}")
    import subject_notation as notation
    try:
        path = notation.parse_subject_expression(value, subject_profile="approved").expression
        if not isinstance(path, notation.Path) or not isinstance(path.head, notation.Name):
            raise ValueError
        _name(path.head.value)
        if path.value_format is not None or path.value_cardinality is not None:
            raise ValueError
        for step in path.steps:
            if step.operator in ("/", ".") and isinstance(step.operand, notation.Name):
                _name(step.operand.value)
            elif step.operator == "/" and isinstance(step.operand, notation.Qualification):
                q = step.operand.relative_path
                if not isinstance(q.head, notation.Name) or q.value_format is not None or q.value_cardinality is not None:
                    raise ValueError
                _name(q.head.value)
                if not q.steps or q.steps[-1].operator != ":=" or not isinstance(q.steps[-1].operand, notation.ValueLiteral):
                    raise ValueError
                _name(q.steps[-1].operand.value)
                for part in q.steps[:-1]:
                    if part.operator != "." or not isinstance(part.operand, notation.Name):
                        raise ValueError
                    _name(part.operand.value)
            else:
                raise ValueError
    except (notation.SubjectNotationError, ValueError, TypeError):
        raise ValueError(f"unsupported compiler name: {value!r}") from None
    return value


def _count(value: Any) -> str:
    if type(value) is int and value >= 0:
        return str(value)
    if not isinstance(value, dict) or set(value) != {"minimum", "maximum"}:
        raise ValueError(f"unsupported cardinality: {value!r}")
    minimum, maximum = value["minimum"], value["maximum"]
    if type(minimum) is not int or minimum < 0 or (
        maximum is not None and (type(maximum) is not int or maximum < minimum)
    ):
        raise ValueError(f"unsupported cardinality: {value!r}")
    if maximum is None:
        return f"{minimum}+"
    if minimum == maximum:
        return str(minimum)
    return f"{minimum}..{maximum}"


def _format(value: Any) -> str:
    if not isinstance(value, str) or value not in _FORMATS:
        raise ValueError(f"unsupported compiler format: {value!r}")
    return _FORMATS[value]


def _aspect_statements(args: Mapping[str, Any]) -> tuple[str, str]:
    from .native_model_claim import validate_aspect_instance

    try:
        address = validate_aspect_instance(dict(args))
    except ValueError:
        raise ValueError("invalid Aspect instance address") from None
    return address, f"({address}) ((INSTANCE_OF)) Aspect"

def has_dataclass_field_contracts(declaration: Mapping[str, Any]) -> bool:
    keys = {"property_occurrence_cardinality", "value_cardinality"}
    classes = declaration.get("classes", ())
    if not isinstance(classes, (tuple, list)):
        return False
    for cls in classes:
        if not isinstance(cls, Mapping):
            continue
        for field in cls.get("fields", ()):
            if not isinstance(field, Mapping) or not isinstance(field.get("field"), Mapping):
                continue
            metadata = field["field"].get("metadata")
            if isinstance(metadata, Mapping) and keys.intersection(metadata):
                return True
    return False


def compiler_model_statements(declaration: Mapping[str, Any], *, model_class_bindings: Mapping[str, Any] | None = None) -> tuple[str, ...]:
    """Return bounded compiler statements from an already parsed native Claim."""
    args = declaration["arguments"]
    if declaration["kind"] == "entity" and has_dataclass_field_contracts(declaration):
        if set(args) - {"entity_name", "entity_class", "incoming_model_relations"} or not {"entity_name", "entity_class"} <= set(args):
            raise ValueError("unsupported dataclass field contract declaration")
        classes = declaration.get("classes", ())
        if (len(classes) != 1 or classes[0]["name"] != args.get("entity_class")
                or classes[0]["bases"] or classes[0]["dataclass"] is None):
            raise ValueError("field contracts require the declared dataclass with no base")
        result = []
        for field in classes[0]["fields"]:
            options = field.get("field", {})
            if set(options) != {"metadata"}:
                raise ValueError("unsupported dataclass field contract")
            meta = options["metadata"]
            if not isinstance(meta, dict) or set(meta) != {"property_occurrence_cardinality", "value_cardinality"}:
                raise ValueError("field contracts require occurrence and value cardinalities")
            address = f"{_name(args['entity_name'])}.{_name(field['name'])}"
            occurrence_count = _count(meta["property_occurrence_cardinality"])
            value_format = _format(field["annotation"])
            value_count = _count(meta["value_cardinality"])
            result.append(f"{address}{{::{occurrence_count}}} :: [{value_format}]{{::{value_count}}}")
        incoming = args.get("incoming_model_relations", ())
        if not isinstance(incoming, tuple):
            raise ValueError("incoming model relations must be a tuple")
        for relation in incoming:
            if not isinstance(relation, dict) or set(relation) != {"source", "relation", "source_cardinality", "target_cardinality"}:
                raise ValueError("invalid incoming model relation")
            result.append(f"{_name(relation['source'])} {{::{_count(relation['source_cardinality'])}}}(({_name(relation['relation'], relation=True)})){{::{_count(relation['target_cardinality'])}}} {_name(args['entity_name'])}")
        return tuple(result)
    if declaration["kind"] == "entity" and ("structure_paths" in args or "aspect_memberships" in args):
        from .native_model_claim import validate_aspect_hierarchy
        paths, memberships = validate_aspect_hierarchy(dict(args))
        return paths + tuple(f"({address}) ((INSTANCE_OF)) Aspect" for address in memberships)
    if declaration["kind"] == "entity" and "allowed_classification_values" in args:
        if set(args) != {"entity_name", "allowed_classification_values"}:
            raise ValueError("unsupported allowed classification declaration")
        values = args["allowed_classification_values"]
        if not isinstance(values, Mapping) or not values:
            raise ValueError("allowed classification values must be a nonempty mapping")
        statements = []
        for axis, items in values.items():
            if not isinstance(items, tuple) or not items or len(set(items)) != len(items):
                raise ValueError("allowed classification values must be distinct tuples")
            statements.extend(f"{_name(args['entity_name'])} >| {_name(axis)}: {_name(item)}" for item in items)
        return tuple(statements)
    if declaration["kind"] == "entity" and args.get("instance", {}).get("type") == "Aspect":
        return _aspect_statements(args)
    if declaration["kind"] == "relation":
        name = _name(args["relation_name"], relation=True)
        statements = [f"Relation//{name}"]
        if inverse := args.get("inverse_alias"):
            inverse = _name(inverse, relation=True)
            instance_levels = {"instances", "model_entities_or_instances"}
            pairs = args.get("endpoint_pairs", (args,))
            if all(pair[endpoint]["level"] in instance_levels for pair in pairs for endpoint in ("source_endpoint", "target_endpoint")):
                statements.append(f"Relation//{name} ((HAS_INVERSE)) Relation//{inverse}")
            else:
                statements.append(f"Relation//{inverse} ((IS_INVERSE_ALIAS_FOR)) Relation//{name}")
        return tuple(statements)

    if declaration["kind"] != "entity":
        raise ValueError(f"unsupported declaration kind: {declaration['kind']!r}")
    if "instance_check" in args:
        raise ValueError("instance_check requires a typed validator before compilation")
    name = _name(args["entity_name"])
    if args.get("relation_name") == "IS_PROPERTY_OF":
        base = _model_base_path(args["base_path"])
        if classes := args.get("applies_to_entity_classes"):
            content = base == "Atom.Content" or base.startswith("Atom.Content.")
            header = base == "Atom.Header" or base.startswith("Atom.Header.")
            if not isinstance(classes, (list, tuple)) or not (content or (header and len(classes) == 1)):
                raise ValueError("unsupported Property class selection")
            roles = ", ".join(_name(role) for role in classes)
            base = f"Atom/(.Header.Context.Role in ({roles})).{base.removeprefix('Atom.')}"
        def property_statements(base):
            address = f"{base}.{name}"
            statement = address
            if "property_occurrence_cardinality" in args:
                statement += f"{{::{_count(args['property_occurrence_cardinality'])}}}"
            if "value_format" in args or "value_cardinality" in args:
                statement += " ::"
                if "value_format" in args:
                    model_class = declaration.get("model_value_format")
                    if model_class is not None:
                        targets = (model_class_bindings or {}).get(model_class)
                        if not isinstance(targets, (set, frozenset, list, tuple)) or len(set(targets)) != 1:
                            raise ValueError(f"missing or ambiguous Model class binding: {model_class}")
                        target = _model_base_path(next(iter(targets)))
                        statement += f" [{target}//]"
                    else:
                        format_name = _format(args['value_format'])
                        if "maximum_value" in args:
                            if "minimum_value" not in args:
                                raise ValueError("bounded range requires minimum_value")
                            format_name += f", {args['minimum_value']}..{args['maximum_value']}"
                        statement += f" [{format_name}]"
                elif args.get("value_cardinality") == 0:
                    statement += " []"
                if "value_cardinality" in args:
                    statement += f"{{::{_count(args['value_cardinality'])}}}"
            if "fallback_value" in args:
                statement += f" ?== {args['fallback_value']}"
            statements = [] if statement == address and args.get("allowed_values") else [statement]
            if "dependent_property_cardinality" in args:
                names = args.get("allowed_dependent_property_names")
                name_format = args.get("dependent_property_name_format")
                if names is not None:
                    if not isinstance(names, (list, tuple)) or not names:
                        raise ValueError("dependent Property names must be a nonempty sequence")
                    selector = "in (" + ", ".join(_name(item) for item in names) + ")"
                    if name_format is not None:
                        selector = _format(name_format) + ", " + selector
                else:
                    selector = _format(name_format) if name_format is not None else ""
                statements.append(f"{address}.*[{selector}]{{::{_count(args['dependent_property_cardinality'])}}}")
            if "recursive_dependent_property_cardinality" in args:
                name_format = args.get("recursive_dependent_property_name_format")
                selector = _format(name_format) if name_format is not None else ""
                statements.append(f"{address}.**[{selector}]{{::{_count(args['recursive_dependent_property_cardinality'])}}}")
            if value_format := args.get("recursive_dependent_property_value_format"):
                statements.append(f"{address}.** :: [{_format(value_format)}]")
            ordering_address = address
            if roles := args.get("ordered_dependent_property_roles"):
                if address != "Atom.Content":
                    raise ValueError("unsupported ordered Property Role selection")
                role_names = ", ".join(_name(role) for role in roles)
                ordering_address = f"Atom/(.Header.Context.Role in ({role_names})).Content"
            for first, second in args.get("ordered_dependent_property_pairs", ()):
                statements.append(f"{ordering_address}.{_name(first)} ;> {ordering_address}.{_name(second)}")
            value_format = args.get("dependent_property_value_format")
            if value_format or "dependent_property_value_cardinality" in args:
                statement = f"{address}.* ::"
                if value_format:
                    statement += f" [{_format(value_format)}]"
                if "dependent_property_value_cardinality" in args:
                    statement += f"{{::{_count(args['dependent_property_value_cardinality'])}}}"
                statements.append(statement)
            if "minimum_value" in args and "maximum_value" not in args:
                minimum = args["minimum_value"]
                if type(minimum) not in (int, float):
                    raise ValueError("minimum_value must be numeric")
                statements.append(f"{address} >= {minimum}")
            allowed = args.get("allowed_values", ())
            statements.extend(f"{address} :: {_name(value)}" for value in allowed)
            return statements

        if forms := args.get("applies_to_forms"):
            import json
            role = _name(args["applies_to_role"])
            role = json.dumps(role) if " " in role else role
            bases = [f"Atom/(.Header.Context.Role in ({role}))/(.Header.Context.Form in ({_name(form)})).Header.State" for form in forms]
        else:
            bases = [base]
        statements = [statement for selected_base in bases for statement in property_statements(selected_base)]
        statements.extend(
            f"Atom/(.Header.State.Status := {status}).Header.State.Status >| (Status Order Number == {order})"
            for status, order in args.get("status_order_numbers", {}).items()
        )
        if groups := args.get("status_groups"):
            role = _name(args["applies_to_entity_classes"][0])
            statements.extend(
                f"Atom/(.Header.Context.Role := {role})/(.Header.State.Status := {_name(status)}).Header.State.Status >| Status Group == {_name(group)}"
                for status, group in groups.items()
            )
        if args.get("fallback_property_name"):
            parts = base.split(".")
            if not parts or any(not _PATH.fullmatch(part) or part != part.strip() for part in parts):
                raise ValueError("fallback requires a simple bearer path")
            fallback = _name(args["fallback_property_name"])
            host = parts[0]
            left = ".".join(parts[1:] + [name])
            right = ".".join(parts[1:] + [fallback])
            variable = re.sub(r"[^a-z0-9_]+", "_", host.casefold())
            statements.extend((f"{host}//${variable}", f"${variable}.{left} ?== ${variable}.{right}"))
        return tuple(statements)

    qualifier = args.get("qualification_property_path")
    if qualifier == "Projection.Form":
        classes = [item for item in declaration["classes"] if item["name"] == args.get("entity_class")]
        if len(classes) != 1 or classes[0]["bases"] != ("Projection",):
            raise ValueError("a Projection Form requires Projection as its sole base")
        return (f"Projection.Form :: {name}", f"Projection/(.Form in ({name}))")
    if qualifier == "Atom.Header.Context.Role":
        statements = [f"{qualifier} :: {name}"]
        classifications = args.get("classifications", {})
        if "Role Order Number" in classifications:
            order = classifications["Role Order Number"]
            if type(order) is not int or order < 1:
                raise ValueError("Role Order Number must be a positive integer")
            statements.append(f"Atom/(.Header.Context.Role := {name}) >| (Role Order Number == {order})")
        return tuple(statements)
    if qualifier == "Atom.Header.Context.Form":
        classes = [item for item in declaration["classes"] if item["name"] == args.get("entity_class")]
        if len(classes) != 1 or len(classes[0]["bases"]) != 1:
            raise ValueError("a Role-qualified Form requires exactly one base class")
        role = _name(classes[0]["bases"][0])
        return (f"Atom/(.Header.Context.Role in ({role})).Header.Context.Form :: {name}",)
    return ()


def compile_scope_level_with_check(declaration):
    """Compile static constraints only for the explicit Scope-level consumer.

    The returned check metadata must be bound to a reviewed packaged callable
    by that consumer. Generic compiler_model_statements stays fail-closed.
    """
    from copy import deepcopy
    args = declaration.get("arguments", {})
    check = declaration.get("instance_check")
    if (declaration.get("kind") != "entity" or args.get("entity_name") != "structural_level"
            or args.get("base_path") != "Scope Unit" or args.get("relation_name") != "IS_PROPERTY_OF"
            or not check or check.get("name") != "check_structural_level"
            or check.get("parameter_type") != "ScopeUnit"
            or declaration.get("imports", {}).get("ScopeUnit") != "caprmedio.model"):
        raise ValueError("instance_check requires a typed validator")
    static = deepcopy(declaration)
    del static["arguments"]["instance_check"]
    del static["instance_check"]
    return compiler_model_statements(static), deepcopy(check)


def compile_atom_dependencies_with_check(declaration, *, model_class_bindings=None):
    """Return static rules and callback metadata for the explicit Atom consumer.

    The consumer must bind the callback through its reviewed-claim boundary.
    """
    from copy import deepcopy
    from .topic_dependencies import DEPENDENCIES_CHECK_SOURCE_SHA256
    from hashlib import sha256
    args = declaration.get("arguments", {})
    check = declaration.get("instance_check")
    if (declaration.get("kind") != "entity" or args.get("entity_name") != "Dependencies"
            or args.get("base_path") != "Atom.Header.Context.Topics"
            or args.get("relation_name") != "IS_PROPERTY_OF"
            or not check or check.get("name") != "dependencies_are_distinct"
            or check.get("parameter_type") != "Atom"
            or declaration.get("imports", {}).get("Atom") != "caprmedio.model"
            or sha256(check["source"].encode()).hexdigest() != DEPENDENCIES_CHECK_SOURCE_SHA256
            or args.get("property_occurrence_cardinality") != {"minimum": 0, "maximum": 1}
            or args.get("value_format") != "str"
            or args.get("value_cardinality") != {"minimum": 0, "maximum": None}
            or args.get("dependent_property_cardinality") != 0
            or len(args) != 8):
        raise ValueError("instance_check requires the typed Atom Dependencies validator")
    static = deepcopy(declaration)
    del static["arguments"]["instance_check"]
    del static["instance_check"]
    return compiler_model_statements(static, model_class_bindings=model_class_bindings), deepcopy(check)
