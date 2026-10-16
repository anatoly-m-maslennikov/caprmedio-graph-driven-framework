"""Independent literal controls for finite reference and Project admission."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parents[1]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

from project_selection import bind_selection, resolve_project
from VALIDATE_ATOMS.validate_atoms_workers.authority import Obligation
from VALIDATE_ATOMS.validate_atoms_workers.check_structure_extended import ADAPTERS
from VALIDATE_ATOMS.validate_atoms_workers.check_support import Check
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    ProposedCarrierError, _FRONTIER_IDS, _GRAPH_IDS, _REGISTRY_IDS, _SUPPORT_IDS,
    source_context_from_project, validate_proposed_carrier,
)
from VALIDATE_ATOMS.validate_atoms_workers.proposed_references import (
    ProposedReferenceError, inventory_proposed_references,
)
from golden_authority import (
    frozen_authority_fixture_bytes,
    frozen_entry,
    write_frozen_authority,
)


PLAN_BODY = "# Summary\n\nIndependent Plan\n\n## Objective\n\nCheck admission.\n\n## Details\n\n### Definition of Done\n\nExact controls pass.\n"
TARGET = b"---\natom_id: CA-O-701\ncontent_role: Operations\ncurrent_scope_unit: TEST\nstatus: Active\nversion: 7\n---\n# Summary\n\nRequested target\n"


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mode, p.stat().st_mtime_ns)
            for p in root.rglob("*") if p.is_file() and not p.is_symlink()}


def authority_fixture_bytes(identifier, entry=None, *, graph=False):
    del entry
    return frozen_authority_fixture_bytes(identifier, graph=graph)


class ProposedCarrierAdmissionRegressions(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/proposed-carrier-admission"
        scratch.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=scratch, ignore_cleanup_errors=True)
        self.addCleanup(self.directory.cleanup)
        self.entry_patch = patch.object(admission, "_entry", frozen_entry)
        self.entry_patch.start()
        self.addCleanup(self.entry_patch.stop)
        self.root = Path(self.directory.name)

    def put(self, relative, raw):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def inventory(self):
        return inventory_proposed_references(
            self.root, {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}, ["CA-O-701"],
            admitted_role_folders={"Operations": "09_operations"},
            admitted_status_folders={"Operations": {"Active": "", "Archived": "archived"}},
        )

    def test_unrelated_partial_and_identityless_legacy_do_not_block_exact_target(self):
        source = self.put("authority/09_operations/requested.md", TARGET)
        self.put("authority/09_operations/unrelated.md", b"---\natom_id: CA-M-999\nversion: 1\n---\n# Legacy\n")
        self.put("authority/09_operations/archive/old.md", b"---\nversion: 2\n---\n# Historical legacy\n")
        before = snapshot(self.root)
        result = self.inventory()
        self.assertEqual(len(result.direct_targets), 1)
        actual = result.direct_targets[0]
        self.assertEqual((actual.atom_id, actual.status, actual.version, actual.path),
                         ("CA-O-701", "Active", 7, "authority/09_operations/requested.md"))
        self.assertEqual(actual.sha256, hashlib.sha256(TARGET).hexdigest())
        self.assertEqual(source.read_bytes(), TARGET)
        self.assertEqual(snapshot(self.root), before)

    def test_requested_missing_status_or_bad_version_still_refuses(self):
        for raw in (TARGET.replace(b"status: Active\n", b""),
                    TARGET.replace(b"version: 7", b"version: 0"),
                    TARGET.replace(b"version: 7", b"version: true")):
            with self.subTest(raw=raw):
                self.put("authority/09_operations/requested.md", raw)
                before = snapshot(self.root)
                with self.assertRaises(ProposedReferenceError):
                    self.inventory()
                self.assertEqual(snapshot(self.root), before)

    def test_requested_duplicate_yaml_and_unrelated_malformed_yaml_refuse(self):
        for requested, unrelated in (
            (TARGET.replace(b"status: Active", b"status: Active\nstatus: Done"), None),
            (TARGET, b"---\natom_id: [unterminated\n---\n# Malformed\n"),
        ):
            with self.subTest(requested=requested, unrelated=unrelated):
                self.put("authority/09_operations/requested.md", requested)
                if unrelated is not None:
                    self.put("authority/09_operations/unrelated.md", unrelated)
                with self.assertRaises(ProposedReferenceError):
                    self.inventory()

    def test_duplicate_current_missing_and_archived_status_targets_refuse(self):
        first = self.put("authority/09_operations/one.md", TARGET)
        second = self.put("authority/09_operations/two.md", TARGET)
        with self.assertRaisesRegex(ProposedReferenceError, "ambiguous"):
            self.inventory()
        first.unlink()
        second.unlink()
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            self.inventory()
        self.put("authority/09_operations/archived/old.md", TARGET.replace(b"status: Active", b"status: Archived"))
        with self.assertRaisesRegex(ProposedReferenceError, "inactive or archived"):
            self.inventory()

    def test_filename_does_not_supply_missing_requested_identity(self):
        self.put("authority/09_operations/CA-O-701--not-an-identity-proof.md", b"---\nversion: 7\nstatus: Active\n---\n# Legacy\n")
        with self.assertRaises(ProposedReferenceError):
            self.inventory()

    def project(self, name="amber", control_name=".caprmedio_selected", *, root=None, source_ids=()):
        root = self.root if root is None else root
        control = root / control_name
        control.mkdir(parents=True, exist_ok=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname = "{name}"\nkey = "{name}"\nrepository_slug = "{name}-repo"\n'
            f'[paths]\ncontrol_root = "{control_name}"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n', encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            'schema_version = 1\n[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\nscope_unit_label = "Layer"\n'
            'structural_level = 1\nnavigational_order_number = 0\n'
            f'authority_path = "{control_name}/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"\n'
            'delivery_path = "methodology"\n', encoding="utf-8",
        )
        (control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n', encoding="utf-8",
        )
        write_frozen_authority(
            root, control, tuple(dict.fromkeys((*_REGISTRY_IDS, *_SUPPORT_IDS, "CA-R-1539", *source_ids))),
        )
        return resolve_project(root, control_name)

    @staticmethod
    def metadata(name="amber", **changes):
        value = {"atom_id": "CA-P-701", "content_role": "Plan", "type": "Plan", "label": "Task",
                 "current_scope_unit": name, "claim_target_scope_unit": name,
                 "local_tier": "Standard", "global_tier": 2, "status": "Active",
                 "author": "Fixture Operator", "version": 1, "updated_at": "2026-10-13 15:00:00 +0400",
                 "subjects": {"governs": "Tool", "depends_on": ["Plan"]}, "relations": {}}
        value.update(changes)
        return value

    def validate_plan(self, selection, metadata=None, relative=Path("03_plan/CA-P-701--independent-plan.md")):
        with bind_selection(selection):
            context = source_context_from_project(selection.root)
            return validate_proposed_carrier(self.metadata(selection.settings["project"]["name"]) if metadata is None else metadata,
                                             PLAN_BODY, context, relative, allow_existing_relations=True)

    def test_root_and_foreign_project_names_use_real_selected_settings_not_folder_name(self):
        for name, control in (("amber", ".caprmedio_selected"), ("violet", ".caprmedio_other")):
            with self.subTest(name=name, control=control):
                root = self.root / name
                root.mkdir()
                selection = self.project(name, control, root=root)
                before = snapshot(root)
                result = self.validate_plan(selection)
                self.assertFalse(result["findings"] + result["gaps"])
                self.assertEqual(snapshot(root), before)

    def test_project_owner_adapter_accepts_only_actual_bound_identity(self):
        selection = self.project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
            for owner, accepted in (("amber", True), ("other-project", False), ("PROJECT", False)):
                with self.subTest(owner=owner):
                    check = Check(Obligation("owner.resolution", [], True, "independent test"), context.authority,
                                  dict(context.inputs))
                    ADAPTERS["owner.resolution"](self.metadata(current_scope_unit=owner), PLAN_BODY, check)
                    self.assertEqual(not check.findings and not check.gaps, accepted)

    def test_unknown_target_wrong_project_owner_and_outside_project_path_refuse(self):
        selection = self.project()
        for metadata, relative in (
            (self.metadata(claim_target_scope_unit="unknown"), Path("03_plan/CA-P-701--independent-plan.md")),
            (self.metadata(current_scope_unit="other-project"), Path("03_plan/CA-P-701--independent-plan.md")),
            (self.metadata(), Path("../03_plan/CA-P-701--outside.md")),
        ):
            with self.subTest(metadata=metadata, relative=relative):
                with self.assertRaises(ProposedCarrierError):
                    self.validate_plan(selection, metadata, relative)

    def test_selected_settings_changed_or_missing_after_resolution_refuse(self):
        selection = self.project()
        original = selection.settings_path.read_bytes()
        for raw in (original.replace(b'name = "amber"', b'name = "other"'), None):
            with self.subTest(raw=raw):
                if raw is None:
                    selection.settings_path.unlink()
                else:
                    selection.settings_path.write_bytes(raw)
                with self.assertRaises((ProposedCarrierError, ValueError)):
                    self.validate_plan(selection)
                selection.settings_path.write_bytes(original)

    def test_bound_selection_from_foreign_root_cannot_supply_project_identity(self):
        selection = self.project()
        foreign = self.root / "foreign"
        foreign.mkdir()
        with bind_selection(selection), self.assertRaises((ProposedCarrierError, ValueError)):
            source_context_from_project(foreign)

    def test_project_and_declared_scope_unit_name_collision_refuses(self):
        selection = self.project()
        structure = selection.structure_path.read_text()
        selection.structure_path.write_text(
            structure + '\n[[scope_units]]\nscope_unit_name = "amber"\nparent = "PROJECT"\n'
            'scope_unit_type = "Unordered"\nscope_unit_label = "Layer"\n'
            'structural_level = 1\nnavigational_order_number = 1\n'
            'authority_path = ".caprmedio_selected/unit"\ndelivery_path = "unit"\n',
            encoding="utf-8",
        )
        selection = resolve_project(self.root, selection.control_relative)
        before = snapshot(self.root)
        with self.assertRaises(ProposedCarrierError):
            self.validate_plan(selection)
        self.assertEqual(snapshot(self.root), before)

    def test_captured_context_rechecks_settings_and_structure_before_validation(self):
        selection = self.project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
        for path in (selection.settings_path, selection.structure_path):
            with self.subTest(path=path.name):
                original = path.read_bytes()
                path.write_bytes(original + b"\n# independently introduced stale bytes\n")
                with self.assertRaises((ProposedCarrierError, ValueError)):
                    validate_proposed_carrier(self.metadata(), PLAN_BODY, context,
                                             Path("03_plan/CA-P-701--independent-plan.md"))
                path.write_bytes(original)

    def test_captured_context_does_not_borrow_an_ambient_foreign_selection(self):
        selection = self.project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
        foreign = self.root / "sibling"
        foreign.mkdir()
        other = self.project("violet", ".caprmedio_foreign", root=foreign)
        before = snapshot(self.root)
        result = validate_proposed_carrier(self.metadata(), PLAN_BODY, context,
                                          Path("03_plan/CA-P-701--independent-plan.md"))
        self.assertFalse(result["findings"] + result["gaps"])
        with bind_selection(other):
            result = validate_proposed_carrier(self.metadata(), PLAN_BODY, context,
                                              Path("03_plan/CA-P-701--independent-plan.md"))
        self.assertFalse(result["findings"] + result["gaps"])
        self.assertEqual(snapshot(self.root), before)

    def test_explicit_project_plan_subtree_resolves_exact_parent_chain(self):
        selection = self.project()
        base = selection.control_relative / "03_plan"
        parent = base / "CA-P-702--parent.md"
        self.put(parent, b"---\natom_id: CA-P-702\ncontent_role: Plan\ntype: Plan\ncurrent_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nParent\n")
        self.put(base / "unrelated-legacy.md", b"---\nversion: 1\n---\n# Legacy\n")
        before = snapshot(self.root)
        result = inventory_proposed_references(
            self.root, {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}, ["CA-P-702"],
            candidate_metadata=self.metadata(relations={"is_decomposition_of": ["CA-P-702"]}),
            candidate_path=parent.with_suffix("") / "CA-P-701--child.md",
            project_authority_paths=(selection.control_relative,), project_name="amber",
            admitted_role_folders={"Plan": "03_plan"},
            admitted_status_folders={"Plan": {"Active": "", "Done": "done"}},
        )
        self.assertEqual([row.atom_id for row in result.direct_targets], ["CA-P-702"])
        self.assertEqual([row.path for row in result.plan_parent_closure], [parent.as_posix()])
        self.assertEqual(snapshot(self.root), before)

    def test_relation_bearing_caller_uses_verified_whitelist_and_graph_authority(self):
        selection = self.project()
        control = selection.control_relative
        write_frozen_authority(
            self.root, control, tuple(dict.fromkeys((*_FRONTIER_IDS, *_GRAPH_IDS))),
            graph_only_identifiers=frozenset(_GRAPH_IDS),
        )
        structure = selection.structure_path.read_text()
        selection.structure_path.write_text(
            structure + '\n[[scope_units]]\nscope_unit_name = "TEST"\nparent = "PROJECT"\n'
            'scope_unit_type = "Unordered"\nscope_unit_label = "Layer"\n'
            'structural_level = 1\nnavigational_order_number = 1\n'
            f'authority_path = "{control}/unit"\ndelivery_path = "unit"\n',
            encoding="utf-8",
        )
        selection = resolve_project(self.root, control)
        target = self.put(control / "unit/09_operations/action.md", TARGET.replace(b"version: 7", b"type: Action\nversion: 7"))
        self.put(control / "unit/evidence/09_operations/broken.md", b"---\natom_id: [unterminated\n---\n")
        self.put(control / "unit/09_operations/evidence/broken.md", b"---\natom_id: [unterminated\n---\n")
        metadata = self.metadata(atom_id="CA-E-701", content_role="Evaluation", type="QA Case", relations={"evaluation_for": ["CA-O-701"]})
        body = "# Summary\n\nEvaluate action.\n\n## Scope\n\nSelected action.\n\n## Claim\n\nVerify the action.\n\n## Details\n\nIndependent check.\n"
        before = snapshot(self.root)

        with bind_selection(selection):
            context = source_context_from_project(self.root)
            result = validate_proposed_carrier(metadata, body, context, Path("06_evaluation/CA-E-701--related.md"))

        self.assertFalse(result["findings"] + result["gaps"])
        self.assertEqual(snapshot(self.root), before)
        target.unlink()
        with self.assertRaises(ProposedCarrierError):
            validate_proposed_carrier(metadata, body, context, Path("06_evaluation/CA-E-701--related.md"))


if __name__ == "__main__":
    unittest.main()
