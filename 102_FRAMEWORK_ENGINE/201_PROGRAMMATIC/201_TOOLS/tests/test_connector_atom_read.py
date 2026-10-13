from __future__ import annotations

import dataclasses
import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_atom_parse import parse_atom, subject_matches
from connector_atom_read import AtomReadError, AtomSourceView, query_atoms, read_atom
from connector_contract import validate_result
from connector_atom_dispatch import execute_atom_request
from connector_bindings import ConnectorBindings, SelectedOperationAdmission, capture_source
from workflow_run_support import RunTracker, _canonical_digest


class AtomConnectorTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[4] / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.control = self.root / ".caprmedio_caprmedio"
        self.owner = self.control / "units" / "CORE"
        self.other = self.control / "units" / "OTHER"
        self.owner.mkdir(parents=True)
        self.other.mkdir(parents=True)
        self.view = AtomSourceView(self.root, self.control, {"CORE": self.owner, "OTHER": self.other},
                                   ("CORE",), ("active", "done", "resolved", "canceled"),
                                   "current", "approved", (), "fixture-source-view")
        self.first = self.write("CA-R-1", "Thing/Part", ["Atom", "atom(atom_id=\"CA-R-1\")"], status="Backlog")
        self.second = self.write("CA-R-2", "Other", ["Thing/Part"], placement="done", status="Done")

    def write(self, identity, governs, dependencies, *, placement="", status="Active", version=1, owner="CORE"):
        base = self.owner if owner == "CORE" else self.other
        directory = base / "04_requirement" / placement
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{identity}--fixture{'@' + str(version) if placement == 'archive' else ''}.md"
        raw = (f"---\natom_id: {identity}\ncontent_role: Requirement\ntype: Requirement\n"
               f"current_scope_unit: {owner}\nstatus: {status}\nversion: {version}\n"
               'updated_at: "2026-10-13 01:00:00 +0400"\n'
               f"subjects:\n  governs: {governs}\n  depends_on: {dependencies!r}\n"
               "extra: keep exactly\n---\n# Summary\n\nFixture\n\n## Detail\n\nComplete body.\n").encode()
        path.write_bytes(raw)
        return path

    def filters(self, value="Thing/Part", mode="exact", fields=None):
        return {"scope_units": ["CORE"], "lifecycles": list(self.view.lifecycles),
                "subjects": [{"fields": fields or ["governs", "depends_on"], "match": mode, "value": value}],
                "result_fields": ["status", "subjects"]}

    def request(self, operation="read"):
        return {"operation": operation, "target": {"kind": "Atom", "identity": "CA-R-1"} if operation == "read" else None,
                "query": {"kind": "Atom", "filters": self.filters()} if operation == "query" else None,
                "delta": None, "expected_state": None, "authorization": "permission.md", "context": "fixture-source-view"}

    def bindings(self, request, *, mapping=True, pins=None, validator=None):
        for name in ("manifest.json", "schema.md", "permission.md"):
            (self.root / name).write_text(name, encoding="utf-8")
        def digest(name):
            return hashlib.sha256((self.root / name).read_bytes()).hexdigest()
        manifest = {"manifest_ref": "manifest.json", "manifest_digest": digest("manifest.json")}
        def observe(outer):
            return {"selected": outer["operation_route"] == "fixture-atom-read", "current": digest("manifest.json") == manifest["manifest_digest"],
                    "observed": {"manifest_digest": digest("manifest.json")}}
        def never_execute(*args):
            raise AssertionError("Inner read cannot invoke an outer execution or Journal writer.")
        tracker = RunTracker(self.root, source_observer=observe, executor=never_execute)
        parameters, frontier, effects = {"connector_request": copy.deepcopy(request)}, ["CA-R-1", "CA-R-2"], []
        outer = {"mode": "preview", "request_id": "atom-fixture-" + _canonical_digest(parameters)[:12],
                 "operation_route": "fixture-atom-read", "parameters": parameters, "parameters_digest": _canonical_digest(parameters),
                 "target_frontier": frontier, "target_frontier_digest": _canonical_digest(frontier),
                 "effects": effects, "effects_digest": _canonical_digest(effects), "definition_manifest": manifest,
                 "source_freshness": {"selected_source_registry_ref": "schema.md", "selected_source_registry_version": 1,
                                      "selected_source_registry_digest": digest("schema.md"), "selected_binding_ref": "manifest.json",
                                      "selected_binding_digest": digest("manifest.json")},
                 "initiative": {"initiative_id": "fixture", "instruction_summary": "explicit Atom Query/Read fixture"}}
        preview = tracker.run_selected_operation(outer)
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"], proposal_receipt_digest=preview["proposal_receipt_digest"],
                     assigned_action_id="fixture-assigned-action", requested_runs=[{"requested_run_id": "fixture-action-run", "kind": "action",
                     "definition": {"atom_id": "CA-O-047", "version": 4, "path": "schema.md", "digest": digest("schema.md")}}])
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest", "target_frontier_digest",
                  "effects_digest", "definition_manifest", "source_freshness")
        outer["operator_authorization"] = {"authorization_ref": "permission.md", "authorization_freshness": {"state": "current", "digest": digest("permission.md")},
                                            **{key: copy.deepcopy(outer[key]) for key in fields}}
        admission = SelectedOperationAdmission(tracker, outer, map_request=(lambda value: (value["parameters"]["connector_request"], "fixture-source-view")) if mapping else None)
        sources = tuple(capture_source(self.root, p.relative_to(self.root)) for p in (self.first, self.second)) if pins is None else pins
        return ConnectorBindings(admission, supported_operations={"query", "read"}, supported_kinds={"Atom"},
                                 validate_payload=validator or (lambda value: None), resolve_sources=lambda value: sources,
                                 authority_sources=tuple(capture_source(self.root, name) for name in ("manifest.json", "schema.md", "permission.md")))

    def test_pure_parse_does_not_open_storage_and_read_is_complete(self):
        raw = self.first.read_bytes()
        with patch("builtins.open", side_effect=AssertionError("storage access")):
            self.assertEqual(parse_atom(raw).text, raw.decode())
        before = {p: p.read_bytes() for p in self.control.rglob("*.md")}
        result = read_atom("CA-R-1", self.view)
        self.assertEqual(result["data"]["source"], raw.decode())
        self.assertEqual(result["current_state"]["source_token"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(result["current_state"]["version"], 1)
        self.assertEqual(result["effects"], [])
        self.assertEqual(before, {p: p.read_bytes() for p in self.control.rglob("*.md")})
        request = {"operation": "read", "target": {"kind": "Atom", "identity": "CA-R-1"}, "query": None,
                   "delta": None, "expected_state": None, "authorization": "bound", "context": "bound"}
        self.assertEqual(validate_result(result, request=request, postconditions_verified=True), [])

    def test_query_empty_singular_multiple_and_explicit_fields(self):
        self.assertEqual(len(query_atoms(self.filters(), self.view)["data"]["matches"]), 2)
        self.assertEqual(len(query_atoms(self.filters(fields=["governs"]), self.view)["data"]["matches"]), 1)
        result = query_atoms(self.filters("absent"), self.view)
        self.assertEqual(result["data"]["matches"], [])
        self.assertTrue(result["data"]["complete"])
        self.assertEqual(result["errors"], [])
        self.assertEqual(query_atoms(self.filters(), self.view)["data"]["matches"][0]["status"], "Backlog")

    def test_literal_matching_and_prefix_boundaries(self):
        separators = ("/", ".", ":")
        for value in ("Thing/Part", "Thing.Part", "Thing:Part", "Thing"):
            self.assertTrue(subject_matches(value, "Thing", "prefix", separators))
        self.assertFalse(subject_matches("Things", "Thing", "prefix", separators))
        self.assertTrue(subject_matches("Anything", "thing", "suffix", separators))
        self.assertTrue(subject_matches("SomethingElse", "thing", "contains", separators))
        self.assertFalse(subject_matches("Atom", "atom", "exact", separators))
        self.assertEqual(len(query_atoms(self.filters("Part", "suffix"), self.view)["data"]["matches"]), 2)

    def test_read_pins_and_historical_view(self):
        observed = read_atom("CA-R-1", self.view)
        self.assertEqual(read_atom("CA-R-1", self.view, observed["current_state"]), observed)
        for expectation in ({"version": 2}, {"source_token": "stale"}):
            with self.assertRaises(AtomReadError) as error:
                read_atom("CA-R-1", self.view, expectation)
            self.assertEqual(error.exception.code, "stale_state")
        self.write("CA-R-1", "Previous", [], placement="archive", status="Archived", version=1)
        historical = dataclasses.replace(self.view, source_view="history", lifecycles=("archived",))
        self.assertIn("Previous", read_atom("CA-R-1", historical, {"version": 1})["data"]["source"])
        self.assertIn("Thing/Part", read_atom("CA-R-1", self.view)["data"]["source"])

    def test_logical_identity_and_explicit_frontier_refusals(self):
        for identity in (self.first.as_posix(), "CA-R-1.md", "Atom", "CA-R-999"):
            with self.assertRaises(AtomReadError):
                read_atom(identity, self.view)
        for key in ("scope_units", "lifecycles", "subjects", "result_fields"):
            filters = self.filters()
            del filters[key]
            with self.assertRaises(AtomReadError):
                query_atoms(filters, self.view)
        filters = self.filters()
        filters["path"] = "physical"
        with self.assertRaises(AtomReadError):
            query_atoms(filters, self.view)

    def test_historical_state_token_selects_exact_revision_without_version(self):
        first = self.write("CA-R-1", "Previous", [], placement="archive", status="Archived", version=1)
        self.write("CA-R-1", "Later", [], placement="archive", status="Archived", version=2)
        history = dataclasses.replace(self.view, source_view="history", lifecycles=("archived",))
        token = hashlib.sha256(first.read_bytes()).hexdigest()
        result = read_atom("CA-R-1", history, {"source_token": token})
        self.assertEqual(result["current_state"]["version"], 1)
        self.assertEqual(result["current_state"]["source_token"], token)
        self.assertIn("Previous", result["data"]["source"])
        with self.assertRaises(AtomReadError) as ambiguous:
            read_atom("CA-R-1", history)
        self.assertEqual(ambiguous.exception.code, "target_ambiguous")
        with self.assertRaises(AtomReadError) as stale:
            read_atom("CA-R-1", history, {"source_token": "unavailable"})
        self.assertEqual(stale.exception.code, "stale_state")

    def test_competing_identity_outside_frontier_and_installed_copy(self):
        copied = self.write("CA-R-1", "Copy", [], owner="OTHER")
        with self.assertRaises(AtomReadError) as error:
            read_atom("CA-R-1", self.view)
        self.assertEqual(error.exception.code, "target_ambiguous")
        # A verified private binding may distinguish an installed source root.
        bound = dataclasses.replace(self.view, installed_roots=(self.other,))
        self.assertEqual(read_atom("CA-R-1", bound)["current_state"]["version"], 1)
        self.assertTrue(copied.exists())

    def test_malformed_source_and_symlink_do_not_become_complete_empty(self):
        self.first.write_bytes(b"---\natom_id: CA-R-1\natom_id: CA-R-1\n---\n")
        with self.assertRaises(AtomReadError) as error:
            query_atoms(self.filters("absent"), self.view)
        self.assertEqual(error.exception.code, "schema_invalid")
        self.first.unlink()
        self.first.symlink_to(self.second)
        with self.assertRaises(AtomReadError):
            query_atoms(self.filters("absent"), self.view)

    def test_dispatch_real_admission_and_pinned_complete_frontier(self):
        for operation in ("query", "read"):
            request = self.request(operation)
            before = {path: path.read_bytes() for path in self.control.rglob("*.md")}
            result = execute_atom_request(request, self.bindings(request), self.view)
            self.assertEqual(result["errors"], [])
            self.assertEqual(set(result), {"data", "current_state", "effects", "errors"})
            self.assertEqual(result["effects"], [])
            self.assertEqual(before, {path: path.read_bytes() for path in self.control.rglob("*.md")})
            self.assertFalse((self.root / "journal").exists())

    def test_dispatch_missing_runtime_mapping_and_unpinned_frontier_fail_closed(self):
        request = self.request()
        missing = execute_atom_request(request, self.bindings(request, mapping=False), self.view)
        self.assertEqual(missing["errors"][0]["code"], "input_invalid")
        incomplete = execute_atom_request(request, self.bindings(request, pins=()), self.view)
        self.assertEqual(incomplete["errors"][0]["code"], "stale_state")
        self.assertIsNone(incomplete["data"])

    def test_dispatch_rechecks_actual_changed_source_before_success(self):
        request = self.request()
        calls = []
        original = self.first.read_bytes()
        def validator(value):
            calls.append(value)
            if len(calls) == 2:
                self.first.write_bytes(original + b"External change.\n")
        result = execute_atom_request(request, self.bindings(request, validator=validator), self.view)
        self.assertEqual(result["errors"][0]["code"], "stale_state")
        self.assertIsNone(result["data"])
        self.assertEqual(self.first.read_bytes(), original + b"External change.\n")
        self.assertEqual(result["effects"], [])


if __name__ == "__main__":
    unittest.main()
