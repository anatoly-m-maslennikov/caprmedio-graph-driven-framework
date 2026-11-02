"""The validator consumes the same inherited Status domains as lifecycle tools."""
from contextlib import nullcontext
import hashlib
import json
import re
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import yaml

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

from authoritative_status_models import StatusModelError, StatusModelIndex, declarations_from_sources  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import authority, proposed_carrier  # noqa: E402
from VALIDATE_ATOMS.tests import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402
from project_selection import bind_selection  # noqa: E402


def source(identifier, subject, claim):
    metadata = {"atom_id": identifier, "version": 1, "status": "Active",
                "content_role": "Requirement", "subjects": {"governs": subject}}
    text = (f"---\natom_id: {identifier}\nversion: 1\nstatus: Active\ncontent_role: Requirement\n"
            f"subjects:\n  governs: {json.dumps(subject)}\n---\n## Claim\n\n{claim}\n")
    return {"metadata": metadata, "text": text, "binding": {
        "atom_id": identifier, "version": 1, "path": f"/fixtures/{identifier}.md",
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }}


BASE = source("CA-R-999001", "Entity/Continuant/Object/Atom.Status",
              "Atom.Status **must** admit (Draft, Active, Archived).")
PLAN = source("CA-R-1539", "Entity/Continuant/Object/Atom/Content Role: Plan.Status",
              "the Core Plan Status model **must** inherit the allowed values of Atom.Status "
              "and add (Backlog, Done, Canceled).")


