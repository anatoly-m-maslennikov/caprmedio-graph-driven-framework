"""Synthetic golden checks for Draft identity markers and canonical targets."""

from __future__ import annotations

import hashlib
import json
import re
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
    replace_frontmatter_scalar,
    scan_atoms,
)
try:  # noqa: E402
    from draft_identity import parse_draft_marker
except ModuleNotFoundError:  # noqa: E402
    from atom_operations import parse_draft_marker
import atom_operations  # noqa: E402
import lifecycle_intents  # noqa: E402
from lifecycle_intents import (  # noqa: E402
    LifecycleError,
    carrier_descriptor,
    change_status_atom_action,
    create_atom_action,
    update_atom_action,
)
import test_model_driven_status_lifecycle as fixture_module  # noqa: E402

ROLE_LETTERS = {
    "Requirement": "R",
    "Method": "M",
    "Evaluation": "E",
    "Delivery": "D",
    "Plan": "P",
    "Concern": "C",
    "Operations": "O",
    "Analysis": "A",
}


class DraftMarkerFormatsGoldenTest(unittest.TestCase):
    """Only disposable Projects and frozen authority are writable here."""

    def setUp(self) -> None:
        fixture_module.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = fixture_module.ModelDrivenStatusLifecycleTest("run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def _marker_frontmatter(
        self,
        frontmatter: str,
        marker: str | None,
        *,
        status: str | None = None,
        version: int | None = None,
    ) -> str:
        result = frontmatter
        if marker is not None:
            if frontmatter_scalar(result, "atom_id") is None:
                result = f"atom_id: {marker}\n" + result
            else:
                result = replace_frontmatter_scalar(result, "atom_id", marker)
        if status is not None:
            result = replace_frontmatter_scalar(result, "status", status)
        if version is not None:
            result = replace_frontmatter_scalar(result, "version", str(version))
        return result

    def _carrier(
        self,
        marker: str | None,
        *,
        role: str = "Requirement",
        status: str = "Draft",
        number: int = 8600,
        filename_marker: str | None = None,
        version: int | None = None,
        relations: str = "relations: {}",
    ) -> dict[str, str]:
        carrier = self.fixture.create_carrier(
            role, "Draft" if marker is not None else status, number=number
        )
        path = carrier["path"]
        if filename_marker is not None:
            path = path.replace(f"CA-{ROLE_LETTERS[role]}--", f"{filename_marker}--", 1)
        elif marker is not None:
            prefix = f"CA-{ROLE_LETTERS[role]}--"
            path = path.replace(prefix, f"{marker}--", 1)
        carrier["path"] = path
        frontmatter = self._marker_frontmatter(
            carrier["frontmatter"], marker, status=status, version=version
        )
        if relations != "relations: {}":
            frontmatter = frontmatter.replace("relations: {}", relations, 1)
        carrier["frontmatter"] = frontmatter
        return carrier

    def _create(self, carrier: dict[str, str]) -> dict[str, object]:
        return create_atom_action(
            self.fixture.root,
            {"carrier": carrier},
            execute=True,
            authorized=True,
        )

    def test_marker_parser_accepts_current_forms_and_rejects_old_forms(self) -> None:
        cases = (
            ("CA-R-draft", None, None),
            ("CA-R-123@4-draft", "CA-R-123", 4),
            ("CA-R-123@draft", "CA-R-123", None),
            ("CA-R-123", False, None),
            ("CA-R-123-draft", False, None),
            ("CA-R-123@4", False, None),
            ("CA-R-123@0-draft", False, None),
            ("CA-R-123@x-draft", False, None),
            ("XX-R-draft", False, None),
            ("CA-M-draft", False, None),
        )
        for value, expected_id, expected_version in cases:
            with self.subTest(value=value):
                try:
                    marker = parse_draft_marker(value, project_prefix="CA", role_letter="R")
                except ValueError:
                    marker = None
                if expected_id is False:
                    self.assertIsNone(marker)
                    continue
                self.assertIsNotNone(marker)
                assert marker is not None
                self.assertEqual(expected_id, marker.canonical_id)
                self.assertEqual(expected_version, marker.proposed_version)

    def test_marker_filename_parser_keeps_descriptors_out_of_identity(self) -> None:
        for filename, marker in (
            ("CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-term.md", "CA-M-draft"),
            ("CA-R-123@4-draft-CORE_META_MODEL-RULE--define-rule.md", "CA-R-123@4-draft"),
            ("03-CA-R-123@4-draft-CORE_META_MODEL-RULE--define-rule.md", "CA-R-123@4-draft"),
            ("CA-D-draft--simple.md", "CA-D-draft"),
        ):
            with self.subTest(filename=filename):
                self.assertEqual(marker, atom_operations._draft_marker_from_filename(filename))
        for filename in (
            "CA-R-draft-CA-M-draft--summary.md",
            "CA-R-123@x-draft-CORE_META_MODEL--summary.md",
            "CA-R-123@4-draft-CORE_META_MODEL--summary@4.md",
            "CA-R-draft-lowercase--summary.md",
        ):
            with self.subTest(filename=filename):
                with self.assertRaises(ValueError):
                    atom_operations._draft_marker_from_filename(filename)
        self.assertIsNone(atom_operations._draft_marker_from_filename("CA-R-draftish--summary.md"))

    def test_create_keeps_id_free_and_role_marker_drafts_without_canonical_allocation(self) -> None:
        self.fixture.set_journal_state("missing")
        cases = (
            (None, None),
            ("CA-R-draft", "CA-R-draft"),
        )
        id_free_result: dict[str, object] | None = None
        for ordinal, (marker, expected_id) in enumerate(cases):
            with self.subTest(marker=marker):
                carrier = self._carrier(marker, number=8600 + ordinal)
                result = self._create(carrier)
                if marker is None:
                    id_free_result = result
                observed = result["observed"]
                self.assertEqual("applied", result["outcome"])
                self.assertIsNone(observed["atom_id"])
                self.assertEqual(carrier["path"], observed["path"])
                self.assertEqual("Draft", observed["status"])
                atom = atom_from_path(self.fixture.root, self.fixture.root / observed["path"])
                self.assertIsNone(atom.atom_id)
                self.assertEqual(expected_id, frontmatter_scalar(atom.frontmatter, "atom_id"))
        assert id_free_result is not None
        promoted = change_status_atom_action(
            self.fixture.root,
            {"target": id_free_result["observed"], "status": "Active"},
            execute=True,
            authorized=True,
        )
        self.assertEqual("applied", promoted["outcome"])
        self.assertRegex(promoted["observed"]["atom_id"], r"^CA-R-[0-9]{3,}$")
        self.assertFalse(
            (self.fixture.root / ".caprmedio_caprmedio/archive/_draft_history").exists()
        )
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())

    def test_change_status_promotes_new_role_markers_without_changing_unrelated_bytes(self) -> None:
        for index, (role, letter) in enumerate((("Method", "M"), ("Requirement", "R"), ("Delivery", "D"))):
            with self.subTest(role=role):
                self.fixture.atom(role, "Archived", number=99100)
                marker = f"CA-{letter}-draft"
                carrier = self._carrier(marker, role=role, number=8610 + index,
                    filename_marker=marker + "-STATUS_FIXTURE-GENERAL")
                created = self._create(carrier)
                source = self.fixture.root / created["observed"]["path"]
                atom = atom_from_path(self.fixture.root, source)
                request = {"target": carrier_descriptor(self.fixture.root, atom), "status": "Active"}
                before = self.fixture.snapshot()
                preview = change_status_atom_action(self.fixture.root, request)
                self.assertEqual("preview", preview["outcome"])
                self.assertEqual(before, self.fixture.snapshot())
                with self.assertRaises(LifecycleError):
                    change_status_atom_action(self.fixture.root, request, execute=True, authorized=False)
                self.assertEqual(before, self.fixture.snapshot())
                promoted = change_status_atom_action(self.fixture.root, request, execute=True, authorized=True)
                self.assertEqual("applied", promoted["outcome"])
                observed = promoted["observed"]
                self.assertRegex(observed["atom_id"], rf"^CA-{letter}-[0-9]+$")
                self.assertNotEqual(f"CA-{letter}-99100", observed["atom_id"])
                self.assertEqual(int(created["observed"]["version"]) + 1, observed["version"])
                self.assertEqual("Active", observed["status"])
                self.assertFalse(source.exists())
                target = self.fixture.root / observed["path"]
                self.assertNotIn("draft", target.parts)
                self.assertEqual(source.name.replace(marker, observed["atom_id"], 1), target.name)
                current = atom_from_path(self.fixture.root, target)
                self.assertEqual(atom.content, current.content)
                def unrelated(frontmatter):
                    return re.sub(r"(?m)^(?:atom_id|status|version|updated_at):.*(?:\n|$)", "", frontmatter)
                self.assertEqual(unrelated(atom.frontmatter), unrelated(current.frontmatter))

    def test_change_status_role_marker_rejects_stale_source_and_identity_collision(self) -> None:
        created = self._create(self._carrier("CA-M-draft", role="Method", number=8620))
        source = self.fixture.root / created["observed"]["path"]
        raw = source.read_bytes()
        request = {"target": created["observed"], "status": "Active"}
        source.write_bytes(raw + b"\nChanged after preview.\n")
        stale = self.fixture.snapshot()
        with self.assertRaises(LifecycleError) as refused:
            change_status_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("stale-carrier", refused.exception.code)
        self.assertEqual(stale, self.fixture.snapshot())
        source.write_bytes(raw)
        self.fixture.atom("Method", "Active", number=99200)
        collided = self.fixture.snapshot()
        with patch.object(lifecycle_intents, "_draft_promotion_identity", return_value="CA-M-99200"):
            with self.assertRaises(LifecycleError) as collision:
                change_status_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("atom-id-collision", collision.exception.code)
        self.assertEqual(collided, self.fixture.snapshot())
        read_atom = atom_operations.atom_from_path
        def reject_published(root, path):
            if path != source:
                raise ToolError("promotion-postcondition-test", "injected postcondition failure")
            return read_atom(root, path)
        with patch.object(atom_operations, "atom_from_path", side_effect=reject_published):
            with self.assertRaises(LifecycleError) as failed:
                change_status_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("promotion-postcondition-test", failed.exception.code)
        self.assertEqual({path: value for path, value in collided.items() if value is not None},
                         {path: value for path, value in self.fixture.snapshot().items() if value is not None})


    def test_change_status_role_marker_rejects_incoherent_markers_without_effects(self) -> None:
        for index, (marker, filename_marker) in enumerate((
            ("CA-M-draft", "CA-M-draft"),
            ("XX-R-draft", "XX-R-draft"),
            ("CA-R-draft", "CA-R-123@4-draft"),
            ("CA-R-123-draft", "CA-R-123-draft"),
        )):
            with self.subTest(marker=marker, filename_marker=filename_marker):
                created = self._create(self._carrier("CA-R-draft", number=8630 + index))
                original = self.fixture.root / created["observed"]["path"]
                changed = original.with_name(original.name.replace("CA-R-draft", filename_marker, 1))
                raw = original.read_text(encoding="utf-8").replace("atom_id: CA-R-draft", f"atom_id: {marker}", 1)
                if changed != original:
                    original.unlink()
                changed.write_text(raw, encoding="utf-8")
                target = {**created["observed"], "path": changed.relative_to(self.fixture.root).as_posix(),
                          "filename": changed.name, "digest": hashlib.sha256(changed.read_bytes()).hexdigest()}
                before = self.fixture.snapshot()
                with self.assertRaises((LifecycleError, ToolError)):
                    change_status_atom_action(self.fixture.root, {"target": target, "status": "Active"},
                                              execute=True, authorized=True)
                self.assertEqual(before, self.fixture.snapshot())
                changed.unlink()

    def test_h2_current_and_edit_draft_promote_under_current_layout_authority(self) -> None:
        captured = json.loads((TOOLS / "tests/fixtures/rmed_current_layout.json").read_text(encoding="utf-8"))
        for row in captured.values():
            self.assertEqual(row["sha256"], hashlib.sha256(row["text"].encode()).hexdigest())
        fixture_layout = next((self.fixture.root / ".caprmedio_caprmedio").rglob("CA-D-479-*.md"))
        fixture_layout.write_text(captured["layout_authority"]["text"], encoding="utf-8")
        _, current_body = atom_operations.split_frontmatter(captured["current"]["text"])
        _, draft_body = atom_operations.split_frontmatter(captured["draft"]["text"])
        current = self.fixture.atom("Requirement", "Active", number=123)
        atom = atom_from_path(self.fixture.root, current)
        current.write_bytes(atom_operations.render(atom.frontmatter, current_body))
        atom = atom_from_path(self.fixture.root, current)
        marker = "CA-R-123@4-draft"
        draft_path = current.parent / "draft" / f"{marker}-STATUS_FIXTURE-RULE--golden.md"
        draft_path.parent.mkdir(exist_ok=True)
        draft_frontmatter = self._marker_frontmatter(atom.frontmatter, marker, status="Draft", version=4)
        draft_path.write_bytes(atom_operations.render(draft_frontmatter, draft_body))
        draft = atom_from_path(self.fixture.root, draft_path)
        before = self.fixture.snapshot()
        request = {
            "target": carrier_descriptor(self.fixture.root, draft), "status": "Active",
            "canonical_target": carrier_descriptor(self.fixture.root, atom), "proposed_version": 4,
        }
        preview = change_status_atom_action(self.fixture.root, request)
        self.assertEqual("preview", preview["outcome"])
        self.assertEqual(before, self.fixture.snapshot())
        promoted = change_status_atom_action(self.fixture.root, request, execute=True, authorized=True)
        self.assertEqual("applied", promoted["outcome"])
        self.assertEqual("CA-R-123", promoted["observed"]["atom_id"])
        self.assertEqual(4, promoted["observed"]["version"])
        published = atom_from_path(self.fixture.root, self.fixture.root / promoted["observed"]["path"])
        self.assertEqual(draft_body, published.content)
        self.assertFalse(draft_path.exists())


    def test_create_rejects_marker_coherence_failures_without_writes(self) -> None:
        cases = (
            {"marker": "CA-R-draft", "filename_marker": "CA-R-123@4-draft"},
            {"marker": "XX-R-draft"},
            {"marker": "CA-R-123-draft"},
            {"marker": "CA-R-123@0-draft"},
            {"marker": "CA-R-draft", "status": "Active"},
            {"marker": "CA-M-draft"},
        )
        for ordinal, parameters in enumerate(cases):
            with self.subTest(parameters=parameters):
                before = self.fixture.snapshot()
                carrier = self._carrier(number=8700 + ordinal, **parameters)
                with self.assertRaises(LifecycleError):
                    self._create(carrier)
                self.assertEqual(before, self.fixture.snapshot())

    def test_validation_keeps_canonical_relations_and_rejects_marker_targets(self) -> None:
        target = self.fixture.atom("Requirement", "Active", number=8001)
        self.assertTrue(target.is_file())
        canonical = self._carrier(
            "CA-R-draft",
            number=8801,
            relations="relations: {depends_on: [CA-R-8001]}",
        )
        result = self._create(canonical)
        observed = atom_from_path(self.fixture.root, self.fixture.root / result["observed"]["path"])
        self.assertIn("depends_on: [CA-R-8001]", observed.frontmatter)

        before = self.fixture.snapshot()
        marker_target = self._carrier(
            "CA-R-draft",
            number=8802,
            relations="relations: {depends_on: [CA-R-8001@draft]}",
        )
        with self.assertRaises(LifecycleError):
            self._create(marker_target)
        self.assertEqual(before, self.fixture.snapshot())

    def test_update_accepts_existing_marker_and_promotion_restores_same_canonical_identity(self) -> None:
        self.fixture.set_journal_state("missing")
        self.fixture.atom("Requirement", "Active", number=8001)
        current = self.fixture.atom(
            "Requirement",
            "Active",
            number=123,
            relations="relations: {depends_on: [CA-R-8001]}",
        )
        current_atom = atom_from_path(self.fixture.root, current)
        current_bytes = current.read_bytes()

        marker = "CA-R-123@4-draft"
        draft = self._carrier(marker, number=8900, version=4)
        draft["content"] = current_atom.content + "\nDraft edit evidence.\n"
        draft["frontmatter"] = self._marker_frontmatter(
            current_atom.frontmatter,
            marker,
            status="Draft",
            version=4,
        )
        draft["path"] = (
            current.parent / "draft" / f"{marker}-STATUS_FIXTURE-GENERAL--golden.md"
        ).relative_to(self.fixture.root).as_posix()
        self._create(draft)

        draft_path = self.fixture.root / draft["path"]
        draft_atom = atom_from_path(self.fixture.root, draft_path)
        self.assertIsNone(draft_atom.atom_id)
        self.assertEqual(marker, frontmatter_scalar(draft_atom.frontmatter, "atom_id"))
        update = update_atom_action(
            self.fixture.root,
            {
                "target": carrier_descriptor(self.fixture.root, draft_atom),
                "proposed": {
                    "frontmatter": draft_atom.frontmatter,
                    "content": draft_atom.content,
                },
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual("no-op", update["outcome"])
        self.assertIsNone(update["observed"]["atom_id"])

        promoted = change_status_atom_action(
            self.fixture.root,
            {
                "target": carrier_descriptor(self.fixture.root, draft_atom),
                "status": "Active",
                "canonical_target": carrier_descriptor(self.fixture.root, current_atom),
                "proposed_version": 4,
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual("applied", promoted["outcome"])
        self.assertEqual("CA-R-123", promoted["observed"]["atom_id"])
        self.assertEqual(4, promoted["observed"]["version"])
        self.assertFalse(draft_path.exists())

        observed = atom_from_path(
            self.fixture.root, self.fixture.root / promoted["observed"]["path"]
        )
        self.assertIn("CA-R-8001", observed.frontmatter)
        predecessor = promoted["history"]["prior_revision"]
        self.assertEqual(hashlib.sha256(current_bytes).hexdigest(), predecessor["digest"])
        self.assertEqual(current_bytes, self.fixture.root.joinpath(predecessor["path"]).read_bytes())
        self.assertFalse((self.fixture.root / ".caprmedio_caprmedio/_journal").exists())
        current_atoms = [
            atom
            for atom in scan_atoms(self.fixture.root)
            if atom.atom_id == "CA-R-123" and atom.lifecycle != "archived"
        ]
        self.assertEqual(1, len(current_atoms))

    def test_existing_marker_promotion_rejects_version_mismatch_and_stale_source_without_writes(self) -> None:
        current = self.fixture.atom("Requirement", "Active", number=123)
        current_atom = atom_from_path(self.fixture.root, current)
        current_bytes = current.read_bytes()
        marker = "CA-R-123@5-draft"
        draft = self._carrier(marker, number=8910, version=5)
        draft["content"] = current_atom.content
        draft["frontmatter"] = self._marker_frontmatter(
            current_atom.frontmatter,
            marker,
            status="Draft",
            version=5,
        )
        draft["path"] = (
            current.parent / "draft" / f"{marker}--golden.md"
        ).relative_to(self.fixture.root).as_posix()
        self._create(draft)
        draft_path = self.fixture.root / draft["path"]
        draft_atom = atom_from_path(self.fixture.root, draft_path)
        before = self.fixture.snapshot()
        with self.assertRaises((LifecycleError, ToolError)) as raised:
            change_status_atom_action(
                self.fixture.root,
                {
                    "target": carrier_descriptor(self.fixture.root, draft_atom),
                    "status": "Active",
                    "canonical_target": carrier_descriptor(self.fixture.root, current_atom),
                    "proposed_version": 5,
                },
                execute=True,
                authorized=True,
            )
        self.assertEqual("atom-version-invalid", raised.exception.code)
        self.assertEqual(before, self.fixture.snapshot())

        matching_marker = "CA-R-123@4-draft"
        matching_draft = self._carrier(matching_marker, number=8911, version=4)
        matching_draft["content"] = current_atom.content
        matching_draft["frontmatter"] = self._marker_frontmatter(
            current_atom.frontmatter,
            matching_marker,
            status="Draft",
            version=4,
        )
        matching_draft["path"] = (
            current.parent / "draft" / f"{matching_marker}--golden.md"
        ).relative_to(self.fixture.root).as_posix()
        self._create(matching_draft)
        canonical_pin = carrier_descriptor(self.fixture.root, current_atom)
        current.write_bytes(current_bytes + b"\nStale source mutation.\n")
        before_stale = self.fixture.snapshot()
        stale_atom = atom_from_path(
            self.fixture.root, self.fixture.root / matching_draft["path"]
        )
        with self.assertRaises(LifecycleError):
            change_status_atom_action(
                self.fixture.root,
                {
                    "target": carrier_descriptor(self.fixture.root, stale_atom),
                    "status": "Active",
                    "canonical_target": canonical_pin,
                    "proposed_version": 4,
                },
                execute=True,
                authorized=True,
            )
        self.assertEqual(before_stale, self.fixture.snapshot())


if __name__ == "__main__":
    unittest.main()
