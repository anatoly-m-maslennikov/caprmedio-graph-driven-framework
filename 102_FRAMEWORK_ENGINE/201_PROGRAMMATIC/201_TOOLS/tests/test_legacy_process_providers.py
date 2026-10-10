"""Fenced provider coverage refuses caller-shaped legacy process evidence."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from legacy_process_providers import (  # noqa: E402
    FencedLegacyProcessProvider,
    LegacyProcessAdmission,
    LegacyProcessCoverageError,
    PROVIDERS,
    collect_provider_coverage,
    dormant_predecessor_is_absent,
    fenced_legacy_process_providers,
    recollect_provider_coverage,
)
from legacy_process_coverage import (  # noqa: E402
    LegacyBootstrapSourceProof,
    NativeTargetContextProof,
    open_legacy_process_coverage,
)
import legacy_process_providers as provider_module  # noqa: E402


class Fence:
    def __init__(self):
        self.calls = 0
        self.fail_after = None

    def revalidate(self):
        self.calls += 1
        if self.fail_after is not None and self.calls > self.fail_after:
            raise RuntimeError("fence changed")


class LegacyProcessProviderTests(unittest.TestCase):
    def setUp(self):
        self.root = TOOLS.parents[2]
        self.fence = Fence()
        self.admission = LegacyProcessAdmission(
            project_root=self.root,
            project_instance_id="1" * 64,
            target_context_sha256="2" * 64,
            prior_target_context_sha256="a" * 64,
            prior_selector_bytes=b"physically-reopened-prior-selector",
            fence=self.fence,
        )

    @staticmethod
    def complete_absent(*_):
        return {"outcome": "complete", "records": []}

    def providers(self, query=None):
        return {name: query or self.complete_absent for name in PROVIDERS}

    @staticmethod
    def legacy_proof() -> LegacyBootstrapSourceProof:
        def digest(value: str) -> str:
            return hashlib.sha256(value.encode("utf-8")).hexdigest()

        return LegacyBootstrapSourceProof(
            framework_selector_bytes=b"[framework]\nversion = 'legacy'\n",
            tool_selector_bytes=b"[tool]\npackage = 'legacy'\n",
            package_manifest_sha256=digest("retained package manifest"),
            source_context_sha256=digest("retained source context"),
            image_digest="sha256:" + digest("retained image"),
            bootstrap_proof_key=digest("canonical bootstrap proof key"),
            raw_receipt_bytes=b"canonical bootstrap evidence receipt\n",
        )

    def record(self, provider, **overrides):
        value = {
            "owned_subtree": provider,
            "pid": 77,
            "state_generation": "legacy-generation-1",
            "observed_start_token": "actual-provider-start-token",
            "command": {
                "sha256": "4" * 64,
                "environment_sha256": "5" * 64,
                "wrapper_sha256": "6" * 64,
                "argv": ["uv", "run", "server.py"],
                "invocation_nonce": "actual-provider-invocation",
            },
            "release": {
                "package_manifest_sha256": "7" * 64,
                "framework_version": "0.4.1",
                "version_carrier_sha256": "8" * 64,
                "source_catalog_sha256": "9" * 64,
                "full_gate_receipt_sha256": "b" * 64,
                "image_digest": "sha256:" + "c" * 64,
                "target_context_sha256": self.admission.prior_target_context_sha256,
                "selector_sha256": self.admission.prior_selector_sha256,
            },
            "shutdown": {
                "requested": True,
                "response": "acknowledged",
                "deadline_status": "within-deadline",
                "verified_exit": True,
            },
        }
        value.update(overrides)
        return value

    def observed_providers(self, record_factory=None):
        factory = record_factory or self.record
        return {
            name: (lambda *_args, name=name: {
                "outcome": "complete", "records": [factory(name)],
            })
            for name in PROVIDERS
        }

    def test_all_three_completed_empty_queries_prove_only_dormant_predecessor(self):
        coverage = collect_provider_coverage(self.admission, providers=self.providers())

        self.assertEqual(list(PROVIDERS), [row["provider"] for row in coverage])
        self.assertEqual(["absent", "absent", "absent"], [row["state"] for row in coverage])
        self.assertTrue(dormant_predecessor_is_absent(coverage, self.admission))
        self.assertGreaterEqual(self.fence.calls, 7)
        self.assertEqual(
            hashlib.sha256(b"physically-reopened-prior-selector").hexdigest(),
            self.admission.prior_selector_sha256,
        )
        self.assertFalse(hasattr(self.admission, "command_sha256"))
        self.assertFalse(hasattr(self.admission, "start_token"))

    def test_empty_or_missing_provider_result_is_unknown_not_absent(self):
        providers = self.providers()
        providers["mcp_hot_reload"] = lambda *_: {"outcome": "unavailable", "records": []}

        coverage = collect_provider_coverage(self.admission, providers=providers)

        self.assertEqual("unknown", coverage[1]["state"])
        self.assertFalse(dormant_predecessor_is_absent(coverage, self.admission))

    def test_nonempty_roster_requires_sealed_identity_and_verified_shutdown(self):
        providers = self.observed_providers()
        coverage = collect_provider_coverage(self.admission, providers=providers)
        self.assertEqual(["observed", "observed", "observed"], [row["state"] for row in coverage])

        # Old flat/shared fields cannot turn a raw live candidate into an
        # observed predecessor after query-only admission removes them.
        providers = self.providers(lambda *_: {
            "outcome": "complete",
            "records": [{"pid": 77, "command_sha256": "4" * 64}],
        })
        coverage = collect_provider_coverage(self.admission, providers=providers)
        self.assertEqual(["unknown", "unknown", "unknown"], [row["state"] for row in coverage])

        def prospective_release(name):
            record = self.record(name)
            record["release"] = {
                **record["release"],
                "target_context_sha256": self.admission.target_context_sha256,
            }
            return record

        providers = self.observed_providers(prospective_release)
        coverage = collect_provider_coverage(self.admission, providers=providers)
        self.assertEqual(["unknown", "unknown", "unknown"], [row["state"] for row in coverage])

        providers = self.observed_providers(
            lambda name: self.record(name, shutdown={"requested": True}),
        )
        coverage = collect_provider_coverage(self.admission, providers=providers)
        self.assertEqual(["unknown", "unknown", "unknown"], [row["state"] for row in coverage])

    def test_fence_loss_or_reopened_roster_change_cannot_cross_copy_switch(self):
        coverage = collect_provider_coverage(self.admission, providers=self.providers())
        changed = self.observed_providers()
        with self.assertRaisesRegex(LegacyProcessCoverageError, "coverage changed"):
            recollect_provider_coverage(self.admission, coverage, providers=changed)

        self.fence.fail_after = self.fence.calls
        coverage = collect_provider_coverage(self.admission, providers=self.providers())
        self.assertEqual(["unknown", "unknown", "unknown"], [row["state"] for row in coverage])

    def test_opaque_coverage_reopens_the_actual_provider_adapters_under_one_admission(self):
        class PhysicalFence:
            def __init__(self):
                self.closed = False
            def snapshot(self, _deadline):
                return {"outcome": "complete", "records": []}
            def close(self):
                self.closed = True

        opened = []
        def open_test_fence(*_args):
            value = PhysicalFence()
            opened.append(value)
            return value
        with patch.object(provider_module, "_open_provider_fence", side_effect=open_test_fence):
            providers = fenced_legacy_process_providers(self.admission)
            self.assertTrue(all(isinstance(provider, FencedLegacyProcessProvider) for provider in providers))
            with open_legacy_process_coverage(
                providers,
                target_context_sha256=self.admission.target_context_sha256,
                prior_target_context_sha256=self.admission.prior_target_context_sha256,
                prior_selector_sha256=self.admission.prior_selector_sha256,
            ) as coverage:
                self.assertEqual(["absent", "absent", "absent"], [row["state"] for row in coverage.retained_rows()])
                coverage.revalidate()
        self.assertTrue(all(item.closed for item in opened))
        with self.assertRaises(TypeError):
            fenced_legacy_process_providers(self.admission, queries=self.providers())  # type: ignore[call-arg]

    def test_unavailable_physical_provider_is_unknown_not_an_open_coverage_failure(self):
        with patch.object(provider_module, "_open_provider_fence", side_effect=RuntimeError("busy")):
            with open_legacy_process_coverage(
                fenced_legacy_process_providers(self.admission),
                target_context_sha256=self.admission.target_context_sha256,
                prior_target_context_sha256=self.admission.prior_target_context_sha256,
                prior_selector_sha256=self.admission.prior_selector_sha256,
            ) as coverage:
                self.assertEqual(["unknown", "unknown", "unknown"],
                                 [row["state"] for row in coverage.retained_rows()])

    def test_provider_held_completed_queries_bind_legacy_bootstrap_proof(self):
        class PhysicalFence:
            def __init__(self):
                self.closed = False

            def snapshot(self, _deadline):
                return {"outcome": "complete", "records": []}

            def close(self):
                self.closed = True

        proof = self.legacy_proof()
        admission = LegacyProcessAdmission(
            project_root=self.root,
            project_instance_id="1" * 64,
            target_context_sha256="2" * 64,
            fence=Fence(),
            predecessor_proof=proof,
        )
        opened = []

        def open_test_fence(*_args):
            physical = PhysicalFence()
            opened.append(physical)
            return physical

        with patch.object(provider_module, "_open_provider_fence", side_effect=open_test_fence):
            with open_legacy_process_coverage(
                fenced_legacy_process_providers(admission),
                target_context_sha256=admission.target_context_sha256,
                predecessor_proof=proof,
            ) as coverage:
                rows = coverage.retained_rows()
                self.assertEqual(["absent", "absent", "absent"], [row["state"] for row in rows])
                self.assertTrue(all("prior_target_context_sha256" not in row for row in rows))
                self.assertTrue(all(row["predecessor_kind"] == "legacy_bootstrap_source_proof" for row in rows))
                coverage.revalidate()
        self.assertTrue(all(item.closed for item in opened))

    def test_provider_held_completed_queries_allow_equal_native_contexts(self):
        class PhysicalFence:
            def snapshot(self, _deadline):
                return {"outcome": "complete", "records": []}

            def close(self):
                return None

        context = "2" * 64
        proof = NativeTargetContextProof(
            execution_selector_bytes=b"[native]\nselector = 'old-package'\n",
            prior_target_context_sha256=context,
        )
        admission = LegacyProcessAdmission(
            project_root=self.root,
            project_instance_id="1" * 64,
            target_context_sha256=context,
            fence=Fence(),
            predecessor_proof=proof,
        )
        with patch.object(provider_module, "_open_provider_fence", return_value=PhysicalFence()):
            with open_legacy_process_coverage(
                fenced_legacy_process_providers(admission),
                target_context_sha256=context,
                predecessor_proof=proof,
            ) as coverage:
                rows = coverage.retained_rows()
                self.assertEqual(["absent", "absent", "absent"], [row["state"] for row in rows])
                self.assertEqual([context] * 3, [row["prior_target_context_sha256"] for row in rows])


if __name__ == "__main__":
    unittest.main()
