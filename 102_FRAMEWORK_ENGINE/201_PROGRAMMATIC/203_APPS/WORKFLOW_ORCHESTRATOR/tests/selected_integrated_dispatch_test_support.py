"""Frozen fixture construction for Integrated dispatch tests."""

from __future__ import annotations

import copy
from collections.abc import Callable, Mapping
from pathlib import Path
import sys
import tempfile
from typing import Any
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, APP / "tests", TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution_run_plan import build_requested_runs  # noqa: E402
from selected_integrated_action_contract import prompt_spec  # noqa: E402
from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402
from workflow_run_support import (  # noqa: E402
    RunTracker,
    _canonical_digest,
    _proposal,
    _validate_common,
)


class PendingProvider:
    """Count real provider calls while returning the fixture's pending packet."""

    def __init__(self) -> None:
        self.calls = 0

    def __call__(
        self,
        packet: Mapping[str, object],
        *,
        agent: Callable[[str, Mapping[str, object]], Mapping[str, object]],
        selected_project_root: Path,
        trusted_execution_authorization: Mapping[str, object] | None = None,
    ) -> dict[str, object]:
        del selected_project_root, trusted_execution_authorization
        self.calls += 1
        return dict(agent(prompt_spec("CA-O-231", "CA-O-017")["prompt"], packet))


class IntegratedDispatchTestCase(unittest.TestCase):
    """Materialize the source-pinned current O016 fixture for each test."""

    fixture_loader: Any = CurrentSharedContextFixture

    def setUp(self) -> None:
        parent = PROJECT_ROOT / ".caprmedio_tmp" / "selected-integrated-dispatch"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        self.fixture = self.fixture_loader.load()
        self.root = self.fixture.materialize(Path(temporary.name) / "project")
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        settings.write_text(
            "[project]\nkey = 'fixture'\n[artifacts.identity]\nproject_prefix = 'CA'\n"
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nruntime_root = '.caprmedio_runtime'\n",
            encoding="utf-8",
        )
        for row in self.fixture._support_rows():
            target = self.root / str(row["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.fixture.support_source_bytes(str(row["atom_id"])))
        self.canonical_revalidate = patch(
            "selected_integrated_dispatch.revalidate",
            side_effect=lambda _root, frozen: copy.deepcopy(frozen["graph"]),
        )
        self.revalidate_mock = self.canonical_revalidate.start()
        self.addCleanup(self.canonical_revalidate.stop)

    def graph(self) -> dict[str, object]:
        pins = {row["atom_id"]: dict(row) for row in self.fixture.source_pins()}

        def pin(atom_id: str) -> dict[str, object]:
            value = pins[atom_id]
            return {
                "atom_id": value["atom_id"],
                "kind": value["kind"],
                "version": value["version"],
                "path": value["source_path"],
                "sha256": value["sha256"],
            }

        return {
            "route": "run_implementation_workflow",
            "workflow": pin("CA-O-016"),
            "entry_step": "CA-O-231",
            "native_action_calls": [],
            "steps": [
                {
                    **pin(step),
                    "actions": [pin(action)],
                    "on_result": [{"result": "blocked", "terminal": "completed"}],
                }
                for step, action in ACTIONS.items()
            ],
        }

    def frozen(self, run_id: str) -> tuple[dict[str, object], RunTracker]:
        graph = self.graph()
        parameters = copy.deepcopy(self.fixture.native_implementation_parameters())
        digest = _canonical_digest
        freshness = {
            "selected_source_registry_ref": "registry.md",
            "selected_source_registry_version": 1,
            "selected_source_registry_digest": "a" * 64,
            "selected_binding_ref": "bindings.json",
            "selected_binding_digest": "b" * 64,
        }
        execution: dict[str, object] = {
            "mode": "execute",
            "request_id": f"request-{run_id}",
            "operation_route": "run_implementation_workflow",
            "parameters": parameters,
            "parameters_digest": digest(parameters),
            "target_frontier": ["frontier.md"],
            "target_frontier_digest": digest(["frontier.md"]),
            "effects": [],
            "effects_digest": digest([]),
            "definition_manifest": {"manifest_ref": "manifest.json", "manifest_digest": "c" * 64},
            "source_freshness": freshness,
            "initiative": {"initiative_id": "fixture", "instruction_summary": "frozen dispatch"},
            "proposal_receipt": {},
            "proposal_receipt_digest": "d" * 64,
            "assigned_action_id": "CA-O-017",
            "operator_authorization": {},
            "requested_runs": build_requested_runs(graph, run_id, parameters["run_visit_limits"]),
        }
        tracker = RunTracker(
            self.root,
            source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
            executor=lambda _request, _session: {},
        )
        parsed = _validate_common(execution)
        proposal = _proposal(parsed, tracker._observe(parsed))
        execution["proposal_receipt"] = proposal
        execution["proposal_receipt_digest"] = digest(proposal)
        execution["operator_authorization"] = {
            "authorization_ref": "authorization.json",
            "authorization_freshness": {"state": "current", "digest": "e" * 64},
            **{
                key: execution[key]
                for key in (
                    "request_id",
                    "operation_route",
                    "parameters_digest",
                    "target_frontier_digest",
                    "effects_digest",
                    "definition_manifest",
                    "source_freshness",
                )
            },
            "proposal_receipt_digest": execution["proposal_receipt_digest"],
        }
        return {
            "request": {"operation": "enqueue_selected", "run_id": run_id, "execution": execution},
            "graph": graph,
        }, tracker
