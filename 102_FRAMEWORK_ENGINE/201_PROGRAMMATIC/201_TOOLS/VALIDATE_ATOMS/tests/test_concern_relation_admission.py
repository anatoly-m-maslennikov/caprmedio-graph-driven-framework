"""Frozen mechanical admission for Concern concern_about targets."""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from typing import Any


HERE = Path(__file__).resolve().parent
TOOL = HERE.parent
sys.path.insert(0, str(TOOL))
sys.path.insert(0, str(HERE))

from authoritative_status_models import (  # noqa: E402
    StatusModelIndex,
    declarations_from_sources,
)
from validate_atoms_workers.authority import AuthorityContext, Obligation, resolve_context  # noqa: E402
from validate_atoms_workers.check_graph_extended import relations_resolution  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.check_schema_extended import TYPE_CONTRIBUTIONS  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from validate_atoms_workers.proposed_references import (  # noqa: E402
    ProposedReferenceError,
    inventory_proposed_references,
)
from golden_authority import frozen_source  # noqa: E402


CURRENT = HERE / "fixtures" / "current_graph_authority"
PINS = {
    "CA-D-268": (18, "eb33ffdb1ae992b8db8ea50dbb332ab3fd91b90040096c5be4965d89afc96888"),
    "CA-R-1022": (17, "1db2ca7916410f89d2cfda9c5defd8c641257c4585ca89233b4361da02586207"),
}


def current_source(atom_id: str) -> dict[str, Any]:
    version, digest = PINS[atom_id]
    path = CURRENT / f"{atom_id}.md"
    raw = path.read_bytes()
    parsed = parse_carrier(raw, path)
    if hashlib.sha256(raw).hexdigest() != digest or parsed.metadata.get("version") != version:
        raise AssertionError("current graph fixture changed: " + atom_id)
    return {
        "binding": {
            "atom_id": atom_id, "version": version, "path": str(path), "sha256": digest,
        },
        "text": parsed.text,
        "metadata": parsed.metadata,
    }


def current_authorities() -> list[dict[str, Any]]:
    schema_ids = ("CA-D-276", "CA-R-1700", *TYPE_CONTRIBUTIONS)
    return [current_source(atom_id) for atom_id in PINS] + [
        frozen_source(atom_id) for atom_id in ("CA-R-1283", "CA-D-378", *schema_ids)
    ]


def status_index() -> StatusModelIndex:
    roles = ("Concern", "Analysis", "Plan", "Requirement", "Method", "Evaluation", "Delivery", "Implementation", "Operations")
    extras = {"Concern": "Resolved, Canceled", "Analysis": "Done", "Plan": "Backlog, Done, Canceled"}
    def source(identifier: str, governs: str, claim: str) -> dict[str, Any]:
        text = (f"---\natom_id: {identifier}\nversion: 1\nstatus: Active\ncontent_role: Requirement\n"
                f"subjects:\n  governs: \"{governs}\"\n---\n{claim}\n")
        return {"binding": {"atom_id": identifier, "version": 1, "path": "/fixtures/" + identifier + ".md", "sha256": hashlib.sha256(text.encode()).hexdigest()}, "text": text}
    base = source("CA-R-1947", "Entity/Node/Continuant/Atom.Status", "Atom.Status **must** admit (Draft, Active, Archived).")
    rows = [base]
    for role in roles:
        added = extras.get(role, "Reviewed")
        rows.append(source("CA-R-" + role[:3], "Atom/Content Role: " + role + ".Status", "the Core " + role + " Status model **must** inherit the allowed values of Atom.Status and add (" + added + ")."))
    return StatusModelIndex(Path("/fixtures"), Path("/fixtures"), {}, tuple(declarations_from_sources(rows)))


STATUS_INDEX = status_index()
ROLE_DOMAIN = resolve_context([frozen_source("CA-R-1283")]).domains["domain.content_role"]
ROLE_TYPES = {
    "Concern": "Question", "Analysis": "Analysis Report", "Plan": "Plan",
    "Requirement": "Goal", "Method": "Implementation Method", "Evaluation": "QA Case",
    "Delivery": "Release Definition", "Operations": "Action",
}
PLAN_STATUS_FOLDERS = {
    "Active": "", "Draft": "draft", "Done": "done", "Canceled": "canceled", "Archived": "archived",
}


