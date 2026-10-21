"""Direct, root-bound Subject lookup through the canonical provider."""
from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import yaml

TOOLS = Path(__file__).resolve().parents[2]
APP_TESTS = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"
for directory in (TOOLS, TOOLS / "ATOM_SEARCH", TOOLS / "ATOM_UPDATE/tests", APP_TESTS):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import atom_search as provider  # noqa: E402
from frozen_selected_workflows import frozen_behavior_bindings, frozen_source_bytes  # noqa: E402
from project_selection import bind_selection, resolve_project  # noqa: E402
from subject_notation import get_profile  # noqa: E402
from subject_grammar_corpus import grammar_carriers  # noqa: E402
import test_subject_lookup as fixtures  # noqa: E402


class SubjectLookupProviderTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SubjectLookupTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        self.settings.write_text('[project]\nname = "Lookup fixture"\n' + self.settings.read_text(), encoding="utf-8")
        self.structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        self.structure.write_text(self.structure.read_text() + 'delivery_path = ".caprmedio_caprmedio/core"\n', encoding="utf-8")
        behavior_bindings = frozen_behavior_bindings()
        for pin in provider.SOURCE_PINS:
            binding = behavior_bindings[pin["atom_id"]]
            self.assertEqual(pin["path"], binding["source_path"])
            destination = self.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            raw = frozen_source_bytes(pin["path"], binding["sha256"])
            destination.write_bytes(raw)
            self.assertEqual(raw, destination.read_bytes())
        grammar = grammar_carriers()
        for profile in ("legacy", "approved"):
            for pin in get_profile(profile).grammar_pins:
                destination = self.root / pin.path
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(grammar[pin.path])
                self.assertEqual(grammar[pin.path], destination.read_bytes())
        self.adapter = provider.create_adapter(self.root)
        self.request = {"subject": "Core/Atom", "subject_field": "both", "subject_match": "prefix",
                        "subject_profile": "legacy", "scope_unit": "CORE",
                        "content_roles": ["Requirement"], "lifecycle": "active"}

    def ledger(self):
        return {p.relative_to(self.root).as_posix(): (p.read_bytes(), p.stat().st_mode & 0o777)
                for p in self.root.rglob("*") if p.is_file()}

    def invoke(self, request=None):
        before = self.ledger()
        result = self.adapter.invoke(self.request if request is None else request).model_dump(mode="json")
        self.assertEqual(before, self.ledger())
        self.assertFalse((self.root / ".caprmedio_tmp").exists())
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        return result

    def test_direct_matches_closed_public_pins_and_no_effects(self):
        result = self.invoke()
        self.assertEqual({"data", "current_state", "effects", "errors"}, set(result))
        self.assertEqual([], result["effects"])
        self.assertEqual([], result["errors"])
        self.assertTrue(result["data"]["complete"])
        self.assertEqual([("CA-R-1", 1, "depends_on", "Core/Atom/child"), ("CA-R-1", 1, "governs", "Core/Atom")],
                         [(m["atom_id"], m["version"], m["field"], m["value"]) for m in result["data"]["matches"]])
        for match in result["data"]["matches"]:
            self.assertEqual({"atom_id", "version", "status", "current_scope_unit", "updated_at", "field", "value"}, set(match))
        self.assertEqual(1, len(result["current_state"]))
        state = result["current_state"][0]
        source = next(self.fixture.role.glob("CA-R-1-*.md"))
        self.assertEqual({"identity": "CA-R-1", "version": 1, "source_token": hashlib.sha256(source.read_bytes()).hexdigest(),
                          "source_view": {"scope_unit": "CORE", "content_roles": ["Requirement"], "lifecycle": "active"}}, state)
        for pin in result["data"]["subject_profile_evidence"]["grammar_pins"]:
            self.assertEqual({"atom_id", "version", "sha256"}, set(pin))
        self.assertEqual("not_performed", result["data"]["subject_profile_evidence"]["native_admission"])

    def test_request_refuses_defaults_unknown_physical_fields_and_duplicates_before_lookup(self):
        requests = [{key: value for key, value in self.request.items() if key != missing} for missing in self.request]
        requests += [{**self.request, key: value} for key, value in (
            ("root", str(self.root)), ("under", ".caprmedio_caprmedio"), ("path", "source.md"),
            ("mode", "preview"), ("session_id", "session"), ("authorization", True),
            ("content_roles", []), ("content_roles", ["Requirement", "Requirement"]),
            ("atom_ids", ["CA-R-1", "CA-R-1"]), ("atom_ids", ["source.md"]), ("subject_profile", None),
        )]
        with patch.object(provider, "run_subject_search", side_effect=AssertionError("invalid request reached lookup")):
            for request in requests:
                with self.subTest(request=request):
                    result = self.invoke(request)
                    self.assertIsNone(result["data"])
                    self.assertIsNone(result["current_state"])
                    self.assertTrue(result["errors"])
                    self.assertEqual("input_invalid", result["errors"][0]["code"])

    def test_logical_id_filter_and_empty_matches_have_complete_empty_state(self):
        result = self.invoke({**self.request, "atom_ids": ["CA-R-2"]})
        self.assertEqual([], result["data"]["matches"])
        self.assertEqual([], result["current_state"])
        self.assertEqual([], result["errors"])
        self.assertEqual(self.invoke(), self.invoke({**self.request, "atom_ids": []}))

    def test_selected_malformed_subjects_are_reported_without_partial_matches(self):
        source = next(self.fixture.role.glob("CA-R-2-*.md"))
        source.write_bytes(source.read_bytes().replace(b'subjects:', b'subjects: invalid\ninvalid_subjects:'))
        result = self.invoke()
        self.assertEqual(["schema_invalid"], [error["code"] for error in result["errors"]])
        self.assertEqual(
            [("CA-R-1", 1, "depends_on", "Core/Atom/child"), ("CA-R-1", 1, "governs", "Core/Atom")],
            [(row["atom_id"], row["version"], row["field"], row["value"])
             for row in result["data"]["matches"]],
        )
        self.assertFalse(result["data"]["complete"])
        warnings = result["data"]["warnings"]
        self.assertIsInstance(warnings, list)
        warning = next((item for item in warnings if item.get("path") == source.relative_to(self.root).as_posix()), None)
        self.assertIsNotNone(warning, warnings)
        self.assertIsInstance(warning.get("reason"), str)
        self.assertTrue(warning["reason"])

    def test_invalid_current_contract_identity_refuses_without_lookup(self):
        source = self.root / provider.SOURCE_PINS[0]["path"]
        source.write_bytes(source.read_bytes().replace(b"CA-R-1936", b"CA-R-99999", 1))
        with patch.object(provider, "run_subject_search", side_effect=AssertionError("stale contract reached lookup")):
            result = self.invoke()
        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual("stale_state", result["errors"][0]["code"])

    def test_subjects_and_version_updates_are_read_on_next_call_in_same_adapter(self):
        first = self.invoke()
        source = self.root / provider.SOURCE_PINS[0]["path"]
        parsed = provider.parse_carrier(source.read_bytes(), source)
        metadata = {**parsed.metadata, "version": parsed.metadata["version"] + 1}
        metadata["subjects"] = {**metadata["subjects"], "governs": "Connector.Interface"}
        source.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + parsed.body)
        second = self.invoke()
        self.assertEqual([], second["errors"])
        self.assertEqual(first["data"]["matches"], second["data"]["matches"])

    def test_contract_changed_during_lookup_is_stale_without_replay(self):
        source = self.root / provider.SOURCE_PINS[0]["path"]
        actual = provider.run_subject_search

        def lookup_then_change(*args, **kwargs):
            value = actual(*args, **kwargs)
            source.write_bytes(source.read_bytes() + b"\nConcurrent current-rule drift.\n")
            return value

        with patch.object(provider, "run_subject_search", side_effect=lookup_then_change) as search:
            result = self.adapter.invoke(self.request).model_dump(mode="json")
        self.assertEqual(1, search.call_count)
        self.assertEqual("stale_state", result["errors"][0]["code"])
        self.assertIsNone(result["data"])
        self.assertEqual([], result["effects"])

    def test_descriptor_and_binding_are_effect_free_and_canonical(self):
        before = self.ledger()
        descriptor = provider.describe_tool()
        self.assertEqual(before, self.ledger())
        self.assertEqual("ATOM_SEARCH", descriptor["identity"]["name"])
        self.assertEqual({"read_only_hint": True, "destructive_hint": False,
                          "idempotent_hint": True, "open_world_hint": False}, descriptor["effect_hints"])
        binding = {"name": "ATOM_SEARCH", "mcp_name": "atom_search", "entrypoint": provider.ENTRYPOINT,
                   "source_atom": "CA-D-424", "action_ids": ["CA-O-046"]}
        self.assertTrue(provider.binding_is_admitted(binding))
        wrong = copy.deepcopy(binding)
        wrong["action_ids"] = ["CA-O-047"]
        self.assertFalse(provider.binding_is_admitted(wrong))

    def foreign_project(self):
        control = self.root / ".caprmedio_caprmedio/nested/.caprmedio_foreign"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "Foreign"\n[paths]\ncontrol_root = ".caprmedio_foreign"\n', encoding="utf-8")
        (control / "project_structure.toml").write_text("schema_version = 1\nscope_units = []\n", encoding="utf-8")
        return control.relative_to(self.root).as_posix() + "/core"

    def test_declared_scope_crossing_actual_nested_project_is_refused(self):
        foreign = self.foreign_project()
        self.structure.write_text(self.structure.read_text().replace(".caprmedio_caprmedio/core", foreign), encoding="utf-8")
        with patch.object(provider, "run_subject_search", side_effect=AssertionError("foreign Project reached lookup")):
            result = self.invoke()
        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual("stale_state", result["errors"][0]["code"])
        self.assertNotIn(foreign, result["errors"][0]["message"])

    def test_stale_bound_structure_cannot_introduce_an_unverified_foreign_declaration(self):
        selection = resolve_project(self.root)
        foreign = self.foreign_project()
        self.structure.write_text(self.structure.read_text() + '\n[[scope_units]]\nscope_unit_name = "FOREIGN"\n'
                                  + f'authority_path = "{foreign}"\ndelivery_path = "{foreign}"\n', encoding="utf-8")
        with bind_selection(selection), patch.object(provider, "run_subject_search", side_effect=AssertionError("stale selection reached lookup")):
            result = self.invoke()
        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual("stale_state", result["errors"][0]["code"])


if __name__ == "__main__":
    unittest.main()
