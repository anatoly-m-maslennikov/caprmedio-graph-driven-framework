# CA-M-465@24
# CA-M-509@1

"""Compile literal Current Relation declarations without evaluating CFEL."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
import re
import sys
from typing import Any

from markdown_it import MarkdownIt

from .markdown_content import source_markdown


TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from carrier_aliases import carrier_read_view  # noqa: E402


_NAME = r"[A-Za-z_][A-Za-z_0-9]*"
_RELATION = re.compile(rf"Relation//({_NAME})(?![A-Za-z_0-9])")
_INVERSE = re.compile(
    rf"Relation//({_NAME})\s+(\(\(HAS_INVERSE\)\)|<\(\(HAS_INVERSE\)\)|<-->)\s+Relation//({_NAME})\s*;?\s*\Z"
)
_INVERSE_ALIAS = re.compile(
    rf"Relation//({_NAME})\s+\(\(IS_INVERSE_ALIAS_FOR\)\)\s+Relation//({_NAME})\s*;?\s*\Z"
)
_CONDITIONAL = re.compile(r"\b(?:IF|THEN|ELSE|ALL|ANY|GROUP)\s*\(", re.IGNORECASE)
_THEN = re.compile(r"\b(?:THEN|ELSE|ALL|ANY|GROUP)\s*\(", re.IGNORECASE)


@dataclass(frozen=True)
class RegistryContribution:
    names: frozenset[str]
    inverses: tuple[tuple[str, str], ...]
    aliases: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class RelationRegistry:
    names: frozenset[str]
    inverse: dict[str, str]
    aliases: dict[str, str]
    collisions: frozenset[str]


@dataclass(frozen=True)
class RegistryCompilation:
    registry: RelationRegistry
    contributions: dict[str, RegistryContribution]
    declaration_rows: tuple[dict[str, Any], ...]


def _subjects(header: Mapping[str, Any]) -> list[str]:
    subjects = carrier_read_view(dict(header)).get("subjects", {})
    active = (
        subjects.get("active", subjects.get("governs", [])) if isinstance(subjects, dict) else []
    )
    if isinstance(active, str):
        return [active]
    return [item for item in active if isinstance(item, str)] if isinstance(active, list) else []


def _unsupported_metadata(source: str) -> None:
    print(
        f"Workbench: {source}: conditional/grouped CFEL relation metadata is unsupported; link skipped",
        file=sys.stderr,
    )


def _literal_metadata(
    body: str, source: str
) -> tuple[tuple[tuple[str, str], ...], tuple[tuple[str, str], ...]]:
    inverses: list[tuple[str, str]] = []
    aliases: list[tuple[str, str]] = []
    for token in MarkdownIt("commonmark").parse(body):
        if token.type != "fence" or token.info.strip().upper() != "CFEL":
            continue
        conditional_pending = False
        group_depth = 0
        for line in token.content.splitlines():
            stripped = line.strip()
            control = _CONDITIONAL.search(stripped)
            grouped = conditional_pending or group_depth > 0 or control is not None
            inverse = _INVERSE.fullmatch(stripped)
            alias = _INVERSE_ALIAS.fullmatch(stripped)
            if grouped and (inverse is not None or alias is not None):
                _unsupported_metadata(source)
            elif inverse is not None:
                left, operator, right = inverse.groups()
                inverses.append((right, left) if operator.startswith("<((") else (left, right))
            elif alias is not None:
                aliases.append((alias.group(1), alias.group(2)))
            if control is not None:
                conditional_pending = True
                opener = _THEN.search(stripped)
                if opener is not None:
                    group_depth += stripped[opener.start() :].count("(") - stripped[
                        opener.start() :
                    ].count(")")
                    conditional_pending = group_depth > 0
            elif group_depth:
                group_depth += stripped.count("(") - stripped.count(")")
                conditional_pending = group_depth > 0
    return tuple(inverses), tuple(aliases)


def _declaration_identity(row: Mapping[str, Any]) -> tuple[str, str, int] | None:
    source = row.get("source_path")
    atom_id = row.get("id")
    version = row.get("version")
    if (
        isinstance(source, str)
        and source
        and isinstance(atom_id, str)
        and atom_id
        and type(version) is int
        and version > 0
    ):
        return source, atom_id, version
    print(
        f"Workbench: {source!r}: Current Relation declaration needs a source path, Atom ID, and positive integer Version; skipped",
        file=sys.stderr,
    )
    return None


def registry_contribution(row: Mapping[str, Any]) -> RegistryContribution:
    """Return one valid source's literal registry input without evaluating CFEL."""
    if row.get("status_group") != "Current" or row.get("role") != "Requirement":
        return RegistryContribution(frozenset(), (), ())
    if row.get("form") not in {
        "Declaration",
        "Definition",
        "Entity Definition",
        "Relation Declaration",
        "Relation Definition",
    }:
        return RegistryContribution(frozenset(), (), ())
    identity = _declaration_identity(row)
    if identity is None:
        return RegistryContribution(frozenset(), (), ())
    source, _atom_id, _version = identity
    names = frozenset(
        name
        for subject in _subjects(row.get("header_json", {}))
        for name in _RELATION.findall(subject)
    )
    inverses, aliases = _literal_metadata(source_markdown(row) or "", source)
    return RegistryContribution(names, inverses if names else (), aliases if names else ())


