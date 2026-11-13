# CA-D-719@1

"""Verify the packaged Change Current Status entry point against admitted Atoms."""

from __future__ import annotations

import argparse
import ast
import base64
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Callable

if not __package__:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402


_CODE_ROOT = Path(__file__).resolve().parents[4]
_ASSET_DIRECTORY = Path(__file__).resolve().with_name('assets')
ASSET = _ASSET_DIRECTORY / 'change_current_status.py'
SNAPSHOT = _ASSET_DIRECTORY / 'change_current_status_sources.json'
CHECKOUT_MODEL = Path('.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/'
                      'CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES')
OPERATIONS = Path('CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations')
WORKFLOW = 'CA-O-10011-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status'
STEP = 'CA-O-10010-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status'
ACTION = 'CA-O-10007-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status'
SOURCES = (
    ('workflow', 'CA-O-10011', 4, OPERATIONS / (WORKFLOW + '.md')),
    ('step', 'CA-O-10010', 1, OPERATIONS / WORKFLOW / (STEP + '.md')),
    ('action', 'CA-O-10007', 1, OPERATIONS / (ACTION + '.md')),
)
HISTORY_FOLDERS = {'archive', 'archived', 'draft', '099_archived', '000_draft'}
_READ_LIMITS = {**CEILINGS, 'max_file_bytes': 128 * 1024, 'max_total_read_bytes': 512 * 1024}


class DefinitionChanged(RuntimeError):
    """The reviewed Workflow or one of its admitted bindings is unavailable."""


def _reader(root: Path) -> ReadContext:
    return ReadContext(roots=[str(root)], limits=dict(_READ_LIMITS))


def _read_source(root, form, atom_id, version, relative):
    path = root / relative
    candidates = [item for item in root.rglob(f'{atom_id}-*.md')
                  if not HISTORY_FOLDERS.intersection(item.relative_to(root).parts)]
    if candidates != [path] or path.resolve() != path or not path.is_file():
        raise ValueError(f'{atom_id}@{version} requires one canonical source at {relative}')
    raw = _reader(root).read(path, remember=False)
    parsed = parse_carrier(raw, path)
    try:
        identity = parsed.metadata['identity']
        state = parsed.metadata['state']
        context = parsed.metadata['context']
        owner = {'atom': 'CA-O-10011'} if form == 'step' else {'scope_unit': 'CA-SU-13'}
        admitted = (
            identity['atom_id'] == identity['ref_id'] == atom_id
            and state['status'].casefold() == 'active'
            and type(state['version']) is int and state['version'] == version
            and context['role'] == 'Operations' and context['form'] == form.title()
            and context['container'] == owner
        )
        if form == 'step':
            admitted = admitted and parsed.metadata['relations']['RUNS'] == ['CA-O-10007']
    except (AttributeError, KeyError, TypeError) as error:
        raise ValueError(f'Malformed {atom_id}@{version} binding') from error
    if not admitted:
        raise ValueError(f'{atom_id}@{version} does not match the admitted {form} binding')
    return raw


def _claim_code(raw, binding):
    _, delimiter, body = raw.partition(b'\n---\n')
    if not delimiter:
        raise ValueError('Expected an LF-delimited Workflow carrier')
    sections = re.split(rb'^### Formal Claim[ \t]*\n', body, flags=re.M)
    if len(sections) != 2:
        raise ValueError('Expected one Workflow Formal Claim')
    section = re.split(rb'^#{1,3} ', sections[1], maxsplit=1, flags=re.M)[0]
    match = re.fullmatch(rb'\n*```python\n(.*?)\n```[ \t]*\n*', section, flags=re.S)
    if match is None:
        raise ValueError('Expected one Python fence in the Workflow Formal Claim')
    code = match[1] + b'\n'
    try:
        module = ast.parse(code)
    except SyntaxError as error:
        raise ValueError('Invalid Python in the Workflow Formal Claim') from error
    if len(module.body) != 1 or not isinstance(module.body[0], ast.FunctionDef):
        raise ValueError('Expected one Python Workflow entry point')
    entry = module.body[0]
    args = entry.args
    if (entry.name != 'change_current_status' or entry.decorator_list or args.posonlyargs
            or args.args or args.vararg or args.kwarg or args.kw_defaults != [None, None]
            or [arg.arg for arg in args.kwonlyargs] != ['invocation', 'engine']):
        raise ValueError('Expected change_current_status(*, invocation, engine)')
    calls = [node for node in ast.walk(entry) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == 'invoke']
    if len(calls) != 1:
        raise ValueError('Expected one declared Action dispatch in the Workflow')
    selected = {keyword.arg: keyword.value.value for keyword in calls[0].keywords
                if isinstance(keyword.value, ast.Constant)}
    if selected.get('step') != binding['step'] or selected.get('action') != binding['action']:
        raise ValueError('Workflow dispatch must name the pinned Step and Action')
    return code


