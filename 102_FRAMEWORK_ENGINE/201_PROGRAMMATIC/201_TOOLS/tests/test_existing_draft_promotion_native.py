"""Native same-identity Draft promotion checks on synthetic Projects."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "tests")]

from atom_operations import (  # noqa: E402
    ToolError,
    atom_from_path,
    frontmatter_scalar,
    render,
    replace_frontmatter_scalar,
    run_promote,
    scan_atoms,
)
from lifecycle_intents import carrier_descriptor, create_atom_action  # noqa: E402
import atom_operations  # noqa: E402
import test_model_driven_status_lifecycle as fixture_module  # noqa: E402


ROLE_DIRECTORIES = {row[0]: row[2] for row in fixture_module.DOMAINS}


class ExistingDraftPromotionNativeTest(unittest.TestCase):
    """Only disposable Projects and checked-in frozen authority are writable."""

    def setUp(self) -> None:
        fixture_module.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = fixture_module.ModelDrivenStatusLifecycleTest("run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def _role_root(self, path: Path, role: str) -> Path:
        expected = ROLE_DIRECTORIES[role]
        for parent in path.parents:
            if parent.name == expected:
                return parent
        raise AssertionError(f"role root not found for {path}")

    def _prepare_existing_marker(
        self,
        *,
        role: str = "Requirement",
        current_status: str = "Active",
        number: int = 123,
        container: str | None = None,
        relations: str = "relations: {}",
        marker_form: str = "qualified",
        proposed_version: int = 4,
        content_delta: bool = True,
    ) -> dict[str, object]:
        current_path = self.fixture.atom(
            role, current_status, number=number, container=container, relations=relations
        )
        current = atom_from_path(self.fixture.root, current_path)
        assert current.atom_id is not None
        if marker_form == "qualified":
            marker = f"{current.atom_id}@{proposed_version}-draft"
        elif marker_form == "legacy":
            marker = f"{current.atom_id}@draft"
        else:
            raise AssertionError(f"unknown marker form: {marker_form}")
        role_root = self._role_root(current_path, role)
        draft_root = role_root / container if container else role_root
        draft_path = draft_root / "draft" / f"{marker}--native.md"
        frontmatter = replace_frontmatter_scalar(current.frontmatter, "atom_id", marker)
        frontmatter = replace_frontmatter_scalar(frontmatter, "status", "Draft")
        frontmatter = replace_frontmatter_scalar(frontmatter, "version", str(proposed_version))
        content = current.content + ("\nNative Draft edit.\n" if content_delta else "")
        carrier = {
            "path": draft_path.relative_to(self.fixture.root).as_posix(),
            "frontmatter": frontmatter,
            "content": content,
        }
        create_atom_action(self.fixture.root, {"carrier": carrier}, execute=True, authorized=True)
        draft = atom_from_path(self.fixture.root, draft_path)
        return {
            "current_path": current_path,
            "current": current,
            "current_bytes": current_path.read_bytes(),
            "draft_path": draft_path,
            "draft": draft,
            "draft_bytes": draft_path.read_bytes(),
            "item": {
                "selector": draft.relative,
                "target": carrier_descriptor(self.fixture.root, draft),
                "atom_id": current.atom_id,
                "canonical_target": carrier_descriptor(self.fixture.root, current),
                "proposed_version": proposed_version,
            },
        }

    def _prepare_role_only_marker(
        self,
        *,
        role: str = "Requirement",
        number: int = 1800,
    ) -> dict[str, object]:
        """Create one role-only Draft marker with no canonical target."""

        role_letter = next(row[1] for row in fixture_module.DOMAINS if row[0] == role)
        role_root = self.fixture.root / fixture_module.CONTROL / "fixture" / ROLE_DIRECTORIES[role]
        draft_path = role_root / "draft" / f"CA-{role_letter}-draft--STATUS_FIXTURE-{role.upper()}--native.md"
        carrier = self.fixture.create_carrier(role, "Draft", number=number)
        carrier["path"] = draft_path.relative_to(self.fixture.root).as_posix()
        carrier["frontmatter"] = replace_frontmatter_scalar(
            carrier["frontmatter"], "atom_id", f"CA-{role_letter}-draft"
        )
        carrier["content"] += "\nNative role-only Draft marker.\n"
        create_atom_action(self.fixture.root, {"carrier": carrier}, execute=True, authorized=True)
        draft = atom_from_path(self.fixture.root, draft_path)
        fresh_id = f"CA-{role_letter}-{number}"
        return {
            "draft_path": draft_path,
            "draft": draft,
            "draft_bytes": draft_path.read_bytes(),
            "item": {
                "selector": draft.relative,
                "target": carrier_descriptor(self.fixture.root, draft),
                "atom_id": fresh_id,
            },
            "fresh_id": fresh_id,
        }

    def _prepare_id_free_draft(
        self,
        *,
        role: str = "Requirement",
        number: int = 1810,
    ) -> dict[str, object]:
        """Create the unchanged ID-free native promotion baseline."""

        role_letter = next(row[1] for row in fixture_module.DOMAINS if row[0] == role)
        role_root = self.fixture.root / fixture_module.CONTROL / "fixture" / ROLE_DIRECTORIES[role]
        draft_path = role_root / "draft" / f"CA-{role_letter}--STATUS_FIXTURE-{role.upper()}--native-id-free.md"
        carrier = self.fixture.create_carrier(role, "Draft", number=number)
        carrier["path"] = draft_path.relative_to(self.fixture.root).as_posix()
        carrier["content"] += "\nNative ID-free Draft baseline.\n"
        create_atom_action(self.fixture.root, {"carrier": carrier}, execute=True, authorized=True)
        draft = atom_from_path(self.fixture.root, draft_path)
        fresh_id = f"CA-{role_letter}-{number}"
        return {
            "draft_path": draft_path,
            "draft": draft,
            "item": {"selector": draft.relative, "atom_id": fresh_id},
            "fresh_id": fresh_id,
        }

    def _packet(self, item: dict[str, object], name: str = "promotion.json") -> Path:
        return self._packet_items([item], name)

    def _packet_items(self, items: list[dict[str, object]], name: str = "promotion.json") -> Path:
        path = self.fixture.root / name
        path.write_text(json.dumps({"atoms": items}, sort_keys=True), encoding="utf-8")
        return path

    def _invoke(self, packet: Path, *, apply: bool) -> dict[str, object]:
        return run_promote(
            self.fixture.root,
            argparse.Namespace(input=packet, apply=apply),
        )

    def _run(self, item: dict[str, object], *, apply: bool, name: str = "promotion.json") -> dict[str, object]:
        return self._invoke(self._packet(item, name), apply=apply)

    def _current(self, atom_id: str):
        matches = [
            atom for atom in scan_atoms(self.fixture.root)
            if atom.atom_id == atom_id and atom.lifecycle not in {"draft", "archived"}
        ]
        self.assertEqual(1, len(matches), f"expected one current carrier for {atom_id}")
        return matches[0]

    def _archived(self, atom_id: str, version: int):
        matches = [
            atom for atom in scan_atoms(self.fixture.root)
            if atom.atom_id == atom_id and atom.lifecycle == "archived"
            and int(frontmatter_scalar(atom.frontmatter, "version") or -1) == version
        ]
        self.assertEqual(1, len(matches), f"expected one archived Version {version} for {atom_id}")
        return matches[0]

    def _assert_changed_promotion(self, case: dict[str, object], *, moved: bool = False) -> None:
        current = case["current"]
        current_path = case["current_path"]
        draft_path = case["draft_path"]
        assert current.atom_id is not None
        observed = self._current(current.atom_id)
        self.assertEqual("Active", frontmatter_scalar(observed.frontmatter, "status"))
        self.assertEqual("4", frontmatter_scalar(observed.frontmatter, "version"))
        if moved:
            self.assertNotEqual(current_path, observed.path)
            self.assertEqual(self._role_root(current_path, "Plan"), observed.path.parent)
        else:
            self.assertEqual(current_path, observed.path)
        self.assertFalse(draft_path.exists())
        predecessor = self._archived(current.atom_id, 3)
        self.assertEqual(case["current_bytes"], predecessor.path.read_bytes())

    def test_qualified_and_legacy_same_identity_promotions_archive_exact_predecessor(self) -> None:
        for offset, marker_form in enumerate(("qualified", "legacy")):
            with self.subTest(marker_form=marker_form):
                case = self._prepare_existing_marker(
                    number=123 + offset,
                    marker_form=marker_form,
                    proposed_version=4,
                )
                preview_packet = self._packet(case["item"], f"preview-{offset}.json")
                before_preview = self.fixture.snapshot()
                preview = self._invoke(preview_packet, apply=False)
                self.assertEqual(1, preview["count"])
                self.assertEqual(before_preview, self.fixture.snapshot())
                self._run(case["item"], apply=True, name=f"apply-{offset}.json")
                self._assert_changed_promotion(case)

    def test_role_only_marker_gets_explicit_fresh_identity_and_id_free_baseline_stays_supported(self) -> None:
        role_marker = self._prepare_role_only_marker(number=1800)
        preview_packet = self._packet(role_marker["item"], "role-marker-preview.json")
        before_preview = self.fixture.snapshot()
        preview = self._invoke(preview_packet, apply=False)
        self.assertEqual(1, preview["count"])
        self.assertEqual(before_preview, self.fixture.snapshot())
        applied = self._invoke(self._packet(role_marker["item"], "role-marker-apply.json"), apply=True)
        self.assertEqual(1, applied["count"])
        observed = self._current(role_marker["fresh_id"])
        self.assertEqual("Active", frontmatter_scalar(observed.frontmatter, "status"))
        self.assertEqual(role_marker["fresh_id"], frontmatter_scalar(observed.frontmatter, "atom_id"))
        self.assertIn("Native role-only Draft marker.", observed.content)
        self.assertFalse(role_marker["draft_path"].exists())

        id_free = self._prepare_id_free_draft(number=1810)
        self._invoke(self._packet(id_free["item"], "id-free-apply.json"), apply=True)
        observed_id_free = self._current(id_free["fresh_id"])
        self.assertEqual("Active", frontmatter_scalar(observed_id_free.frontmatter, "status"))
        self.assertIn("Native ID-free Draft baseline.", observed_id_free.content)
        self.assertFalse(id_free["draft_path"].exists())

    def test_native_marker_batch_rejects_multi_and_mixed_actions_before_effects(self) -> None:
        first = self._prepare_role_only_marker(role="Requirement", number=1820)
        second = self._prepare_role_only_marker(role="Method", number=1821)
        cases = [("multi-marker", [first["item"], second["item"]])]

        existing = self._prepare_existing_marker(number=1822, proposed_version=4)
        third = self._prepare_role_only_marker(role="Evaluation", number=1823)
        cases.append(("mixed-existing-and-role-only", [existing["item"], third["item"]]))

        for name, items in cases:
            with self.subTest(name=name):
                packet = self._packet_items(items, f"{name}.json")
                before = self.fixture.snapshot()
                with self.assertRaises(ToolError) as raised:
                    self._invoke(packet, apply=True)
                self.assertEqual("mixed-draft-promotion-batch-unadmitted", raised.exception.code)
                self.assertEqual(before, self.fixture.snapshot())

    def test_legacy_exact_noop_keeps_canonical_version_time_and_no_archive(self) -> None:
        case = self._prepare_existing_marker(
            number=130,
            marker_form="legacy",
            proposed_version=3,
            content_delta=False,
        )
        current = case["current"]
        assert current.atom_id is not None
        before_bytes = case["current_bytes"]
        before_updated_at = frontmatter_scalar(current.frontmatter, "updated_at")
        packet = self._packet(case["item"], "legacy-exact-noop.json")
        before_snapshot = self.fixture.snapshot()
        self._invoke(packet, apply=True)
        self.assertEqual(before_snapshot, self.fixture.snapshot())
        observed = self._current(current.atom_id)
        self.assertEqual(current.path, observed.path)
        self.assertEqual(before_bytes, observed.path.read_bytes())
        self.assertEqual("3", frontmatter_scalar(observed.frontmatter, "version"))
        self.assertEqual(before_updated_at, frontmatter_scalar(observed.frontmatter, "updated_at"))
        self.assertTrue(case["draft_path"].exists())
        self.assertEqual(case["draft_bytes"], case["draft_path"].read_bytes())
        self.assertFalse(any(
            atom.atom_id == current.atom_id and atom.lifecycle == "archived"
            for atom in scan_atoms(self.fixture.root)
        ))

    def test_plan_done_current_promotes_to_active_with_real_history_and_exact_archive(self) -> None:
        parent_path = self.fixture.atom("Plan", "Active", number=7999)
        case = self._prepare_existing_marker(
            role="Plan",
            current_status="Done",
            number=1400,
            container=parent_path.stem,
            relations="relations:\n  is_decomposition_of: [CA-P-7999]",
            marker_form="qualified",
            proposed_version=4,
        )
        current = case["current"]
        assert current.atom_id is not None
        local_root = case["current_path"].parent.parent
        old_history = local_root / "archive" / f"{case['current_path'].stem}@2.md"
        old_history.parent.mkdir(parents=True, exist_ok=True)
        old_frontmatter = replace_frontmatter_scalar(current.frontmatter, "status", "Archived")
        old_frontmatter = replace_frontmatter_scalar(old_frontmatter, "version", "2")
        old_history.write_bytes(render(old_frontmatter, current.content))
        old_history_bytes = old_history.read_bytes()

        self._run(case["item"], apply=True)
        observed = self._current(current.atom_id)
        self.assertEqual("Active", frontmatter_scalar(observed.frontmatter, "status"))
        self.assertEqual(local_root, observed.path.parent)
        self.assertFalse(case["draft_path"].exists())
        self.assertEqual(case["current_bytes"], self._archived(current.atom_id, 3).path.read_bytes())
        self.assertEqual(old_history_bytes, old_history.read_bytes())

    def test_stale_canonical_or_draft_descriptor_refuses_without_effect(self) -> None:
        for offset, drift in enumerate(("canonical", "draft")):
            with self.subTest(drift=drift):
                case = self._prepare_existing_marker(number=1500 + offset, proposed_version=4)
                if drift == "canonical":
                    case["current_path"].write_bytes(case["current_bytes"] + b"\nCanonical drift.\n")
                else:
                    case["draft_path"].write_bytes(case["draft_bytes"] + b"\nDraft drift.\n")
                packet = self._packet(case["item"], f"stale-{offset}.json")
                before = self.fixture.snapshot()
                with self.assertRaises(ToolError) as raised:
                    self._invoke(packet, apply=True)
                self.assertEqual("stale-carrier", raised.exception.code)
                self.assertEqual(before, self.fixture.snapshot())

    def test_version_mismatch_and_duplicate_current_refuse_without_effect(self) -> None:
        mismatch = self._prepare_existing_marker(number=1600, proposed_version=5)
        mismatch_packet = self._packet(mismatch["item"], "mismatch.json")
        before_mismatch = self.fixture.snapshot()
        with self.assertRaises(ToolError) as raised:
            self._invoke(mismatch_packet, apply=True)
        self.assertEqual("atom-version-invalid", raised.exception.code)
        self.assertEqual(before_mismatch, self.fixture.snapshot())

        duplicate = self._prepare_existing_marker(
            role="Plan",
            current_status="Done",
            number=1610,
            proposed_version=4,
        )
        current = duplicate["current"]
        duplicate_path = self._role_root(duplicate["current_path"], "Plan") / "canceled" / "CA-P-1610--duplicate.md"
        duplicate_path.parent.mkdir(parents=True, exist_ok=True)
        duplicate_raw = replace_frontmatter_scalar(current.frontmatter, "status", "Canceled")
        duplicate_path.write_bytes(render(duplicate_raw, current.content))
        duplicate_packet = self._packet(duplicate["item"], "duplicate.json")
        before_duplicate = self.fixture.snapshot()
        with self.assertRaises(ToolError) as raised:
            self._invoke(duplicate_packet, apply=True)
        self.assertEqual("atom-identity-duplicate", raised.exception.code)
        self.assertEqual(before_duplicate, self.fixture.snapshot())

    def test_postwrite_failure_restores_exact_promotion_before_state(self) -> None:
        case = self._prepare_existing_marker(number=9901, proposed_version=4)
        packet = self._packet(case["item"], "recovery.json")
        before = {
            path.relative_to(self.fixture.root).as_posix(): path.read_bytes()
            for path in self.fixture.root.rglob("*") if path.is_file()
        }
        real_write = atom_operations.write_raw_atom_revision
        calls = 0

        def fail_after_first(*args: object, **kwargs: object) -> object:
            nonlocal calls
            calls += 1
            result = real_write(*args, **kwargs)
            if calls == 1:
                raise OSError("injected promotion publication failure")
            return result

        with patch.object(atom_operations, "write_raw_atom_revision", side_effect=fail_after_first):
            with self.assertRaises((ToolError, OSError)):
                self._invoke(packet, apply=True)
        self.assertGreaterEqual(calls, 1)
        after = {
            path.relative_to(self.fixture.root).as_posix(): path.read_bytes()
            for path in self.fixture.root.rglob("*") if path.is_file()
        }
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