def _unambiguous_inverses(bindings: list[tuple[str, str]]) -> dict[str, str]:
    pairs = set(bindings)
    targets_by_direct: dict[str, set[str]] = defaultdict(set)
    owners_by_target: dict[str, set[str]] = defaultdict(set)
    for direct, derived in pairs:
        targets_by_direct[direct].add(derived)
        owners_by_target[derived].add(direct)
    derived_as_direct = {
        direct
        for direct in targets_by_direct
        if any(owner != direct for owner in owners_by_target[direct])
    }
    rejected = {
        (direct, derived)
        for direct, derived in pairs
        if direct == derived
        or len(targets_by_direct[direct]) > 1
        or len(owners_by_target[derived]) > 1
        or direct in derived_as_direct
        or derived in derived_as_direct
    }
    for direct, derived in sorted(pairs):
        if direct == derived:
            print(
                f"Workbench: ambiguous inverse binding {direct} -> {derived}: self-pair",
                file=sys.stderr,
            )
    for direct, targets in sorted(targets_by_direct.items()):
        if len(targets) > 1:
            print(
                f"Workbench: ambiguous inverse bindings for {direct}: multiple inverses {', '.join(sorted(targets))}",
                file=sys.stderr,
            )
    for derived, owners in sorted(owners_by_target.items()):
        if len(owners) > 1:
            print(
                f"Workbench: ambiguous inverse bindings for {derived}: multiple direct owners {', '.join(sorted(owners))}",
                file=sys.stderr,
            )
    for direct in sorted(derived_as_direct):
        print(
            f"Workbench: ambiguous inverse binding: derived Relation {direct} is declared direct",
            file=sys.stderr,
        )
    return {direct: derived for direct, derived in pairs - rejected}


def registry_from_contributions(
    contributions: Mapping[str, RegistryContribution],
) -> tuple[set[str], dict[str, str], set[str]]:
    registered: set[str] = set()
    origins: dict[str, set[str]] = defaultdict(set)
    bindings: list[tuple[str, str]] = []
    for source, contribution in contributions.items():
        registered.update(contribution.names)
        for name in contribution.names:
            origins[name].add(source)
        bindings.extend(contribution.inverses)
    collisions = _case_collisions(registered, origins)
    registered.difference_update(collisions)
    admitted = [
        (direct, derived)
        for direct, derived in bindings
        if direct in registered and derived in registered
    ]
    return registered, _unambiguous_inverses(admitted), collisions


def _unambiguous_aliases(
    contributions: Mapping[str, RegistryContribution],
    registered: set[str],
) -> dict[str, str]:
    targets: dict[str, set[str]] = defaultdict(set)
    sources: dict[str, set[str]] = defaultdict(set)
    for source, contribution in contributions.items():
        for alias, direct in contribution.aliases:
            targets[alias].add(direct)
            sources[alias].add(source)
    aliases: dict[str, str] = {}
    for alias, direct in sorted(
        (name, next(iter(values))) for name, values in targets.items() if len(values) == 1
    ):
        if alias in registered:
            print(
                f"Workbench: ambiguous inverse alias {alias}; canonical Relation already registered; link skipped",
                file=sys.stderr,
            )
        elif direct not in registered:
            print(
                f"Workbench: inverse alias {alias} has unknown canonical Relation {direct}; link skipped",
                file=sys.stderr,
            )
        else:
            aliases[alias] = direct
    for alias, target_names in sorted(targets.items()):
        if len(target_names) > 1:
            print(
                f"Workbench: ambiguous inverse aliases for {alias}: {', '.join(sorted(target_names))}; sources: {', '.join(sorted(sources[alias]))}; link skipped",
                file=sys.stderr,
            )
    return aliases


def _case_collisions(registered: set[str], origins: Mapping[str, set[str]]) -> set[str]:
    names_by_case: dict[str, set[str]] = defaultdict(set)
    for name in registered:
        names_by_case[name.casefold()].add(name)
    collisions = set()
    for names in sorted(names_by_case.values(), key=lambda value: sorted(value)):
        if len(names) < 2:
            continue
        collisions.update(names)
        detail = "; ".join(
            f"{name}: {', '.join(sorted(origins.get(name, ()) or ('<unknown>',)))}"
            for name in sorted(names)
        )
        print(
            "Workbench: ambiguous Relation definitions differ only by case: "
            f"{', '.join(sorted(names))}; sources: {detail}; links skipped",
            file=sys.stderr,
        )
    return collisions


def _warn_colliding_uses(
    atoms: list[dict[str, Any]], collisions: set[str] | frozenset[str]
) -> None:
    variants_by_case: dict[str, list[str]] = defaultdict(list)
    for name in collisions:
        variants_by_case[name.casefold()].append(name)
    for row in atoms:
        relations = row.get("header_json", {}).get("relations", {})
        if not isinstance(relations, dict):
            continue
        source = row.get("source_path")
        if not isinstance(source, str):
            continue
        for name in sorted(key for key in relations if isinstance(key, str)):
            variants = variants_by_case.get(name.casefold())
            if variants:
                print(
                    f"Workbench: {source}: ambiguous registered Relation {name}; candidates: {', '.join(sorted(variants))}; link skipped",
                    file=sys.stderr,
                )


def compile_registry(atoms: list[dict[str, Any]]) -> RegistryCompilation:
    """Compile one captured inventory and retain its declared source rows once."""
    contributions = {}
    declaration_rows = {}
    for row in atoms:
        contribution = registry_contribution(row)
        source = row.get("source_path")
        if isinstance(source, str):
            contributions[source] = contribution
            if contribution.names:
                declaration_rows[source] = row
    registered, inverse, collisions = registry_from_contributions(contributions)
    aliases = _unambiguous_aliases(contributions, registered)
    registry = RelationRegistry(frozenset(registered), inverse, aliases, frozenset(collisions))
    return RegistryCompilation(registry, contributions, tuple(declaration_rows.values()))


def compile_relation_registry(atoms: list[dict[str, Any]]) -> RelationRegistry:
    """Compile the declared literal relation registry from one captured inventory."""
    return compile_registry(atoms).registry
