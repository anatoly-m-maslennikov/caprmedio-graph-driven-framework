"""Golden source-admission checks for D613's additive public.release record."""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
PUBLIC_RELEASE = TOOLS / "PUBLIC_RELEASE"
REPOSITORY = TOOLS.parents[2]
for item in (str(TOOLS), str(PUBLIC_RELEASE)):
    if item not in sys.path:
        sys.path.insert(0, item)

import selected_admission  # noqa: E402
from selected_admission import (  # noqa: E402
    AUTHORITY_PIN,
    AUTHORITY_REF,
    PublicReleaseSourceAdmissionError,
    derive_public_release_source_admission,
    validate_public_release_source_admission,
)


class SelectedPublicReleaseAdmissionTests(unittest.TestCase):
    """Only a copied, fixture-local CA-P-1869 may be made Done here."""

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.temp.name).resolve()
        self.authority = self.root / AUTHORITY_REF
        authority_source = REPOSITORY / AUTHORITY_REF
        self.authority_text = authority_source.read_text(encoding="utf-8")
        sources = set(re.findall(r"`(\.caprmedio_caprmedio/[^`]+\.md)`", self.authority_text))
        self.assertEqual(46, len(sources))
        for relative in sources | {AUTHORITY_REF}:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, destination)
        self.acceptance_path = self.root / next(path for path in sources if "CA-P-1869-" in path)
        self.projection = REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        self.projection_before = self.projection.read_bytes()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def snapshot(self) -> dict[str, bytes]:
        return {str(path.relative_to(self.root)): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}

    def make_fixture_acceptance_done(self) -> None:
        raw = self.acceptance_path.read_text(encoding="utf-8")
        self.assertEqual(1, len(re.findall(r"(?m)^status:\s*Active$", raw)))
        done = re.sub(r"(?m)^status:\s*Active$", "status: Done", raw, count=1)
        self.acceptance_path.write_text(done, encoding="utf-8")
        old_digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        new_digest = hashlib.sha256(done.encode("utf-8")).hexdigest()
        authority = self.authority.read_text(encoding="utf-8")
        self.assertEqual(1, authority.count(old_digest))
        self.authority.write_text(authority.replace(old_digest, new_digest, 1), encoding="utf-8")

    @contextmanager
    def trusted_fixture_authority(self):
        pin = {**AUTHORITY_PIN, "digest": hashlib.sha256(self.authority.read_bytes()).hexdigest()}
        with patch.object(selected_admission, "AUTHORITY_PIN", pin):
            yield

    def derive_done_record(self) -> dict[str, object]:
        self.make_fixture_acceptance_done()
        with self.trusted_fixture_authority():
            return derive_public_release_source_admission(self.root)

    def authority_mutation_refuses(self, mutate) -> None:
        self.make_fixture_acceptance_done()
        mutate()
        with self.trusted_fixture_authority():
            with self.assertRaises(PublicReleaseSourceAdmissionError):
                derive_public_release_source_admission(self.root)

    def test_actual_active_acceptance_refuses_and_never_changes_projection(self) -> None:
        with self.assertRaisesRegex(PublicReleaseSourceAdmissionError, "actually Done"):
            derive_public_release_source_admission(REPOSITORY)
        self.assertEqual(self.projection_before, self.projection.read_bytes())
        self.assertEqual(16, len(json.loads(self.projection_before)["routes"]))

    def test_done_fixture_derives_and_validates_one_closed_46_pin_record(self) -> None:
        self.make_fixture_acceptance_done()
        before = self.snapshot()
        with self.trusted_fixture_authority():
            record = derive_public_release_source_admission(self.root)
        with self.trusted_fixture_authority():
            validated = validate_public_release_source_admission(self.root, record)
        self.assertEqual(record, validated)
        self.assertEqual({
            "route", "acceptance_frontier", "workflow", "ordered_steps", "ordered_actions",
            "rmed_frontier", "mutation_capable", "native_action_calls",
        }, set(record))
        self.assertEqual("public.release", record["route"])
        self.assertEqual(5, len(record["ordered_steps"]))
        self.assertEqual(5, len(record["ordered_actions"]))
        self.assertEqual(34, sum(len(rows) for rows in record["rmed_frontier"].values()))
        self.assertEqual(46, 2 + len(record["ordered_steps"]) + len(record["ordered_actions"])
                         + sum(len(rows) for rows in record["rmed_frontier"].values()))
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.projection_before, self.projection.read_bytes())
        self.assertEqual(16, len(json.loads(self.projection_before)["routes"]))

    def test_stale_observed_source_refuses_even_after_fixture_acceptance_is_done(self) -> None:
        self.make_fixture_acceptance_done()
        workflow = self.root / (
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/"
            "CA-O-188-PROJECT_CONFIGURATION-WORKFLOW--release-a-selected-public-version.md"
        )
        workflow.write_bytes(workflow.read_bytes() + b"\nfixture stale source\n")
        with self.trusted_fixture_authority():
            with self.assertRaisesRegex(PublicReleaseSourceAdmissionError, "pin is stale"):
                derive_public_release_source_admission(self.root)

    def test_ambiguous_reordered_and_incomplete_authority_rows_refuse(self) -> None:
        def ambiguous() -> None:
            text = self.authority.read_text(encoding="utf-8")
            first = next(line for line in text.splitlines() if line.startswith("| 1 | CA-O-189 |"))
            second = next(line for line in text.splitlines() if line.startswith("| 2 | CA-O-191 |"))
            self.authority.write_text(text.replace(second, first.replace("| 1 |", "| 2 |", 1), 1), encoding="utf-8")

        def reordered() -> None:
            text = self.authority.read_text(encoding="utf-8")
            first = next(line for line in text.splitlines() if line.startswith("| 1 | CA-O-189 |"))
            second = next(line for line in text.splitlines() if line.startswith("| 2 | CA-O-191 |"))
            marker = "__SECOND_ROW__"
            text = text.replace(first, marker, 1).replace(second, first, 1).replace(marker, second, 1)
            self.authority.write_text(text, encoding="utf-8")

        def incomplete() -> None:
            text = self.authority.read_text(encoding="utf-8")
            row = next(line for line in text.splitlines() if line.startswith("| 5 | CA-O-197 |")) + "\n"
            self.authority.write_text(text.replace(row, "", 1), encoding="utf-8")

        for mutation in (ambiguous, reordered, incomplete):
            with self.subTest(mutation=mutation.__name__):
                self.authority_mutation_refuses(mutation)
                self.authority.write_text(self.authority_text, encoding="utf-8")
                raw = self.acceptance_path.read_text(encoding="utf-8")
                self.acceptance_path.write_text(
                    re.sub(r"(?m)^status:\s*Done$", "status: Active", raw, count=1), encoding="utf-8"
                )

    def test_rmed_blocks_cannot_be_reordered_missing_or_extra(self) -> None:
        def block_reordered() -> None:
            text = self.authority.read_text(encoding="utf-8")
            requirement = next(line for line in text.splitlines() if line.startswith("| requirements | 1 |"))
            method = next(line for line in text.splitlines() if line.startswith("| methods | 1 |"))
            marker = "__FIRST_METHOD_ROW__"
            text = text.replace(requirement, marker, 1).replace(method, requirement, 1).replace(marker, method, 1)
            self.authority.write_text(text, encoding="utf-8")

        def missing() -> None:
            text = self.authority.read_text(encoding="utf-8")
            row = next(line for line in text.splitlines() if line.startswith("| deliveries | 9 |")) + "\n"
            self.authority.write_text(text.replace(row, "", 1), encoding="utf-8")

        def extra() -> None:
            text = self.authority.read_text(encoding="utf-8")
            row = next(line for line in text.splitlines() if line.startswith("| requirements | 1 |"))
            self.authority.write_text(text.replace(row, row + "\n" + row, 1), encoding="utf-8")

        for mutation in (block_reordered, missing, extra):
            with self.subTest(mutation=mutation.__name__):
                self.authority_mutation_refuses(mutation)
                self.authority.write_text(self.authority_text, encoding="utf-8")
                raw = self.acceptance_path.read_text(encoding="utf-8")
                self.acceptance_path.write_text(
                    re.sub(r"(?m)^status:\s*Done$", "status: Active", raw, count=1), encoding="utf-8"
                )

    def test_self_shadow_and_caller_pass_fields_refuse(self) -> None:
        record = self.derive_done_record()
        for field, value in (
            ("canonical_manifest_sha256", "f" * 64),
            ("caller_pass", True),
            ("authority_pin", copy.deepcopy(AUTHORITY_PIN)),
        ):
            with self.subTest(field=field), self.trusted_fixture_authority():
                forged = copy.deepcopy(record)
                forged[field] = value
                with self.assertRaises(PublicReleaseSourceAdmissionError):
                    validate_public_release_source_admission(self.root, forged)


if __name__ == "__main__":
    unittest.main()
