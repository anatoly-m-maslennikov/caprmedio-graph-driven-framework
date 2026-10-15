"""Actual connected SDK context reaches the reviewed native Subject publisher."""

from __future__ import annotations

import copy
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession

MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
for path in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "ATOM_UPDATE/tests", TOOLS_ROOT / "tests"):
    sys.path.insert(0, str(path))

import hot_reload  # noqa: E402
from ATOM_UPDATE import atom_update as preparation  # noqa: E402
from test_direct_subject_preparation_protocol import PREPARATION_PINS  # noqa: E402
from test_subject_apply_portfolio import REPOSITORY, SubjectApplyProject  # noqa: E402


class SubjectPublicationGatewayTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.fixture = SubjectApplyProject(Path(directory.name).resolve())
        for pin in PREPARATION_PINS:
            destination = self.fixture.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / pin["path"], destination)
        self.runner, self.frozen = self.fixture.execution("gateway-subject-fixture")
        self.request = self.frozen["request"]["execution"]
        self.preparation_request = {
            "operation": "preview_subjects",
            "subject_profile": "approved",
            "atoms": [
                {
                    "atom_id": self.fixture.target["atom_id"],
                    "version": self.fixture.target["version"],
                    "sha256": self.fixture.target["digest"],
                    "subject_patches": self.fixture.patches,
                }
            ],
        }
        self.child_calls, self.forms = [], []
        self.reply = types.ElicitResult(action="accept", content={"review": True, "pause": True})
        self.gateway = hot_reload.Gateway(self.fixture.root)
        self.gateway.active = SimpleNamespace(
            client=SimpleNamespace(call_tool=self.child_call),
            fingerprint="fixture-generation",
            in_flight=0,
            tools=[
                types.Tool(name=name, input_schema={"type": "object"})
                for name in ("atom_update", "update_atom", "create_atom")
            ],
        )

    async def child_call(self, name, arguments, **_kwargs):
        self.child_calls.append((name, copy.deepcopy(arguments)))
        if name != "atom_update":
            return hot_reload.result({"forwarded": True})
        value = preparation.create_adapter(self.fixture.root).invoke(arguments["request"])
        return hot_reload.result(value.model_dump(mode="json"))

    async def elicit(self, _context, params):
        self.fixture.assert_unchanged(self)
        self.forms.append(params)
        return self.reply

    async def stage(self, client):
        preview = await client.call_tool("atom_update", {"request": self.preparation_request})
        self.assertEqual([], preview.structured_content["errors"])
        value = preview.structured_content["preview"]
        response = await client.call_tool(
            "atom_update",
            {
                "request": {
                    **self.preparation_request,
                    "operation": "stage_subjects",
                    "preview_sha256": value["preview_sha256"],
                    "illustrative_updated_at": value["illustrative_updated_at"],
                }
            },
        )
        self.assertEqual([], response.structured_content["errors"])
        return response.structured_content

    async def test_connected_stage_and_form_publish_in_host_without_child_enqueue(self):
        async with InMemoryTransport(self.gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=self.elicit) as client:
                await client.initialize()
                staged = await self.stage(client)
                response = await client.call_tool("update_atom", {"request": self.request})
        self.assertEqual("dispatched", response.structured_content["status"])
        self.assertEqual("terminal", response.structured_content["result"]["disposition"])
        self.assertEqual(1, len(self.forms))
        self.assertIn(staged["staging"]["manifest_path"], self.forms[0].message)
        self.assertIn("golden-operator", self.forms[0].message)
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertNotEqual(self.fixture.before, self.fixture.path.read_bytes())
        self.assertEqual(["atom_update", "atom_update"], [name for name, _ in self.child_calls])

    async def test_decline_preserves_sources_and_does_not_enqueue(self):
        self.reply = types.ElicitResult(action="decline")
        async with InMemoryTransport(self.gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=self.elicit) as client:
                await client.initialize()
                await self.stage(client)
                response = await client.call_tool("update_atom", {"request": self.request})
        self.assertEqual("decline", response.structured_content["status"])
        self.fixture.assert_unchanged(self)
        self.assertEqual(2, len(self.child_calls))

    async def test_stage_is_bound_to_actual_session_and_exact_intent(self):
        first, second = object(), object()
        staged = hot_reload.result(
            {
                "operation": "stage_subjects",
                "errors": [],
                "preview": {"count": 1, "atoms": [{"subject_intent_sha256": "other-intent"}]},
                "staging": {"manifest_path": "unused", "manifest_sha256": "unused"},
            }
        )
        self.gateway._retain_subject_stage(
            SimpleNamespace(session=SimpleNamespace(_connection=first)), staged
        )
        for session in (first, second):
            response = await self.gateway.call(
                SimpleNamespace(session=SimpleNamespace(_connection=session)),
                SimpleNamespace(name="update_atom", arguments={"request": self.request}),
            )
            self.assertEqual("refused", response.structured_content["status"])
            self.assertIn(
                "no successful one-Atom stage", response.structured_content["diagnostics"][0]
            )
        staged.structured_content["preview"]["atoms"][0]["subject_intent_sha256"] = (
            self.fixture.parameters["subject_intent_sha256"]
        )
        self.gateway._retain_subject_stage(
            SimpleNamespace(session=SimpleNamespace(_connection=first)), staged
        )
        response = await self.gateway.call(
            SimpleNamespace(session=SimpleNamespace(_connection=second)),
            SimpleNamespace(name="update_atom", arguments={"request": self.request}),
        )
        self.assertIn("no successful one-Atom stage", response.structured_content["diagnostics"][0])
        self.fixture.assert_unchanged(self)
        self.assertEqual([], self.child_calls)

    async def test_error_and_multi_atom_stage_responses_are_not_retained(self):
        session = object()
        value = {
            "operation": "stage_subjects",
            "errors": [],
            "preview": {
                "count": 1,
                "atoms": [
                    {"subject_intent_sha256": self.fixture.parameters["subject_intent_sha256"]}
                ],
            },
            "staging": {"manifest_path": "unused", "manifest_sha256": "unused"},
        }
        self.gateway._retain_subject_stage(
            SimpleNamespace(session=SimpleNamespace(_connection=session)),
            hot_reload.result(value, True),
        )
        value["errors"] = [{"code": "failed"}]
        self.gateway._retain_subject_stage(
            SimpleNamespace(session=SimpleNamespace(_connection=session)), hot_reload.result(value)
        )
        value["errors"], value["preview"]["count"] = [], 2
        value["preview"]["atoms"] *= 2
        self.gateway._retain_subject_stage(
            SimpleNamespace(session=SimpleNamespace(_connection=session)), hot_reload.result(value)
        )
        self.assertEqual({}, self.gateway.subject_stages)

    async def test_stage_drift_and_ambiguous_operator_refuse_without_form(self):
        async with InMemoryTransport(self.gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=self.elicit) as client:
                await client.initialize()
                staged = await self.stage(client)
                path = self.fixture.root / staged["staging"]["manifest_path"]
                original = path.read_bytes()
                path.write_bytes(original + b"\nchanged\n")
                response = await client.call_tool("update_atom", {"request": self.request})
                self.assertEqual("refused", response.structured_content["status"])
                path.write_bytes(original)
                registry = self.fixture.root / ".caprmedio_caprmedio/operators_registry.toml"
                registry.write_bytes(
                    registry.read_bytes() + b'\n[[operators]]\nname="Other"\nrole="owner"\n'
                )
                response = await client.call_tool("update_atom", {"request": self.request})
                self.assertEqual("refused", response.structured_content["status"])
                self.assertIn(
                    "one registered Operator", response.structured_content["diagnostics"][0]
                )
                registry.write_bytes(b"operators = []\n")
                response = await client.call_tool("update_atom", {"request": self.request})
                self.assertEqual("refused", response.structured_content["status"])
                self.assertIn("Operator registry", response.structured_content["diagnostics"][0])
        self.assertEqual([], self.forms)
        self.fixture.assert_unchanged(self)

    async def test_preview_and_non_subject_execution_keep_child_path(self):
        for name, request in (
            ("update_atom", {**self.request, "mode": "preview"}),
            ("create_atom", {"mode": "execute", "parameters": {}}),
            ("update_atom", {"mode": "execute", "parameters": {}}),
        ):
            response = await self.gateway.call(
                None, SimpleNamespace(name=name, arguments={"request": request})
            )
            self.assertEqual({"forwarded": True}, response.structured_content)
        self.assertEqual(3, len(self.child_calls))
        self.fixture.assert_unchanged(self)

    async def test_operator_registry_drift_during_freeze_refuses_before_form(self):
        from selected_execution import SelectedExecution

        original_freeze = SelectedExecution.freeze
        registry = self.fixture.root / ".caprmedio_caprmedio/operators_registry.toml"

        def drift(runner, request):
            frozen = original_freeze(runner, request)
            registry.write_bytes(
                registry.read_bytes() + b'\n[[operators]]\nname="Other"\nrole="owner"\n'
            )
            return frozen

        async with InMemoryTransport(self.gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=self.elicit) as client:
                await client.initialize()
                await self.stage(client)
                with patch.object(SelectedExecution, "freeze", drift):
                    response = await client.call_tool("update_atom", {"request": self.request})
        self.assertEqual("refused", response.structured_content["status"])
        self.assertEqual([], self.forms)
        self.fixture.assert_unchanged(self)
        self.assertEqual(2, len(self.child_calls))

    async def test_operator_registry_drift_during_frontier_capture_refuses_before_form(self):
        import subject_publication_confirmation as confirmation

        original_frontier = confirmation._frontier
        registry = self.fixture.root / ".caprmedio_caprmedio/operators_registry.toml"
        changed = []

        def drift(*args):
            if not changed:
                registry.write_bytes(
                    registry.read_bytes() + b'\n[[operators]]\nname="Other"\nrole="owner"\n'
                )
                changed.append(True)
            return original_frontier(*args)

        async with InMemoryTransport(self.gateway.build_server(), raise_exceptions=True) as streams:
            async with ClientSession(*streams, elicitation_callback=self.elicit) as client:
                await client.initialize()
                await self.stage(client)
                with patch.object(confirmation, "_frontier", drift):
                    response = await client.call_tool("update_atom", {"request": self.request})
        self.assertEqual("refused", response.structured_content["status"])
        self.assertEqual([], self.forms)
        self.fixture.assert_unchanged(self)
        self.assertEqual(2, len(self.child_calls))

    async def test_current_native_noop_needs_neither_stage_nor_form(self):
        from atom_subject_patch import prepare_subject_intent

        self.fixture.patches = []
        self.fixture.prepared = prepare_subject_intent(
            self.fixture.root, self.fixture.target, [], subject_profile="approved"
        )
        self.fixture.parameters = {
            "target": self.fixture.target,
            "subject_patches": [],
            "subject_intent_sha256": self.fixture.prepared["subject_intent_sha256"],
            "subject_profile": "approved",
        }
        self.fixture.golden._semantic_update_parameters = self.fixture.parameters
        _, frozen = self.fixture.execution("gateway-noop-fixture")
        response = await self.gateway.call(
            None,
            SimpleNamespace(
                name="update_atom", arguments={"request": frozen["request"]["execution"]}
            ),
        )
        self.assertEqual({"forwarded": True}, response.structured_content)
        self.assertEqual(1, len(self.child_calls))
        self.assertEqual({}, self.gateway.subject_stages)
        self.assertEqual([], self.forms)
        self.fixture.assert_unchanged(self)
