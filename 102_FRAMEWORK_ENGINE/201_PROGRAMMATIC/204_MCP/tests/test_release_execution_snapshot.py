"""Per-run Release binding snapshots; no Action, gate, image or install executes."""

from __future__ import annotations

import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

MCP_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = MCP_ROOT.parents[2]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

import release_source_admission as source_admission  # noqa: E402
import selected_routes  # noqa: E402


def _pins(value):
    result = {}
    if isinstance(value, dict):
        if {"atom_id", "version", "source_path", "digest"} <= set(value):
            result[value["source_path"]] = dict(value)
        for child in value.values():
            result.update(_pins(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            result.update(_pins(child))
    return result


class ReleaseExecutionSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current = source_admission.derive_release_execution_source_snapshot(REPOSITORY)
        cls.sources = _pins(cls.current)

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        for relative in self.sources:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        for relative in (source_admission._OPERATIONS_ROOT,
                         *source_admission._RMED_ROOTS.values(),
                         *source_admission._TOOLS_RMED_ROOTS.values()):
            (self.root / relative).mkdir(parents=True, exist_ok=True)
        for filename in ("project_structure.toml", "caprmedio_project_settings.toml"):
            shutil.copyfile(REPOSITORY / ".caprmedio_caprmedio" / filename,
                            self.root / ".caprmedio_caprmedio" / filename)
        self.native = self.write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_version.py",
            b"# bounded documentary native implementation fixture\nVALUE = 1\n",
        )
        self.executing_root_from_file = selected_routes._release_executing_implementation_root
        executing_root = patch.object(selected_routes, "_release_executing_implementation_root", return_value=self.root)
        executing_root.start()
        self.addCleanup(executing_root.stop)
        self.required = next(pin for pin in self.sources.values() if pin["atom_id"] == "CA-O-176")
        self.required_tool = next(pin for pin in self.sources.values() if pin["atom_id"] == "CA-D-560")
        self.unrelated = self.write(
            source_admission._OPERATIONS_ROOT + "/CA-O-030--unrelated.md",
            (self.root / self.required["source_path"]).read_bytes().replace(b"CA-O-176", b"CA-O-030"),
        )
        # Copy only the existing portfolio document, not its unrelated source
        # graph. The Release loader must neither validate nor relabel it.
        portfolio_bytes = (REPOSITORY / selected_routes.selected_manifest_ref(REPOSITORY)).read_bytes()
        self.raw_manifest = json.loads(portfolio_bytes)
        self.raw_path = self.write(".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
                                   portfolio_bytes)
        self.calls = []
        self.support = SimpleNamespace(run_selected_operation=self.dispatch)
        self.adapter = selected_routes.SelectedRouteAdapter(self.root, service=self.support, strict_manifest=False)
        native_boundary = SimpleNamespace(validate_prepared_release_request=Mock())
        loader = patch.object(self.adapter, "_release_request_module", return_value=native_boundary)
        loader.start()
        self.addCleanup(loader.stop)

    def write(self, relative, data):
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return target

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                for path in self.root.rglob("*") if path.is_file()}

    def manifest(self):
        return selected_routes.load_release_execution_manifest(self.root)

    def dispatch(self, request):
        self.calls.append(copy.deepcopy(request))
        receipt = {"definition_manifest": copy.deepcopy(request["definition_manifest"])}
        return {"disposition": "preview" if request["mode"] == "preview" else "started",
                "outcome": "prepared" if request["mode"] == "preview" else "started",
                "proposal_receipt": receipt, "proposal_receipt_digest": selected_routes.canonical_digest(receipt)}

    def request(self, manifest, *, execute=False):
        digest = selected_routes.canonical_digest
        parameters = {"operation": "apply", "project_root": str(self.root),
                      "candidateSnapshotManifest": {"sha256": "d" * 64}}
        frontier = ["methodology:sources"]
        request = {"operation_route": "release_version", "mode": "execute" if execute else "preview",
                   "request_id": "release-snapshot-fixture", "parameters": parameters,
                   "parameters_digest": digest(parameters), "target_frontier": frontier,
                   "target_frontier_digest": digest(frontier), "effects": [], "effects_digest": digest([]),
                   "definition_manifest": {"manifest_ref": manifest["manifest_ref"],
                                           "manifest_digest": manifest["canonical_manifest_sha256"]},
                   "source_freshness": copy.deepcopy(manifest["source_freshness"]),
                   "initiative": {"initiative_id": "fixture", "instruction_summary": "preview release snapshot"}}
        if execute:
            receipt = {"definition_manifest": copy.deepcopy(request["definition_manifest"])}
            request.update(proposal_receipt=receipt, proposal_receipt_digest=digest(receipt),
                           assigned_action_id="fixture-operator", requested_runs=[{"kind": "workflow"}])
            fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                      "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
            request["operator_authorization"] = {
                **{key: copy.deepcopy(request[key]) for key in fields}, "authorization_ref": "fixture-authorization",
                "authorization_freshness": {"state": "current", "digest": "e" * 64},
            }
        return request

    def test_unrelated_o030_and_stale_raw_seventeen_route_identity_do_not_block_release(self):
        manifest = self.manifest()
        self.unrelated.write_bytes(self.unrelated.read_bytes() + b"\nchanged unrelated source\n")
        before = self.snapshot()
        self.assertEqual(self.manifest(), manifest)
        result = self.adapter.invoke("release_version", self.request(manifest))
        self.assertEqual((result["disposition"], result["outcome"]), ("preview", "prepared"))
        self.assertEqual(self.snapshot(), before)

    def test_changed_release_source_or_native_code_refuses_old_preview_until_fresh_preview(self):
        for target in (self.root / self.required["source_path"], self.native):
            with self.subTest(target=target.relative_to(self.root).as_posix()):
                old_manifest = self.manifest()
                original = target.read_bytes()
                self.assertEqual(self.adapter.invoke("release_version", self.request(old_manifest))["disposition"], "preview")
                before_dispatch = len(self.calls)
                revised = original + b"\n# current bytes changed\n"
                if target == self.root / self.required["source_path"]:
                    revised = revised.replace(
                        f'version: {self.required["version"]}\n'.encode(),
                        f'version: {self.required["version"] + 1}\n'.encode(), 1,
                    )
                target.write_bytes(revised)
                before = self.snapshot()
                stale = self.adapter.invoke("release_version", self.request(old_manifest, execute=True))
                self.assertIn(stale["disposition"], {"rejected", "blocked"})
                self.assertEqual(len(self.calls), before_dispatch)
                fresh = self.manifest()
                self.assertNotEqual(fresh["canonical_manifest_sha256"], old_manifest["canonical_manifest_sha256"])
                self.assertEqual(self.adapter.invoke("release_version", self.request(fresh))["disposition"], "preview")
                self.assertEqual(self.adapter.invoke("release_version", self.request(fresh, execute=True))["disposition"], "started")
                self.assertEqual(self.snapshot(), before)
                target.write_bytes(original)

    def test_missing_inactive_or_malformed_required_source_refuses_without_effects(self):
        for source in (self.required, self.required_tool):
            target = self.root / source["source_path"]
            original = target.read_bytes()
            for changed in (None, original.replace(b"status: Active", b"status: Archived", 1), b"malformed required source\n"):
                with self.subTest(source=source["atom_id"], condition="missing" if changed is None else changed[:48]):
                    if changed is None:
                        target.unlink()
                    else:
                        target.write_bytes(changed)
                    before = self.snapshot()
                    with self.assertRaises(ValueError):
                        self.manifest()
                    self.assertEqual(self.calls, [])
                    self.assertEqual(self.snapshot(), before)
                    target.write_bytes(original)

    def test_required_source_change_during_capture_cannot_seal_mixed_snapshot(self):
        read_pin = source_admission._read_pin
        target = self.root / self.required["source_path"]
        changed = False

        def read_then_change(root, pin):
            nonlocal changed
            result = read_pin(root, pin)
            if pin["source_path"] == self.required["source_path"] and not changed:
                changed = True
                target.write_bytes(target.read_bytes() + b"\nchanged during source capture\n")
            return result

        with patch.object(source_admission, "_read_pin", side_effect=read_then_change):
            with self.assertRaises(ValueError):
                self.manifest()
        self.assertTrue(changed)
        self.assertEqual(self.calls, [])
        self.assertFalse((self.root / ".caprmedio_caprmedio/_projection/release_execution_snapshot.json").exists())

    def test_snapshot_digest_is_self_consistent_and_never_claims_raw_manifest_identity(self):
        before = self.snapshot()
        manifest = self.manifest()
        unsigned = {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        self.assertEqual(manifest["canonical_manifest_sha256"], selected_routes.canonical_digest(unsigned))
        self.assertTrue(manifest["manifest_ref"].endswith("/release_execution_snapshot.json"))
        self.assertNotEqual(manifest["manifest_ref"], self.raw_path.relative_to(self.root).as_posix())
        self.assertNotEqual(manifest["canonical_manifest_sha256"], self.raw_manifest["canonical_manifest_sha256"])
        self.assertEqual([row["route"] for row in manifest["routes"]], ["release_version"])
        self.assertFalse((self.root / manifest["manifest_ref"]).exists())
        self.assertEqual(self.raw_path.read_bytes(), before[self.raw_path.relative_to(self.root).as_posix()][0])
        self.assertEqual(self.snapshot(), before)

    def test_worker_reopens_exact_release_snapshot_without_using_raw_portfolio(self):
        app_root = MCP_ROOT.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
        if str(app_root) not in sys.path:
            sys.path.insert(0, str(app_root))
        from selected_execution import SelectedExecution, SelectedExecutionError

        # Isolate the worker's read-only definition loader from handler setup.
        worker = SelectedExecution.__new__(SelectedExecution)
        worker.root = self.root
        manifest = self.manifest()
        request = self.request(manifest, execute=True)
        before = self.snapshot()
        observed, reference, digest = worker._load_manifest(request)
        self.assertEqual(observed, manifest)
        self.assertEqual(reference, manifest["manifest_ref"])
        self.assertEqual(digest, manifest["canonical_manifest_sha256"])
        self.assertEqual(self.snapshot(), before)
        wrong_reference = copy.deepcopy(request)
        wrong_reference["definition_manifest"]["manifest_ref"] = self.raw_path.relative_to(self.root).as_posix()
        with self.assertRaises(SelectedExecutionError):
            worker._load_manifest(wrong_reference)
        self.native.write_bytes(self.native.read_bytes() + b"\n# changed before worker load\n")
        with self.assertRaises(SelectedExecutionError):
            worker._load_manifest(request)
        fresh = self.manifest()
        self.assertEqual(worker._load_manifest(self.request(fresh, execute=True))[0], fresh)
        self.assertEqual(self.calls, [])

    def test_executor_origin_is_program_owned_and_candidate_override_cannot_substitute_it(self):
        self.assertEqual(self.executing_root_from_file(), Path(selected_routes.__file__).resolve().parents[3])
        runtime = self.root / ".caprmedio_tmp/executor"
        alternate_candidate = self.root / ".caprmedio_tmp/candidate"
        native_relative = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_version.py"
        self.write((runtime.relative_to(self.root) / native_relative).as_posix(), b"VALUE = 'actual executor'\n")
        self.write((alternate_candidate.relative_to(self.root) / native_relative).as_posix(), b"VALUE = 'alternate candidate'\n")
        with patch.object(selected_routes, "_release_executing_implementation_root", return_value=runtime):
            actual = self.manifest()["release_execution_snapshot"]
            alternate = selected_routes.load_release_execution_manifest(
                self.root, implementation_root=alternate_candidate,
            )["release_execution_snapshot"]
        self.assertEqual(actual["executing_implementation"], alternate["executing_implementation"])
        self.assertNotEqual(actual["implementation"]["sha256"], alternate["implementation"]["sha256"])
        self.assertNotEqual(actual["implementation"]["sha256"], actual["executing_implementation"]["sha256"])

    def test_actual_executor_bytes_drift_invalidates_preview_with_unchanged_candidate_bytes(self):
        runtime = self.root / ".caprmedio_tmp/executor"
        actual_native = self.write(
            (runtime.relative_to(self.root) / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_version.py").as_posix(),
            b"VALUE = 'actual executor'\n",
        )
        with patch.object(selected_routes, "_release_executing_implementation_root", return_value=runtime):
            old = self.manifest()
            self.assertEqual(self.adapter.invoke("release_version", self.request(old))["disposition"], "preview")
            dispatches = len(self.calls)
            actual_native.write_bytes(actual_native.read_bytes() + b"\n# runtime helper changed\n")
            before = self.snapshot()
            stale = self.adapter.invoke("release_version", self.request(old, execute=True))
            self.assertIn(stale["disposition"], {"rejected", "blocked"})
            self.assertEqual(len(self.calls), dispatches)
            current = self.manifest()
            self.assertEqual(old["release_execution_snapshot"]["implementation"],
                             current["release_execution_snapshot"]["implementation"])
            self.assertNotEqual(old["release_execution_snapshot"]["executing_implementation"]["sha256"],
                                current["release_execution_snapshot"]["executing_implementation"]["sha256"])
            self.assertNotEqual(old["canonical_manifest_sha256"], current["canonical_manifest_sha256"])
            self.assertEqual(self.adapter.invoke("release_version", self.request(current))["disposition"], "preview")
            self.assertEqual(self.adapter.invoke("release_version", self.request(current, execute=True))["disposition"], "started")
            self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