def atom(atom_id: str = "X-R-1", role: str = "Requirement", **extra: Any) -> dict[str, Any]:
    return {
        "atom_id": atom_id,
        "version": 1,
        "content_role": role,
        "type": ROLE_TYPES.get(role, role),
        "status": "Active",
        "current_scope_unit": "EXAMPLE",
        **extra,
    }


def reference(metadata: dict[str, Any], path: str = "/inventory/target.md") -> dict[str, Any]:
    return {"metadata": metadata, "path": Path(path)}


def inventory_target(status: str):
    root = Path(tempfile.mkdtemp(prefix="concern-target-"))
    path = root / "authority" / "03_plan" / PLAN_STATUS_FOLDERS[status] / f"{status.lower()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\natom_id: CA-P-1\ncontent_role: Plan\ntype: Plan\n"
        f"current_scope_unit: TEST\nstatus: {status}\nversion: 1\n---\n", encoding="utf-8",
    )
    try:
        return inventory_proposed_references(
            root, {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}, ["CA-P-1"],
            admitted_role_folders={"Plan": "03_plan"}, admitted_status_folders={"Plan": PLAN_STATUS_FOLDERS},
            current_target_ids=["CA-P-1"],
        )
    finally:
        shutil.rmtree(root)


def check(
    metadata: dict[str, Any], references: list[dict[str, Any]], extra_sources: list[dict[str, Any]] | None = None,
) -> Check:
    sources = [*current_authorities(), *(extra_sources or [])]
    item = Check(
        Obligation("relations.resolution", [], True, "current R1022 fixture"),
        AuthorityContext([], 0, 0, 0, [], (), {"domain.content_role": ROLE_DOMAIN}, False),
        {
            "sources": sources,
            "references": references,
            "reference_complete": True,
            "status_root": Path("/fixtures"),
            "status_index": STATUS_INDEX,
            "path": Path("/inventory/concern.md"),
        },
    )
    relations_resolution(metadata, "", item)
    return item


def unresolved_type_source() -> dict[str, Any]:
    text = "---\natom_id: CA-R-EXT\nversion: 1\nstatus: Active\ncontent_role: Requirement\nsubjects:\n  governs: 'Atom/Content Role: Requirement/Type: Revision'\n---\n"
    return {"binding": {"atom_id": "CA-R-EXT", "version": 1, "path": "/fixtures/CA-R-EXT.md", "sha256": hashlib.sha256(text.encode()).hexdigest()}, "text": text, "metadata": parse_carrier(text.encode(), Path("/fixtures/CA-R-EXT.md")).metadata}


