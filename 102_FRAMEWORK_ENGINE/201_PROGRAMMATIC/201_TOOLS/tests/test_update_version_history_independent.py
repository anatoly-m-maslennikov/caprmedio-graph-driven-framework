"""Independent same-ID Update checks using the existing real authority fixture."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_selected_atom_lifecycle as fixtures  # noqa: E402
import lifecycle_intents  # noqa: E402
from atom_operations import ToolError, split_frontmatter  # noqa: E402
from connector_property_carrier import prepare_property_carrier  # noqa: E402
from connector_section_parse import edit_section  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (  # noqa: E402
    source_context_from_project, validate_proposed_carrier,
)
from lifecycle_intents import LifecycleError, carrier_descriptor, update_atom_action  # noqa: E402


class UpdateVersionHistoryIndependentTests(unittest.TestCase):
    def fixture(self):
        fixture = fixtures.SelectedAtomLifecycleTest(methodName="runTest")
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        return fixture

    @staticmethod
    def parameters(fixture, change_class):
        proposal = fixture._proposal(fixture.target, summary="Stable summary")
        proposal["content"] += "\n" if change_class == "carrier_only" else "\nClarified acceptance detail.\n"
        parameters = {"target": carrier_descriptor(fixture.root, "CA-R-100"),
                      "proposed": proposal, "change_class": change_class}
        if change_class != "carrier_only":
            parameters["semantic_assessment_report"] = fixture._semantic_assessment_report(
                proposal, change_class=change_class)
        return parameters

    def assert_applied(self, fixture, parameters):
        before = fixture.target.read_bytes()
        def snapshot():
            return {path.relative_to(fixture.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                    for path in fixture.root.rglob("*") if path.is_file()}
        original_files = snapshot()
        prior = parameters["target"]
        start = datetime.now(timezone.utc).replace(microsecond=0)
        result = update_atom_action(fixture.root, parameters, execute=True, authorized=True)
        stop = datetime.now(timezone.utc).replace(microsecond=0)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(prior["version"] + 1, result["observed"]["version"])
        self.assertEqual(prior["atom_id"], result["observed"]["atom_id"])
        self.assertEqual(prior["status"], result["observed"]["status"])
        self.assertNotEqual(prior["updated_at"], result["observed"]["updated_at"])
        stamp = datetime.strptime(result["observed"]["updated_at"], "%Y-%m-%d %H:%M:%S %z")
        self.assertLessEqual(start, stamp)
        self.assertLessEqual(stamp, stop)
        history = result["history"]["prior_revision"]
        self.assertEqual(before, (fixture.root / history["path"]).read_bytes())
        self.assertEqual(hashlib.sha256(before).hexdigest(), history["digest"])
        for field in ("version", "status", "updated_at", "atom_id"):
            self.assertEqual(prior[field], history[field])
        self.assertEqual({result["observed"]["path"]},
                         {effect["carrier"]["path"] for effect in result["effects"] if effect["state"] == "changed"})
        self.assertNotEqual(before, fixture.target.read_bytes())
        observed_files = snapshot()
        self.assertEqual({history["path"]}, set(observed_files) - set(original_files))
        self.assertEqual(set(original_files), set(observed_files) - {history["path"]})
        for path, original in original_files.items():
            if path != prior["path"]:
                self.assertEqual(original, observed_files[path], f"Unrelated fixture changed: {path}")
        return result

    def test_each_admitted_actual_change_increments_once_and_preserves_exact_history(self):
        for change_class in ("carrier_only", "equivalent_refinement", "semantic_revision"):
            with self.subTest(change_class=change_class):
                fixture = self.fixture()
                self.assert_applied(fixture, self.parameters(fixture, change_class))

    def test_exact_noop_preserves_bytes_version_timestamp_and_creates_no_history(self):
        fixture = self.fixture()
        before = fixture.target.read_bytes()
        prior = carrier_descriptor(fixture.root, "CA-R-100")
        for change_class in ("carrier_only", "equivalent_refinement", "semantic_revision"):
            with self.subTest(change_class=change_class):
                result = update_atom_action(fixture.root, {
                    "target": prior, "proposed": fixture._proposal(fixture.target, summary="Stable summary"),
                    "change_class": change_class}, execute=True, authorized=True)
                self.assertEqual("no-op", result["outcome"])
                self.assertEqual(prior, result["observed"])
                self.assertEqual(before, fixture.target.read_bytes())
                self.assertEqual({"unchanged"}, {effect["state"] for effect in result["effects"]})
                self.assertNotIn("prior_revision", result["history"])
                self.assertFalse((fixture.requirements / "archive").exists())

    def test_crlf_predecessor_bytes_are_not_reconstructed_from_parsed_fields(self):
        for change_class in ("carrier_only", "equivalent_refinement"):
            with self.subTest(change_class=change_class):
                fixture = self.fixture()
                before = fixture.target.read_bytes().replace(b"\n", b"\r\n")
                fixture.target.write_bytes(before)
                self.assertIn(b"\r\n", before)
                result = self.assert_applied(fixture, self.parameters(fixture, change_class))
                self.assertEqual(before, (fixture.root / result["history"]["prior_revision"]["path"]).read_bytes())

    def test_unsupported_bom_is_refused_without_inventing_identity_or_history(self):
        fixture = self.fixture()
        parameters = self.parameters(fixture, "carrier_only")
        before = b"\xef\xbb\xbf" + fixture.target.read_bytes()
        fixture.target.write_bytes(before)
        with self.assertRaises((LifecycleError, ToolError)):
            update_atom_action(fixture.root, parameters, execute=True, authorized=True)
        self.assertEqual(before, fixture.target.read_bytes())
        self.assertFalse((fixture.requirements / "archive").exists())

    def test_unproven_refinement_remains_unresolved_without_revision_or_history(self):
        fixture = self.fixture()
        parameters = self.parameters(fixture, "equivalent_refinement")
        del parameters["semantic_assessment_report"]
        before = fixture.target.read_bytes()
        result = update_atom_action(fixture.root, parameters, execute=True, authorized=True)
        self.assertEqual("unresolved", result["outcome"])
        self.assertEqual("semantic-assessment-unverified", result["classification"]["reason"])
        self.assertEqual(before, fixture.target.read_bytes())
        self.assertEqual({"unchanged"}, {effect["state"] for effect in result["effects"]})
        self.assertFalse((fixture.requirements / "archive").exists())

    def test_real_property_and_section_proposals_use_the_same_version_history_boundary(self):
        for kind in ("Property", "Section"):
            with self.subTest(kind=kind):
                fixture = self.fixture()
                context = source_context_from_project(fixture.root)
                relative = fixture.target.relative_to(context._selection.control_root)
                raw = fixture.target.read_bytes()

                def validate(metadata, body):
                    validate_proposed_carrier(metadata, body, context, relative)

                if kind == "Property":
                    prepared = prepare_property_carrier(
                        raw, [{"field": "Dependencies", "operation": "add", "value": "Atom"}],
                        expected_sha256=hashlib.sha256(raw).hexdigest(),
                        field_paths={"Dependencies": ("subjects", "depends_on")},
                        list_fields={"Dependencies"}, list_entry_edit=lambda _edit: True,
                        validate_final=validate)
                    change_class = "semantic_revision"
                else:
                    prepared = edit_section(raw, {"operation": "replace", "section": {"level": 2, "title": "Details"},
                                                  "content": "\nFixture details clarified.\n"})
                    parsed = parse_carrier(prepared, fixture.target)
                    validate(parsed.metadata, parsed.body)
                    change_class = "equivalent_refinement"
                self.assertEqual(raw, fixture.target.read_bytes(), "Preparation must not publish")
                frontmatter, content = split_frontmatter(prepared.decode())
                proposal = {"frontmatter": frontmatter, "content": content}
                parameters = {"target": carrier_descriptor(fixture.root, "CA-R-100"),
                              "proposed": proposal, "change_class": change_class,
                              "semantic_assessment_report": fixture._semantic_assessment_report(
                                  proposal, change_class=change_class)}
                self.assert_applied(fixture, parameters)

    def test_denied_preview_stale_target_and_stale_assessment_do_not_publish(self):
        fixture = self.fixture()
        parameters = self.parameters(fixture, "equivalent_refinement")
        before = fixture.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "authorization-required"):
            update_atom_action(fixture.root, parameters, execute=True, authorized=False)
        preview = update_atom_action(fixture.root, parameters, execute=False)
        self.assertEqual("preview", preview["outcome"])
        stale_target = {**parameters, "target": {**parameters["target"], "digest": "0" * 64}}
        with self.assertRaisesRegex(LifecycleError, "stale-carrier"):
            update_atom_action(fixture.root, stale_target, execute=True, authorized=True)
        report = fixture.root / parameters["semantic_assessment_report"]["path"]
        report.write_bytes(report.read_bytes() + b"\nStale report bytes.\n")
        stale = update_atom_action(fixture.root, parameters, execute=True, authorized=True)
        self.assertEqual("unresolved", stale["outcome"])
        self.assertEqual(before, fixture.target.read_bytes())
        self.assertFalse((fixture.requirements / "archive").exists())

    def test_caught_postpublication_error_restores_current_and_removes_only_new_history(self):
        for change_class in ("carrier_only", "equivalent_refinement"):
            with self.subTest(change_class=change_class):
                fixture = self.fixture()
                parameters = self.parameters(fixture, change_class)
                before = fixture.target.read_bytes()
                fixture.target.chmod(0o640)
                unrelated = fixture._unrelated_history()
                unrelated_before = unrelated.read_bytes()
                real_write = lifecycle_intents.write_atom_revision

                def publish_then_fail(*args):
                    real_write(*args)
                    raise OSError("independent publication failure")

                with patch("lifecycle_intents.write_atom_revision", side_effect=publish_then_fail):
                    with self.assertRaisesRegex(OSError, "independent publication failure"):
                        update_atom_action(fixture.root, parameters, execute=True, authorized=True)
                self.assertEqual(before, fixture.target.read_bytes())
                self.assertEqual(0o640, fixture.target.stat().st_mode & 0o777)
                self.assertEqual(unrelated_before, unrelated.read_bytes())
                self.assertFalse((unrelated.parent / (fixture.target.stem + "@1.md")).exists())

    def test_failed_history_cleanup_retains_truthful_recoverable_history_effect(self):
        for change_class in ("carrier_only", "equivalent_refinement"):
            with self.subTest(change_class=change_class):
                fixture = self.fixture()
                parameters = self.parameters(fixture, change_class)
                before = fixture.target.read_bytes()
                history = fixture.requirements / "archive" / (fixture.target.stem + "@1.md")
                real_write, real_unlink = lifecycle_intents.write_atom_revision, Path.unlink

                def publish_then_fail(*args):
                    real_write(*args)
                    raise OSError("independent publication failure")

                def deny_history_cleanup(path, *args, **kwargs):
                    if path == history:
                        raise PermissionError("independent cleanup failure")
                    return real_unlink(path, *args, **kwargs)

                with (patch("lifecycle_intents.write_atom_revision", side_effect=publish_then_fail),
                      patch.object(Path, "unlink", autospec=True, side_effect=deny_history_cleanup)):
                    result = update_atom_action(fixture.root, parameters, execute=True, authorized=True)
                self.assertEqual("partial", result["outcome"])
                self.assertEqual("update-rollback-uncertain", result["failure"]["code"])
                self.assertEqual("remove-new-history", result["failure"]["recovery"]["phase"])
                self.assertEqual(before, fixture.target.read_bytes())
                self.assertEqual(before, history.read_bytes())
                self.assertFalse(result["recovery"]["automatic_retry"])
                self.assertEqual({history.relative_to(fixture.root).as_posix()},
                                 {effect["carrier"]["path"] for effect in result["effects"] if effect["state"] == "changed"})
                self.assertEqual({fixture.target.relative_to(fixture.root).as_posix()},
                                 {effect["carrier"]["path"] for effect in result["effects"] if effect["state"] == "unknown"})


if __name__ == "__main__":
    unittest.main()
