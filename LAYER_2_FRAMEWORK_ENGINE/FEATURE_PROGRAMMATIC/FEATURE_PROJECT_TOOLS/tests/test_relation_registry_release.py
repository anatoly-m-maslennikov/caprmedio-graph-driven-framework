# CA-M-509@1
# CA-D-705@1
# CA-E-804@1

"""The canonical registry is a generated release-package input."""

from pathlib import Path
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "LAYER_5_FRAMEWORK_DELIVERY/tests"))
import test_simple_local_release as release_fixture
import local_release


class RelationRegistryReleaseTests(unittest.TestCase):
    def setUp(self):
        self.fixture = release_fixture.SimpleLocalReleaseTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_generated_registry_replaces_stale_package_asset_before_image_build(self):
        fixture = self.fixture
        relative = Path(
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/"
            "APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/canonical_relation_registry.json"
        )
        (fixture.root / relative).write_text("stale source asset", encoding="utf-8")
        observed = []

        def resolve(**kwargs):
            if kwargs != {"use_packaged_assets": True}:
                return fixture.image_id
            package = Path(fixture.image_factory.call_args.args[0])
            self.assertEqual('{"schema_version":1,"registered_names":[]}\n',
                             (package / relative).read_text(encoding="utf-8"))
            self.assertEqual((package / relative).read_bytes(), (fixture.root / relative).read_bytes())
            observed.append(package)
            return fixture.image_id

        fixture.image.resolve.side_effect = resolve
        runner, _calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="relation-registry-build", runner=runner)
        self.assertEqual("completed", result["outcome"], result)
        self.assertEqual(1, len(observed))
        self.assertEqual('{"schema_version":1,"registered_names":[]}\n', (fixture.root / relative).read_text())

    def test_missing_fresh_output_does_not_reuse_a_copied_registry(self):
        fixture = self.fixture
        script = fixture.root / (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
            "FEATURE_WORKBENCH_BACKEND/generate_relation_registry.py"
        )
        script.write_text("pass\n", encoding="utf-8")
        script.with_name("canonical_relation_registry.json").write_text("stale asset", encoding="utf-8")
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="relation-registry-no-output", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("build_package", result["failed_step"])
        self.assertEqual("stale asset", script.with_name("canonical_relation_registry.json").read_text())
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))

    def test_generator_failure_stops_before_image_build_or_startup(self):
        fixture = self.fixture
        script = fixture.root / (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
            "FEATURE_WORKBENCH_BACKEND/generate_relation_registry.py"
        )
        script.write_text("raise SystemExit(1)\n", encoding="utf-8")
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="relation-registry-failure", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("build_package", result["failed_step"])
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))

    def test_missing_tool_registry_generator_stops_before_image_build_or_startup(self):
        fixture = self.fixture
        (fixture.engine_bootstrap.parent.parent / "generate_tool_registry.py").unlink()
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="tool-registry-missing", runner=runner)
        self.assertEqual(("failed", "build_package"), (result["outcome"], result["failed_step"]))
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))

    def test_invalid_tool_registry_output_stops_before_image_build_or_startup(self):
        fixture = self.fixture
        script = fixture.engine_bootstrap.parent.parent / "generate_tool_registry.py"
        script.write_text(
            "from pathlib import Path\n"
            "import sys\n"
            "root = Path(sys.argv[sys.argv.index('--package-root') + 1])\n"
            "(root / 'LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry.json').write_text('not-json', encoding='utf-8')\n",
            encoding="utf-8",
        )
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="tool-registry-invalid", runner=runner)
        self.assertEqual(("failed", "build_package"), (result["outcome"], result["failed_step"]))
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))

    def test_generated_schema_replaces_stale_package_asset_and_is_sealed(self):
        fixture = self.fixture
        relative = Path(
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/"
            "APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/workbench_schema.json"
        )
        (fixture.root / relative).write_text("stale source asset", encoding="utf-8")
        expected_maps = []
        observed = []
        verify = local_release._verify_package

        def capture(package, expected):
            if package.name == "package":
                expected_maps.append(expected)
            return verify(package, expected)

        def resolve(**kwargs):
            if kwargs == {"use_packaged_assets": True}:
                package = Path(fixture.image_factory.call_args.args[0])
                observed.append((package / relative).read_text(encoding="utf-8"))
            return fixture.image_id

        fixture.image.resolve.side_effect = resolve
        runner, _calls = fixture._runner()
        with fixture._compiler(), mock.patch.object(local_release, "_verify_package", side_effect=capture):
            result = local_release.run_local_release(fixture.root, run_id="workbench-schema-build", runner=runner)
        self.assertEqual("completed", result["outcome"], result)
        self.assertEqual(['{"schema_version":1,"tables":[]}\n'], observed)
        self.assertTrue(any(relative.as_posix() in expected for expected in expected_maps))
        self.assertEqual(observed[0], (fixture.root / relative).read_text())

    def test_missing_fresh_schema_does_not_reuse_a_copied_asset(self):
        fixture = self.fixture
        script = fixture.root / (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
            "FEATURE_WORKBENCH_BACKEND/generate_workbench_schema.py"
        )
        script.write_text("pass\n", encoding="utf-8")
        script.with_name("workbench_schema.json").write_text("stale asset", encoding="utf-8")
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="workbench-schema-no-output", runner=runner)
        self.assertEqual(("failed", "build_package"), (result["outcome"], result["failed_step"]))
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))

    def test_symlinked_schema_output_stops_before_image_build_or_startup(self):
        fixture = self.fixture
        script = fixture.root / (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/"
            "FEATURE_WORKBENCH_BACKEND/generate_workbench_schema.py"
        )
        target = script.with_name("schema-target.json")
        target.write_text("schema", encoding="utf-8")
        script.write_text(
            "from pathlib import Path\n"
            "import sys\n"
            "output = Path(sys.argv[sys.argv.index('--output') + 1])\n"
            "output.symlink_to(output.with_name('schema-target.json'))\n",
            encoding="utf-8",
        )
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="workbench-schema-symlink", runner=runner)
        self.assertEqual(("failed", "build_package"), (result["outcome"], result["failed_step"]))
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))


if __name__ == "__main__":
    unittest.main()
