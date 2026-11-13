# CA-M-551@2
# CA-R-1308@27
# CA-R-1521@34
# CA-R-1539@25
# CA-R-1608@23
# CA-R-2696@3

"""Build and load a bounded, source-bound Atom Status declaration asset."""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from collections.abc import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from carrier_aliases import canonical_role_name, carrier_read_view, carrier_status_folder, matches_named_value, named_value_token
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier


class StatusModelError(ValueError):
    """A source or compiled Status model is invalid or unsupported."""


def encode_status(value: str) -> str:
    token = named_value_token(value)
    if token is None:
        raise StatusModelError('Unsupported Status name encoding')
    return token


def canonical_status(model, role, form, carried):
    allowed = model.allowed(role, form)
    encoded = {}
    for value in allowed:
        key = encode_status(value)
        if key in encoded and encoded[key] != value:
            raise StatusModelError('Ambiguous Status encoding')
        encoded[key] = value
    matches = {value for value in allowed if matches_named_value(carried, value)}
    if len(matches) != 1:
        raise StatusModelError('Status is not admitted by the applicable model')
    return matches.pop()


# The current declarations use single literal memberships only. This deliberately
# does not interpret arbitrary selectors, lists, CFEL controls, or inheritance.
_NAME = r'(?:"[^"\r\n]+"|[A-Za-z][A-Za-z0-9 &_-]*)'
_STATUS_TARGET = re.compile(r'^Atom\b.*?\.Header\.(?:State\.)?Status\s*(?=[:.{])', re.DOTALL)
_DECL = re.compile(
    rf'^Atom\s*(?:/\s*\(\s*\.Header\.(?:Context\.)?Role\s+in\s*\(\s*(?P<role>{_NAME})\s*\)\s*\)\s*)?'
    rf'(?:/\s*\(\s*\.Header\.(?:Context\.)?Form\s+in\s*\(\s*(?P<form>{_NAME})\s*\)\s*\)\s*)?'
    rf'\.Header\.(?:State\.)?Status\s*::\s*(?P<value>{_NAME})$'
)
_PLAN_BACKLOG_GROUP = re.compile(
    r'^Atom/\(\s*\.Header\.Context\.Role\s*:=\s*Plan\s*\)'
    r'/\(\s*\.Header\.State\.Status\s*:=\s*Backlog\s*\)'
    r'\.Header\.State\.Status\s*>\|\s*Status Group\s*==\s*Backlog$'
)
_STATUS_ORDER = re.compile(
    r'^Atom/\(\s*\.Header\.State\.Status\s*:=\s*(?P<status>"[^"\r\n]+"|[A-Za-z][A-Za-z0-9 _-]*)\s*\)'
    r'\.Header\.State\.Status\s*>\|\s*\(\s*Status Order Number\s*==\s*(?P<order>0|[1-9][0-9]*)\s*\)$')


def _formal_claim_blocks(body: str, *, model_class_bindings=None, skip_typed_model_properties=False) -> tuple[str, ...]:
    # Build-time only; loading an already compiled asset has no Workbench dependency.
    programmatic = Path(__file__).resolve().parents[2]
    if str(programmatic) not in sys.path:
        sys.path.insert(0, str(programmatic))
    workbench_parent = programmatic / 'FEATURE_APPS/APP_WORKBENCH'
    if str(workbench_parent) not in sys.path:
        sys.path.insert(0, str(workbench_parent))
    from FEATURE_WORKBENCH_BACKEND.declaration_cfel import formal_claim_blocks
    return formal_claim_blocks(body, model_class_bindings=model_class_bindings, skip_typed_model_properties=skip_typed_model_properties)


def _statements(block: str) -> list[str]:
    from FEATURE_WORKBENCH_BACKEND.declaration_cfel import model_statements
    return model_statements(block)


def _name(value: str | None) -> str | None:
    if value is None:
        return None
    return value[1:-1] if value.startswith('"') else value


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _validate(data: object) -> tuple[tuple[str | None, str | None, str], ...]:
    if not isinstance(data, dict) or set(data) != {'schema', 'sources', 'declarations'} or data['schema'] != 1 or type(data['schema']) is not int:
        raise StatusModelError('Invalid Status model schema')
    sources = data['sources']
    if not isinstance(sources, list) or not sources:
        raise StatusModelError('Status model requires sources')
    ids: set[str] = set()
    for source in sources:
        if (not isinstance(source, dict) or set(source) != {'atom_id', 'version'}
                or not _text(source['atom_id']) or type(source['version']) is not int or source['version'] < 1
                or source['atom_id'] in ids):
            raise StatusModelError('Invalid or duplicate Status source')
        ids.add(source['atom_id'])
    declarations = data['declarations']
    if not isinstance(declarations, list) or not declarations:
        raise StatusModelError('Status model requires declarations')
    rows = []
    seen = set()
    for row in declarations:
        if (not isinstance(row, dict) or set(row) != {'source', 'role', 'form', 'value'}
                or not _text(row['source']) or row['source'] not in ids or not _text(row['value'])
                or any(v is not None and not _text(v) for v in (row['role'], row['form']))):
            raise StatusModelError('Invalid Status declaration')
        key = (row['source'], row['role'], row['form'], row['value'])
        if key in seen:
            raise StatusModelError('Duplicate Status declaration')
        seen.add(key)
        rows.append((row['role'], row['form'], row['value']))
    if not any(role is None and form is None for role, form, _ in rows):
        raise StatusModelError('Status model requires base declarations')
    return tuple(rows)


