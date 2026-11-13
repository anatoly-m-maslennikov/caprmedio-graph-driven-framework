"""Check native Model Declaration references against a supplied catalog."""

from __future__ import annotations

import re
from collections.abc import Collection, Callable, Mapping


def lint_native_model_claim(declaration: dict, *, declared_addresses: Collection[str],
                            relation_names: Collection[str], path: str, first_line: int,
                            resolve_address: Callable, simple_address: Callable, canonical_address: Callable,
                            python_class_bindings: Mapping[str, Collection[str]] | None = None) -> tuple[str, ...]:
    declared = set()
    canonical = set()
    class_names: dict[str, set[str]] = {}
    for address in declared_addresses:
        try:
            canonical.add(canonical_address(address))
        except ValueError:
            pass
        try:
            simple = simple_address(address)
        except ValueError:
            simple = None
        if simple is not None:
            declared.add(simple)
            if "." not in simple and "//" not in simple:
                name = re.sub(r"[^a-z0-9]", "", simple.rsplit("/", 1)[-1].casefold())
                class_names.setdefault(name, set()).add(re.sub(r"\s+", "", simple).casefold())
        qualifier = re.search(r"/\(\.Header\.Context\.(?:Role|Form)\s*:=\s*([^)]*)\)\s*$", address)
        if qualifier:
            name = re.sub(r"[^a-z0-9]", "", qualifier[1].casefold())
            class_names.setdefault(name, set()).add(re.sub(r"\s+", "", address).casefold())

    args = declaration["arguments"]
    line = first_line + declaration["line"] - 1

    def error(message: str) -> tuple[str, ...]:
        return (f"{path}:{line}:1: {message}",)

    from .compiler_claim import has_dataclass_field_contracts, compiler_model_statements
    if has_dataclass_field_contracts(declaration):
        try:
            compiler_model_statements(declaration)
        except ValueError as failure:
            return error(str(failure))

    check = declaration.get("instance_check")
    if check is not None:
        model_type = check["parameter_type"]
        local_classes = {item["name"] for item in declaration["classes"]}
        if model_type not in local_classes and declaration["imports"].get(model_type) != "caprmedio.model":
            return error(f"instance check requires a Model class: {model_type}")
        entity_class = args.get("entity_class")
        if entity_class is not None and model_type != entity_class:
            return error(f"instance check does not match entity_class: {model_type}")

    for name, module in declaration["imports"].items():
        if module == "caprmedio.model":
            if python_class_bindings is not None and name in python_class_bindings:
                targets = python_class_bindings[name]
                if isinstance(targets, str) or not isinstance(targets, Collection):
                    return error(f"invalid Model class binding: {name}")
                try:
                    matches = {canonical_address(target) for target in targets}
                except (ValueError, TypeError):
                    return error(f"invalid Model class binding: {name}")
                if matches - canonical:
                    return error(f"unknown Model class address: {name}")
            else:
                matches = class_names.get(re.sub(r"[^a-z0-9]", "", name.casefold()), set())
            if not matches:
                return error(f"unknown Model class: {name}")
            if len(matches) > 1:
                return error(f"ambiguous Model class: {name}")

    if "fallback_chain" in args:
        lookup, project = args["fallback_chain"]
        if lookup["lookup_relation"] not in relation_names:
            return error(f"unknown fallback Relation: {lookup['lookup_relation']}")
        for full in (lookup["lookup_property"], project["project_property"]):
            try:
                if canonical_address(full) not in canonical:
                    return error(f"unknown fallback Property address: {full}")
            except (TypeError, ValueError):
                return error(f"invalid fallback Property address: {full}")
        try:
            if canonical_address(project["project_entity"]) not in canonical:
                return error(f"unknown Project model address: {project['project_entity']}")
        except (TypeError, ValueError):
            return error(f"invalid Project model address: {project['project_entity']}")

    if "fallback_property_name" in args:
        bearer = args.get("base_path")
        if not isinstance(bearer, str):
            return error("fallback requires a bearer")
        for member in (args.get("entity_name"), args["fallback_property_name"]):
            full = f"{bearer}.{member}"
            try:
                if simple_address(full) not in declared:
                    return error(f"unknown declared fallback Property: {full}")
            except (TypeError, ValueError):
                return error(f"invalid fallback Property: {full}")

    for rule in args.get("population_unique_constraints", ()):
        population = args.get("population_entity_path", args["base_path"])
        for relative in (*rule["keys"], *(("Header.State.Status",) if "status" in rule else ())):
            full = f"{population}.{relative}"
            try:
                if canonical_address(full) in canonical or resolve_address(full, declared, relation_names, {}):
                    continue
                return error(f"unknown population Property address: {full}")
            except (TypeError, ValueError):
                return error(f"unknown population Property address: {full}")

    for dependency in args.get("population_functional_dependencies", ()):
        population = args.get("population_entity_path", args["base_path"])
        paths = (*dependency["keys"], *dependency["dependents"])
        if "status_groups" in dependency:
            paths = (*paths, "Header.State.Status")
        for relative in paths:
            full = f"{population}.{relative}"
            try:
                if canonical_address(full) not in canonical:
                    return error(f"unknown population Property address: {full}")
            except (TypeError, ValueError):
                return error(f"invalid population Property address: {full}")

    paths = [args[key] for key in ("base_path", "qualification_property_path", "population_entity_path") if key in args]
    for pair in args.get("ordered_dependent_property_pairs", ()):
        paths.extend(f"{args['base_path']}.{args['entity_name']}.{name}" for name in pair)
    endpoints = [args.get("source_endpoint", {}), args.get("target_endpoint", {})]
    for pair in args.get("endpoint_pairs", ()):
        endpoints.extend((pair["source_endpoint"], pair["target_endpoint"]))
    for endpoint in endpoints:
        paths.extend(endpoint.get("entity_paths", ()))
    relations = ["IS_ORDERED_RIGHT_BEFORE"] if args.get("ordered_dependent_property_pairs") else []
    for incoming in args.get("incoming_model_relations", ()):
        paths.append(incoming["source"])
        relations.append(incoming["relation"])
    for field in ("model_relation_constraints", "instance_relation_constraints"):
        constraints = args.get(field, {})
        if not isinstance(constraints, dict) or any(not isinstance(item, dict) for item in constraints.values()):
            return error(f"{field} must map Relation names to constraints")
        relations.extend(constraints)
        for constraint in constraints.values():
            targets = constraint.get("target_entity_paths", ())
            if not isinstance(targets, (tuple, list)):
                return error("target_entity_paths must be a list of Model addresses")
            paths.extend(targets)
    for address in paths:
        if not isinstance(address, str):
            return error("Model address must be a string")
        try:
            if canonical_address(address) in canonical:
                continue
        except ValueError:
            pass
        try:
            if not resolve_address(address, declared, relation_names, {}):
                return error(f"unknown Model address: {address}")
        except ValueError as exc:
            return error(str(exc))

    if declaration["kind"] == "entity" and args.get("relation_name"):
        relations.append(args["relation_name"])
    for relation in relations:
        if relation not in relation_names:
            return error(f"unknown Relation: {relation}")
    return ()
