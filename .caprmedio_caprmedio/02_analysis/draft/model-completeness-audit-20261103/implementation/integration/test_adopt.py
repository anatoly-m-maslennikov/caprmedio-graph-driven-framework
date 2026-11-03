import contextlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import adopt


class AdoptionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve(); self.packets = self.root / 'packets'; self.packets.mkdir()
        self.out = self.root / 'integration'; self.out.mkdir()
        for target, name, value in [(adopt, 'ROOT', self.root), (adopt, 'PACKETS', self.packets),
                                    (adopt.native, 'ROOT', self.root), (adopt.native, 'HERE', self.out),
                                    (adopt.native, 'control_root', lambda root: root),
                                    (adopt.native, 'atom_identity_lock', lambda root: contextlib.nullcontext()),
                                    (adopt.native, 'atom_id_has_preserved_history_evidence', lambda root, identity: False)]:
            patcher = patch.object(target, name, value); patcher.start(); self.addCleanup(patcher.stop)
        self.rows = []
        self.source('CA-R-2279', 'Old declaring view', 'Declare IS_DECLARED_BY')
        self.source('CA-R-2', 'Stable Summary', 'Stable Summary')
        self.source('CA-R-3', 'Retire Summary', None)
        self.manifest = self.packets / 'manifest.json'; self.manifest.write_text(json.dumps(self.rows))

    def raw(self, identity, summary):
        return f'---\natom_id: {identity}\nversion: 3\nstatus: Active\nupdated_at: old\nrole: Requirement\nform: Declaration\n---\n## Summary\n\n{summary}\n\n## Claim\n\nMeaning.\n'.encode()

    def source(self, identity, old, new):
        directory = self.root / 'current'; directory.mkdir(exist_ok=True)
        path = directory / (identity + '-source.md'); path.write_bytes(self.raw(identity, old))
        row = {'id': identity, 'source': str(path.relative_to(self.root)), 'source_sha256': adopt.native.sha(path.read_bytes())}
        if new is None: row.update(action='retire', candidate=None)
        else:
            candidate = self.packets / (identity + '.txt'); candidate.write_bytes(self.raw(identity, new))
            row.update(candidate=candidate.name, candidate_sha256=adopt.native.sha(candidate.read_bytes()))
        self.rows.append(row)

    def prepare(self):
        frontier = {'operations': [{'destination_path': row['source'], 'sha256': row['source_sha256']} for row in self.rows]}
        return adopt.prepare([self.manifest], 'CA-R-999', '2026-11-03 23:00:00 +0400', frontier)

    def test_prepare_dry_check_archives_refresh_and_noop_state(self):
        plan = self.prepare()
        self.assertEqual(adopt.check(plan), 'before')
        self.assertFalse((self.root / 'current/archive').exists())
        originals = {row['source_path']: (self.root / row['source_path']).read_bytes() for row in plan['outputs']}
        (self.out / 'adoption-plan.json').write_text(json.dumps(plan))
        adopt.native.apply()
        self.assertEqual(adopt.check(plan), 'after')
        for row in plan['operations']:
            if '/archive/' in row['path']:
                self.assertIn((self.root / row['path']).read_bytes(), originals.values())
        frontier = {'operations': [{'destination_path': path} for path in originals]}
        result = adopt.refresh(frontier, plan)
        self.assertEqual(len(result['operations']), 2)
        self.assertEqual({r['base_id'] for r in result['operations']}, {'CA-R-999', 'CA-R-2'})
        self.assertEqual(adopt.check(plan), 'after')

    def test_overlap_stale_source_and_corrupt_candidate_rejected(self):
        with self.assertRaises(ValueError): adopt.normalize([self.manifest, self.manifest])
        first = self.root / self.rows[0]['source']; first.write_bytes(b'drift')
        with self.assertRaises(ValueError): self.prepare()
        first.write_bytes(self.raw('CA-R-2279', 'Old declaring view'))
        candidate = self.packets / self.rows[0]['candidate']; candidate.write_bytes(b'corrupt')
        with self.assertRaises(ValueError): self.prepare()

    def test_reference_tokens_preserve_identity_summary_frozen_and_literals(self):
        raw = b"---\natom_id: CA-R-2279\nstatus: Active\nsubjects:\n  active: 'CAPRMEDIO_MODEL <+ Relation//IS_DEFINED_BY'\n  passive: ['CA-R-2279', 'CA-R-2279@5', 'alias(Relation//A) == \"IS_DEFINED_BY\"']\n---\n## Summary\nCA-R-2279 IS_DEFINED_BY\n## Claim\nCA-R-2279 CA-R-2279@5 CA-R-22790 IS_DEFINED_BY IS_DEFINED_BY@2 \"CA-R-2279 IS_DEFINED_BY\"\n"
        result = adopt.reference_payload(raw, {'CA-R-2279': 'CA-R-999'})
        self.assertIn(b'atom_id: CA-R-2279', result)
        self.assertIn(b'## Summary\nCA-R-2279 IS_DEFINED_BY', result)
        self.assertIn(b"active: 'CAPRMEDIO_MODEL <+ Relation//IS_DECLARED_BY'", result)
        self.assertIn(b"['CA-R-999', 'CA-R-2279@5'", result)
        self.assertIn(b'CA-R-999 CA-R-2279@5 CA-R-22790 IS_DECLARED_BY IS_DEFINED_BY@2 "CA-R-2279 IS_DEFINED_BY"', result)
        self.assertIn(b'alias(Relation//A) == "IS_DEFINED_BY"', result)
        self.assertEqual(adopt.reference_payload(result, {'CA-R-2279': 'CA-R-999'}), result)

    def test_version_scan_and_fresh_id_recheck_under_lock(self):
        history = self.root / 'history'; history.mkdir()
        (history / 'CA-R-2@9.md').write_bytes(self.raw('CA-R-2', 'Stable Summary').replace(b'version: 3', b'version: 9'))
        plan = self.prepare()
        self.assertEqual(next(r['version'] for r in plan['outputs'] if r['source_id'] == 'CA-R-2'), 10)
        (self.out / 'adoption-plan.json').write_text(json.dumps(plan))
        with patch.object(adopt.native, 'atom_id_has_preserved_history_evidence', return_value=True):
            with self.assertRaises(ValueError): adopt.apply_plan(plan)
        self.assertEqual(adopt.check(plan), 'before')
        self.assertFalse((self.root / 'current/archive').exists())

    def test_apply_stale_hash_and_failure_rollback(self):
        plan = self.prepare(); (self.out / 'adoption-plan.json').write_text(json.dumps(plan))
        with patch.object(adopt.native, 'atomic_replace', side_effect=OSError('injected')):
            with self.assertRaises(OSError): adopt.native.apply()
        self.assertEqual(adopt.check(plan), 'before')
        changed = self.root / self.rows[1]['source']; changed.write_bytes(b'drift')
        with self.assertRaises(ValueError): adopt.native.apply()
        self.assertTrue((self.root / self.rows[0]['source']).exists())


if __name__ == '__main__': unittest.main()
