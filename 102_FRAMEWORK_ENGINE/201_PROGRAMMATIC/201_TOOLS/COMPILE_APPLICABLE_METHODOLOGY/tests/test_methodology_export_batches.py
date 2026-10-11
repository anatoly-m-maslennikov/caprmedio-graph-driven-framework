"""Guarded batch reads remain bounded without weakening source admission."""

from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import test_methodology_export as fixtures


exporter = fixtures.exporter


class MethodologyExportBatchTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def pin(self, name: str, data: bytes):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return exporter.SourcePin(name, hashlib.sha256(data).hexdigest())

    def test_large_pin_batch_performs_two_full_metadata_guards_not_one_per_file(self) -> None:
        expected = [(self.pin(f"support/item-{index:03}.json", f"{{\"item\":{index}}}\n".encode()),
                     f"{{\"item\":{index}}}\n".encode()) for index in range(256)]
        with patch.object(exporter, "_guard_source_metadata", wraps=exporter._guard_source_metadata) as guard:
            actual = list(exporter._pin_batch_bytes(self.root, (pin for pin, _ in expected), "support"))
        self.assertEqual(actual, expected)
        self.assertEqual(guard.call_args_list, [unittest.mock.call(self.root), unittest.mock.call(self.root)])

    def test_protected_metadata_refuses_before_any_payload_read(self) -> None:
        pin = self.pin("support.json", b"{}\n")
        # Name-only discovery avoids reading or creating protected credentials.
        entries = fixtures.FakeScandir([fixtures.FakeDirEntry(".env-protected")])
        with patch.object(exporter.os, "scandir", return_value=entries), \
             patch.object(exporter.os, "open", side_effect=AssertionError("protected tree payload opened")):
            with self.assertRaises(exporter.MethodologyExportError) as raised:
                list(exporter._pin_batch_bytes(self.root, [pin], "support"))
        self.assertEqual(raised.exception.code, "protected-source-path")

    def test_symlink_metadata_refuses_before_any_payload_read(self) -> None:
        pin = self.pin("support.json", b"{}\n")
        (self.root / "alias.json").symlink_to(self.root / "support.json")
        with patch.object(exporter.os, "open", side_effect=AssertionError("aliased tree payload opened")):
            with self.assertRaises(exporter.MethodologyExportError) as raised:
                list(exporter._pin_batch_bytes(self.root, [pin], "support"))
        self.assertEqual(raised.exception.code, "source-symlink-forbidden")

    def test_pin_byte_mutation_between_batch_members_is_stale(self) -> None:
        first, second = self.pin("a.json", b"first\n"), self.pin("b.json", b"second\n")
        batch = exporter._pin_batch_bytes(self.root, [first, second], "support")
        self.assertEqual(next(batch), (first, b"first\n"))
        (self.root / second.path).write_bytes(b"changed\n")
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            next(batch)
        self.assertEqual(raised.exception.code, "support-pin-stale")

    def test_batch_end_guard_rejects_tree_alias_added_after_last_verified_read(self) -> None:
        pin = self.pin("support.json", b"{}\n")
        batch = exporter._pin_batch_bytes(self.root, [pin], "support")
        self.assertEqual(next(batch), (pin, b"{}\n"))
        (self.root / "late-alias.json").symlink_to(self.root / pin.path)
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            next(batch)
        self.assertEqual(raised.exception.code, "source-symlink-forbidden")

    def test_pin_replaced_by_symlink_during_batch_is_not_followed(self) -> None:
        first, second = self.pin("a.json", b"first\n"), self.pin("b.json", b"second\n")
        batch = exporter._pin_batch_bytes(self.root, [first, second], "support")
        self.assertEqual(next(batch), (first, b"first\n"))
        (self.root / second.path).unlink()
        (self.root / second.path).symlink_to(self.root / first.path)
        with patch.object(exporter.os, "fdopen", side_effect=AssertionError("symlink payload opened")):
            with self.assertRaises(exporter.MethodologyExportError) as raised:
                next(batch)
        self.assertEqual(raised.exception.code, "source-symlink-forbidden")

    def test_standalone_pin_read_retains_guard_and_atom_support_classification(self) -> None:
        support = self.pin("support.md", b"# non-Atom support\n")
        with patch.object(exporter, "_guard_source_metadata", wraps=exporter._guard_source_metadata) as guard:
            data = exporter._pin_bytes(self.root, support, "support")
        self.assertEqual(data, b"# non-Atom support\n")
        self.assertGreaterEqual(guard.call_count, 1)
        exporter._support_is_atom(support, data)
        for status in ("Active", "Inactive", "Archived"):
            with self.subTest(status=status):
                pin = self.pin(f"{status}.md", fixtures.carrier("CA-R-001", status=status))
                with self.assertRaises(exporter.MethodologyExportError) as raised:
                    exporter._support_is_atom(pin, exporter._pin_bytes(self.root, pin, "support"))
                self.assertEqual(raised.exception.code, "support-atom-forbidden")

    def engine_fixture(self):
        fixture = fixtures.MethodologyExportTest("run")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        engine = fixture.root / "102_FRAMEWORK_ENGINE"
        member = engine / "201_PROGRAMMATIC/tool.py"
        member.parent.mkdir(parents=True)
        member.write_bytes(b"PERSISTENT_TOOL = 1\n")
        binding = exporter.reopen_project_export_binding(fixture.root, fixture.source)
        return fixture, engine, member, binding

    def test_engine_transient_cache_symlink_is_excluded_before_walk_or_payload_read(self) -> None:
        fixture, engine, _member, binding = self.engine_fixture()
        before = exporter._framework_engine_inventory_digest(binding)
        external = fixture.root / "external-cache"
        external.mkdir()
        (external / "cached.txt").write_bytes(b"not release source\n")
        cache = engine / ".caprmedio_tmp/cache"
        cache.mkdir(parents=True)
        (cache / "uv").symlink_to(external, target_is_directory=True)
        real_read, real_scandir = Path.read_bytes, exporter.os.scandir

        def guarded_read(path):
            if path.is_relative_to(engine / ".caprmedio_tmp") or path.resolve().is_relative_to(external):
                raise AssertionError("transient cache payload read")
            return real_read(path)

        def guarded_scandir(path):
            if not isinstance(path, int) and Path(path).is_relative_to(engine / ".caprmedio_tmp"):
                raise AssertionError("transient cache subtree walked")
            return real_scandir(path)

        with patch.object(Path, "read_bytes", guarded_read), patch.object(exporter.os, "scandir", guarded_scandir):
            self.assertEqual(exporter._framework_engine_inventory_digest(binding), before)

    def test_engine_persistent_symlink_is_still_rejected(self) -> None:
        _fixture, engine, member, binding = self.engine_fixture()
        (engine / "201_PROGRAMMATIC/alias.py").symlink_to(member)
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter._framework_engine_inventory_digest(binding)
        self.assertEqual(raised.exception.code, "release-inventory-symlink")

    def test_engine_persistent_byte_change_changes_inventory_digest(self) -> None:
        _fixture, _engine, member, binding = self.engine_fixture()
        before = exporter._framework_engine_inventory_digest(binding)
        member.write_bytes(b"PERSISTENT_TOOL = 2\n")
        self.assertNotEqual(exporter._framework_engine_inventory_digest(binding), before)


if __name__ == "__main__":
    unittest.main()
