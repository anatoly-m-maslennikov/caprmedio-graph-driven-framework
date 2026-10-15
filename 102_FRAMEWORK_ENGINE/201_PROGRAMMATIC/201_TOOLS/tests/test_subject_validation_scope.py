"""Invocation-local validation reuse keeps all carrier and authority checks."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "ATOM_UPDATE/tests"))

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subjects  # noqa: E402
import atom_subject_stage as staging  # noqa: E402
import test_nonarchived_subject_preview as fixtures  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission  # noqa: E402

STAMP = "2026-10-12 10:20:30 +0400"


class SubjectValidationScopeTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan("Done", number=7801)
        self.items = self.fixture._payload(self.path)
        self.status = next(self.root.rglob("CA-R-1539-*.md"))

    def preview(self, **kwargs):
        return subjects.preview_subject_patches(self.root, self.items, timestamp=STAMP, **kwargs)

    def test_one_context_and_index_per_invocation_but_every_carrier_is_validated(self):
        other = self.fixture._plan("Active", number=7802)
        self.items += self.fixture._payload(other)
        expected = self.preview()
        with (
            patch.object(
                admission,
                "source_context_from_project",
                wraps=admission.source_context_from_project,
            ) as context,
            patch.object(
                admission, "capture_status_models", wraps=admission.capture_status_models
            ) as index,
            patch.object(
                admission, "validate_proposed_carrier", wraps=admission.validate_proposed_carrier
            ) as validate,
        ):
            self.assertEqual(expected, self.preview())
            self.assertEqual((1, 1, 4), (context.call_count, index.call_count, validate.call_count))
            first = validate.call_args_list[0].args[2]
            result = staging.stage_subject_preview(self.root, self.items, timestamp=STAMP)
            self.assertEqual(expected, result["preview"])
            self.assertEqual(
                (2, 2, 14), (context.call_count, index.call_count, validate.call_count)
            )
            self.assertIsNot(first, validate.call_args_list[-1].args[2])
            self.assertEqual(1, len({id(call.args[2]) for call in validate.call_args_list[4:]}))
            self.assertEqual(
                1, len({id(call.kwargs["_status_index"]) for call in validate.call_args_list[4:]})
            )

    def test_next_request_does_not_reuse_status_declarations(self):
        self.preview()
        duplicate = self.status.with_name("CA-R-999999--competing-status.md")
        duplicate.write_bytes(self.status.read_bytes().replace(b"CA-R-1539", b"CA-R-999999"))
        with self.assertRaises(operations.ToolError):
            self.preview()

    def test_final_status_frontier_checks_changed_added_deleted_and_symlink_sources(self):
        original = self.status.read_bytes()
        unrelated = self.status.with_name("unrelated.md")
        for change in ("changed", "added", "deleted", "symlink", "new-declaration"):
            with self.subTest(change=change):
                unrelated.write_bytes(b"# unrelated source\n")
                real = subjects._materialize_item

                def mutate(*args, **kwargs):
                    result = real(*args, **kwargs)
                    if change == "changed":
                        self.status.write_bytes(original + b"\n")
                    elif change == "deleted":
                        self.status.unlink()
                    elif change == "symlink":
                        self.status.unlink()
                        self.status.symlink_to(unrelated)
                    elif change == "new-declaration":
                        unrelated.write_bytes(original)
                    else:
                        self.status.with_name("added.md").write_bytes(b"# added\n")
                    return result

                try:
                    with patch.object(subjects, "_materialize_item", side_effect=mutate):
                        with self.assertRaises(operations.ToolError):
                            self.preview()
                finally:
                    if self.status.is_symlink():
                        self.status.unlink()
                    self.status.write_bytes(original)
                    self.status.with_name("added.md").unlink(missing_ok=True)
                    unrelated.unlink(missing_ok=True)

    def test_final_finite_authority_settings_structure_and_operators_are_rechecked(self):
        for key in ("authority", "settings", "structure", "operators"):
            changed = []
            real = subjects._materialize_item

            def mutate(*args, **kwargs):
                result = real(*args, **kwargs)
                context = kwargs["validation_scope"]._context
                paths = {
                    "authority": Path(context.inputs["sources"][0]["binding"]["path"]),
                    "settings": context._selection.settings_path,
                    "structure": context._selection.structure_path,
                    "operators": context._selection.control_root / "operators_registry.toml",
                }
                path = paths[key]
                changed.append((path, path.read_bytes()))
                path.write_bytes(changed[-1][1] + b"\n")
                return result

            try:
                with (
                    self.subTest(key=key),
                    patch.object(subjects, "_materialize_item", side_effect=mutate),
                ):
                    with self.assertRaises(operations.ToolError):
                        self.preview()
            finally:
                for path, raw in changed:
                    path.write_bytes(raw)

    def test_late_stage_authority_drift_reports_retained_artifacts(self):
        real = staging._write_candidate
        original = self.status.read_bytes()

        def mutate(root, path, raw):
            result = real(root, path, raw)
            if path.name == "manifest.json":
                self.status.write_bytes(original + b"\n")
            return result

        with patch.object(staging, "_write_candidate", side_effect=mutate):
            with self.assertRaises(operations.ToolError) as raised:
                staging.stage_subject_preview(self.root, self.items, timestamp=STAMP)
        self.assertTrue(raised.exception.details["staging_only"])
        self.assertTrue(raised.exception.details["retained_artifacts"])
        self.assertEqual(
            self.items[0]["expected"]["sha256"],
            subjects.hashlib.sha256(self.path.read_bytes()).hexdigest(),
        )

    def test_explicit_scope_from_another_project_refuses_before_validation(self):
        scope = admission.CarrierValidationScope(self.root)
        with self.assertRaises(admission.ProposedCarrierError):
            scope.validate(
                self.root.parent, {}, "", Path("target.md"), allow_existing_relations=True
            )

    def test_invalid_original_and_proposed_carriers_still_fail_complete_validation(self):
        original = self.path.read_bytes()
        self.path.write_bytes(original.replace(b"author: Anatoly Maslennikov", b"author: Unknown"))
        self.items = self.fixture._payload(self.path)
        with self.assertRaises(operations.ToolError) as raised:
            self.preview()
        self.assertEqual("complete-carrier-invalid", raised.exception.code)
        self.path.write_bytes(original)
        self.items = self.fixture._payload(self.path)
        real = subjects._apply_replacements

        def invalid_proposal(frontmatter, replacements):
            return real(frontmatter, replacements).replace(
                "author: Anatoly Maslennikov", "author: Unknown"
            )

        with patch.object(subjects, "_apply_replacements", side_effect=invalid_proposal):
            with self.assertRaises(operations.ToolError) as raised:
                self.preview()
        self.assertEqual("complete-carrier-invalid", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