class ConcernRelationAdmissionTests(unittest.TestCase):
    def test_any_carried_content_role_is_admitted_after_resolution(self) -> None:
        for role in ROLE_TYPES:
            with self.subTest(role=role):
                target = atom("X-" + role[:1] + "-2", role)
                result = check(
                    atom("X-C-1", "Concern", relations={"concern_about": [target["atom_id"]]}),
                    [reference(target)],
                )
                self.assertFalse(result.findings + result.gaps)

        unsupported = check(
            atom("X-C-1", "Concern", relations={"concern_about": ["X-I-2"]}),
            [reference(atom("X-I-2", "Implementation"))],
        )
        self.assertTrue(unsupported.gaps)

    def test_current_non_active_statuses_are_admitted(self) -> None:
        for role, status in (("Plan", "Done"), ("Plan", "Canceled"), ("Concern", "Resolved"), ("Method", "Reviewed")):
            with self.subTest(role=role, status=status):
                target = atom("X-" + role[:1] + "-2", role, status=status)
                result = check(
                    atom("X-C-1", "Concern", relations={"concern_about": [target["atom_id"]]}),
                    [reference(target)],
                )
                self.assertFalse(result.findings + result.gaps)

    def test_draft_and_archived_targets_are_not_current(self) -> None:
        for status in ("Draft", "Archived"):
            with self.subTest(status=status):
                target = atom("X-R-2", "Requirement", status=status)
                result = check(
                    atom("X-C-1", "Concern", relations={"concern_about": [target["atom_id"]]}),
                    [reference(target)],
                )
                self.assertTrue(any("Current Status" in gap["reason"] for gap in result.gaps))

    def test_draft_marker_target_is_not_a_canonical_relation_target(self) -> None:
        target = atom("X-R-2@draft", "Requirement", status="Draft")
        result = check(
            atom("X-C-1", "Concern", relations={"concern_about": [target["atom_id"]]}),
            [reference(target)],
        )
        self.assertTrue(result.gaps)
        self.assertFalse(result.findings)

    def test_inventory_admits_current_done_and_canceled_but_not_draft_or_archived(self) -> None:
        for status in ("Done", "Canceled"):
            result = inventory_target(status)
            self.assertEqual(status, result.direct_targets[0].status)
        for status in ("Draft", "Archived"):
            with self.assertRaisesRegex(ProposedReferenceError, "inactive|missing"):
                inventory_target(status)

    def test_id_only_or_missing_role_status_is_not_a_valid_atom_target(self) -> None:
        no_role = check(
            atom("X-C-1", "Concern", relations={"concern_about": ["X-R-1"]}),
            [reference({"atom_id": "X-R-1", "version": 1, "status": "Active"})],
        )
        self.assertTrue(any("Content Role" in gap["reason"] for gap in no_role.gaps))

        no_status = check(
            atom("X-C-1", "Concern", relations={"concern_about": ["X-R-1"]}),
            [reference({"atom_id": "X-R-1", "version": 1, "content_role": "Requirement"})],
        )
        self.assertTrue(any("Status" in gap["reason"] for gap in no_status.gaps))

    def test_missing_ambiguous_bad_revision_and_projection_stay_gaps(self) -> None:
        owner = atom("X-C-1", "Concern", relations={"concern_about": ["X-R-1"]})
        self.assertTrue(check(owner, []).gaps)
        self.assertTrue(
            check(owner, [reference(atom()), reference(atom(version=2), "/inventory/other.md")]).gaps
        )
        bad_revision = atom()
        bad_revision.pop("version")
        self.assertTrue(check(owner, [reference(bad_revision)]).gaps)
        projected = atom(projection={"unexpected": "binding"})
        self.assertTrue(check(owner, [reference(projected)]).gaps)

    def test_owner_must_be_a_concern(self) -> None:
        target = atom()
        result = check(
            atom("X-P-2", "Plan", relations={"concern_about": [target["atom_id"]]}),
            [reference(target)],
        )
        self.assertTrue(any("inadmissible Content Role" in finding["reason"] for finding in result.findings))
        self.assertFalse(result.gaps)

    def test_unknown_role_invalid_status_and_identity_role_mismatch_are_gaps(self) -> None:
        unknown_role = check(
            atom("X-C-1", "Concern", relations={"concern_about": ["X-Z-2"]}),
            [reference(atom("X-Z-2", "Unknown"))],
        )
        self.assertTrue(any("unadmitted Content Role" in gap["reason"] for gap in unknown_role.gaps))

        invalid_status = check(
            atom("X-C-1", "Concern", relations={"concern_about": ["X-R-2"]}),
            [reference(atom("X-R-2", "Requirement", status="NotAStatus"))],
        )
        self.assertTrue(any("unadmitted Status" in gap["reason"] for gap in invalid_status.gaps))

        mismatched_identity = check(
            atom("X-C-1", "Concern", relations={"concern_about": ["X-C-2"]}),
            [reference(atom("X-C-2", "Requirement"))],
        )
        self.assertTrue(any("identity disagrees" in gap["reason"] for gap in mismatched_identity.gaps))

        for identity in ("!!!-R-2", "X-R-²"):
            malformed = check(
                atom("X-C-1", "Concern", relations={"concern_about": [identity]}),
                [reference(atom(identity, "Requirement"))],
            )
            self.assertTrue(any("identity disagrees" in gap["reason"] for gap in malformed.gaps))

    def test_target_type_uses_qualified_schema_authority(self) -> None:
        owner = atom("X-C-1", "Concern", relations={"concern_about": ["X-R-2"]})
        for role in ("Requirement", "Method", "Delivery"):
            target = atom("X-" + role[:1] + "-2", role)
            target.pop("type")
            result = check(
                atom("X-C-1", "Concern", relations={"concern_about": [target["atom_id"]]}),
                [reference(target)],
            )
            self.assertFalse(result.findings + result.gaps)

        invalid = check(owner, [reference(atom("X-R-2", "Requirement", type="Revision"))])
        self.assertTrue(any("Type is not admitted" in finding["reason"] for finding in invalid.findings))

        unresolved = check(
            owner,
            [reference(atom("X-R-2", "Requirement", type="Revision"))],
            [unresolved_type_source()],
        )
        self.assertTrue(any("completely resolved schema" in gap["reason"] for gap in unresolved.gaps))


if __name__ == "__main__":
    unittest.main()
