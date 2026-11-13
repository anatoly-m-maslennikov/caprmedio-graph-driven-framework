# CA-E-677@30
"""A native destination-create event can arrive before its source-remove event."""

from pathlib import Path
import sys
import tempfile
import unittest

APP_ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(APP_ROOT.parent), str(APP_ROOT.parents[1] / "FEATURE_TOOLS")]

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import source_path, write_atom, write_settings  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import materialize  # noqa: E402


class SourceMoveEventTests(unittest.TestCase):
    def test_batched_current_move_and_draft_removal_leave_no_stale_source_row(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            root.mkdir()
            control = write_settings(root)
            declarations = write_scope_unit_declarations(root, (
                {"scope_unit_name": "MAIN"}, {"scope_unit_name": "TARGET"},
            ), control_root=control)
            current = source_path(declarations, "MAIN", "04_requirement", "current.md")
            draft = source_path(declarations, "MAIN", "04_requirement/draft", "draft.md")
            write_atom(current, "CA-R-424241")
            write_atom(draft, "CA-R-424242", status="Draft", version=2)
            reader = SourceReader(root)
            reader.capture()

            moved = source_path(declarations, "TARGET", "04_requirement", "moved.md")
            moved.parent.mkdir(parents=True, exist_ok=True)
            current.rename(moved)
            draft.unlink()
            rows, _ = reader.capture([
                {
                    "operation": "move", "old_path": current.relative_to(root).as_posix(),
                    "new_path": moved.relative_to(root).as_posix(),
                },
                {"operation": "remove", "old_path": draft.relative_to(root).as_posix(), "new_path": None},
            ])

            self.assertEqual([moved.relative_to(root).as_posix()], [
                row["source_path"] for row in rows if row["ref"] == "CA-R-424241"
            ])
            self.assertFalse(any(row["ref"] == "CA-R-424242@2-draft" for row in rows))
            self.assertIsNone(reader.capture_delta[draft.relative_to(root).as_posix()])

    def test_destination_event_prunes_missing_alias_but_not_real_duplicate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            root.mkdir()
            control = write_settings(root)
            declarations = write_scope_unit_declarations(root, (
                {"scope_unit_name": "MAIN"}, {"scope_unit_name": "TARGET"},
            ), control_root=control)
            source = source_path(declarations, "MAIN", "04_requirement", "original.md")
            write_atom(source, "CA-R-424242")
            reader = SourceReader(root)
            reader.capture()
            target = source_path(declarations, "TARGET", "04_requirement", "moved.md")
            target.parent.mkdir(parents=True, exist_ok=True)
            source.rename(target)
            rows, scopes = reader.capture([{
                "operation": "create", "old_path": None,
                "new_path": target.relative_to(root).as_posix(),
            }])
            matches = [row for row in rows if row["ref"] == "CA-R-424242"]
            self.assertEqual([target.relative_to(root).as_posix()], [row["source_path"] for row in matches])
            self.assertNotIn(source, reader._cached)
            self.assertNotIn(source, reader._source_paths)
            self.assertIsNone(reader.capture_delta[source.relative_to(root).as_posix()])
            self.assertIsNotNone(reader.capture_delta[target.relative_to(root).as_posix()])

            # Both existing carriers remain queryable.
            write_atom(source, "CA-R-424242")
            rows, _ = reader.capture([{
                "operation": "create", "old_path": None,
                "new_path": source.relative_to(root).as_posix(),
            }])
            rows, _ = materialize(rows, scopes)
            self.assertEqual(2, len([row for row in rows if row["ref"] == "CA-R-424242"]))
            self.assertEqual(2, len(reader._references.paths["CA-R-424242"]))


if __name__ == "__main__":
    unittest.main()
