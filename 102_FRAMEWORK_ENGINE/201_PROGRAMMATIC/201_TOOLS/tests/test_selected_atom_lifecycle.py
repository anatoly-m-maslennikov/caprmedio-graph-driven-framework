from __future__ import annotations

import hashlib
import copy
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

import sys

TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
APP_TESTS = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
_VALIDATE_WORKERS = TOOLS / "VALIDATE_ATOMS" / "validate_atoms_workers"
_VALIDATE_TESTS = _VALIDATE_WORKERS.parent / "tests"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(APP_TESTS))
sys.path.insert(0, str(_VALIDATE_TESTS))
_FIXTURE_SCOPE = "LIFECYCLE_FIXTURE"
_FIXTURE_RELATIVE_PATH = "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/LIFECYCLE_FIXTURE"
_FIXTURE_AUTHORITY_PATH = f".caprmedio_caprmedio/{_FIXTURE_RELATIVE_PATH}"

from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier  # noqa: E402
from frozen_selected_workflows import (  # noqa: E402
    frozen_complete_carrier_authority,
    frozen_graph_authority,
    frozen_source_bytes,
    frozen_source_root,
)
from golden_authority import frozen_authority_fixture_bytes  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.support_authority import support_sources  # noqa: E402

REQUIREMENT_STATUS_AUTHORITY = (
    REPOSITORY
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
    / "001_CORE_META_MODEL/04_requirement"
    / "CA-R-1309-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-requirement-status-values.md"
)
DELIVERY_STATUS_AUTHORITY = (
    REPOSITORY
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
    / "001_CORE_META_MODEL/04_requirement"
    / "CA-R-1399-CORE_META_MODEL-GENERAL--register-core-delivery-status-values.md"
)
SEMANTIC_ASSESSMENT_AUTHORITIES = tuple(
    REPOSITORY
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
    / "001_CORE_META_MODEL/04_requirement"
    / name
    for name in (
        "CA-R-1875-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-analysis-status-values.md",
        "CA-R-1432-CORE_META_MODEL-GENERAL--classify-admitted-atom-changes-by-semantic-effect.md",
        "CA-R-1464-CORE_META_MODEL--keep-summary-fixed-for-atom-identity.md",
    )
)

from lifecycle_intents import (  # noqa: E402
    LifecycleError,
    carrier_descriptor,
    change_status_atom_action,
    create_atom_action,
    replace_atom_action,
    update_atom_action,
    update_assessment_seal,
)
from atom_operations import Atom, ToolError, atom_from_path, frontmatter_scalar, split_frontmatter  # noqa: E402
from authoritative_status_models import resolve_status_model  # noqa: E402


