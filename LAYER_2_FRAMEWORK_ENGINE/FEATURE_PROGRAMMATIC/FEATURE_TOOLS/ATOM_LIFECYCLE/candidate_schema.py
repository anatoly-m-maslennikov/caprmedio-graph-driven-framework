# CA-M-551@2
# CA-O-10002@2

"""Build a candidate-validation schema from explicitly staged model sources."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parents[1]
WORKBENCH = TOOLS.parent / 'FEATURE_APPS/APP_WORKBENCH'
sys.path.insert(0, str(TOOLS.parent))
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(WORKBENCH))

from ATOM_LIFECYCLE.content_constraints import compile_content_constraints, load_content_constraints  # noqa: E402
from ATOM_LIFECYCLE.header_constraints import compile_header_constraints, load_header_constraints  # noqa: E402
from ATOM_LIFECYCLE.placement_model import compile_placement, load_placement  # noqa: E402
from ATOM_LIFECYCLE.role_form_schema import compile_role_form, load_role_form  # noqa: E402
from carrier_aliases import canonical_role_name, carrier_read_view, carrier_status_folder, matches_named_value, named_value_token  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from header_groups import header_value  # noqa: E402
from subject_notation import SubjectNotationError, parse_subject_expression, render_subject  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import (  # noqa: E402
    compile_schema, load_image_schema, schema_asset,
)

from ATOM_LIFECYCLE.placement_sources import bootstrap_rows, inventory, read_selected  # noqa: E402
from FEATURE_FORMAL_MODEL_ENGINE.topic_dependencies import (  # noqa: E402
    Atom, DEPENDENCIES_CLAIM_SHA256, dependencies_are_distinct, verify_packaged_dependencies_check,
)

_DEPENDENCIES_SUBJECT = 'CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics.Dependencies'


@dataclass(frozen=True)
class CandidateSchema:
    workbench: object
    role_form: object
    header_constraints: object
    content_constraints: object
    placement: object = None
    atom_dependencies_check: bool = False

    def header(self, mode):
        return self.workbench.header(mode)

    @property
    def content(self):
        return self.workbench.content

    def validate_role_form(self, role, form):
        self.role_form.validate(role, form)

    def validate_atom_dependencies(self, metadata):
        present, values = header_value(metadata, 'topics.dependencies')
        if not present:
            return
        if isinstance(values, dict) and set(values) <= {'continuant', 'occurrent'} and all(
            isinstance(group, list) for group in values.values()
        ):
            values = [item for group in values.values() for item in group]
        if not isinstance(values, list) or any(type(value) is not str for value in values):
            raise ValueError('Topic Dependencies require a list of strings.')
        if not dependencies_are_distinct(Atom(tuple(values))):
            raise ValueError('Topic Dependencies must be distinct.')


class _MemoryAsset:
    def __init__(self, payload):
        self.payload = payload

    def is_symlink(self):
        return False

    def is_file(self):
        return True

    def read_bytes(self):
        return json.dumps(self.payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def _canonical(payload):
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def load_candidate_schema(path: Path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError('candidate schema is missing or is a symlink')
    try:
        payload = json.loads(path.read_bytes())
        required = {
            'schema_version', 'workbench', 'role_form', 'header_constraints', 'content_constraints', 'digest',
        }
        if not isinstance(payload, dict) or not required <= payload.keys() <= required | {'placement', 'atom_dependencies_check'}:
            raise ValueError('invalid candidate schema shape')
        digest = payload.pop('digest')
        if payload['schema_version'] != 2 or type(payload['schema_version']) is not int:
            raise ValueError('unsupported candidate schema version')
        if digest != hashlib.sha256(_canonical(payload)).hexdigest():
            raise ValueError('candidate schema digest mismatch')
        workbench = load_image_schema(_MemoryAsset(payload['workbench']))
        source_pins = payload['workbench']['sources']
        source_ids = {pin['atom_id'] for pin in source_pins}
        check = 'atom_dependencies_check' in payload
        if check:
            pin = payload['atom_dependencies_check']
            if (not isinstance(pin, dict) or set(pin) != {'claim_sha256', 'source'}
                    or pin['claim_sha256'] != DEPENDENCIES_CLAIM_SHA256
                    or source_pins.count(pin['source']) != 1):
                raise ValueError('Invalid reviewed Atom Dependencies check')
            verify_packaged_dependencies_check()
        return CandidateSchema(workbench, load_role_form(payload['role_form'], source_ids),
                               load_header_constraints(payload['header_constraints'], source_ids),
                               load_content_constraints(payload['content_constraints'], source_ids),
                               load_placement(payload['placement']) if 'placement' in payload else None, check)
    except (OSError, KeyError, TypeError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f'invalid candidate schema: {error}') from error


def _dependencies_declaration(rows):
    from FEATURE_FORMAL_MODEL_ENGINE.model_catalog import _native_block
    from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim

    selected = None
    for row in rows:
        _, subject = header_value(row['header_json'], 'topics.main_subject')
        canonical = None
        if isinstance(subject, str):
            try:
                canonical = render_subject(parse_subject_expression(subject))
            except SubjectNotationError:
                pass
        body = row['_content_bytes']
        if canonical == _DEPENDENCIES_SUBJECT:
            if selected is not None:
                raise ValueError(f'Multiple Current Declarations for {_DEPENDENCIES_SUBJECT}')
            selected = row
        elif b'dependencies_are_distinct' in body:
            for code in _native_block(body.decode('utf-8')):
                if 'dependencies_are_distinct' in code:
                    parsed = parse_native_model_claim(code)
                    if parsed and (parsed.get('instance_check') or {}).get('name') == 'dependencies_are_distinct':
                        raise ValueError(f"{row['source_path']}: Atom Dependencies check requires {_DEPENDENCIES_SUBJECT}")
    if selected is None:
        return None
    blocks = tuple(_native_block(selected['_content_bytes'].decode('utf-8')))
    if not blocks:
        return None
    if len(blocks) != 1 or hashlib.sha256(blocks[0].encode()).hexdigest() != DEPENDENCIES_CLAIM_SHA256:
        raise ValueError(f"{selected['source_path']}: Atom Dependencies differs from the reviewed Python Claim")
    verify_packaged_dependencies_check()
    return selected['source_path']


def compile_candidate_schema(root: Path, placement_selection: Path | None = None) -> bytes:  # noqa: C901
    """Compile Active Requirement/Declaration carriers from this root only."""
    root = Path(root)
    if not root.is_dir():
        raise ValueError(f'{root}: staged model root is not a directory')
    rows = []
    seen = set()
    for path in sorted(root.rglob('CA-R-*.md')):
        relative = path.relative_to(root)
        if any(carrier_status_folder(part) in {'archived', 'draft'} for part in relative.parts):
            continue
        raw = path.read_bytes()
        carrier = parse_carrier(raw, path)
        view = carrier_read_view(carrier.metadata)
        if (view.get('status') not in ('Active', 'active')
                or not matches_named_value(view.get('role'), 'Requirement')
                or not matches_named_value(view.get('form'), 'Declaration')):
            continue
        atom_id, version = view.get('atom_id'), view.get('version')
        if not isinstance(atom_id, str) or not atom_id.strip() or type(version) is not int or version < 1:
            raise ValueError(f'{path}: declaration requires ID and version')
        if atom_id in seen:
            raise ValueError(f'{path}: duplicate declaration ID {atom_id}')
        seen.add(atom_id)
        rows.append({'source_path': relative.as_posix(), 'status_group': 'Current',
                     'id': atom_id, 'ref': atom_id, 'version': version,
                     'role': 'Requirement', 'form': 'Declaration',
                     'header_json': carrier.metadata, '_content_bytes': carrier.body.encode('utf-8'),
                     '_sha256': hashlib.sha256(raw).hexdigest()})
    if not rows:
        raise ValueError(f'{root}: no Active Requirement Declarations in staged sources')
    from FEATURE_FORMAL_MODEL_ENGINE.model_catalog import bindings_from_workbench_rows
    dependencies_source = _dependencies_declaration(rows)
    model_class_bindings = bindings_from_workbench_rows(rows)
    for row in rows:
        row['_model_class_bindings'] = model_class_bindings
    workbench = json.loads(schema_asset(rows, compile_schema(rows, compile_content_schema(rows))))
    payload = {'schema_version': 2, 'workbench': workbench, 'role_form': compile_role_form(rows),
               'header_constraints': compile_header_constraints(rows),
               'content_constraints': compile_content_constraints(rows)}
    if dependencies_source is not None:
        pin, = (pin for pin in workbench['sources'] if pin['path'] == dependencies_source)
        payload['atom_dependencies_check'] = {'claim_sha256': DEPENDENCIES_CLAIM_SHA256, 'source': pin}
    if placement_selection is None:
        delivery_rows = bootstrap_rows(inventory(root))
    else:
        selection_path = Path(placement_selection)
        if selection_path.is_symlink() or not selection_path.is_file():
            raise ValueError('placement selection is missing or is a symlink')
        try:
            selection = json.loads(selection_path.read_bytes())
        except (UnicodeError, json.JSONDecodeError) as error:
            raise ValueError(f'invalid placement selection: {error}') from error
        delivery_rows = read_selected(root, selection)
    roles = load_role_form(payload['role_form'], {row['id'] for row in rows}).roles
    from ATOM_LIFECYCLE.status_model import _STATUS_TARGET, _formal_claim_blocks, _statements, compile_status_model
    status_paths = [root / row['source_path'] for row in rows
                    if any(_STATUS_TARGET.match(statement)
                           for block in _formal_claim_blocks(row['_content_bytes'].decode('utf-8'), model_class_bindings=model_class_bindings)
                           for statement in _statements(block))]
    required_statuses = None
    if status_paths:
        declarations = json.loads(compile_status_model(status_paths, model_class_bindings=model_class_bindings))['declarations']
        required_statuses = {
            named_value_token(canonical_role_name(role)): {
                row['value'] for row in declarations
                if row['role'] is None or canonical_role_name(row['role']) == canonical_role_name(role)
            } for role in roles
        }
    placement = compile_placement(delivery_rows, rows, roles, required_statuses)
    if placement is not None:
        payload['placement'] = placement
    elif placement_selection is not None and required_statuses is not None:
        raise ValueError('Placement selection has no authoritative placement rules')
    payload['digest'] = hashlib.sha256(_canonical(payload)).hexdigest()
    return _canonical(payload) + b'\n'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-root', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--placement-selection', type=Path)
    args = parser.parse_args()
    try:
        payload = compile_candidate_schema(args.model_root, args.placement_selection)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(payload)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Candidate schema build failed: {error}\n')


if __name__ == '__main__':
    main()
