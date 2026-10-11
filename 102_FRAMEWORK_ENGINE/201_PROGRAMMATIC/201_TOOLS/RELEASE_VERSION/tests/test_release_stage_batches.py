"""Real staging scans stay bounded; undeclared inputs never become support."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

import test_release_stage_preparation as stage_fixture  # noqa: E402
import release_actions as actions  # noqa: E402
import release_version as native  # noqa: E402


class ReleaseStageBatchTests(unittest.TestCase):
    def test_real_native_preparation_and_staging_exclude_engine_transient_cache_without_waiver(self) -> None:
        fixture = stage_fixture.ReleaseStagePreparationTests("run")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        before = fixture.protected_bytes()
        frozen_before_cache = fixture.request
        cache = fixture.root / "102_FRAMEWORK_ENGINE/.caprmedio_tmp/cache"
        cache.mkdir(parents=True)
        external = fixture.root / "external-tool-cache"
        external.mkdir()
        (external / "cached.txt").write_bytes(b"not a product input\n")
        (cache / "uv").symlink_to(external, target_is_directory=True)
        fixture.request = native.prepare_release_request(
            fixture.root, {"operation": "apply", "project_root": str(fixture.root)},
        )
        self.assertEqual(fixture.request, frozen_before_cache)
        fixture.run = actions.begin_release_action_run(
            fixture.request, workflow_run_id="stage-current-active", checkpoint_callback=lambda run: None,
        )
        self.assertEqual(fixture.execute(0).outcome, "completed")
        fixture.bind_stage_session()
        result = fixture.execute(1)
        self.assertEqual(result.outcome, "completed", result.reason)
        self.assertIsNotNone(fixture.run.private_compilation)
        self.assertIsNotNone(fixture.run.prepared_portable_package)
        self.assertEqual(fixture.protected_bytes(), before)
        self.assertIsNone(fixture.run.full_gate)
        self.assertIsNone(fixture.run.promotion)
        self.assertTrue((cache / "uv").is_symlink())

    def test_real_preparation_metadata_scan_count_does_not_grow_with_undeclared_inventory(self) -> None:
        counts = []
        for size in (4, 128):
            with self.subTest(undeclared_files=size):
                fixture = stage_fixture.ReleaseStagePreparationTests("run")
                fixture.setUp()
                self.addCleanup(fixture.doCleanups)
                for index in range(size):
                    fixture.fixture.write(
                        f"{stage_fixture.CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/bulk/item-{index:03}.json",
                        f"{{\"item\":{index}}}\n".encode(),
                    )
                fixture.request = native.prepare_release_request(
                    fixture.root, {"operation": "apply", "project_root": str(fixture.root)},
                )
                fixture.run = actions.begin_release_action_run(
                    fixture.request, workflow_run_id="stage-current-active",
                    checkpoint_callback=lambda run: None,
                )
                self.assertEqual(fixture.execute(0).outcome, "completed")
                fixture.bind_stage_session()
                actual_exporter = actions._exporter_module()
                with patch.object(actions, "_exporter_module", return_value=actual_exporter), \
                     patch.object(actual_exporter, "_guard_source_metadata", wraps=actual_exporter._guard_source_metadata) as guard:
                    result = fixture.execute(1)
                self.assertEqual(result.outcome, "completed", result.reason)
                counts.append(guard.call_count)
                sealed = actual_exporter.read_sealed_export(release_candidate_root=fixture.candidate_root)
                self.assertEqual(sealed.support_count, 1)
                self.assertEqual([row["path"] for row in sealed.inventory["support"]],
                                 [actual_exporter.compiler.DEFAULT_SETTINGS_RELATIVE.as_posix()])
                exported = fixture.candidate_root / "methodology/003_PROJECT_CONFIGURATION/bulk"
                self.assertFalse(exported.exists())
                self.assertEqual(sealed.atom_count, 2)
                self.assertIsNone(fixture.run.full_gate)
                self.assertIsNone(fixture.run.promotion)
        self.assertEqual(counts[0], counts[1], f"full metadata scans scaled with inventory: {counts}")
        self.assertGreater(counts[0], 0)
        self.assertLess(counts[1], 64)


if __name__ == "__main__":
    unittest.main()
