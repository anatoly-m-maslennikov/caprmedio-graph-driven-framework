from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
from subject_notation import SubjectNotationError, get_profile, parse_subject  # noqa: E402


class SubjectPatchPreviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.control = self.root / ".caprmedio_caprmedio"
        self.requirements = self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY" / "04_requirement"
        self.requirements.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n",
            encoding="utf-8",
        )
        self.path = self.requirements / "CA-R-501-FRAMEWORK_METHODOLOGY-REQUIREMENT--subject-fixture.md"
        self.path.write_bytes(self._carrier("\n"))
        self.selector = self.path.relative_to(self.root).as_posix()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def _carrier(newline: str) -> bytes:
        return (
            f"---{newline}"
            f"atom_id: CA-R-501{newline}"
            f"content_role: Requirement{newline}"
            f"current_scope_unit: FRAMEWORK_METHODOLOGY{newline}"
            f"local_tier: Standard{newline}"
            f"global_tier: 11{newline}"
            f"author: Test{newline}"
            f"status: Active{newline}"
            f"subjects:{newline}"
            f"  governs: \"Atom/Status\"{newline}"
            f"  depends_on: [Atom, \"Atom/Revision\"]{newline}"
            f"version: 7{newline}"
            f"updated_at: \"2026-10-10 12:00:00 +0400\"{newline}"
            f"unknown_key: [kept, exactly]{newline}"
            f"relations: {{relates_to: [CA-R-500]}}{newline}"
            f"---{newline}"
            f"# Subject fixture{newline}{newline}"
            f"The exact body mentions Atom/Status and must not be changed.{newline}"
        ).encode("utf-8")

    def _payload(self, patches: list[dict[str, object]]) -> list[object]:
        raw = self.path.read_bytes()
        return [{
            "selector": self.selector,
            "expected": {
                "atom_id": "CA-R-501",
                "version": 7,
                "sha256": hashlib.sha256(raw).hexdigest(),
            },
            "subject_patches": patches,
        }]

    def _preview(
        self,
        payload: list[object],
        *,
        timestamp: str = "2026-10-11 10:20:30 +0400",
        subject_profile: object = "legacy",
    ) -> dict[str, object]:
        # Unit fixtures deliberately isolate parser/span behavior.  The test
        # below separately proves that no result is returned if the existing
        # complete-carrier authority declines it.
        with patch.object(operations, "_validate_complete_carrier") as validate:
            result = subject_patch.preview_subject_patches(
                self.root,
                payload,
                timestamp=timestamp,
                subject_profile=subject_profile,
            )
        self.assertEqual(validate.call_count, 2)
        return result

    def _notation_code(self, value: str, subject_profile: object) -> str:
        with self.assertRaises(SubjectNotationError) as context:
            parse_subject(value, subject_profile=subject_profile)
        return context.exception.code

    def test_replaces_exact_subject_spans_and_preserves_crlf_unicode_unknown_and_body(self) -> None:
        self.path.write_bytes(self._carrier("\r\n").replace(b"unknown_key: [kept, exactly]", "unknown_key: [kept, caf\u00e9]".encode("utf-8")))
        before = self.path.read_bytes()
        result = self._preview(self._payload([
            {"field": "governs", "old": "Atom/Status", "new": "Atom/State"},
            {"field": "depends_on", "index": 1, "old": "Atom/Revision", "new": "Atom/Revision/State"},
        ]))
        atom = result["atoms"][0]
        proposed = atom["proposed_carrier"].encode("utf-8")
        self.assertEqual(self.path.read_bytes(), before)
        self.assertIn(b"\r\n", proposed)
        self.assertIn("unknown_key: [kept, caf\u00e9]".encode("utf-8"), proposed)
        self.assertIn(b"The exact body mentions Atom/Status and must not be changed.\r\n", proposed)
        self.assertIn(b'governs: "Atom/State"', proposed)
        self.assertIn(b'depends_on: [Atom, "Atom/Revision/State"]', proposed)
        self.assertIn(b"version: 8", proposed)
        self.assertEqual(atom["before_version"], 7)
        self.assertEqual(atom["after_version"], 8)
        self.assertFalse(atom["noop"])
        self.assertEqual(result["preview_sha256"], self._preview(self._payload([
            {"field": "governs", "old": "Atom/Status", "new": "Atom/State"},
            {"field": "depends_on", "index": 1, "old": "Atom/Revision", "new": "Atom/Revision/State"},
        ]))["preview_sha256"])

    def test_empty_and_unchanged_patches_are_truthful_noops(self) -> None:
        before = self.path.read_bytes()
        for patches in ([], [{"field": "governs", "old": "Atom/Status", "new": "Atom/Status"}]):
            with self.subTest(patches=patches):
                result = self._preview(self._payload(patches))
                atom = result["atoms"][0]
                self.assertTrue(atom["noop"])
                self.assertEqual(atom["proposed_carrier"].encode("utf-8"), before)
                self.assertEqual(atom["before_sha256"], atom["after_sha256"])
                self.assertEqual(atom["before_version"], atom["after_version"])
                self.assertIsNone(atom["illustrative_updated_at"])

    def test_selected_profile_evidence_is_sealed_for_noops(self) -> None:
        legacy = self._preview(self._payload([]))
        approved = self._preview(self._payload([]), subject_profile="approved")
        for profile, preview in (("legacy", legacy), ("approved", approved)):
            self.assertEqual(preview["subject_profile"], profile)
            evidence = preview["subject_profile_evidence"]
            self.assertEqual(set(evidence), {"grammar_pins", "native_admission"})
            self.assertEqual(evidence["native_admission"], "not_performed")
            self.assertEqual(len(evidence["grammar_pins"]), 5)
            for grammar_pin in evidence["grammar_pins"]:
                self.assertEqual(set(grammar_pin), {"atom_id", "version", "path", "sha256"})
        self.assertNotEqual(legacy["preview_sha256"], approved["preview_sha256"])
        self.assertEqual(legacy["preview_sha256"], self._preview(self._payload([]))["preview_sha256"])

    def test_selected_profile_rejects_invalid_source_and_proposed_subjects(self) -> None:
        self.path.write_bytes(self.path.read_bytes().replace(b'governs: "Atom/Status"', b'governs: "Atom@Status"'))
        with patch.object(operations, "_validate_complete_carrier") as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, self._payload([]), subject_profile="legacy")
        self.assertEqual(context.exception.code, self._notation_code("Atom@Status", "legacy"))
        validate.assert_not_called()

        self.path.write_bytes(self._carrier("\n"))
        payload = self._payload([{"field": "governs", "old": "Atom/Status", "new": "Atom@Status"}])
        with patch.object(operations, "_validate_complete_carrier") as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, payload, subject_profile="approved")
        self.assertEqual(context.exception.code, self._notation_code("Atom@Status", "approved"))
        validate.assert_not_called()

    def test_unknown_or_malformed_profile_fails_before_source_validation(self) -> None:
        for supplied in ("unknown", None):
            with self.subTest(supplied=supplied), self.assertRaises(SubjectNotationError) as expected:
                get_profile(supplied)
            with patch.object(operations, "_validate_complete_carrier") as validate:
                with self.assertRaises(operations.ToolError) as context:
                    subject_patch.preview_subject_patches(self.root, self._payload([]), subject_profile=supplied)
            self.assertEqual(context.exception.code, expected.exception.code)
            validate.assert_not_called()

    def test_default_preview_time_uses_the_configured_project_timezone(self) -> None:
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n\n"
            "[artifact_timestamps]\ntimezone = \"UTC\"\n",
            encoding="utf-8",
        )
        with patch.object(operations, "_validate_complete_carrier") as validate:
            result = subject_patch.preview_subject_patches(
                self.root,
                self._payload([{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}]),
            )
        self.assertEqual(validate.call_count, 2)
        self.assertRegex(result["illustrative_updated_at"], r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+0000$")

    def test_stale_pin_repeated_occurrence_and_duplicate_resulting_dependencies_stop_before_authority(self) -> None:
        stale = self._payload([])
        stale[0]["expected"]["sha256"] = "0" * 64
        repeated = self._payload([
            {"field": "governs", "old": "Atom/Status", "new": "Atom/State"},
            {"field": "governs", "old": "Atom/Status", "new": "Atom/State/Again"},
        ])
        duplicates = self._payload([
            {"field": "depends_on", "index": 1, "old": "Atom/Revision", "new": "Atom"},
        ])
        for payload, code in ((stale, "subject-pin-stale"), (repeated, "subject-occurrence-duplicate"), (duplicates, "subject-dependency-duplicate")):
            with self.subTest(code=code), patch.object(operations, "_validate_complete_carrier") as validate:
                with self.assertRaises(operations.ToolError) as context:
                    subject_patch.preview_subject_patches(self.root, payload, timestamp="2026-10-11 10:20:30 +0400")
                self.assertEqual(context.exception.code, code)
                validate.assert_not_called()

    def test_rejects_escaping_projection_and_symlink_paths(self) -> None:
        cases = [
            ("../outside.md", "subject-selector-invalid"),
            (str(self.path), "subject-selector-invalid"),
        ]
        projection = self.control / "_projection" / "101_LAYER_1_FRAMEWORK_METHODOLOGY" / "04_requirement" / self.path.name
        projection.parent.mkdir(parents=True)
        projection.write_bytes(self.path.read_bytes())
        cases.append((projection.relative_to(self.root).as_posix(), "subject-selector-projection"))
        linked = self.requirements / "CA-R-502-FRAMEWORK_METHODOLOGY-REQUIREMENT--linked.md"
        linked.symlink_to(self.path)
        cases.append((linked.relative_to(self.root).as_posix(), "subject-selector-symlink"))
        for selector, code in cases:
            with self.subTest(selector=selector):
                payload = self._payload([])
                payload[0]["selector"] = selector
                with self.assertRaises(operations.ToolError) as context:
                    subject_patch.preview_subject_patches(self.root, payload, timestamp="2026-10-11 10:20:30 +0400")
                self.assertEqual(context.exception.code, code)

    def test_complete_carrier_authority_is_called_and_stops_result(self) -> None:
        payload = self._payload([{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}])
        with patch.object(operations, "_validate_complete_carrier", side_effect=operations.ToolError("complete-carrier-invalid", "no")) as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, payload, timestamp="2026-10-11 10:20:30 +0400")
        self.assertEqual(context.exception.code, "complete-carrier-invalid")
        validate.assert_called_once()

    def test_refuses_invalid_source_metadata_instead_of_repairing_it(self) -> None:
        original = self.path.read_bytes()
        for before, after, code in (
            (b"version: 7", b"version: 0", "atom-version-invalid"),
            (b"status: Active", b"status: Draft", "atom-not-active"),
        ):
            with self.subTest(code=code):
                self.path.write_bytes(original.replace(before, after))
                with patch.object(operations, "_validate_complete_carrier") as validate:
                    with self.assertRaises(operations.ToolError) as context:
                        subject_patch.preview_subject_patches(self.root, self._payload([]), timestamp="2026-10-11 10:20:30 +0400")
                self.assertEqual(context.exception.code, code)
                validate.assert_not_called()
        self.path.write_bytes(original)
        missing_id_filename = self.requirements / "subject-fixture.md"
        self.path.replace(missing_id_filename)
        self.path = missing_id_filename
        self.selector = self.path.relative_to(self.root).as_posix()
        with patch.object(operations, "_validate_complete_carrier") as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, self._payload([]), timestamp="2026-10-11 10:20:30 +0400")
        self.assertEqual(context.exception.code, "atom-frontmatter-id-mismatch")
        validate.assert_not_called()

    def test_rejects_inode_swap_after_the_pinned_snapshot(self) -> None:
        payload = self._payload([{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}])
        replacement = self.requirements / "replacement.md"
        replacement.write_bytes(self._carrier("\n").replace(b"Atom/Status", b"Atom/Changed"))
        calls = 0

        def swap_source(*_args: object, **_kwargs: object) -> None:
            nonlocal calls
            calls += 1
            if calls == 1:
                replacement.replace(self.path)

        with patch.object(operations, "_validate_complete_carrier", side_effect=swap_source) as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, payload, timestamp="2026-10-11 10:20:30 +0400")
        self.assertEqual(context.exception.code, "subject-source-changed")
        self.assertEqual(validate.call_count, 2)

    def test_rejects_changed_same_path_snapshot_before_returning_preview(self) -> None:
        payload = self._payload([{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}])

        def rewrite_source(*_args: object, **_kwargs: object) -> None:
            self.path.write_bytes(self.path.read_bytes() + b"\n")

        with patch.object(operations, "_validate_complete_carrier", side_effect=rewrite_source) as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, payload, timestamp="2026-10-11 10:20:30 +0400")
        self.assertEqual(context.exception.code, "subject-source-changed")
        self.assertEqual(validate.call_count, 2)

    def test_rejects_symlink_swap_after_the_pinned_snapshot(self) -> None:
        payload = self._payload([{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}])
        replacement = self.requirements / "replacement.md"
        replacement.write_bytes(self._carrier("\n"))

        def swap_to_symlink(*_args: object, **_kwargs: object) -> None:
            self.path.unlink()
            self.path.symlink_to(replacement)

        with patch.object(operations, "_validate_complete_carrier", side_effect=swap_to_symlink) as validate:
            with self.assertRaises(operations.ToolError) as context:
                subject_patch.preview_subject_patches(self.root, payload, timestamp="2026-10-11 10:20:30 +0400")
        self.assertEqual(context.exception.code, "subject-selector-symlink")
        self.assertEqual(validate.call_count, 2)


if __name__ == "__main__":
    unittest.main()
