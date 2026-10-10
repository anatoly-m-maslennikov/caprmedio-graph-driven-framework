"""Fixture coverage for the retained legacy-installation state carriers."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import installation_state as state  # noqa: E402
from installation_state import (  # noqa: E402
    InstallationStateError,
    build_legacy_inventory,
    prove_quiescence,
    stage_legacy_copy,
    switch_runtime_selector,
    verify_inventory,
    verify_staged_copy,
    write_generation_process_proof,
    write_inventory,
    write_quiescence,
)
from installation_transaction import installation_publication_lock  # noqa: E402
from legacy_process_coverage import (  # noqa: E402
    LegacyBootstrapSourceProof,
    ProviderCoverageEvidence,
    open_legacy_process_coverage,
)


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class _CoverageHandle:
    def __init__(self, provider: "_CoverageProvider") -> None:
        self._provider = provider
        self.owned_subtree = provider.owned_subtree
        self.provider_namespace = provider.provider_namespace

    def snapshot(self) -> ProviderCoverageEvidence:
        return ProviderCoverageEvidence(
            state=self._provider.state,
            namespace=self.provider_namespace,
            evidence=dict(self._provider.evidence),
            observations=tuple(dict(item) for item in self._provider.observations),
        )

    def close(self) -> None:
        return None


class _CoverageProvider:
    def __init__(self, owned_subtree: str, proof: LegacyBootstrapSourceProof, *, observations=()) -> None:
        self.owned_subtree = owned_subtree
        self.provider_namespace = f"fixture://{owned_subtree}"
        self.state = "observed" if observations else "absent"
        self.evidence = {"query": "fixture", "predecessor_proof": proof.evidence_binding()}
        self.observations = observations

    def open_legacy_process_evidence(self, **_bindings: object) -> _CoverageHandle:
        return _CoverageHandle(self)


class InstallationStateTests(unittest.TestCase):
    def setUp(self) -> None:
        # Legacy carriers are intentionally retention-only.  The managed test
        # host also protects those fixture paths from recursive cleanup, so do
        # not ask ``TemporaryDirectory`` to delete them after the assertion.
        self.root = Path(tempfile.mkdtemp(dir="/private/tmp"))
        self.target_context = _digest("target-context")
        self.command = _digest("install-command")
        selector = self.root / ".caprmedio_install" / "current.toml"
        selector.parent.mkdir()
        selector.write_text('schema_version = 1\nrelease = "legacy"\n', encoding="utf-8")
        for name, content, mode in (
            ("project_mcp", b"mcp", 0o640),
            ("mcp_hot_reload", b"reload", 0o600),
            ("workflow_orchestrator", b"workflow", 0o644),
        ):
            carrier = selector.parent / name / "state.bin"
            carrier.parent.mkdir()
            carrier.write_bytes(content)
            carrier.chmod(mode)
        (selector.parent / "unowned_adjacent").mkdir()
        (selector.parent / "unowned_adjacent" / "keep.txt").write_text("keep", encoding="utf-8")

    def _proof(self, *, pid: int = 1234, subtree: str = "project_mcp") -> dict[str, object]:
        return {
            "pid": pid,
            "owned_subtree": subtree,
            "state_generation": "generation-1",
            "observed_start_token": "start-token-1",
            "command": {
                "sha256": self.command,
                "argv": ["TOOLS/START_BACKGROUND_SERVICES/start_background_services.py"],
                "environment_sha256": _digest("environment"),
                "wrapper_sha256": _digest("wrapper"),
                "invocation_nonce": "nonce-1",
            },
            "release": {
                "package_manifest_sha256": _digest("package"),
                "framework_version": "0.4.1",
                "version_carrier_sha256": _digest("version"),
                "source_catalog_sha256": _digest("catalog"),
                "full_gate_receipt_sha256": _digest("gate"),
                "image_digest": "sha256:" + _digest("image"),
                "target_context_sha256": self.target_context,
                "selector_sha256": hashlib.sha256(
                    (self.root / ".caprmedio_install/current.toml").read_bytes()
                ).hexdigest(),
            },
            "shutdown": {
                "requested": True,
                "response": "acknowledged",
                "deadline_status": "within-deadline",
            },
        }

    def _lock(self):
        return installation_publication_lock(
            self.root,
            target_context_sha256=self.target_context,
            owner_run_id="state-test",
            operation="legacy-migration",
            command_sha256=self.command,
        )

    def _legacy_bootstrap_proof(self) -> LegacyBootstrapSourceProof:
        framework = self.root / ".caprmedio_runtime/framework/current.toml"
        framework.parent.mkdir(parents=True, exist_ok=True)
        framework.write_text('schema_version = 1\nrelease = "framework-legacy"\n', encoding="utf-8")
        return LegacyBootstrapSourceProof(
            framework_selector_bytes=framework.read_bytes(),
            tool_selector_bytes=(self.root / ".caprmedio_install/current.toml").read_bytes(),
            package_manifest_sha256=_digest("bootstrap-package"),
            source_context_sha256=_digest("bootstrap-source-context"),
            image_digest="sha256:" + _digest("bootstrap-image"),
            bootstrap_proof_key=_digest("bootstrap-proof-key"),
            raw_receipt_bytes=b"retained bootstrap receipt\n",
        )

    def _legacy_observation(self, proof: LegacyBootstrapSourceProof) -> dict[str, object]:
        release = proof.evidence_binding()
        release.pop("kind")
        return {
            "pid": 4321,
            "owned_subtree": "project_mcp",
            "state_generation": "legacy-generation-1",
            "observed_start_token": "legacy-start-token",
            "command": {
                "sha256": self.command,
                "argv": ["TOOLS/START_BACKGROUND_SERVICES/start_background_services.py"],
                "environment_sha256": _digest("legacy-environment"),
                "wrapper_sha256": _digest("legacy-wrapper"),
                "invocation_nonce": "legacy-nonce",
            },
            "release": release,
            "shutdown": {
                "requested": True,
                "response": "acknowledged",
                "deadline_status": "within-deadline",
            },
        }

    def test_inventory_is_exact_and_staged_copy_preserves_legacy_sources(self) -> None:
        proof = self._proof()
        inventory = build_legacy_inventory(
            self.root,
            migration_id="migration-1",
            target_context_sha256=self.target_context,
            process_observations=[proof],
        )
        self.assertEqual(
            ["project_mcp", "mcp_hot_reload", "workflow_orchestrator"],
            [row["name"] for row in inventory["source_roots"]],
        )
        self.assertNotIn("unowned_adjacent", {row["name"] for row in inventory["source_roots"]})
        quiescence = prove_quiescence(inventory, [proof])
        self.assertTrue(quiescence["safe"])

        with self._lock() as lock:
            write_inventory(self.root, inventory, lock=lock)
            generation = write_generation_process_proof(
                self.root,
                proof,
                state_generation="generation-1",
                target_context_sha256=self.target_context,
                lock=lock,
            )
            staged = stage_legacy_copy(self.root, inventory, quiescence, lock=lock)
            lock.release("partial")

        self.assertTrue((self.root / ".caprmedio_install/project_mcp/state.bin").is_file())
        self.assertTrue((self.root / ".caprmedio_install/unowned_adjacent/keep.txt").is_file())
        self.assertTrue(
            (self.root / ".caprmedio_runtime/installation/migrations/migration-1/staging/runtime/project_mcp/state.bin").is_file()
        )
        self.assertTrue((generation / "release-proof.toml").is_file())
        self.assertTrue((generation / "command.toml").is_file())
        self.assertTrue((generation / "process.toml").is_file())
        self.assertEqual(0o640, staged["rows"]["project_mcp/state.bin"]["mode"])
        verify_staged_copy(self.root, inventory, staged)

    def test_tampered_source_rejects_before_copy(self) -> None:
        inventory = build_legacy_inventory(
            self.root, migration_id="migration-2", target_context_sha256=self.target_context
        )
        (self.root / ".caprmedio_install/mcp_hot_reload/state.bin").write_bytes(b"changed")
        with self.assertRaisesRegex(InstallationStateError, "inventory-changed"):
            verify_inventory(self.root, inventory)

    def test_symlink_and_pid_only_observations_are_blocked(self) -> None:
        target = self.root / "outside"
        target.mkdir()
        os.symlink(target, self.root / ".caprmedio_install/project_mcp/link")
        with self.assertRaisesRegex(InstallationStateError, "legacy-symlink"):
            build_legacy_inventory(self.root, migration_id="migration-3", target_context_sha256=self.target_context)
        (self.root / ".caprmedio_install/project_mcp/link").unlink()

        pid_only = {"pid": 1234, "owned_subtree": "project_mcp"}
        inventory = build_legacy_inventory(
            self.root,
            migration_id="migration-4",
            target_context_sha256=self.target_context,
            process_observations=[pid_only],
        )
        quiescence = prove_quiescence(inventory, [pid_only])
        self.assertFalse(quiescence["safe"])
        self.assertEqual("pid-proof-insufficient", quiescence["processes"][0]["status"])

    def test_protected_name_is_rejected_from_metadata_before_any_payload_read(self) -> None:
        # The managed filesystem denies creating dotenv-shaped fixture paths;
        # exercising the name predicate itself proves the pre-open metadata
        # gate without creating or reading a protected payload.
        self.assertTrue(state._protected_legacy_name("credential.env"))
        self.assertTrue(state._protected_legacy_name(".env.local"))
        self.assertFalse(state._protected_legacy_name("state.toml"))
        protected = self.root / ".caprmedio_install/project_mcp/credential.env"
        original_iterdir = Path.iterdir

        def metadata_children(path: Path):
            if path == protected.parent:
                return iter((protected,))
            return original_iterdir(path)

        with patch.object(Path, "iterdir", new=metadata_children):
            with self.assertRaisesRegex(InstallationStateError, "legacy-protected-name"):
                build_legacy_inventory(
                    self.root, migration_id="migration-protected", target_context_sha256=self.target_context
                )

    def test_full_immutable_binding_tuple_rejects_changed_release_and_command_fields(self) -> None:
        proof = self._proof()
        inventory = build_legacy_inventory(
            self.root,
            migration_id="migration-bindings",
            target_context_sha256=self.target_context,
            process_observations=[proof],
        )
        for section, field in (
            ("release", "package_manifest_sha256"),
            ("release", "selector_sha256"),
            ("release", "source_catalog_sha256"),
            ("command", "environment_sha256"),
            ("command", "wrapper_sha256"),
        ):
            with self.subTest(section=section, field=field):
                changed = dict(proof)
                changed[section] = dict(proof[section], **{field: _digest(f"changed-{section}-{field}")})  # type: ignore[arg-type]
                self.assertFalse(prove_quiescence(inventory, [changed])["safe"])

    def test_forged_safe_quiescence_and_tampered_staged_selector_are_refused(self) -> None:
        pid_only = {"pid": 1234, "owned_subtree": "project_mcp"}
        inventory = build_legacy_inventory(
            self.root,
            migration_id="migration-forged",
            target_context_sha256=self.target_context,
            process_observations=[pid_only],
        )
        forged = prove_quiescence(inventory, [pid_only])
        forged["safe"] = True
        forged["processes"] = []
        forged["quiescence_sha256"] = state._digest({key: value for key, value in forged.items() if key != "quiescence_sha256"})
        with self._lock() as lock:
            write_inventory(self.root, inventory, lock=lock)
            with self.assertRaisesRegex(InstallationStateError, "quiescence-invalid"):
                stage_legacy_copy(self.root, inventory, forged, lock=lock)
            lock.release("blocked")

        clean_inventory = build_legacy_inventory(
            self.root, migration_id="migration-selector", target_context_sha256=self.target_context
        )
        quiescence = prove_quiescence(clean_inventory, [])
        with self._lock() as lock:
            write_inventory(self.root, clean_inventory, lock=lock)
            write_quiescence(self.root, clean_inventory, quiescence, lock=lock)
            staged = stage_legacy_copy(self.root, clean_inventory, quiescence, lock=lock)
            selector = self.root / ".caprmedio_runtime/installation/migrations/migration-selector/staging/selector/current.toml"
            selector.write_text('release = "arbitrary"\n', encoding="utf-8")
            staged["staged_selector_sha256"] = hashlib.sha256(selector.read_bytes()).hexdigest()
            with self.assertRaisesRegex(InstallationStateError, "staged-selector-tampered"):
                switch_runtime_selector(
                    self.root, clean_inventory, staged, state_generation="generation-selector", lock=lock
                )
            lock.release("blocked")

    def test_existing_migration_ancestor_symlink_refuses_write_before_escape(self) -> None:
        inventory = build_legacy_inventory(
            self.root, migration_id="migration-symlink", target_context_sha256=self.target_context
        )
        outside = self.root / "outside-migrations"
        outside.mkdir()
        installation = self.root / ".caprmedio_runtime/installation"
        installation.mkdir(parents=True)
        os.symlink(outside, installation / "migrations")
        (outside / "migration-symlink").mkdir()
        with self._lock() as lock:
            with self.assertRaisesRegex(InstallationStateError, "installation-carrier-unsafe"):
                write_inventory(self.root, inventory, lock=lock)
            lock.release("blocked")
        self.assertFalse((outside / "migration-symlink/inventory.toml").exists())

    def test_changed_command_or_release_binding_refuses_generation_proof(self) -> None:
        proof = self._proof()
        inventory = build_legacy_inventory(
            self.root,
            migration_id="migration-binding",
            target_context_sha256=self.target_context,
            process_observations=[proof],
        )
        changed_command = dict(proof)
        changed_command["command"] = dict(proof["command"], sha256=_digest("changed-command"))  # type: ignore[arg-type]
        self.assertFalse(prove_quiescence(inventory, [changed_command])["safe"])
        changed_release = dict(proof)
        changed_release["release"] = dict(proof["release"], target_context_sha256=_digest("other-context"))  # type: ignore[arg-type]
        with self._lock() as lock:
            with self.assertRaisesRegex(InstallationStateError, "release-proof-stale"):
                write_generation_process_proof(
                    self.root,
                    changed_release,
                    state_generation="generation-1",
                    target_context_sha256=self.target_context,
                    lock=lock,
                )
            lock.release("blocked")

    def test_legacy_bootstrap_coverage_omits_d600_context_and_revalidates_typed_proof(self) -> None:
        predecessor = self._legacy_bootstrap_proof()
        observation = self._legacy_observation(predecessor)
        providers = [
            _CoverageProvider("project_mcp", predecessor, observations=(observation,)),
            _CoverageProvider("mcp_hot_reload", predecessor),
            _CoverageProvider("workflow_orchestrator", predecessor),
        ]
        with open_legacy_process_coverage(
            providers, target_context_sha256=self.target_context, predecessor_proof=predecessor,
        ) as coverage:
            inventory = build_legacy_inventory(
                self.root,
                migration_id="legacy-bootstrap",
                target_context_sha256=self.target_context,
                process_coverage=coverage,
                predecessor_proof=predecessor,
            )
            self.assertNotIn("prior_execution_context_sha256", inventory)
            self.assertEqual(predecessor.framework_selector_sha256, inventory["prior_execution_selector_sha256"])
            quiescence = prove_quiescence(inventory, process_coverage=coverage, predecessor_proof=predecessor)
            self.assertTrue(quiescence["safe"])
            with self._lock() as lock:
                write_inventory(self.root, inventory, lock=lock, predecessor_proof=predecessor)
                self.assertEqual(
                    inventory,
                    state.read_inventory(self.root, "legacy-bootstrap", predecessor_proof=predecessor),
                )
                write_quiescence(self.root, inventory, quiescence, lock=lock, predecessor_proof=predecessor)
                verify_inventory(self.root, inventory, process_coverage=coverage, predecessor_proof=predecessor)
                staged = stage_legacy_copy(
                    self.root, inventory, quiescence, lock=lock,
                    process_coverage=coverage, predecessor_proof=predecessor,
                )
                verify_staged_copy(self.root, inventory, staged, predecessor_proof=predecessor)
                lock.release("partial")

    def test_raw_predecessor_candidate_is_refused(self) -> None:
        predecessor = self._legacy_bootstrap_proof()
        providers = [
            _CoverageProvider("project_mcp", predecessor),
            _CoverageProvider("mcp_hot_reload", predecessor),
            _CoverageProvider("workflow_orchestrator", predecessor),
        ]
        coverage = open_legacy_process_coverage(
            providers, target_context_sha256=self.target_context, predecessor_proof=predecessor,
        )
        self.addCleanup(coverage.close)
        with self.assertRaisesRegex(InstallationStateError, "process-coverage-invalid"):
            build_legacy_inventory(
                self.root,
                migration_id="raw-predecessor",
                target_context_sha256=self.target_context,
                process_coverage=coverage,
                predecessor_proof={"kind": "legacy_bootstrap_source_proof"},  # type: ignore[arg-type]
            )

    def test_typed_predecessor_requires_open_provider_coverage(self) -> None:
        predecessor = self._legacy_bootstrap_proof()
        with self.assertRaisesRegex(InstallationStateError, "process-coverage-required"):
            build_legacy_inventory(
                self.root,
                migration_id="typed-proof-without-coverage",
                target_context_sha256=self.target_context,
                predecessor_proof=predecessor,
            )

    def test_typed_predecessor_refuses_empty_retained_coverage(self) -> None:
        predecessor = self._legacy_bootstrap_proof()
        inventory = build_legacy_inventory(
            self.root,
            migration_id="typed-proof-empty-coverage",
            target_context_sha256=self.target_context,
        )
        inventory["provider_coverage"] = []
        inventory["inventory_sha256"] = state._digest(state._inventory_body(inventory))
        with self.assertRaisesRegex(InstallationStateError, "process-coverage-required"):
            prove_quiescence(inventory, predecessor_proof=predecessor)


if __name__ == "__main__":
    unittest.main()
