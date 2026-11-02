from __future__ import annotations

import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_bindings import (
    ConnectorBindingError, ConnectorBindings, SelectedOperationAdmission, capture_source,
)
from workflow_run_support import RunTracker, _canonical_digest, _proposal


class ConnectorBindingTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[4] / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="connector-bindings-", dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name, text in {"manifest.json": "bound definition", "schema.md": "Atom ID schema",
                           "permission.md": "read/modify explicit fixture target",
                           "source.txt": "actual complete content"}.items():
            (self.root / name).write_text(text, encoding="utf-8")
        self.authorities = tuple(capture_source(self.root, name) for name in
                                 ("manifest.json", "schema.md", "permission.md"))
        self.manifest = {"manifest_ref": "manifest.json", "manifest_digest": self.digest("manifest.json")}
        self.request = {
            "operation": "read", "target": {"kind": "Atom", "identity": "CA-R-863"},
            "query": None, "delta": None, "expected_state": None,
            "authorization": "permission.md", "context": self.manifest,
        }
        self.tracker = RunTracker(self.root, source_observer=self.observe,
                                  executor=self.never_execute)

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def observe(self, outer):
        current = self.digest("manifest.json") == outer["definition_manifest"]["manifest_digest"]
        return {"selected": outer["operation_route"] == "fixture-existing-route", "current": current,
                "observed": {"manifest_digest": self.digest("manifest.json")}}

    def never_execute(self, *_args):
        raise AssertionError("Binding must not execute the outer service or record a Run.")

    def outer(self, request=None, mode="execute", *, context_reference=None):
        parameters = {"connector_request": copy.deepcopy(request or self.request)}
        if context_reference is not None:
            parameters["context_reference"] = copy.deepcopy(context_reference)
        frontier, effects = ["source.txt"], []
        value = {
            "mode": "preview", "request_id": f"fixture-{_canonical_digest(parameters)[:12]}",
            "operation_route": "fixture-existing-route",
            "parameters": parameters, "parameters_digest": _canonical_digest(parameters),
            "target_frontier": frontier, "target_frontier_digest": _canonical_digest(frontier),
            "effects": effects, "effects_digest": _canonical_digest(effects),
            "definition_manifest": self.manifest,
            "source_freshness": {
                "selected_source_registry_ref": "schema.md", "selected_source_registry_version": 1,
                "selected_source_registry_digest": self.digest("schema.md"),
                "selected_binding_ref": "manifest.json", "selected_binding_digest": self.digest("manifest.json"),
            },
            "initiative": {"initiative_id": "fixture", "instruction_summary": "explicit fixture operation"},
        }
        preview = self.tracker.run_selected_operation(value)
        if mode == "preview":
            return value
        value.update({
            "mode": "execute", "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "fixture-assigned-action",
            "requested_runs": [{"requested_run_id": "fixture-action-run", "kind": "action",
                                "definition": {"atom_id": "CA-O-047", "version": 1,
                                               "path": "schema.md", "digest": self.digest("schema.md")}}],
        })
        fields = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                  "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        value["operator_authorization"] = {
            "authorization_ref": "permission.md",
            "authorization_freshness": {"state": "current", "digest": self.digest("permission.md")},
            **{key: copy.deepcopy(value[key]) for key in fields},
        }
        return value

    @staticmethod
    def map_request(outer):
        return outer["parameters"]["connector_request"], outer["definition_manifest"]

    @staticmethod
    def validate_payload(request):
        if request["target"]["identity"] != "CA-R-863":
            raise ConnectorBindingError("input_invalid", "Exact admitted Atom identity is required.", "target")

    def bindings(self, *, request=None, mode="execute", mapping=True, validator=None, resolver=None):
        admission = SelectedOperationAdmission(
            self.tracker, self.outer(request, mode), map_request=self.map_request if mapping else None,
        )
        return ConnectorBindings(
            admission, supported_operations=("read", "modify", "create"), supported_kinds=("Atom",),
            validate_payload=validator or self.validate_payload,
            resolve_sources=resolver or (lambda _request: (capture_source(self.root, "source.txt"),)),
            authority_sources=self.authorities,
        )

    def assert_code(self, code, action):
        with self.assertRaises(ConnectorBindingError) as caught:
            action()
        self.assertEqual(caught.exception.code, code)
        self.assertEqual(set(caught.exception.record()), {"code", "message", "field"})

    def test_receiving_mapping_binds_nested_request_and_uses_real_source_bytes(self):
        before = copy.deepcopy(self.request)
        bound = self.bindings().bind(self.request)
        self.assertEqual(bound.request, before)
        self.assertEqual(bound.sources[0].read_bytes(), b"actual complete content")
        bound.revalidate_before_effect()
        self.assertEqual(self.request, before)
        self.assertFalse((self.root / "journal").exists())

    def test_absent_mapping_and_preview_do_not_acquire_permission(self):
        self.assert_code("input_invalid", lambda: self.bindings(mapping=False).bind(self.request))
        self.assert_code("permission_denied", lambda: self.bindings(mode="preview").bind(self.request))

    def test_changed_request_and_unresolved_context_are_rejected(self):
        binding = self.bindings()
        self.assert_code("permission_denied", lambda: binding.bind({**self.request, "expected_state": {"digest": "other"}}))
        changed = {**self.request, "context": "unresolved-context"}
        self.assert_code("input_invalid", lambda: self.bindings(request=changed).bind(changed))

    def test_permission_reference_is_matched_to_existing_outer_authorization(self):
        changed = {**self.request, "authorization": "not-the-permission"}
        self.assert_code("permission_denied", lambda: self.bindings(request=changed).bind(changed))

    def test_source_and_each_authority_pin_are_checked_before_effect(self):
        for name in ("source.txt", "manifest.json", "schema.md", "permission.md"):
            with self.subTest(name=name):
                bound = self.bindings().bind(self.request)
                path = self.root / name
                before = path.read_bytes()
                path.write_bytes(before + b" changed")
                self.assert_code("stale_state", bound.revalidate_before_effect)
                path.write_bytes(before)

    def test_observed_absence_is_rechecked_without_creating_a_file(self):
        source = capture_source(self.root, "new.txt")
        self.assertIsNone(source.sha256)
        source.revalidate()
        self.assert_code("target_not_found", source.read_bytes)
        (self.root / "new.txt").write_text("appeared", encoding="utf-8")
        self.assert_code("stale_state", source.revalidate)

    def test_private_resolution_cannot_switch_target_after_binding(self):
        selected = ["source.txt"]
        binding = self.bindings(resolver=lambda _: (capture_source(self.root, selected[0]),))
        bound = binding.bind(self.request)
        selected[0] = "schema.md"
        self.assert_code("stale_state", bound.revalidate_before_effect)

    def test_mutating_validator_cannot_change_the_request_or_its_seal(self):
        def validator(request):
            request["target"]["identity"] = "silently-substituted"
        bound = self.bindings(validator=validator).bind(self.request)
        self.assertEqual(bound.request["target"]["identity"], "CA-R-863")
        bound.revalidate_before_effect()

    def test_callback_alias_mutation_cannot_change_the_admitted_snapshot(self):
        for callback in ("validator", "resolver"):
            with self.subTest(callback=callback):
                self.request["target"]["identity"] = "CA-R-863"
                def mutate_alias(_request):
                    self.request["target"]["identity"] = "changed-after-admission"
                    if callback == "resolver":
                        return (capture_source(self.root, "source.txt"),)
                options = {callback: mutate_alias}
                bound = self.bindings(**options).bind(self.request)
                self.assertEqual(bound.request["target"]["identity"], "CA-R-863")
                self.assertEqual(self.request["target"]["identity"], "changed-after-admission")
                bound.revalidate_before_effect()

    def test_non_json_object_is_refused_before_copy_can_invoke_its_hooks(self):
        class NotJSON:
            def __deepcopy__(self, _memo):
                raise AssertionError("Non-JSON caller object must not invoke copy hooks.")
        self.assert_code("input_invalid", lambda: self.bindings().bind({**self.request, "expected_state": NotJSON()}))

    def test_private_paths_cannot_escape_or_follow_symlinks(self):
        self.assert_code("input_invalid", lambda: capture_source(self.root, "../source.txt"))
        (self.root / "linked.txt").symlink_to(self.root / "source.txt")
        self.assert_code("permission_denied", lambda: capture_source(self.root, "linked.txt"))
        pinned = capture_source(self.root, "source.txt")
        (self.root / "source.txt").unlink()
        (self.root / "source.txt").symlink_to(self.root / "schema.md")
        self.assert_code("permission_denied", pinned.revalidate)

    def test_bool_schema_attestation_is_not_accepted(self):
        for value in (True, False):
            with self.subTest(value=value):
                self.assert_code("schema_invalid", lambda: self.bindings(validator=lambda _request: value).bind(self.request))

    def test_missing_authority_or_duplicate_private_resolution_is_rejected(self):
        admission = SelectedOperationAdmission(self.tracker, self.outer(), map_request=self.map_request)
        with self.assertRaises(ValueError):
            ConnectorBindings(admission, supported_operations=("read",), supported_kinds=("Atom",),
                              validate_payload=self.validate_payload, resolve_sources=lambda _: (), authority_sources=())
        source = capture_source(self.root, "source.txt")
        self.assert_code("target_ambiguous", lambda: self.bindings(resolver=lambda _: (source, source)).bind(self.request))

    def test_changed_preview_evidence_is_refused_by_existing_gate(self):
        outer = self.outer()
        outer["proposal_receipt_digest"] = "0" * 64
        admission = SelectedOperationAdmission(self.tracker, outer, map_request=self.map_request)
        self.assert_code("stale_state", lambda: admission.check(self.request))

    def test_existing_native_request_id_conflict_is_preserved_without_execution(self):
        outer = self.outer()
        outer["initiative"]["instruction_summary"] = "different canonical request"
        outer["proposal_receipt"] = _proposal(outer, self.observe(outer))
        outer["proposal_receipt_digest"] = _canonical_digest(outer["proposal_receipt"])
        outer["operator_authorization"]["proposal_receipt_digest"] = outer["proposal_receipt_digest"]
        admission = SelectedOperationAdmission(self.tracker, outer, map_request=self.map_request)
        self.assert_code("permission_denied", lambda: admission.check(self.request))
        self.assertFalse((self.root / "journal").exists())

    def test_exact_inner_seal_distinguishes_boolean_integer_and_float(self):
        for admitted, substituted in ((1, True), (True, 1), (1, 1.0), (1.0, 1)):
            with self.subTest(admitted=admitted, substituted=substituted):
                original = {**self.request, "expected_state": {"revision": admitted}}
                changed = {**self.request, "expected_state": {"revision": substituted}}
                self.assert_code("permission_denied", lambda: self.bindings(request=original).bind(changed))

    def test_exact_context_reference_distinguishes_boolean_integer_and_float(self):
        for admitted, substituted in ((1, True), (True, 1), (1, 1.0), (1.0, 1)):
            with self.subTest(admitted=admitted, substituted=substituted):
                request = {**self.request, "context": {"revision": substituted}}
                outer = self.outer(request, context_reference={"revision": admitted})
                admission = SelectedOperationAdmission(self.tracker, outer, map_request=lambda outer: (
                    outer["parameters"]["connector_request"], outer["parameters"]["context_reference"],
                ))
                self.assert_code("input_invalid", lambda: admission.check(request))

    def test_unknown_operation_and_public_physical_selector_are_rejected_first(self):
        binding = self.bindings()
        self.assert_code("unsupported_operation", lambda: binding.bind({**self.request, "operation": "delete"}))
        self.assert_code("input_invalid", lambda: binding.bind({**self.request, "target": {"kind": "Atom", "path": "source.txt"}}))


if __name__ == "__main__":
    unittest.main()
