"""Closed selected command and actual canonical Session provenance tests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import unittest

RELEASE_ROOT = Path(__file__).resolve().parents[1]
for folder in (RELEASE_ROOT, RELEASE_ROOT.parent, Path(__file__).resolve().parent):
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))

from release_actions import SelectedReleaseActionContext, begin_release_action_run  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_handoff import FRAMEWORK_SETTINGS_RELATIVE  # noqa: E402
from release_promotion import admit_selected_native_promotion_start  # noqa: E402
from selected_installation_command import (  # noqa: E402
    SelectedInstallationCommandError, read_selected_installation_command_receipt,
    reopen_selected_installation_command_start,
    _registered_journal_author,
)
from workflow_run_support import RunExecutionSession, RunTracker  # noqa: E402
import work_journal  # noqa: E402
import test_portable_contract as portable_fixture  # noqa: E402
from operator_registry import parse_operators_registry  # noqa: E402


class SelectedRegisteredJournalAuthorTests(unittest.TestCase):
    def test_literal_registered_account_name_needs_no_alias_mapping(self) -> None:
        record = parse_operators_registry(b'[[operators]]\nname = "fixture-author"\nrole = "maintainer"\n')[0]
        self.assertEqual(_registered_journal_author(record), "fixture-author")

    def test_unmapped_human_name_is_not_inferred_as_account(self) -> None:
        record = parse_operators_registry(b'[[operators]]\nname = "Registered Fixture"\nrole = "maintainer"\n')[0]
        self.assertIsNone(_registered_journal_author(record))


class SelectedInstallationCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = portable_fixture.PortableContractTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        retired_settings = self.fixture.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml"
        canonical_settings = self.root / FRAMEWORK_SETTINGS_RELATIVE
        if retired_settings != canonical_settings and retired_settings.is_file():
            canonical_settings.parent.mkdir(parents=True, exist_ok=True)
            canonical_settings.write_bytes(retired_settings.read_bytes())
            retired_settings.unlink()
        candidate, _private = self.fixture.sealed()
        manifest = candidate.manifest.model_dump(mode="json", by_alias=True)
        parameters = {
            "operation": "apply", "project_root": str(self.root),
            "candidateSnapshotManifest": manifest,
            "expected_executing_release": manifest["executing_release"],
            "expected_project_structure_digest": manifest["project_structure_digest"],
            "expected_framework_settings_digest": manifest["framework_settings_digest"],
            "expected_source_frontier_digest": manifest["source_frontier_digest"],
            "run_receipt_refs": ["fixture-release-receipt"],
        }
        definitions = {}
        for kind, atom_id, version in (("workflow", "CA-O-164", 9), ("step", "CA-O-178", 3), ("action", "CA-O-169", 5)):
            relative = f"operations/{atom_id}.md"
            path = self.root / relative
            path.parent.mkdir(exist_ok=True)
            payload = f"---\natom_id: {atom_id}\nversion: {version}\n---\nfixture source\n".encode()
            path.write_bytes(payload)
            definitions[kind] = {"atom_id": atom_id, "version": version, "path": relative,
                                 "digest": hashlib.sha256(payload).hexdigest()}
        requested = [
            {"requested_run_id": "wf", "kind": "workflow", "definition": definitions["workflow"]},
            {"requested_run_id": "step", "kind": "step", "definition": definitions["step"], "parent_requested_run_id": "wf"},
            {"requested_run_id": "action", "kind": "action", "definition": definitions["action"], "parent_requested_run_id": "step"},
        ]
        request = {
            "mode": "execute", "request_id": "selected-promotion-fixture", "operation_route": "release_version",
            "parameters": parameters, "parameters_digest": hashlib.sha256(canonical_json(parameters)).hexdigest(),
            "target_frontier_digest": "a" * 64, "effects_digest": "b" * 64,
            "definition_manifest": {"manifest_ref": "fixture.json", "manifest_digest": "c" * 64},
            "source_freshness": {}, "assigned_action_id": "selected-fixture-assignment",
            "initiative": {"initiative_id": "fixture", "instruction_summary": "selected publication test"},
            "requested_runs": requested, "proposal_receipt": {"fixture": "exact"}, "proposal_receipt_digest": "d" * 64,
        }
        auth_keys = ("request_id", "operation_route", "proposal_receipt_digest", "parameters_digest",
                     "target_frontier_digest", "effects_digest", "definition_manifest", "source_freshness")
        request["operator_authorization"] = {
            **{key: request[key] for key in auth_keys}, "authorization_ref": "fixture/authorization",
            "authorization_freshness": {"state": "current", "digest": "e" * 64},
        }
        self.tracker = RunTracker(
            self.root, source_observer=lambda _request: {"selected": True, "current": True, "observed": {}},
            executor=lambda _request, _runs: {}, journal_context={"author": "fixture-author", "timezone": "UTC"},
        )
        self.session = RunExecutionSession(self.tracker, request)
        self.session.start_run("wf", run_id="actual-workflow")
        self.session.start_run("step", run_id="actual-step")
        self.session.start_run("action", run_id="actual-action")
        self.run = begin_release_action_run(parameters, workflow_run_id="actual-workflow")
        self.run.selected_action_session = self.session
        self.context = SelectedReleaseActionContext(
            str(self.root), "actual-workflow", "actual-step", "actual-action",
            "actual-workflow", "actual-step", "CA-O-178", "CA-O-169",
            self.run.frozen_parameters_sha256, workflow_version=9,
        )
        self.source = definitions["action"]

    def command(self):
        provenance = self.session.read_recorded_action_start("actual-action")
        registry = b'[[operators]]\nname = "Registered Fixture"\nrole = "maintainer"\njournal_author = "fixture-author"\n'
        (self.root / ".caprmedio_caprmedio/operators_registry.toml").write_bytes(registry)
        payload = canonical_json({
            "schema_version": 1, "operation": "promote_selected_runtime", "command_id": "actual-action",
            "operator": "Registered Fixture", "journal_author": "fixture-author", "operators_registry_sha256": hashlib.sha256(registry).hexdigest(),
            "action_source": {"atom_id": self.source["atom_id"], "version": self.source["version"],
                              "path": self.source["path"], "sha256": self.source["digest"]},
            "target_project_context_sha256": "2" * 64, "package_manifest_sha256": "3" * 64,
            "full_gate_receipt_sha256": "4" * 64, "prior_runtime_selector_sha256": "5" * 64,
            "selected_start_receipt": self.session.read_recorded_action_start_receipt("actual-action"),
            "parent_lineage": list(provenance.parent_lineage),
        })
        receipt = read_selected_installation_command_receipt(payload)
        path = self.root / ".caprmedio_runtime/installation/commands" / f"{receipt.sha256}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        return receipt

    def test_actual_selected_start_and_exact_receipt_accessor_are_read_only(self) -> None:
        carrier = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        before = carrier.read_bytes()
        provenance = admit_selected_native_promotion_start(self.run, self.context)
        receipt = self.session.read_recorded_action_start_receipt("actual-action")
        self.assertEqual(provenance.event_id, receipt["event_id"])
        self.assertEqual(provenance.parent_lineage, ("actual-step", "actual-workflow"))
        self.assertEqual(before, carrier.read_bytes())
        receipt["event_id"] = "caller-tamper"
        self.assertEqual(provenance.event_id, self.session.read_recorded_action_start_receipt("actual-action")["event_id"])

    def test_session_identity_source_and_authorization_cannot_be_replaced(self) -> None:
        self.run.selected_action_session = object()
        with self.assertRaises(ReleaseContractError):
            admit_selected_native_promotion_start(self.run, self.context)
        self.run.selected_action_session = self.session
        self.session.request["operator_authorization"]["parameters_digest"] = "f" * 64
        with self.assertRaises(ReleaseContractError):
            admit_selected_native_promotion_start(self.run, self.context)

    def test_selected_command_is_separate_closed_variant_and_tamper_refuses(self) -> None:
        receipt = self.command()
        self.assertEqual(receipt.parent_lineage, ("actual-step", "actual-workflow"))
        changed = json.loads(receipt.payload)
        changed["unknown"] = True
        with self.assertRaises(SelectedInstallationCommandError):
            read_selected_installation_command_receipt(canonical_json(changed))
        changed = json.loads(receipt.payload)
        changed["action_source"]["atom_id"] = "CA-O-200"
        with self.assertRaises(SelectedInstallationCommandError):
            read_selected_installation_command_receipt(canonical_json(changed))
        with self.assertRaises(SelectedInstallationCommandError):
            read_selected_installation_command_receipt(receipt.payload + b"\n", expected_sha256=receipt.sha256)

    def test_missing_parent_query_configuration_cannot_assert_final_provenance(self) -> None:
        receipt = self.command()
        with self.assertRaises((SelectedInstallationCommandError, ValueError)):
            reopen_selected_installation_command_start(self.root, receipt)

    def query_defaults(self):
        defaults = self.root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        )
        defaults.write_text(
            "[query]\nmax_request_bytes = 4096\nmax_grammar_depth = 20\nmax_filter_tokens = 100\n"
            "max_in_members = 10\nmax_selected_fields = 20\nmax_page_size = 10\n"
            "max_snapshot_members = 20\nmax_file_bytes = 8388608\nmax_total_read_bytes = 33554432\n"
            "timeout_seconds = 5\nmax_findings = 5\n", encoding="utf-8",
        )

    def test_final_reader_reopens_unique_actual_parent_chain_across_canonical_carriers(self) -> None:
        receipt = self.command()
        self.query_defaults()
        event = reopen_selected_installation_command_start(self.root, receipt)
        self.assertEqual("actual-action", event["run"]["run_id"])
        self.assertEqual(receipt.selected_start_receipt["event_id"], event["event_id"])

    def test_duplicate_actual_parent_start_cannot_be_chosen_by_latest_record(self) -> None:
        receipt = self.command()
        self.query_defaults()
        carrier = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        parent = next(json.loads(line) for line in carrier.read_bytes().splitlines()
                      if json.loads(line)["run"]["run_id"] == "actual-step")
        parent["event_id"] += "-duplicate"
        duplicate = work_journal.with_event_digest(parent)
        with carrier.open("ab") as stream:
            stream.write(canonical_json(duplicate) + b"\n")
        with self.assertRaises(SelectedInstallationCommandError):
            reopen_selected_installation_command_start(self.root, receipt)

    def test_changed_registered_attribution_cannot_assert_final_provenance(self) -> None:
        receipt = self.command()
        self.query_defaults()
        registry = self.root / ".caprmedio_caprmedio/operators_registry.toml"
        registry.write_bytes(registry.read_bytes().replace(b"fixture-author", b"another-author"))
        with self.assertRaises(SelectedInstallationCommandError):
            reopen_selected_installation_command_start(self.root, receipt)


if __name__ == "__main__":
    unittest.main()
