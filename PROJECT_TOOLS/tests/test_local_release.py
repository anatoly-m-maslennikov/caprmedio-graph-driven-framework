from __future__ import annotations

import stat
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1] / "RELEASE_VERSION"
sys.path.insert(0, str(MODULE_ROOT))

from local_release import LocalReleaseError, run_local_release  # noqa: E402


class LocalReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True, dir="/private/tmp")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        sources = control / "101_LAYER_1_FRAMEWORK_METHODOLOGY" / "METHODOLOGY_SOURCES"
        control.mkdir()
        (control / "project_structure.toml").write_text(
            "\n".join(
                [
                    "[[scope_units]]",
                    'scope_unit_name = "CORE_META_MODEL"',
                    'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"',
                    "",
                    "[[scope_units]]",
                    'scope_unit_name = "INSTALLED_EXTENSIONS"',
                    'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/002_INSTALLED_EXTENSIONS"',
                    "",
                    "[[scope_units]]",
                    'scope_unit_name = "PROJECT_CONFIGURATION"',
                    'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION"',
                    "",
                ]
            ),
            encoding="utf-8",
        )
        for number, name in (("001", "CORE_META_MODEL"), ("002", "INSTALLED_EXTENSIONS"), ("003", "PROJECT_CONFIGURATION")):
            unit = sources / f"{number}_{name}"
            unit.mkdir(parents=True)
            active = unit / "active.md"
            active.write_text("---\natom_id: CA-X-1\nstatus: Active\n---\nactive\n", encoding="utf-8")
            active.chmod(0o640)
            (unit / "retired.md").write_text("---\natom_id: CA-X-2\nstatus: Retired\n---\nretired\n", encoding="utf-8")
        product = self.root / "101_FRAMEWORK_METHODOLOGY"
        product.mkdir()
        (product / "old.txt").write_text("old-product", encoding="utf-8")
        (product / "settings.toml").write_text("keep = true\n", encoding="utf-8")
        (product / "project_settings.toml").write_text("product = true\n", encoding="utf-8")
        (product / "caprmedio_framework_settings.toml").write_text("framework = true\n", encoding="utf-8")
        (product / "operators_registry.toml").write_text("operators = true\n", encoding="utf-8")
        installed = control / "000_CAPRMEDIO_framework"
        installed.mkdir()
        (installed / "old.txt").write_text("old-installed", encoding="utf-8")
        (installed / "config.toml").write_text("keep = true\n", encoding="utf-8")
        (installed / "project_structure.toml").write_text("keep = true\n", encoding="utf-8")
        (installed / "project_settings.toml").write_text("project = true\n", encoding="utf-8")
        (installed / "caprmedio_framework_settings.toml").write_text("framework = true\n", encoding="utf-8")
        (installed / "operators_registry.toml").write_text("operators = true\n", encoding="utf-8")
        (installed / "operator_registry").mkdir()
        (installed / "operator_registry" / "entry.txt").write_text("keep", encoding="utf-8")
        (self.root / ".caprmedio_runtime").mkdir()
        (self.root / ".caprmedio_runtime" / "config.toml").write_text("runtime = true\n", encoding="utf-8")

    def _hooks(self, *, fail_test: bool = False, failed_report: bool = False,
               mutate_source: bool = False) -> tuple[dict[str, object], list[tuple[str, object]]]:
        calls: list[tuple[str, object]] = []

        def compile(*, source_root: Path, output_root: Path, project_root: Path) -> None:
            calls.append(("compile", source_root))
            output_root.mkdir(parents=True, exist_ok=False)
            (output_root / "compiled.md").write_text("compiled", encoding="utf-8")

        def test(*, project_root: Path, candidate_root: Path) -> None:
            calls.append(("test", candidate_root))
            self.assertTrue((project_root / "101_FRAMEWORK_METHODOLOGY" / "old.txt").is_file())
            if fail_test:
                raise RuntimeError("configured full suite failed")
            if mutate_source:
                source = project_root / ".caprmedio_caprmedio" / "101_LAYER_1_FRAMEWORK_METHODOLOGY" / "METHODOLOGY_SOURCES" / "001_CORE_META_MODEL" / "active.md"
                source.write_text("---\natom_id: CA-X-1\nstatus: Active\n---\nchanged-after-test\n", encoding="utf-8")
            if failed_report:
                return {"passed": False}

        def commit(*, project_root: Path, paths: tuple[str, ...], message: str) -> None:
            calls.append(("commit", (paths, message)))

        def install_engine(*, project_root: Path, candidate_root: Path) -> None:
            calls.append(("install_engine", candidate_root))

        def start_mcp(*, project_root: Path) -> None:
            calls.append(("start_mcp", project_root))

        def journal(*, event: dict[str, object]) -> None:
            calls.append(("journal", event["phase"]))

        return {"compile": compile, "test": test, "commit": commit, "install_engine": install_engine,
                "start_mcp": start_mcp, "journal": journal}, calls

    def test_happy_path_copies_active_atoms_and_preserves_configuration(self) -> None:
        hooks, calls = self._hooks(mutate_source=True)
        result = run_local_release(self.root, run_id="r1", hooks=hooks)
        self.assertEqual("completed", result["outcome"])
        candidate = Path(result["candidate_root"])
        for unit in ("001_CORE_META_MODEL", "002_INSTALLED_EXTENSIONS", "003_PROJECT_CONFIGURATION"):
            active = candidate / "sources" / unit / "active.md"
            self.assertTrue(active.is_file())
            self.assertFalse((candidate / "sources" / unit / "retired.md").exists())
            self.assertEqual(0o640, stat.S_IMODE(active.stat().st_mode))
            self.assertTrue((self.root / "101_FRAMEWORK_METHODOLOGY" / "sources" / unit / "active.md").is_file())
        self.assertIn("active", (self.root / "101_FRAMEWORK_METHODOLOGY" / "sources" / "001_CORE_META_MODEL" / "active.md").read_text())
        self.assertNotIn("changed-after-test", (self.root / "101_FRAMEWORK_METHODOLOGY" / "sources" / "001_CORE_META_MODEL" / "active.md").read_text())
        self.assertFalse((self.root / "101_FRAMEWORK_METHODOLOGY" / "old.txt").exists())
        self.assertEqual("keep = true\n", (self.root / "101_FRAMEWORK_METHODOLOGY" / "settings.toml").read_text())
        self.assertEqual("product = true\n", (self.root / "101_FRAMEWORK_METHODOLOGY" / "project_settings.toml").read_text())
        self.assertEqual("framework = true\n", (self.root / "101_FRAMEWORK_METHODOLOGY" / "caprmedio_framework_settings.toml").read_text())
        self.assertEqual("operators = true\n", (self.root / "101_FRAMEWORK_METHODOLOGY" / "operators_registry.toml").read_text())
        installed = self.root / ".caprmedio_caprmedio" / "000_CAPRMEDIO_framework"
        self.assertFalse((installed / "old.txt").exists())
        self.assertTrue((installed / "applicable_methodology" / "compiled.md").is_file())
        self.assertEqual("keep = true\n", (installed / "config.toml").read_text())
        self.assertEqual("project = true\n", (installed / "project_settings.toml").read_text())
        self.assertEqual("framework = true\n", (installed / "caprmedio_framework_settings.toml").read_text())
        self.assertEqual("operators = true\n", (installed / "operators_registry.toml").read_text())
        self.assertEqual("keep", (installed / "operator_registry" / "entry.txt").read_text())
        self.assertEqual("runtime = true\n", (self.root / ".caprmedio_runtime" / "config.toml").read_text())
        commits = [payload for name, payload in calls if name == "commit"]
        self.assertEqual(
            [
                "local release r1: clear product",
                "local release r1: copy active sources",
                "local release r1: compile product",
                "local release r1: clear installed framework",
                "local release r1: copy product to installed framework",
            ],
            [message for _, message in commits],
        )
        self.assertEqual(("101_FRAMEWORK_METHODOLOGY/old.txt",), commits[0][0])
        self.assertEqual((
            "101_FRAMEWORK_METHODOLOGY/sources/001_CORE_META_MODEL/active.md",
            "101_FRAMEWORK_METHODOLOGY/sources/002_INSTALLED_EXTENSIONS/active.md",
            "101_FRAMEWORK_METHODOLOGY/sources/003_PROJECT_CONFIGURATION/active.md",
        ), commits[1][0])
        self.assertEqual(("101_FRAMEWORK_METHODOLOGY/applicable_methodology/compiled.md",), commits[2][0])
        self.assertEqual((".caprmedio_caprmedio/000_CAPRMEDIO_framework/old.txt",), commits[3][0])
        self.assertNotIn(".caprmedio_caprmedio/000_CAPRMEDIO_framework/config.toml", commits[4][0])
        for preserved in (
            "project_settings.toml",
            "caprmedio_framework_settings.toml",
            "operators_registry.toml",
        ):
            self.assertFalse(any(path.endswith(preserved) for paths, _ in commits for path in paths))
        self.assertEqual(["compile", "test", "commit", "commit", "compile", "commit", "commit", "commit", "install_engine", "start_mcp"],
                         [name for name, _ in calls if name != "journal"])

    def test_test_failure_stops_before_first_wipe(self) -> None:
        hooks, calls = self._hooks(fail_test=True)
        result = run_local_release(self.root, run_id="r2", hooks=hooks)
        self.assertEqual({"outcome": "failed", "phase": "full_test"},
                         {key: result[key] for key in ("outcome", "phase")})
        self.assertEqual("old-product", (self.root / "101_FRAMEWORK_METHODOLOGY" / "old.txt").read_text())
        self.assertEqual("old-installed", (self.root / ".caprmedio_caprmedio" / "000_CAPRMEDIO_framework" / "old.txt").read_text())
        self.assertNotIn("commit", [name for name, _ in calls])
        self.assertNotIn("install_engine", [name for name, _ in calls])

    def test_historical_active_metadata_is_not_released(self) -> None:
        source = self.root / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"
        for directory in ("archive", "draft", "_projection"):
            historical = source / directory / "old.md"
            historical.parent.mkdir()
            historical.write_text("---\natom_id: CA-R-1\nstatus: Active\n---\nhistorical\n", encoding="utf-8")
        hooks, _ = self._hooks()
        result = run_local_release(self.root, run_id="r-history", hooks=hooks)
        self.assertEqual("completed", result["outcome"])
        released = self.root / "101_FRAMEWORK_METHODOLOGY/sources/001_CORE_META_MODEL"
        self.assertEqual(["active.md"], [path.name for path in released.rglob("*.md")])

    def test_failed_test_report_stops_before_first_wipe(self) -> None:
        hooks, calls = self._hooks(failed_report=True)
        result = run_local_release(self.root, run_id="r2-report", hooks=hooks)
        self.assertEqual({"outcome": "failed", "phase": "full_test"},
                         {key: result[key] for key in ("outcome", "phase")})
        self.assertEqual("old-product", (self.root / "101_FRAMEWORK_METHODOLOGY" / "old.txt").read_text())
        self.assertNotIn("commit", [name for name, _ in calls])

    def test_empty_extensions_and_descendant_ds_store_are_retained(self) -> None:
        extension = self.root / ".caprmedio_caprmedio" / "101_LAYER_1_FRAMEWORK_METHODOLOGY" / "METHODOLOGY_SOURCES" / "002_INSTALLED_EXTENSIONS" / "active.md"
        extension.unlink()
        product_directory = self.root / "101_FRAMEWORK_METHODOLOGY" / "obsolete"
        product_directory.mkdir()
        (product_directory / ".DS_Store").write_text("ignored", encoding="utf-8")
        (product_directory / "owned.txt").write_text("remove", encoding="utf-8")
        installed_directory = self.root / ".caprmedio_caprmedio" / "000_CAPRMEDIO_framework" / "obsolete"
        installed_directory.mkdir()
        (installed_directory / ".DS_Store").write_text("ignored", encoding="utf-8")
        (installed_directory / "owned.txt").write_text("remove", encoding="utf-8")
        hooks, _ = self._hooks()
        result = run_local_release(self.root, run_id="r-empty-extension", hooks=hooks)
        self.assertEqual("completed", result["outcome"])
        self.assertFalse((self.root / "101_FRAMEWORK_METHODOLOGY" / "sources" / "002_INSTALLED_EXTENSIONS" / "active.md").exists())
        self.assertTrue((product_directory / ".DS_Store").is_file())
        self.assertFalse((product_directory / "owned.txt").exists())
        self.assertTrue((installed_directory / ".DS_Store").is_file())
        self.assertFalse((installed_directory / "owned.txt").exists())

    def test_rejects_broad_product_target_before_callbacks(self) -> None:
        hooks, calls = self._hooks()
        with self.assertRaisesRegex(LocalReleaseError, "local-release-target-invalid"):
            run_local_release(self.root, run_id="r3", hooks=hooks, config={"product_root": "."})
        self.assertEqual([], calls)

    def test_missing_required_hook_refuses_before_private_candidate_creation(self) -> None:
        hooks, calls = self._hooks()
        del hooks["start_mcp"]
        with self.assertRaisesRegex(LocalReleaseError, "local-release-hooks-invalid:start_mcp"):
            run_local_release(self.root, run_id="r4", hooks=hooks)
        self.assertFalse((self.root / ".caprmedio_tmp" / "local_release" / "r4").exists())
        self.assertEqual([], calls)