class SelectedAtomLifecycleTest(unittest.TestCase):
    """Golden single-target lifecycle cases for the CA-D-527 route payload."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.input_root = frozen_source_root(self.root / "_frozen_authority")
        self.frozen_by_id: dict[str, Path] = {}
        for path in self.input_root.rglob("*.md"):
            match = re.search(r"(?m)^atom_id:\s*[\"']?([^\s\"']+)", path.read_text(encoding="utf-8"))
            if match:
                existing = self.frozen_by_id.setdefault(match[1], path)
                self.assertEqual(
                    hashlib.sha256(existing.read_bytes()).hexdigest(),
                    hashlib.sha256(path.read_bytes()).hexdigest(),
                    f"frozen authority aliases diverge: {match[1]}",
                )
        self.requirements = (
            self.root
            / ".caprmedio_caprmedio"
            / _FIXTURE_RELATIVE_PATH
            / "04_requirement"
        )
        self.requirements.mkdir(parents=True)
        self.goal_requirements = (
            self.root
            / ".caprmedio_caprmedio"
            / "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"
            / "04_requirement"
        )
        self.goal_requirements.mkdir(parents=True)
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[project]\nkey = \"lifecycle-fixture\"\nname = \"lifecycle-fixture\"\n"
            "repository_slug = \"lifecycle-fixture\"\n"
            "[artifacts.identity]\nproject_prefix = \"CA\"\n"
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n"
            "[artifact_timestamps]\ntimezone = \"UTC\"\n", encoding="utf-8"
        )
        self._copy_complete_carrier_authority()
        self._copy_frozen_goal_admission_authority()
        self._copy_type_recovery_authority()
        for atom_id in ("CA-R-1309", "CA-R-1399", "CA-R-1875", "CA-R-1432", "CA-R-1464"):
            self._copy_frozen_atom(atom_id)
        self.target = self._atom("CA-R-100", "target", "Stable summary")
        self.successor_one = self._atom("CA-R-101", "first-successor", "First successor")
        self.successor_two = self._atom("CA-R-102", "second-successor", "Second successor")

    def _copy_type_recovery_authority(self) -> None:
        for atom_id, relative, name in (
            ("CA-R-1766", "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement", "type-identity"),
            ("CA-D-531", "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/ATOM_LIFECYCLE/07_delivery", "lifecycle-dispatch"),
        ):
            path = self.root / ".caprmedio_caprmedio" / relative / f"{atom_id}--{name}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"---\natom_id: {atom_id}\ncontent_role: {'Requirement' if atom_id == 'CA-R-1766' else 'Delivery'}\n"
                "status: Active\nversion: 1\nrelations: {}\n---\n# Summary\n\nFixture authority\n",
                encoding="utf-8",
            )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _assert_configured_timestamp(self, path: Path) -> None:
        self.assertRegex(
            path.read_text(encoding="utf-8"),
            r'(?m)^updated_at: "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+0000"$',
        )

    def _copy_complete_carrier_authority(self) -> None:
        """Mirror the finite source closure used by proposed-carrier admission."""
        for entry in {**frozen_complete_carrier_authority(), **frozen_graph_authority()}.values():
            source_path = entry["source_path"]
            destination = self.root / source_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(frozen_source_bytes(source_path, entry["sha256"]))
            self.assertEqual(entry["sha256"], hashlib.sha256(destination.read_bytes()).hexdigest())
        for relative in (
            ".caprmedio_caprmedio/project_structure.toml",
            ".caprmedio_caprmedio/operators_registry.toml",
        ):
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
        (self.root / ".caprmedio_caprmedio/operators_registry.toml").write_text(
            '[[operators]]\nname = "Anatoly Maslennikov"\n'
            'role = "project owner"\njournal_author = "anatoly-m-maslennikov"\n', encoding="utf-8",
        )
        (self.root / ".caprmedio_caprmedio/project_structure.toml").write_text(
            'schema_version = 1\n\n'
            '[[scope_units]]\nscope_unit_name = "FRAMEWORK_METHODOLOGY"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\nscope_unit_label = "METHODOLOGY"\n'
            'structural_level = 1\nnavigational_order_number = 0\n'
            'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY"\n'
            'delivery_path = "framework-product"\n\n'
            '[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            'parent = "FRAMEWORK_METHODOLOGY"\nscope_unit_type = "Unordered"\nscope_unit_label = "METHODOLOGY"\n'
            'structural_level = 2\nnavigational_order_number = 0\n'
            'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"\n'
            'delivery_path = "framework-product/sources"\n\n'
            '[[scope_units]]\nscope_unit_name = "APPLICABLE_METHODOLOGY"\n'
            'parent = "FRAMEWORK_METHODOLOGY"\nscope_unit_type = "Unordered"\nscope_unit_label = "METHODOLOGY"\n'
            'structural_level = 2\nnavigational_order_number = 1\n'
            'authority_path = ".caprmedio_caprmedio/fixture/applicable"\n'
            'delivery_path = "framework-product/applicable"\n\n'
            '[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\n'
            'parent = "METHODOLOGY_SOURCES"\nscope_unit_type = "Unordered"\nscope_unit_label = "METHODOLOGY"\n'
            'structural_level = 3\nnavigational_order_number = 0\n'
            'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"\n'
            'delivery_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"\n\n'
            '[[scope_units]]\nscope_unit_name = "PROJECT_CONFIGURATION"\n'
            'parent = "METHODOLOGY_SOURCES"\nscope_unit_type = "Ordered"\nscope_unit_label = "LAYER"\n'
            'structural_level = 3\nlocal_order = 3\nnavigational_order_number = 3\n'
            'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/003_PROJECT_CONFIGURATION"\n'
            'authority_mode = "strict"\n\n'
            '[[scope_units]]\nscope_unit_name = "ENGINE"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\nscope_unit_label = "ENGINE"\n'
            'structural_level = 1\nnavigational_order_number = 1\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"\n'
            'delivery_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"\n\n'
            '[[scope_units]]\nscope_unit_name = "PROGRAMMATIC"\n'
            'parent = "ENGINE"\nscope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\n'
            'structural_level = 2\nnavigational_order_number = 1\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"\n'
            'delivery_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"\n\n'
            '[[scope_units]]\nscope_unit_name = "MCP"\n'
            'parent = "PROGRAMMATIC"\nscope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\n'
            'structural_level = 3\nnavigational_order_number = 3\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP"\n'
            'delivery_path = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"\n\n'
            '[[scope_units]]\nscope_unit_name = "TOOLS"\n'
            'parent = "PROGRAMMATIC"\nscope_unit_type = "Unordered"\nscope_unit_label = "TOOL"\n'
            'structural_level = 3\nnavigational_order_number = 1\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"\n'
            'delivery_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"\n\n'
            f'[[scope_units]]\nscope_unit_name = "{_FIXTURE_SCOPE}"\n'
            'parent = "TOOLS"\nscope_unit_type = "Unordered"\nscope_unit_label = "TOOL"\n'
            'structural_level = 4\nnavigational_order_number = 999\n'
            f'authority_path = "{_FIXTURE_AUTHORITY_PATH}"\n'
            f'delivery_path = "{_FIXTURE_AUTHORITY_PATH}"\n',
            encoding="utf-8",
        )

    def _copy_frozen_goal_admission_authority(self) -> None:
        """Materialize the finite checked Goal-admission closure at its pinned locators."""
        for atom_id in ("CA-R-924", "CA-R-925", "CA-R-926", "CA-R-947", "CA-R-1392",
                        "CA-R-1389", "CA-R-1390", "CA-R-1391"):
            entry = support_sources()[atom_id]
            source_path, digest = entry["source_path"], entry["sha256"]
            self.assertIsInstance(source_path, str)
            self.assertIsInstance(digest, str)
            payload = frozen_authority_fixture_bytes(atom_id)
            self.assertEqual(digest, hashlib.sha256(payload).hexdigest())
            destination = self.root / source_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)

    def _copy_frozen_atom(self, atom_id: str) -> Path:
        source = self.frozen_by_id[atom_id]
        relative = source.relative_to(self.input_root)
        legacy = Path(".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources")
        if relative.is_relative_to(legacy):
            relative = Path(".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES") / relative.relative_to(legacy)
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        return destination

    def _atom(
        self,
        atom_id: str,
        slug: str,
        summary: str,
        *,
        status: str = "Active",
        version: int = 1,
        relations: str = "relations: {}",
        include_type: bool = False,
    ) -> Path:
        path = self.requirements / f"{atom_id}--{slug}.md"
        payload = (
            "---\n"
            + f"atom_id: {atom_id}\n"
            + "content_role: Requirement\n"
            + ("type: Requirement\n" if include_type else "")
            + f"current_scope_unit: {_FIXTURE_SCOPE}\n"
            + f"claim_target_scope_unit: {_FIXTURE_SCOPE}\n"
            + "local_tier: Standard\n"
            + "global_tier: 14\n"
            + "author: Anatoly Maslennikov\n"
            + f"status: {status}\n"
            + f"version: {version}\n"
            + "updated_at: \"2026-01-01 00:00:00 +0000\"\n"
            + "subjects:\n"
            + "  governs: Atom/Test\n"
            + "  depends_on: []\n"
            + f"{relations}\n"
            + "---\n"
            + "# Summary\n\n"
            + f"{summary}\n\n"
            + "## Scope\n\n"
            + "Fixture scope.\n\n"
            + "## Claim\n\n"
            + "Fixture claim.\n"
            + "\n## Details\n\n"
            + "Fixture details.\n"
        )
        path.write_text(payload, encoding="utf-8")
        return path

    def _model(self) -> dict[str, object]:
        return resolve_status_model(
            self.root, carrier_descriptor(self.root, "CA-R-100"), "Archived",
        )

    def _carrier(self, atom_id: str, slug: str, summary: str) -> dict[str, str]:
        path = self.requirements / f"{atom_id}--{slug}.md"
        return {
            "path": path.relative_to(self.root).as_posix(),
            "frontmatter": (
                f"atom_id: {atom_id}\ncontent_role: Requirement\ncurrent_scope_unit: {_FIXTURE_SCOPE}\n"
                f"claim_target_scope_unit: {_FIXTURE_SCOPE}\nlocal_tier: Standard\nglobal_tier: 14\n"
                "author: Anatoly Maslennikov\nstatus: Active\nsubjects:\n"
                "  governs: Atom/Test\n  depends_on: []\nrelations: {}"
            ),
            "content": f"# Summary\n\n{summary}\n\n## Scope\n\nFixture.\n\n## Claim\n\nFixture claim.\n\n## Details\n\nFixture details.\n",
        }

    @staticmethod
    def _proposal(path: Path, *, summary: str, body_suffix: str = "") -> dict[str, str]:
        text = path.read_text(encoding="utf-8")
        frontmatter, content = text[4:].split("\n---\n", 1)
        current_summary = content.split("# Summary\n\n", 1)[1].split("\n\n", 1)[0]
        return {
            "frontmatter": frontmatter,
            "content": content.replace(current_summary, summary, 1) + body_suffix,
        }

    def test_authorized_create_uses_a_complete_carrier_and_rejects_occupied_destination(self) -> None:
        path = self.requirements / "CA-R-103--created.md"
        carrier = self._carrier("CA-R-103", "created", "Created summary")

        result = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)

        self.assertEqual(result["operation"], "create")
        self.assertEqual(result["effects"][0]["state"], "changed")
        self.assertEqual(carrier_descriptor(self.root, "CA-R-103")["version"], 1)
        self._assert_configured_timestamp(path)
        before = path.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
        self.assertEqual(path.read_bytes(), before)

        missing_identity = dict(carrier)
        missing_identity["path"] = (self.requirements / "CA-R-104--missing-id.md").relative_to(self.root).as_posix()
        missing_identity["frontmatter"] = "content_role: Requirement\nstatus: Active"
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-required"):
            create_atom_action(self.root, {"carrier": missing_identity}, execute=True, authorized=True)
        mismatch = dict(carrier)
        mismatch["path"] = (self.requirements / "CA-R-105--mismatch.md").relative_to(self.root).as_posix()
        mismatch["frontmatter"] = "atom_id: CA-R-106\ncontent_role: Requirement\nstatus: Active"
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-mismatch"):
            create_atom_action(self.root, {"carrier": mismatch}, execute=True, authorized=True)

    def test_changed_summary_is_a_terminal_non_effect_replace_handoff(self) -> None:
        before = self.target.read_bytes()
        result = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Changed summary"),
                "change_class": "semantic_revision",
                "successors": [self._carrier("CA-R-105", "replacement", "Changed summary")],
            },
            execute=True,
            authorized=True,
        )

        self.assertEqual(result["outcome"], "replace_handoff")
        self.assertEqual(result["effects"][0]["state"], "unchanged")
        self.assertEqual(result["replace_handoff"]["predecessor"]["atom_id"], "CA-R-100")
        self.assertEqual(result["replace_handoff"]["successors"][0]["frontmatter"].splitlines()[0], "atom_id: CA-R-105")
        self.assertEqual(self.target.read_bytes(), before)

    def test_update_honors_identity_revision_class_and_true_noop(self) -> None:
        before = self.target.read_bytes()
        unproven_carrier_only = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nCarrier note.\n"),
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(unproven_carrier_only["outcome"], "unresolved")
        self.assertEqual(unproven_carrier_only["classification"]["reason"], "semantic-assessment-unverified")
        self.assertEqual(self.target.read_bytes(), before)

        lossless = self._proposal(self.target, summary="Stable summary")
        lossless["content"] += "\n"
        carrier_only = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": lossless,
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(carrier_only["observed"]["version"], 2)
        self.assertEqual(carrier_only["effects"][0]["state"], "changed")
        self.assertEqual(before, (self.root / carrier_only["history"]["prior_revision"]["path"]).read_bytes())
        self._assert_configured_timestamp(self.target)

        before_semantic = self.target.read_bytes()
        semantic = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nSemantic detail.\n"),
                "change_class": "semantic_revision",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(semantic["outcome"], "unresolved")
        self.assertEqual(semantic["classification"]["requested"], "semantic_revision")
        self.assertIn("lineage-impact review", semantic["classification"]["required"])
        self.assertEqual(self.target.read_bytes(), before_semantic)

        before = self.target.read_bytes()
        history_before = {path: path.read_bytes() for path in (self.requirements / "archive").glob("*.md")}
        noop = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary"),
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(noop["outcome"], "no-op")
        self.assertEqual(self.target.read_bytes(), before)
        self.assertEqual(history_before, {path: path.read_bytes() for path in (self.requirements / "archive").glob("*.md")})

    def test_admitted_equivalent_refinement_increments_and_preserves_exact_prior(self) -> None:
        before = self.target.read_bytes()
        prior = carrier_descriptor(self.root, "CA-R-100")
        proposal = self._proposal(self.target, summary="Stable summary", body_suffix="\nEquivalent acceptance clarification.\n")
        parameters = {"target": prior, "proposed": proposal, "change_class": "equivalent_refinement",
                      "semantic_assessment_report": self._semantic_assessment_report(proposal, change_class="equivalent_refinement")}
        preview = update_atom_action(self.root, parameters)
        self.assertEqual("preview", preview["outcome"])
        assessment = update_assessment_seal(parameters, preview["assessment_evidence"])
        result = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(prior["version"] + 1, result["observed"]["version"])
        self.assertEqual(prior["atom_id"], result["observed"]["atom_id"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
        self._assert_configured_timestamp(self.target)

    def test_identified_nonactive_current_carrier_retains_exact_history(self) -> None:
        self._copy_frozen_atom("CA-R-1539")
        current = self.requirements.parent / "03_plan/done/01-CA-P-200-TASK--completed-fixture-plan.md"
        current.parent.mkdir(parents=True)
        current.write_text(
            "---\natom_id: CA-P-200\ncontent_role: Plan\ntype: Plan\nlabel: Task\n"
            f"current_scope_unit: {_FIXTURE_SCOPE}\nclaim_target_scope_unit: {_FIXTURE_SCOPE}\n"
            "work_sequence_number: 1\nlocal_tier: Standard\nglobal_tier: 14\n"
            "author: Anatoly Maslennikov\nstatus: Done\nversion: 3\n"
            "updated_at: \"2026-01-01 00:00:00 +0000\"\nsubjects:\n"
            "  governs: Atom/Test\n  depends_on: []\nrelations: {}\n---\n"
            "# Summary\n\nCompleted fixture Plan\n\n## Objective\n\nRetain fixture evidence.\n"
            "\n## Details\n\n### Definition of Done\n\nFixture evidence is retained.\n",
            encoding="utf-8",
        )
        parsed = proposed_carrier.parse_carrier(current.read_bytes(), current)
        proposed_carrier.validate_proposed_carrier(
            parsed.metadata, parsed.body, proposed_carrier.source_context_from_project(self.root),
            current.relative_to(self.root / ".caprmedio_caprmedio"),
        )
        before = current.read_bytes()
        prior = carrier_descriptor(self.root, current.relative_to(self.root).as_posix())
        self.assertEqual("done", prior["lifecycle"])
        frontmatter, content = split_frontmatter(current.read_text(encoding="utf-8"))
        proposal = {"frontmatter": frontmatter, "content": content}
        proposal["content"] += "\n"
        result = update_atom_action(self.root, {"target": prior, "proposed": proposal, "change_class": "carrier_only"},
                                    execute=True, authorized=True)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(prior["version"] + 1, result["observed"]["version"])
        self.assertEqual(prior["status"], result["observed"]["status"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())

    def test_update_rejects_unproven_equivalent_refinement(self) -> None:
        before = self.target.read_bytes()
        result = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nUnproven refinement.\n"),
                "change_class": "equivalent_refinement",
            },
            execute=True,
            authorized=True,
        )

        self.assertEqual(result["outcome"], "unresolved")
        self.assertEqual(result["classification"]["requested"], "equivalent_refinement")
        self.assertEqual(self.target.read_bytes(), before)

    def test_update_rechecks_the_completed_assessment_comparison(self) -> None:
        proposal = self._proposal(self.target, summary="Stable summary")
        proposal["content"] += "\n"
        parameters = {
            "target": carrier_descriptor(self.root, "CA-R-100"),
            "proposed": proposal,
            "change_class": "carrier_only",
        }
        preview = update_atom_action(self.root, parameters, execute=False, authorized=True)
        evidence = preview["assessment_evidence"]
        assessment = update_assessment_seal(parameters, evidence)
        tampered = {
            **assessment,
            "comparison": {
                **assessment["comparison"],
                "target": {**assessment["comparison"]["target"], "digest": "0" * 64},
            },
        }
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "reassessment-required"):
            update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=tampered)
        self.assertEqual(self.target.read_bytes(), before)

        applied = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual(applied["outcome"], "applied")
        self.assertEqual(applied["assessment"], assessment)

    def _semantic_assessment_report(self, proposed: dict[str, str], *, change_class: str = "semantic_revision",
                                    target_descriptor: dict[str, object] | None = None,
                                    carrier_recovery: bool = False) -> dict[str, str]:
        authority_root = SEMANTIC_ASSESSMENT_AUTHORITIES[0].parent
        def pin(path: Path) -> dict[str, str]:
            return {"path": path.relative_to(self.root).as_posix(), "digest": hashlib.sha256(path.read_bytes()).hexdigest()}

        target = target_descriptor or carrier_descriptor(self.root, "CA-R-100")
        report = self.root / ".caprmedio_caprmedio/02_analysis/done/CA-A-400--semantic-update-assessment.md"
        report.parent.mkdir(parents=True, exist_ok=True)
        evidence = {
            "target": {"atom_id": target["atom_id"], "path": target["path"], "digest": target["digest"]},
            "proposal": {"frontmatter_digest": hashlib.sha256(proposed["frontmatter"].encode()).hexdigest(),
                         "content_digest": hashlib.sha256(proposed["content"].encode()).hexdigest()},
            "authorityPins": {"r1432": pin(self.root / authority_root.relative_to(REPOSITORY) / SEMANTIC_ASSESSMENT_AUTHORITIES[1].name),
                              "r1464": pin(self.root / authority_root.relative_to(REPOSITORY) / SEMANTIC_ASSESSMENT_AUTHORITIES[2].name)},
            "admittedChangeClass": "carrier_only" if carrier_recovery else change_class,
            "primaryClaimIdentityPreserved": True,
            "declaredDelta": "Clarify the same fixture Claim's acceptance detail.",
            "lineageEvidencePins": [pin(self.root / str(target["path"]))] + ([
                pin(self.root / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1766--type-identity.md"),
                pin(self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/ATOM_LIFECYCLE/07_delivery/CA-D-531--lifecycle-dispatch.md"),
            ] if carrier_recovery else []),
        }
        report.write_text(
            "---\natom_id: CA-A-400\ncontent_role: Analysis\ntype: Analysis Report\nstatus: Done\nversion: 1\n"
            "updated_at: 2026-10-06 00:00:00 +0000\nrelations: {}\n---\n# Summary\n\nSemantic update assessment\n"
            "\n## Results\n\n### Update assessment evidence\n\n```json\n"
            + json.dumps(evidence, sort_keys=True, separators=(",", ":")) + "\n```\n",
            encoding="utf-8",
        )
        return pin(report)

    def test_semantic_update_requires_and_consumes_a_bound_done_analysis_report(self) -> None:
        proposal = self._proposal(self.target, summary="Stable summary", body_suffix="\nClarified acceptance detail.\n")
        report = self._semantic_assessment_report(proposal)
        parameters = {
            "target": carrier_descriptor(self.root, "CA-R-100"), "proposed": proposal,
            "change_class": "semantic_revision", "semantic_assessment_report": report,
        }
        preview = update_atom_action(self.root, parameters, execute=False, authorized=True)
        self.assertEqual(preview["outcome"], "preview")
        evidence = preview["assessment_evidence"]
        assessment = update_assessment_seal(parameters, evidence)
        report_path = self.root / report["path"]
        report_path.write_text(report_path.read_text(encoding="utf-8") + "\ntampered\n", encoding="utf-8")
        before = self.target.read_bytes()
        stale = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual(stale["outcome"], "unresolved")
        self.assertEqual(self.target.read_bytes(), before)

        parameters["semantic_assessment_report"] = self._semantic_assessment_report(proposal)
        preview = update_atom_action(self.root, parameters, execute=False, authorized=True)
        assessment = update_assessment_seal(parameters, preview["assessment_evidence"])
        applied = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual(applied["outcome"], "applied")
        self.assertEqual(applied["observed"]["version"], 2)

    def _semantic_update_parameters(self) -> dict[str, object]:
        proposal = self._proposal(self.target, summary="Stable summary", body_suffix="\nClarified acceptance detail.\n")
        return {"target": carrier_descriptor(self.root, "CA-R-100"), "proposed": proposal,
                "change_class": "semantic_revision", "semantic_assessment_report": self._semantic_assessment_report(proposal)}

    def _unrelated_history(self) -> Path:
        history = self.requirements / "archive" / (self.successor_one.stem + "@1.md")
        history.parent.mkdir(exist_ok=True)
        history.write_bytes(self.successor_one.read_bytes())
        return history

    def test_same_id_update_postwrite_parse_failure_restores_current_and_preserves_other_history(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        unrelated = self._unrelated_history()
        historical = unrelated.read_bytes()
        def refuse_postwrite_parse(root, path):
            if path == self.target and self.target.read_bytes() != before:
                raise ToolError("injected-postwrite-parse", "post-write parse failed")
            return atom_from_path(root, path)

        with patch("lifecycle_intents.atom_from_path", side_effect=refuse_postwrite_parse):
            with self.assertRaisesRegex(LifecycleError, "injected-postwrite-parse"):
                update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(before, self.target.read_bytes())
        self.assertEqual(historical, unrelated.read_bytes())
        self.assertFalse((unrelated.parent / (self.target.stem + "@1.md")).exists())

    def test_same_id_update_postwrite_current_read_failure_restores_exact_bytes(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        original_descriptor = carrier_descriptor
        failed = False

        def refuse_postwrite_read(root, selector):
            nonlocal failed
            if isinstance(selector, Atom) and selector.path == self.target and self.target.read_bytes() != before and not failed:
                failed = True
                raise OSError("injected post-write current read failure")
            return original_descriptor(root, selector)

        with patch("lifecycle_intents.carrier_descriptor", side_effect=refuse_postwrite_read):
            with self.assertRaisesRegex(OSError, "post-write current read failure"):
                update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertTrue(failed)
        self.assertEqual(before, self.target.read_bytes())
        self.assertFalse((self.requirements / "archive" / (self.target.stem + "@1.md")).exists())

    def test_same_id_update_postwrite_history_read_failure_restores_current(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        original_descriptor = carrier_descriptor

        def refuse_history_read(root, selector):
            if isinstance(selector, Atom) and selector.path.parent.name == "archive" and self.target.read_bytes() != before:
                raise OSError("injected post-write history read failure")
            return original_descriptor(root, selector)

        with patch("lifecycle_intents.carrier_descriptor", side_effect=refuse_history_read):
            with self.assertRaisesRegex(OSError, "post-write history read failure"):
                update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(before, self.target.read_bytes())
        self.assertFalse((self.requirements / "archive" / (self.target.stem + "@1.md")).exists())

    def test_same_id_update_unverified_rollback_retains_recoverable_prior_and_original_diagnostic(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        unrelated = self._unrelated_history()
        historical = unrelated.read_bytes()
        def refuse_postwrite_parse(root, path):
            if path == self.target and self.target.read_bytes() != before:
                raise ToolError("injected-postwrite-parse", "post-write parse failed")
            return atom_from_path(root, path)

        with (patch("lifecycle_intents.atom_from_path", side_effect=refuse_postwrite_parse),
              patch("lifecycle_intents._atomic_write", side_effect=PermissionError("rollback denied"), create=True)):
            partial = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual("partial", partial["outcome"])
        self.assertEqual({"type": "ToolError", "code": "injected-postwrite-parse"}, partial["failure"]["original"])
        self.assertNotEqual(before, self.target.read_bytes())
        prior = self.requirements / "archive" / (self.target.stem + "@1.md")
        self.assertEqual(before, prior.read_bytes())
        self._assert_uncertain_update_references(partial, parameters, prior)
        self.assertEqual(historical, unrelated.read_bytes())

    def test_same_id_update_preexisting_history_collision_does_not_remove_history(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        prior = self.requirements / "archive" / (self.target.stem + "@1.md")
        prior.parent.mkdir()
        prior.write_bytes(before)
        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(before, self.target.read_bytes())
        self.assertEqual(before, prior.read_bytes())

    def test_same_id_update_publication_error_after_write_restores_current(self) -> None:
        import lifecycle_intents
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        before_mode = self.target.stat().st_mode & 0o777
        real_write = lifecycle_intents.write_atom_revision

        def write_then_fail(*args):
            real_write(*args)
            raise OSError("injected post-publication failure")

        with patch("lifecycle_intents.write_atom_revision", side_effect=write_then_fail):
            with self.assertRaisesRegex(OSError, "post-publication failure"):
                update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(before, self.target.read_bytes())
        self.assertEqual(before_mode, self.target.stat().st_mode & 0o777)
        self.assertFalse((self.requirements / "archive" / (self.target.stem + "@1.md")).exists())

    def test_same_id_update_history_cleanup_failure_retains_history_after_current_restoration(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        prior = self.requirements / "archive" / (self.target.stem + "@1.md")
        real_unlink = Path.unlink

        def refuse_postwrite_parse(root, path):
            if path == self.target and self.target.read_bytes() != before:
                raise ToolError("injected-postwrite-parse", "post-write parse failed")
            return atom_from_path(root, path)

        def refuse_history_cleanup(path, *args, **kwargs):
            if path == prior:
                self.assertEqual(before, self.target.read_bytes())
                raise PermissionError("owned history cleanup denied")
            return real_unlink(path, *args, **kwargs)

        with (patch("lifecycle_intents.atom_from_path", side_effect=refuse_postwrite_parse),
              patch.object(Path, "unlink", autospec=True, side_effect=refuse_history_cleanup)):
            partial = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual("partial", partial["outcome"])
        self._assert_uncertain_update_references(partial, parameters, prior)
        self.assertEqual(before, self.target.read_bytes())
        self.assertEqual(before, prior.read_bytes())

    def _assert_uncertain_update_references(self, partial, parameters, prior) -> None:
        current_ref = self.target.relative_to(self.root).as_posix()
        history_ref = prior.relative_to(self.root).as_posix()
        self.assertEqual("update-rollback-uncertain", partial["failure"]["code"])
        self.assertEqual(parameters["target"], partial["recovery"]["before"])
        self.assertEqual(current_ref, partial["recovery"]["current"]["path"])
        self.assertEqual("unknown", partial["recovery"]["current"]["verification"])
        self.assertFalse(partial["recovery"]["automatic_retry"])
        self.assertEqual(history_ref, partial["history"]["prior_revision"]["path"])
        # Match the existing adapter's extraction: only known changed history
        # is a canonical effect. Unknown current stays in the retained native
        # packet; it must never be relabeled as a verified changed carrier.
        changed_refs = {effect["carrier"]["path"] for effect in partial["effects"] if effect["state"] == "changed"}
        unknown_refs = {effect["carrier"]["path"] for effect in partial["effects"] if effect["state"] == "unknown"}
        self.assertEqual({history_ref}, changed_refs)
        self.assertEqual({current_ref}, unknown_refs)
        retained = json.dumps(partial, sort_keys=True)
        self.assertIn(current_ref, retained)
        self.assertIn(history_ref, retained)
        self.assertIn("injected-postwrite-parse", retained)
        self.assertNotIn("rollback denied", retained)

    def test_same_id_update_ownership_unverified_history_remains_unknown_and_untouched(self) -> None:
        parameters = self._semantic_update_parameters()
        before = self.target.read_bytes()
        prior = self.requirements / "archive" / (self.target.stem + "@1.md")
        replacement = b"fixture history altered by another owner\n"

        def alter_history_after_publication(root, path):
            if path == self.target and self.target.read_bytes() != before:
                prior.write_bytes(replacement)
                raise ToolError("injected-postwrite-parse", "post-write parse failed")
            return atom_from_path(root, path)

        with patch("lifecycle_intents.atom_from_path", side_effect=alter_history_after_publication):
            partial = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual("partial", partial["outcome"])
        self.assertEqual("verify-history-ownership", partial["failure"]["recovery"]["phase"])
        self.assertEqual("unverified", partial["history"]["prior_revision"]["ownership_verification"])
        self.assertEqual({"unknown"}, {effect["state"] for effect in partial["effects"]})
        self.assertEqual(before, self.target.read_bytes())
        self.assertEqual(replacement, prior.read_bytes())

    def _legacy_update(self, *, legacy_status: str | None = None,
                       current_summary_layout: bool = False) -> tuple[dict[str, object], bytes]:
        original = self.target.read_text(encoding="utf-8").replace("atom_id: CA-R-100\n", "").replace(
            "status: Active\n", ""
        )
        if not current_summary_layout:
            original = original.replace("# Summary\n\nStable summary", "# Stable summary")
        if legacy_status is not None:
            original = original.replace("version: 1\n", f"status: {legacy_status}\nversion: 1\n")
        self.target.write_text(original, encoding="utf-8")
        for args in (("init",), ("add", "--", self.target.relative_to(self.root).as_posix()),
                     ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                      "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-m", "legacy carrier")):
            subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, check=True)
        commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                capture_output=True, check=True, text=True).stdout.strip()
        fm, content = split_frontmatter(original)
        atom = Atom(self.target, self.target.relative_to(self.root).as_posix(), self.target.name,
                    "CA-R-100", "active", "04_requirement", fm, content)
        target = carrier_descriptor(self.root, atom)
        proposed = {"frontmatter": fm + "\natom_id: CA-R-100\nstatus: Active",
                    "content": (content if current_summary_layout
                                else content.replace("# Stable summary", "# Summary\n\nStable summary", 1))}
        return {"target": target, "proposed": proposed, "change_class": "carrier_only",
                "legacy_identity_proof": {"atom_id": "CA-R-100", "commit": commit,
                                          "path": atom.relative, "digest": target["digest"]}}, original.encode()

    def test_explicit_historical_migration_is_preview_only_until_authorized_and_preserves_bytes(self) -> None:
        parameters, before = self._legacy_update()
        with self.assertRaisesRegex(ToolError, "declare atom_id"):
            atom_from_path(self.root, self.target)
        without_proof = {k: v for k, v in parameters.items() if k != "legacy_identity_proof"}
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-required"):
            update_atom_action(self.root, without_proof, execute=True, authorized=True)
        preview = update_atom_action(self.root, parameters)
        self.assertEqual(preview["outcome"], "preview")
        self.assertEqual(self.target.read_bytes(), before)
        self.assertFalse((self.requirements / "archive").exists())
        with self.assertRaisesRegex(LifecycleError, "authorization-required"):
            update_atom_action(self.root, parameters, execute=True)
        result = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(result["observed"]["atom_id"], "CA-R-100")
        self.assertEqual(result["observed"]["version"], 2)
        self.assertEqual(atom_from_path(self.root, self.target).atom_id, "CA-R-100")
        self.assertEqual((self.root / result["history"]["prior_revision"]["path"]).read_bytes(), before)
        self.assertEqual(1, result["history"]["prior_revision"]["version"])
        self._assert_configured_timestamp(self.target)
        normalized = self.target.read_bytes()
        atom = atom_from_path(self.root, self.target)
        noop = update_atom_action(
            self.root, {"target": carrier_descriptor(self.root, atom),
                        "proposed": {"frontmatter": atom.frontmatter, "content": atom.content},
                        "change_class": "carrier_only"}, execute=True, authorized=True)
        self.assertEqual("no-op", noop["outcome"])
        self.assertEqual(2, noop["observed"]["version"])
        self.assertEqual(normalized, self.target.read_bytes())

    def test_historical_migration_accepts_current_summary_layout_without_metadata(self) -> None:
        parameters, before = self._legacy_update(current_summary_layout=True)
        preview = update_atom_action(self.root, parameters)
        self.assertEqual("preview", preview["outcome"])
        self.assertEqual(before, self.target.read_bytes())
        result = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual("CA-R-100", result["observed"]["atom_id"])
        self.assertEqual(parameters["target"]["version"] + 1, result["observed"]["version"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
        normalized = atom_from_path(self.root, self.target)
        self.assertEqual("CA-R-100", normalized.atom_id)
        self.assertIn("status: Active", normalized.frontmatter)
        self.assertEqual("Stable summary", normalized.content.split("\n", 3)[2])

    def test_historical_migration_consumes_bound_semantic_assessment_evidence(self) -> None:
        parameters, before = self._legacy_update()
        parameters["change_class"] = "semantic_revision"
        parameters["semantic_assessment_report"] = self._semantic_assessment_report(
            parameters["proposed"], target_descriptor=parameters["target"]
        )
        preview = update_atom_action(self.root, parameters)
        self.assertEqual("preview", preview["outcome"])
        self.assertEqual("semantic_revision", preview["assessment_evidence"]["admitted_change_class"])
        malformed = copy.deepcopy(parameters)
        malformed["semantic_assessment_report"]["digest"] = "0" * 64
        invalid = update_atom_action(self.root, malformed, execute=True, authorized=True)
        self.assertEqual("unresolved", invalid["outcome"])
        self.assertEqual(before, self.target.read_bytes())
        assessment = update_assessment_seal(parameters, preview["assessment_evidence"])
        report_path = self.root / parameters["semantic_assessment_report"]["path"]
        report_path.write_text(report_path.read_text(encoding="utf-8") + "\nstale\n", encoding="utf-8")
        stale = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual("unresolved", stale["outcome"])
        self.assertEqual(before, self.target.read_bytes())

        parameters["semantic_assessment_report"] = self._semantic_assessment_report(
            parameters["proposed"], target_descriptor=parameters["target"]
        )
        preview = update_atom_action(self.root, parameters)
        assessment = update_assessment_seal(parameters, preview["assessment_evidence"])
        result = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(parameters["target"]["version"] + 1, result["observed"]["version"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())

    def _goal_type_recovery_parameters(
        self,
        atom_id: str,
        *,
        legacy: bool,
        claim_scope: str = "MCP",
        source_status: str | None = None,
        ambiguous_filename: bool = False,
        remove_unretired_metadata: bool = False,
        stale_projection: bool = False,
        missing_author: bool = False,
        missing_tier: bool = False,
        proposed_author: str = "Anatoly Maslennikov",
        proposed_tier: tuple[str, int] = ("Standard", 8),
    ) -> tuple[dict[str, object], bytes, Path]:
        """Create one frozen current or R1188-style legacy Goal carrier."""
        filename = f"{atom_id}-DEFINES_GOAL_FOR-{claim_scope}--goal"
        if ambiguous_filename:
            filename += f"-DEFINES_GOAL_FOR-{claim_scope}--duplicate"
        path = self.goal_requirements / f"{filename}.md"
        source_lines = [
            "content_role: Requirement",
            "current_scope_unit: PROGRAMMATIC" if not legacy else "",
            f"claim_target_scope_unit: {claim_scope}" if not legacy else "",
            "local_tier: Standard" if not (legacy and missing_tier) else "",
            "global_tier: 8" if not (legacy and missing_tier) else "",
            "author: Anatoly Maslennikov" if not (legacy and missing_author) else "",
            f"status: {source_status or 'Active'}" if (not legacy or source_status is not None) else "",
            "version: 1",
            'updated_at: "2026-01-01 00:00:00 +0000"',
            "subjects:",
            f"  governs: {claim_scope}/Goal",
            "  depends_on: []",
            "relations: {}",
        ]
        if not legacy:
            source_lines.insert(0, f"atom_id: {atom_id}")
        else:
            source_lines.extend(("cce_version: 9", "cce_form: legacy", "llm_session_ids: [retired]"))
            if remove_unretired_metadata:
                source_lines.append("cce_untrusted: must-remain")
        source_frontmatter = "\n".join(line for line in source_lines if line)
        source_content = (
            "# Summary\n\nFrozen goal summary\n\n## Scope\n\nMCP.\n\n## Claim\n\nFrozen Goal claim.\n\n## Details\n\n"
            "Frozen goal details.\n"
            if not legacy else "# Frozen goal summary\n\nFrozen Goal claim.\n"
        )
        original = f"---\n{source_frontmatter}\n---\n{source_content}"
        path.write_text(original, encoding="utf-8")

        if legacy:
            for args in (
                ("init",),
                ("add", "--", path.relative_to(self.root).as_posix()),
                ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-m", "legacy Goal"),
            ):
                subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, check=True)
            commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"], capture_output=True,
                                    check=True, text=True).stdout.strip()
            atom = Atom(path, path.relative_to(self.root).as_posix(), path.name, atom_id,
                        "active", "04_requirement", source_frontmatter, source_content)
            target = carrier_descriptor(self.root, atom)
            proposal_frontmatter = "\n".join(
                line for line in source_frontmatter.splitlines()
                if not line.startswith(("cce_version:", "cce_form:", "llm_session_ids:"))
                and (not remove_unretired_metadata or not line.startswith("cce_untrusted:"))
            )
            additions = [
                f"atom_id: {atom_id}",
                "current_scope_unit: PROGRAMMATIC",
                f"claim_target_scope_unit: {claim_scope}",
            ]
            if missing_tier:
                additions.extend((f"local_tier: {proposed_tier[0]}", f"global_tier: {proposed_tier[1]}"))
            if missing_author:
                additions.append(f"author: {proposed_author}")
            additions.extend(("status: Active", "type: Goal"))
            proposal_frontmatter += "\n" + "\n".join(additions)
            proof: dict[str, object] = {
                "atom_id": atom_id, "commit": commit, "path": atom.relative, "digest": target["digest"],
            }
        else:
            target = carrier_descriptor(self.root, atom_id)
            proposal_frontmatter = source_frontmatter + "\ntype: Goal"
            proof = {}

        proposal = {
            "frontmatter": proposal_frontmatter,
            "content": (
                "# Summary\n\nFrozen goal summary\n\n## Scope\n\nMCP.\n\n## Claim\n\nFrozen Goal claim.\n\n## Details\n\n"
                if legacy else source_content
            ),
        }
        parameters: dict[str, object] = {
            "target": target,
            "proposed": proposal,
            "change_class": "carrier_only",
            "semantic_assessment_report": self._semantic_assessment_report(
                proposal, target_descriptor=target, carrier_recovery=True,
            ),
        }
        if legacy:
            parameters["legacy_identity_proof"] = proof
        if stale_projection:
            projection = self.root / ".caprmedio_caprmedio/_projection/project_scope_unit_graph.projection.toml"
            projection.parent.mkdir(parents=True, exist_ok=True)
            projection.write_text(
                "[[scope_units]]\nname = \"MCP\"\nunit_name = \"MCP\"\nparent = \"caprmedio\"\n"
                "authority_path = \".caprmedio_caprmedio/obsolete-mcp\"\n",
                encoding="utf-8",
            )
        return parameters, original.encode(), path

    def test_goal_type_recovery_is_bound_carrier_only_and_preserves_exact_history(self) -> None:
        for atom_id, legacy, stale_projection in (
            ("CA-R-710", False, False),
            ("CA-R-711", True, True),
        ):
            with self.subTest(atom_id=atom_id, legacy=legacy):
                parameters, before, path = self._goal_type_recovery_parameters(
                    atom_id, legacy=legacy, stale_projection=stale_projection,
                )
                preview = update_atom_action(self.root, parameters)
                evidence = preview["assessment_evidence"]
                self.assertEqual("preview", preview["outcome"])
                self.assertEqual("carrier_only", evidence["admitted_change_class"])
                self.assertEqual({"CA-R-1766", "CA-D-531"}, set(evidence["comparison"]["type_recovery"]))
                assessment = update_assessment_seal(parameters, evidence)
                result = update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
                self.assertEqual("applied", result["outcome"])
                self.assertEqual(atom_id, result["observed"]["atom_id"])
                self.assertEqual("Goal", result["observed"]["type"])
                self.assertEqual(parameters["target"]["version"] + 1, result["observed"]["version"])
                self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
                self.assertEqual(path, self.root / result["observed"]["path"])

    def _mutate_goal_recovery_case(self, kind: str, parameters: dict[str, object]) -> None:
        proposal = parameters["proposed"]
        assert isinstance(proposal, dict)
        frontmatter, content = proposal["frontmatter"], proposal["content"]
        if kind == "claim":
            proposal["content"] = content.replace("Frozen Goal claim.", "Changed Goal claim.")
        elif kind == "summary":
            proposal["content"] = content.replace("Frozen goal summary", "Changed goal summary", 1)
        elif kind == "role":
            proposal["frontmatter"] = frontmatter.replace("content_role: Requirement", "content_role: Delivery")
        elif kind == "target":
            proposal["frontmatter"] = frontmatter.replace("claim_target_scope_unit: MCP", "claim_target_scope_unit: TOOLS")
        elif kind == "owner":
            proposal["frontmatter"] = frontmatter.replace("current_scope_unit: PROGRAMMATIC", "current_scope_unit: MCP")
        elif kind == "author":
            proposal["frontmatter"] = frontmatter.replace("author: Anatoly Maslennikov", "author: Unregistered Fixture")
        elif kind == "tier":
            proposal["frontmatter"] = frontmatter.replace("global_tier: 8", "global_tier: 14")
        elif kind == "subjects":
            proposal["frontmatter"] = frontmatter.replace("governs: MCP/Goal", "governs: MCP/Requirement")
        elif kind == "relations":
            proposal["frontmatter"] = frontmatter.replace("relations: {}", "relations: {references: CA-R-999}")
        elif kind == "scope":
            proposal["content"] = content.replace("## Scope\n\nMCP.", "## Scope\n\nTOOLS.")
        elif kind == "details":
            proposal["content"] = content.replace("Frozen goal details.", "Changed goal details.")
        elif kind == "type":
            proposal["frontmatter"] = frontmatter.replace("type: Goal", "type: Requirement")
        elif kind == "stale-report":
            report = self.root / str(parameters["semantic_assessment_report"]["path"])
            report.write_text(report.read_text(encoding="utf-8") + "\nstale\n", encoding="utf-8")
        elif kind == "stale-authority":
            authority = self.root / (
                ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/"
                "001_CORE_META_MODEL/04_requirement/CA-R-1766--type-identity.md"
            )
            authority.write_text(authority.read_text(encoding="utf-8") + "\nstale\n", encoding="utf-8")
        else:
            raise AssertionError(f"unknown Goal recovery mutation: {kind}")

    def test_goal_type_recovery_refuses_non_carrier_deltas(self) -> None:
        cases = (
            ("changed-claim", False, {}, "claim"),
            ("changed-summary", False, {}, "summary"),
            ("changed-role", False, {}, "role"),
            ("changed-target", False, {}, "target"),
            ("wrong-owner", False, {}, "owner"),
            ("unregistered-author", False, {}, "author"),
            ("wrong-tier", False, {}, "tier"),
            ("changed-subjects", False, {}, "subjects"),
            ("changed-relations", False, {}, "relations"),
            ("changed-scope", False, {}, "scope"),
            ("changed-details", False, {}, "details"),
            ("ambiguous-filename", False, {"ambiguous_filename": True}, "none"),
            ("unregistered-target", False, {"claim_scope": "UNREGISTERED"}, "none"),
            ("current-type-delta", False, {}, "type"),
            ("legacy-type-delta", True, {}, "type"),
            ("legacy-inactive", True, {"source_status": "Done"}, "none"),
            ("legacy-unregistered-author", True,
             {"missing_author": True, "proposed_author": "Unregistered Fixture"}, "none"),
            ("legacy-invalid-tier", True,
             {"missing_tier": True, "proposed_tier": ("Unsupported", 99)}, "none"),
            ("legacy-unretired-metadata", True, {"remove_unretired_metadata": True}, "none"),
            ("stale-report", False, {}, "stale-report"),
            ("stale-authority", False, {}, "stale-authority"),
        )
        for index, (name, legacy, options, mutation) in enumerate(cases, start=720):
            with self.subTest(name=name):
                parameters, before, path = self._goal_type_recovery_parameters(
                    f"CA-R-{index}", legacy=legacy, **options,
                )
                if mutation != "none":
                    self._mutate_goal_recovery_case(mutation, parameters)
                try:
                    result = update_atom_action(self.root, parameters, execute=True, authorized=True)
                except LifecycleError:
                    result = None
                if result is not None:
                    self.assertNotEqual("applied", result["outcome"])
                    self.assertTrue(all(effect["state"] == "unchanged" for effect in result["effects"]))
                self.assertEqual(before, path.read_bytes())
                self.assertFalse((path.parent / "archive").exists())

    def test_historical_migration_rejects_forged_stale_or_nonhistorical_identity(self) -> None:
        parameters, before = self._legacy_update()
        for key, value in (("commit", "0" * 40), ("digest", "0" * 64), ("atom_id", "CA-R-999"),
                           ("path", "../outside.md")):
            invalid = copy.deepcopy(parameters)
            invalid["legacy_identity_proof"][key] = value
            with self.assertRaisesRegex(LifecycleError, "legacy-proof-invalid|legacy-history-unavailable"):
                update_atom_action(self.root, invalid, execute=True, authorized=True)
            self.assertEqual(self.target.read_bytes(), before)
        self.target.write_bytes(before + b"\nchanged\n")
        with self.assertRaisesRegex(LifecycleError, "legacy-proof-invalid"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)

    def test_historical_migration_does_not_choose_between_duplicate_owners(self) -> None:
        parameters, before = self._legacy_update()
        duplicate = self._atom("CA-R-100", "duplicate", "Distinct claim")
        with self.assertRaisesRegex(LifecycleError, "active-atom-id-ambiguous"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)
        duplicate.write_text(duplicate.read_text().replace("atom_id: CA-R-100\n", ""))
        with self.assertRaisesRegex(LifecycleError, "active-atom-id-ambiguous"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)

    def test_historical_migration_cannot_promote_a_draft(self) -> None:
        parameters, before = self._legacy_update(legacy_status="draft")
        with self.assertRaisesRegex(LifecycleError, "legacy-proof-inapplicable"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)

    def _explicit_legacy_r793(self) -> tuple[dict[str, object], Path, Path, bytes]:
        pinned = frozen_complete_carrier_authority().get("CAPRMEDIO-R-793")
        if pinned is not None:
            (self.root / pinned["source_path"]).unlink(missing_ok=True)
        old_id = "CAPRMEDIO-R-793"
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        structure_text = structure.read_text(encoding="utf-8")
        for scope_path, delivery in (
            (".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE", "framework-product/engine-delivery"),
            (".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
             "framework-product/programmatic-delivery"),
            (".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS",
             "framework-product/tools-delivery"),
            (_FIXTURE_AUTHORITY_PATH, "framework-product/lifecycle-fixture-delivery"),
        ):
            structure_text = structure_text.replace(f'delivery_path = "{scope_path}"',
                                                    f'delivery_path = "{delivery}"')
        structure.write_text(structure_text, encoding="utf-8")
        canonical_source = self._atom(
            "CA-R-793", "define-evaluation-approach-as-a-type-value-for-evaluation-atoms",
            "Define Evaluation Approach as a Type Value for Evaluation Atoms", version=22,
            relations="relations: {depends_on: [CA-R-1503, CA-R-1506]}",
        )
        source = self.requirements / (
            old_id + "-LIFECYCLE_FIXTURE--define-evaluation-approach-as-a-type-value-for-evaluation-atoms.md"
        )
        original = canonical_source.read_bytes().replace(
            b"atom_id: CA-R-793\n", f'atom_id: "{old_id}"\n'.encode(), 1,
        )
        source.write_bytes(original)
        canonical_source.unlink()
        destination = self.requirements / (
            "CA-R-793-LIFECYCLE_FIXTURE--define-evaluation-approach-as-a-type-value-for-evaluation-atoms.md"
        )
        subprocess.run(["git", "-C", str(self.root), "init"], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "--", source.relative_to(self.root).as_posix()],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=Fixture", "-c",
                        "user.email=fixture@example.invalid", "-c", "commit.gpgSign=false", "-c",
                        "core.hooksPath=/dev/null", "commit", "-m", "legacy R793 carrier"],
                       capture_output=True, check=True)
        commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                capture_output=True, check=True, text=True).stdout.strip()
        frontmatter, content = split_frontmatter(original.decode())
        legacy = Atom(source, source.relative_to(self.root).as_posix(), source.name,
                      old_id, "active", "04_requirement", frontmatter, content)
        target = carrier_descriptor(self.root, legacy)
        proposed = frontmatter.replace(f'atom_id: "{old_id}"', 'atom_id: "CA-R-793"')
        parameters = {
            "target": target,
            "proposed": {"frontmatter": proposed, "content": content},
            "change_class": "carrier_only",
            "legacy_identity_proof": {"atom_id": old_id, "commit": commit,
                                       "path": target["path"], "digest": target["digest"]},
            "legacy_identity_mapping": {"legacy_atom_id": old_id, "atom_id": "CA-R-793",
                                        "destination": destination.relative_to(self.root).as_posix()},
        }
        return parameters, source, destination, original

    def _mapped_delivery(self) -> tuple[dict[str, object], Path, Path, bytes]:
        role = self.requirements.parent / "07_delivery"
        role.mkdir()
        old_id = "CAPRMEDIO-FRAMEWORK-ENGINE-DELV-005"
        source = role / (old_id + "-GRAPH_UI-DELIVERY--stable-delivery.md")
        original = b"---\nversion: 8\nrelations: {}\n---\n# Stable delivery\n\nDeliver the browser locally.\n"
        source.write_bytes(original)
        for args in (("init",), ("add", "--", source.relative_to(self.root).as_posix()),
                     ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                      "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null", "commit", "-m", "legacy delivery")):
            subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, check=True)
        commit = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"],
                                capture_output=True, check=True, text=True).stdout.strip()
        fm, body = split_frontmatter(original.decode())
        old = Atom(source, source.relative_to(self.root).as_posix(), source.name, old_id,
                   "active", "07_delivery", fm, body)
        target = carrier_descriptor(self.root, old)
        destination = role / "CA-D-560-GRAPH_UI--stable-delivery.md"
        return {"target": target,
                "proposed": {"frontmatter": (
                                fm + "\natom_id: CA-D-560\ncontent_role: Delivery\n"
                                f"current_scope_unit: {_FIXTURE_SCOPE}\nclaim_target_scope_unit: {_FIXTURE_SCOPE}\n"
                                "local_tier: Standard\nglobal_tier: 14\n"
                                "author: Anatoly Maslennikov\nstatus: Active\nsubjects:\n"
                                "  governs: Atom/Test\n  depends_on: []"
                             ),
                             "content": "# Summary\n\nStable delivery\n\n## Scope\n\nFixture scope.\n"
                                        "\n## Claim\n\nDeliver the browser locally.\n"
                                        "\n## Details\n\nFixture details.\n"},
                "change_class": "carrier_only",
                "legacy_identity_proof": {"atom_id": old_id, "commit": commit, "path": old.relative, "digest": target["digest"]},
                "legacy_identity_mapping": {"legacy_atom_id": old_id, "atom_id": "CA-D-560",
                                            "destination": destination.relative_to(self.root).as_posix()}}, source, destination, original

    def test_approved_legacy_identity_encoding_preserves_exact_history_and_explicit_mapping(self) -> None:
        parameters, source, destination, before = self._mapped_delivery()
        preview = update_atom_action(self.root, parameters)
        self.assertEqual(preview["outcome"], "preview")
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(destination.exists())
        with self.assertRaisesRegex(LifecycleError, "authorization-required"):
            update_atom_action(self.root, parameters, execute=True)
        result = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(result["observed"]["atom_id"], "CA-D-560")
        self.assertEqual(result["observed"]["version"], parameters["target"]["version"] + 1)
        self.assertFalse(source.exists())
        self.assertEqual(atom_from_path(self.root, destination).atom_id, "CA-D-560")
        self.assertEqual(result["history"]["identity_mapping"], parameters["legacy_identity_mapping"])
        self.assertEqual((self.root / result["history"]["prior_revision"]["path"]).read_bytes(), before)

    def test_explicit_legacy_r793_header_maps_with_exact_history_and_ignores_noncurrent_copies(self) -> None:
        parameters, source, destination, before = self._explicit_legacy_r793()
        obsolete = self.root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement"
        ) / source.name
        projection = source.parent / "_projection" / source.name
        obsolete.parent.mkdir(parents=True, exist_ok=True)
        projection.parent.mkdir(parents=True, exist_ok=True)
        obsolete.write_bytes(before)
        projection.write_bytes(before)

        preview = update_atom_action(self.root, parameters)
        self.assertEqual("preview", preview["outcome"])
        self.assertEqual(before, source.read_bytes())
        self.assertFalse(destination.exists())

        result = update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual("CA-R-793", result["observed"]["atom_id"])
        self.assertEqual(23, result["observed"]["version"])
        self.assertFalse(source.exists())
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
        observed = atom_from_path(self.root, destination)
        self.assertEqual("CA-R-793", observed.atom_id)
        self.assertEqual("Active", frontmatter_scalar(observed.frontmatter, "status"))
        self.assertIsNone(frontmatter_scalar(observed.frontmatter, "type"))
        self.assertEqual(split_frontmatter(before.decode())[1], observed.content)
        for field in ("content_role", "current_scope_unit", "claim_target_scope_unit", "local_tier",
                      "global_tier", "author", "subjects", "relations"):
            self.assertEqual(frontmatter_scalar(split_frontmatter(before.decode())[0], field),
                             frontmatter_scalar(observed.frontmatter, field), field)

    def test_exact_legacy_identity_encoding_has_sealed_carrier_only_evidence(self) -> None:
        parameters, source, destination, before = self._explicit_legacy_r793()
        preview = update_atom_action(self.root, parameters)
        evidence = preview["assessment_evidence"]
        self.assertEqual("preview", preview["outcome"])
        self.assertEqual("carrier_only", evidence["admitted_change_class"])
        comparison = evidence["comparison"]
        self.assertEqual(parameters["legacy_identity_mapping"], comparison["identity_mapping"])
        self.assertFalse(comparison["properties"]["equal"])
        self.assertTrue(comparison["metadata_equal_except_identity"])
        self.assertEqual("identity-encoding-only", comparison["carrier_normalization"])
        self.assertTrue(comparison["summary"]["equal"])
        self.assertTrue(comparison["claim"]["equal"])
        seal = update_assessment_seal(parameters, evidence)
        sealed_preview = update_atom_action(self.root, parameters, assessment=seal)
        self.assertEqual("preview", sealed_preview["outcome"])
        self.assertEqual(seal, sealed_preview["assessment"])
        self.assertEqual(before, source.read_bytes())
        self.assertFalse(destination.exists())

    def test_legacy_identity_mapping_requires_exact_body_and_other_metadata(self) -> None:
        parameters, source, destination, before = self._explicit_legacy_r793()
        for field in ("body", "metadata"):
            with self.subTest(field=field):
                invalid = copy.deepcopy(parameters)
                if field == "body":
                    invalid["proposed"]["content"] += "\nExtra prose.\n"
                else:
                    invalid["proposed"]["frontmatter"] = invalid["proposed"]["frontmatter"].replace(
                        "author: Anatoly Maslennikov", "author: changed author")
                preview = update_atom_action(self.root, invalid)
                self.assertEqual("preview", preview["outcome"])
                self.assertIsNone(preview.get("assessment_evidence"))
                self.assertFalse(destination.exists())
                self.assertEqual(before, source.read_bytes())

    def test_legacy_identity_encoding_seal_tampering_is_refused(self) -> None:
        parameters, source, destination, before = self._explicit_legacy_r793()
        evidence = update_atom_action(self.root, parameters)["assessment_evidence"]
        seal = update_assessment_seal(parameters, evidence)
        seal["comparison"]["identity_mapping"]["atom_id"] = "CA-R-794"
        with self.assertRaisesRegex(LifecycleError, "reassessment-required"):
            update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=seal)
        self.assertEqual(before, source.read_bytes())
        self.assertFalse(destination.exists())

    def test_explicit_legacy_mapping_rejects_duplicate_current_claim(self) -> None:
        parameters, source, _destination, before = self._explicit_legacy_r793()
        duplicate = source.with_name(
            "CAPRMEDIO-R-793-PROJECT_CONFIGURATION--duplicate-current-requirement.md"
        )
        duplicate.write_bytes(before)
        with self.assertRaisesRegex(LifecycleError, "atom-identity-duplicate"):
            update_atom_action(self.root, parameters)
        self.assertEqual(before, source.read_bytes())
        self.assertEqual(before, duplicate.read_bytes())

    def test_identity_mapping_rejects_missing_proof_scope_change_summary_change_and_reserved_ids(self) -> None:
        parameters, source, destination, before = self._mapped_delivery()
        invalid = copy.deepcopy(parameters)
        del invalid["legacy_identity_proof"]
        with self.assertRaisesRegex(LifecycleError, "identity-mapping-invalid"):
            update_atom_action(self.root, invalid, execute=True, authorized=True)
        invalid = copy.deepcopy(parameters)
        invalid["legacy_identity_mapping"]["destination"] = (self.requirements / destination.name).relative_to(self.root).as_posix()
        with self.assertRaisesRegex(LifecycleError, "identity-mapping-invalid"):
            update_atom_action(self.root, invalid, execute=True, authorized=True)
        invalid = copy.deepcopy(parameters)
        invalid["proposed"]["content"] = invalid["proposed"]["content"].replace("Stable delivery", "Changed summary")
        with self.assertRaisesRegex(LifecycleError, "legacy-summary-changed"):
            update_atom_action(self.root, invalid, execute=True, authorized=True)
        archive = source.parent / "archive"
        archive.mkdir()
        (archive / "CA-D-560--reserved@1.md").write_text("legacy reserved ID", encoding="utf-8")
        with self.assertRaisesRegex(LifecycleError, "atom-id-collision"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(destination.exists())

    def test_identity_mapping_cannot_renumber_a_current_ca_identity(self) -> None:
        parameters, before = self._legacy_update()
        parameters["legacy_identity_mapping"] = {"legacy_atom_id": "CA-R-100", "atom_id": "CA-R-999",
                                                  "destination": (self.requirements / "CA-R-999--changed.md").relative_to(self.root).as_posix()}
        parameters["proposed"]["frontmatter"] = parameters["proposed"]["frontmatter"].replace("CA-R-100", "CA-R-999")
        with self.assertRaisesRegex(LifecycleError, "legacy-proof-invalid"):
            update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(self.target.read_bytes(), before)

    def test_identity_encoding_migration_rolls_back_when_source_removal_fails(self) -> None:
        parameters, source, destination, before = self._mapped_delivery()
        original_unlink = Path.unlink

        def refuse_source(path: Path, *args: object, **kwargs: object) -> None:
            if path == source:
                raise PermissionError("fixture source-removal failure")
            original_unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", refuse_source):
            with self.assertRaisesRegex(PermissionError, "source-removal failure"):
                update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(destination.exists())
        self.assertFalse((source.parent / "archive" / (source.stem + "@8.md")).exists())

    def test_replace_publishes_supplied_successors_then_archives_one_predecessor(self) -> None:
        first = self._carrier("CA-R-105", "first-replacement", "First replacement")
        second = self._carrier("CA-R-106", "second-replacement", "Second replacement")
        before = self.target.read_bytes()
        before_mode = self.target.stat().st_mode & 0o777
        result = replace_atom_action(
            self.root,
            {
                "predecessor": carrier_descriptor(self.root, "CA-R-100"),
                "successors": [first, second],
                "status_model": self._model(),
            },
            execute=True,
            authorized=True,
        )

        predecessor = result["predecessor"]
        self.assertEqual(result["outcome"], "applied")
        self.assertEqual(len(result["successors"]), 2)
        self.assertFalse(self.target.exists())
        self.assertTrue((self.root / first["path"]).exists())
        self.assertTrue((self.root / second["path"]).exists())
        archived = self.root / predecessor["path"]
        self.assertTrue(archived.exists())
        self.assertEqual(self.target.stem + "@2.md", archived.name)
        self.assertEqual(2, predecessor["version"])
        self.assertIn("status: Archived", archived.read_text(encoding="utf-8"))
        history = self.root / result["history"]["prior_revision"]["path"]
        self.assertEqual(self.target.stem + "@1.md", history.name)
        self.assertEqual(before, history.read_bytes())
        self.assertEqual(before_mode, history.stat().st_mode & 0o777)
        self.assertEqual(before_mode, archived.stat().st_mode & 0o777)
        self.assertEqual([1, 1], [row["version"] for row in result["successors"]])
        self.assertIn(result["history"]["prior_revision"], [row["carrier"] for row in result["effects"]])
        for path in (self.root / first["path"], self.root / second["path"], archived):
            self._assert_configured_timestamp(path)

    def test_replace_requires_prepared_new_successors_and_archives_only_after_all_are_active(self) -> None:
        first = self._carrier("CA-R-105", "first-replacement", "First replacement")
        second = self._carrier("CA-R-106", "second-replacement", "Second replacement")
        original_archive = __import__("lifecycle_intents").archive_atom_revision

        def verify_active_before_archive(root: Path, atom: object, frontmatter: str, content: str, **kwargs: object) -> object:
            for successor in (first, second):
                candidate = root / successor["path"]
                self.assertTrue(candidate.exists())
                self.assertIn("status: Active", candidate.read_text(encoding="utf-8"))
            return original_archive(root, atom, frontmatter, content, **kwargs)

        with patch("lifecycle_intents.archive_atom_revision", side_effect=verify_active_before_archive):
            result = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                 "successors": [first, second], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(["CA-R-105", "CA-R-106"], [row["atom_id"] for row in result["successors"]])

    def test_replace_archive_collision_preserves_history_and_created_successor(self) -> None:
        successor = self._carrier("CA-R-105", "archive-collision", "Archive collision")
        before = self.target.read_bytes()
        history = self.target.parent / "archived" / (self.target.stem + "@1.md")
        history.parent.mkdir()
        foreign = b"existing history must not be replaced\n"
        history.write_bytes(foreign)

        result = replace_atom_action(
            self.root, {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                        "successors": [successor], "status_model": self._model()},
            execute=True, authorized=True)

        self.assertEqual("partial", result["outcome"])
        self.assertEqual("destination-collision", result["unknown_remainder"][0]["code"])
        self.assertEqual(before, self.target.read_bytes())
        self.assertEqual(foreign, history.read_bytes())
        self.assertTrue((self.root / successor["path"]).exists())
        self.assertFalse(history.with_name(self.target.stem + "@2.md").exists())

    def test_replace_archive_verification_failure_restores_predecessor_without_replaying_successor(self) -> None:
        successor = self._carrier("CA-R-105", "archive-restoration", "Archive restoration")
        before = self.target.read_bytes()
        original_read = __import__("atom_operations").atom_from_path

        def refuse_archived_read(root: Path, path: Path) -> object:
            if path.name == self.target.stem + "@2.md":
                raise ToolError("injected-archive-readback", "archived current readback failed")
            return original_read(root, path)

        with patch("atom_operations.atom_from_path", side_effect=refuse_archived_read), patch(
                "lifecycle_intents.create_atom_revision", wraps=__import__("lifecycle_intents").create_atom_revision) as create:
            result = replace_atom_action(
                self.root, {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                            "successors": [successor], "status_model": self._model()},
                execute=True, authorized=True)

        self.assertEqual("partial", result["outcome"])
        self.assertEqual("injected-archive-readback", result["unknown_remainder"][0]["code"])
        self.assertEqual(1, create.call_count)
        self.assertEqual(before, self.target.read_bytes())
        self.assertTrue((self.root / successor["path"]).exists())
        self.assertFalse((self.target.parent / "archived" / (self.target.stem + "@1.md")).exists())
        self.assertFalse((self.target.parent / "archived" / (self.target.stem + "@2.md")).exists())

    def test_replace_retains_exact_crlf_predecessor_history(self) -> None:
        self.target.write_bytes(self.target.read_bytes().replace(b"\n", b"\r\n"))
        before = self.target.read_bytes()
        successor = self._carrier("CA-R-105", "crlf-replacement", "CRLF replacement")

        result = replace_atom_action(
            self.root, {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                        "successors": [successor], "status_model": self._model()},
            execute=True, authorized=True)

        self.assertEqual("applied", result["outcome"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
        self.assertEqual(2, result["predecessor"]["version"])

    def test_replace_rejects_preexisting_successor_without_archiving_predecessor(self) -> None:
        successor = self._carrier("CA-R-105", "already-present", "Already present")
        create_atom_action(self.root, {"carrier": successor}, execute=True, authorized=True)
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                 "successors": [successor], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(before, self.target.read_bytes())

    def test_replace_rejects_preexisting_successor_id_at_unused_destination(self) -> None:
        existing = self._carrier("CA-R-105", "already-present", "Already present")
        create_atom_action(self.root, {"carrier": existing}, execute=True, authorized=True)
        replacement = self._carrier("CA-R-105", "new-destination", "Different destination")
        before_predecessor = self.target.read_bytes()
        before_existing = (self.root / existing["path"]).read_bytes()
        new_destination = self.root / replacement["path"]

        with self.assertRaisesRegex(LifecycleError, "atom-id-collision"):
            replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"),
                 "successors": [replacement], "status_model": self._model()},
                execute=True,
                authorized=True,
            )

        self.assertEqual(before_predecessor, self.target.read_bytes())
        self.assertEqual(before_existing, (self.root / existing["path"]).read_bytes())
        self.assertFalse(new_destination.exists())
        self.assertFalse((self.target.parent / "archive" / "CA-R-100--target@1.md").exists())

    def test_replace_rejects_caller_model_that_contradicts_current_authority(self) -> None:
        successor = self._carrier("CA-R-105", "forged-model", "Replacement summary")
        forged = self._model()
        forged["statuses"] = ["Active", "Reviewed", "Archived"]
        before = self.target.read_bytes()

        with self.assertRaisesRegex(LifecycleError, "model-forged"):
            replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [successor],
                 "status_model": forged},
                execute=True,
                authorized=True,
            )

        self.assertEqual(before, self.target.read_bytes())
        self.assertFalse((self.root / successor["path"]).exists())

    def test_source_model_status_noop_and_archive_relation_diagnostics(self) -> None:
        self.target.write_text(
            self.target.read_text(encoding="utf-8").replace("relations: {}", "relations:\n  depends_on: [CA-R-101]"),
            encoding="utf-8",
        )
        self._atom("CA-R-104", "inbound", "Inbound", relations="relations:\n  depends_on: [CA-R-100]")
        self.assertNotIn("type:", self.target.read_text(encoding="utf-8"))

        noop = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Active"},
            execute=True,
            authorized=True,
        )
        self.assertEqual(noop["outcome"], "no-op")

        archived = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Archived"},
            execute=True,
            authorized=True,
        )
        self.assertEqual(archived["outcome"], "applied")
        self._assert_configured_timestamp(self.root / archived["observed"]["path"])
        self.assertEqual({item["direction"] for item in archived["broken_references"]}, {"inbound", "outgoing"})
        self.assertEqual(archived["repair_handoff"]["operation"], "repair_relations")
        self.assertTrue(self.successor_one.exists())

    def test_replace_reports_partial_when_successor_or_archive_publication_fails(self) -> None:
        first = self._carrier("CA-R-105", "first-partial", "First partial")
        second = self._carrier("CA-R-106", "second-partial", "Second partial")
        original_create = __import__("lifecycle_intents").create_atom_revision
        calls = 0

        def fail_second(*args: object, **kwargs: object) -> object:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise ToolError("injected-successor-failure", "second successor failed")
            return original_create(*args, **kwargs)

        with patch("lifecycle_intents.create_atom_revision", side_effect=fail_second):
            partial = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [first, second], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(partial["outcome"], "partial")
        self.assertTrue((self.root / first["path"]).exists())
        self.assertFalse((self.root / second["path"]).exists())
        self.assertTrue(self.target.exists())
        self.assertEqual(partial["unknown_remainder"][0]["phase"], "publish_successor")

        archive_failure = self._carrier("CA-R-107", "archive-partial", "Archive partial")
        with patch("lifecycle_intents.archive_atom_revision", side_effect=ToolError("injected-archive-failure", "archive failed")):
            partial_archive = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [archive_failure], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(partial_archive["outcome"], "partial")
        self.assertTrue((self.root / archive_failure["path"]).exists())
        self.assertTrue(self.target.exists())
        self.assertEqual(partial_archive["unknown_remainder"][0]["phase"], "archive_predecessor")

    def test_stale_and_multi_target_requests_stop_before_an_effect(self) -> None:
        descriptor = carrier_descriptor(self.root, "CA-R-100")
        descriptor["digest"] = hashlib.sha256(b"stale").hexdigest()
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "stale-carrier"):
            update_atom_action(
                self.root,
                {"target": descriptor, "proposed": self._proposal(self.target, summary="Stable summary"), "change_class": "carrier_only"},
                execute=True,
                authorized=True,
            )
        with self.assertRaisesRegex(LifecycleError, "one-target-required"):
            change_status_atom_action(
                self.root,
                {"target": [carrier_descriptor(self.root, "CA-R-100")], "status": "Archived"},
                execute=True,
                authorized=True,
            )
        self.assertEqual(self.target.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
