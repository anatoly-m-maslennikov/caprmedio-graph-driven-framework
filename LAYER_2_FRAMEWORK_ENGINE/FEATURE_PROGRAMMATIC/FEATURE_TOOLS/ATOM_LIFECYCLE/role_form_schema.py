"""Finite literal Role and Form declarations for lifecycle candidate checks."""
from __future__ import annotations

from dataclasses import dataclass
import re

from FEATURE_WORKBENCH_BACKEND.declaration_cfel import formal_claim_blocks, model_statements
from FEATURE_WORKBENCH_BACKEND.declaration_ancestry import compile_ancestry
from carrier_aliases import canonical_role_name, matches_named_value, named_value_token

_NAME = r'(?:"[^"\r\n]+"|[A-Za-z][A-Za-z0-9 &_-]*)'
_ROLE = re.compile(rf'^Atom\.Header\.(?:Context\.)?Role\s*::\s*({_NAME})$')
_FORM = re.compile(rf'^Atom(?:/\(\s*\.Header\.(?:Context\.)?Role\s+in\s*\(\s*({_NAME})\s*\)\s*\))?\.Header\.(?:Context\.)?Form\s*::\s*({_NAME})$')
_PROJECTED_FORM = re.compile(r'^Atom//\$declared\.Header\.(?:Context\.)?Form\s*::\s*\[\s*in\s*\(')
_EACH = re.compile(
    rf'FOR\s+EACH\s+\$(?P<var>\w+)\[<Atom>,\s*\(\.Header\.(?:Context\.)?Form\s*=\s*(?P<form>{_NAME})\)\]\s*:\s*\('
    rf'\s*\$(?P=var)\.Header\.(?:Context\.)?Role\s*(?:(?:==\s*(?P<single>{_NAME}))|(?:\s*::\s*\[\s*in\s*\((?P<list>[^()]*)\)\s*\]\s*\{{\s*::\s*1\s*\}}))\s*(?:;|(?=\)))', re.I)


def _name(value):
    value = value.strip()
    return value[1:-1] if value.startswith('"') and value.endswith('"') else value


def compile_role_form(rows):
    records = set()
    statements = []
    for row in rows:
        source = row['id']
        for block in formal_claim_blocks(row['_content_bytes'].decode('utf-8'), model_class_bindings=row.get('_model_class_bindings')):
            for statement in model_statements(block):
                statements.append((statement, source))
                if match := _ROLE.fullmatch(statement):
                    records.add(('role', _name(match[1]), '', source))
                elif match := _FORM.fullmatch(statement):
                    role, form = match.groups()
                    records.add(('qualified' if role else 'form', _name(form), _name(role) if role else '', source))
            for match in _EACH.finditer(block):
                role_text = match['single'] or match['list']
                roles = [_name(item) for item in role_text.split(',')]
                if not roles or any(not re.fullmatch(_NAME, item) for item in roles):
                    raise ValueError(f"{source}: unsupported Form Role constraint")
                for role in roles:
                    records.add(('constraint', _name(match['form']), role, source))
    records.update(_projected_bindings(statements))
    return [dict(zip(('kind', 'value', 'role', 'source'), item)) for item in sorted(records)]


def _projected_bindings(statements):
    for projected in compile_ancestry(statements):
        if _PROJECTED_FORM.match(projected.statement):
            for role in projected.roles or ():
                for form in projected.forms or ():
                    yield 'qualified', form, role, projected.source


@dataclass(frozen=True)
class RoleFormSchema:
    roles: frozenset[str]
    forms: frozenset[str]
    qualified: frozenset[tuple[str, str]]
    constraints: tuple[tuple[str, frozenset[str]], ...]

    def names(self, field):
        if field == 'role':
            return self.roles
        return self.forms | {form for _, form in self.qualified}

    def decode(self, field, carried):
        if field == 'role':
            carried = canonical_role_name(carried)
        matches = {name for name in self.names(field) if matches_named_value(carried, name)}
        if len(matches) > 1:
            raise ValueError(f'Ambiguous {field} Carrier spelling.')
        return next(iter(matches), carried)

    def encode(self, field, canonical):
        if not isinstance(canonical, str) or canonical not in self.names(field):
            return canonical
        token = named_value_token(canonical)
        if token is None:
            return canonical
        if self.decode(field, token) != canonical:
            raise ValueError(f'Ambiguous {field} Carrier spelling.')
        return token

    def validate(self, role, form):
        if role not in self.roles:
            raise ValueError(f'Role is not declared: {role}')
        qualified_roles = {declared_role for declared_role, declared_form in self.qualified if declared_form == form}
        if qualified_roles and form not in self.forms and role not in qualified_roles:
            raise ValueError(f'Role {role} is not permitted for Form {form}; allowed: {", ".join(sorted(qualified_roles))}')
        for constrained_form, allowed in self.constraints:
            if form == constrained_form and role not in allowed:
                raise ValueError(f'Role {role} is not permitted for Form {form}; allowed: {", ".join(sorted(allowed))}')


def load_role_form(records, source_ids):
    if not isinstance(records, list):
        raise ValueError('invalid Role/Form records')
    seen = set()
    roles, forms, qualified, constraints = set(), set(), set(), {}
    for row in records:
        if not isinstance(row, dict) or set(row) != {'kind', 'value', 'role', 'source'}:
            raise ValueError('invalid Role/Form record')
        kind, value, role, source = (row[k] for k in ('kind', 'value', 'role', 'source'))
        if (kind not in {'role', 'form', 'qualified', 'constraint'} or not isinstance(value, str) or not value
                or not isinstance(role, str) or not isinstance(source, str) or source not in source_ids
                or (kind in {'role', 'form'} and role) or (kind in {'qualified', 'constraint'} and not role)):
            raise ValueError('invalid Role/Form record')
        key = (kind, value, role, source)
        if key in seen:
            raise ValueError('duplicate Role/Form record')
        seen.add(key)
        if kind == 'role':
            roles.add(value)
        elif kind == 'form':
            forms.add(value)
        elif kind == 'qualified':
            qualified.add((role, value))
        else:
            constraints.setdefault((value, source), set()).add(role)
    return RoleFormSchema(frozenset(roles), frozenset(forms), frozenset(qualified),
                          tuple((form, frozenset(allowed)) for (form, _), allowed in sorted(constraints.items())))
