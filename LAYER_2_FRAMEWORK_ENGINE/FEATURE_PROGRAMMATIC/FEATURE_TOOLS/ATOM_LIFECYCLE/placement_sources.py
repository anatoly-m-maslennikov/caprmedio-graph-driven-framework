"""Select and pin staged Delivery declarations for the image build."""
from __future__ import annotations

import contextlib
import hashlib
import json
from pathlib import Path
import re
import sys

# In the selector container this file is mounted at /selector.py.  The parser
# and query backend must come from the previous image, never the staged source.
_PACKAGED = Path('/workspace/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC')
_TOOLS = (_PACKAGED / 'FEATURE_TOOLS' if _PACKAGED.is_dir()
          else Path(__file__).resolve().parents[1])
_APPS = _TOOLS.parent / 'FEATURE_APPS'
for _directory in (_TOOLS, _APPS, _APPS / 'APP_WORKBENCH'):
    sys.path.insert(0, str(_directory))

from carrier_aliases import carrier_read_view, carrier_status_folder, matches_named_value  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402

PLACEMENT_SUBJECT = re.compile(
    r'^CAPRMEDIO_MODEL\s*<\+\s*(?:Carrier|Atom\.Header\.Context\.Role|'
    r'Atom(?:/\([^)]*\))*\.Header\.State\.Status(?:\s*:\s*[^/]+)?|'
    r'Atom/\(\.Header\.Context\.Role\s*:=\s*Plan\)\.Header\.State\.Status'
    r'\s*>\|\s*Status Group\s*:=\s*Backlog|'
    r'Atom\.Header\.State\.Status\s*>\|\s*Status Group\s*:=\s*(?:Draft|Archived|Current))$'
)


def carrier_paths(root: Path) -> list[Path]:
    """List eligible staged Delivery paths without reading their contents."""
    root = Path(root)
    if not root.is_dir():
        raise ValueError(f'{root}: staged model root is not a directory')
    paths = sorted(root.rglob('CA-D-*.md'))

    def core(path):
        return any(part.upper() == 'CORE_META_MODEL' or part.upper().endswith('_CORE_META_MODEL')
                   for part in path.relative_to(root).parts[:-1])

    layered = any(any('LAYER_' in part.upper() for part in path.relative_to(root).parts[:-1])
                  for path in paths)
    if layered or any(core(path) for path in paths):
        paths = [path for path in paths if core(path)]
    return [path for path in paths if not any(
        carrier_status_folder(part) in {'archived', 'draft'} for part in path.relative_to(root).parts
    )]


def read_record(root: Path, path: Path) -> dict:
    """Read one pinned staged carrier and compute its identity and digest."""
    relative = path.relative_to(root)
    raw = path.read_bytes()
    carrier = parse_carrier(raw, path)
    view = carrier_read_view(carrier.metadata)
    topics = view.get('topics')
    return {
        'source_path': relative.as_posix(), 'id': view.get('atom_id'),
        'version': view.get('version'), 'ref_id': view.get('ref_id', view.get('atom_id')),
        'status': view.get('status'), 'role': view.get('role'),
        'subject': topics.get('main_subject') if isinstance(topics, dict) else None,
        '_content_bytes': carrier.body.encode('utf-8'), '_sha256': hashlib.sha256(raw).hexdigest(),
    }


def inventory(root: Path) -> list[dict]:
    """Read the eligible native carrier inventory once, in deterministic order."""
    root = Path(root)
    return [read_record(root, path) for path in carrier_paths(root)]


def eligible(row: dict) -> bool:
    subject = row['subject']
    return (row['status'] in ('Active', 'active') and matches_named_value(row['role'], 'Delivery')
            and isinstance(subject, str) and bool(PLACEMENT_SUBJECT.fullmatch(subject.strip())))


def pin(row: dict) -> dict:
    return {'source_path': row['source_path'], 'id': row['id'],
            'version': row['version'], 'sha256': row['_sha256']}


