"""Regression for native Plan demotion retaining canonical history."""
from __future__ import annotations

from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

from atom_operations import atom_from_path, frontmatter_scalar  # noqa: E402
import test_model_driven_status_lifecycle as model_fixture  # noqa: E402


class PlanDraftHistoryRegressionTest(unittest.TestCase):
    def setUp(self) -> None:
        model_fixture.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = model_fixture.ModelDrivenStatusLifecycleTest("run")
        self.addCleanup(self.fixture.tearDown)
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()

    def test_plan_active_to_draft_reads_canonical_archived_predecessor(self) -> None:
        path = self.fixture.atom("Plan", "Active", number=8001, container="CA-P-8000--parent")
        before_atom = atom_from_path(self.fixture.root, path)
        before = path.read_bytes()
        fixture_plan_root = self.fixture.root / ".caprmedio_caprmedio" / "fixture" / "03_plan"
        expected_history = fixture_plan_root / "archived" / f"{path.stem}@{frontmatter_scalar(before_atom.frontmatter, 'version')}{path.suffix}"

        result = self.fixture.execute(self.fixture.request(path, "Draft"))

        draft = self.fixture.root / result["observed"]["path"]
        history = self.fixture.root / result["history"]["prior_revision"]["path"]
        self.assertEqual("CA-P--golden.md", draft.name)
        self.assertEqual("Draft", frontmatter_scalar(atom_from_path(self.fixture.root, draft).frontmatter, "status"))
        self.assertEqual(expected_history, history)
        self.assertEqual(before, history.read_bytes())


if __name__ == "__main__":
    unittest.main()
