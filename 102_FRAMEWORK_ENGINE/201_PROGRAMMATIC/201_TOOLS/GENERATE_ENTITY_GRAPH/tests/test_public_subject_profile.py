"""D539 public profile binding without selector resolution or native admission."""

from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from pydantic import ValidationError

import test_graph_publication_safety as publication
import test_selected_graphs as selected
from historical_core_authority import historical_authority_bytes


graph = publication.graph
subject_notation = graph.subject_notation


class PublicSubjectProfileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = publication.GraphPublicationSafetyTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.source = self.fixture.selected / "CA-R-1872.md"
        self.journal = self.root / self.fixture.control_root / "_journal/events.ndjson"
        self.journal.parent.mkdir(parents=True)
        self.journal.write_bytes(b'{"event":"existing fixture Journal"}\n')
        self.journal_before = self.journal.read_bytes()

    def request(self, graph_kind: str = "entities", *, publish: bool = False, **overrides: object) -> dict[str, object]:
        request = self.fixture.request()
        request["graph_kind"] = graph_kind
        if not publish:
            request.pop("run_recording_context")
            request.pop("output_destination")
            request["selection"] = {"atom_ids": ["CA-R-1872"], "scope_unit_names": []}
        request.update(overrides)
        return request

    def copy_approved_pins(self) -> None:
        pins = subject_notation.get_profile("approved").grammar_pins
        self.assertEqual(5, len(pins))
        for pin in pins:
            destination = self.root / pin.path
            suffix = "/".join(Path(pin.path).parts[-2:])
            payload = historical_authority_bytes(suffix, pin.sha256)
            self.assertEqual(pin.sha256, hashlib.sha256(payload).hexdigest())
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)

    def write_subject(self, subject: str, *, depends_on: tuple[str, ...] = ()) -> None:
        self.source.write_text(
            selected.current_atom("CA-R-1872", governs=subject, depends_on=depends_on,
                                  claim="Subjects supply incidence without native fact admission."),
            encoding="utf-8", newline="\n",
        )

    def assert_sources_preserved(self, before: bytes) -> None:
        self.assertEqual(before, self.source.read_bytes())
        self.assertEqual(self.journal_before, self.journal.read_bytes())

    def assert_pin_failure(self, result: dict[str, object], *, code: str, before: bytes | None = None) -> None:
        self.assertEqual("failed" if code.endswith("symlink") else "stale", result["outcome"])
        self.assertIn(code, {row["code"] for row in result["diagnostics"]})
        if result["outcome"] == "stale":
            self.assertEqual("fail", result["quality_dispositions"]["currentness"])
        if before is None:
            self.assertEqual({"state": "none", "paths": [], "before": None, "after": None}, result["output_effects"])
            self.assertFalse(self.fixture.output.exists())
        else:
            self.fixture.assert_preserved(result, before)

    def test_public_schema_accepts_only_optional_legacy_or_approved_profile(self) -> None:
        schema = graph.GenerateEntityGraphRequest.model_json_schema()
        body = schema["$defs"][schema["$ref"].rsplit("/", 1)[1]]
        self.assertNotIn("subject_profile", body["required"])
        self.assertIn("subject_profile", body["properties"])
        self.assertEqual(["legacy", "approved"], body["properties"]["subject_profile"]["enum"])
        default = graph.GenerateEntityGraphRequest.model_validate(self.request())
        self.assertNotIn("subject_profile", default.root.model_dump(mode="json", exclude_unset=True))
        for profile in ("legacy", "approved"):
            with self.subTest(profile=profile):
                model = graph.GenerateEntityGraphRequest.model_validate(self.request(subject_profile=profile))
                self.assertEqual(profile, model.root.model_dump(mode="json", exclude_unset=True)["subject_profile"])

    def test_public_schema_rejects_null_unknown_nontext_and_forged_internal_evidence(self) -> None:
        for value in (None, "", "APPROVED", "unknown", 1, True, [], {}):
            with self.subTest(profile=value):
                with self.assertRaises(ValidationError):
                    graph.GenerateEntityGraphRequest.model_validate(self.request(subject_profile=value))
        for field, value in (
            ("subject_profile_evidence", {"grammar_pins": []}),
            ("grammar_pins", []),
            ("source_fact_context", {}),
            ("run_recording_context", {"state": "confirmed"}),
            ("terminal_receipt_refs", ["forged"]),
        ):
            with self.subTest(field=field):
                with self.assertRaises(ValidationError):
                    graph.GenerateEntityGraphRequest.model_validate(self.request(subject_profile="approved", **{field: value}))

    def test_strict_builder_rejects_invalid_profiles_and_forged_profile_evidence_without_effects(self) -> None:
        source_before = self.source.read_bytes()
        for value in (None, "", "APPROVED", "unknown", 1, True, [], {}):
            with self.subTest(profile=value):
                result = graph.build_graph(self.root, self.request(subject_profile=value))
                self.assertEqual("failed", result["outcome"])
                expected = "profile-unknown" if isinstance(value, str) and value else "profile-invalid"
                self.assertEqual(expected, result["diagnostics"][0]["code"])
                self.assertEqual("none", result["output_effects"]["state"])
                self.assertTrue(result["diagnostics"])
        for field in ("subject_profile_evidence", "grammar_pins", "source_fact_context", "terminal_receipt_refs"):
            with self.subTest(field=field):
                result = graph.build_graph(self.root, self.request(subject_profile="approved", **{field: {"forged": True}}))
                self.assertEqual("failed", result["outcome"])
                self.assertEqual("request-schema-invalid", result["diagnostics"][0]["code"])
                self.assertEqual("none", result["output_effects"]["state"])
        result = graph.build_graph(self.root, self.request(subject_profile="approved", run_recording_context={"state": "confirmed"}))
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("recording-context-untrusted", result["diagnostics"][0]["code"])
        self.assertEqual("none", result["output_effects"]["state"])
        self.assert_sources_preserved(source_before)

    def test_default_and_explicit_legacy_preserve_complete_canonical_results_without_approved_pins(self) -> None:
        self.write_subject("Core.Atom/Property: Value")
        source_before = self.source.read_bytes()
        for kind in ("entities", "terms"):
            with self.subTest(graph_kind=kind):
                default = graph.build_graph(self.root, self.request(kind))
                explicit = graph.build_graph(self.root, self.request(kind, subject_profile="legacy"))
                self.assertEqual("incomplete", default["outcome"])
                self.assertEqual(graph.canonical_json(default), graph.canonical_json(explicit))
                self.assertEqual({"selection": {"atom_ids": ["CA-R-1872"], "scope_unit_names": []}}, default["selection_evidence"])
        self.assert_sources_preserved(source_before)

    def test_explicit_legacy_preserves_published_bytes_and_identical_output_confirmation(self) -> None:
        first = graph.build_graph(self.root, self.request(publish=True))
        self.assertEqual("created", first["output_effects"]["state"])
        before = self.fixture.output.read_bytes()
        second = graph.build_graph(self.root, self.request(
            publish=True, subject_profile="legacy",
            existing_projection_evidence={"sha256": hashlib.sha256(before).hexdigest()},
        ))
        self.fixture.assert_preserved(second, before)
        self.assertEqual(first["selection_evidence"], second["selection_evidence"])
        self.assertEqual(first["source_fact_context_evidence"], second["source_fact_context_evidence"])
        self.assertEqual({"state": "awaiting_terminal_recording"}, second["completion"])

    def test_approved_public_incidence_retains_notation_and_never_admits_selector_instances_or_edges(self) -> None:
        self.copy_approved_pins()
        owner = 'atom(content_role="Plan",type="Plan")'
        subject = owner + ".Status: Active"
        dependencies = ("Core/Atom.Dependent: Value", 'atom(atom_id="CA-O-135")', "Atom")
        self.write_subject(subject, depends_on=dependencies)
        source_before = self.source.read_bytes()
        for kind in ("entities", "terms"):
            with self.subTest(graph_kind=kind):
                result = graph.build_graph(self.root, self.request(kind, subject_profile="approved"))
                self.assertEqual("incomplete", result["outcome"])
                self.assertEqual("approved", result["selection_evidence"]["subject_profile"])
                self.assertEqual(subject_notation.profile_evidence("approved"), result["selection_evidence"]["subject_profile_evidence"])
                namespace = result[f"{kind}_graph"]
                self.assertEqual({subject, *dependencies}, {row["subject_path"] for row in namespace["incidence"]})
                self.assertEqual({"GOVERNS", "DEPENDS_ON"}, {row["kind"] for row in namespace["incidence"]})
                self.assertEqual([], namespace["entities" if kind == "entities" else "terms"])
                self.assertEqual([], namespace["native_relations"])
                self.assertEqual([], namespace["external_references"])
                if kind == "entities":
                    self.assertEqual([], namespace["native_properties"])
        self.assert_sources_preserved(source_before)

    def test_approved_profile_reaches_descriptor_action_and_queue_adapters(self) -> None:
        self.copy_approved_pins()
        self.write_subject('atom(atom_id="CA-O-135").Status: Active')
        for kind, action in (("entities", "CA-O-134"), ("terms", "CA-O-137")):
            with self.subTest(graph_kind=kind):
                request = self.request(kind, subject_profile="approved")
                try:
                    model = graph.GenerateEntityGraphRequest.model_validate(request)
                except ValidationError as error:
                    self.fail(f"Public request must accept approved Subject notation: {error}")
                descriptor = graph.create_adapter(self.root).invoke(model)
                action_result = graph.ACTION_HANDLERS[action](self.root, request)
                queued = graph.queue_action_handlers(self.root)[action]({"parameters": {"graph_request": request}})
                self.assertEqual("incomplete", descriptor["outcome"])
                self.assertEqual(graph.canonical_json(descriptor), graph.canonical_json(action_result))
                self.assertEqual(graph.canonical_json(descriptor), graph.canonical_json(queued["graph_result"]))
                self.assertEqual([], queued["effect_refs"])

    def test_approved_rejects_wrong_selector_case_and_nontext_subjects_via_real_parser(self) -> None:
        self.copy_approved_pins()
        for subject, code in (
            ('Atom(content_role="Plan").Status', "subject-selector-invalid"),
            ('atom(type="Plan").Status', "subject-selector-invalid"),
            ("Atom@12", "subject-at-unsupported"),
        ):
            with self.subTest(subject=subject):
                self.write_subject(subject)
                result = graph.build_graph(self.root, self.request(subject_profile="approved"))
                self.assertEqual("failed", result["outcome"])
                self.assertIn(code, {row["code"] for row in result["diagnostics"]})
                self.assertEqual("none", result["output_effects"]["state"])
        self.write_subject("Atom")
        self.source.write_text(self.source.read_text(encoding="utf-8").replace('governs: "Atom"', "governs: true"), encoding="utf-8")
        result = graph.build_graph(self.root, self.request(subject_profile="approved"))
        self.assertEqual("failed", result["outcome"])
        self.assertIn("subjects-yaml-invalid", {row["code"] for row in result["diagnostics"]})

    def test_every_approved_pin_is_checked_from_requested_root_before_subject_parsing(self) -> None:
        self.copy_approved_pins()
        before = self.fixture.write_existing()
        source_before = self.source.read_bytes()
        request = self.request(publish=True, subject_profile="approved", selection={"atom_ids": ["CA-R-1872"]},
                               existing_projection_evidence={"sha256": hashlib.sha256(before).hexdigest()})
        for pin in subject_notation.get_profile("approved").grammar_pins:
            path = self.root / pin.path
            original = path.read_bytes()
            for missing in (False, True):
                with self.subTest(atom_id=pin.atom_id, missing=missing):
                    if missing:
                        path.unlink()
                    else:
                        path.write_bytes(original + b"\nchanged fixture grammar\n")
                    try:
                        with patch.object(graph, "parse_subject_relations", wraps=graph.parse_subject_relations) as parser:
                            result = graph.build_graph(self.root, request)
                        self.assert_pin_failure(result, code="approved-grammar-pin-stale", before=before)
                        parser.assert_not_called()
                    finally:
                        path.write_bytes(original)
        self.assert_sources_preserved(source_before)

    def test_approved_pin_and_parent_directory_symlinks_fail_without_publication(self) -> None:
        self.copy_approved_pins()
        pin = subject_notation.get_profile("approved").grammar_pins[0]
        path = self.root / pin.path
        replacement = path.with_name("fixture-grammar-target.md")
        replacement.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(replacement)
        result = graph.build_graph(self.root, self.request(subject_profile="approved"))
        self.assert_pin_failure(result, code="approved-grammar-pin-symlink")
        path.unlink()
        path.write_bytes(replacement.read_bytes())
        directory = path.parent
        moved = directory.with_name("fixture-grammar-directory")
        directory.rename(moved)
        directory.symlink_to(moved, target_is_directory=True)
        result = graph.build_graph(self.root, self.request(subject_profile="approved"))
        self.assert_pin_failure(result, code="approved-grammar-pin-symlink")

    def test_approved_pin_drift_after_real_parsing_is_stale_even_without_output_destination(self) -> None:
        self.copy_approved_pins()
        self.write_subject("Core/Atom.Dependent: Value")
        source_before = self.source.read_bytes()
        path = self.root / subject_notation.get_profile("approved").grammar_pins[0].path
        original = graph.parse_subject_relations

        def parse_then_drift(*args, **kwargs):
            result = original(*args, **kwargs)
            path.write_bytes(path.read_bytes() + b"\nchanged after fixture parsing\n")
            return result

        with patch.object(graph, "parse_subject_relations", side_effect=parse_then_drift) as parser:
            result = graph.build_graph(self.root, self.request(subject_profile="approved"))
        self.assert_pin_failure(result, code="approved-grammar-pin-stale")
        parser.assert_called_once()
        self.assertEqual("approved", parser.call_args.kwargs["subject_profile"])
        self.assert_sources_preserved(source_before)

    def assert_prepublication_drift_rejected(self, *, identical: bool) -> None:
        self.copy_approved_pins()
        if identical:
            first = graph.build_graph(self.root, self.request(publish=True, subject_profile="approved"))
            self.assertEqual("created", first["output_effects"]["state"])
            before = self.fixture.output.read_bytes()
        else:
            before = self.fixture.write_existing()
        source_before = self.source.read_bytes()
        path = self.root / subject_notation.get_profile("approved").grammar_pins[-1].path
        import graph_fact_context as facts
        original = facts.prepare_fact_context
        calls = 0

        def prepare_then_drift(*args, **kwargs):
            nonlocal calls
            calls += 1
            result = original(*args, **kwargs)
            if calls == 2:
                path.write_bytes(path.read_bytes() + b"\nchanged before fixture publication\n")
            return result

        request = self.request(publish=True, subject_profile="approved",
                               existing_projection_evidence={"sha256": hashlib.sha256(before).hexdigest()})
        with patch.object(facts, "prepare_fact_context", side_effect=prepare_then_drift):
            result = graph.build_graph(self.root, request)
        self.assert_pin_failure(result, code="approved-grammar-pin-stale", before=before)
        self.assertEqual(2, calls)
        self.assert_sources_preserved(source_before)

    def test_approved_pin_drift_before_publication_preserves_existing_bytes(self) -> None:
        self.assert_prepublication_drift_rejected(identical=False)

    def test_approved_pin_drift_blocks_identical_output_confirmation(self) -> None:
        self.assert_prepublication_drift_rejected(identical=True)

    def test_approved_publication_carries_five_pins_and_preserves_fact_context_and_recording_boundary(self) -> None:
        self.copy_approved_pins()
        legacy = graph.build_graph(self.root, self.request(selection={"atom_ids": []}))
        source_before = self.source.read_bytes()
        result = graph.build_graph(self.root, self.request(publish=True, subject_profile="approved"))
        self.assertEqual("created", result["output_effects"]["state"])
        published = json.loads(self.fixture.output.read_bytes())
        self.assertEqual(result["selection_evidence"], published["selection_evidence"])
        self.assertEqual(subject_notation.profile_evidence("approved"), published["selection_evidence"]["subject_profile_evidence"])
        self.assertEqual(legacy["source_fact_context_evidence"], result["source_fact_context_evidence"])
        self.fixture.assert_awaiting_terminal(result)
        self.assert_sources_preserved(source_before)


if __name__ == "__main__":
    unittest.main()
