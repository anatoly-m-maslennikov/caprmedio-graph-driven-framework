"""Physical retained-O164 to direct-O199 bridge coverage."""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
WORKFLOW_ROOT = TOOLS_ROOT.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
for _path in (RELEASE_ROOT, TOOLS_ROOT, WORKFLOW_ROOT, Path(__file__).resolve().parent):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from direct_action_session import SOURCE_ADMISSION_ATOM_RELATIVE  # noqa: E402
from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE  # noqa: E402
from release_actions import PHASES, ReleaseActionRun, ReleasePhaseResult, SelectedReleaseActionContext, begin_release_action_run  # noqa: E402
from release_checkpoint import dump_release_checkpoint  # noqa: E402
from release_compilation import preflight_release_compilation  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from source_admission_host_command import (  # noqa: E402
    SourceAdmissionHostCommandError,
    SourceAdmissionHostCommandRequest,
    execute_source_admission_command,
    preview_source_admission_command,
    run_release_source_admission_command,
)
from workflow_run_support import RunExecutionSession, RunTracker  # noqa: E402
import work_journal  # noqa: E402


def _repository_root() -> Path:
    for candidate in RELEASE_ROOT.parents:
        if (candidate / SOURCE_ADMISSION_ATOM_RELATIVE).is_file():
            return candidate
    raise RuntimeError("repository root is unavailable")


REPOSITORY_ROOT = _repository_root()


def _digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


