"""D607v4 native-process quiescence is retained without a legacy inventory."""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import installation_state as state  # noqa: E402
from installation_state import InstallationStateError  # noqa: E402
from installation_transaction import InstallationPublicationLock, InstallationTransactionError  # noqa: E402
from legacy_process_coverage import (  # noqa: E402
    LegacyProcessCoverage,
    NativeTargetContextProof,
    ProviderCoverageEvidence,
    open_legacy_process_coverage,
)


def _sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class _ProviderHandle:
    """Physical-fixture provider handle: its snapshot is re-opened each time."""

    def __init__(self, provider: "_Provider") -> None:
        self._provider = provider
        self.owned_subtree = provider.owned_subtree
        self.provider_namespace = provider.provider_namespace
        self.closed = False

    def snapshot(self) -> ProviderCoverageEvidence:
        if self.closed:
            raise RuntimeError("fixture provider handle is closed")
        self._provider.snapshots += 1
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
        proof: NativeTargetContextProof,
        *,
        state_name: str = "absent",
        observations: tuple[dict[str, object], ...] = (),
    ) -> None:
        self.owned_subtree = owned_subtree
        self.provider_namespace = f"fixture://{owned_subtree}/native-project"
        self.state = state_name
        self.observations = observations
        self.evidence: dict[str, object] = {
            "query": "bounded-physical-fixture",
            "matches": [],
            "predecessor_proof": proof.evidence_binding(),
        }
        self.snapshots = 0
        self.closed = 0
        self.openings: list[dict[str, object]] = []

    def open_legacy_process_evidence(self, **bindings: object) -> _ProviderHandle:
        self.openings.append(dict(bindings))
        return _ProviderHandle(self)