@dataclass(frozen=True)
class StatusModel:
    _rows: tuple[tuple[str | None, str | None, str], ...]
    candidate_schema: object | None = None

    def allowed(self, role: str, form: str) -> frozenset[str]:
        if not _text(role) or not _text(form):
            raise StatusModelError('Role and Form must be nonempty exact strings')
        role = canonical_role_name(role)
        return frozenset(value for r, f, value in self._rows
                         if (r is None or canonical_role_name(r) == role) and (f is None or f == form))


def compile_status_model(paths: Iterable[Path], *, model_class_bindings=None) -> bytes:
    """Compile only the supplied native current Declaration carriers."""
    sources = []
    declarations = []
    for supplied in paths:
        path = Path(supplied)
        try:
            carrier = parse_carrier(path.read_bytes(), path)
        except (OSError, ValueError) as error:
            raise StatusModelError(f'{path}: invalid source: {error}') from error
        meta = carrier_read_view(carrier.metadata)
        atom_id, version = meta.get('atom_id'), meta.get('version')
        if (not _text(atom_id) or type(version) is not int or version < 1
                or not matches_named_value(meta.get('role'), 'Requirement')
                or not matches_named_value(meta.get('form'), 'Declaration')
                or meta.get('status') not in {'Active', 'active'}):
            raise StatusModelError(f'{path}: expected an Active Requirement Declaration with ID and version')
        sources.append({'atom_id': atom_id, 'version': version})
        blocks = _formal_claim_blocks(carrier.body, model_class_bindings=model_class_bindings)
        if not blocks:
            raise StatusModelError(f'{path}: missing formal CFEL block')
        for block in blocks:
            for expression in _statements(block):
                if (_PLAN_BACKLOG_GROUP.fullmatch(expression) or _STATUS_ORDER.fullmatch(expression)
                        or _STATUS_TARGET.match(expression) is None):
                    continue
                # Property shape declarations do not introduce allowed literals.
                if re.match(r'^Atom\.Header\.(?:State\.)?Status(?:\{|\.\*)', expression):
                    continue
                match = _DECL.fullmatch(expression)
                if match is None:
                    raise StatusModelError(f'{path}: unsupported Status declaration: {expression}')
                declarations.append({'source': atom_id, 'role': _name(match['role']),
                                     'form': _name(match['form']), 'value': _name(match['value'])})
    sources.sort(key=lambda x: x['atom_id'])
    declarations.sort(key=lambda x: (x['source'], x['role'] or '', x['form'] or '', x['value']))
    data = {'schema': 1, 'sources': sources, 'declarations': declarations}
    _validate(data)
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def load_status_model(path: Path) -> StatusModel:
    def unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result = {}
        for key, value in pairs:
            if key in result:
                raise StatusModelError('Duplicate JSON key in Status model')
            result[key] = value
        return result
    try:
        data = json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique)
        return StatusModel(_validate(data))
    except (OSError, UnicodeError, json.JSONDecodeError, TypeError) as error:
        raise StatusModelError(f'Invalid Status model asset: {error}') from error


def _staged_declarations(root: Path) -> list[Path]:
    """Find current Status declarations solely in the supplied staged sources."""
    if not root.is_dir():
        raise StatusModelError(f'{root}: staged model root is not a directory')
    found = []
    for path in sorted(root.rglob('CA-R-*.md')):
        if any(carrier_status_folder(part) in {'archived', 'draft'} for part in path.relative_to(root).parts):
            continue
        try:
            carrier = parse_carrier(path.read_bytes(), path)
        except (OSError, ValueError) as error:
            raise StatusModelError(f'{path}: invalid staged source: {error}') from error
        meta = carrier_read_view(carrier.metadata)
        if (meta.get('status') not in {'Active', 'active'}
                or not matches_named_value(meta.get('role'), 'Requirement')
                or not matches_named_value(meta.get('form'), 'Declaration')):
            continue
        blocks = _formal_claim_blocks(carrier.body, skip_typed_model_properties=True)
        if any(_STATUS_TARGET.match(statement)
               for block in blocks for statement in _statements(block)):
            found.append(path)
    if not found:
        raise StatusModelError(f'{root}: no current Status declarations in staged sources')
    return found


def _main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description='Compile Status declarations from staged model sources')
    parser.add_argument('--model-root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        payload = compile_status_model(_staged_declarations(args.model_root))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(payload)
    except (StatusModelError, OSError) as error:
        parser.exit(1, f'Status model build failed: {error}\n')


if __name__ == '__main__':
    _main()
