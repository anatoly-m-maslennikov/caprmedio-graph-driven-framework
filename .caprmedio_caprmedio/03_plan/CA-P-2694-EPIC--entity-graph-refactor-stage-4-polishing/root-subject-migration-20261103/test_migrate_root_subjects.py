import importlib.util
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

SCRIPT = Path(__file__).with_name("migrate_root_subjects.py")
spec = importlib.util.spec_from_file_location("migration", SCRIPT)
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)


class MigrationTests(unittest.TestCase):
    def test_only_target_subject_values_change_and_is_idempotent(self):
        source = b'''---\natom_id: CA-R-1\nversion: 4\nsubjects:\n  active: "CAPRMEDIO <+ MODEL <+ Type"\n  passive:\n    - 'CAPRMEDIO <+ STRUCTURE <+ Project'\n    - |\n      prefix CAPRMEDIO <+ MODEL\n  other: CAPRMEDIO <+ MODEL\nclaim: CAPRMEDIO <+ STRUCTURE\n---\nBody CAPRMEDIO <+ MODEL\n'''
        expected = source.replace(b'active: "CAPRMEDIO <+ MODEL', b'active: "CAPRMEDIO_MODEL').replace(
            b"'CAPRMEDIO <+ STRUCTURE", b"'CAPRMEDIO_STRUCTURE"
        )
        # The multiline value does not begin with a root prefix and is untouched.
        result = migration.transform(source)
        self.assertEqual(result, expected)
        self.assertEqual(migration.transform(result), result)

    def test_prefix_boundary(self):
        source = b"---\nsubjects:\n  active: CAPRMEDIO <+ MODELISH\n---\n"
        self.assertEqual(migration.transform(source), source)

    def test_invalid_yaml_and_unsupported_subject_shape_fail(self):
        for source in (
            b"---\nsubjects: [oops\n---\n",
            b"---\nsubjects:\n  active: {nested: value}\n---\n",
        ):
            with self.subTest(source=source), self.assertRaises(Exception):
                migration.transform(source)

    @staticmethod
    def records(paths):
        records = []
        for path in paths:
            before = path.read_bytes()
            after = migration.transform(before)
            records.append({"path": str(path), "before_sha256": migration.digest(before),
                            "after_sha256": migration.digest(after), "candidate": after.decode()})
        return records

    def test_drift_fails_before_writing_any_target(self):
        with tempfile.TemporaryDirectory() as temp:
            a, b = Path(temp) / "a.md", Path(temp) / "b.md"
            a.write_bytes(b"---\nsubjects:\n  active: CAPRMEDIO <+ MODEL\n---\n")
            b.write_bytes(b"---\nsubjects:\n  active: CAPRMEDIO <+ STRUCTURE\n---\n")
            records = self.records((a, b))
            b.write_bytes(b"drift")
            original_a = a.read_bytes()
            with self.assertRaises(ValueError):
                migration.apply_records(records)
            self.assertEqual(a.read_bytes(), original_a)

    def test_recheck_detects_drift_after_first_replace_and_rolls_back(self):
        with tempfile.TemporaryDirectory() as temp:
            a, b = Path(temp) / "a.md", Path(temp) / "b.md"
            a.write_bytes(b"---\nsubjects:\n  active: CAPRMEDIO <+ MODEL\n---\n")
            b.write_bytes(b"---\nsubjects:\n  active: CAPRMEDIO <+ STRUCTURE\n---\n")
            originals = [a.read_bytes(), b.read_bytes()]
            records = self.records((a, b))
            replace = migration.atomic_replace

            def mutate_between(path, data):
                replace(path, data)
                if path == a:
                    b.write_bytes(b"concurrent change")

            with patch.object(migration, "atomic_replace", side_effect=mutate_between):
                with self.assertRaisesRegex(ValueError, "before replace"):
                    migration.apply_records(records)
            self.assertEqual(a.read_bytes(), originals[0])
            self.assertEqual(b.read_bytes(), b"concurrent change")

    def test_write_failure_rolls_back_only_our_written_files(self):
        with tempfile.TemporaryDirectory() as temp:
            a, b = Path(temp) / "a.md", Path(temp) / "b.md"
            for path, value in ((a, "MODEL"), (b, "STRUCTURE")):
                path.write_text(f"---\nsubjects:\n  active: CAPRMEDIO <+ {value}\n---\n")
            originals = [a.read_bytes(), b.read_bytes()]
            records = self.records((a, b))
            replace = migration.atomic_replace
            calls = 0

            def fail_second(path, data):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("injected write failure")
                replace(path, data)

            with patch.object(migration, "atomic_replace", side_effect=fail_second):
                with self.assertRaisesRegex(OSError, "injected"):
                    migration.apply_records(records)
            self.assertEqual([a.read_bytes(), b.read_bytes()], originals)


if __name__ == "__main__":
    unittest.main()
