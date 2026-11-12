"""A watcher must see the final inode after the staging link is removed."""
from pathlib import Path
from contextlib import contextmanager
import hashlib
from types import SimpleNamespace
import os
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import effects, source, state_actions  # noqa: E402


class PublicationTest(unittest.TestCase):
    def test_watcher_cannot_observe_staged_hard_link(self):
        base = ROOT / '.caprmedio_tmp' / 'effect-publication-test'
        base.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as directory:
            path = Path(directory) / 'CA-R-1-TEST.md'
            lock = threading.RLock()
            attempted, observed = threading.Event(), []
            original_link = os.link
            workers = []
            class Reader:
                def lifecycle_file_effect(self):
                    return lock
                def lifecycle_read(self, target, *, descriptor=None):
                    return target.read_bytes()
                def lifecycle_changed(self, old, new):
                    observed.append(('notification', new.stat().st_nlink))
            def link_then_watch(*args, **kwargs):
                original_link(*args, **kwargs)
                def watch():
                    attempted.set()
                    with lock:
                        observed.append(('watcher', path.stat().st_nlink))
                worker = threading.Thread(target=watch)
                worker.start()
                workers.append(worker)
                self.assertTrue(attempted.wait(1))
                self.assertEqual([], observed)
            with patch.object(effects, '_reader', return_value=Reader()), \
                    patch.object(effects.os, 'link', side_effect=link_then_watch):
                result = effects.create(ROOT, path, b'content')
            for worker in workers:
                worker.join(1)
                self.assertFalse(worker.is_alive())
            self.assertFalse(result.errors, result.errors)
            self.assertEqual({('watcher', 1), ('notification', 1)}, set(observed))

    def test_watcher_sees_only_final_state_of_paired_move(self):
        base = ROOT / '.caprmedio_tmp' / 'effect-publication-test'
        base.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as directory:
            old = Path(directory) / 'CA-R-1-OLD.md'
            new = Path(directory) / 'CA-R-1-NEW.md'
            old.write_bytes(b'original')
            lock, attempted, observed, workers = threading.RLock(), threading.Event(), [], []
            class Reader:
                def lifecycle_file_effect(self):
                    return lock
                def lifecycle_read(self, path, *, descriptor=None):
                    return path.read_bytes()
                def lifecycle_changed(self, before, after):
                    if before is None and after == new:
                        def watch():
                            attempted.set()
                            with lock:
                                observed.append((old.exists(), new.exists()))
                        worker = threading.Thread(target=watch)
                        worker.start()
                        workers.append(worker)
                        self_outer.assertTrue(attempted.wait(1))
                        self_outer.assertEqual([], observed)
            self_outer = self
            pin = SimpleNamespace(path=old, sha256=hashlib.sha256(b'original').hexdigest(),
                                  atom_id='CA-R-1', version=1)
            with source.bind_query_reader(Reader()):
                result = state_actions._publish(SimpleNamespace(root=ROOT), pin, new, b'updated', 'Active', 'CA-R-1')
            for worker in workers:
                worker.join(1)
                self.assertFalse(worker.is_alive())
            self.assertFalse(result['errors'], result)
            self.assertEqual([(False, True)], observed)

    def test_failed_publication_reports_effects(self):
        base = ROOT / '.caprmedio_tmp' / 'effect-publication-test'
        base.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as directory:
            old = Path(directory) / 'CA-R-1-OLD.md'
            new = Path(directory) / 'CA-R-1-NEW.md'
            old.write_bytes(b'original')
            class Reader:
                @contextmanager
                def lifecycle_publication(self):
                    publication = {}
                    yield publication
                    publication['error'] = 'Publication failed.'
                def lifecycle_read(self, path, *, descriptor=None):
                    return path.read_bytes()
                def lifecycle_changed(self, before, after):
                    pass
            pin = SimpleNamespace(path=old, sha256=hashlib.sha256(b'original').hexdigest(),
                                  atom_id='CA-R-1', version=1)
            with source.bind_query_reader(Reader()):
                result = state_actions._publish(SimpleNamespace(root=ROOT), pin, new, b'updated', 'Active', 'CA-R-1')
            self.assertEqual('projection_refresh_failed', result['errors'][0]['code'])
            self.assertEqual(['create', 'remove'], [entry['operation'] for entry in result['effects']])
            self.assertTrue(new.exists())
            self.assertFalse(old.exists())


if __name__ == '__main__':
    unittest.main()
