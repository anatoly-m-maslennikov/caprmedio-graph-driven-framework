"""Selected native publication frontier tests; no live installation or Docker."""

from __future__ import annotations

from dataclasses import asdict, replace
import copy
import hashlib
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_checkpoint import (  # noqa: E402
    _load_e2e, _validate_native_evidence_bindings, _native_packet_value, _load_native_packet,
    _native_document_value, _load_native_document, _native_result_value, _load_native_result,
    _NATIVE_STATE_NAMES, _candidate_value, _fingerprint, release_action_checkpoint_sha256,
    NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA,
    LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA, read_native_checkpoint_packet,
    read_direct_native_result_effects, read_direct_native_result_packet,
    _tag, _load_tag, _shared_recording,
)
from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json  # noqa: E402
from release_promotion import NativePromotionEvidence  # noqa: E402
from release_version import ReleaseVersionRequest  # noqa: E402
from release_e2e_gate import CandidateE2EGateEvidence, PortableCandidateE2EGateEvidence  # noqa: E402
from release_actions import ReleasePhaseResult, SelectedReleaseActionContext, _retirement_recording_handoff  # noqa: E402
from release_image import ImageRetirementEvidence  # noqa: E402
from release_actions import PHASES  # noqa: E402
from methodology_layout import resolve_methodology_layout  # noqa: E402


