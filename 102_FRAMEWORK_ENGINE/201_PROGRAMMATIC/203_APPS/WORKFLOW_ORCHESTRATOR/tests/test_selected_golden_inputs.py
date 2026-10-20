"""Functional golden inputs for the original selected lifecycle/structure routes.

This suite proves the corpus payloads against the native domain adapters in
fresh disposable Projects.  It does not claim queue, MCP, Docker, Run, or
Journal coverage; those remain owned by their separately bounded packets.
"""
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
STRUCTURE = TOOLS / "WORKFLOW_OPERATIONS" / "PROJECT_STRUCTURE" / "project_structure.py"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from lifecycle_intents import (  # noqa: E402
    change_status_atom_action,
    create_atom_action,
    replace_atom_action,
    update_atom_action,
)
from authoritative_status_models import resolve_status_model  # noqa: E402
from frozen_selected_workflows import frozen_source_bytes  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject, ROUTE_CASES  # noqa: E402

SPEC = importlib.util.spec_from_file_location("selected_golden_project_structure", STRUCTURE)
assert SPEC and SPEC.loader
project_structure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = project_structure
SPEC.loader.exec_module(project_structure)

ROOT = APP.parents[3]


class SelectedGoldenInputsTest(unittest.TestCase):
    """One real native Action invocation per W01--W08 source-valid payload."""

    def _fixture(self, case_id: str, route: str) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-golden-inputs"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, GoldenCase(case_id, route))
        fixture.prepare()
        return FixtureLease(root), fixture

    def _invoke(self, fixture: GoldenProject) -> dict:
        parameters = fixture.native_parameters()
        route = fixture.case.route
        if route == "create_atom":
            return create_atom_action(fixture.root, parameters, execute=True, authorized=True)
        if route == "update_atom":
            return update_atom_action(fixture.root, parameters, execute=True, authorized=True)
        if route == "replace_atom":
            return replace_atom_action(fixture.root, parameters, execute=True, authorized=True)
        if route == "change_atom_status":
            return change_status_atom_action(fixture.root, parameters, execute=True, authorized=True)
        return getattr(project_structure, route)(fixture.root, parameters)

    def test_w01_w08_requests_are_native_payloads_with_real_frontiers(self) -> None:
        for case_id, route in ROUTE_CASES[:8]:
            with self.subTest(case=case_id):
                lease, fixture = self._fixture(case_id, route)
                try:
                    request = fixture.request(request_id=f"golden-{case_id.lower()}")
                    self.assertNotIn("fixture_schema", request["parameters"])
                    self.assertEqual(fixture.native_parameters(), request["parameters"])
                    frontier = request["target_frontier"]
                    self.assertIsInstance(frontier, list)
                    self.assertEqual(1, len(frontier))
                    target = fixture.root / frontier[0]
                    # Create's target is deliberately absent before its native
                    # effect; all other frontiers are current observed files.
                    self.assertTrue(target.is_file() or (route == "create_atom" and target.parent.is_dir()))
                finally:
                    lease.cleanup()

    def test_w01_w08_native_adapters_apply_actual_filesystem_effects(self) -> None:
        for case_id, route in ROUTE_CASES[:8]:
            with self.subTest(case=case_id):
                lease, fixture = self._fixture(case_id, route)
                try:
                    result = self._invoke(fixture)
                    if route.startswith(("create_atom", "update_atom", "replace_atom", "change_atom_status")):
                        self.assertEqual("applied", result["outcome"], result)
                        self.assertTrue(any(effect["state"] == "changed" for effect in result["effects"]), result)
                    else:
                        self.assertEqual("completed", result["state"], result)
                        self.assertTrue(result["actual_effects"], result)
                    if route == "create_atom":
                        self.assertTrue((fixture.root / result["observed"]["path"]).is_file())
                    elif route == "update_atom":
                        self.assertIn("Clarified fixture acceptance detail.",
                                      (fixture.root / result["observed"]["path"]).read_text(encoding="utf-8"))
                        self.assertEqual(2, result["observed"]["version"])
                    elif route == "replace_atom":
                        self.assertTrue((fixture.root / result["successors"][0]["path"]).is_file())
                    elif route == "change_atom_status":
                        self.assertIn("/archived/", result["observed"]["path"])
                        self.assertEqual("Archived", result["observed"]["status"])
                    elif route == "rename_scope_unit":
                        self.assertEqual("RENAMED\n", (fixture.root / "fixture/reference.txt").read_text(encoding="utf-8"))
                    else:
                        self.assertIn("scope_units", (fixture.root / ".caprmedio_caprmedio/project_structure.toml").read_text(encoding="utf-8"))
                finally:
                    lease.cleanup()

    def test_concern_status_model_uses_frozen_inherited_sources(self) -> None:
        lease, fixture = self._fixture("W01", "create_atom")
        try:
            carrier = fixture.create_status_carrier("Concern", "Resolved", number=8299)
            model = resolve_status_model(fixture.root, carrier, "Resolved")
            self.assertEqual(
                ["Draft", "Active", "Archived", "Resolved", "Canceled"],
                model["statuses"],
            )
            self.assertEqual(
                ("CA-R-1947", "CA-R-1608"),
                tuple(row["atom_id"] for row in model["model_sources"]),
            )
            self.assertEqual((3, 8), tuple(row["revision"] for row in model["model_sources"]))
            for row in model["model_sources"]:
                copied = fixture.root / row["path"]
                self.assertEqual(frozen_source_bytes(row["path"]), copied.read_bytes())
                self.assertEqual(row["sha256"], hashlib.sha256(copied.read_bytes()).hexdigest())
        finally:
            lease.cleanup()

    def test_plan_status_model_uses_frozen_inherited_sources(self) -> None:
        lease, fixture = self._fixture("W01", "create_atom")
        try:
            carrier = fixture.create_status_carrier("Plan", "Done", number=8298)
            model = resolve_status_model(fixture.root, carrier, "Done")
            self.assertEqual(
                ["Draft", "Active", "Archived", "Backlog", "Done", "Canceled"],
                model["statuses"],
            )
            self.assertEqual(
                ("CA-R-1947", "CA-R-1539"),
                tuple(row["atom_id"] for row in model["model_sources"]),
            )
            self.assertEqual((3, 9), tuple(row["revision"] for row in model["model_sources"]))
            for row in model["model_sources"]:
                copied = fixture.root / row["path"]
                self.assertEqual(frozen_source_bytes(row["path"]), copied.read_bytes())
                self.assertEqual(row["sha256"], hashlib.sha256(copied.read_bytes()).hexdigest())
        finally:
            lease.cleanup()


if __name__ == "__main__":
    unittest.main()
