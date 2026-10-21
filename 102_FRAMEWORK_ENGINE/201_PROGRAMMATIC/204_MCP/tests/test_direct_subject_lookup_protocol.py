"""Real registered Subject lookup protocol; no Session, Run or freshness mocks."""

from __future__ import annotations

from contextlib import asynccontextmanager
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
REPOSITORY = MCP_ROOT.parents[2]
APP_TESTS = MCP_ROOT.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS", TOOLS_ROOT / "ATOM_UPDATE/tests", APP_TESTS):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import implementation_server  # noqa: E402
import atom_subject_lookup as lookup  # noqa: E402
from ATOM_SEARCH import atom_search as provider  # noqa: E402
from frozen_selected_workflows import frozen_behavior_bindings, frozen_source_bytes  # noqa: E402
from subject_notation import get_profile  # noqa: E402
from subject_grammar_corpus import grammar_carriers  # noqa: E402


PRMEDO = ["Plan", "Requirement", "Method", "Evaluation", "Delivery", "Operations"]
KINDS = dict(zip(PRMEDO, "PRMEDO"))
ROLE_FOLDERS = {"Plan": "03_plan", "Requirement": "04_requirement", "Method": "05_method",
                "Evaluation": "06_evaluation", "Delivery": "07_delivery", "Operations": "09_operations"}
REQUIRED = {"subject", "subject_field", "subject_match", "subject_profile", "scope_unit",
            "content_roles", "lifecycle"}
CONTROL = ".caprmedio_caprmedio"
TEMP_ROOT = REPOSITORY / ".caprmedio_tmp/tests/test_direct_subject_lookup_protocol"


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _snapshot(root: Path) -> dict[str, str]:
    """Directories and file bytes detect even an empty recording directory."""
    result = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            result[relative] = "symlink:" + str(path.readlink())
        elif path.is_dir():
            result[relative] = "directory"
        else:
            result[relative] = "file:" + _digest(path.read_bytes())
    return result


def _keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from _keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from _keys(child)


class DirectSubjectLookupProtocolTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / ".git").mkdir()
        control = self.root / CONTROL
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            '[project]\nkey = "direct-subject-fixture"\nname = "direct-subject-fixture"\n'
            'repository_slug = "direct-subject-fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n', encoding="utf-8",
        )
        structure = "schema_version = 1\n"
        for name, relative in (
            ("TEST_LOOKUP", CONTROL + "/lookup"),
            ("CORE_META_MODEL", CONTROL + "/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
             "METHODOLOGY_SOURCES/001_CORE_META_MODEL"),
            ("CONNECTOR_TOOLS", CONTROL + "/102_LAYER_2_FRAMEWORK_ENGINE/"
             "201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS"),
        ):
            structure += (f'[[scope_units]]\nscope_unit_name = "{name}"\nauthority_path = "{relative}"\n'
                          f'delivery_path = "{relative}"\n')
        (control / "project_structure.toml").write_text(structure, encoding="utf-8")
        # Copy each frozen selected authority into the disposable Project.
        behavior_bindings = frozen_behavior_bindings()
        for pin in provider.SOURCE_PINS:
            binding = behavior_bindings[pin["atom_id"]]
            self.assertEqual(pin["path"], binding["source_path"])
            self._copy_pin(pin["path"], frozen_source_bytes(pin["path"], binding["sha256"]), binding["sha256"])
        grammar = grammar_carriers()
        for name in ("legacy", "approved"):
            for pin in get_profile(name).grammar_pins:
                raw = grammar[pin.path]
                self._copy_pin(pin.path, raw, _digest(raw))
        self.paths = {}
        for role, kind in KINDS.items():
            atom_id = f"CA-{kind}-9200"
            self.paths[atom_id] = self._write_atom(atom_id, role)
        self._write_atom("CA-R-9201", "Requirement", governs="Other", dependencies=[])
        for kind, folder in (("C", "01_concern"), ("A", "02_analysis")):
            excluded = control / "lookup" / folder
            excluded.mkdir()
            (excluded / f"CA-{kind}-9299-TEST--unrelated-malformed.md").write_text(
                f"---\natom_id: [unrelated-{kind}\ncontent_role: broken\n---\nAtom.Status\n",
                encoding="utf-8",
            )
        self.request = {
            "subject": "Atom.Status", "subject_field": "both", "subject_match": "exact",
            "subject_profile": "approved", "scope_unit": "TEST_LOOKUP",
            "content_roles": PRMEDO.copy(), "lifecycle": "active",
        }

    def _copy_pin(self, relative: str, raw: bytes, expected: str) -> None:
        self.assertEqual(expected, _digest(raw), f"frozen fixture pin stale: {relative}")
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
        self.assertEqual(raw, destination.read_bytes())

    def _write_atom(self, atom_id, role, *, governs="Atom.Status", dependencies=None,
                    owner="TEST_LOOKUP", parent=None):
        parent = parent or self.root / CONTROL / "lookup" / ROLE_FOLDERS[role]
        parent.mkdir(parents=True, exist_ok=True)
        path = parent / f"{atom_id}-TEST-{role.upper()}--fixture.md"
        dependencies = ["Atom/Plan.Status", "Other"] if dependencies is None else dependencies
        # No Type: direct PRMEDO lookup must not adopt unrelated header migration.
        path.write_text(
            f"---\natom_id: {atom_id}\nversion: 1\nstatus: Active\ncontent_role: {role}\n"
            f"current_scope_unit: {owner}\nupdated_at: '2026-10-14 12:00:00 +0300'\n"
            f"subjects:\n  governs: {json.dumps(governs)}\n  depends_on: {json.dumps(dependencies)}\n"
            "---\n# Summary\nAtom.Status body text is not a Subject occurrence.\n",
            encoding="utf-8",
        )
        return path

    @asynccontextmanager
    async def _session(self):
        before = _snapshot(self.root)
        server = implementation_server.create_server(self.root)
        self.assertEqual(before, _snapshot(self.root), "registration must be effect-free")
        async with InMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams) as session:
                await session.initialize()
                yield session

    async def _call(self, session, request):
        before = _snapshot(self.root)
        response = await session.call_tool("atom_search", {"request": request})
        self.assertEqual(before, _snapshot(self.root), "lookup changed Project bytes or membership")
        return response

    def _assert_public(self, response):
        self.assertFalse(response.is_error, response)
        result = response.structured_content
        self.assertEqual({"data", "current_state", "effects", "errors"}, set(result))
        self.assertEqual([], result["effects"])
        logical = {**result, "data": None if result["data"] is None else
                   {key: value for key, value in result["data"].items() if key != "warnings"}}
        self.assertFalse({"path", "relative_path", "source_path", "index"} & set(_keys(logical)))
        for warning in (result["data"] or {}).get("warnings", []):
            self.assertEqual({"code", "path", "reason"}, set(warning))
            self.assertIn(warning["code"], {"schema_invalid", "diagnostic_logging_failed"})
            path = Path(warning["path"])
            self.assertFalse(path.is_absolute())
            self.assertNotIn("..", path.parts)
        self.assertNotIn(self.root.as_posix(), json.dumps(result), "public result leaked a private root")
        return result

    def _assert_refusal(self, response, code=None):
        result = self._assert_public(response)
        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertTrue(result["errors"])
        for error in result["errors"]:
            self.assertEqual({"code", "message", "field"}, set(error))
        if code is not None:
            self.assertIn(code, {error["code"] for error in result["errors"]})

    async def test_production_registration_exposes_closed_schema_and_readonly_hints(self):
        async with self._session() as session:
            tools = (await session.list_tools()).tools
            matches = [tool for tool in tools if tool.name == "atom_search"]
            self.assertEqual(1, len(matches))
            tool = matches[0]
            schema = tool.input_schema
            self.assertEqual(["request"], schema["required"])
            self.assertEqual({"request"}, set(schema["properties"]))
            request_schema = schema["properties"]["request"]
            if "$ref" in request_schema:
                request_schema = schema
                for part in schema["properties"]["request"]["$ref"].split("/")[1:]:
                    request_schema = request_schema[part]
            self.assertEqual(REQUIRED, set(request_schema["required"]))
            self.assertEqual(REQUIRED | {"atom_ids"}, set(request_schema["properties"]))
            self.assertFalse(request_schema["additionalProperties"])
            self.assertTrue(tool.annotations.read_only_hint)
            self.assertFalse(tool.annotations.destructive_hint)
            self.assertTrue(tool.annotations.idempotent_hint)
            self.assertFalse(tool.annotations.open_world_hint)

    async def test_real_call_returns_only_logical_matches_and_actual_source_hashes(self):
        async with self._session() as session:
            result = self._assert_public(await self._call(session, self.request))
        self.assertEqual([], result["errors"])
        data = result["data"]
        self.assertTrue(data["complete"])
        expected = [{"atom_id": atom_id, "version": 1, "status": "Active",
                     "current_scope_unit": "TEST_LOOKUP", "updated_at": "2026-10-14 12:00:00 +0300",
                     "field": "governs", "value": "Atom.Status"} for atom_id in sorted(self.paths)]
        self.assertEqual(expected, data["matches"])
        self.assertEqual("approved", data["subject_profile"])
        evidence = data["subject_profile_evidence"]
        self.assertEqual("not_performed", evidence["native_admission"])
        self.assertEqual(5, len(evidence["grammar_pins"]))
        for pin in evidence["grammar_pins"]:
            self.assertEqual({"atom_id", "version", "sha256"}, set(pin))
        self.assertEqual(sorted(self.paths), [state["identity"] for state in result["current_state"]])
        for state in result["current_state"]:
            self.assertEqual({"identity", "version", "source_token", "source_view"}, set(state))
            self.assertEqual(1, state["version"])
            self.assertEqual(_digest(self.paths[state["identity"]].read_bytes()), state["source_token"])
            self.assertEqual({"scope_unit": "TEST_LOOKUP", "content_roles": PRMEDO, "lifecycle": "active"},
                             state["source_view"])

    async def test_all_four_modes_and_fields_use_literal_matches_without_body_hits(self):
        cases = [
            ("Atom.Status", "exact", "governs", [("governs", "Atom.Status")]),
            ("Atom", "prefix", "both", [("depends_on", "Atom/Plan.Status"), ("governs", "Atom.Status")]),
            (".Status", "suffix", "depends_on", [("depends_on", "Atom/Plan.Status")]),
            ("Status", "contains", "both", [("depends_on", "Atom/Plan.Status"), ("governs", "Atom.Status")]),
        ]
        async with self._session() as session:
            for subject, mode, field, values in cases:
                with self.subTest(mode=mode, field=field):
                    request = {**self.request, "subject": subject, "subject_match": mode, "subject_field": field}
                    result = self._assert_public(await self._call(session, request))
                    self.assertEqual([], result["errors"])
                    expected = [(atom_id, field_name, value) for atom_id in sorted(self.paths)
                                for field_name, value in values]
                    self.assertEqual(expected, [(row["atom_id"], row["field"], row["value"])
                                                for row in result["data"]["matches"]])
                    self.assertEqual(6, len(result["current_state"]))

    async def test_valid_empty_and_explicit_full_id_filter_are_successful(self):
        async with self._session() as session:
            empty = self._assert_public(await self._call(session, {**self.request, "subject": "Atom.State"}))
            self.assertEqual([], empty["errors"])
            self.assertEqual([], empty["data"]["matches"])
            self.assertEqual([], empty["current_state"])
            one = self._assert_public(await self._call(session, {**self.request, "atom_ids": ["CA-R-9200"]}))
            self.assertEqual(["CA-R-9200"], [row["atom_id"] for row in one["data"]["matches"]])

    async def test_closed_request_rejects_physical_effect_and_ambiguous_inputs(self):
        invalid = [{key: value for key, value in self.request.items() if key != "lifecycle"}]
        invalid.extend({**self.request, **delta} for delta in (
            {"path": "outside.md"}, {"index": 0}, {"session_id": "invented"}, {"operation": "modify"},
            {"context": "invented"}, {"authorization": "invented"}, {"subject_match": "regex"},
            {"content_roles": []}, {"content_roles": ["Requirement", "Requirement"]},
            {"atom_ids": ["9200"]}, {"atom_ids": ["CA-R-9200", "CA-R-9200"]},
            {"subject": 1}, {"lifecycle": "unknown"},
        ))
        async with self._session() as session:
            with patch.object(lookup, "run_subject_search", wraps=lookup.run_subject_search) as search:
                for request in invalid:
                    with self.subTest(request=request):
                        self.assertTrue((await self._call(session, request)).is_error)
                search.assert_not_called()

    async def test_selected_malformed_carrier_warns_and_preserves_other_matches(self):
        self.paths["CA-R-9200"].write_text("---\natom_id: [CA-R-9200\n---\n", encoding="utf-8")
        async with self._session() as session:
            result = self._assert_public(await self._call(session, self.request))
        self.assertEqual([], result["errors"])
        self.assertFalse(result["data"]["complete"])
        self.assertEqual(sorted(set(self.paths) - {"CA-R-9200"}),
                         [match["atom_id"] for match in result["data"]["matches"]])
        warnings = result["data"]["warnings"]
        self.assertEqual(1, len(warnings))
        self.assertEqual("schema_invalid", warnings[0]["code"])
        self.assertEqual(self.paths["CA-R-9200"].relative_to(self.root).as_posix(), warnings[0]["path"])

    async def test_selected_identity_claim_hidden_in_excluded_role_refuses(self):
        excluded = self.root / CONTROL / "lookup/01_concern/CA-C-9299-TEST--unrelated-malformed.md"
        excluded.write_text(
            "---\natom_id: CA-R-9200\ncontent_role: Concern\nsubjects: [broken\n---\n",
            encoding="utf-8",
        )
        async with self._session() as session:
            self._assert_refusal(await self._call(session, self.request), "target_ambiguous")

    async def test_foreign_owner_and_symlink_sources_refuse_without_widening(self):
        async with self._session() as session:
            self._assert_refusal(await self._call(session, {**self.request, "scope_unit": "UNKNOWN"}))
        self.paths["CA-R-9200"].unlink()
        self.paths["CA-R-9200"].symlink_to(self.paths["CA-M-9200"])
        async with self._session() as session:
            self._assert_refusal(await self._call(session, self.request))

    async def test_changed_registered_delivery_is_refused_by_real_registry_freshness(self):
        async with self._session() as session:
            delivery = next(pin for pin in provider.SOURCE_PINS if pin["atom_id"] == "CA-D-424")
            path = self.root / delivery["path"]
            path.write_bytes(path.read_bytes() + b"\nChanged after registration.\n")
            response = await self._call(session, self.request)
            self.assertTrue(response.is_error, response)

    async def test_real_final_currentness_refuses_midread_source_change_without_tool_writes(self):
        async with self._session() as session:
            target = self.paths["CA-R-9200"]
            original_currentness = lookup.ReadContext.currentness
            expected = {}

            def change_then_check(reader):
                if not expected and str(target) in reader.fingerprints:
                    target.write_bytes(target.read_bytes() + b"\nExternal concurrent source change.\n")
                    expected.update(_snapshot(self.root))
                return original_currentness(reader)

            with patch.object(lookup.ReadContext, "currentness", change_then_check):
                response = await session.call_tool("atom_search", {"request": copy.deepcopy(self.request)})
            self.assertTrue(expected, "the real currentness boundary must be reached")
            self.assertEqual(expected, _snapshot(self.root), "lookup wrote after external fixture change")
            self._assert_refusal(response, "stale_state")


if __name__ == "__main__":
    unittest.main()
