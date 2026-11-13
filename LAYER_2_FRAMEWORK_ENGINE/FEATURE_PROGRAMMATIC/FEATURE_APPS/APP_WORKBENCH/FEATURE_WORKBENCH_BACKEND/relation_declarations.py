"""Read Relation contributions from Formal Claims."""

from dataclasses import dataclass
import re
import sys

from .declaration_cfel import cfel_without_comments, formal_claim_fences, model_statements


_NAME = r"[A-Za-z_][A-Za-z_0-9]*"
_DECLARATION = re.compile(rf"Relation//({_NAME})(?:\s+(?:<\(\(|\(\().+)?\Z", re.DOTALL)
_INVERSE = re.compile(
    rf"Relation//({_NAME})\s+(\(\(HAS_INVERSE\)\)|<\(\(HAS_INVERSE\)\)|<-->)\s+Relation//({_NAME})\s*;?\s*\Z"
)
_INVERSE_ALIAS = re.compile(
    rf"Relation//({_NAME})\s+\(\(IS_INVERSE_ALIAS_FOR\)\)\s+Relation//({_NAME})\s*;?\s*\Z"
)
_CONDITIONAL = re.compile(r"\b(?:IF|THEN|ELSE|ALL|ANY|GROUP)\s*\(", re.IGNORECASE)


@dataclass(frozen=True)
class RegistryContribution:
    names: frozenset[str]
    inverses: tuple[tuple[str, str], ...]
    aliases: tuple[tuple[str, str], ...]


def _unsupported_metadata(source: str) -> None:
    print(
        f"Workbench: {source}: conditional/grouped CFEL relation metadata is unsupported; link skipped",
        file=sys.stderr,
    )


def relation_declaration(body: str, source: str) -> RegistryContribution:
    names: set[str] = set()
    inverses: list[tuple[str, str]] = []
    aliases: list[tuple[str, str]] = []
    for language, claim in formal_claim_fences(body):
        if language == "python":
            native = _native_contribution(claim)
            if native is not None:
                names.update(native.names)
                inverses.extend(native.inverses)
                aliases.extend(native.aliases)
                continue
            from python_model_claim import parse_python_model_claim

            block = ";\n".join(parse_python_model_claim(claim))
        elif language == "cfel":
            block = cfel_without_comments(claim)
        else:
            continue
        group_depth = 0
        for statement in model_statements(block):
            control = _CONDITIONAL.search(statement)
            grouped = group_depth > 0 or control is not None
            inverse = _INVERSE.fullmatch(statement)
            alias = _INVERSE_ALIAS.fullmatch(statement)
            if grouped:
                if _INVERSE.search(statement) or _INVERSE_ALIAS.search(statement):
                    _unsupported_metadata(source)
            elif inverse is not None:
                left, operator, right = inverse.groups()
                names.update((left, right))
                inverses.append((right, left) if operator.startswith("<((") else (left, right))
            elif alias is not None:
                aliases.append((alias.group(1), alias.group(2)))
                names.add(alias.group(2))
            elif (
                "((HAS_INVERSE))" not in statement
                and "((IS_INVERSE_ALIAS_FOR))" not in statement
                and (declaration := _DECLARATION.fullmatch(statement))
            ):
                names.add(declaration.group(1))
            if grouped:
                group_depth = max(0, group_depth + statement.count("(") - statement.count(")"))
    return RegistryContribution(frozenset(names), tuple(inverses), tuple(aliases))


def _native_contribution(claim: str) -> RegistryContribution | None:
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim

    declaration = parse_native_model_claim(claim)
    if declaration is None:
        return None
    if declaration["kind"] != "relation":
        return RegistryContribution(frozenset(), (), ())
    arguments = declaration["arguments"]
    name = _relation_name(arguments["relation_name"])
    inverse = arguments.get("inverse_alias")
    if not inverse:
        return RegistryContribution(frozenset({name}), (), ())
    inverse = _relation_name(inverse)
    pairs = arguments.get("endpoint_pairs", (arguments,))
    instance_levels = {"instances", "model_entities_or_instances"}
    if all(pair[endpoint]["level"] in instance_levels
           for pair in pairs for endpoint in ("source_endpoint", "target_endpoint")):
        return RegistryContribution(frozenset({name, inverse}), ((name, inverse),), ())
    return RegistryContribution(frozenset({name}), (), ((inverse, name),))


def _relation_name(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(_NAME, value):
        raise ValueError(f"unsupported Relation name: {value!r}")
    return value
