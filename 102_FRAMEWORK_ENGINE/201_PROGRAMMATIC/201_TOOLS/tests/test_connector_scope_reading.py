from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_bindings import ConnectorBindingError, ConnectorBindings, SelectedOperationAdmission, capture_source
from connector_scope_parsing import validate_scope_request
from connector_scope_reading import execute_scope_request
from test_connector_scope_parsing import SETTINGS, filters, rows, serialize_project_structure


def request(operation="read", identity="ALPHA"):
    return {"operation": operation, "target": {"kind": "Scope Unit", "identity": identity} if operation == "read" else None,
            "query": {"kind": "Scope Unit", "filters": filters(identity="demo")} if operation == "query" else None,
            "delta": None, "expected_state": None, "authorization": "fixture-read-permission",
            "context": "fixture-current-context"}


class ScopeReadingTests(unittest.TestCase):
    """Actual file observations with native admission mocked, never runtime proof."""

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(dir=Path.cwd() / ".caprmedio_tmp")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir()
        self.settings_path, self.structure_path = self.control / "caprmedio_project_settings.toml", self.control / "project_structure.toml"
        self.settings_path.write_text(SETTINGS, encoding="utf-8")
        self.structure_path.write_text(serialize_project_structure(rows()), encoding="utf-8")
        self.authority = self.root / "accepted-schema.md"
        self.authority.write_text("independently fixed fixture schema authority", encoding="utf-8")
        self.calls = []
        # Isolate reader mechanics; the existing selected-service admission has
        # separate tests and is deliberately not claimed by this fixture.
        self.admission = object.__new__(SelectedOperationAdmission)
        self.admission_patch = patch.object(SelectedOperationAdmission, "check", self.admit)
        self.admission_patch.start()
        self.addCleanup(self.admission_patch.stop)
        self.sources = self.capture()
        self.binding = self.make_binding()

    def admit(self, value):
        self.calls.append(copy.deepcopy(value))
        if value["authorization"] != "fixture-read-permission":
            raise ConnectorBindingError("permission_denied", "Read permission is not bound.", "authorization")
        if value["context"] != "fixture-current-context":
            raise ConnectorBindingError("input_invalid", "Context is not bound.", "context")

    def capture(self):
        return tuple(capture_source(self.root, path.relative_to(self.root))
                     for path in (self.settings_path, self.structure_path))

    def make_binding(self, resolver=None):
        return ConnectorBindings(self.admission, supported_operations={"query", "read"}, supported_kinds={"Scope Unit"},
            validate_payload=validate_scope_request, resolve_sources=resolver or (lambda value: self.sources),
            authority_sources=[capture_source(self.root, self.authority.relative_to(self.root))])

    def run_request(self, value=None, **kwargs):
        return execute_scope_request(request() if value is None else value,
            bindings=kwargs.pop("bindings", self.binding), project_name=kwargs.pop("project_name", "demo"),
            source_view=kwargs.pop("source_view", "current"), **kwargs)

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.root.rglob("*") if path.is_file()}

    def assert_error(self, result, code):
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["errors"][0]["code"], code)

    def test_complete_independent_reads_and_no_effects(self):
        before = self.snapshot()
        for identity, declaration in [("demo", {"name": "demo", "key": "demo", "obsolete_names": ["old"]}),
                                      *[(row["scope_unit_name"], row) for row in rows()]]:
            result = self.run_request(request(identity=identity))
            self.assertEqual(result["data"], {"identity": identity, "declaration": declaration})
            self.assertEqual(result["errors"], [])
            self.assertEqual(result["effects"], [])
            self.assertNotIn(str(self.root), str(result))
            self.assertNotIn("relative_path", str(result["current_state"]))
        self.assertEqual(before, self.snapshot())
        self.assertFalse(any("query" == value["operation"] for value in self.calls))

    def test_query_complete_coverage_and_pinning(self):
        before = self.snapshot()
        value = request("query")
        result = self.run_request(value)
        self.assertEqual([item["identity"] for item in result["data"]["matches"]], ["ALPHA", "BETA", "CHILD", "demo"])
        self.assertEqual(result["errors"], [])
        self.assertTrue(result["data"]["coverage"]["complete"])
        value["expected_state"] = copy.deepcopy(result["current_state"])
        self.assertEqual(self.run_request(value), result)
        value["expected_state"]["source_evidence"]["project_structure"]["sha256"] = "0" * 64
        self.assert_error(self.run_request(value), "stale_state")
        self.assertEqual(before, self.snapshot())

    def test_historical_exact_view_and_missing_history(self):
        historical = self.root / "retained-history"
        historical.mkdir()
        history_settings, history_structure = historical / "settings.toml", historical / "structure.toml"
        history_settings.write_text(SETTINGS, encoding="utf-8")
        historic_rows = rows(); historic_rows[0]["scope_unit_label"] = "OLD"
        history_structure.write_text(serialize_project_structure(historic_rows), encoding="utf-8")
        sources = tuple(capture_source(self.root, path.relative_to(self.root)) for path in (history_settings, history_structure))
        binding = self.make_binding(lambda value: sources)
        value = request()
        state = {"project": "demo", "source_view": "retained-fixture", "source_evidence": {
            "project_settings": {"sha256": sources[0].sha256}, "project_structure": {"sha256": sources[1].sha256}}}
        value["expected_state"] = state
        result = self.run_request(value, bindings=binding, source_view="retained-fixture")
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["data"]["declaration"]["scope_unit_label"], "OLD")
        self.assertEqual(result["current_state"], state)
        value["expected_state"] = None
        self.assert_error(self.run_request(value, bindings=binding, source_view="retained-fixture"), "input_invalid")
        history_structure.unlink()
        self.assert_error(self.run_request(value, bindings=binding, source_view="retained-fixture"), "stale_state")

    def test_stale_pin_and_authority_are_refused(self):
        before = self.snapshot()
        self.structure_path.write_text(self.structure_path.read_text() + "\n# concurrent observation\n", encoding="utf-8")
        changed = self.snapshot()
        self.assert_error(self.run_request(), "stale_state")
        self.assertEqual(changed, self.snapshot())
        self.assertNotEqual(before, changed)
        self.sources = self.capture()
        self.authority.write_text("changed schema", encoding="utf-8")
        self.assert_error(self.run_request(), "stale_state")

    def test_drift_before_completion_has_incomplete_query_coverage(self):
        calls = 0
        original = self.admit
        def drift(admission, value):
            nonlocal calls
            calls += 1
            original(value)
            if calls == 2:
                self.structure_path.write_text(self.structure_path.read_text() + "\n# drift\n", encoding="utf-8")
        with patch.object(SelectedOperationAdmission, "check", drift):
            result = self.run_request(request("query"))
        self.assert_error(result, "stale_state")
        self.assertFalse(result["data"]["coverage"]["complete"])

    def test_invalid_missing_denied_and_backend_results_have_no_effects(self):
        before = self.snapshot()
        cases = [(request(identity="MISSING"), "target_not_found"),
                 ({**request(), "authorization": "unbound"}, "permission_denied"),
                 ({**request(), "context": "unbound"}, "input_invalid"),
                 ({**request(), "delta": {"unexpected": True}}, "input_invalid"),
                 ({**request(), "target": {"kind": "Atom", "identity": "ALPHA"}}, "input_invalid"),
                 ({**request(), "operation": "create"}, "unsupported_operation")]
        for value, code in cases:
            with self.subTest(value=value):
                result = self.run_request(value)
                self.assert_error(result, code)
                self.assertIsNone(result["data"])
        absent = capture_source(self.root, "missing.toml")
        self.assert_error(self.run_request(bindings=self.make_binding(lambda value: (self.sources[0],))), "backend_failure")
        self.assert_error(self.run_request(bindings=self.make_binding(lambda value: (self.sources[0], absent))), "backend_failure")
        self.assert_error(self.run_request(bindings=self.make_binding(lambda value: (self.sources[0], self.sources[0]))), "target_ambiguous")
        self.assert_error(self.run_request(project_name="another-project"), "schema_invalid")
        self.assertEqual(before, self.snapshot())

    def test_schema_and_escaping_declared_binding_refusals(self):
        self.structure_path.write_text(serialize_project_structure(rows()) + 'node_id = "invented"\n', encoding="utf-8")
        self.sources = self.capture()
        self.assert_error(self.run_request(), "schema_invalid")
        outside = Path(self.directory.name).parent
        (self.root / "escape").symlink_to(outside, target_is_directory=True)
        values = rows(); values[0]["delivery_path"] = "escape/ALPHA"
        self.structure_path.write_text(serialize_project_structure(values), encoding="utf-8")
        self.sources = self.capture()
        self.assert_error(self.run_request(), "schema_invalid")


if __name__ == "__main__":
    unittest.main()
