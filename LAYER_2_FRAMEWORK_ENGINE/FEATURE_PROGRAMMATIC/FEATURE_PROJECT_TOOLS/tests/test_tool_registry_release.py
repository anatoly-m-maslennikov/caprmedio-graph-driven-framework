# CA-E-798@1
# CA-D-704@1

"""Registration configuration is part of the package before image startup."""

from pathlib import Path
import unittest

import test_simple_local_release as release_fixture
import local_release


class ToolRegistryReleaseTests(unittest.TestCase):
    def setUp(self):
        self.fixture = release_fixture.SimpleLocalReleaseTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_generated_registry_replaces_stale_package_asset_before_image_build(self):
        fixture = self.fixture
        relative = Path("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tool_registry.json")
        (fixture.root / relative).write_text("stale source asset", encoding="utf-8")
        generator = fixture.root / relative.parent / "generate_tool_registry.py"
        generator.with_name("registry_payload.py").write_text("VALUE = 1\n", encoding="utf-8")
        generator.write_text("import registry_payload\n" + generator.read_text(), encoding="utf-8")
        observed = []

        def resolve(**kwargs):
            if kwargs:
                return fixture.image_id
            package = Path(fixture.image_factory.call_args.args[0])
            self.assertEqual(
                '{"schema_version":1,"providers":[]}\n',
                (package / relative).read_text(encoding="utf-8"),
            )
            self.assertEqual([], list(package.rglob("*.pyc")))
            observed.append(package)
            return fixture.image_id

        fixture.image.resolve.side_effect = resolve
        runner, _calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="registry-build", runner=runner)
        self.assertEqual("completed", result["outcome"], result)
        self.assertEqual(1, len(observed))
        self.assertEqual("stale source asset", (fixture.root / relative).read_text())

    def test_success_without_fresh_output_does_not_reuse_a_copied_registry(self):
        fixture = self.fixture
        script = fixture.root / (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tool_registry.py"
        )
        script.write_text("pass\n", encoding="utf-8")
        script.with_name("tool_registry.json").write_text("stale asset", encoding="utf-8")
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="registry-no-output", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("build_package", result["failed_step"])
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))

    def test_generator_failure_stops_before_image_build_or_startup(self):
        fixture = self.fixture
        script = fixture.root / (
            "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tool_registry.py"
        )
        script.write_text("raise SystemExit(1)\n", encoding="utf-8")
        runner, calls = fixture._runner()
        with fixture._compiler():
            result = local_release.run_local_release(fixture.root, run_id="registry-failure", runner=runner)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("build_package", result["failed_step"])
        fixture.image_factory.assert_not_called()
        self.assertFalse(any(fixture._is_mcp_bootstrap(argv) for argv in calls))


if __name__ == "__main__":
    unittest.main()
