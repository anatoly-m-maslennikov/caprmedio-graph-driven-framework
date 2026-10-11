"""MCP preparation composition; test doubles prove no release or gate receipt."""

from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

MCP_ROOT = Path(__file__).resolve().parents[1]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

from selected_routes import SelectedRouteAdapter, canonical_digest  # noqa: E402


class ReleasePreparationMcpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.manifest = {"manifest_ref": "bindings.json", "canonical_manifest_sha256": "a" * 64,
                         "source_freshness": {"state": "current", "digest": "b" * 64},
                         "routes": [{"route": "release_version"}]}
        loader = patch("selected_routes.load_selected_manifest", return_value=self.manifest)
        loader.start()
        self.addCleanup(loader.stop)
        snapshot_loader = patch("selected_routes.load_release_execution_manifest", return_value=self.manifest)
        snapshot_loader.start()
        self.addCleanup(snapshot_loader.stop)
        self.resolved = {"operation": "apply", "project_root": str(self.root),
                         "candidateSnapshotManifest": {"sha256": "c" * 64},
                         "run_receipt_refs": []}
        self.native = SimpleNamespace(
            prepare_release_request=Mock(return_value=copy.deepcopy(self.resolved)),
            validate_prepared_release_request=Mock(),
        )
        self.calls = []
        self.support = SimpleNamespace(run_selected_operation=self.dispatch)
        self.adapter = SelectedRouteAdapter(self.root, service=self.support)
        native_loader = patch.object(self.adapter, "_release_request_module", return_value=self.native)
        self.native_loader = native_loader.start()
        self.addCleanup(native_loader.stop)

    def dispatch(self, request: dict) -> dict:
        self.calls.append(copy.deepcopy(request))
        if request["mode"] == "preview":
            receipt = {"parameters_digest": request["parameters_digest"]}
            return {"disposition": "preview", "outcome": "prepared", "proposal_receipt": receipt,
                    "proposal_receipt_digest": canonical_digest(receipt)}
        return {"disposition": "started", "outcome": "started", "workflow_run_id": "fixture-run"}

    def request(self, parameters: dict | None = None, *, execute: bool = False) -> dict:
        parameters = copy.deepcopy(parameters or {"operation": "apply", "project_root": str(self.root)})
        frontier = ["methodology:sources"]
        request = {"operation_route": "release_version", "mode": "execute" if execute else "preview",
                   "request_id": "release-preparation-fixture", "parameters": parameters,
                   "parameters_digest": canonical_digest(parameters), "target_frontier": frontier,
                   "target_frontier_digest": canonical_digest(frontier), "effects": [],
                   "effects_digest": canonical_digest([]),
                   "definition_manifest": {"manifest_ref": self.manifest["manifest_ref"],
                                           "manifest_digest": self.manifest["canonical_manifest_sha256"]},
                   "source_freshness": copy.deepcopy(self.manifest["source_freshness"]),
                   "initiative": {"initiative_id": "fixture", "instruction_summary": "prepare release"}}
        if execute:
            receipt = {"parameters_digest": request["parameters_digest"]}
            request.update(proposal_receipt=receipt, proposal_receipt_digest=canonical_digest(receipt),
                           assigned_action_id="fixture-operator", requested_runs=[{"kind": "workflow"}])
            bindings = {key: copy.deepcopy(request[key]) for key in (
                "request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness"
            )}
            request["operator_authorization"] = {**bindings, "authorization_ref": "fixture-authorization",
                                                  "authorization_freshness": {"state": "current", "digest": "d" * 64}}
        return request

    def test_minimal_preview_expands_before_receipt_seal_and_returns_exact_resolved_inputs(self) -> None:
        request = self.request()
        original = copy.deepcopy(request)
        result = self.adapter.invoke("release_version", request)
        expected_digest = canonical_digest(self.resolved)
        self.assertEqual((result["disposition"], result["outcome"]), ("preview", "prepared"))
        self.assertEqual(result["resolved_parameters"], self.resolved)
        self.assertEqual(result["resolved_parameters_digest"], expected_digest)
        self.assertEqual(result["proposal_receipt"]["parameters_digest"], expected_digest)
        self.assertEqual(self.calls[0]["parameters"], self.resolved)
        self.assertEqual(self.calls[0]["parameters_digest"], expected_digest)
        self.assertEqual(request, original)
        self.native.prepare_release_request.assert_called_once_with(self.root, request["parameters"])
        self.native.validate_prepared_release_request.assert_not_called()
        self.assertNotIn("gate_evidence_refs", result)

    def test_wrong_original_digest_is_rejected_before_preparation_or_dispatch(self) -> None:
        request = self.request()
        request["parameters_digest"] = "e" * 64
        result = self.adapter.invoke("release_version", request)
        self.assertEqual(result["disposition"], "rejected")
        self.native_loader.assert_not_called()
        self.assertEqual(self.calls, [])

    def test_minimal_execute_cannot_regenerate_after_authorization(self) -> None:
        result = self.adapter.invoke("release_version", self.request(execute=True))
        self.assertEqual((result["disposition"], result["outcome"]), ("blocked", "blocked"))
        self.native_loader.assert_not_called()
        self.assertEqual(self.calls, [])

    def test_complete_execute_revalidates_and_forwards_sealed_parameters_once(self) -> None:
        request = self.request(self.resolved, execute=True)
        result = self.adapter.invoke("release_version", request)
        self.assertEqual((result["disposition"], result["outcome"]), ("started", "started"))
        self.assertEqual(self.calls, [request])
        self.native.validate_prepared_release_request.assert_called_once_with(self.root, request["parameters"])
        self.native.prepare_release_request.assert_not_called()
        self.assertNotIn("resolved_parameters", result)
        self.assertNotIn("gate_evidence_refs", result)

    def test_stale_sealed_native_inputs_block_before_shared_support(self) -> None:
        self.native.validate_prepared_release_request.side_effect = RuntimeError("stale source")
        result = self.adapter.invoke("release_version", self.request(self.resolved, execute=True))
        self.assertEqual((result["disposition"], result["outcome"]), ("blocked", "blocked"))
        self.assertEqual(self.calls, [])
        self.native.prepare_release_request.assert_not_called()

    def test_missing_authorization_blocks_before_native_validation(self) -> None:
        request = self.request(self.resolved, execute=True)
        request.pop("operator_authorization")
        result = self.adapter.invoke("release_version", request)
        self.assertEqual(result["disposition"], "blocked")
        self.native_loader.assert_not_called()
        self.assertEqual(self.calls, [])

    def test_bound_host_identity_seals_external_root_while_real_observers_read_mount(self) -> None:
        # The disposable fixture is the physical mount. The external host path
        # deliberately need not exist in the MCP process's filesystem.
        release_tests = MCP_ROOT.parent / "201_TOOLS/RELEASE_VERSION/tests"
        if str(release_tests) not in sys.path:
            sys.path.insert(0, str(release_tests))
        import test_release_preparation as preparation_fixture
        import release_version as native
        import release_compilation as compilation

        fixture = preparation_fixture.ReleasePreparationTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.root = fixture.root
        self.adapter.root = self.root
        self.native_loader.return_value = native
        external = Path("/host/external/caprmedio-project")
        minimal = {"operation": "apply", "project_root": str(external)}
        request = self.request(minimal)
        original = copy.deepcopy(request)
        before = fixture.snapshot()
        with patch("selected_routes.bound_selection", return_value=SimpleNamespace(host_root=external)), \
             patch("release_compilation.build_preflight_validated_candidate",
                   wraps=compilation.build_preflight_validated_candidate) as observe:
            preview = self.adapter.invoke("release_version", request)
            self.assertEqual(preview["disposition"], "preview")
            observe.assert_called_once()
            self.assertEqual(observe.call_args.args[0], self.root)
            sealed = preview["resolved_parameters"]
            self.assertEqual(sealed["project_root"], str(external))
            self.assertEqual(preview["resolved_parameters_digest"], canonical_digest(sealed))
            self.assertEqual(sealed["candidateSnapshotManifest"]["framework_version"], "N+1")
            frozen = self.request(sealed, execute=True)
            frozen_before = copy.deepcopy(frozen)
            with patch("release_version.build_validated_candidate", wraps=native.build_validated_candidate) as reopen:
                result = self.adapter.invoke("release_version", frozen)
            self.assertEqual((result["disposition"], result["outcome"]), ("started", "started"))
            reopen.assert_called_once()
            self.assertEqual(reopen.call_args.args[0], str(self.root))
            self.assertEqual(frozen, frozen_before)
            self.assertEqual(self.calls[-1], frozen_before)
        self.assertEqual(request, original)
        self.assertEqual(fixture.snapshot(), before)

    def test_bound_host_identity_refuses_wrong_external_or_mount_caller_root(self) -> None:
        external = Path("/host/external/caprmedio-project")
        with patch("selected_routes.bound_selection", return_value=SimpleNamespace(host_root=external)):
            for supplied in ("/host/external/other-project", str(self.root)):
                with self.subTest(supplied=supplied):
                    result = self.adapter.invoke("release_version", self.request({
                        "operation": "apply", "project_root": supplied,
                    }))
                    self.assertEqual((result["disposition"], result["outcome"]), ("blocked", "blocked"))
        self.native_loader.assert_not_called()
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
