"""End-to-end admission contracts for proposed relation-bearing Atom carriers.

The fixture intentionally mirrors only the finite authority closure read by the
pre-write boundary.  It never changes the repository's Project or authority
carriers: every created target lives under the disposable ``.caprmedio_tmp``
fixture root.
"""

from __future__ import annotations

import hashlib
import os
import sys
import tempfile
import threading
import unittest
import warnings
from unittest.mock import patch
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
PROJECT = TOOLS.parents[2]
VALIDATE = TOOLS / "VALIDATE_ATOMS"
WORKERS = VALIDATE / "validate_atoms_workers"
TEST_TEMP_ROOT = PROJECT / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(VALIDATE))

from atom_operations import ToolError, prepare_create_atom_revision  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier  # noqa: E402
from validate_atoms_workers.graph_authority_refresh import (  # noqa: E402
    APPROVED_GRAPH_AUTHORITY_IDS,
)
from VALIDATE_ATOMS.tests.golden_authority import (  # noqa: E402
    frozen_authority_fixture_bytes,
    frozen_entry,
    write_frozen_authority,
)
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402


FIXTURE_SCOPE = "PARENT"
FIXTURE_AUTHORITY = (
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/"
    "201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/PARENT"
)
METHODOLOGY_AUTHORITY = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
FROZEN_AUTHORITY = f"{METHODOLOGY_AUTHORITY}/frozen-authority"
CONTROL = Path(".caprmedio_caprmedio")
REGISTERED_AUTHOR = "Anatoly Maslennikov"
PLAN_STATUS_BASE = VALIDATE / "tests" / "fixtures" / "current_graph_authority" / "CA-R-1947.md"
PLAN_STATUS_BASE_SHA256 = "ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f"


def _frozen_entry(identifier: str, *, graph: bool = False) -> dict[str, object]:
    entry = frozen_entry(identifier, graph=graph or identifier == "CA-R-1539")
    if graph:
        entry["source_path"] = f".caprmedio_caprmedio/frozen-graph-authority/{identifier}.md"
    return entry


