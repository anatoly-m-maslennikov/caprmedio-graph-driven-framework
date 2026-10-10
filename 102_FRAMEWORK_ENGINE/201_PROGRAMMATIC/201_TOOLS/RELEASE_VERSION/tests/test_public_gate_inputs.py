"""Focused physical-input refusals for the future public Full Gate producer."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import SimpleNamespace
import shutil
import sys
import tempfile
import unittest
from unittest import mock


TOOLS = Path(__file__).resolve().parents[2]
RELEASE = TOOLS / "RELEASE_VERSION"
PUBLIC = TOOLS / "PUBLIC_RELEASE"
MCP = TOOLS.parent / "204_MCP"
REPOSITORY = MCP.parents[2]
for path in (str(TOOLS), str(RELEASE), str(PUBLIC), str(MCP), str(MCP / "tests")):
    if path not in sys.path:
        sys.path.insert(0, path)

import release_public_gate as public_gate  # noqa: E402
import selected_admission as public_admission  # noqa: E402
from public_release import SourceProof  # noqa: E402
from release_handoff import NativeInstalledNBinding  # noqa: E402
from release_retained_package import RetainedNativePackageEvidence  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402
from selected_routes import canonical_digest, load_selected_manifest, selected_manifest_ref  # noqa: E402
from test_release_manifest_admission import ReleaseManifestAdmissionTest  # noqa: E402
from workflow_run_support import RunExecutionSession, RunTracker, _canonical_digest, _proposal  # noqa: E402


class PublicFreshGateInputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = ReleaseManifestAdmissionTest()
        self.fixture.setUpClass()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.save(self.fixture.successor())
        self.fixture._copy_public_release_sources()
        self.root = self.fixture.root.resolve()
        settings = REPOSITORY / ".caprmedio_caprmedio" / "caprmedio_project_settings.toml"
        target_settings = self.root / ".caprmedio_caprmedio" / "caprmedio_project_settings.toml"
        target_settings.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(settings, target_settings)
        (self.root / ".git").mkdir()
        self._d613_context = self.fixture._locally_completed_d613()
        self._d613_context.__enter__()
        self.addCleanup(self._d613_context.__exit__, None, None, None)
        record = public_admission.derive_public_release_source_admission(self.root)
        self.fixture.save(self.fixture.public_successor(record))
        self.manifest = load_selected_manifest(self.root)
        (self.root / "README.md").write_text("# CAPRMEDIO\n", encoding="utf-8")
        (self.root / "docs").mkdir()
        (self.root / "docs" / "public-pr.md").write_text(
            "# Release\n\n## What's new\n\n- Gate.\n\n## What's fixed\n\n- Binding.\n",
            encoding="utf-8",
        )
        (self.root / "VERSION_HISTORY.md").write_text("- Gate\n", encoding="utf-8")
        (self.root / "version.toml").write_text("[framework]\nversion = \"0.4.1\"\n", encoding="utf-8")
        self.candidate_sha = "a" * 64
        self.package_sha = "b" * 64
        self.catalog_sha = "c" * 64
        self.receipt_sha = "d" * 64
        self.image_sha = "e" * 64
        self.source = self._source()
        self.packet, self.retained, self.current = self._native_inputs()
        self.session = self._session("CA-O-194")

    def _source(self, *, pr_number: int | None = None) -> SourceProof:
        pr_url = (
            f"https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/pull/{pr_number}"
            if pr_number is not None else None
        )
        history = "- Gate" + (f" [PR #{pr_number}]({pr_url})" if pr_url else "") + "\n"
        (self.root / "VERSION_HISTORY.md").write_text(history, encoding="utf-8")
        values = {
            "candidate_snapshot_manifest_sha256": self.candidate_sha,
            "framework_version": "0.4.1",
            "version_toml_sha256": sha256((self.root / "version.toml").read_bytes()).hexdigest(),
            "readme_ref": "README.md",
            "readme_sha256": sha256((self.root / "README.md").read_bytes()).hexdigest(),
            "pr_body_ref": "docs/public-pr.md",
            "pr_body_sha256": sha256((self.root / "docs" / "public-pr.md").read_bytes()).hexdigest(),
            "version_history_ref": "VERSION_HISTORY.md",
            "version_history_sha256": sha256(history.encode("utf-8")).hexdigest(),
            "version_history_summary": "Gate",
            "version_history_pr_url": pr_url,
            "version_history_pr_number": pr_number,
        }
        fields = SourceProof.__dataclass_fields__
        source = SourceProof(**{key: values[key] for key, field in fields.items() if field.init})
        self.assertEqual(source.public_document_closure_sha256, public_gate._document_closure(source))
        return source

    def _requested_rows(self) -> list[dict[str, object]]:
        route = self.manifest["routes"][-1]
        workflow = route["workflow"]
        rows: list[dict[str, object]] = [{
            "requested_run_id": "workflow",
            "kind": "workflow",
            "definition": {
                "atom_id": workflow["atom_id"], "version": workflow["version"],
                "path": workflow["source_path"], "digest": workflow["digest"],
            },
        }]
        for pair in route["ordered_steps"]:
            step, action = pair["step"], pair["action"]
            step_requested = f"step-{step['atom_id'].removeprefix('CA-O-')}"
            rows.extend((
                {
                    "requested_run_id": step_requested,
                    "kind": "step",
                    "definition": {
                        "atom_id": step["atom_id"], "version": step["version"],
                        "path": step["source_path"], "digest": step["digest"],
                    },
                    "parent_requested_run_id": "workflow",
                },
                {
                    "requested_run_id": f"action-{action['atom_id'].removeprefix('CA-O-')}",
                    "kind": "action",
                    "definition": {
                        "atom_id": action["atom_id"], "version": action["version"],
                        "path": action["source_path"], "digest": action["digest"],
                    },
                    "parent_requested_run_id": step_requested,
                },
            ))
        return rows

    @staticmethod
    def _requested_id(session: RunExecutionSession, atom_id: str) -> str:
        return next(
            requested_id for requested_id, row in session.requested.items()
            if row["definition"]["atom_id"] == atom_id
        )

    def _session(self, action_id: str) -> RunExecutionSession:
        requested = self._requested_rows()
        parameters = {
            "release": {
                "selected_version": "0.4.1",
                "release_branch": "amm/dev",
                "target_branch": "main",
                "remote": {
                    "scope": "personal",
                    "name": "personal",
                    "owner": "anatoly-m-maslennikov",
                    "repository": "caprmedio-graph-driven-framework",
                },
            },
            "source": {
                "candidate_snapshot_manifest_sha256": self.candidate_sha,
                "readme_ref": "README.md",
                "pr_body_ref": "docs/public-pr.md",
                "version_history_ref": "VERSION_HISTORY.md",
                "version_history_summary": "Gate",
            },
            "recovery": {"prior_push": "not_started", "prior_pr": "not_started"},
        }
        frontier = ["README.md", "VERSION_HISTORY.md", "docs/public-pr.md"]
        effects = [
            {"type": "git_push", "target": "amm/dev"},
            {"type": "pull_request_upsert", "target": "main"},
        ]
        request = {
            "request_id": f"public-gate-input-{action_id}",
            "assigned_action_id": action_id,
            "initiative": {
                "initiative_id": "public-gate-inputs",
                "instruction_summary": "record the admitted public Action start",
            },
            "mode": "execute",
            "operation_route": "public.release",
            "parameters": parameters,
            "parameters_digest": canonical_digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": canonical_digest(frontier),
            "effects": effects,
            "effects_digest": canonical_digest(effects),
            "definition_manifest": {
                "manifest_ref": self.manifest["manifest_ref"],
                "manifest_digest": self.manifest["canonical_manifest_sha256"],
            },
            "source_freshness": self.manifest["source_freshness"],
            "requested_runs": requested,
        }
        tracker = RunTracker(
            self.root,
            source_observer=lambda _request: {"selected": True, "current": True, "observed": {
                "definition_manifest": request["definition_manifest"],
                **request["source_freshness"],
            }},
            executor=lambda _request, _runs: {"outcome": "no_op", "result_ref": "results/no-op.json", "effect_refs": []},
            journal_context={"author": "public-gate-fixture", "timezone": "UTC"},
        )
        proposal = _proposal(request, tracker._observe(request))
        request["proposal_receipt"] = proposal
        request["proposal_receipt_digest"] = _canonical_digest(proposal)
        request["operator_authorization"] = {
            "authorization_ref": "authorizations/public-gate-inputs.md",
            "authorization_freshness": {"state": "current", "digest": "9" * 64},
            "request_id": request["request_id"],
            "operation_route": request["operation_route"],
            "proposal_receipt_digest": request["proposal_receipt_digest"],
            "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"],
            "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }
        session = RunExecutionSession(tracker, request)
        session.start_run("workflow", run_id="actual-workflow")
        for _name, step_id, candidate_action_id in public_gate.STEPS:
            step = session.start_run(self._requested_id(session, step_id), run_id=f"actual-{step_id.lower()}")
            action = session.start_run(
                self._requested_id(session, candidate_action_id), run_id=f"actual-{candidate_action_id.lower()}"
            )
            if candidate_action_id == action_id:
                break
            session.finish_run(action["run_id"], outcome="completed", result_ref=f"results/{candidate_action_id}.json", effect_refs=[])
            session.finish_run(step["run_id"], outcome="completed", result_ref=f"results/{step_id}.json", effect_refs=[])
        return session

    @staticmethod
    def _refresh_execute_admission(session: RunExecutionSession) -> None:
        request = session.request
        request["parameters_digest"] = canonical_digest(request["parameters"])
        proposal = _proposal(request, session.tracker._observe(request))
        request["proposal_receipt"] = proposal
        request["proposal_receipt_digest"] = _canonical_digest(proposal)
        authorization = request["operator_authorization"]
        authorization["parameters_digest"] = request["parameters_digest"]
        authorization["proposal_receipt_digest"] = request["proposal_receipt_digest"]

    def _journal_carrier(self) -> Path:
        return next((self.root / ".caprmedio_caprmedio" / "_journal").glob("*.ndjson"))

    def _native_inputs(self):
        candidate = SimpleNamespace(
            candidate_snapshot_manifest_sha256=self.candidate_sha,
            framework_version="0.4.1",
            version_toml_sha256=self.source.version_toml_sha256,
        )
        evidence = SimpleNamespace(
            candidate_snapshot_manifest_sha256=self.candidate_sha,
            framework_version="0.4.1",
            version_toml_sha256=self.source.version_toml_sha256,
            package_manifest_sha256=self.package_sha,
            receipt_sha256=self.receipt_sha,
            candidate_image_digest="sha256:" + self.image_sha,
        )
        packet = RetainedNativeFullGatePacket(
            self.root,
            candidate,
            object(),
            object(),
            object(),
            object(),
            evidence,
        )
        view = SimpleNamespace(
            candidate_snapshot_manifest_sha256=self.candidate_sha,
            actual_package_manifest_sha256=self.package_sha,
            source_catalog_sha256=self.catalog_sha,
            framework_version="0.4.1",
            version_toml_sha256=self.source.version_toml_sha256,
        )
        retained = RetainedNativePackageEvidence(view, "f" * 64, self.root / "package-evidence.json")
        package = SimpleNamespace(
            manifest_digest=self.package_sha,
            framework_version="0.4.1",
            version_toml_sha256=self.source.version_toml_sha256,
            source_catalog_sha256=self.catalog_sha,
        )
        selected = SimpleNamespace(
            package_manifest_sha256=self.package_sha,
            framework_version="0.4.1",
            version_toml_sha256=self.source.version_toml_sha256,
            source_catalog_sha256=self.catalog_sha,
            full_gate_receipt_sha256=self.receipt_sha,
            image_digest=self.image_sha,
        )
        current = NativeInstalledNBinding(package, packet, selected)
        return packet, retained, current

    def _reopen(self, *, current=None):
        selected = self.current if current is None else current
        return mock.patch.multiple(
            public_gate,
            verify_detached_native_full_gate_evidence=mock.DEFAULT,
            bind_selected_native_n_from_checkpoint=mock.DEFAULT,
            reopen_native_installed_n=mock.DEFAULT,
        ), selected

    def test_reopens_initial_inputs_without_claiming_a_gate_result(self) -> None:
        patches, current = self._reopen()
        with patches as patched:
            patched["verify_detached_native_full_gate_evidence"].return_value = self.retained
            patched["bind_selected_native_n_from_checkpoint"].return_value = current
            patched["reopen_native_installed_n"].return_value = current
            inputs = public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )

        self.assertIsInstance(inputs, public_gate.PublicFreshGateInputs)
        self.assertEqual(inputs.phase, "initial")
        self.assertEqual(inputs.action_definition_id, "CA-O-194")
        self.assertEqual(inputs.public_document_closure_sha256, public_gate._document_closure(self.source))
        self.assertEqual(inputs.fresh_attempt_root.parent.parent, self.root / ".caprmedio_tmp")
        self.assertFalse(hasattr(inputs, "passed"))
        self.assertFalse(inputs.fresh_attempt_root.exists())

    def test_derives_history_link_phase_from_active_o198_action(self) -> None:
        self.source = self._source(pr_number=42)
        self.session = self._session("CA-O-198")
        patches, current = self._reopen()
        with patches as patched:
            patched["verify_detached_native_full_gate_evidence"].return_value = self.retained
            patched["bind_selected_native_n_from_checkpoint"].return_value = current
            patched["reopen_native_installed_n"].return_value = current
            inputs = public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )

        self.assertEqual(inputs.phase, "history_link")
        self.assertEqual(inputs.action_definition_id, "CA-O-198")

    def test_initial_phase_allows_an_already_actual_pr_link(self) -> None:
        self.source = self._source(pr_number=42)
        self.session = self._session("CA-O-194")
        patches, current = self._reopen()
        with patches as patched:
            patched["verify_detached_native_full_gate_evidence"].return_value = self.retained
            patched["bind_selected_native_n_from_checkpoint"].return_value = current
            patched["reopen_native_installed_n"].return_value = current
            inputs = public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )

        self.assertEqual(inputs.phase, "initial")

    def test_refuses_history_link_without_the_actual_pr_proof(self) -> None:
        self.session = self._session("CA-O-198")

        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )

        self.assertEqual(raised.exception.code, "public-gate-history-source-unproven")

    def test_refuses_forged_document_closure_before_any_native_reopen(self) -> None:
        object.__setattr__(self.source, "public_document_closure_sha256", "0" * 64)
        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )
        self.assertEqual(raised.exception.code, "public-gate-source-stale")

    def test_refuses_stale_document_bytes_before_any_native_reopen(self) -> None:
        (self.root / "VERSION_HISTORY.md").write_text("- changed\n", encoding="utf-8")
        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )
        self.assertEqual(raised.exception.code, "public-gate-source-stale")

    def test_refuses_missing_active_action_parent(self) -> None:
        action = self._requested_id(self.session, "CA-O-194")
        self.session.actual[action]["parent_run_id"] = "different-step"
        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )
        self.assertEqual(raised.exception.code, "public-gate-action-lineage-invalid")

    def test_refuses_fabricated_session_without_a_recorded_action_start(self) -> None:
        fabricated = object.__new__(RunExecutionSession)
        fabricated.tracker = self.session.tracker
        fabricated.request = self.session.request
        fabricated.requested = self.session.requested
        fabricated.actual = self.session.actual
        fabricated.terminal = {}
        fabricated.interrupted = {}

        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, fabricated, self.packet, self.source
            )

        self.assertEqual(raised.exception.code, "public-gate-action-lineage-invalid")

    def test_refuses_when_the_receipt_addressed_action_start_is_absent(self) -> None:
        carrier = self._journal_carrier()
        carrier.unlink()

        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )

        self.assertEqual(raised.exception.code, "public-gate-action-lineage-invalid")

    def test_refuses_each_admitted_source_binding_that_differs_from_the_reopened_source_proof(self) -> None:
        source_parameters = self.session.request["parameters"]["source"]
        replacements = {
            "candidate_snapshot_manifest_sha256": "f" * 64,
            "readme_ref": "VERSION_HISTORY.md",
            "pr_body_ref": "README.md",
            "version_history_ref": "docs/public-pr.md",
            "version_history_summary": "Different retained summary",
        }
        patches, _ = self._reopen()
        with patches as patched:
            for field, replacement in replacements.items():
                with self.subTest(field=field):
                    original = source_parameters[field]
                    source_parameters[field] = replacement
                    self._refresh_execute_admission(self.session)
                    try:
                        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
                            public_gate.reopen_public_fresh_gate_inputs(
                                self.root, self.session, self.packet, self.source
                            )
                    finally:
                        source_parameters[field] = original
                        self._refresh_execute_admission(self.session)
                    self.assertEqual(raised.exception.code, "public-gate-source-mismatch")
            patched["verify_detached_native_full_gate_evidence"].assert_not_called()
            patched["bind_selected_native_n_from_checkpoint"].assert_not_called()
            patched["reopen_native_installed_n"].assert_not_called()

    def test_refuses_mutated_step_or_workflow_records_despite_their_mutable_session_lineage(self) -> None:
        for atom_id in ("CA-O-193", "CA-O-188"):
            with self.subTest(atom_id=atom_id):
                session = self._session("CA-O-194")
                requested = self._requested_id(session, atom_id)
                record = session.actual[requested]
                record["definition"] = {**record["definition"], "digest": "f" * 64}

                with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
                    public_gate.reopen_public_fresh_gate_inputs(
                        self.root, session, self.packet, self.source
                    )

                self.assertEqual(raised.exception.code, "public-gate-action-lineage-invalid")

    def test_refuses_absent_public_source_admission_before_native_reopen(self) -> None:
        path = self.root / selected_manifest_ref(self.root)
        raw = json.loads(path.read_text(encoding="utf-8"))
        raw.pop("public_release_source_admissions")
        unsigned = {key: value for key, value in raw.items() if key != "canonical_manifest_sha256"}
        raw["canonical_manifest_sha256"] = canonical_digest(unsigned)
        path.write_text(json.dumps(raw, separators=(",", ":")), encoding="utf-8")

        with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
            public_gate.reopen_public_fresh_gate_inputs(
                self.root, self.session, self.packet, self.source
            )

        self.assertEqual(raised.exception.code, "public-gate-session-unadmitted")

    def test_refuses_current_n_image_mismatch(self) -> None:
        mismatched = NativeInstalledNBinding(
            self.current.verified_package,
            self.packet,
            SimpleNamespace(**{**vars(self.current.selected), "image_digest": "f" * 64}),
        )
        patches, _ = self._reopen(current=mismatched)
        with patches as patched:
            patched["verify_detached_native_full_gate_evidence"].return_value = self.retained
            patched["bind_selected_native_n_from_checkpoint"].return_value = mismatched
            patched["reopen_native_installed_n"].return_value = mismatched
            with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
                public_gate.reopen_public_fresh_gate_inputs(
                    self.root, self.session, self.packet, self.source
                )
        self.assertEqual(raised.exception.code, "public-gate-identity-mismatch")

    def test_refuses_current_n_packet_for_a_different_candidate(self) -> None:
        other_packet = RetainedNativeFullGatePacket(
            self.root,
            SimpleNamespace(
                candidate_snapshot_manifest_sha256="f" * 64,
                framework_version="0.4.1",
                version_toml_sha256=self.source.version_toml_sha256,
            ),
            self.packet.suite,
            self.packet.build,
            self.packet.verification,
            self.packet.e2e,
            self.packet.evidence,
        )
        mismatched = NativeInstalledNBinding(
            self.current.verified_package,
            other_packet,
            self.current.selected,
        )
        patches, _ = self._reopen(current=mismatched)
        with patches as patched:
            patched["verify_detached_native_full_gate_evidence"].return_value = self.retained
            patched["bind_selected_native_n_from_checkpoint"].return_value = mismatched
            patched["reopen_native_installed_n"].return_value = mismatched
            with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
                public_gate.reopen_public_fresh_gate_inputs(
                    self.root, self.session, self.packet, self.source
                )
        self.assertEqual(raised.exception.code, "public-gate-identity-mismatch")

    def test_refuses_original_packet_from_another_project(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as foreign:
            packet = RetainedNativeFullGatePacket(
                Path(foreign).resolve(),
                self.packet.retained_candidate,
                self.packet.suite,
                self.packet.build,
                self.packet.verification,
                self.packet.e2e,
                self.packet.evidence,
            )
            with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
                public_gate.reopen_public_fresh_gate_inputs(
                    self.root, self.session, packet, self.source
                )
        self.assertEqual(raised.exception.code, "public-gate-original-packet-invalid")

    def test_refuses_when_current_n_cannot_be_physically_reopened(self) -> None:
        patches, _ = self._reopen()
        with patches as patched:
            patched["verify_detached_native_full_gate_evidence"].return_value = self.retained
            patched["bind_selected_native_n_from_checkpoint"].return_value = None
            with self.assertRaises(public_gate.PublicFreshGateInputError) as raised:
                public_gate.reopen_public_fresh_gate_inputs(
                    self.root, self.session, self.packet, self.source
                )
        self.assertEqual(raised.exception.code, "public-gate-current-n-unavailable")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