def _snapshot_bytes(encoded: dict[str, str]) -> bytes:
    return json.dumps(encoded, sort_keys=True, separators=(',', ':')).encode() + b'\n'


def _generated_assets(model_root: Path) -> tuple[bytes, bytes]:
    root = model_root.resolve(strict=True)
    binding = {form: f'{atom_id}@{version}' for form, atom_id, version, _ in SOURCES}
    sources = {form: _read_source(root, form, atom_id, version, relative)
               for form, atom_id, version, relative in SOURCES}
    hashes = {binding[form]: hashlib.sha256(raw).hexdigest() for form, raw in sources.items()}
    header = '# Generated from the admitted Workflow Formal Claim.\n\n'
    header += f'WORKFLOW_BINDING = {binding!r}\nSOURCE_SHA256 = {{\n'
    header += ''.join(f'    {ref!r}: {sha!r},\n' for ref, sha in hashes.items())
    python = (header + '}\n\n\n').encode() + _claim_code(sources['workflow'], binding)
    encoded = {binding[form]: base64.b64encode(raw).decode('ascii') for form, raw in sources.items()}
    return python, _snapshot_bytes(encoded)


def verify_installed(model_root: Path) -> None:
    """Fail a build if admitted source bytes or the generated entry point drift."""
    reader = _reader(_CODE_ROOT)
    expected_python, expected_snapshot = _generated_assets(model_root)
    if reader.read(ASSET, remember=False) != expected_python:
        raise ValueError('Generated Change Current Status Workflow differs from admitted sources')
    if reader.read(SNAPSHOT, remember=False) != expected_snapshot:
        raise ValueError('Packaged Change Current Status snapshot differs from admitted sources')


def _installed_model(code_root: Path) -> Path | None:
    checkout = code_root / '.git'
    if checkout.exists() or checkout.is_symlink():
        return code_root / CHECKOUT_MODEL
    methodology = code_root / 'METHODOLOGY'
    delivery = code_root / 'LAYER_5_FRAMEWORK_DELIVERY'
    if any(marker.exists() or marker.is_symlink() for marker in (methodology, delivery)):
        return methodology / 'sources'
    return None


def _verify_digest(raw: bytes, revision: str, expected: str) -> None:
    if hashlib.sha256(raw).hexdigest() != expected:
        raise DefinitionChanged(f'Admitted Workflow definition {revision} changed')


def _verify_sources(code_root: Path, paths: tuple[tuple[Path, str, str], ...]) -> None:
    reader = _reader(code_root)
    for path, revision, digest in paths:
        try:
            raw = reader.read(path, remember=False)
        except (OSError, RuntimeError, ValueError) as error:
            raise DefinitionChanged(f'Admitted Workflow definition {revision} is unavailable') from error
        _verify_digest(raw, revision, digest)


def _verify_snapshot(code_root: Path, path: Path, pins: tuple[tuple[str, str], ...]) -> None:
    try:
        payload = _reader(code_root).read(path, remember=False)
        encoded = json.loads(payload)
        if (not isinstance(encoded, dict) or encoded.keys() != {revision for revision, _ in pins}
                or _snapshot_bytes(encoded) != payload):
            raise ValueError('Invalid source snapshot')
        sources = {revision: base64.b64decode(value, validate=True) for revision, value in encoded.items()}
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise DefinitionChanged('Packaged Change Current Status definition snapshot is unavailable') from error
    for revision, digest in pins:
        _verify_digest(sources[revision], revision, digest)


def _bind_definition_check(code_root: Path) -> Callable[[], None]:
    from .assets.change_current_status import SOURCE_SHA256, WORKFLOW_BINDING

    pinned = tuple((WORKFLOW_BINDING[form], relative) for form, _, _, relative in SOURCES)
    model = _installed_model(code_root)
    if model is not None:
        paths = tuple((model / relative, revision, SOURCE_SHA256[revision]) for revision, relative in pinned)
        return lambda: _verify_sources(code_root, paths)
    snapshot = code_root / SNAPSHOT.relative_to(_CODE_ROOT)
    pins = tuple((revision, SOURCE_SHA256[revision]) for revision, _ in pinned)
    return lambda: _verify_snapshot(code_root, snapshot, pins)


def bind_definition_check() -> Callable[[], None]:
    """Bind reviewed sources from the code installation before dispatch."""
    return _bind_definition_check(_CODE_ROOT)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-root', required=True, type=Path)
    parser.add_argument('--write-asset', action='store_true', help='Generate for source review')
    args = parser.parse_args()
    if args.write_asset:
        payload, snapshot = _generated_assets(args.model_root)
        ASSET.parent.mkdir(exist_ok=True)
        ASSET.write_bytes(payload)
        SNAPSHOT.write_bytes(snapshot)
    else:
        verify_installed(args.model_root)


if __name__ == '__main__':
    main()