class DirectNativeResultFormatTests(unittest.TestCase):
    """Documentary parser checks; these fixtures never grant install authority."""

    def setUp(self) -> None:
        from framework_installation_command import FrameworkInstallationCommandReceipt

        self.command = FrameworkInstallationCommandReceipt(
            "documentary-command", "documentary-operator", "documentary-author", "a" * 64,
            {}, "b" * 64, "c" * 64, "d" * 64, None, "e" * 64, b"documentary-only",
        )
        references = {
            "package_selector": ".caprmedio_install/current.toml",
            "runtime_selector": ".caprmedio_runtime/installation/current.toml",
            "release_proof": ".caprmedio_runtime/installation/generations/1/release-proof.toml",
            "package_manifest": f".caprmedio_install/releases/{self.command.package_manifest_sha256}/manifest.toml",
            "full_gate_receipt": "original/gates/full/receipt.json",
            "retained_candidate_descriptor": "original/candidate-snapshot.json",
            "retained_package_sidecar": "original/package_evidence/receipt.json",
            "unit_gate_receipt": "original/gates/unit/receipt.json",
            "build_receipt": "original/gates/build/receipt.json",
            "verification_receipt": "original/gates/image/receipt.json",
            "e2e_gate_receipt": "original/gates/e2e/receipt.json",
        }
        self.payload = {
            "schema_version": 1, "action_id": "CA-O-200", "action_run_id": "direct-action:documentary",
            "installation_command_sha256": self.command.sha256,
            "package_manifest_sha256": self.command.package_manifest_sha256,
            "target_project_context_sha256": self.command.target_project_context_sha256,
            "state_generation": 1, "effect_outcome": "completed", "reason": None,
            "effects": [{"kind": kind, "reference": ref, "sha256": self.command.full_gate_receipt_sha256
                         if kind == "full_gate_receipt" else "f" * 64} for kind, ref in references.items()],
        }

    def read(self, payload=None):
        return read_direct_native_result_effects(canonical_json(payload or self.payload), command=self.command,
            action_run_id="direct-action:documentary", state_generation=1)

    def test_closed_effect_format_preserves_exact_original_reference_order(self) -> None:
        observed = self.read()
        self.assertEqual(list(observed), [row["kind"] for row in self.payload["effects"]])
        self.assertEqual(list(observed.values()), self.payload["effects"])

    def test_historical_four_effect_result_remains_readable_but_has_no_packet(self) -> None:
        historical = copy.deepcopy(self.payload)
        historical["effects"] = historical["effects"][:4]
        self.assertEqual(len(self.read(historical)), 4)
        with self.assertRaises(ReleaseContractError) as rejected:
            read_direct_native_result_packet(canonical_json(historical), project_root="/unused-documentary-root",
                command=self.command, action_run_id="direct-action:documentary", state_generation=1)
        self.assertEqual(rejected.exception.code, "release-native-n-direct-packet-association-unavailable")

    def test_result_cannot_relabel_selected_action_or_change_original_binding(self) -> None:
        for key, changed in (("action_id", "CA-O-169"), ("action_run_id", "other-run"),
                             ("installation_command_sha256", "9" * 64), ("package_manifest_sha256", "9" * 64),
                             ("target_project_context_sha256", "9" * 64), ("state_generation", True)):
            with self.subTest(key=key):
                payload = copy.deepcopy(self.payload)
                payload[key] = changed
                with self.assertRaises(ReleaseContractError):
                    self.read(payload)

    def test_unknown_duplicate_and_alias_effect_associations_are_refused(self) -> None:
        for change in ("unknown", "duplicate-kind", "duplicate-reference", "escape", "extra-member"):
            with self.subTest(change=change):
                payload = copy.deepcopy(self.payload)
                row = payload["effects"][-1]
                if change == "unknown":
                    row["kind"] = "latest_full_gate"
                elif change == "duplicate-kind":
                    row["kind"] = payload["effects"][0]["kind"]
                elif change == "duplicate-reference":
                    row["reference"] = payload["effects"][0]["reference"]
                elif change == "escape":
                    row["reference"] = "../other/receipt.json"
                else:
                    row["permission"] = True
                with self.assertRaises(ReleaseContractError):
                    self.read(payload)

    def test_changed_gate_or_current_carrier_reference_is_refused(self) -> None:
        for index, key, changed in ((4, "sha256", "9" * 64), (0, "reference", "old/current.toml")):
            payload = copy.deepcopy(self.payload)
            payload["effects"][index][key] = changed
            with self.assertRaises(ReleaseContractError):
                self.read(payload)

    def test_partial_uncertain_or_noncanonical_result_cannot_supply_installed_n(self) -> None:
        for outcome in ("effect_uncertain", "unavailable_after_delete", "blocked_before_delete"):
            payload = copy.deepcopy(self.payload)
            payload["effect_outcome"] = outcome
            with self.assertRaises(ReleaseContractError):
                self.read(payload)
        with self.assertRaises(ReleaseContractError):
            read_direct_native_result_effects(canonical_json(self.payload) + b"\n", command=self.command,
                action_run_id="direct-action:documentary", state_generation=1)

    def test_reason_matches_existing_closed_direct_result_semantics(self) -> None:
        for reason in (None, "", " documentary reason "):
            payload = copy.deepcopy(self.payload)
            payload["reason"] = reason
            self.read(payload)
        for reason in (True, "newline\n", "null\x00"):
            payload = copy.deepcopy(self.payload)
            payload["reason"] = reason
            with self.assertRaises(ReleaseContractError):
                self.read(payload)

    def documentary_carriers(self, root):
        payload = copy.deepcopy(self.payload)
        for row in payload["effects"]:
            carrier = root / row["reference"]
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(b"documentary-carrier-not-a-gate")
            row["sha256"] = hashlib.sha256(carrier.read_bytes()).hexdigest()
        command = replace(self.command, full_gate_receipt_sha256=payload["effects"][4]["sha256"])
        return payload, command

    def test_changed_physical_associated_carrier_is_refused_before_packet_loading(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
            root = Path(directory).resolve(strict=True)
            payload, command = self.documentary_carriers(root)
            (root / payload["effects"][0]["reference"]).write_bytes(b"changed")
            with self.assertRaises(ReleaseContractError) as rejected:
                read_direct_native_result_packet(canonical_json(payload), project_root=str(root), command=command,
                    action_run_id="direct-action:documentary", state_generation=1)
            self.assertEqual(rejected.exception.code, "release-native-n-direct-carrier-invalid")

    def test_associated_file_alias_is_refused_even_with_same_bytes(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
            root = Path(directory).resolve(strict=True)
            payload, command = self.documentary_carriers(root)
            carrier = root / payload["effects"][0]["reference"]
            actual = root / "documentary-original.toml"
            actual.write_bytes(carrier.read_bytes())
            carrier.unlink()
            carrier.symlink_to(actual)
            with self.assertRaises(ReleaseContractError):
                read_direct_native_result_packet(canonical_json(payload), project_root=str(root), command=command,
                    action_run_id="direct-action:documentary", state_generation=1)


class DirectNativeTerminalReaderTests(unittest.TestCase):
    """Real bounded carrier reads of documentary events, not an executor fixture."""

    def setUp(self) -> None:
        DirectNativeResultFormatTests.setUp(self)
        import work_journal

        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.temp.name)
        control = self.root / ".caprmedio_documentary"
        self.journal = control / "_journal"
        self.journal.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_documentary"\n', encoding="utf-8")
        defaults = control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        defaults.mkdir(parents=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_text(
            "[query]\nmax_request_bytes=4096\nmax_grammar_depth=16\nmax_filter_tokens=128\n"
            "max_in_members=16\nmax_selected_fields=8\nmax_page_size=3\nmax_snapshot_members=8\n"
            "max_file_bytes=32768\nmax_total_read_bytes=65536\ntimeout_seconds=10\nmax_findings=8\n",
            encoding="utf-8")
        definition = {"atom_id": "CA-O-200", "version": 1, "path": "owned/action.md", "digest": "a" * 64}
        self.started = work_journal.with_event_digest({
            "schema_version": 5, "kind": "workflow_execution", "event_id": "direct-action:documentary:started",
            "action_id": "CA-O-200", "event": "started", "author": "documentary-author",
            "occurred_at": "2026-10-10T00:00:00+00:00", "llm_session": {"app": "documentary", "uuid": "a" * 64},
            "structural_scope": "documentary", "initiative": {"initiative_id": "CA-O-200", "instruction_summary": "documentary-only"},
            "run": {"run_id": "direct-action:documentary", "kind": "action", "definition": definition},
            "definition_bindings": [{"kind": "action", **definition}], "input_ref": "documentary/input.json",
            "outcome": None, "result_ref": None, "effect_refs": [], "report_ref": None,
            "redaction": {"redacted": False, "fields": []},
        })
        self.result_ref = ".caprmedio_tmp/installation/results/direct-action:documentary/result.json"
        self.effects = DirectNativeResultFormatTests.read(self)
        refs = [row["reference"] for row in self.effects.values()] + [self.result_ref]
        digest = work_journal.canonical_json_digest({"intent_sha256": self.started["llm_session"]["uuid"],
            "outcome": "completed", "result_ref": self.result_ref, "effect_refs": refs, "report_ref": None})
        terminal = dict(self.started)
        terminal.update(event_id=f"direct-action:documentary:terminal:{digest}", event="completed", outcome="completed",
                        result_ref=self.result_ref, effect_refs=refs)
        self.terminal = work_journal.with_event_digest(terminal)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_events(self, *events) -> None:
        (self.journal / "documentary.ndjson").write_bytes(b"".join(canonical_json(event) + b"\n" for event in events))

    def reopen(self) -> None:
        from release_promotion import _reopen_completed_direct_native_result
        _reopen_completed_direct_native_result(self.root, self.started, self.result_ref, self.effects)

    def test_reader_accepts_exact_documentary_start_terminal_pair_without_writes(self) -> None:
        from FIND_AND_FETCH_JOURNAL_EVENTS import find_and_fetch_journal_events as reader

        self.write_events(self.started, self.terminal)
        before = (self.journal / "documentary.ndjson").read_bytes()
        with patch.object(reader, "query", wraps=reader.query) as query_call:
            self.reopen()
        self.assertEqual(query_call.call_args.args[1]["filter"], '"event:/run/run_id" = "direct-action:documentary"')
        self.assertEqual(query_call.call_args.args[1]["limit"], 3)
        self.assertEqual((self.journal / "documentary.ndjson").read_bytes(), before)

    def test_missing_terminal_and_duplicate_start_are_refused(self) -> None:
        for events in ((self.started,), (self.started, self.started, self.terminal)):
            self.write_events(*events)
            with self.assertRaises(ReleaseContractError):
                self.reopen()

    def test_other_terminal_digest_for_same_original_run_cannot_hide(self) -> None:
        import work_journal

        other = dict(self.terminal)
        other["event_id"] = "direct-action:documentary:terminal:" + "9" * 64
        other["result_ref"] = "other/result.json"
        self.write_events(self.started, self.terminal, work_journal.with_event_digest(other))
        with self.assertRaises(ReleaseContractError):
            self.reopen()

    def test_resealed_changed_author_or_ordered_effects_cannot_account_for_result(self) -> None:
        import work_journal

        for key, changed in (("author", "other-author"), ("effect_refs", list(reversed(self.terminal["effect_refs"])))):
            terminal = dict(self.terminal)
            terminal[key] = changed
            self.write_events(self.started, work_journal.with_event_digest(terminal))
            with self.assertRaises(ReleaseContractError):
                self.reopen()

    def test_parented_selected_run_cannot_be_relabelled_direct(self) -> None:
        self.started["run"]["parent_run_id"] = "selected-step"
        with self.assertRaises(ReleaseContractError) as rejected:
            self.reopen()
        self.assertEqual(rejected.exception.code, "release-native-n-direct-start-invalid")


class SelectedNativePromotionCodecTests(unittest.TestCase):
    def evidence(self) -> PortableCandidateE2EGateEvidence:
        return PortableCandidateE2EGateEvidence(
            candidate_snapshot_manifest_sha256="a" * 64,
            candidate_image_digest="sha256:" + "b" * 64,
            phase_map_sha256="c" * 64,
            grammar_sha256="d" * 64,
            outcome="passed", reason="synthetic carrier only",
            harness_receipts=(), evidence_root=".caprmedio_tmp/gate",
            receipt_sha256="e" * 64,
            settings_snapshot_path=".caprmedio_tmp/gate/settings.json",
            settings_snapshot_sha256="f" * 64,
            host_capability_path=".caprmedio_tmp/gate/capability.json",
            host_capability_sha256="1" * 64,
            execution_kind="host-subprocess", package_schema="portable-1",
            package_manifest_sha256="2" * 64,
            package_evidence_sha256="3" * 64,
            package_evidence_relpath=".caprmedio_tmp/package_evidence/receipt.json",
            source_catalog_sha256="4" * 64,
            candidate_run_id="selected-native", input_manifest_sha256="5" * 64,
            framework_version="0.4.2", version_toml_sha256="6" * 64,
        )

    def payload(self, evidence):
        payload = asdict(evidence)
        payload["harness_receipts"] = []
        return payload

    def test_native_e2e_roundtrip_preserves_every_portable_binding(self) -> None:
        evidence = self.evidence()
        restored = _load_e2e(self.payload(evidence), native=True)
        self.assertIs(type(restored), PortableCandidateE2EGateEvidence)
        self.assertEqual(restored, evidence)

    def test_native_e2e_cannot_be_loaded_as_legacy_observation(self) -> None:
        with self.assertRaises(ReleaseContractError):
            _load_e2e(self.payload(self.evidence()))

    def test_legacy_e2e_remains_closed_and_cannot_supply_native_frontier(self) -> None:
        portable = self.evidence()
        fields = CandidateE2EGateEvidence.__dataclass_fields__
        legacy = CandidateE2EGateEvidence(**{
            name: getattr(portable, name) for name in fields
        })
        self.assertEqual(_load_e2e(self.payload(legacy)), legacy)
        with self.assertRaises(ReleaseContractError):
            _load_e2e(self.payload(legacy), native=True)

    def state(self):
        evidence = self.evidence()
        return {
            "candidate": SimpleNamespace(manifest=SimpleNamespace(sha256="a" * 64)),
            "portable_compilation": SimpleNamespace(
                candidate_run_id=evidence.candidate_run_id,
                input_manifest_sha256=evidence.input_manifest_sha256,
                source_catalog_sha256=evidence.source_catalog_sha256,
                framework_version=evidence.framework_version,
                version_toml_sha256=evidence.version_toml_sha256,
            ),
            "prepared_portable_package": SimpleNamespace(package_manifest_sha256="2" * 64),
            "portable_suite": None, "build": None, "verification": None,
            "e2e": evidence, "full_gate": None,
            "promotion": None, "retirement": None,
        }

    def test_changed_native_package_identity_cannot_cross_checkpoint_frontier(self) -> None:
        state = self.state()
        _validate_native_evidence_bindings(state)
        state["prepared_portable_package"].package_manifest_sha256 = "9" * 64
        with self.assertRaises(ReleaseContractError) as rejected:
            _validate_native_evidence_bindings(state)
        self.assertEqual(rejected.exception.code, "release-checkpoint-binding-mismatch")

    def test_changed_native_aggregate_predecessor_is_refused(self) -> None:
        state = self.state()
        state["full_gate"] = SimpleNamespace(
            suite_receipt_sha256="9" * 64, build_receipt_sha256="a" * 64,
            image_receipt_sha256="b" * 64, e2e_receipt_sha256="e" * 64,
        )
        state["portable_suite"] = SimpleNamespace(receipt_sha256="8" * 64)
        with self.assertRaises(ReleaseContractError):
            _validate_native_evidence_bindings(state)

    def test_documentary_codec_cannot_encode_executable_or_unrecognized_type(self) -> None:
        root = "/fixture"
        value = (Path(root), Path(root) / "retained" / "proof.toml")
        self.assertEqual(_load_native_document(_native_document_value(value, root), root), value)
        with self.assertRaises(ReleaseContractError):
            _native_document_value(lambda: True, root)
        with self.assertRaises(ReleaseContractError):
            _load_native_document({"type": "RunExecutionSession", "value": {}}, root)

    def test_historical_retirement_carrier_does_not_become_a_current_phase(self) -> None:
        retired = ImageRetirementEvidence(
            "a" * 64, "retired", "synthetic documentary carrier", "sha256:" + "b" * 64,
            "sha256:" + "c" * 64, "d" * 64, (), (), (), "until_verified_promotion", "e" * 64,
            ".caprmedio_runtime/removal-intent.json", 0, True, ".caprmedio_runtime/retirement/attempt",
            "f" * 64, "docker-subprocess", "1" * 64,
        )
        packet = _retirement_recording_handoff(retired)
        candidate = SimpleNamespace(manifest=SimpleNamespace(sha256="a" * 64))
        # Read the historical typed carrier through its actual retained tag
        # codec, not through a nonexistent current retirement phase index.
        name, restored = _load_tag(_tag("retirement", retired), candidate, "/fixture")
        self.assertEqual(name, "retirement")
        self.assertEqual(restored, retired)
        self.assertEqual(_shared_recording(packet, "historical recording"), packet)
        changed = _tag("retirement", retired)
        changed["value"]["candidate_snapshot_manifest_sha256"] = "9" * 64
        with self.assertRaises(ReleaseContractError):
            _load_tag(changed, candidate, "/fixture")
        self.assertEqual(10, len(PHASES))
        self.assertEqual(("CA-O-178", "CA-O-169", "promote"), PHASES[-1])
        self.assertNotIn("retire", [phase for _, _, phase in PHASES])
        result = ReleasePhaseResult(
            "workflow", "step", "action", "CA-O-179", "CA-O-169", "retire", "pending",
            "shared recording remains pending", "a" * 64, ("retire",),
            (packet["retirement_receipt_ref"],), ("declared-run-ref",),
            output=retired, effect_outcome="retired", shared_action_recording=packet,
        )
        context = SelectedReleaseActionContext(
            "/fixture", "workflow", "step", "action", "workflow", "step",
            "CA-O-178", "CA-O-169", "2" * 64, workflow_version=11,
        )
        value = _native_result_value(result, len(PHASES) - 1)
        with self.assertRaises(ReleaseContractError):
            _load_native_result(value, len(PHASES) - 1, context, candidate,
                                {"promotion": retired, "retirement": retired})


class SelectedNativePacketCodecPhysicalTests(unittest.TestCase):
    """Physical typed packet coverage with explicitly mocked command artifacts."""

    @classmethod
    def setUpClass(cls) -> None:
        tests_root = Path(__file__).resolve().parent
        if str(tests_root) not in sys.path:
            sys.path.insert(0, str(tests_root))
        import test_detached_native_full_gate as packet_fixture
        from retained_full_gate_packet import RetainedNativeFullGatePacket

        fixture = packet_fixture.packet_fixtures._NativeHappyPathFixture()
        root, identity, suite, build, verification, e2e, full_gate = packet_fixture.DetachedNativeFullGateTests()._packet(fixture)
        cls.root = root
        cls.packet = RetainedNativeFullGatePacket(root, identity, suite, build, verification, e2e, full_gate)
        cls.candidate = ValidatedCandidate(str(root), fixture.candidate.manifest, fixture.candidate.authority, fixture.candidate.intent)

    def historical_checkpoint(self):
        import work_journal

        packet = self.packet
        manifest = self.candidate.manifest
        default_settings = (
            RELEASE_ROOT.parents[3]
            / resolve_methodology_layout(RELEASE_ROOT.parents[3]).source_root
            / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        )
        settings_path = work_journal.resolve_settings_path(self.root)
        query_defaults = settings_path.parent / (
            "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        )
        query_defaults.parent.mkdir(parents=True, exist_ok=True)
        query_defaults.write_bytes(default_settings.read_bytes())
        request = ReleaseVersionRequest.model_validate({
            "operation": "apply", "project_root": str(self.root),
            "candidateSnapshotManifest": manifest.model_dump(mode="json", by_alias=True),
            "expected_executing_release": manifest.executing_release,
            "expected_project_structure_digest": manifest.project_structure_digest,
            "expected_framework_settings_digest": manifest.framework_settings_digest,
            "expected_source_frontier_digest": manifest.source_frontier_digest,
            "run_receipt_refs": ["historical-packet-documentary-test"],
        })
        publication = NativePromotionEvidence(
            manifest.sha256, "promoted", "documentary packet extraction fixture only", packet.evidence.candidate_image_digest,
            None, manifest.executing_release, packet.evidence.package_manifest_sha256, packet.evidence.receipt_sha256,
            manifest.framework_version, manifest.version_toml_sha256, "actual-action", "actual-start", "1" * 64,
            "2" * 64, 1, f".caprmedio_runtime/release_promotion/{manifest.sha256}/observations/attempt-codec",
            f".caprmedio_runtime/release_promotion/{manifest.sha256}/prior-selector.toml",
        )
        raw = canonical_json(asdict(publication))
        receipt = self.root / publication.evidence_root / "receipt.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_bytes(raw)
        publication = replace(publication, receipt_sha256=hashlib.sha256(raw).hexdigest())
        action_source = self.root / "fixture-selected-source/CA-O-169.md"
        action_source.parent.mkdir(parents=True, exist_ok=True)
        action_source.write_bytes(b"# fixture selected O169 source\n")
        action_definition = {
            "atom_id": "CA-O-169", "version": 5,
            "path": action_source.relative_to(self.root).as_posix(),
            "digest": hashlib.sha256(action_source.read_bytes()).hexdigest(),
        }
        context = SelectedReleaseActionContext(
            str(self.root), "original-workflow", "original-step", publication.action_run_id,
            "original-workflow", "original-step", "CA-O-178", "CA-O-169",
            _fingerprint(request), workflow_version=9,
        )
        result = ReleasePhaseResult(
            context.workflow_run_id, context.step_run_id, context.action_run_id,
            context.step_atom_id, context.action_atom_id, "promote", "completed", publication.reason,
            manifest.sha256, publication.effect_refs, publication.effect_refs, (), output=publication,
            effect_outcome="promoted",
        )
        requested_action = f"{context.workflow_run_id}:step:11:action:1"
        result_ref = (
            f".caprmedio_install/workflow_orchestrator/runs/{context.workflow_run_id}/{requested_action}.json"
        )
        progress_path = self.root / result_ref
        progress_path.parent.mkdir(parents=True, exist_ok=True)
        progress_path.write_bytes(canonical_json({
            "result": "promoted", "action_run_id": context.action_run_id,
            "effect_refs": list(result.effect_evidence_refs), "native_result": asdict(result),
            "compiler_publication_recording": None,
        }))
        started = work_journal.with_event_digest({
            "schema_version": 5, "kind": "workflow_execution", "event_id": publication.action_start_event_id,
            "action_id": "CA-O-169", "event": "started", "author": "fixture-author",
            "occurred_at": "2026-10-10T00:00:00+00:00", "llm_session": {"app": "fixture", "uuid": "1" * 64},
            "structural_scope": "fixture", "initiative": {"initiative_id": "CA-O-169", "instruction_summary": "fixture"},
            "run": {"run_id": context.action_run_id, "kind": "action", "parent_run_id": context.step_run_id,
                    "definition": action_definition},
            "definition_bindings": [{"kind": "action", **action_definition}], "input_ref": "fixture/input.json",
            "outcome": None, "result_ref": None, "effect_refs": [], "report_ref": None,
            "redaction": {"redacted": False, "fields": []},
        })
        terminal = dict(started)
        terminal.update({
            "event_id": "actual-terminal", "event": "completed", "outcome": "completed",
            "result_ref": result_ref, "effect_refs": list(result.effect_evidence_refs),
        })
        terminal = work_journal.with_event_digest(terminal)
        journal_path = self.root / work_journal.configured_journal_root(self.root) / "historical-native-promotion.ndjson"
        journal_path.parent.mkdir(parents=True, exist_ok=True)
        journal_path.write_bytes(canonical_json(started) + b"\n" + canonical_json(terminal) + b"\n")
        self._historical_started = started
        self._historical_terminal = terminal
        self._historical_journal_path = journal_path
        self._historical_progress_path = progress_path
        state = {name: None for name in _NATIVE_STATE_NAMES}
        state.update({"candidate": _candidate_value(self.candidate),
                      "portable_suite": asdict(packet.suite), "build": asdict(packet.build),
                      "verification": asdict(packet.verification), "e2e": asdict(packet.e2e),
                      "full_gate": asdict(packet.evidence), "promotion": asdict(publication),
                      "prepared_portable_package": {
                          "candidate_run_id": packet.evidence.candidate_run_id,
                          "candidate_snapshot_manifest_sha256": manifest.sha256,
                          "input_manifest_sha256": packet.evidence.input_manifest_sha256,
                          "package_manifest_sha256": packet.evidence.package_manifest_sha256,
                      }})
        historical_result = asdict(result)
        historical_result["output"] = "promotion"
        checkpoint = {"schema": LEGACY_NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA, "kind": "release_action_run",
                      "project_root": str(self.root), "workflow_run_id": "original-workflow",
                      "request": request.model_dump(mode="json", by_alias=True), "frozen_parameters_sha256": _fingerprint(request),
                      "next_phase": 11, "stopped": False, "in_progress": None,
                      "contexts": [{"index": 10, "context": asdict(context)}],
                      "results": [{"index": 10, "result": historical_result}],
                      "shared_recordings": [{"index": 10, "terminal_outcome": "completed", "receipt_refs": [terminal["event_id"]]}],
                      "pending_recordings": [], "state": state}
        checkpoint["sha256"] = release_action_checkpoint_sha256(checkpoint)
        # Normalize exactly as the canonical checkpoint carrier does.
        import json
        return json.loads(canonical_json(checkpoint)), request, publication

    def test_historical_packet_transport_ignores_new_checkout_frontier_not_retained_gate(self) -> None:
        checkpoint, request, publication = self.historical_checkpoint()
        source = self.root / "fixture-selected-source/CA-O-169.md"
        before = source.read_bytes()
        try:
            source.write_bytes(before + b"\n# next release source frontier\n")
            packet, observed = read_native_checkpoint_packet(
                checkpoint, project_root=str(self.root), expected_request=request,
                expected_workflow_run_id="original-workflow",
            )
        finally:
            source.write_bytes(before)
        self.assertEqual(packet, self.packet)
        self.assertEqual(observed, publication)
        changed = copy.deepcopy(checkpoint)
        changed["state"]["full_gate"]["receipt_sha256"] = "f" * 64
        changed["sha256"] = release_action_checkpoint_sha256(changed)
        with self.assertRaises(ReleaseContractError):
            read_native_checkpoint_packet(changed, project_root=str(self.root), expected_request=request,
                                          expected_workflow_run_id="original-workflow")

    def test_historical_packet_refuses_missing_pending_tampered_result_or_wrong_start(self) -> None:
        import work_journal

        checkpoint, request, _publication = self.historical_checkpoint()
        cases = []
        cases.append(("missing-terminal", lambda payload: self._historical_journal_path.write_bytes(canonical_json(self._historical_started) + b"\n")))

        def pending(payload):
            payload["pending_recordings"] = [{"index": 10, "event_id": "actual-terminal", "event_outcome": "completed"}]
            payload["sha256"] = release_action_checkpoint_sha256(payload)

        cases.append(("pending", pending))

        def other_publication_action(payload):
            payload["state"]["promotion"]["action_run_id"] = "other-action"
            payload["sha256"] = release_action_checkpoint_sha256(payload)

        cases.append(("other-publication-action", other_publication_action))
        cases.append(("result", lambda payload: self._historical_progress_path.write_bytes(canonical_json({
            "result": "promoted", "action_run_id": "other-action", "effect_refs": [],
            "native_result": {}, "compiler_publication_recording": None,
        }))))

        def tampered_terminal(payload):
            terminal = dict(self._historical_terminal)
            terminal["author"] = "other-author"
            terminal = work_journal.with_event_digest(terminal)
            self._historical_journal_path.write_bytes(
                canonical_json(self._historical_started) + b"\n" + canonical_json(terminal) + b"\n"
            )

        cases.append(("tampered-terminal", tampered_terminal))

        def wrong_start(payload):
            started = dict(self._historical_started)
            terminal = dict(self._historical_terminal)
            started["run"] = {**started["run"], "parent_run_id": "other-step"}
            terminal["run"] = dict(started["run"])
            started = work_journal.with_event_digest(started)
            terminal = work_journal.with_event_digest(terminal)
            self._historical_journal_path.write_bytes(canonical_json(started) + b"\n" + canonical_json(terminal) + b"\n")

        cases.append(("wrong-start", wrong_start))
        for name, mutate in cases:
            with self.subTest(name=name):
                checkpoint, request, _publication = self.historical_checkpoint()
                mutate(checkpoint)
                with self.assertRaises(ReleaseContractError):
                    read_native_checkpoint_packet(
                        checkpoint, project_root=str(self.root), expected_request=request,
                        expected_workflow_run_id="original-workflow",
                    )

    def test_actual_retained_packet_roundtrip_reopens_all_physical_constituents(self) -> None:
        payload = _native_packet_value(self.packet, str(self.root))
        self.assertEqual(_load_native_packet(payload, str(self.root)), self.packet)

    def test_changed_native_descriptor_cannot_reconstruct_transport(self) -> None:
        payload = copy.deepcopy(_native_packet_value(self.packet, str(self.root)))
        payload["descriptor_sha256"] = "9" * 64
        with self.assertRaises(ReleaseContractError):
            _load_native_packet(payload, str(self.root))

    def test_native_packet_refuses_legacy_e2e_coercion_and_unknown_members(self) -> None:
        payload = copy.deepcopy(_native_packet_value(self.packet, str(self.root)))
        payload["e2e"].pop("package_manifest_sha256")
        with self.assertRaises(ReleaseContractError):
            _load_native_packet(payload, str(self.root))
        payload = copy.deepcopy(_native_packet_value(self.packet, str(self.root)))
        payload["native_action"] = "CA-O-200"
        with self.assertRaises(ReleaseContractError):
            _load_native_packet(payload, str(self.root))


if __name__ == "__main__":
    unittest.main()
