from __future__ import annotations

import argparse
import copy
import hashlib
import shutil
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
from atom_subject_lookup import run_subject_search  # noqa: E402
from atom_subject_patch import preview_subject_patches  # noqa: E402
from subject_notation import get_profile  # noqa: E402
import test_selected_atom_lifecycle as lifecycle_fixture  # noqa: E402


class NonarchivedSubjectPreviewTests(unittest.TestCase):
    """Real complete-carrier admission against a disposable Project only."""

    def setUp(self) -> None:
        self.fixture = lifecycle_fixture.SelectedAtomLifecycleTest(
            "test_authorized_create_uses_a_complete_carrier_and_rejects_occupied_destination"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        plan_status = lifecycle_fixture.REQUIREMENT_STATUS_AUTHORITY.with_name(
            "CA-R-1539-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-plan-status-values.md"
        )
        destination = self.root / plan_status.relative_to(lifecycle_fixture.REPOSITORY)
        shutil.copyfile(plan_status, destination)
        for profile in ("legacy", "approved"):
            for pin in get_profile(profile).grammar_pins:
                destination = self.root / pin.path
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(lifecycle_fixture.REPOSITORY / pin.path, destination)
                self.assertEqual(pin.sha256, hashlib.sha256(destination.read_bytes()).hexdigest())

    def _plan(self, status: str, *, number: int = 501, folder: str | None = None) -> Path:
        directory = self.fixture.requirements.parent / "03_plan"
        status_folder = {"Active": "", "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled", "Archived": "archived"}
        directory /= status_folder[status] if folder is None else folder
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"CA-P-{number}--subject-fixture.md"
        path.write_bytes((
            "---\r\n"
            f"atom_id: CA-P-{number}\r\n"
            "content_role: Plan\r\n"
            "type: Plan\r\n"
            "current_scope_unit: LIFECYCLE_FIXTURE\r\n"
            "claim_target_scope_unit: LIFECYCLE_FIXTURE\r\n"
            "local_tier: Standard\r\n"
            "global_tier: 14\r\n"
            "# Preserve this unrelated café comment exactly.\r\n"
            "author: Anatoly Maslennikov\r\n"
            f"status: {status}\r\n"
            "version: 7\r\n"
            'updated_at: "2026-01-01 00:00:00 +0000"\r\n'
            "subjects:\r\n"
            '  governs: "Atom/Status"\r\n'
            '  depends_on: [Atom, "Atom/Revision"]\r\n'
            "relations: {}\r\n"
            "---\r\n"
            "# Summary\r\n\r\nSubject fixture\r\n\r\n"
            "## Objective\r\n\r\nKeep the carried Plan status.\r\n\r\n"
            "## Details\r\n\r\nThe exact body mentions Atom/Status.\r\n\r\n"
            "### Definition of Done\r\n\r\nOnly the explicit Subjects change.\r\n"
        ).encode("utf-8"))
        return path

    def _payload(self, path: Path, *, patches: bool = True) -> list[dict[str, object]]:
        parsed = operations.parse_carrier(path.read_bytes(), path)
        return [{
            "selector": path.relative_to(self.root).as_posix(),
            "expected": {
                "atom_id": parsed.metadata["atom_id"],
                "version": parsed.metadata["version"],
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            },
            "subject_patches": [{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}] if patches else [],
        }]

    def _preview(self, payload: list[dict[str, object]]) -> dict[str, object]:
        return preview_subject_patches(
            self.root, payload, timestamp="2026-10-12 10:20:30 +0400"
        )

    def _assert_complete_carrier(self, path: Path) -> None:
        frontmatter, body = operations.split_frontmatter(path.read_text(encoding="utf-8"))
        operations._validate_complete_carrier(self.root, path, frontmatter, body, creating=False)

    def _snapshot(self) -> dict[str, bytes]:
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    def test_by_value_dependency_replacements_bind_original_nodes_and_replay(self) -> None:
        path = self._plan("Backlog")
        before = self._snapshot()
        payload = self._payload(path)
        patches = [
            {"field": "depends_on", "old": "Atom", "new": "Atom/Revision"},
            {"field": "depends_on", "old": "Atom/Revision", "new": "Atom/Revision/Status"},
        ]
        payload[0]["subject_patches"] = patches
        result = self._preview(payload)
        atom = result["atoms"][0]
        self.assertEqual([0, 1], [patch["index"] for patch in atom["patches"]])
        self.assertTrue(all(set(patch["span"]) == {"start", "end"} for patch in atom["patches"]))
        self.assertEqual(patches, atom["subject_intent"]["subject_patches"])
        proposed = operations.parse_carrier(atom["proposed_carrier"].encode(), path)
        self.assertEqual(["Atom/Revision", "Atom/Revision/Status"], proposed.metadata["subjects"]["depends_on"])
        self.assertEqual("Backlog", proposed.metadata["status"])
        prepared = subject_patch.prepare_subject_intent(self.root, atom["subject_intent"]["target"], patches)
        materialized = subject_patch.materialize_subject_intent(self.root, prepared, "2026-10-14 00:40:00 +0400")
        self.assertEqual(["Atom/Revision", "Atom/Revision/Status"], operations.parse_carrier(materialized["carrier_bytes"], path).metadata["subjects"]["depends_on"])
        self.assertEqual(before, self._snapshot())

    def _installed_copy(self, path: Path, *, collection: str | None = None) -> Path:
        from RELEASE_VERSION.methodology_layout import resolve_methodology_layout

        layout = resolve_methodology_layout(self.root)
        copied = self.root / layout.installed_root / (collection or Path(layout.source_copy_root).name)
        destination = copied / "LIFECYCLE_FIXTURE" / path.relative_to(self.fixture.requirements.parent)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, destination)
        return destination

    def test_real_complete_validator_accepts_the_status_fixtures(self) -> None:
        self._assert_complete_carrier(self.fixture.target)
        for number, status in enumerate(("Active", "Backlog", "Done", "Canceled"), start=501):
            with self.subTest(status=status):
                self._assert_complete_carrier(self._plan(status, number=number))

    def test_nonarchived_plan_preview_preserves_status_and_all_unrelated_bytes(self) -> None:
        for number, status in enumerate(("Active", "Backlog", "Done", "Canceled"), start=501):
            with self.subTest(status=status):
                path = self._plan(status, number=number)
                self._assert_complete_carrier(path)
                before = self._snapshot()
                original = path.read_bytes()
                preview = self._preview(self._payload(path))
                atom = preview["atoms"][0]
                expected = original.replace(b'governs: "Atom/Status"', b'governs: "Atom/State"')
                expected = expected.replace(b"version: 7\r\n", b"version: 8\r\n")
                expected = expected.replace(b'updated_at: "2026-01-01 00:00:00 +0000"', b'updated_at: "2026-10-12 10:20:30 +0400"')
                self.assertEqual(expected, atom["proposed_carrier"].encode("utf-8"))
                self.assertEqual(7, atom["before_version"])
                self.assertEqual(8, atom["after_version"])
                self.assertEqual(before, self._snapshot())

    def test_nonarchived_plan_noop_keeps_the_full_carrier_and_version(self) -> None:
        path = self._plan("Done")
        self._assert_complete_carrier(path)
        before = self._snapshot()
        preview = self._preview(self._payload(path, patches=False))
        atom = preview["atoms"][0]
        self.assertTrue(atom["noop"])
        self.assertEqual(path.read_bytes(), atom["proposed_carrier"].encode("utf-8"))
        self.assertEqual(atom["before_version"], atom["after_version"])
        self.assertEqual(before, self._snapshot())

    def test_default_lookup_still_filters_nonactive_plan_statuses(self) -> None:
        for number, status in enumerate(("Active", "Backlog", "Done", "Canceled"), start=501):
            self._plan(status, number=number)
        before = self._snapshot()
        args = argparse.Namespace(subject="Atom/Status", content_role=["Plan"])
        active = run_subject_search(self.root, args)
        self.assertEqual(["CA-P-501"], [row["atom_id"] for row in active["occurrences"]])
        args.lifecycle = "all"
        all_statuses = run_subject_search(self.root, args)
        self.assertEqual({"Active", "Backlog", "Done", "Canceled"},
                         {row["status"] for row in all_statuses["occurrences"]})
        self.assertEqual(before, self._snapshot())

    def test_archived_and_draft_sources_are_ineligible(self) -> None:
        archived = self._plan("Archived")
        self._assert_complete_carrier(archived)
        draft = self.fixture._atom("CA-R-501", "draft-fixture", "Draft fixture", status="Draft")
        draft_payload = self._payload(draft, patches=False)
        draft_folder = draft.parent / "draft"
        draft_folder.mkdir()
        draft = draft.rename(draft_folder / "CA-R--draft-fixture.md")
        draft.write_bytes(draft.read_bytes().replace(b"atom_id: CA-R-501\n", b""))
        self._assert_complete_carrier(draft)
        draft_payload[0]["selector"] = draft.relative_to(self.root).as_posix()
        draft_payload[0]["expected"]["sha256"] = hashlib.sha256(draft.read_bytes()).hexdigest()
        for path, payload in ((archived, self._payload(archived, patches=False)), (draft, draft_payload)):
            with self.subTest(path=path):
                before = self._snapshot()
                with self.assertRaises(operations.ToolError) as invalid:
                    self._preview(payload)
                self.assertEqual("atom-not-active", invalid.exception.code)
                self.assertEqual(before, self._snapshot())

    def test_bad_placement_and_role_status_are_rejected_by_complete_validation(self) -> None:
        bad_placement = self._plan("Backlog", folder="backlog")
        bad_status = self.fixture._atom("CA-R-501", "bad-status", "Stable summary", status="Done")
        for path in (bad_placement, bad_status):
            with self.subTest(path=path):
                with self.assertRaises(operations.ToolError) as invalid:
                    self._assert_complete_carrier(path)
                self.assertEqual("complete-carrier-invalid", invalid.exception.code)
                before = self._snapshot()
                with self.assertRaises(operations.ToolError) as invalid:
                    self._preview(self._payload(path, patches=False))
                self.assertEqual("complete-carrier-invalid", invalid.exception.code)
                self.assertEqual(before, self._snapshot())

    def test_each_stale_pin_is_rejected_without_mutation(self) -> None:
        path = self._plan("Active")
        self._assert_complete_carrier(path)
        before = self._snapshot()
        for key, value in (("atom_id", "CA-P-999"), ("version", 6), ("sha256", "0" * 64)):
            with self.subTest(key=key):
                payload = copy.deepcopy(self._payload(path))
                payload[0]["expected"][key] = value
                with self.assertRaises(operations.ToolError) as invalid:
                    self._preview(payload)
                self.assertEqual("subject-pin-stale", invalid.exception.code)
                self.assertEqual(before, self._snapshot())

    def test_duplicate_original_elsewhere_rejects_singleton_changed_and_noop_previews(self) -> None:
        for number, other_status in enumerate(("Active", "Backlog"), start=510):
            selected = self._plan("Done", number=number)
            duplicate = self._plan(other_status, number=number)
            self._assert_complete_carrier(selected)
            self._assert_complete_carrier(duplicate)
            self._installed_copy(selected)
            before = self._snapshot()
            for patches in (True, False):
                with self.subTest(other_status=other_status, patches=patches):
                    with self.assertRaises(operations.ToolError) as invalid:
                        self._preview(self._payload(selected, patches=patches))
                    self.assertEqual("subject-identity-duplicate", invalid.exception.code)
                    self.assertEqual(before, self._snapshot())

    def test_declared_installed_source_copy_does_not_compete_with_original(self) -> None:
        from lifecycle_intents import carrier_descriptor

        selected = self._plan("Done")
        self._installed_copy(selected)
        before = self._snapshot()
        target = carrier_descriptor(self.root, selected.relative_to(self.root).as_posix())
        for patches in (True, False):
            with self.subTest(patches=patches):
                payload = self._payload(selected, patches=patches)
                preview = self._preview(payload)
                self.assertEqual(1, preview["count"])
                self.assertEqual(not patches, preview["noop"])
                prepared = subject_patch.prepare_subject_intent(self.root, target, payload[0]["subject_patches"])
                materialized = subject_patch.materialize_subject_intent(self.root, prepared, "2026-10-12 10:20:30 +0400")
                self.assertEqual(preview["atoms"][0]["proposed_carrier"].encode(), materialized["carrier_bytes"])
                self.assertEqual(before, self._snapshot())

    def test_installed_source_copy_cannot_be_selected_as_an_original(self) -> None:
        selected = self._plan("Done")
        copied = self._installed_copy(selected)
        before = self._snapshot()
        for patches in (True, False):
            with self.subTest(patches=patches), self.assertRaises(operations.ToolError) as invalid:
                self._preview(self._payload(copied, patches=patches))
            self.assertEqual("complete-carrier-invalid", invalid.exception.code)
            self.assertEqual(before, self._snapshot())

    def test_installed_root_outside_declared_source_copy_collection_still_competes(self) -> None:
        selected = self._plan("Done")
        self._installed_copy(selected, collection="unclassified")
        before = self._snapshot()
        with self.assertRaises(operations.ToolError) as invalid:
            self._preview(self._payload(selected))
        self.assertEqual("subject-identity-duplicate", invalid.exception.code)
        self.assertEqual(before, self._snapshot())

    def test_absent_or_invalid_release_layout_grants_no_copy_exemption(self) -> None:
        selected = self._plan("Done")
        self._installed_copy(selected)
        registry = operations.control_root(self.root) / "project_structure.toml"
        original = registry.read_bytes()
        for declaration in ("missing", "invalid"):
            with self.subTest(declaration=declaration):
                if declaration == "missing":
                    registry.unlink()
                else:
                    registry.write_bytes(original.replace(b'scope_unit_name = "METHODOLOGY_SOURCES"',
                                                          b'scope_unit_name = "UNDECLARED_SOURCES"'))
                layout = subject_patch._capture_identity_layout(operations, self.root)
                self.assertIsNone(layout)
                before = self._snapshot()
                with self.assertRaises(operations.ToolError) as invalid:
                    subject_patch._assert_original_identity_unique(operations, self.root, {"CA-P-501"}, layout)
                self.assertEqual("subject-identity-duplicate", invalid.exception.code)
                self.assertEqual(before, self._snapshot())
                registry.write_bytes(original)

    def test_layout_change_after_materialization_blocks_preview_and_intent_materialization(self) -> None:
        from lifecycle_intents import carrier_descriptor

        selected = self._plan("Done")
        self._installed_copy(selected)
        registry = operations.control_root(self.root) / "project_structure.toml"
        materialize = subject_patch._materialize_item
        original = registry.read_bytes()
        for operation in ("preview", "materialize"):
            payload = self._payload(selected)
            target = carrier_descriptor(self.root, selected.relative_to(self.root).as_posix())
            prepared = subject_patch.prepare_subject_intent(self.root, target, payload[0]["subject_patches"])
            injected: list[dict[str, bytes]] = []

            def materialize_then_change_layout(*args: object, **kwargs: object) -> dict[str, object]:
                result = materialize(*args, **kwargs)
                registry.write_bytes(original + b"\n# Changed layout observation.\n")
                injected.append(self._snapshot())
                return result

            with self.subTest(operation=operation), patch.object(
                subject_patch, "_materialize_item", side_effect=materialize_then_change_layout
            ), self.assertRaises(operations.ToolError) as invalid:
                if operation == "preview":
                    self._preview(payload)
                else:
                    subject_patch.materialize_subject_intent(self.root, prepared, "2026-10-12 10:20:30 +0400")
            self.assertEqual("subject-source-changed", invalid.exception.code)
            self.assertEqual(injected[-1], self._snapshot())
            registry.write_bytes(original)

    def test_installed_copy_read_remains_fingerprinted_and_currentness_checked(self) -> None:
        selected = self._plan("Done")
        copied = self._installed_copy(selected)
        read = subject_patch.ReadContext.read
        injected: list[dict[str, bytes]] = []

        def read_then_change_copy(reader: object, path: Path, *, remember: bool = True) -> bytes:
            raw = read(reader, path, remember=remember)
            if path == copied and not injected:
                copied.write_bytes(raw + b"\nChanged delivered copy.\n")
                injected.append(self._snapshot())
            return raw

        with patch.object(subject_patch.ReadContext, "read", autospec=True, side_effect=read_then_change_copy), \
                self.assertRaises(operations.ToolError) as invalid:
            self._preview(self._payload(selected))
        self.assertEqual("subject-source-changed", invalid.exception.code)
        self.assertEqual(injected[-1], self._snapshot())

    def test_installed_source_copy_file_and_collection_symlinks_are_not_exempt(self) -> None:
        from RELEASE_VERSION.methodology_layout import resolve_methodology_layout

        selected = self._plan("Done")
        copied = self._installed_copy(selected)
        copied.unlink()
        copied.symlink_to(selected)
        before = self._snapshot()
        with self.assertRaises(operations.ToolError) as invalid:
            self._preview(self._payload(selected))
        self.assertEqual("subject-identity-inventory-unavailable", invalid.exception.code)
        self.assertEqual(before, self._snapshot())
        copied.unlink()
        layout = resolve_methodology_layout(self.root)
        collection = self.root / layout.installed_root / Path(layout.source_copy_root).name
        moved = collection.rename(collection.with_name("unclassified"))
        collection.symlink_to(moved, target_is_directory=True)
        before = self._snapshot()
        with self.assertRaises(operations.ToolError) as invalid:
            self._preview(self._payload(selected))
        self.assertEqual("subject-identity-inventory-unavailable", invalid.exception.code)
        self.assertEqual(before, self._snapshot())

    def test_archived_historical_revision_does_not_duplicate_the_original(self) -> None:
        selected = self._plan("Done")
        historical = self._plan("Archived")
        historical = historical.rename(historical.with_name("CA-P-501--subject-fixture@6.md"))
        historical.write_bytes(historical.read_bytes().replace(b"version: 7\r\n", b"version: 6\r\n"))
        self._assert_complete_carrier(selected)
        self._assert_complete_carrier(historical)
        before = self._snapshot()
        for patches in (True, False):
            with self.subTest(patches=patches):
                preview = self._preview(self._payload(selected, patches=patches))
                self.assertEqual(1, preview["count"])
                atom = preview["atoms"][0]
                self.assertEqual("CA-P-501", atom["atom_id"])
                self.assertEqual(7, atom["before_version"])
                self.assertEqual(8 if patches else 7, atom["after_version"])
                self.assertEqual(before, self._snapshot())

    def test_malformed_competitor_claims_by_filename_or_frontmatter_block_preview(self) -> None:
        for number, claim in enumerate(("filename", "frontmatter"), start=520):
            selected = self._plan("Done", number=number)
            competitor = self._plan("Active", number=number if claim == "filename" else number + 100)
            self._assert_complete_carrier(selected)
            self._assert_complete_carrier(competitor)
            self._installed_copy(selected)
            raw = competitor.read_bytes().replace(b'  governs: "Atom/Status"', b"  governs: [unfinished")
            if claim == "frontmatter":
                raw = raw.replace(f"atom_id: CA-P-{number + 100}\r\n".encode(),
                                  f"atom_id: CA-P-{number}\r\n".encode())
            competitor.write_bytes(raw)
            before = self._snapshot()
            for patches in (True, False):
                with self.subTest(claim=claim, patches=patches):
                    with self.assertRaises(operations.ToolError) as invalid:
                        self._preview(self._payload(selected, patches=patches))
                    self.assertEqual("subject-identity-inventory-unavailable", invalid.exception.code)
                    self.assertEqual(before, self._snapshot())

    def test_duplicate_inserted_after_materialization_blocks_changed_and_noop_previews(self) -> None:
        materialize = subject_patch._materialize_item
        for number, patches in enumerate((True, False), start=530):
            selected = self._plan("Done", number=number)
            injected: list[dict[str, bytes]] = []

            def materialize_then_insert(*args: object, **kwargs: object) -> dict[str, object]:
                result = materialize(*args, **kwargs)
                self._plan("Backlog", number=number)
                injected.append(self._snapshot())
                return result

            with self.subTest(patches=patches), patch.object(
                subject_patch, "_materialize_item", side_effect=materialize_then_insert
            ):
                with self.assertRaises(operations.ToolError) as invalid:
                    self._preview(self._payload(selected, patches=patches))
            self.assertEqual("subject-identity-duplicate", invalid.exception.code)
            self.assertEqual(1, len(injected))
            self.assertEqual(injected[0], self._snapshot())

    def test_identity_membership_change_during_real_read_blocks_changed_and_noop_previews(self) -> None:
        read = subject_patch.ReadContext.read
        for number, patches in enumerate((True, False), start=540):
            selected = self._plan("Done", number=number)
            injected: list[dict[str, bytes]] = []

            def read_then_insert(reader: object, path: Path, *, remember: bool = True) -> bytes:
                raw = read(reader, path, remember=remember)
                if path == selected and not injected:
                    self._plan("Active", number=number)
                    injected.append(self._snapshot())
                return raw

            with self.subTest(patches=patches), patch.object(
                subject_patch.ReadContext, "read", autospec=True, side_effect=read_then_insert
            ):
                with self.assertRaises(operations.ToolError) as invalid:
                    self._preview(self._payload(selected, patches=patches))
            self.assertEqual("subject-source-changed", invalid.exception.code)
            self.assertEqual(1, len(injected))
            self.assertEqual(injected[0], self._snapshot())

    def test_existing_identityless_member_gaining_selected_id_during_final_read_blocks_preview(self) -> None:
        read = subject_patch.ReadContext.read
        materialize = subject_patch._materialize_item
        for number, patches in enumerate((True, False), start=550):
            selected = self._plan("Done", number=number)
            candidate = self._plan("Active", number=number + 100)
            candidate = candidate.rename(candidate.with_name(f"identityless-{number}.md"))
            candidate.write_bytes(candidate.read_bytes().replace(
                f"atom_id: CA-P-{number + 100}\r\n".encode(), b""
            ))
            materialized = [False]
            injected: list[dict[str, bytes]] = []

            def mark_materialized(*args: object, **kwargs: object) -> dict[str, object]:
                result = materialize(*args, **kwargs)
                materialized[0] = True
                return result

            def read_then_claim_id(reader: object, path: Path, *, remember: bool = True) -> bytes:
                raw = read(reader, path, remember=remember)
                if path == candidate and materialized[0] and not injected:
                    candidate.write_bytes(raw.replace(
                        b"---\r\n", f"---\r\natom_id: CA-P-{number}\r\n".encode(), 1
                    ))
                    injected.append(self._snapshot())
                return raw

            with self.subTest(patches=patches), \
                    patch.object(subject_patch, "_materialize_item", side_effect=mark_materialized), \
                    patch.object(subject_patch.ReadContext, "read", autospec=True, side_effect=read_then_claim_id):
                with self.assertRaises(operations.ToolError) as invalid:
                    self._preview(self._payload(selected, patches=patches))
            self.assertEqual("subject-source-changed", invalid.exception.code)
            self.assertEqual(1, len(injected))
            self.assertEqual(injected[0], self._snapshot())
            self._assert_complete_carrier(candidate)

    def test_original_role_directory_symlink_blocks_identity_inventory(self) -> None:
        selected = self._plan("Done")
        competitor = self._plan("Active")
        self._assert_complete_carrier(selected)
        self._assert_complete_carrier(competitor)
        outside = self.root / "outside-control"
        outside.mkdir()
        link = competitor.parent / "aliased-originals"
        competitor.rename(outside / competitor.name)
        link.symlink_to(outside, target_is_directory=True)
        before = self._snapshot()
        with self.assertRaises(operations.ToolError) as invalid:
            self._preview(self._payload(selected))
        self.assertEqual("subject-identity-inventory-unavailable", invalid.exception.code)
        self.assertTrue(link.is_symlink())
        self.assertEqual(before, self._snapshot())


if __name__ == "__main__":
    unittest.main()
