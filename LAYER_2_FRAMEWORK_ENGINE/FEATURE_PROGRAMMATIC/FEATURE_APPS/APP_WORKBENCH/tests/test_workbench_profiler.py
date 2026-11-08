# CA-R-2998@1
# CA-M-503@1
# CA-D-703@1
# CA-E-795@1

"""Bounded checks for the explicitly invoked Workbench profiler CLI."""

from __future__ import annotations

from pathlib import Path
import os
import pstats
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"))

from profile_workbench import output_directory, profile
from smalltest_support import extension_directory, write_atom
from scope_declaration_test_support import write_scope_unit_declarations


REPOSITORY = Path(__file__).resolve().parents[5]


class WorkbenchProfilerTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary_root = REPOSITORY / ".caprmedio_tmp/tests/workbench-profiler"
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary_root)
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name) / "project"
        self.control = self.project / ".caprmedio_caprmedio"
        self.control.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[project]\nname = 'fixture'\n[artifacts.identity]\nproject_prefix = 'CA'\n[paths]\n"
            "control_root = '.caprmedio_caprmedio'\ntemporary_root = '.caprmedio_tmp'\n",
            encoding="utf-8",
        )
        write_scope_unit_declarations(self.project, (), control_root=self.control)

    def test_output_stays_under_project_temporary_root(self) -> None:
        output = output_directory(self.project, self.project / ".caprmedio_tmp/reports/run")
        self.assertEqual((self.project / ".caprmedio_tmp/reports/run").resolve(), output)
        with self.assertRaisesRegex(ValueError, "temporary root"):
            output_directory(self.project, self.project / "outside")

    def test_cli_help_is_available_without_profiling(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("profile_workbench.py")), "--help"],
            check=True, text=True, capture_output=True,
        )
        self.assertIn("--project-root", completed.stdout)
        self.assertIn("--output", completed.stdout)

    def test_profile_isolated_small_project_with_native_duckpgq(self) -> None:
        declarations = write_scope_unit_declarations(
            self.project,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=self.control,
        )
        source = Path(declarations["ENGINE"]["authority_path"]) / "04_requirement" / "source.md"
        write_atom(source, "CA-R-501")
        source_bytes = source.read_bytes()
        output = output_directory(self.project, None)
        with patch.dict(
            os.environ,
            {"CAPRMEDIO_DUCKPGQ_EXTENSION_DIRECTORY": str(extension_directory(REPOSITORY))},
        ):
            report = profile(self.project, output)
        self.assertEqual(3, report["rebuild_cycles"])
        self.assertTrue(report["instrumented"])
        self.assertEqual(report["source_hashes_before"], report["source_hashes_after"])
        self.assertTrue((output / "cpu.pstats").is_file())
        self.assertTrue((output / "report.json").is_file())
        self.assertTrue(pstats.Stats(str(output / "cpu.pstats")).stats)
        self.assertTrue(report["python_allocations"]["top"])
        self.assertIn("process_high_water_rss_bytes", report["measurements"][0])
        self.assertFalse(report["measurements"][0]["process_high_water_rss_is_current_memory"])
        self.assertTrue(report["runtime"]["duckdb_package_version"])
        self.assertTrue(report["disposable_database_cleanup"]["succeeded"])
        self.assertEqual(source_bytes, source.read_bytes())

    def test_failed_database_cleanup_is_confined_to_profile_output(self) -> None:
        declarations = write_scope_unit_declarations(
            self.project,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=self.control,
        )
        source = Path(declarations["ENGINE"]["authority_path"]) / "04_requirement" / "source.md"
        write_atom(source, "CA-R-502")
        source_bytes = source.read_bytes()
        output = output_directory(self.project, None)
        with (
            patch.dict(os.environ, {"CAPRMEDIO_DUCKPGQ_EXTENSION_DIRECTORY": str(extension_directory(REPOSITORY))}),
            patch("profile_workbench.shutil.rmtree", side_effect=OSError("denied")),
        ):
            report = profile(self.project, output)
        cleanup = report["disposable_database_cleanup"]
        self.assertFalse(cleanup["succeeded"])
        self.assertEqual(str(output / "disposable-database"), cleanup["retained_path"])
        self.assertTrue(Path(cleanup["retained_path"]).is_relative_to(output))
        self.assertEqual(source_bytes, source.read_bytes())


if __name__ == "__main__":
    unittest.main()