class _HostCommandFixture(PortablePackageFixture):
    """A real candidate/export chain plus physical selected-run carriers."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        # The direct O199 command physically reopens the bounded Journal
        # reader.  These are project-default query limits, sealed with the
        # candidate below; do not add them after the retained O172 frontier.
        default = self.root / CANONICAL_SOURCE_RELATIVE / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        default.write_bytes(default.read_bytes() + (
            "\n[query]\nmax_request_bytes = 4096\nmax_grammar_depth = 20\nmax_filter_tokens = 100\n"
            "max_in_members = 10\nmax_selected_fields = 20\nmax_page_size = 10\nmax_snapshot_members = 20\n"
            "max_file_bytes = 8388608\nmax_total_read_bytes = 33554432\ntimeout_seconds = 5\nmax_findings = 5\n"
        ).encode())
        self.write(
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            b"[paths]\ncontrol_root = '.caprmedio_caprmedio'\njournal_root = '.caprmedio_caprmedio/_journal'\nruntime_root = '.caprmedio_runtime'\n",
        )
        self.write(
            ".caprmedio_caprmedio/operators_registry.toml",
            b'[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\njournal_author = "fixture-operator"\n',
        )
        target = self.root / SOURCE_ADMISSION_ATOM_RELATIVE
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / SOURCE_ADMISSION_ATOM_RELATIVE, target)


class SourceAdmissionHostCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = _HostCommandFixture(admit=False)
        self.addCleanup(self.fixture.cleanup)
        self.release_run_id = self.fixture.run_id
        self.requested_action_run_id = f"{self.release_run_id}:step:3:action:1"
        self.parameters = self._parameters()
        self.execution = self._execution()
        self.frozen = self._frozen()
        self.tracker = RunTracker(
            self.fixture.root,
            source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
            executor=lambda _request, _session: {},
            journal_context={"author": "run-support", "timezone": "UTC"},
        )
        self.session = RunExecutionSession(self.tracker, self.execution)
        self.actual = self._record_delivery_frontier(complete_delivery=True)
        self._write_selected_carriers()

    def _parameters(self) -> dict[str, object]:
        manifest = self.fixture.candidate.manifest.model_dump(mode="json", by_alias=True)
        return {
            "operation": "apply",
            "project_root": str(self.fixture.root),
            "candidateSnapshotManifest": manifest,
            "expected_executing_release": manifest["executing_release"],
            "expected_project_structure_digest": manifest["project_structure_digest"],
            "expected_framework_settings_digest": manifest["framework_settings_digest"],
            "expected_source_frontier_digest": manifest["source_frontier_digest"],
            "run_receipt_refs": ["fixture-release-receipt"],
        }

    @staticmethod
    def _definition(atom_id: str, kind: str, ordinal: int) -> dict[str, object]:
        return {
            "atom_id": atom_id,
            "version": 9 if atom_id == "CA-O-164" else 1,
            "path": f"operations/{ordinal:02d}-{atom_id}.md",
            "digest": hashlib.sha256(f"{kind}:{atom_id}:{ordinal}".encode()).hexdigest(),
        }

    def _execution(self) -> dict[str, object]:
        requested: list[dict[str, object]] = [{
            "requested_run_id": self.release_run_id,
            "kind": "workflow",
            "definition": self._definition("CA-O-164", "workflow", 0),
        }]
        for index, (step, action, _phase) in enumerate(PHASES, start=1):
            requested_step = f"{self.release_run_id}:step:{index}"
            requested.extend(({
                "requested_run_id": requested_step,
                "kind": "step",
                "definition": self._definition(step, "step", index),
                "parent_requested_run_id": self.release_run_id,
            }, {
                "requested_run_id": f"{requested_step}:action:1",
                "kind": "action",
                "definition": self._definition(action, "action", index),
                "parent_requested_run_id": requested_step,
            }))
        frontier = ["fixture/frontier"]
        effects: list[object] = []
        execution: dict[str, object] = {
            "mode": "execute",
            "request_id": "fixture-retained-o164",
            "operation_route": "release_version",
            "parameters": self.parameters,
            "parameters_digest": _digest(self.parameters),
            "target_frontier": frontier,
            "target_frontier_digest": _digest(frontier),
            "effects": effects,
            "effects_digest": _digest(effects),
            "definition_manifest": {"manifest_ref": "fixture/selected.json", "manifest_digest": "a" * 64},
            "source_freshness": {
                "selected_source_registry_ref": "fixture/source-registry.json",
                "selected_source_registry_version": 1,
                "selected_source_registry_digest": "d" * 64,
                "selected_binding_ref": "fixture/release-binding.json",
                "selected_binding_digest": "e" * 64,
            },
            "initiative": {"initiative_id": "fixture", "instruction_summary": "retained O164", "initiative_ref": "fixture/plan.md"},
            "requested_runs": requested,
            "proposal_receipt": {"fixture": "retained"},
            "proposal_receipt_digest": "b" * 64,
            "assigned_action_id": "fixture-selected-release",
        }
        authorization_keys = (
            "request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
            "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness",
        )
        execution["operator_authorization"] = {
            **{key: execution[key] for key in authorization_keys},
            "authorization_ref": "fixture/release-authorization",
            "authorization_freshness": {"state": "current", "digest": "c" * 64},
        }
        return execution

    def _frozen(self) -> dict[str, object]:
        requested = self.execution["requested_runs"]
        assert isinstance(requested, list)
        workflow = requested[0]["definition"]
        assert isinstance(workflow, dict)
        steps: list[dict[str, object]] = []
        for index, (step_id, action_id, _phase) in enumerate(PHASES, start=1):
            step = requested[(index - 1) * 2 + 1]["definition"]
            action = requested[(index - 1) * 2 + 2]["definition"]
            assert isinstance(step, dict) and isinstance(action, dict)
            steps.append({
                "atom_id": step_id, "kind": "step", "version": step["version"], "path": step["path"], "sha256": step["digest"],
                "actions": [{
                    "atom_id": action_id, "kind": "action", "version": action["version"], "path": action["path"], "sha256": action["digest"],
                    "result_map": {"completed": "completed"},
                }],
                "on_result": [{"result": "completed", "terminal": "completed"}],
            })
        return {
            "request": {"operation": "enqueue_selected", "run_id": self.release_run_id, "execution": self.execution},
            "graph": {
                "route": "release_version", "manifest_ref": "fixture/selected.json", "manifest_digest": "a" * 64,
                "workflow": {"atom_id": "CA-O-164", "kind": "workflow", "version": workflow["version"], "path": workflow["path"], "sha256": workflow["digest"]},
                "entry_step": PHASES[0][0], "steps": steps, "native_action_calls": [],
            },
        }

    def _record_delivery_frontier(self, *, complete_delivery: bool) -> dict[str, str]:
        # The physical export is sealed under this selected Run identity, so
        # retain that same identity as the actual Workflow Run for this
        # compact fixture.  The bridge still derives it from Journal evidence.
        workflow = self.session.start_run(self.release_run_id, run_id=self.release_run_id)
        result: dict[str, str] = {"workflow": workflow["run_id"]}
        for index in range(3):
            requested_step = f"{self.release_run_id}:step:{index + 1}"
            requested_action = f"{requested_step}:action:1"
            step = self.session.start_run(requested_step, run_id=f"actual-release-step-{index + 1}")
            action = self.session.start_run(requested_action, run_id=f"actual-release-action-{index + 1}")
            result[f"step-{index}"] = step["run_id"]
            result[f"action-{index}"] = action["run_id"]
            if index < 2 or complete_delivery:
                self.session.finish_run(action["run_id"], outcome="completed", result_ref=f"fixture/phase-{index}.json", effect_refs=[])
                self.session.finish_run(step["run_id"], outcome="completed", result_ref=f"fixture/step-{index}.json", effect_refs=[])
        return result

    def _private_run(self) -> ReleaseActionRun:
        run = begin_release_action_run(self.parameters, workflow_run_id=self.actual["workflow"])
        run.candidate = self.fixture.candidate
        run.preflight = preflight_release_compilation(self.fixture.root, candidate_release="N+1")
        run.methodology_export = self.fixture.export
        for index, (step_atom_id, action_atom_id, phase) in enumerate(PHASES[:3]):
            step_id = self.actual[f"step-{index}"]
            action_id = self.actual[f"action-{index}"]
            context = SelectedReleaseActionContext(
                str(self.fixture.root), self.actual["workflow"], step_id, action_id,
                self.actual["workflow"], step_id, step_atom_id, action_atom_id,
                run.frozen_parameters_sha256, workflow_version=9,
            )
            output = self.fixture.candidate if index < 2 else self.fixture.export
            run.contexts[index] = context
            run.results[index] = ReleasePhaseResult(
                self.actual["workflow"], step_id, action_id, step_atom_id, action_atom_id,
                phase, "completed", "fixture retained O164 observation", self.fixture.candidate.manifest.sha256,
                () if index < 2 else (phase,), (), tuple(self.parameters["run_receipt_refs"]), output=output,
            )
        run.next_phase = 3
        return run

    def _write_selected_carriers(self) -> None:
        # The accepted selected-dispatch carrier is immutable input to the
        # read-only journal reconstruction; it is not synthesized by the
        # production bridge.
        dispatch_bytes = json.dumps(
            {key: self.execution[key] for key in sorted(self.execution) if key != "mode"},
            ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        ).encode()
        dispatch = {
            "schema_version": 1,
            "request_id": self.execution["request_id"],
            "canonical_request_bytes": dispatch_bytes.decode(),
            "canonical_request_bytes_digest": hashlib.sha256(dispatch_bytes).hexdigest(),
            "state": "accepted",
        }
        request_id = str(self.execution["request_id"])
        dispatch_path = self.fixture.root / ".caprmedio_runtime/state/work_journal/selected_runs/requests" / f"{hashlib.sha256(request_id.encode()).hexdigest()}.json"
        dispatch_path.parent.mkdir(parents=True, exist_ok=True)
        dispatch_path.write_bytes(canonical_json(dispatch))
        runner = SelectedExecution(self.fixture.root)
        folder = runner.run_directory(self.release_run_id)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "selected_request.json").write_bytes(canonical_json(self.frozen))
        (folder / "release_action_run.json").write_bytes(canonical_json(dump_release_checkpoint(self._private_run())))

    def _command(self, **changes: object) -> SourceAdmissionHostCommandRequest:
        values: dict[str, object] = {
            "project_root": self.fixture.root,
            "release_run_id": self.release_run_id,
            "requested_action_run_id": self.requested_action_run_id,
            "operator": "Fixture Operator",
            "command_id": "fixture-retained-o199",
            "operators_registry_ref": ".caprmedio_caprmedio/operators_registry.toml",
            "release_authorization_ref": "fixture/release-authorization",
        }
        values.update(changes)
        return SourceAdmissionHostCommandRequest(**values)  # type: ignore[arg-type]

    def _execute(self, snapshot_sha256: str, **changes: object):
        values: dict[str, object] = {
            "project_root": self.fixture.root,
            "command_id": "fixture-retained-o199",
            "release_run_id": self.release_run_id,
            "operator": "Fixture Operator",
            "authorization_ref": "fixture/release-authorization",
            "observed_snapshot_sha256": snapshot_sha256,
        }
        values.update(changes)
        return execute_source_admission_command(**values)  # type: ignore[arg-type]

    def _bridge_patches(self):
        return (
            patch.object(SelectedExecution, "_revalidate", autospec=True, side_effect=lambda _self, frozen: frozen["graph"]),
            patch.object(SelectedExecution, "_shared_tracker", autospec=True, return_value=self.tracker),
        )

    def _events(self) -> list[dict[str, object]]:
        journal = self.fixture.root / ".caprmedio_caprmedio/_journal"
        return [json.loads(line) for path in sorted(journal.glob("*.ndjson")) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_reopens_real_o172_and_admits_one_direct_o199_command(self) -> None:
        with self._bridge_patches()[0], self._bridge_patches()[1]:
            preview = preview_source_admission_command(self.fixture.root, release_run_id=self.release_run_id)
            self.assertFalse((self.fixture.root / "catalog.toml").exists())
            result = self._execute(preview.snapshot_sha256)

        self.assertEqual(self.release_run_id, result.frontier.release_run_id)
        self.assertEqual(self.requested_action_run_id, result.frontier.requested_action_run_id)
        self.assertEqual("actual-release-action-3", result.frontier.action_provenance.action_run_id)
        self.assertEqual(self.fixture.private_compilation, result.frontier.private_compilation)
        self.assertEqual(result.frontier.source_snapshot, result.admission_command.source_snapshot)
        self.assertEqual(preview.snapshot_sha256, result.admission_command.command_receipt.snapshot_sha256)
        self.assertTrue(result.admission_command.admission.catalog_path.is_file())
        self.assertTrue(result.admission_command.command_receipt_path.is_file())
        self.assertEqual(["CA-O-199", "CA-O-199"], [item["action_id"] for item in self._events() if item["action_id"] == "CA-O-199"])

    def test_mismatched_authorization_or_action_refuses_before_o199_start(self) -> None:
        before = self._events()
        with self._bridge_patches()[0], self._bridge_patches()[1]:
            preview = preview_source_admission_command(self.fixture.root, release_run_id=self.release_run_id)
        for execute_changes, code in (({"authorization_ref": "other/auth"}, "source-admission-host-command-authorization-mismatch"),
                                      ({"observed_snapshot_sha256": "0" * 64}, "source-admission-host-command-snapshot-mismatch")):
            with self.subTest(execute_changes=execute_changes), self._bridge_patches()[0], self._bridge_patches()[1], self.assertRaises(SourceAdmissionHostCommandError) as refused:
                self._execute(preview.snapshot_sha256, **execute_changes)
            self.assertEqual(code, refused.exception.code)
            self.assertEqual(before, self._events())
            self.assertFalse((self.fixture.root / "catalog.toml").exists())
        with self._bridge_patches()[0], self._bridge_patches()[1], self.assertRaises(SourceAdmissionHostCommandError) as refused:
            run_release_source_admission_command(self._command(requested_action_run_id=f"{self.release_run_id}:step:2:action:1"))
        self.assertEqual("source-admission-host-command-action-mismatch", refused.exception.code)
        self.assertEqual(before, self._events())

    def test_incomplete_o172_refuses_before_o199_start(self) -> None:
        fixture = _HostCommandFixture(admit=False)
        self.addCleanup(fixture.cleanup)
        # This fixture differs only in its terminal Journal record: O172 has
        # an actual start but no durable completion.  Its stale checkpoint is
        # intentionally retained to prove Journal evidence wins.
        self.fixture, original = fixture, self.fixture
        try:
            self.release_run_id = fixture.run_id
            self.requested_action_run_id = f"{self.release_run_id}:step:3:action:1"
            self.parameters = self._parameters()
            self.execution = self._execution()
            self.frozen = self._frozen()
            self.tracker = RunTracker(fixture.root, source_observer=lambda _request: {"selected": True, "current": True, "observed": {}}, executor=lambda _request, _session: {}, journal_context={"author": "run-support", "timezone": "UTC"})
            self.session = RunExecutionSession(self.tracker, self.execution)
            self.actual = self._record_delivery_frontier(complete_delivery=False)
            self._write_selected_carriers()
            before = self._events()
            with self._bridge_patches()[0], self._bridge_patches()[1], self.assertRaises(SourceAdmissionHostCommandError) as refused:
                preview_source_admission_command(self.fixture.root, release_run_id=self.release_run_id)
            self.assertEqual("source-admission-host-command-release-incomplete", refused.exception.code)
            self.assertEqual(before, self._events())
            self.assertFalse((fixture.root / "catalog.toml").exists())
        finally:
            self.fixture = original

    def test_reopen_is_effect_free_and_second_command_never_replays_o199_start(self) -> None:
        with self._bridge_patches()[0], self._bridge_patches()[1]:
            before = self._events()
            reopened = preview_source_admission_command(self.fixture.root, release_run_id=self.release_run_id)
            self.assertEqual(before, self._events())
            self.assertEqual(self.fixture.source_snapshot, reopened.frontier.source_snapshot)
            first = self._execute(reopened.snapshot_sha256)
            after_first = self._events()
            with self.assertRaises(Exception):
                self._execute(reopened.snapshot_sha256)
            self.assertEqual(after_first, self._events())
            self.assertTrue(first.admission_command.admission.catalog_path.is_file())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
