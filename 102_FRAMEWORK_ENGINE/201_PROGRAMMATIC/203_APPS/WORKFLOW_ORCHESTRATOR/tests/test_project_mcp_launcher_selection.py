"""Golden contract for explicit Project MCP selection before runtime effects."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path.insert(0, str(TOOLS))

from project_selection import active_selection, bind_selection, resolve_project  # noqa: E402


GOLDENS = Path(__file__).parent / "launcher_golden" / "selection_cases.json"


class ProjectSelectionGoldenTests(unittest.TestCase):
    """Fixtures are deliberately retained: sandbox cleanup is not test evidence."""

    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp" / "launcher-epic-1829" / "selection"
        parent.mkdir(parents=True, exist_ok=True)
        self.fixture_root = Path(tempfile.mkdtemp(dir=parent))

    def project(self, name: str, *, control: str = ".caprmedio_demo") -> Path:
        root = self.fixture_root / name
        carrier = root / control
        carrier.mkdir(parents=True)
        (carrier / "caprmedio_project_settings.toml").write_text(
            f'[paths]\ncontrol_root = "{control}"\n[project]\nname = "{name}"\n',
            encoding="utf-8",
        )
        (carrier / "project_structure.toml").write_text("schema_version = 1\n", encoding="utf-8")
        return root

    def test_golden_corpus_covers_selection_refusals_and_context_cases(self) -> None:
        cases = json.loads(GOLDENS.read_text(encoding="utf-8"))
        self.assertEqual(8, len(cases))
        self.assertEqual(
            {"selected", "refused"}, {case["outcome"] for case in cases}
        )
        self.assertEqual(len(cases), len({case["id"] for case in cases}))

    def test_sibling_project_roots_select_only_their_direct_control_and_need_no_git(self) -> None:
        repository = self.fixture_root / "repository"
        alpha = self.project("repository/projects/alpha")
        beta = self.project("repository/projects/beta")
        # The parent may be a Git repository, but neither selected Project is.
        (repository / ".git").mkdir(parents=True)

        selected_alpha = resolve_project(alpha)
        selected_beta = resolve_project(beta)

        self.assertEqual(alpha.resolve(), selected_alpha.root)
        self.assertEqual(beta.resolve(), selected_beta.root)
        self.assertEqual(Path(".caprmedio_demo"), selected_alpha.control_relative)
        self.assertNotEqual(selected_alpha.instance_id, selected_beta.instance_id)
        self.assertEqual(
            hashlib.sha256(
                f"{alpha.resolve()}\0.caprmedio_demo".encode("utf-8")
            ).hexdigest(),
            selected_alpha.instance_id,
        )
        self.assertFalse((alpha / ".git").exists())
        self.assertFalse((beta / ".git").exists())

    def test_explicit_direct_control_root_is_allowed_but_ambiguous_or_unsafe_selectors_refuse(self) -> None:
        project = self.project("one")
        self.assertEqual(
            project / ".caprmedio_demo",
            resolve_project(project, ".caprmedio_demo").control_root,
        )
        self.project("one", control=".caprmedio_other")
        with self.assertRaises(ValueError):
            resolve_project(project)
        for unsafe in ("../.caprmedio_demo", "/tmp/not-a-control-root", ".caprmedio_demo/nested"):
            with self.subTest(selector=unsafe), self.assertRaises(ValueError):
                resolve_project(project, unsafe)

    def test_symlink_and_contradictory_control_bindings_refuse_without_sibling_fallback(self) -> None:
        project = self.project("selected")
        sibling = self.project("sibling")
        alias = project / ".caprmedio_alias"
        alias.symlink_to(sibling / ".caprmedio_demo", target_is_directory=True)
        with self.assertRaises(ValueError):
            resolve_project(project, ".caprmedio_alias")

        settings = project / ".caprmedio_demo" / "caprmedio_project_settings.toml"
        settings.write_text('[paths]\ncontrol_root = ".caprmedio_other"\n', encoding="utf-8")
        with self.assertRaises(ValueError):
            resolve_project(project, ".caprmedio_demo")

    def test_foreign_active_selection_context_refuses_without_substitution(self) -> None:
        alpha = self.project("repository/projects/alpha")
        beta = self.project("repository/projects/beta")
        selection_a = resolve_project(alpha)
        with bind_selection(selection_a):
            self.assertIs(selection_a, active_selection(alpha))
            with self.assertRaises(ValueError):
                active_selection(beta)


if __name__ == "__main__":
    unittest.main()
