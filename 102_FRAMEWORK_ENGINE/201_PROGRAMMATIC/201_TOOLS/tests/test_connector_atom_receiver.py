"""Private Atom receiving checks with actual accepted sources and Session starts."""

import copy
import dataclasses
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
PROJECT = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

from connector_atom_read import AtomSourceView
from connector_atom_receiver import make_atom_receiver
from connector_bindings import capture_source
from project_selection import resolve_project
from subject_notation import get_profile
from workflow_run_support import LazyRunTracker, _canonical_digest


CONTRACT_ROOT = PROJECT / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS"
CONTRACT_FILES = {
    "CA-D-625": "07_delivery/CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface.md",
    "CA-R-1936": "04_requirement/CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface.md",
    "CA-M-376": "05_method/CA-M-376-CONNECTOR_TOOLS-CORE-METHOD--execute-one-explicit-connector-operation.md",
    "CA-O-047": "09_operations/CA-O-047-CONNECTOR_TOOLS-STANDARD-ACTION--read-selected-caprmedio-atom-carriers.md",
    "CA-O-046": "09_operations/CA-O-046-CONNECTOR_TOOLS-STANDARD-ACTION--search-caprmedio-atom-carriers.md",
}


class AtomReceiverTests(unittest.TestCase):
    def setUp(self):
        scratch = PROJECT / ".caprmedio_tmp/tests/atom-receiver"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = self.root / ".caprmedio_demo"
        self.control.mkdir()
        self.settings = self.control / "caprmedio_project_settings.toml"
        self.settings.write_text('[project]\nname="demo"\nkey="demo"\n'
                                 '[paths]\ncontrol_root=".caprmedio_demo"\n'
                                 'journal_root=".caprmedio_demo/_journal"\n', encoding="utf-8")
        self.structure = self.control / "project_structure.toml"
        self.structure.write_text('schema_version=1\n' + "\n".join(
            f'[[scope_units]]\nscope_unit_name="{name}"\nparent="PROJECT"\n'
            'scope_unit_type="Unordered"\nscope_unit_label="UNIT"\nstructural_level=1\n'
            f'navigational_order_number=0\nauthority_path=".caprmedio_demo/units/{name}"\n'
            f'delivery_path="implementation/{name}"\n' for name in ("CORE", "OTHER")), encoding="utf-8")
        self.selection = resolve_project(self.root)
        self.owners = {name: self.control / "units" / name for name in ("CORE", "OTHER")}
        self.first = self.atom("CA-R-1", governs="Thing/Part", version=3)
        self.second = self.atom("CA-R-2", governs="Other", dependencies=["Thing/Part"], version=7)
        self.manifest = self.root / "manifest.json"
        self.manifest.write_bytes(b'{"fixture":"private-accepted-atom-receiver"}\n')
        self.context = {"manifest_ref": "manifest.json", "manifest_digest": self.digest(self.manifest)}
        self.view = AtomSourceView(self.root, self.control, self.owners, ("CORE",), ("active",),
                                   "current", "approved", (), self.context)
        self.authorities = {identity: self.copy_authority(CONTRACT_ROOT / relative, identity)
                            for identity, relative in CONTRACT_FILES.items()}
        self.schemas = tuple(self.authorities[identity] for identity in ("CA-D-625", "CA-R-1936", "CA-M-376"))
        self.grammar = tuple(self.copy_authority(PROJECT / pin.path, pin.atom_id, pin.path)
                             for pin in get_profile("approved").grammar_pins)
        self.sequence = 0
        self.current = True

    @staticmethod
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def copy_authority(self, source, identity, relative=None):
        path = self.root / relative if relative is not None else self.root / "receiver_authority" / (identity + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, path)
        self.assertEqual(source.read_bytes(), path.read_bytes())
        return capture_source(self.root, path.relative_to(self.root))

    def atom(self, identity, *, governs="Thing", dependencies=(), version=1, owner="CORE", archive=False):
        folder = self.owners[owner] / "04_requirement"
        if archive:
            folder /= "archive"
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{identity}--fixture{'@' + str(version) if archive else ''}.md"
        path.write_text(f"---\natom_id: {identity}\ncontent_role: Requirement\ntype: Requirement\n"
                        f"current_scope_unit: {owner}\nstatus: {'Archived' if archive else 'Active'}\nversion: {version}\n"
                        'updated_at: "2026-10-13 00:00:00 +0000"\n'
                        f"subjects:\n  governs: {governs}\n  depends_on: {list(dependencies)!r}\n"
                        "custom: preserved\n---\n# Summary\n\nImmutable full body.\n", encoding="utf-8")
        return path

    def frontier(self, paths=None):
        return tuple(capture_source(self.root, path.relative_to(self.root))
                     for path in ((self.first, self.second) if paths is None else paths))

    def receiver(self, operation="read", *, view=None, frontier=None, schemas=None):
        return make_atom_receiver(self.selection, source_view=self.view if view is None else view,
                                  source_frontier=self.frontier() if frontier is None else frontier,
                                  schema_sources=(*self.schemas, *self.grammar) if schemas is None else schemas,
                                  frontier_references=("CA-R-1", "CA-R-2"),
                                  action_definition=self.authorities["CA-O-047" if operation == "read" else "CA-O-046"])

    def inner(self, operation="read"):
        filters = {"scope_units": ["CORE"], "lifecycles": ["active"],
                   "subjects": [{"fields": ["governs", "depends_on"], "match": "exact", "value": "Thing/Part"}],
                   "result_fields": ["subjects", "status"]}
        return {"operation": operation, "target": {"kind": "Atom", "identity": "CA-R-1"} if operation == "read" else None,
                "query": {"kind": "Atom", "filters": filters} if operation == "query" else None,
                "delta": None, "expected_state": None, "authorization": "read-permission", "context": self.context}

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file() and not path.is_symlink()}

    def invoke(self, *, operation="read", request=None, receiver=None, before=None, started=True,
               finish_first=False, effects=None, definition_identity=None, frontier_references=None):
        inner = copy.deepcopy(self.inner(operation) if request is None else request)
        self.sequence += 1
        effects = [] if effects is None else effects
        frontier = ["CA-R-1", "CA-R-2"] if frontier_references is None else frontier_references
        outer = {"mode": "preview", "request_id": f"atom-receiver-{self.sequence}",
                 "operation_route": "fixture.atom-read-query", "parameters": inner,
                 "parameters_digest": _canonical_digest(inner), "target_frontier": frontier,
                 "target_frontier_digest": _canonical_digest(frontier), "effects": effects,
                 "effects_digest": _canonical_digest(effects), "definition_manifest": self.context,
                 "source_freshness": {"selected_source_registry_ref": self.schemas[0].relative_path.as_posix(),
                    "selected_source_registry_version": 3, "selected_source_registry_digest": self.schemas[0].sha256,
                    "selected_binding_ref": "manifest.json", "selected_binding_digest": self.context["manifest_digest"]},
                 "initiative": {"initiative_id": "fixture", "instruction_summary": "Read or Query the explicit accepted Atom view"}}
        receiver = self.receiver(operation) if receiver is None else receiver
        captured = {}
        def executor(request, session):
            if started:
                session.start_run("action", run_id="actual-atom-action")
            if finish_first:
                session.finish_run("actual-atom-action", outcome="completed", result_ref="read.json", effect_refs=[])
            if before:
                before(session)
            prior = self.snapshot()
            captured["result"] = receiver(session, "actual-atom-action")
            self.assertEqual(self.snapshot(), prior, "Receiver changed source or Journal bytes")
            if started and not finish_first:
                session.finish_run("actual-atom-action", outcome="failed" if captured["result"]["errors"] else "completed",
                                   result_ref="read.json", effect_refs=[])
        tracker = LazyRunTracker(self.root, source_observer=lambda request: {
            "selected": request["operation_route"] == "fixture.atom-read-query",
            "current": self.current and self.digest(self.manifest) == request["definition_manifest"]["manifest_digest"],
            "observed": {"manifest_digest": self.digest(self.manifest)}}, executor=executor,
            journal_context={"author": "trusted-reader", "timezone": "UTC"})
        preview = tracker.run_selected_operation(outer)
        source = self.authorities["CA-O-047" if operation == "read" else "CA-O-046"]
        outer.update(mode="execute", proposal_receipt=preview["proposal_receipt"],
                     proposal_receipt_digest=preview["proposal_receipt_digest"], assigned_action_id="assigned-reader",
                     requested_runs=[{"requested_run_id": "action", "kind": "action", "definition": {
                         "atom_id": definition_identity or ("CA-O-047" if operation == "read" else "CA-O-046"),
                         "version": 4 if operation == "read" else 9,
                         "path": source.relative_path.as_posix(), "digest": source.sha256}}])
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        outer["operator_authorization"] = {"authorization_ref": "read-permission",
            "authorization_freshness": {"state": "current", "digest": "a" * 64},
            **{key: copy.deepcopy(outer[key]) for key in fields}}
        terminal = tracker.run_selected_operation(outer)
        self.assertNotIn("execution_error", terminal, terminal)
        result = captured["result"]
        self.assertEqual(result["effects"], [])
        return result

    def refused(self, result, code):
        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual(result["errors"][0]["code"], code)

    def test_read_is_independent_complete_and_returns_actual_unpinned_version(self):
        with patch("connector_atom_dispatch.query_atoms", side_effect=AssertionError("Read must not Find")):
            result = self.invoke()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["data"]["source"], self.first.read_text())
        self.assertEqual(result["current_state"], {"identity": "CA-R-1", "version": 3,
                         "source_token": self.digest(self.first), "source_view": self.context})
        request = self.inner(); request["expected_state"] = result["current_state"]
        self.assertEqual(self.invoke(request=request), result)

    def test_query_explicit_literal_empty_singular_multiple_results_without_full_read(self):
        for fields, value, count in ((["governs", "depends_on"], "Thing/Part", 2),
                                     (["governs"], "Thing/Part", 1), (["governs"], "Missing", 0)):
            request = self.inner("query")
            request["query"]["filters"]["subjects"][0].update(fields=fields, value=value)
            with patch("connector_atom_dispatch.read_atom", side_effect=AssertionError("Query must not Read")):
                result = self.invoke(operation="query", request=request)
            self.assertEqual(result["errors"], [])
            self.assertEqual(len(result["data"]["matches"]), count)
            self.assertTrue(result["data"]["complete"])
            self.assertTrue(all("source" not in row for row in result["data"]["matches"]))
            request["expected_state"] = result["current_state"]
            self.assertEqual(self.invoke(operation="query", request=request), result)

    def test_missing_target_wrong_expected_state_and_physical_target_refuse(self):
        for identity, expected, code in (("CA-R-999", None, "target_not_found"),
                                         ("CA-R-1", {"version": 2}, "stale_state"),
                                         (self.first.as_posix(), None, "input_invalid"), (7, None, "input_invalid")):
            request = self.inner(); request["target"]["identity"] = identity; request["expected_state"] = expected
            self.refused(self.invoke(request=request), code)

    def test_context_permission_and_action_state_refuse(self):
        for field, value, code in (("context", "unresolved", "input_invalid"),
                                    ("authorization", "unbound", "permission_denied")):
            request = self.inner(); request[field] = value
            self.refused(self.invoke(request=request), code)
        self.refused(self.invoke(started=False), "permission_denied")
        self.refused(self.invoke(finish_first=True), "permission_denied")
        self.refused(self.invoke(definition_identity="CA-O-212"), "permission_denied")
        self.refused(self.invoke(effects=[{"type": "mutation"}]), "permission_denied")
        self.refused(self.invoke(frontier_references=["unrelated-sealed-target"]), "permission_denied")

    def test_schema_and_source_pins_currentness_rechecked_without_rebinding(self):
        receiver = self.receiver()
        for path in (self.first, self.settings, self.structure,
                     *(self.root / source.relative_path for source in (*self.schemas, self.authorities["CA-O-047"]))):
            raw = path.read_bytes()
            def drift(_session, path=path, raw=raw):
                path.write_bytes(raw + b"\n# external drift\n")
            self.refused(self.invoke(receiver=receiver, before=drift), "stale_state")
            path.write_bytes(raw)
        self.refused(self.invoke(receiver=receiver, before=lambda _session: setattr(self, "current", False)), "stale_state")

    def test_source_frontier_omission_addition_and_other_owner_competing_identity_refuse(self):
        self.refused(self.invoke(receiver=self.receiver(frontier=self.frontier((self.first,)))), "stale_state")
        receiver = self.receiver()
        self.refused(self.invoke(receiver=receiver, before=lambda _: self.atom("CA-R-3")), "stale_state")
        added = self.owners["CORE"] / "04_requirement/CA-R-3--fixture.md"; added.unlink()
        duplicate = self.atom("CA-R-1", owner="OTHER")
        self.refused(self.invoke(receiver=self.receiver(frontier=self.frontier((self.first, self.second, duplicate)))), "target_ambiguous")

    def test_query_requires_complete_explicit_frontier_criteria(self):
        for field in ("scope_units", "lifecycles", "subjects", "result_fields"):
            request = self.inner("query"); del request["query"]["filters"][field]
            self.refused(self.invoke(operation="query", request=request), "input_invalid")
        request = self.inner("query"); request["query"]["filters"]["scope_units"] = ["OTHER"]
        self.refused(self.invoke(operation="query", request=request), "input_invalid")

    def test_factory_requires_actual_owner_map_and_exact_accepted_schema_profile_sources(self):
        with self.assertRaises(ValueError):
            self.receiver(view=dataclasses.replace(self.view, owners={"CORE": self.owners["CORE"]}))
        with self.assertRaises(ValueError):
            self.receiver(schemas=self.schemas[:1])
        with self.assertRaises(ValueError):
            self.receiver("query", schemas=self.schemas)
        # Faithful Read does not interpret Subject grammar or require Find evidence.
        result = self.invoke(receiver=self.receiver(schemas=self.schemas))
        self.assertEqual(result["errors"], [])

    def test_recaptured_same_identity_version_schema_or_action_cannot_substitute_accepted_bytes(self):
        for identity in CONTRACT_FILES:
            with self.subTest(identity=identity):
                prior_pin = self.authorities[identity]
                path = self.root / prior_pin.relative_path
                prior = path.read_bytes()
                path.write_bytes(prior + b"\nUnreviewed replacement body with unchanged identity and Version.\n")
                substitute = capture_source(self.root, prior_pin.relative_path)
                self.assertNotEqual(substitute.sha256, prior_pin.sha256)
                self.authorities[identity] = substitute
                schemas = tuple(substitute if source == prior_pin else source for source in (*self.schemas, *self.grammar))
                operation = "query" if identity == "CA-O-046" else "read"
                with self.assertRaises(ValueError):
                    self.receiver(operation, schemas=schemas)
                self.authorities[identity] = prior_pin
                path.write_bytes(prior)

    def test_historical_read_enforces_exact_version_in_explicit_view(self):
        historical = self.atom("CA-R-1", governs="Previous", version=1, archive=True)
        view = dataclasses.replace(self.view, source_view="history", lifecycles=("archived",))
        # History inventory excludes all current revisions, so its exact pins are separate.
        receiver = self.receiver(view=view, frontier=self.frontier((historical,)))
        request = self.inner(); request["expected_state"] = {"version": 1}
        result = self.invoke(receiver=receiver, request=request)
        self.assertEqual(result["errors"], [])
        self.assertIn("Previous", result["data"]["source"])
        self.assertEqual(result["current_state"]["version"], 1)


if __name__ == "__main__":
    unittest.main()
