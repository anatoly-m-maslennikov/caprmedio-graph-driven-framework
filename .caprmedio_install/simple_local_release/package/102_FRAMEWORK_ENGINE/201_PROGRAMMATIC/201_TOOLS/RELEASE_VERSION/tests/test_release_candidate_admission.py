"""Private candidate admission does not mutate or inherit Project catalogs."""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path


TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

import test_release_stage_preparation as stage_fixture  # noqa: E402
import release_actions as actions  # noqa: E402
import release_version as native  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_checkpoint import dump_release_checkpoint, restore_release_action_checkpoint  # noqa: E402
from release_portable_contract import revalidate_sealed_portable_compilation, seal_portable_source_snapshot  # noqa: E402
from source_catalog_admission import (  # noqa: E402
    SourceCatalogAdmissionError, TrustedSourceAdmissionInvocation,
    admit_package_sources, read_source_admission_receipt,
)


class ReleaseCandidateAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = stage_fixture.ReleaseStagePreparationTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.checkpoints = []
        # A legitimate existing catalog for an earlier frontier deliberately
        # differs from the new complete active/defaults-only candidate.
        self.fixture.fixture._write_catalog(workspace=".prior-admission")
        self.original = self.root_admission_bytes()
        for payload in self.original.values():
            if payload.startswith(b'{'):
                read_source_admission_receipt(payload)

    def root_admission_bytes(self):
        paths = [self.root / "catalog.toml", *(self.root / "admissions").glob("*.json")]
        return {path.relative_to(self.root).as_posix(): path.read_bytes() for path in paths}

    def stage(self, run_id):
        self.fixture.request = native.prepare_release_request(
            self.root, {"operation": "apply", "project_root": str(self.root)},
        )
        self.fixture.run = actions.begin_release_action_run(
            self.fixture.request, workflow_run_id=run_id,
            checkpoint_callback=lambda run: self.checkpoints.append(dump_release_checkpoint(run)),
        )
        self.assertEqual(self.fixture.execute(0).outcome, "completed")
        self.fixture.bind_stage_session()
        result = self.fixture.execute(1)
        self.assertEqual(result.outcome, "completed", result.reason)
        self.assertEqual(self.root_admission_bytes(), self.original)
        return self.fixture.run

    def test_two_fresh_native_runs_publish_distinct_private_admissions_preserving_root_bytes(self) -> None:
        runs = [self.stage("private-admission-1"), self.stage("private-admission-2")]
        receipts = []
        for run in runs:
            private_root = self.root / ".caprmedio_tmp/release_candidates" / run.workflow_run_id
            self.assertTrue((private_root / "catalog.toml").is_file())
            rows = run.portable_compilation.portable_package_rows
            catalog = next(row for row in rows if row.resource == "CATALOG")
            self.assertEqual(catalog.source_path, (private_root / "catalog.toml").relative_to(self.root).as_posix())
            self.assertEqual(catalog.destination_path, "catalog.toml")
            admissions = [row for row in rows if row.resource == "SOURCE_ADMISSION"]
            self.assertEqual(len(admissions), 1)
            for row in admissions:
                source = self.root / row.source_path
                self.assertEqual(source.parent, private_root / "admissions")
                self.assertEqual(row.destination_path, f"admissions/{source.name}")
                receipt = read_source_admission_receipt(source.read_bytes())
                self.assertEqual(receipt.action_run_id, f"{run.workflow_run_id}:step:2:action:1")
                self.assertEqual(receipt.sha256, hashlib.sha256(source.read_bytes()).hexdigest())
                receipts.append(receipt.sha256)
            self.assertEqual(revalidate_sealed_portable_compilation(run.portable_compilation), run.portable_compilation)
            restored = restore_release_action_checkpoint(canonical_json(dump_release_checkpoint(run)))
            self.assertEqual(restored.portable_compilation, run.portable_compilation)
            self.assertEqual(restored.prepared_portable_package, run.prepared_portable_package)
            self.assertIsNone(run.full_gate)
            self.assertIsNone(run.promotion)
        self.assertNotEqual(receipts[0], receipts[1])
        self.assertEqual(self.root_admission_bytes(), self.original)

    def test_arbitrary_or_symlink_publication_roots_refuse_without_new_outputs(self) -> None:
        run = self.stage("private-admission-safe")
        snapshot = run.portable_source_snapshot
        arbitrary = self.root / "caller-output"
        alias = self.root / ".caprmedio_tmp/release_candidates/alias"
        alias.symlink_to(alias.parent / run.workflow_run_id, target_is_directory=True)
        invoked = []

        def invocation(request):
            invoked.append(request)
            return TrustedSourceAdmissionInvocation(request.snapshot_sha256, "fixture", "fixture", "fixture")

        for target in (arbitrary, alias):
            with self.subTest(target=target.name):
                with self.assertRaises(SourceCatalogAdmissionError):
                    admit_package_sources(self.root, snapshot, invocation_admitter=invocation, publication_root=target)
                with self.assertRaises(ReleaseContractError):
                    seal_portable_source_snapshot(snapshot, publication_root=target)
        self.assertFalse(invoked)
        self.assertFalse(arbitrary.exists())
        self.assertTrue(alias.is_symlink())
        self.assertEqual(self.root_admission_bytes(), self.original)

    def test_changed_candidate_catalog_or_receipt_refuses_revalidation_not_root_fallback(self) -> None:
        run = self.stage("private-admission-drift")
        rows = run.portable_compilation.portable_package_rows
        for row in rows:
            if row.resource not in {"CATALOG", "SOURCE_ADMISSION"}:
                continue
            path = self.root / row.source_path
            original = path.read_bytes()
            try:
                with self.subTest(resource=row.resource):
                    path.write_bytes(original + b"\n")
                    with self.assertRaises(ReleaseContractError):
                        revalidate_sealed_portable_compilation(run.portable_compilation)
                    self.assertEqual(self.root_admission_bytes(), self.original)
            finally:
                path.write_bytes(original)
        self.assertEqual(revalidate_sealed_portable_compilation(run.portable_compilation), run.portable_compilation)


if __name__ == "__main__":
    unittest.main()