class InheritedStatusAuthorityTests(unittest.TestCase):
    def test_plan_mapping_accepts_current_root_paths_and_legacy_leaf_paths(self):
        source = """
- Draft: **in** the owning Scope Unit's shared `03_plan/draft` area.
- Active: directly **in** its local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** the owning Scope Unit's shared `03_plan/archived` area.
"""
        expected = {"Draft": "draft", "Active": "", "Archived": "archived",
                    "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled"}
        self.assertEqual(proposed_carrier._plan_mapping(source), expected)
        self.assertEqual(proposed_carrier._plan_mapping(source.replace("03_plan/", "")), expected)

    def test_plan_mapping_rejects_traversal_absolute_and_wrong_role_paths(self):
        template = """
- Draft: **in** its `{draft}` subdirectory.
- Active: directly **in** its local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** its `archived` subdirectory.
"""
        for path in ("../draft", "/03_plan/draft", "03_plan/../draft",
                     "04_requirement/draft", "03_plan/draft/child"):
            with self.subTest(path=path), self.assertRaises(proposed_carrier.ProposedCarrierError):
                proposed_carrier._plan_mapping(template.format(draft=path))

    def inherited_fixture(self):
        fixture = fixtures.ProposedCarrierAdmissionRegressions()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        selection = fixture.project(source_ids=tuple(dict.fromkeys(
            (*proposed_carrier._FRONTIER_IDS, *proposed_carrier._GRAPH_IDS, "CA-D-378"))))
        source_path = next(fixture.root.rglob("CA-R-1539*.md"))
        before = source_path.read_text()
        updated = re.sub(r"## Claim\n.*?(?=\n## Details|\Z)",
                         "## Claim\n\n" + PLAN["text"].split("## Claim\n", 1)[1], before, flags=re.S)
        self.assertNotEqual(before, updated)
        source_path.write_text(updated, encoding="utf-8")
        for path in source_path.parent.glob("CA-R-1947*.md"):
            path.unlink()
        base_path = source_path.parent / "CA-R-999001--base-status.md"
        base_path.write_text(BASE["text"], encoding="utf-8")
        delivery = next(fixture.root.rglob("CA-D-461*.md"))
        delivery_text = delivery.read_text()
        if "- Draft:" not in delivery_text:
            delivery.write_text(delivery_text.replace(
                "- Active:", "- Draft: **in** its `draft` subdirectory.\n- Active:", 1), encoding="utf-8")
        return fixture, selection, base_path

    def test_scoped_inherited_base_drift_uses_carrier_error_boundary(self):
        fixture, selection, base_path = self.inherited_fixture()
        scope = proposed_carrier.CarrierValidationScope(fixture.root)
        with bind_selection(selection):
            scope.validate(fixture.root, fixture.metadata(), fixtures.PLAN_BODY,
                           Path("03_plan/CA-P-701--candidate.md"), allow_existing_relations=True)
        base_path.write_text(BASE["text"].replace("version: 1", "version: 2"), encoding="utf-8")
        with self.assertRaises(proposed_carrier.ProposedCarrierError) as raised:
            scope.revalidate()
        self.assertIsInstance(raised.exception.__cause__, StatusModelError)
        self.assertEqual(raised.exception.__cause__.code, "source-stale")

    def test_full_proposed_carrier_with_plan_reference_after_status_source_alignment(self):
        fixture, selection, _ = self.inherited_fixture()
        target = fixture.metadata(atom_id="CA-P-702")
        fixture.put(selection.control_relative / "03_plan/CA-P-702--target.md",
                    ("---\n" + yaml.safe_dump(target) + "---\n" + fixtures.PLAN_BODY).encode())
        metadata = fixture.metadata(relations={"blocks": ["CA-P-702"]})
        with bind_selection(selection):
            context = proposed_carrier.source_context_from_project(fixture.root)
            result = proposed_carrier.validate_proposed_carrier(metadata, fixtures.PLAN_BODY, context,
                Path("03_plan/CA-P-701--candidate.md"), reference_roles=("Plan", "Requirement", "Delivery"))
        self.assertFalse(result["findings"] + result["gaps"])
        self.assertIn("CA-P-702", result["reference_scope"]["direct_targets"])

    def test_domain_obligation_retains_both_verified_bindings(self):
        context = authority.resolve_context([BASE, PLAN])
        domain = next(row for row in context.obligations if row.code == "domain.status.plan")
        self.assertTrue(domain.supported)
        self.assertEqual({"CA-R-1539", "CA-R-999001"}, {row["atom_id"] for row in domain.authority})
        self.assertEqual(("Draft", "Active", "Archived", "Backlog", "Done", "Canceled"),
                         context.domains["domain.status.plan"])
        self.assertFalse(any(row.code == "authority.unclassified.CA-R-999001"
                             for row in context.obligations))

    def test_missing_or_unverified_base_cannot_supply_domain(self):
        stale = {**BASE, "text": BASE["text"] + "changed"}
        for sources in ([PLAN], [PLAN, stale], [PLAN, BASE, stale]):
            context = authority.resolve_context(sources)
            domain = next(row for row in context.obligations if row.code == "domain.status.plan")
            self.assertFalse(domain.supported)

    def test_frontier_uses_inherited_values_and_checks_delivery_mapping(self):
        sources = {"CA-R-1539": PLAN}
        for role, identifier in proposed_carrier._FRONTIER_STATUS_IDS.items():
            if role != "Plan":
                sources[identifier] = source(identifier, f"Atom/Content Role: {role}.Status",
                    f"the Core {role} Status **must** be exactly (Draft, Active, Archived).")
        for identifier in proposed_carrier._FRONTIER_IDS:
            sources.setdefault(identifier, source(identifier, "Carrier", "Carrier rule."))
        declarations = declarations_from_sources([BASE, *sources.values()])
        index = StatusModelIndex(Path("/fixtures"), Path("/fixtures"), {}, tuple(declarations))
        context = SimpleNamespace(root=Path("/fixtures"), _selection=None, _reader=None)
        mapping = {"Draft": "draft", "Active": "", "Archived": "archived",
                   "Backlog": "001_backlog", "Done": "done", "Canceled": "canceled"}
        with patch.object(proposed_carrier, "bind_selection", return_value=nullcontext()), \
             patch.object(proposed_carrier, "_source", side_effect=lambda root, identifier, *a, **kw: sources[identifier]):
            result = proposed_carrier._frontier_status_folders(context, mapping, index)
            self.assertEqual(mapping, result["Plan"])
            with self.assertRaisesRegex(proposed_carrier.ProposedCarrierError, "incomplete"):
                proposed_carrier._frontier_status_folders(context,
                    {key: value for key, value in mapping.items() if key != "Draft"}, index)


if __name__ == "__main__":
    unittest.main()
