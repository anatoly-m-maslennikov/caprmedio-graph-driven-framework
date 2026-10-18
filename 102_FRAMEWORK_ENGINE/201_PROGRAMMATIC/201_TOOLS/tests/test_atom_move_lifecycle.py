"""Focused same-ID Core <-> Project Atom move lifecycle cases."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import atom_operations  # noqa: E402
import lifecycle_intents  # noqa: E402
import test_selected_atom_lifecycle as selected_lifecycle  # noqa: E402
from lifecycle_intents import (  # noqa: E402
    LifecycleError,
    carrier_descriptor,
    move_atom_action,
)


CORE_REQUIREMENTS = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement"
)
PROJECT_REQUIREMENTS = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/04_requirement"
)
CORE_PLANS = CORE_REQUIREMENTS.parent / "03_plan"
PROJECT_PLANS = PROJECT_REQUIREMENTS.parent / "03_plan"
CORE_OPERATIONS = CORE_REQUIREMENTS.parent / "09_operations"
PROJECT_OPERATIONS = PROJECT_REQUIREMENTS.parent / "09_operations"


class AtomMoveLifecycleTest(unittest.TestCase):
    """Exercise one sealed current carrier at a time; no project-wide scan."""

    move_id = "CA-R-100"

    def setUp(self) -> None:
        self.fixture = selected_lifecycle.SelectedAtomLifecycleTest("runTest")
        self.fixture.setUp()
        self.root = self.fixture.root
        self._add_project_configuration_scope()
        self.fixture._copy_frozen_atom("CA-R-1539")
        self.core_path = self._move_fixture_atom(
            self.fixture.target, CORE_REQUIREMENTS / "CA-R-100-CORE_META_MODEL--core-move.md",
            "CORE_META_MODEL",
        )

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def _add_project_configuration_scope(self) -> None:
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        structure.write_text(
            structure.read_text(encoding="utf-8")
            + "\n[[scope_units]]\n"
            + 'scope_unit_name = "PROJECT_CONFIGURATION"\n'
            + 'parent = "METHODOLOGY_SOURCES"\n'
            + 'scope_unit_type = "Unordered"\n'
            + 'scope_unit_label = "METHODOLOGY"\n'
            + "structural_level = 3\n"
            + "navigational_order_number = 1\n"
            + 'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION"\n'
            + 'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/003_PROJECT_CONFIGURATION"\n',
            encoding="utf-8",
        )

    def _move_fixture_atom(self, source: Path, relative: Path, owner: str) -> Path:
        payload = source.read_text(encoding="utf-8").replace(
            "current_scope_unit: LIFECYCLE_FIXTURE", f"current_scope_unit: {owner}"
        ).replace(
            "claim_target_scope_unit: LIFECYCLE_FIXTURE", f"claim_target_scope_unit: {owner}"
        )
        source.unlink()
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(payload, encoding="utf-8")
        return destination

    def _placement(self, destination: Path, owner: str) -> dict[str, str]:
        return {
            "destination_path": destination.relative_to(self.root).as_posix(),
            "owning_scope_unit": owner,
            "claim_target_scope_unit": owner,
        }

    def _request(self, source: Path, destination: Path, owner: str) -> dict[str, object]:
        return {
            "target": carrier_descriptor(self.root, source.relative_to(self.root).as_posix()),
            "placement": self._placement(destination, owner),
        }

    def _snapshot(self, *extra: Path) -> dict[str, bytes]:
        """Snapshot only the current carrier, destination, and their history areas."""
        paths = {self.core_path, *extra}
        paths.update({path.parent / name for path in tuple(paths) for name in ("archive", "archived")})
        result: dict[str, bytes] = {}
        for path in paths:
            if path.is_file():
                result[path.relative_to(self.root).as_posix()] = path.read_bytes()
            elif path.is_dir():
                for child in path.rglob("*"):
                    if child.is_file():
                        result[child.relative_to(self.root).as_posix()] = child.read_bytes()
        return result

    def _workflow_bundle(self) -> tuple[Path, Path, dict[str, bytes]]:
        self.fixture._copy_frozen_atom("CA-R-1874")
        source = self.root / CORE_OPERATIONS / "CA-O-010-CORE_META_MODEL-WORKFLOW--bundle-move.md"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(
            "---\natom_id: CA-O-010\ncontent_role: Operations\ntype: Workflow\n"
            "current_scope_unit: CORE_META_MODEL\nclaim_target_scope_unit: CORE_META_MODEL\n"
            "local_tier: Standard\nglobal_tier: 11\nauthor: Anatoly Maslennikov\n"
            "status: Active\nversion: 1\nupdated_at: \"2026-01-01 00:00:00 +0000\"\n"
            "subjects:\n  governs: Tool\n  depends_on: [Plan]\nrelations: {}\n---\n"
            "# Summary\n\nBundle move fixture\n\n## Scope\n\nOne explicitly selected Workflow.\n\n"
            "## Operation\n\nKeep this workflow unchanged.\n\n## Details\n\nMove only this carrier.\n",
            encoding="utf-8",
        )
        bundle = source.with_suffix("")
        bundle.mkdir()
        (bundle / "CA-O-146-CORE_META_MODEL-STEP--child.md").write_bytes(
            b"---\natom_id: CA-O-146\ncurrent_scope_unit: CORE_META_MODEL\nversion: 5\n---\nchild\r\n"
        )
        nested = bundle / "CA-O-146-CORE_META_MODEL-STEP--child"
        nested.mkdir()
        (nested / "CA-O-147-CORE_META_MODEL-STEP--nested.md").write_bytes(b"nested child bytes\n")
        (bundle / "archived").mkdir()
        (bundle / "archived" / "CA-O-146-CORE_META_MODEL-STEP--child@4.md").write_bytes(
            b"exact historical child bytes\n"
        )
        destination = self.root / PROJECT_OPERATIONS / "CA-O-010-PROJECT_CONFIGURATION-WORKFLOW--bundle-move.md"
        contents = {
            path.relative_to(bundle).as_posix(): path.read_bytes()
            for path in bundle.rglob("*") if path.is_file()
        }
        return source, destination, contents

    @staticmethod
    def _raw_body(payload: bytes) -> bytes:
        return payload.split(b"\n---\n", 1)[1]

    def _destination(self) -> Path:
        return self.root / PROJECT_REQUIREMENTS / "CA-R-100-PROJECT_CONFIGURATION--project-move.md"

    def test_preview_core_to_project_has_no_effect(self) -> None:
        destination = self._destination()
        before = self._snapshot(destination)
        result = move_atom_action(
            self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
            execute=False, authorized=False,
        )

        self.assertEqual(result["outcome"], "preview")
        self.assertEqual(before, self._snapshot(destination))
        self.assertTrue(self.core_path.exists())
        self.assertFalse(destination.exists())

    def test_execute_core_to_project_advances_revision_and_retains_carrier(self) -> None:
        destination = self._destination()
        before_bytes = self.core_path.read_bytes()
        before = atom_operations.atom_from_path(self.root, self.core_path)
        before_version = atom_operations.atom_version(before)
        archive = self.core_path.parent / "archive" / f"{self.core_path.stem}@{before_version}.md"

        result = move_atom_action(
            self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
            execute=True, authorized=True,
        )

        self.assertEqual(result["outcome"], "applied")
        self.assertFalse(self.core_path.exists())
        self.assertTrue(destination.exists())
        self.assertEqual(archive.read_bytes(), before_bytes)
        moved = atom_operations.atom_from_path(self.root, destination)
        self.assertEqual(moved.atom_id, self.move_id)
        self.assertEqual(atom_operations.atom_version(moved), before_version + 1)
        self.assertEqual(moved.content, before.content)
        self.assertEqual(self._raw_body(destination.read_bytes()), self._raw_body(before_bytes))
        self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "status"), "Active")
        self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "current_scope_unit"), "PROJECT_CONFIGURATION")
        self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "claim_target_scope_unit"), "PROJECT_CONFIGURATION")
        self.assertRegex(moved.frontmatter, r'(?m)^updated_at: "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+0000"$')

    def test_execute_project_to_core_preserves_same_identity_and_typed_relations(self) -> None:
        source = self._destination()
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_bytes(self.core_path.read_bytes())
        source.write_text(
            source.read_text(encoding="utf-8").replace("CORE_META_MODEL", "PROJECT_CONFIGURATION"),
            encoding="utf-8",
        )
        self.core_path.unlink()
        destination = self.root / CORE_REQUIREMENTS / "CA-R-100-CORE_META_MODEL--core-return.md"
        before_bytes = source.read_bytes()
        before = atom_operations.atom_from_path(self.root, source)

        result = move_atom_action(
            self.root, self._request(source, destination, "CORE_META_MODEL"),
            execute=True, authorized=True,
        )

        self.assertEqual(result["outcome"], "applied")
        self.assertFalse(source.exists())
        moved = atom_operations.atom_from_path(self.root, destination)
        self.assertEqual(moved.atom_id, self.move_id)
        self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "current_scope_unit"), "CORE_META_MODEL")
        self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "claim_target_scope_unit"), "CORE_META_MODEL")
        self.assertIn("relations: {}", moved.frontmatter)
        self.assertEqual(moved.content, before.content)
        self.assertEqual(self._raw_body(destination.read_bytes()), self._raw_body(before_bytes))

    def test_crlf_body_is_retained_byte_for_byte(self) -> None:
        destination = self._destination()
        payload = self.core_path.read_bytes()
        head, body = payload.split(b"\n---\n", 1)
        body = body.replace(b"\n", b"\r\n")
        self.core_path.write_bytes(head + b"\n---\n" + body)
        before_bytes = self.core_path.read_bytes()

        move_atom_action(
            self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
            execute=True, authorized=True,
        )

        self.assertEqual(self._raw_body(destination.read_bytes()), self._raw_body(before_bytes))

    def test_current_done_and_backlog_statuses_are_retained(self) -> None:
        for status, folder in (("Done", "done"), ("Backlog", "001_backlog")):
            with self.subTest(status=status):
                source = self.root / CORE_PLANS / folder / f"CA-P-200-CORE_META_MODEL--{status.lower()}.md"
                source.parent.mkdir(parents=True, exist_ok=True)
                payload = (
                    "---\natom_id: CA-P-200\ncontent_role: Plan\ntype: Plan\nlabel: Task\n"
                    "current_scope_unit: CORE_META_MODEL\nclaim_target_scope_unit: CORE_META_MODEL\n"
                    "work_sequence_number: 1\nlocal_tier: Standard\nglobal_tier: 14\n"
                    f"author: Anatoly Maslennikov\nstatus: {status}\nversion: 1\n"
                    'updated_at: "2026-01-01 00:00:00 +0000"\nsubjects:\n'
                    "  governs: Atom/Test\n  depends_on: []\nrelations: {}\n---\n"
                    "# Summary\n\nStatus fixture plan\n\n## Objective\n\nMove one plan.\n"
                    "\n## Details\n\n### Definition of Done\n\nThe plan remains complete.\n"
                )
                source.write_text(payload, encoding="utf-8")
                destination = self.root / PROJECT_PLANS / folder / f"CA-P-200-PROJECT_CONFIGURATION--{status.lower()}.md"
                result = move_atom_action(
                    self.root, self._request(source, destination, "PROJECT_CONFIGURATION"),
                    execute=True, authorized=True,
                )
                self.assertEqual(result["outcome"], "applied")
                moved = atom_operations.atom_from_path(self.root, destination)
                self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "status"), status)
                self.assertEqual(atom_operations.atom_version(moved), 2)
                destination.unlink()

    def test_same_location_is_noop_without_revision_history_or_journal_effect(self) -> None:
        before = self._snapshot()
        result = move_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, self.core_path.relative_to(self.root).as_posix()),
             "placement": self._placement(self.core_path, "CORE_META_MODEL")},
            execute=True, authorized=True,
        )

        self.assertEqual(result["outcome"], "no-op")
        self.assertEqual(before, self._snapshot())
        self.assertFalse((self.core_path.parent / "archive").exists())

    def test_stale_source_and_destination_collision_refuse_without_effect(self) -> None:
        destination = self._destination()
        request = self._request(self.core_path, destination, "PROJECT_CONFIGURATION")
        self.core_path.write_bytes(self.core_path.read_bytes() + b"\nDrift.\n")
        before = self._snapshot(destination)
        with self.assertRaisesRegex(LifecycleError, "stale"):
            move_atom_action(self.root, request, execute=True, authorized=True)
        self.assertEqual(before, self._snapshot(destination))

        self.core_path.write_bytes(self.core_path.read_bytes()[:-len(b"\nDrift.\n")])
        destination.write_bytes(b"KEEP EXISTING DESTINATION\n")
        before = self._snapshot(destination)
        with self.assertRaisesRegex(LifecycleError, "collision"):
            move_atom_action(self.root, request, execute=True, authorized=True)
        self.assertEqual(before, self._snapshot(destination))

    def test_invalid_destination_preview_has_no_effect(self) -> None:
        destination = self.root / "outside-control" / self.core_path.name
        before = self._snapshot(destination)
        with self.assertRaises(LifecycleError):
            move_atom_action(
                self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
                execute=False, authorized=False,
            )
        self.assertEqual(before, self._snapshot(destination))

    def test_failed_second_action_leaves_first_move_and_remaining_atom_untouched(self) -> None:
        first_destination = self._destination()
        second_source = self._move_fixture_atom(
            self.fixture.successor_one,
            CORE_REQUIREMENTS / "CA-R-101-CORE_META_MODEL--second.md",
            "CORE_META_MODEL",
        )
        second_destination = self.root / PROJECT_REQUIREMENTS / "CA-R-101-PROJECT_CONFIGURATION--second.md"
        second_before = second_source.read_bytes()

        first = move_atom_action(
            self.root, self._request(self.core_path, first_destination, "PROJECT_CONFIGURATION"),
            execute=True, authorized=True,
        )
        self.assertEqual(first["outcome"], "applied")
        second_destination.write_bytes(b"DO NOT OVERWRITE\n")
        with self.assertRaisesRegex(LifecycleError, "collision"):
            move_atom_action(
                self.root, self._request(second_source, second_destination, "PROJECT_CONFIGURATION"),
                execute=True, authorized=True,
            )
        self.assertTrue(first_destination.exists())
        self.assertEqual(second_source.read_bytes(), second_before)
        self.assertEqual(second_destination.read_bytes(), b"DO NOT OVERWRITE\n")

    def test_failed_publication_restores_source_destination_and_exact_history(self) -> None:
        destination = self._destination()
        before = self._snapshot(destination)
        archive = self.core_path.parent / "archive" / f"{self.core_path.stem}@1.md"
        real_lifecycle_write = lifecycle_intents._atomic_write
        real_atom_write = atom_operations._atomic_write

        def fail_destination(path: Path, content: bytes) -> None:
            if Path(path).resolve() == destination.resolve():
                raise OSError("injected destination publication failure")
            real_lifecycle_write(path, content)

        def fail_atom_destination(path: Path, content: bytes) -> None:
            if Path(path).resolve() == destination.resolve():
                raise OSError("injected destination publication failure")
            real_atom_write(path, content)

        with patch.object(lifecycle_intents, "_atomic_write", side_effect=fail_destination), patch.object(
            atom_operations, "_atomic_write", side_effect=fail_atom_destination
        ):
            with self.assertRaises((LifecycleError, OSError)):
                move_atom_action(
                    self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
                    execute=True, authorized=True,
                )

        self.assertEqual(before, self._snapshot(destination))
        self.assertTrue(self.core_path.exists())
        self.assertFalse(destination.exists())
        self.assertFalse(archive.exists())

    def test_foreign_metadata_edit_during_readback_is_not_deleted(self) -> None:
        """A same-ID destination edit is foreign even when its body is unchanged."""
        destination = self._destination()
        before_bytes = self.core_path.read_bytes()
        real_atom_write = atom_operations._atomic_write
        foreign_bytes: bytes | None = None

        def inject_foreign_metadata(path: Path, content: bytes) -> None:
            nonlocal foreign_bytes
            real_atom_write(path, content)
            if Path(path).resolve() == destination.resolve():
                foreign_bytes = destination.read_bytes().replace(
                    b"author: Anatoly Maslennikov", b"author: External Operator", 1
                )
                destination.write_bytes(foreign_bytes)

        with patch.object(atom_operations, "_atomic_write", side_effect=inject_foreign_metadata):
            result = move_atom_action(
                self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
                execute=True, authorized=True,
            )

        self.assertEqual(result["outcome"], "partial")
        self.assertEqual(result["failure"]["code"], "move-rollback-uncertain")
        self.assertIsNotNone(foreign_bytes)
        self.assertEqual(destination.read_bytes(), foreign_bytes)
        self.assertFalse(self.core_path.exists())
        archive = self.core_path.parent / "archive" / f"{self.core_path.stem}@1.md"
        self.assertTrue(archive.exists())
        self.assertEqual(archive.read_bytes(), before_bytes)
        destination_relative = destination.relative_to(self.root).as_posix()
        self.assertEqual(result["recovery"]["destination"], {
            "path": destination_relative, "verification": "unknown"
        })
        self.assertTrue(any(
            effect["state"] == "unknown"
            and effect.get("carrier", {}).get("path") == destination_relative
            for effect in result["effects"]
        ))
        self.assertIn("prior_revision", result["history"])
        self.assertIn("prior_revision", result["recovery"])

    def test_workflow_bundle_moves_with_exact_nested_and_historical_bytes(self) -> None:
        source, destination, contents = self._workflow_bundle()
        bundle = source.with_suffix("")
        before = atom_operations.atom_from_path(self.root, source)
        before_bytes = source.read_bytes()
        history = source.parent / "archive" / f"{source.stem}@{atom_operations.atom_version(before)}.md"

        result = move_atom_action(
            self.root, self._request(source, destination, "PROJECT_CONFIGURATION"),
            execute=True, authorized=True,
        )

        moved_bundle = destination.with_suffix("")
        self.assertEqual(result["outcome"], "applied")
        self.assertFalse(source.exists())
        self.assertFalse(bundle.exists())
        self.assertEqual(history.read_bytes(), before_bytes)
        self.assertEqual(
            {path.relative_to(moved_bundle).as_posix(): path.read_bytes()
             for path in moved_bundle.rglob("*") if path.is_file()},
            contents,
        )
        moved = atom_operations.atom_from_path(self.root, destination)
        self.assertEqual(atom_operations.atom_version(moved), atom_operations.atom_version(before) + 1)
        self.assertEqual(atom_operations.frontmatter_scalar(moved.frontmatter, "current_scope_unit"), "PROJECT_CONFIGURATION")
        self.assertEqual(
            (moved_bundle / "CA-O-146-CORE_META_MODEL-STEP--child.md").read_bytes(),
            contents["CA-O-146-CORE_META_MODEL-STEP--child.md"],
        )

    def test_matching_destination_directory_collision_is_no_effect(self) -> None:
        source, destination, _ = self._workflow_bundle()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.with_suffix("").mkdir()
        (destination.with_suffix("") / "keep.md").write_bytes(b"do not overwrite\n")
        before = self._snapshot(destination, source.with_suffix(""), destination.with_suffix(""))

        with self.assertRaisesRegex(LifecycleError, "collision"):
            move_atom_action(
                self.root, self._request(source, destination, "PROJECT_CONFIGURATION"),
                execute=True, authorized=True,
            )

        self.assertEqual(before, self._snapshot(destination, source.with_suffix(""), destination.with_suffix("")))

    def test_nested_bundle_drift_during_action_is_not_overwritten(self) -> None:
        source, destination, _ = self._workflow_bundle()
        child = source.with_suffix("") / "CA-O-146-CORE_META_MODEL-STEP--child.md"
        original = child.read_bytes()
        changed = original + b"changed during action\n"
        real_move_atom_revision = lifecycle_intents.move_atom_revision

        def change_child_before_publication(*args, **kwargs):
            child.write_bytes(changed)
            return real_move_atom_revision(*args, **kwargs)

        with patch.object(lifecycle_intents, "move_atom_revision", side_effect=change_child_before_publication):
            result = move_atom_action(
                self.root, self._request(source, destination, "PROJECT_CONFIGURATION"),
                execute=True, authorized=True,
            )

        self.assertEqual(result["outcome"], "partial")
        self.assertFalse(result["recovery"]["automatic_retry"])
        self.assertEqual(child.read_bytes(), changed)
        self.assertTrue(source.exists())
        self.assertTrue(source.with_suffix("").exists())
        self.assertFalse(destination.exists())
        self.assertFalse(destination.with_suffix("").exists())

    def test_directory_move_failure_restores_source_and_exact_history(self) -> None:
        source, destination, _ = self._workflow_bundle()
        source_bundle, destination_bundle = source.with_suffix(""), destination.with_suffix("")
        before = self._snapshot(source, source_bundle, destination, destination_bundle)
        real_atom_from_path = atom_operations.atom_from_path

        def fail_after_bundle_move(root: Path, path: Path):
            if Path(path).resolve() == destination.resolve():
                raise OSError("injected readback failure")
            return real_atom_from_path(root, path)

        with patch.object(atom_operations, "atom_from_path", side_effect=fail_after_bundle_move):
            with self.assertRaises((LifecycleError, OSError)):
                move_atom_action(
                    self.root, self._request(source, destination, "PROJECT_CONFIGURATION"),
                    execute=True, authorized=True,
                )

        self.assertEqual(before, self._snapshot(source, source_bundle, destination, destination_bundle))
        self.assertTrue(source.exists())
        self.assertTrue(source_bundle.exists())
        self.assertFalse(destination.exists())
        self.assertFalse(destination_bundle.exists())

    def test_same_byte_nested_mode_drift_during_readback_is_foreign(self) -> None:
        source, destination, _ = self._workflow_bundle()
        child = source.with_suffix("") / "CA-O-146-CORE_META_MODEL-STEP--child.md"
        child_bytes = child.read_bytes()
        real_snapshot = lifecycle_intents.status_bundle_snapshot
        calls = 0

        def change_child_mode_after_move(root: Path, atom):
            nonlocal calls
            calls += 1
            if calls == 2:
                child_at_destination = destination.with_suffix("") / child.name
                child_at_destination.chmod(0o600)
            return real_snapshot(root, atom)

        with patch.object(lifecycle_intents, "status_bundle_snapshot", side_effect=change_child_mode_after_move):
            result = move_atom_action(
                self.root, self._request(source, destination, "PROJECT_CONFIGURATION"),
                execute=True, authorized=True,
            )

        moved_child = destination.with_suffix("") / child.name
        self.assertEqual(result["outcome"], "partial")
        self.assertFalse(result["recovery"]["automatic_retry"])
        self.assertEqual(moved_child.read_bytes(), child_bytes)
        self.assertEqual(moved_child.stat().st_mode & 0o777, 0o600)
        self.assertFalse(source.exists())
        self.assertFalse(source.with_suffix("").exists())
        self.assertTrue(destination.exists())
        self.assertTrue(destination.with_suffix("").exists())

    def test_unsupported_bundle_is_rejected_without_orphan_effect(self) -> None:
        bundle = self.core_path.with_suffix("")
        bundle.mkdir()
        (bundle / "nested.md").write_text("bundle", encoding="utf-8")
        destination = self._destination()
        before = self._snapshot(destination, bundle)
        with self.assertRaisesRegex(LifecycleError, "bundle"):
            move_atom_action(
                self.root, self._request(self.core_path, destination, "PROJECT_CONFIGURATION"),
                execute=True, authorized=True,
            )
        self.assertEqual(before, self._snapshot(destination, bundle))

    def test_multi_target_request_is_rejected_without_orphan_effect(self) -> None:
        before = self._snapshot()
        descriptor = carrier_descriptor(self.root, self.core_path.relative_to(self.root).as_posix())
        request = {"target": [descriptor, descriptor],
                   "placement": self._placement(self._destination(), "PROJECT_CONFIGURATION")}
        with self.assertRaisesRegex(LifecycleError, "one-target|required|target"):
            move_atom_action(self.root, request, execute=True, authorized=True)
        self.assertEqual(before, self._snapshot())


if __name__ == "__main__":
    unittest.main()
