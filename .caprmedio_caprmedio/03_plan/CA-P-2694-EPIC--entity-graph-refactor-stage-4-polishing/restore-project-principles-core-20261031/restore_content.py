"""One-time, content-only restoration from the recorded Oct 27 snapshot."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import os
import re
import sys
import tempfile
import uuid
import yaml

ROOT = Path.cwd()
PACKET = Path(__file__).resolve().parent
PATTERN = re.compile(rb'\A---\r?\n(.*?)^---[^\S\r\n]*\r?\n(.*)\Z', re.M | re.S)

def split(raw):
    match = PATTERN.match(raw)
    assert match, 'missing frontmatter'
    return match.group(1), match.group(2)

def field(header, name, value):
    result, count = re.subn(rb'^' + name.encode() + rb':[^\r\n]*', (name + ': ' + str(value)).encode(), header, flags=re.M)
    assert count == 1, name
    return result

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def atomic_write(path, raw):
    fd, temporary = tempfile.mkstemp(prefix='.restore-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, path.stat().st_mode & 0o777)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def plan():
    changes = []
    for entry in json.loads((PACKET / 'inventory.json').read_text()):
        if entry['state'] != 'ready':
            continue
        path = ROOT / entry['current_path']
        before = path.read_bytes()
        assert sha(before) == entry['current_sha256'], str(path) + ' changed since preparation'
        historical = (PACKET / 'historical' / (entry['historical_id'] + '.md')).read_bytes()
        assert sha(historical) == entry['historical_sha256']
        header, old_body = split(before)
        _, body = split(historical)
        metadata = yaml.safe_load(header)
        assert metadata['atom_id'] == entry['current_id'] and metadata['status'] == 'Active'
        archive = path.parent / 'archive' / path.name.replace(entry['current_id'] + '-', entry['current_id'] + '@' + str(metadata['version']) + '-', 1)
        assert archive != path
        assert not archive.exists(), 'archive collision: ' + str(archive)
        changes.append((entry, path, before, header, body, archive, metadata))
    assert len(changes) == 47 and len({x[1] for x in changes}) == 47
    return changes

def main():
    changes = plan()
    if '--apply' not in sys.argv:
        print('PREVIEW: 47 Active project Atoms; content-only; no source writes')
        return
    assert not any((PACKET / name).exists() for name in ('applied.json','progress.json')), 'prior attempt recorded; inspect receipts before retry'
    from work_journal import append_sealed_events
    now = datetime.now(ZoneInfo('Asia/Tbilisi'))
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S %z')
    receipts = []
    for entry, path, before, header, body, archive, metadata in changes:
        assert path.read_bytes() == before, 'concurrent edit: ' + str(path)
        next_version = metadata['version'] + 1
        new_header = field(field(header, 'version', next_version), 'updated_at', timestamp)
        after = b'---\n' + new_header + b'---\n' + body
        new_meta = yaml.safe_load(new_header)
        assert {k:v for k,v in metadata.items() if k not in ('version','updated_at')} == {k:v for k,v in new_meta.items() if k not in ('version','updated_at')}
        archive_header = field(field(header, 'atom_id', metadata['atom_id'] + '@' + str(metadata['version'])), 'status', 'Archived')
        archive_raw = b'---\n' + archive_header + b'---\n' + split(before)[1]
        archive.parent.mkdir(exist_ok=True)
        with archive.open('xb') as stream:
            stream.write(archive_raw)
            stream.flush()
            os.fsync(stream.fileno())
        assert path.read_bytes() == before, 'concurrent edit after archive: ' + str(path)
        atomic_write(path, after)
        assert path.read_bytes() == after
        receipt = dict(atom_id=metadata['atom_id'], historical_id=entry['historical_id'], historical_version=entry['historical_version'], source_commit=entry['baseline_commit'], current_path=entry['current_path'], archive_path=str(archive.relative_to(ROOT)), previous_version=metadata['version'], version=next_version, before_sha256=sha(before), after_sha256=sha(after), historical_body_sha256=sha(body))
        event = dict(event_id=str(uuid.uuid4()), event='atom_content_restored', occurred_at=now.isoformat(), actor='Codex', operator='Anatoly Maslennikov', session='codex:01a0263a-7510-7672-bce4-58830bc4d184', **receipt)
        receipt['state'] = 'restored-awaiting-journal'
        receipts.append(receipt)
        (PACKET / 'progress.json').write_text(json.dumps(receipts, indent=2) + '\n')
        receipt['journal'] = append_sealed_events(ROOT, [event], author='codex-methodology', local_date=now.date().isoformat(), timezone='Asia/Tbilisi')
        receipt['state'] = 'complete'
        (PACKET / 'progress.json').write_text(json.dumps(receipts, indent=2) + '\n')
    (PACKET / 'applied.json').write_text(json.dumps(receipts, indent=2) + '\n')
    print('APPLIED: 47 content restorations, 47 predecessor archives, 47 Journal events')

if __name__ == '__main__':
    main()