class NativeQuiescenceTests(unittest.TestCase):
    def setUp(self) -> None:
        # Retained intentionally: macOS can deny recursive fixture cleanup.
        self.root = Path(tempfile.mkdtemp(prefix="native-quiescence-", dir="/private/tmp"))
        self.target_context = _sha("prospective native target context")
        self.prior_context = _sha("prior native target context")
        self.predecessor = NativeTargetContextProof(
            execution_selector_bytes=b"schema_version = 2\nstate_generation = 4\n",
            prior_target_context_sha256=self.prior_context,
        )

    def _providers(
        self,
        *,
        first_state: str = "absent",
        first_observations: tuple[dict[str, object], ...] = (),
    ) -> list[_Provider]:
        return [
            _Provider("project_mcp", self.predecessor, state_name=first_state, observations=first_observations),
            _Provider("mcp_hot_reload", self.predecessor),
            _Provider("workflow_orchestrator", self.predecessor),
        ]

    def _coverage(
        self,
        providers: list[_Provider],
        *,
        target_context: str | None = None,
        predecessor: NativeTargetContextProof | None = None,
    ) -> LegacyProcessCoverage:
        return open_legacy_process_coverage(
            providers,
            target_context_sha256=target_context or self.target_context,
            predecessor_proof=predecessor or self.predecessor,
        )

    @contextmanager
    def _lock(self):
        lock = InstallationPublicationLock(
            self.root,
            target_context_sha256=self.target_context,
            owner_run_id="native-quiescence-test",
            operation="install_framework_runtime",
            command_sha256=_sha("native quiescence command"),
        ).acquire()
        try:
            yield lock
        finally:
            if lock.active:
                lock.close_uncertain()

    def _retain(
        self,
        coverage: LegacyProcessCoverage,
        lock: InstallationPublicationLock,
        *,
        predecessor: NativeTargetContextProof | None = None,
    ):
        return state.retain_native_quiescence(
            self.root,
            process_coverage=coverage,
            predecessor_proof=predecessor or self.predecessor,
            lock=lock,
        )

    def _read(
        self,
        retained: object,
        coverage: LegacyProcessCoverage,
        lock: InstallationPublicationLock,
        *,
        predecessor: NativeTargetContextProof | None = None,
    ):
        return state.read_native_quiescence(
            self.root,
            retained,
            process_coverage=coverage,
            predecessor_proof=predecessor or self.predecessor,
            lock=lock,
        )

    def _carrier(self, retained: object) -> tuple[Path, dict[str, object]]:
        path = Path(getattr(retained, "path"))
        self.assertTrue(path.is_file())
        self.assertFalse(path.is_symlink())
        self.assertEqual(0o600, path.stat().st_mode & 0o777)
        return path, tomllib.loads(path.read_text(encoding="utf-8"))

    def _assert_no_legacy_inventory(self) -> None:
        self.assertFalse((self.root / ".caprmedio_install").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/installation/migrations").exists())
        self.assertEqual([], list(self.root.rglob("inventory.toml")))

    def _observed_process(self) -> dict[str, object]:
        return {
            "pid": 607,
            "owned_subtree": "project_mcp",
            "state_generation": "native-generation-4",
            "observed_start_token": "native-start-token",
            "command": {
                "sha256": _sha("native command"),
                "argv": ["uv", "run", "implementation_server.py"],
                "environment_sha256": _sha("native environment"),
                "wrapper_sha256": _sha("native wrapper"),
                "invocation_nonce": "native-invocation-nonce",
            },
            "release": {
                "package_manifest_sha256": _sha("native package"),
                "framework_version": "0.4.1",
                "version_carrier_sha256": _sha("native version"),
                "source_catalog_sha256": _sha("native catalog"),
                "full_gate_receipt_sha256": _sha("native gate"),
                "image_digest": "sha256:" + _sha("native image"),
                "target_context_sha256": self.prior_context,
                "selector_sha256": self.predecessor.execution_selector_sha256,
            },
            "shutdown": {
                "requested": True,
                "response": "acknowledged",
                "deadline_status": "within-deadline",
                "verified_exit": True,
            },
        }

    def test_retains_complete_provider_absence_without_legacy_inventory(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            path, document = self._carrier(retained)
            self.assertEqual(
                self.root / ".caprmedio_runtime/installation/quiescence" / lock.lock_generation
                / retained.quiescence_sha256 / "quiescence.toml",
                path,
            )
            self.assertEqual(
                {
                    "schema_version", "kind", "target_context_sha256", "prior_target_context_sha256",
                    "prior_selector_sha256", "installation_lock_generation", "safe",
                    "revalidation_error_code", "quiescence_sha256", "provider_coverage", "processes",
                },
                set(document),
            )
            self.assertEqual(2, document["schema_version"])
            self.assertEqual("native_process_coverage", document["kind"])
            self.assertTrue(retained.safe)
            self.assertEqual("", document["revalidation_error_code"])
            self.assertEqual(["absent", "absent", "absent"], [row["state"] for row in document["provider_coverage"]])
            reopened = self._read(retained, coverage, lock)
            self.assertEqual(retained.path, reopened.path)
            self.assertEqual(retained.quiescence_sha256, reopened.quiescence_sha256)
            self.assertTrue(reopened.safe)
        self._assert_no_legacy_inventory()
        self.assertTrue(all(provider.snapshots >= 3 for provider in providers))

    def test_stable_unknown_is_retained_false_before_the_caller_blocks_effects(self) -> None:
        providers = self._providers(first_state="unknown")
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            _path, document = self._carrier(retained)
            self.assertFalse(retained.safe)
            self.assertFalse(document["safe"])
            self.assertEqual("", document["revalidation_error_code"])
            self.assertEqual("unknown", document["provider_coverage"][0]["state"])
            self.assertFalse(self._read(retained, coverage, lock).safe)
        self._assert_no_legacy_inventory()

    def test_observed_shutdown_uses_existing_process_status_decision(self) -> None:
        providers = self._providers(first_state="observed", first_observations=(self._observed_process(),))
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            _path, document = self._carrier(retained)
            self.assertTrue(retained.safe)
            self.assertEqual(["proven-quiescent"], [row["status"] for row in document["processes"]])
            self.assertIn("shutdown", document["processes"][0]["reason"])

    def test_changed_revalidation_persists_a_false_failure_without_fresh_assertion(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            providers[0].evidence["matches"] = ["changed-after-fence"]
            retained = self._retain(coverage, lock)
            _path, document = self._carrier(retained)
            self.assertFalse(retained.safe)
            self.assertEqual("coverage-changed", document["revalidation_error_code"])
            self.assertEqual(["absent", "absent", "absent"], [row["state"] for row in document["provider_coverage"]])
            original = retained.path.read_bytes()
            with self.assertRaisesRegex(InstallationStateError, "coverage-changed"):
                self._read(retained, coverage, lock)
            self.assertEqual(original, retained.path.read_bytes())

    def test_reader_refuses_closed_coverage(self) -> None:
        providers = self._providers()
        coverage = self._coverage(providers)
        with self._lock() as lock:
            retained = self._retain(coverage, lock)
            coverage.close()
            with self.assertRaises(InstallationStateError):
                self._read(retained, coverage, lock)

    def test_reader_refuses_aliased_quiescence_carrier(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            path, _document = self._carrier(retained)
            target = self.root / "outside-quiescence.toml"
            target.write_bytes(path.read_bytes())
            path.unlink()
            path.symlink_to(target)
            with self.assertRaises(InstallationStateError):
                self._read(retained, coverage, lock)

    def test_reader_refuses_native_carrier_with_noncanonical_mode(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            path, _document = self._carrier(retained)
            path.chmod(0o644)

            with self.assertRaises(InstallationStateError):
                self._read(retained, coverage, lock)
            self.assertEqual(0o644, path.stat().st_mode & 0o777)

    def test_retain_refuses_noncanonical_existing_identical_carrier_mode(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            path, _document = self._carrier(retained)
            path.chmod(0o644)

            with self.assertRaises(InstallationStateError):
                self._retain(coverage, lock)
            self.assertEqual(0o644, path.stat().st_mode & 0o777)

    def test_retain_refuses_symlinked_generation_ancestor_before_existing_carrier_read(self) -> None:
        reference_root = Path(tempfile.mkdtemp(prefix="native-quiescence-reference-", dir="/private/tmp"))
        with self._lock() as lock:
            reference_lock = InstallationPublicationLock(
                reference_root,
                target_context_sha256=self.target_context,
                owner_run_id="native-quiescence-test",
                operation="install_framework_runtime",
                command_sha256=_sha("native quiescence command"),
            )
            # The reference derives its generation from the active target lock;
            # retention is otherwise a separate physical Project fixture.
            reference_lock.lock_generation = lock.lock_generation
            reference_lock._record["lock_generation"] = lock.lock_generation
            reference_lock.acquire()
            try:
                reference_providers = self._providers()
                with self._coverage(reference_providers) as reference_coverage:
                    reference_retained = state.retain_native_quiescence(
                        reference_root,
                        process_coverage=reference_coverage,
                        predecessor_proof=self.predecessor,
                        lock=reference_lock,
                    )
            finally:
                if reference_lock.active:
                    reference_lock.close_uncertain()

            quiescence_root = self.root / ".caprmedio_runtime/installation/quiescence"
            quiescence_root.mkdir()
            generation = quiescence_root / lock.lock_generation
            generation.symlink_to(reference_retained.path.parent.parent, target_is_directory=True)
            seeded = generation / reference_retained.quiescence_sha256 / "quiescence.toml"
            self.assertEqual(reference_retained.path.read_bytes(), seeded.read_bytes())

            providers = self._providers()
            with self._coverage(providers) as coverage:
                with self.assertRaises(InstallationStateError):
                    self._retain(coverage, lock)

    def test_reader_refuses_self_consistent_float_schema_version(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            path, document = self._carrier(retained)
            document["schema_version"] = 2.0
            document["quiescence_sha256"] = hashlib.sha256(
                state.canonical_json(
                    {key: value for key, value in document.items() if key != "quiescence_sha256"}
                ).encode("utf-8")
            ).hexdigest()
            original = path.read_text(encoding="utf-8")
            tampered = original.replace("schema_version = 2\n", "schema_version = 2.0\n", 1).replace(
                retained.quiescence_sha256,
                document["quiescence_sha256"],
                1,
            )
            self.assertNotEqual(original, tampered)
            path.write_text(tampered, encoding="utf-8")

            with self.assertRaises(InstallationStateError):
                self._read(retained, coverage, lock)

    def test_reader_refuses_physical_row_and_digest_tampering(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            path, _document = self._carrier(retained)
            original = path.read_text(encoding="utf-8")
            tampered = (
                original.replace('kind = "native_process_coverage"', 'kind = "forged"'),
                original.replace('state = "absent"', 'state = "unknown"', 1),
                original.replace(retained.quiescence_sha256, "0" * 64),
            )
            for payload in tampered:
                with self.subTest(payload=payload[:48]):
                    path.write_text(payload, encoding="utf-8")
                    with self.assertRaises(InstallationStateError):
                        self._read(retained, coverage, lock)
                    path.write_text(original, encoding="utf-8")

    def test_reader_refuses_lock_context_and_prior_proof_tampering(self) -> None:
        providers = self._providers()
        with self._coverage(providers) as coverage, self._lock() as lock:
            retained = self._retain(coverage, lock)
            with self.assertRaises(InstallationStateError):
                self._read(retained, coverage, object())

            lock_bytes = lock.lock_path.read_bytes()
            lock.lock_path.write_bytes(b"schema_version = 1\n")
            with self.assertRaises(InstallationTransactionError):
                self._read(retained, coverage, lock)
            lock.lock_path.write_bytes(lock_bytes)

            forged_prior = NativeTargetContextProof(
                execution_selector_bytes=b"schema_version = 2\nstate_generation = 99\n",
                prior_target_context_sha256=_sha("forged native prior context"),
            )
            with self.assertRaises(InstallationStateError):
                self._read(retained, coverage, lock, predecessor=forged_prior)

            foreign_providers = self._providers()
            with self._coverage(foreign_providers, target_context=_sha("foreign prospective target")) as foreign_coverage:
                with self.assertRaises(InstallationStateError):
                    self._retain(foreign_coverage, lock)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
