# CA-M-500@12
"""Compile the literal named ancestry needed by the Atom schema projection.

This is deliberately not a CFEL evaluator. Inputs are already extracted Formal
Claim statements; unrecognized expressions never introduce names or edges.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import re
from typing import Generic, Iterable, Iterator, TypeVar

from .declaration_cfel import filters

S = TypeVar('S')
_NAME = r'[A-Za-z_][A-Za-z_0-9 -]*?'
_REL = re.compile(rf'^\s*({_NAME})\s*\(\((NARROWER_THAN|INSTANCE_OF)\)\)\s*(.+?)\s*$')
_BINDING = re.compile(rf'^\s*({_NAME})\.Header\.(?:Context\.)?(Role|Form)\s*::\s*\[\s*in\s*\(([^()]*)\)\s*\]')
_PROPERTY = re.compile(r'\.(?:Content|Header)(?=\.|\s|\[|\{|::|$)')


@dataclass(frozen=True)
class ProjectedStatement(Generic[S]):
    statement: str
    source: S
    roles: frozenset[str] | None = None
    forms: frozenset[str] | None = None
    provenance: tuple[S, ...] = ()
    original_statement: str = ""
    constraints: str = ""


def _path(text: str) -> tuple[list[tuple[str, str, str]], str] | None:  # noqa: C901
    """Return named nodes and their incoming selectors; reject unsupported paths."""
    match = re.match(rf'\s*({_NAME})(?=\s*(?:/|$))', text)
    if not match:
        return None
    nodes = [(match.group(1).strip(), '', '')]
    pos = match.end()
    pending = ''
    while pos < len(text):
        while pos < len(text) and text[pos].isspace():
            pos += 1
        if pos == len(text):
            break
        if text[pos] != '/':
            return None
        op = '//' if text.startswith('//', pos) else '/'
        pos += len(op)
        if pos < len(text) and text[pos] == '(':
            start = pos
            depth = 0
            while pos < len(text):
                if text[pos] == '(':
                    depth += 1
                if text[pos] == ')':
                    depth -= 1
                pos += 1
                if depth == 0:
                    break
            if depth:
                return None
            pending += '/'+text[start:pos]
            continue
        m = re.match(r'\s*([^/]+)', text[pos:])
        if not m:
            return None
        name = m.group(1).strip()
        if name.startswith('$'):
            # Variables denote populations, not reusable names, and must end the path.
            if '/' in text[pos + m.end():]:
                return None
            pos += m.end()
            break
        if not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9 -]*', name):
            return None
        nodes.append((name, op, pending))
        pending = ''
        pos += m.end()
    return nodes, pending


def _intersect(a: frozenset[str] | None, b: frozenset[str] | None) -> frozenset[str] | None:
    return b if a is None else a if b is None else a & b


def _form_role_constraints(items: tuple[tuple[str, S], ...]) -> list[tuple[S, str, frozenset[str]]]:
    """Recognize the two literal, source-local population declarations."""
    populations: list[tuple[S, str, str]] = []
    constraints: list[tuple[S, str, frozenset[str]]] = []
    for statement, source in items:
        match = re.fullmatch(
            r'\s*Atom/\(\.Header\.(?:Context\.)?Form\s*:=\s*([^()]+)\)//\$[A-Za-z_][A-Za-z_0-9]*'
            r'\.Header\.(?:Context\.)?Role\s*::\s*\[\s*in\s*\(([^()]*)\)\s*\]\s*\{::1\}\s*', statement,
        )
        if match:
            form, value = match.groups()
            roles = filters('/(.Header.Role in (' + value + '))', 'Role')
            if roles is not None:
                constraints.append((source, form.strip(), roles))
        population = re.fullmatch(
            r'\s*\$([A-Za-z_][A-Za-z_0-9]*)\[<Atom>,\s*\(\.Header\.(?:Context\.)?Form\s*=\s*([^()]+)\)\]\s*', statement,
        )
        if population:
            variable, form = population.groups()
            populations.append((source, variable, form.strip()))
    for statement, source in items:
        match = re.fullmatch(r'\s*\$([A-Za-z_][A-Za-z_0-9]*)\.Header\.(?:Context\.)?Role\s*==\s*([A-Za-z_][A-Za-z_0-9 ]*)\s*', statement)
        if match:
            variable, role = match.groups()
            constraints.extend((source, form, frozenset({role.strip()})) for owner, name, form in populations
                               if owner == source and name == variable)
    return constraints


def compile_ancestry(statements: Iterable[tuple[str, S]]) -> tuple[ProjectedStatement[S], ...]:  # noqa: C901
    """Return direct Atom expressions and conservatively projected named properties."""
    items = tuple(statements)
    form_roles = _form_role_constraints(items)
    aliases = defaultdict(set)
    parsed_items = []
    relations = []
    direct_statements = []
    for statement, source in items:
        relation = _REL.fullmatch(statement)
        if relation:
            child_name, _, parent_path = relation.groups()
            parent = _path(parent_path) if '$' not in parent_path else None
            if parent:
                nodes, trailing = parent
                aliases[child_name.strip()].add((child_name.strip(),))
                address = (nodes[0][0],)
                aliases[nodes[0][0]].add(address)
                for name, op, _ in nodes[1:]:
                    address += (op, name)
                    aliases[name].add(address)
                relations.append((child_name.strip(), nodes, trailing, source))
            continue
        prop = next((m for m in _PROPERTY.finditer(statement) if statement[:m.start()].count('(') == statement[:m.start()].count(')')), None)
        parsed = _path(statement[:prop.start()] if prop else statement)
        if not parsed:
            if statement.startswith("Atom") and not re.match(r"Atom/\*", statement):
                direct_statements.append((statement, source))
            continue
        nodes, trailing = parsed
        if statement.startswith("Atom") and (not prop or len(nodes) == 1):
            direct_statements.append((statement, source))
        address: tuple[str, ...] = (nodes[0][0],)
        aliases[nodes[0][0]].add(address)
        for name, op, _ in nodes[1:]:
            address += (op, name)
            aliases[name].add(address)
        parsed_items.append((statement, source, prop, nodes, trailing))

    def resolve(name: str) -> tuple[str, ...] | None:
        choices = aliases.get(name, set())
        extended = {a for a in choices if len(a) > 1}
        choices = extended or choices
        return next(iter(choices)) if len(choices) == 1 else None

    edges = defaultdict(list)
    bindings = defaultdict(list)
    properties = []
    result = []
    for statement, source, prop, nodes, trailing in parsed_items:
        first = resolve(nodes[0][0]) or (nodes[0][0],)
        address = first
        for name, op, selector in nodes[1:]:
            child = address + (op, name)
            edges[child].append((address, selector, source))
            address = child
        if prop:
            suffix = statement[prop.start():]
            properties.append((statement, source, address, trailing, suffix))
            binding = re.match(r'^\.Header\.(?:Context\.)?(Role|Form)\s*::\s*\[\s*in\s*\(([^()]*)\)\s*\]', suffix)
            if binding:
                field, raw = binding.groups()
                vals = frozenset(v.strip().strip("\"'") for v in raw.split(',') if v.strip())
                if vals:
                    bindings[address].append((field, vals, source))
    for child_name, nodes, trailing, source in relations:
        address = resolve(nodes[0][0]) or (nodes[0][0],)
        for name, op, selector in nodes[1:]:
            child = address + (op, name)
            edges[child].append((address, selector, source))
            address = child
        child = resolve(child_name)
        if child is not None:
            edges[child].append((address, trailing, source))
    for statement, source in direct_statements:
        roles = None
        prop = next((m for m in _PROPERTY.finditer(statement) if statement[:m.start()].count('(') == statement[:m.start()].count(')')), None)
        if prop and statement.startswith('Atom/'):
            try:
                selected_forms = filters(statement[:prop.start()], 'Form')
                for owner, form, allowed in form_roles:
                    if owner == source and selected_forms == frozenset({form}):
                        roles = _intersect(roles, allowed)
            except ValueError:
                # Existing direct-declaration validation reports unsupported selectors.
                pass
        result.append(ProjectedStatement(statement, source, roles=roles, provenance=(source,), original_statement=statement))

    def paths(address: tuple[str, ...], visited: frozenset[tuple[str, ...]]) -> Iterator[tuple[str, tuple[S, ...], tuple[tuple[str, ...], ...]]]:
        if address == ('Atom',):
            yield '', (), ()
            return
        if address in visited:
            return
        for parent, selector, src in edges.get(address, ()):
            for prior, provenance, names in paths(parent, visited | {address}):
                yield prior + selector, provenance + (src,), names + (address,)

    from .declaration_cfel import _filter_groups
    for original, source, address, trailing, suffix in properties:
        if original.startswith('Atom') and address == ('Atom',):
            continue
        for selectors, provenance, names in paths(address, frozenset()):
            roles = forms = None
            for group in _filter_groups(selectors + trailing):
                try:
                    roles = _intersect(roles, filters('/(' + group + ')', 'Role'))
                    forms = _intersect(forms, filters('/(' + group + ')', 'Form'))
                except ValueError:
                    roles = frozenset()
            binding_sources = []
            for node in names:
                for field, values, binding_source in bindings.get(node, ()):
                    if field == 'Role':
                        roles = _intersect(roles, values)
                    else:
                        forms = _intersect(forms, values)
                    binding_sources.append(binding_source)
            if not any(field == 'Form' for field, _, _ in bindings.get(address, ())):
                roles = frozenset()
            result.append(ProjectedStatement('Atom//$declared' + suffix, source, roles, forms,
                                             provenance + tuple(binding_sources) + (source,), original, selectors + trailing))
    return tuple(result)