class ProposedRelationAdmissionTest(unittest.TestCase):
    """Exercise the public create-preflight boundary against a real mini-Project."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        self.authority = self.root / FIXTURE_AUTHORITY
        self.authority.mkdir(parents=True)
        self.entry_patch = patch.object(proposed_carrier, "_entry", _frozen_entry)
        self.entry_patch.start()
        self.addCleanup(self.entry_patch.stop)
        self._write_project_context()
        self._copy_verified_authority_closure()

    def tearDown(self) -> None:
        self.doCleanups()
        self.temporary.cleanup()
        if self.root.exists():
            warnings.warn(
                f"Host denied temporary fixture cleanup; retained {self.root}",
                RuntimeWarning,
            )

    def _write_project_context(self) -> None:
        control = self.root / ".caprmedio_caprmedio"
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nkey = "CA"\nname = "caprmedio"\nrepository_slug = "fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        (control / "operators_registry.toml").write_text(
            "[[operators]]\n"
            f'name = "{REGISTERED_AUTHOR}"\n'
            'role = "project owner"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "schema_version = 1\n\n"
            "[[scope_units]]\n"
            f'scope_unit_name = "{FIXTURE_SCOPE}"\n'
            'parent = "PROJECT"\n'
            'scope_unit_type = "Ordered"\n'
            'scope_unit_label = "LAYER"\n'
            "structural_level = 1\n"
            "local_order = 1\n"
            "navigational_order_number = 1\n"
            f'authority_path = "{FIXTURE_AUTHORITY}"\n'
            'delivery_path = "102_FRAMEWORK_ENGINE"\n'
            'authority_mode = "strict"\n\n'
            '[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "LAYER"\nstructural_level = 1\n'
            'navigational_order_number = 2\n'
            f'authority_path = "{METHODOLOGY_AUTHORITY}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources"\n'
            'authority_mode = "strict"\n\n'
            '[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\n'
            'parent = "METHODOLOGY_SOURCES"\nscope_unit_type = "Unordered"\n'
            'scope_unit_label = "LAYER"\nstructural_level = 2\n'
            'navigational_order_number = 1\n'
            f'authority_path = "{FROZEN_AUTHORITY}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources/001_CORE_META_MODEL"\n'
            'authority_mode = "strict"\n',
            encoding="utf-8",
        )

    def _copy_verified_authority_closure(self) -> None:
        """Materialize the finite checked-in authority closure for this Project."""

        authority_ids = tuple(
            identifier
            for identifier in dict.fromkeys(
                (
                    *proposed_carrier._REGISTRY_IDS,
                    *proposed_carrier._SUPPORT_IDS,
                    *proposed_carrier._FRONTIER_IDS,
                )
            )
            if identifier != "CA-R-1539"
        )
        write_frozen_authority(
            self.root,
            CONTROL,
            authority_ids,
        )
        plan_status_entry = _frozen_entry("CA-R-1539")
        plan_status_path = self.root / plan_status_entry["source_path"]
        self.assertIsInstance(plan_status_entry["source_path"], str)
        plan_status_path.parent.mkdir(parents=True, exist_ok=True)
        plan_status_path.write_bytes(frozen_authority_fixture_bytes("CA-R-1539", graph=True))
        self._write_plan_status_base()
        self.assertEqual(26, len(APPROVED_GRAPH_AUTHORITY_IDS))
        self.graph_entries = {}
        for identifier in APPROVED_GRAPH_AUTHORITY_IDS:
            entry = _frozen_entry(identifier, graph=True)
            source_path = entry["source_path"]
            self.assertIsInstance(source_path, str)
            destination = self.root / source_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(frozen_authority_fixture_bytes(identifier, graph=True))
            self.graph_entries[identifier] = entry

    def _write_plan_status_base(self) -> None:
        raw = PLAN_STATUS_BASE.read_bytes()
        self.assertEqual(PLAN_STATUS_BASE_SHA256, hashlib.sha256(raw).hexdigest())
        parsed = parse_carrier(raw, PLAN_STATUS_BASE)
        self.assertEqual(("CA-R-1947", 3), (parsed.metadata["atom_id"], parsed.metadata["version"]))
        destination = self.root / FROZEN_AUTHORITY / "CA-R-1947.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)

    @property
    def _authority_relative(self) -> Path:
        return Path(FIXTURE_AUTHORITY)

    def _relative(self, *parts: str) -> str:
        return (self._authority_relative.joinpath(*parts)).as_posix()

    @staticmethod
    def _body(role: str) -> str:
        if role == "Plan":
            return (
                "# Summary\n\nFixture plan.\n\n"
                "## Objective\n\nFixture objective.\n\n"
                "## Details\n\nFixture details.\n\n"
                "### Definition of Done\n\nFixture definition.\n"
            )
        return (
            "# Summary\n\nFixture summary.\n\n"
            "## Scope\n\nFixture scope.\n\n"
            "## Claim\n\nFixture claim.\n\n"
            "## Details\n\nFixture details.\n"
        )

    @staticmethod
    def _relations_yaml(relations: dict[str, list[str]]) -> str:
        if not relations:
            return "relations: {}"
        rows = ["relations:"]
        for kind, targets in relations.items():
            rows.append(f"  {kind}:")
            rows.extend(f'    - "{target}"' for target in targets)
        return "\n".join(rows)

    def _frontmatter(
        self,
        atom_id: str,
        role: str,
        *,
        status: str = "Active",
        relations: dict[str, list[str]] | None = None,
        version: int = 1,
        extra: str = "",
    ) -> str:
        kind = 'type: "QA Case"\n' if role == "Evaluation" else 'type: "Plan"\n' if role == "Plan" else ""
        return (
            f'atom_id: "{atom_id}"\n'
            f'content_role: "{role}"\n'
            + kind
            + f'current_scope_unit: "{FIXTURE_SCOPE}"\n'
            + f'claim_target_scope_unit: "{FIXTURE_SCOPE}"\n'
            + 'local_tier: "Standard"\n'
            + "global_tier: 5\n"
            + f'author: "{REGISTERED_AUTHOR}"\n'
            + f'status: "{status}"\n'
            + f"version: {version}\n"
            + 'updated_at: "2026-10-08 12:00:00 +0400"\n'
            + "subjects:\n"
            + '  governs: "Atom/Test"\n'
            + "  depends_on: []\n"
            + self._relations_yaml(relations or {})
            + (f"\n{extra}" if extra else "")
        )

    def _target(
        self,
        atom_id: str,
        *,
        role: str = "Requirement",
        status: str = "Active",
        relations: dict[str, list[str]] | None = None,
        relative: str | None = None,
    ) -> Path:
        directory = "03_plan" if role == "Plan" else "04_requirement"
        filename = f"{atom_id}--target.md"
        path = self.root / (relative or self._relative(directory, filename))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            + self._frontmatter(atom_id, role, status=status, relations=relations)
            + "\n---\n"
            + self._body(role),
            encoding="utf-8",
        )
        return path

    def _evaluation(self, atom_id: str, targets: list[str]) -> tuple[str, str, str]:
        filename = f"{atom_id}--evaluate-target.md"
        relative = self._relative("06_evaluation", filename)
        return (
            relative,
            self._frontmatter(atom_id, "Evaluation", relations={"evaluation_for": targets}),
            self._body("Evaluation"),
        )

    def _plan(
        self, atom_id: str, parent: str | None, *, relative: str | None = None, status: str = "Active"
    ) -> tuple[str, str, str]:
        filename = f"{atom_id}--nested-plan.md"
        candidate = relative or self._relative("03_plan", filename)
        relations = {"is_decomposition_of": [parent]} if parent else {}
        return (
            candidate,
            self._frontmatter(atom_id, "Plan", status=status, relations=relations),
            self._body("Plan"),
        )

    def _prepare(self, proposal: tuple[str, str, str]) -> tuple[Path, str, str | None]:
        return prepare_create_atom_revision(self.root, *proposal)

    def _refuses(self, proposal: tuple[str, str, str]) -> None:
        path = self.root / proposal[0]
        with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
            self._prepare(proposal)
        self.assertFalse(path.exists())

    def test_standard_evaluation_requires_and_admits_one_exact_active_target(self) -> None:
        missing_relation = self._evaluation("CA-E-910001", [])
        self._refuses(missing_relation)

        self._target("CA-R-910002")
        proposal = self._evaluation("CA-E-910003", ["CA-R-910002"])
        path, frontmatter, atom_id = self._prepare(proposal)

        self.assertEqual(self.root / proposal[0], path)
        self.assertEqual("CA-E-910003", atom_id)
        self.assertIn("version: 1", frontmatter)
        self.assertIn('updated_at: "', frontmatter)
        self.assertFalse(path.exists())

    def test_direct_target_missing_inactive_and_ambiguous_refuse(self) -> None:
        self._refuses(self._evaluation("CA-E-920001", ["CA-R-920999"]))

        self._target("CA-R-920002", status="Backlog")
        self._refuses(self._evaluation("CA-E-920003", ["CA-R-920002"]))

        self._target("CA-R-920004")
        self._target(
            "CA-R-920004",
            relative=self._relative("04_requirement", "CA-R-920004--duplicate.md"),
        )
        self._refuses(self._evaluation("CA-E-920005", ["CA-R-920004"]))

    def test_nested_plan_admits_authenticated_parent_directory(self) -> None:
        parent_id = "CA-P-930001"
        parent_relative = self._relative("03_plan", f"{parent_id}--target.md")
        self._target(parent_id, role="Plan", relative=parent_relative)
        candidate = self._plan(
            "CA-P-930002",
            parent_id,
            relative=self._relative(
                "03_plan", f"{parent_id}--target", "CA-P-930002--nested-plan.md"
            ),
        )

        path, _, atom_id = self._prepare(candidate)

        self.assertEqual("CA-P-930002", atom_id)
        self.assertEqual(self.root / candidate[0], path)
        self.assertFalse(path.exists())

    def test_nested_done_plan_requires_its_admitted_status_container(self) -> None:
        parent_id = "CA-P-932001"
        parent_stem = f"{parent_id}--target"
        self._target(parent_id, role="Plan", relative=self._relative("03_plan", f"{parent_stem}.md"))

        admitted = self._plan(
            "CA-P-932002",
            parent_id,
            status="Done",
            relative=self._relative("03_plan", parent_stem, "done", "CA-P-932002--nested-plan.md"),
        )
        path, _, atom_id = self._prepare(admitted)
        self.assertEqual("CA-P-932002", atom_id)
        self.assertEqual(self.root / admitted[0], path)
        self.assertFalse(path.exists())

        self._refuses(
            self._plan(
                "CA-P-932003",
                parent_id,
                status="Done",
                relative=self._relative(
                    "03_plan", parent_stem, "001_backlog", "CA-P-932003--nested-plan.md"
                ),
            )
        )

    def test_deep_plan_without_a_declared_parent_refuses(self) -> None:
        """Only an admitted decomposition edge can authorize a nested carrier."""

        self._refuses(
            self._plan(
                "CA-P-935001",
                None,
                relative=self._relative(
                    "03_plan", "unrelated-directory", "CA-P-935001--nested-plan.md"
                ),
            )
        )

    def test_nested_plan_cycle_and_wrong_parent_placement_refuse(self) -> None:
        self._target(
            "CA-P-940001",
            role="Plan",
            relations={"is_decomposition_of": ["CA-P-940002"]},
        )
        self._target(
            "CA-P-940002",
            role="Plan",
            relations={"is_decomposition_of": ["CA-P-940001"]},
        )
        self._refuses(self._plan("CA-P-940003", "CA-P-940001"))

        parent_id = "CA-P-940004"
        self._target(parent_id, role="Plan")
        self._refuses(
            self._plan(
                "CA-P-940005",
                parent_id,
                relative=self._relative("03_plan", "not-the-parent", "CA-P-940005--nested-plan.md"),
            )
        )

    def test_current_graph_authority_and_post_read_drift(self) -> None:
        self._target("CA-R-950001")
        proposal = self._evaluation("CA-E-950002", ["CA-R-950001"])

        graph_entry = self.graph_entries["CA-R-1018"]
        graph_path = self.root / graph_entry["source_path"]
        graph_path.write_text(graph_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        path, _, atom_id = self._prepare(proposal)
        self.assertEqual("CA-E-950002", atom_id)
        self.assertFalse(path.exists())
        original_read = proposed_carrier.ReadContext.read
        authority_changed = False

        def read(reader, candidate, *args, **kwargs):
            nonlocal authority_changed
            raw = original_read(reader, candidate, *args, **kwargs)
            if Path(candidate) == graph_path and not authority_changed:
                authority_changed = True
                graph_path.write_bytes(raw + b"\nChanged graph authority after observation.\n")
            return raw

        with patch.object(proposed_carrier.ReadContext, "read", read):
            self._refuses(proposal)
        self.assertTrue(authority_changed)

    def test_changed_target_refuses(self) -> None:
        # A fresh isolated Project proves target-currentness separately.  The
        # writer uses atomic replacements of valid carriers; it neither patches
        # the resolver nor manufactures a pin.
        target = self._target("CA-R-950003")
        proposal = self._evaluation("CA-E-950004", ["CA-R-950003"])
        original = target.read_text(encoding="utf-8")
        stop = threading.Event()
        changed = threading.Event()

        def change_target() -> None:
            counter = 0
            while not stop.is_set():
                counter += 1
                replacement = target.with_suffix(".swap")
                replacement.write_text(original + f"\nrace_counter: {counter}\n", encoding="utf-8")
                os.replace(replacement, target)
                changed.set()

        writer = threading.Thread(target=change_target, daemon=True)
        writer.start()
        try:
            self.assertTrue(changed.wait(timeout=2), "fixture writer did not change the direct target")
            self._refuses(proposal)
        finally:
            stop.set()
            writer.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
