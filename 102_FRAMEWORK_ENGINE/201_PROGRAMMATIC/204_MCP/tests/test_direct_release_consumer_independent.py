"""Direct-route refusal/effect truth checks with actual loader and Journal I/O."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

import test_simple_local_release_route as route_fixture
import selected_routes
import work_journal


class DirectReleaseConsumerIndependentTests(unittest.TestCase):
    def setUp(self):
        scratch = route_fixture.PROJECT / ".caprmedio_tmp/tests/direct-release-consumer-independent"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nkey = "CA"\nname = "fixture"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            '[artifact_timestamps]\ntimezone = "UTC"\n', encoding="utf-8")
        (control / "project_structure.toml").write_text(
            'schema_version = 1\nscope_units = []\n', encoding="utf-8")
        self.entrypoint = self.root / "PROJECT_TOOLS/RELEASE_VERSION/local_release.py"
        self.entrypoint.parent.mkdir(parents=True)
        shutil.copyfile(route_fixture.PROJECT / "PROJECT_TOOLS/RELEASE_VERSION/local_release.py", self.entrypoint)
        self.product = self.root / "101_FRAMEWORK_METHODOLOGY"
        self.product.mkdir()
        self.sentinel = self.product / "keep.md"
        self.sentinel.write_bytes(b"No release step reached this product.\n")
        server = route_fixture._Server()
        mcp = types.ModuleType("mcp")
        mcp_types = types.ModuleType("mcp.types")
        mcp_types.ToolAnnotations = route_fixture._Annotations
        mcp.types = mcp_types
        with patch.dict(sys.modules, {"mcp": mcp, "mcp.types": mcp_types}):
            selected_routes.register_selected_routes(server, self.root)
        self.release = server.tools["release_version"]
        self.request = {"project_root": str(self.root), "run_id": "independent-release"}

    def files(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob("*") if p.is_file() and not p.is_symlink()}

    def events(self):
        return [json.loads(line) for path in self.root.rglob("src-work-journal-*.ndjson")
                for line in path.read_bytes().splitlines()]

    def fail_first_command(self, argv, *, cwd, **options):
        self.assertEqual(cwd, self.root)
        self.assertEqual(argv[:3], ("git", "add", "-A"))
        return subprocess.CompletedProcess(argv, 2, "", "Independent first-command refusal")

    def test_invalid_or_legacy_manifest_envelope_refuses_without_dispatch_or_journal(self):
        before = self.files()
        for request in (
            {**self.request, "run_id": "../unsafe"},
            {**self.request, "project_root": str(self.root.parent)},
            {**self.request, "mode": "apply"},
            {**self.request, "definition_manifest": {"manifest_ref": "old.json", "manifest_digest": "0" * 64}},
        ):
            with self.subTest(request=request), patch.object(subprocess, "run", side_effect=AssertionError("Unexpected dispatch")):
                result = self.release(request)
            self.assertEqual(result["outcome"], "failed")
            self.assertEqual(self.files(), before)
        self.assertEqual(self.events(), [])

    def test_actual_loader_and_runner_failure_preserves_product_and_records_exact_outcome(self):
        prior = self.sentinel.read_bytes()
        with patch.object(subprocess, "run", side_effect=self.fail_first_command) as command:
            result = self.release(self.request)
        self.assertEqual(command.call_count, 1)
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(result["failed_step"], "git_before_tests")
        self.assertEqual(self.sentinel.read_bytes(), prior)
        self.assertTrue((self.root / result["report_path"]).is_file())
        events = self.events()
        self.assertEqual([event["event"] for event in events], ["started", "failed"])
        self.assertEqual(events[1]["preceding_event"], events[0]["event_id"])
        self.assertEqual(events[1]["details"], {"outcome": "failed"})
        self.assertEqual([event["operation"] for event in events], ["release_version", "release_version"])

    def test_start_recording_failure_does_not_gate_actual_entrypoint(self):
        before = self.sentinel.read_bytes()
        with patch.object(work_journal, "append_record", side_effect=OSError("Journal unavailable")), \
                patch.object(subprocess, "run", side_effect=self.fail_first_command) as command:
            result = self.release(self.request)
        self.assertEqual(command.call_count, 1)
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(result["failed_step"], "git_before_tests")
        self.assertTrue((self.root / result["report_path"]).is_file())
        self.assertIn("Journal unavailable", result["recording_error"])
        self.assertEqual(self.sentinel.read_bytes(), before)
        self.assertEqual(self.events(), [])

    def test_symlinked_entrypoint_refuses_with_actual_failed_terminal_event(self):
        source = self.entrypoint.with_name("other.py")
        self.entrypoint.rename(source)
        self.entrypoint.symlink_to(source)
        before = self.sentinel.read_bytes()
        with patch.object(subprocess, "run", side_effect=AssertionError("Unexpected dispatch")):
            result = self.release(self.request)
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(result["diagnostics"], ["Release implementation path is a symlink"])
        self.assertEqual(self.sentinel.read_bytes(), before)
        self.assertEqual([event["event"] for event in self.events()], ["started", "failed"])

    def test_terminal_recording_failure_preserves_actual_runner_failure(self):
        append = work_journal.append_record
        def refuse_terminal(root, record):
            if record["event"] != "started":
                raise OSError("Terminal Journal unavailable")
            return append(root, record)
        with patch.object(subprocess, "run", side_effect=self.fail_first_command), \
                patch.object(work_journal, "append_record", side_effect=refuse_terminal):
            result = self.release(self.request)
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(result["failed_step"], "git_before_tests")
        self.assertIn("Terminal Journal unavailable", result["recording_error"])
        self.assertEqual([event["event"] for event in self.events()], ["started"])
        self.assertEqual(self.sentinel.read_bytes(), b"No release step reached this product.\n")


if __name__ == "__main__":
    unittest.main()
