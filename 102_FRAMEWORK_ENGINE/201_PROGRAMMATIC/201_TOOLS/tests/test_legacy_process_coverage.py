"""D607 provider-held process-coverage fixtures; no process is started."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from installation_state import (  # noqa: E402
    InstallationStateError,
    build_legacy_inventory,
    prove_quiescence,
    read_inventory,
    read_quiescence,
    stage_legacy_copy,
    write_inventory,
    write_quiescence,
)
from installation_transaction import installation_publication_lock  # noqa: E402
from legacy_process_coverage import (  # noqa: E402
    LegacyBootstrapSourceProof,
    LegacyProcessCoverageError,
    NativeTargetContextProof,
    ProviderCoverageEvidence,
    open_legacy_process_coverage,
    validate_retained_coverage_rows,
)


def _sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class _Handle:
    def __init__(self, provider: "_Provider") -> None:
        self._provider = provider
        self.owned_subtree = provider.owned_subtree
        self.provider_namespace = provider.provider_namespace
        self.closed = False

    def snapshot(self) -> ProviderCoverageEvidence:
        if self.closed:
            raise RuntimeError("released handle")
        self._provider.queries += 1
        if self._provider.failure:
            raise RuntimeError("provider unavailable")
        return ProviderCoverageEvidence(
            state=self._provider.state,
            namespace=self.provider_namespace,
            evidence=dict(self._provider.evidence),
            observations=tuple(dict(row) for row in self._provider.observations),
        )

    def close(self) -> None:
        self.closed = True
        self._provider.closed += 1


class _Provider:
    def __init__(
        self,
        owned_subtree: str,
        *,
        state: str = "absent",
        observations: tuple[dict[str, object], ...] = (),
    ) -> None:
        self.owned_subtree = owned_subtree
        self.provider_namespace = f"fixture://{owned_subtree}/selected-project"
        self.state = state
        self.observations = observations
        self.evidence: dict[str, object] = {"query": "physical-fixture", "matches": []}
        self.failure = False
        self.queries = 0
        self.closed = 0

    def open_legacy_process_evidence(self, **_bindings: str) -> _Handle:
        return _Handle(self)


class LegacyProcessCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(dir="/private/tmp"))
        self.target_context = _sha("prospective target context")
        self.prior_context = _sha("prior native context")
        self.prior_selector = _sha("prior execution selector")
        self.command = _sha("installation command")
        selector = self.root / ".caprmedio_install" / "current.toml"
        selector.parent.mkdir()
        selector.write_text('schema_version = 1\nrelease = "legacy"\n', encoding="utf-8")
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            state = selector.parent / name / "state.bin"
            state.parent.mkdir()
            state.write_bytes(name.encode("utf-8"))

    def _providers(self, *, first: _Provider | None = None) -> list[_Provider]:
        return [
            first or _Provider("project_mcp"),
            _Provider("mcp_hot_reload"),
            _Provider("workflow_orchestrator"),
        ]

    def _coverage(self, providers: list[_Provider]):
        return open_legacy_process_coverage(
            providers,
            target_context_sha256=self.target_context,
            prior_target_context_sha256=self.prior_context,
            prior_selector_sha256=self.prior_selector,
        )

    def _legacy_proof(self) -> LegacyBootstrapSourceProof:
        return LegacyBootstrapSourceProof(
            framework_selector_bytes=b"[framework]\nversion = 'legacy'\n",
            tool_selector_bytes=b"[tool]\npackage = 'legacy'\n",
            package_manifest_sha256=_sha("retained bootstrap package manifest"),
            source_context_sha256=_sha("retained bootstrap source context"),
            image_digest="sha256:" + _sha("retained bootstrap image"),
            bootstrap_proof_key=_sha("retained bootstrap proof key"),
            raw_receipt_bytes=b"canonical retained bootstrap receipt\n",
        )

    def _lock(self):
        return installation_publication_lock(
            self.root,
            target_context_sha256=self.target_context,
            owner_run_id="coverage-test",
            operation="legacy-migration",
            command_sha256=self.command,
        )

    def _inventory(self, coverage):
        return build_legacy_inventory(
            self.root,
            migration_id="coverage-test",
            target_context_sha256=self.target_context,
            process_coverage=coverage,
            prior_execution_context_sha256=self.prior_context,
            prior_execution_selector_sha256=self.prior_selector,
        )

    def test_complete_provider_verified_absence_is_safe_and_persisted(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage:
            inventory = self._inventory(coverage)
            proof = prove_quiescence(inventory, process_coverage=coverage)
            self.assertTrue(proof["safe"])
            self.assertEqual([], proof["processes"])
            self.assertEqual(
                ["absent", "absent", "absent"], [row["state"] for row in proof["provider_coverage"]]
            )
            with self._lock() as lock:
                write_inventory(self.root, inventory, lock=lock)
                write_quiescence(self.root, inventory, proof, lock=lock)
                self.assertEqual(inventory, read_inventory(self.root, "coverage-test"))
                self.assertEqual(proof, read_quiescence(self.root, inventory))
                staged = stage_legacy_copy(self.root, inventory, proof, lock=lock, process_coverage=coverage)
                self.assertIn("project_mcp/state.bin", staged["rows"])
                lock.release("partial")
        self.assertTrue(all(provider.queries >= 4 for provider in providers))
        self.assertEqual([1, 1, 1], [provider.closed for provider in providers])

    def test_precoverage_schema_one_inventory_stays_readable(self) -> None:
        inventory = build_legacy_inventory(
            self.root,
            migration_id="legacy-schema-one",
            target_context_sha256=self.target_context,
        )
        self.assertNotIn("provider_coverage", inventory)
        with self._lock() as lock:
            write_inventory(self.root, inventory, lock=lock)
            self.assertEqual(inventory, read_inventory(self.root, "legacy-schema-one"))
            lock.release("partial")

    def test_missing_duplicate_or_out_of_order_provider_is_refused(self) -> None:
        with self.assertRaisesRegex(LegacyProcessCoverageError, "coverage-incomplete"):
            self._coverage(self._providers()[:2])
        duplicate = [_Provider("project_mcp"), _Provider("project_mcp"), _Provider("workflow_orchestrator")]
        with self.assertRaisesRegex(LegacyProcessCoverageError, "coverage-order-invalid"):
            self._coverage(duplicate)
        reversed_providers = list(reversed(self._providers()))
        with self.assertRaisesRegex(LegacyProcessCoverageError, "coverage-order-invalid"):
            self._coverage(reversed_providers)

    def test_query_error_and_noncoverage_input_are_refused(self) -> None:
        providers = self._providers()
        providers[1].failure = True
        with self.assertRaisesRegex(LegacyProcessCoverageError, "coverage-query-failed"):
            self._coverage(providers)
        with self.assertRaisesRegex(InstallationStateError, "process-coverage-invalid"):
            build_legacy_inventory(
                self.root,
                migration_id="invalid-coverage",
                target_context_sha256=self.target_context,
                process_coverage=object(),  # type: ignore[arg-type]
                prior_execution_context_sha256=self.prior_context,
                prior_execution_selector_sha256=self.prior_selector,
            )

    def test_pid_only_observation_is_not_quiescent(self) -> None:
        pid_only = {"pid": 1234, "owned_subtree": "project_mcp"}
        providers = self._providers(first=_Provider("project_mcp", state="observed", observations=(pid_only,)))
        with self._coverage(providers) as coverage:
            proof = prove_quiescence(self._inventory(coverage), process_coverage=coverage)
        self.assertFalse(proof["safe"])
        self.assertEqual("pid-proof-insufficient", proof["processes"][0]["status"])

    def test_unknown_provider_coverage_is_retained_but_blocks_copy(self) -> None:
        providers = self._providers(first=_Provider("project_mcp", state="unknown"))
        with self._coverage(providers) as coverage:
            inventory = self._inventory(coverage)
            proof = prove_quiescence(inventory, process_coverage=coverage)
            self.assertFalse(proof["safe"])
            with self._lock() as lock:
                write_inventory(self.root, inventory, lock=lock)
                write_quiescence(self.root, inventory, proof, lock=lock)
                with self.assertRaisesRegex(InstallationStateError, "migration-quiescence-blocked"):
                    stage_legacy_copy(self.root, inventory, proof, lock=lock, process_coverage=coverage)
                lock.release("blocked")

    def test_observed_predecessor_uses_prior_not_prospective_context(self) -> None:
        observation = {
            "pid": 1234,
            "owned_subtree": "project_mcp",
            "state_generation": "old-generation",
            "observed_start_token": "old-start-token",
            "command": {
                "sha256": _sha("old command"),
                "argv": ["TOOLS/server.py"],
                "environment_sha256": _sha("old environment"),
                "wrapper_sha256": _sha("old wrapper"),
                "invocation_nonce": "old-nonce",
            },
            "release": {
                "package_manifest_sha256": _sha("old package"),
                "framework_version": "0.4.1",
                "version_carrier_sha256": _sha("old version"),
                "source_catalog_sha256": _sha("old catalog"),
                "full_gate_receipt_sha256": _sha("old gate"),
                "image_digest": "sha256:" + _sha("old image"),
                "target_context_sha256": self.prior_context,
                "selector_sha256": self.prior_selector,
            },
            "shutdown": {"requested": True, "response": "acknowledged", "deadline_status": "within-deadline"},
        }
        providers = self._providers(first=_Provider("project_mcp", state="observed", observations=(observation,)))
        with self._coverage(providers) as coverage:
            proof = prove_quiescence(self._inventory(coverage), process_coverage=coverage)
        self.assertTrue(proof["safe"])
        self.assertEqual("proven-quiescent", proof["processes"][0]["status"])

    def test_stale_binding_and_coverage_race_are_refused(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage:
            with self.assertRaisesRegex(InstallationStateError, "coverage-binding-stale"):
                build_legacy_inventory(
                    self.root,
                    migration_id="stale-binding",
                    target_context_sha256=self.target_context,
                    process_coverage=coverage,
                    prior_execution_context_sha256=self.prior_context,
                    prior_execution_selector_sha256=_sha("different prior selector"),
                )
            inventory = self._inventory(coverage)
            providers[0].evidence["matches"] = ["newly-started-runtime"]
            with self.assertRaisesRegex(InstallationStateError, "coverage-changed"):
                prove_quiescence(inventory, process_coverage=coverage)

    def test_bootstrap_predecessor_retains_two_raw_selectors_without_native_context(self) -> None:
        proof = self._legacy_proof()
        providers = self._providers()
        for provider in providers:
            provider.evidence["predecessor_proof"] = proof.evidence_binding()

        with open_legacy_process_coverage(
            providers,
            target_context_sha256=self.target_context,
            predecessor_proof=proof,
        ) as coverage:
            rows = coverage.retained_rows()
            self.assertEqual(["legacy_bootstrap_source_proof"] * 3, [row["predecessor_kind"] for row in rows])
            self.assertTrue(all("prior_target_context_sha256" not in row for row in rows))
            self.assertEqual(
                [proof.framework_selector_sha256] * 3,
                [row["prior_selector_sha256"] for row in rows],
            )
            self.assertEqual(
                proof.evidence_binding(),
                json.loads(str(rows[0]["evidence_json"]))["predecessor_proof"],
            )
            validated = validate_retained_coverage_rows(
                list(rows),
                target_context_sha256=self.target_context,
                predecessor_proof=proof,
            )
            self.assertEqual(rows, validated)

    def test_equal_native_context_is_bound_and_tampered_bootstrap_evidence_is_refused(self) -> None:
        native_proof = NativeTargetContextProof(
            execution_selector_bytes=b"[native]\nselector = 'prior'\n",
            prior_target_context_sha256=self.target_context,
        )
        native_providers = self._providers()
        for provider in native_providers:
            provider.evidence["predecessor_proof"] = native_proof.evidence_binding()
        with open_legacy_process_coverage(
            native_providers,
            target_context_sha256=self.target_context,
            predecessor_proof=native_proof,
        ) as coverage:
            self.assertEqual(
                [self.target_context] * 3,
                [row["prior_target_context_sha256"] for row in coverage.retained_rows()],
            )
        with self.assertRaisesRegex(LegacyProcessCoverageError, "contradicts caller bindings"):
            open_legacy_process_coverage(
                self._providers(),
                target_context_sha256=self.target_context,
                prior_selector_sha256=_sha("forged native selector"),
                predecessor_proof=native_proof,
            )

        proof = self._legacy_proof()
        providers = self._providers()
        for provider in providers:
            provider.evidence["predecessor_proof"] = {
                **proof.evidence_binding(),
                "raw_receipt_sha256": _sha("forged bootstrap receipt"),
            }
        with self.assertRaisesRegex(LegacyProcessCoverageError, "coverage-predecessor-proof-invalid"):
            open_legacy_process_coverage(
                providers,
                target_context_sha256=self.target_context,
                predecessor_proof=proof,
            )

    def test_rehashed_optional_native_proof_cannot_contradict_outer_bindings(self) -> None:
        native_proof = NativeTargetContextProof(
            execution_selector_bytes=b"prior execution selector",
            prior_target_context_sha256=self.prior_context,
        )
        providers = self._providers()
        for provider in providers:
            provider.evidence["predecessor_proof"] = native_proof.evidence_binding()
        with self._coverage(providers) as coverage:
            rows = [dict(row) for row in coverage.retained_rows()]

        forged = NativeTargetContextProof(
            execution_selector_bytes=b"different native selector",
            prior_target_context_sha256=self.prior_context,
        )
        for row in rows:
            evidence = json.loads(str(row["evidence_json"]))
            evidence["predecessor_proof"] = forged.evidence_binding()
            row["evidence_json"] = json.dumps(evidence, sort_keys=True, separators=(",", ":"))
            row["evidence_sha256"] = hashlib.sha256(row["evidence_json"].encode("utf-8")).hexdigest()
        with self.assertRaisesRegex(LegacyProcessCoverageError, "contradicts coverage bindings"):
            validate_retained_coverage_rows(
                rows,
                target_context_sha256=self.target_context,
                prior_target_context_sha256=self.prior_context,
                prior_selector_sha256=self.prior_selector,
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
