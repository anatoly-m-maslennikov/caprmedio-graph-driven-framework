"""Host-only assembly tests for the separately commanded O199 admission seam."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from source_admission_host import (  # noqa: E402
    SourceAdmissionHostError,
    make_source_admission_invocation_admitter,
)
from source_catalog_admission import AdmissionInvocationRequest  # noqa: E402
from workflow_run_support import RunExecutionSession, RunTracker  # noqa: E402


class SourceAdmissionHostTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.operator = "trusted-operator"
        self.registry_ref = ".caprmedio_fixture/operators_registry.toml"
        registry = self.root / self.registry_ref
        registry.parent.mkdir()
        registry.write_text(
            f'[[operators]]\nname = "{self.operator}"\nrole = "project owner"\n', encoding="utf-8",
        )
        self.action_path = Path("operations/CA-O-199.md")
        self._write_action("# Admit local package sources\n")

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _write_action(self, content: str) -> None:
        path = self.root / self.action_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    @staticmethod
    def _definition(kind: str, atom_id: str, *, digest: str = "a" * 64) -> dict[str, object]:
        return {"atom_id": atom_id, "version": 1, "path": f"operations/{atom_id}.md", "digest": digest}

    def _session(self, *, author: str | None = None) -> tuple[RunExecutionSession, str]:
        tracker = RunTracker(
            self.root,
            source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
            executor=lambda _request, _runs: {"outcome": "no_op", "result_ref": "results/no-op.json", "effect_refs": []},
            journal_context={"author": author or self.operator, "timezone": "UTC"},
        )
        request = {
            "request_id": "o199-host-fixture",
            "assigned_action_id": "caller-controlled-assignment-is-not-provenance",
            "initiative": {"initiative_id": "fixture", "instruction_summary": "record O199 start"},
            "requested_runs": [
                {"requested_run_id": "workflow", "kind": "workflow", "definition": self._definition("workflow", "CA-O-1")},
                {"requested_run_id": "step", "kind": "step", "definition": self._definition("step", "CA-O-2"), "parent_requested_run_id": "workflow"},
                {
                    "requested_run_id": "action",
                    "kind": "action",
                    "definition": self._definition(
                        "action", "CA-O-199",
                        digest=hashlib.sha256((self.root / self.action_path).read_bytes()).hexdigest(),
                    ),
                    "parent_requested_run_id": "step",
                },
            ],
        }
        session = RunExecutionSession(tracker, request)
        session.start_run("workflow", run_id="actual-workflow")
        session.start_run("step", run_id="actual-step")
        action = session.start_run("action", run_id="actual-action")
        return session, action["run_id"]

    def _context(self, session: RunExecutionSession, action_run_id: str, *, action_id: str = "CA-O-199") -> dict[str, object]:
        payload = (self.root / self.action_path).read_bytes()
        return {
            "project_root": self.root,
            "sealed_outer_admission": True,
            "action_definition_id": action_id,
            "action_definition": {
                "atom_id": action_id,
                "kind": "action",
                "version": 1,
                "path": self.action_path.as_posix(),
                "sha256": hashlib.sha256(payload).hexdigest(),
            },
            "session": session,
            "action_run_id": action_run_id,
            "requested_action_run_id": "action",
            # These are deliberately ignored by the helper.
            "parameters": {"operator": "caller supplied", "command_ref": "caller supplied"},
        }

    @staticmethod
    def _request() -> AdmissionInvocationRequest:
        return AdmissionInvocationRequest("a" * 64, ())

    def _assert_no_publication(self) -> None:
        self.assertFalse((self.root / "catalog.toml").exists())
        self.assertFalse((self.root / "admissions").exists())

    def test_binds_real_sealed_start_to_explicit_mocked_host_command(self) -> None:
        session, action_run_id = self._session()
        observed: list[object] = []

        def trusted_host_binder(request, provenance):
            observed.extend((request, provenance))
            self.assertEqual(self.operator, provenance.author)
            self.assertEqual(action_run_id, provenance.action_run_id)
            self.assertEqual(("actual-step", "actual-workflow"), provenance.parent_lineage)
            return self.operator, "commands/o199/fixture"

        admitter = make_source_admission_invocation_admitter(
            self.root, selected_context=self._context(session, action_run_id),
            operators_registry_ref=self.registry_ref, command_binder=trusted_host_binder,
        )
        invocation = admitter(self._request())

        self.assertEqual("a" * 64, invocation.snapshot_sha256)
        self.assertEqual(self.operator, invocation.operator)
        self.assertEqual("commands/o199/fixture", invocation.command_ref)
        self.assertEqual(action_run_id, invocation.action_run_id)
        self.assertEqual(2, len(observed))
        self._assert_no_publication()

    def test_wrong_action_definition_refuses_before_binder(self) -> None:
        session, action_run_id = self._session()
        called = False

        def binder(_request, _provenance):
            nonlocal called
            called = True
            return self.operator, "commands/o199/fixture"

        with self.assertRaises(SourceAdmissionHostError) as refused:
            make_source_admission_invocation_admitter(
                self.root, selected_context=self._context(session, action_run_id, action_id="CA-O-198"),
                operators_registry_ref=self.registry_ref, command_binder=binder,
            )
        self.assertEqual("source-admission-host-action-invalid", refused.exception.code)
        self.assertFalse(called)
        self._assert_no_publication()

    def test_context_must_match_actual_action_binding_and_session_project(self) -> None:
        session, action_run_id = self._session()
        context = self._context(session, action_run_id)
        definition = dict(context["action_definition"])
        definition["sha256"] = "b" * 64
        context["action_definition"] = definition
        with self.assertRaises(SourceAdmissionHostError) as binding:
            make_source_admission_invocation_admitter(
                self.root, selected_context=context,
                operators_registry_ref=self.registry_ref,
                command_binder=lambda _request, _provenance: (self.operator, "commands/o199/fixture"),
            )
        self.assertEqual("source-admission-host-context-invalid", binding.exception.code)
        self._assert_no_publication()

        session, action_run_id = self._session()
        foreign_root = self.root / "other-project"
        foreign_root.mkdir()
        session.tracker.root = foreign_root
        with self.assertRaises(SourceAdmissionHostError) as project:
            make_source_admission_invocation_admitter(
                self.root, selected_context=self._context(session, action_run_id),
                operators_registry_ref=self.registry_ref,
                command_binder=lambda _request, _provenance: (self.operator, "commands/o199/fixture"),
            )
        self.assertEqual("source-admission-host-context-invalid", project.exception.code)
        self._assert_no_publication()

    def test_run_support_or_unregistered_journal_author_refuses_before_binder(self) -> None:
        for author in ("run-support", "unregistered-operator"):
            with self.subTest(author=author):
                session, action_run_id = self._session(author=author)
                called = False

                def binder(_request, _provenance):
                    nonlocal called
                    called = True
                    return author, "commands/o199/fixture"

                admitter = make_source_admission_invocation_admitter(
                    self.root, selected_context=self._context(session, action_run_id),
                    operators_registry_ref=self.registry_ref, command_binder=binder,
                )
                with self.assertRaises(SourceAdmissionHostError) as refused:
                    admitter(self._request())
                self.assertEqual("source-admission-host-operator-invalid", refused.exception.code)
                self.assertFalse(called)
                self._assert_no_publication()

    def test_mismatched_or_failed_binder_refuses_without_publication(self) -> None:
        session, action_run_id = self._session()
        admitter = make_source_admission_invocation_admitter(
            self.root,
            selected_context=self._context(session, action_run_id),
            operators_registry_ref=self.registry_ref,
            command_binder=lambda _request, _provenance: ("other-operator", "commands/o199/fixture"),
        )
        with self.assertRaises(SourceAdmissionHostError) as mismatch:
            admitter(self._request())
        self.assertEqual("source-admission-host-command-invalid", mismatch.exception.code)
        self._assert_no_publication()

        def rejected(_request, _provenance):
            raise RuntimeError("host rejected command")

        failed = make_source_admission_invocation_admitter(
            self.root, selected_context=self._context(session, action_run_id),
            operators_registry_ref=self.registry_ref, command_binder=rejected,
        )
        with self.assertRaises(SourceAdmissionHostError) as refusal:
            failed(self._request())
        self.assertEqual("source-admission-host-command-rejected", refusal.exception.code)
        self._assert_no_publication()

    def test_changed_retained_start_evidence_after_binder_refuses_without_publication(self) -> None:
        session, action_run_id = self._session()

        def binder(_request, _provenance):
            changed = dict(session._started_receipts["action"])
            changed["event_id"] = "event-forged-after-binding"
            session._started_receipts["action"] = changed
            return self.operator, "commands/o199/fixture"

        admitter = make_source_admission_invocation_admitter(
            self.root, selected_context=self._context(session, action_run_id),
            operators_registry_ref=self.registry_ref, command_binder=binder,
        )
        with self.assertRaises(SourceAdmissionHostError) as refused:
            admitter(self._request())
        self.assertEqual("source-admission-host-start-invalid", refused.exception.code)
        self._assert_no_publication()

    def test_actual_run_binding_mutation_after_binder_refuses_without_publication(self) -> None:
        session, action_run_id = self._session()

        def binder(_request, _provenance):
            changed = dict(session.actual["action"]["definition"])
            changed["digest"] = "b" * 64
            session.actual["action"]["definition"] = changed
            return self.operator, "commands/o199/fixture"

        admitter = make_source_admission_invocation_admitter(
            self.root, selected_context=self._context(session, action_run_id),
            operators_registry_ref=self.registry_ref, command_binder=binder,
        )
        with self.assertRaises(SourceAdmissionHostError) as refused:
            admitter(self._request())
        self.assertEqual("source-admission-host-context-stale", refused.exception.code)
        self._assert_no_publication()

    def test_registry_or_action_source_drift_after_binder_refuses_without_publication(self) -> None:
        cases = ("registry", "source")
        for case in cases:
            with self.subTest(case=case):
                session, action_run_id = self._session()

                def binder(_request, _provenance, *, _case=case):
                    if _case == "registry":
                        (self.root / self.registry_ref).write_text(
                            f'[[operators]]\nname = "{self.operator}"\nrole = "changed role"\n', encoding="utf-8",
                        )
                    else:
                        self._write_action("# changed after host binding\n")
                    return self.operator, "commands/o199/fixture"

                admitter = make_source_admission_invocation_admitter(
                    self.root, selected_context=self._context(session, action_run_id),
                    operators_registry_ref=self.registry_ref, command_binder=binder,
                )
                with self.assertRaises(SourceAdmissionHostError) as refused:
                    admitter(self._request())
                expected = "source-admission-host-operator-stale" if case == "registry" else "source-admission-host-source-stale"
                self.assertEqual(expected, refused.exception.code)
                self._assert_no_publication()
                if case == "registry":
                    (self.root / self.registry_ref).write_text(
                        f'[[operators]]\nname = "{self.operator}"\nrole = "project owner"\n', encoding="utf-8",
                    )
                else:
                    self._write_action("# Admit local package sources\n")


if __name__ == "__main__":
    unittest.main()
