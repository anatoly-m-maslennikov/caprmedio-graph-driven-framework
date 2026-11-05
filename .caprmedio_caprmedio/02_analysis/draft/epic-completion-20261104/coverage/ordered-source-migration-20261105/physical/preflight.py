#!/usr/bin/env python3
"""Read-only collision audit of an externally derived, post-property-check move plan."""
import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[7]
CONTROL = ROOT / '.caprmedio_caprmedio'
PROTECTED = {'archive', 'archived', 'journal', 'journals', 'snapshot', 'snapshots', 'projections', 'withdrawn'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_path(value):
    p = PurePosixPath(value)
    if not value or p.is_absolute() or '..' in p.parts or '.' in p.parts or not p.parts or p.parts[0] != '.caprmedio_caprmedio':
        raise ValueError('path must be repository-relative and under .caprmedio_caprmedio')
    if any(x.lower() in PROTECTED for x in p.parts):
        raise ValueError('protected history or projection path')
    result = ROOT.joinpath(*p.parts)
    if not result.resolve().is_relative_to(CONTROL.resolve()):
        raise ValueError('path escapes repository through a symlink')
    if result.resolve() != result:
        raise ValueError('symlink paths require independent review')
    return result


def identity(path):
    try:
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            return None
        header = text[4:text.find('\n---\n', 4)]
        aid = re.search(r'(?m)^atom_id:\s*["\']?([^\s"\']+)', header)
        version = re.search(r'(?m)^version:\s*["\']?(\d+)', header)
        return [aid.group(1), int(version.group(1))] if aid and version else None
    except (OSError, UnicodeError):
        return None


def audit(row):
    result = {'source': row.get('source'), 'destination': row.get('destination'), 'owner': row.get('owner'), 'status': 'HOLD'}
    try:
        source = safe_path(row['source']); target = safe_path(row['destination'])
        if source.suffix != '.md' or target.suffix != '.md':
            raise ValueError('Atom carriers must be Markdown files')
        if not source.is_file():
            raise ValueError('source missing or not a file')
        expected = [row['atom_id'], int(row['version'])]
        result['actual_source_sha256'] = digest(source)
        result['source_identity'] = identity(source)
        if result['actual_source_sha256'] != row['source_sha256'] or result['source_identity'] != expected:
            raise ValueError('source hash or identity mismatch')
        if not row.get('destination_authority'):
            raise ValueError('destination lacks cited declaration-derived authority')
        if not row.get('owner'):
            raise ValueError('source owner must be explicitly supplied')
        if not isinstance(row.get('other_owner'), bool):
            raise ValueError('other_owner must be explicitly true or false')
        if row['other_owner']:
            result.update(classification='other_owner_review_required'); return result
        if source == target:
            result.update(status='NO_MOVE', classification='same_path'); return result
        if target.exists():
            if not target.is_file():
                result.update(classification='destination_not_file'); return result
            result['destination_sha256'] = digest(target)
            result['destination_identity'] = identity(target)
            result['classification'] = ('same_id_version_duplicate' if result['destination_identity'] == expected else 'different_or_unknown_identity_collision')
            result['bytes_identical'] = result['destination_sha256'] == result['actual_source_sha256']
            return result
        result.update(status='READY_FOR_RECHECK', classification='vacant_destination')
    except (KeyError, ValueError, OSError, TypeError) as exc:
        result['reason'] = str(exc)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path, help='reviewed destination-authority move plan JSON')
    args = parser.parse_args()
    data = json.loads(args.plan.read_text(encoding='utf-8'))
    if data.get('source_migration_applied') is not True or data.get('property_checks_passed') is not True or data.get('destination_authority_reviewed') is not True:
        raise SystemExit('HOLD: source migration, property check and destination authority must each be explicitly complete')
    moves = data.get('moves')
    if not isinstance(moves, list) or not moves:
        raise SystemExit('HOLD: no derived moves supplied')
    rows = [audit(x) for x in moves]
    targets = {}
    for index, row in enumerate(rows):
        targets.setdefault(row['destination'], []).append(index)
    for indexes in targets.values():
        if len(indexes) > 1:
            for i in indexes:
                rows[i]['status'] = 'HOLD'; rows[i]['classification'] = 'duplicate_planned_destination'
    report = {'status': 'HOLD' if any(r['status'] == 'HOLD' for r in rows) else 'PREFLIGHT_ONLY', 'plan_sha256': digest(args.plan), 'moves': rows, 'limits': 'No file moves or writes. Recheck source hashes and destination absence immediately before any separately authorized atomic move. Foreign-owner rows require owner routing.'}
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