def validate_selection(records: list[dict], selected: object, *, require_complete: bool = True) -> list[dict]:
    """Reject stale, incomplete, duplicate or noneligible selection pins."""
    if not isinstance(selected, list):
        raise ValueError('placement selection must be a list')
    by_path = {row['source_path']: row for row in records}
    seen, ids, selected_rows = set(), set(), []
    for item in selected:
        if not isinstance(item, dict) or set(item) != {'source_path', 'id', 'version', 'sha256'}:
            raise ValueError('invalid placement source pin')
        path = item['source_path']
        if not isinstance(path, str) or path in seen or path not in by_path:
            raise ValueError(f'invalid or duplicate placement path: {path}')
        row = by_path[path]
        atom_id = row['id']
        filename = Path(path).name
        if (not eligible(row) or not isinstance(atom_id, str)
                or not (filename == atom_id + '.md' or filename.startswith(atom_id + '-'))
                or row['ref_id'] != atom_id or type(row['version']) is not int or row['version'] < 1
                or atom_id in ids or type(item['version']) is not int or item != pin(row)):
            raise ValueError(f'{path}: invalid, duplicate or stale Delivery source pin')
        seen.add(path)
        ids.add(atom_id)
        selected_rows.append(row)
    if require_complete and seen != {row['source_path'] for row in records if eligible(row)}:
        raise ValueError('placement selection does not cover all eligible sources')
    return sorted(selected_rows, key=lambda row: row['source_path'])


def read_selected(root: Path, selected: object) -> list[dict]:
    """Verify pins against current files, without reading unselected carriers."""
    root = Path(root)
    if not isinstance(selected, list):
        raise ValueError('placement selection must be a list')
    allowed = {path.relative_to(root).as_posix(): path for path in carrier_paths(root)}
    seen, records = set(), []
    for item in selected:
        if not isinstance(item, dict) or set(item) != {'source_path', 'id', 'version', 'sha256'}:
            raise ValueError('invalid placement source pin')
        path = item['source_path']
        if not isinstance(path, str) or path in seen or path not in allowed:
            raise ValueError(f'invalid or duplicate placement path: {path}')
        seen.add(path)
        records.append(read_record(root, allowed[path]))
    return validate_selection(records, selected, require_complete=False)


def bootstrap_rows(records: list[dict]) -> list[dict]:
    return validate_selection(records, [pin(row) for row in records if eligible(row)])


def query_pins(root: Path, store_factory=None) -> list[dict]:
    """Query the staged inventory through the previous image's Workbench backend."""
    from FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
    from FEATURE_WORKBENCH_BACKEND.header_columns import HeaderColumn, HeaderSchema
    from FEATURE_WORKBENCH_BACKEND.query_store import QueryStore
    from FEATURE_WORKBENCH_BACKEND.source_rows import atom

    records = inventory(root)
    rows = []
    for record in records:
        projection = {key: record[key] if isinstance(record[key], str) else None
                      for key in ('role', 'status', 'subject')}
        row = atom(Path(root) / record['source_path'], Path(root), projection,
                   {'atom_id': record['id'], 'version': record['version']}, b'', 'Current')
        # A duplicate or invalid ID must still be visible to the selection query.
        row['ref'] = record['source_path']
        rows.append(row)
    header = HeaderSchema(tuple(HeaderColumn((key,), 'header.' + key, 'VARCHAR', True)
                                for key in ('role', 'status', 'subject')))
    store = (store_factory or QueryStore)()
    try:
        store.replace(rows, [], relation_types=set(), header_schema=header,
                      content_schema=compile_content_schema([]))
        # Regex is the same expression used by the first-build bootstrap and compiler.
        pattern = PLACEMENT_SUBJECT.pattern.replace("'", "''")
        sql = ("SELECT relative_path, filename FROM atoms WHERE "
               "\"header.status\" IN ('Active', 'active') AND "
               "\"header.role\" IN ('Delivery', 'delivery') AND "
               f"regexp_full_match(trim(\"header.subject\"), '{pattern}') "
               'ORDER BY relative_path, filename')
        result = store.run(sql, page_size=1000)
        paths = []
        while True:
            paths.extend((Path(row[0]) / row[1]).as_posix() for row in result['rows'])
            if not result['has_more']:
                break
            result = store.page(result['query_id'], len(paths), page_size=1000)
        by_path = {row['source_path']: row for row in records}
        selected = [pin(by_path[path]) for path in paths]
        return [pin(row) for row in validate_selection(records, selected)]
    finally:
        store.close()


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit('usage: selector.py MODEL_ROOT')
    try:
        with contextlib.redirect_stdout(sys.stderr):
            selected = query_pins(Path(sys.argv[1]))
        print(json.dumps(selected, ensure_ascii=False, sort_keys=True, separators=(',', ':')))
    except (OSError, ValueError) as error:
        raise SystemExit(f'placement selection failed: {error}') from error


if __name__ == '__main__':
    main()
