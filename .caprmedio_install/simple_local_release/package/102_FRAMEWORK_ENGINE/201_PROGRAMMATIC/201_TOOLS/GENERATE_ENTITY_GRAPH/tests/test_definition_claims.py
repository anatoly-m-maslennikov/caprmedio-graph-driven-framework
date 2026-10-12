"""Focused tests for current-Core definition claim recognition."""

from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import sys
import unittest
from dataclasses import dataclass, replace
from pathlib import Path


MODULE = Path(__file__).resolve().parents[1] / "definition_claims.py"
SPEC = importlib.util.spec_from_file_location("definition_claims", MODULE)
assert SPEC is not None and SPEC.loader is not None
definition_claims = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = definition_claims
SPEC.loader.exec_module(definition_claims)


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class Carrier:
    body: str
    content_role: str
    status: str = "Active"
    frontmatter: str = ""

    def evidence(self) -> dict[str, object]:
        return {
            "atom_id": "CA-R-TEST",
            "atom_revision": 7,
            "carrier_path": "core/test.md",
            "carrier_sha256": "a" * 64,
        }


@dataclass(frozen=True)
class Relation:
    kind: str
    subject_path: str

    def evidence(self) -> dict[str, object]:
        return {
            "atom_id": "CA-R-TEST",
            "atom_revision": 7,
            "carrier_path": "core/test.md",
            "carrier_sha256": "a" * 64,
            "kind": self.kind,
            "subject_path": self.subject_path,
        }


@dataclass(frozen=True)
class RawCarrier:
    atom_id: str
    version: int
    carrier_path: str
    sha256: str
    frontmatter: str
    body: str
    content_role: str = "Requirement"
    status: str = "Active"

    def evidence(self) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.version,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.sha256,
        }


def sections(primary: str, *, claim_name: str = "Claim") -> str:
    return (
        "# Summary\n\nIgnored **means** text.\n\n"
        "## Scope\n\nIgnored **means** text.\n\n"
        f"## {claim_name}\n\n{primary}\n\n"
        "## Details\n\nIgnored **means** text.\n"
    )


class DefinitionClaimTests(unittest.TestCase):
    def assess(
        self,
        primary: str,
        target: str,
        *,
        role: str = "Requirement",
        status: str = "Active",
        claim_name: str | None = None,
        relations: tuple[Relation, ...] | None = None,
    ) -> dict[str, object]:
        section = claim_name or ("Operation" if role == "Operations" else "Claim")
        carrier = Carrier(sections(primary, claim_name=section), role, status)
        return definition_claims.assess_definition(
            carrier,
            relations if relations is not None else (Relation("GOVERNS", target),),
        )

    def test_recognizes_requirement_definition_with_traceable_source(self) -> None:
        result = self.assess(
            "a Subject Path **means** one full canonical Subject Expression.",
            "Subject Path",
        )

        self.assertEqual("recognized", result["state"])
        self.assertEqual("Subject Path", result["term"])
        self.assertEqual("Subject Path", result["subject_path"])
        contribution = result["contribution"]
        self.assertEqual("Claim", contribution["section"])
        self.assertEqual("CA-R-TEST", contribution["source"]["carrier"]["atom_id"])
        self.assertEqual(7, contribution["source"]["carrier"]["revision"])
        self.assertEqual("a" * 64, contribution["source"]["carrier"]["carrier_sha256"])
        self.assertEqual(64, len(contribution["source"]["digest"]))

    def test_recognizes_delivery_claim(self) -> None:
        result = self.assess(
            "Release Receipt **means** the immutable accepted release record.",
            "Release Receipt",
            role="Delivery",
        )

        self.assertEqual("recognized", result["state"])
        self.assertEqual("Claim", result["contribution"]["section"])

    def test_operations_reads_operation_not_claim(self) -> None:
        body = (
            "## Claim\n\nAction **means** an ignored claim section.\n\n"
            "## Operation\n\nAction **means** a reusable operational building block.\n\n"
            "## Details\n\nIgnored **means** text.\n"
        )
        result = definition_claims.assess_definition(
            Carrier(body, "Operations"),
            (Relation("GOVERNS", "Atom/Content Role: Operations/Type: Action"),),
        )

        self.assertEqual("recognized", result["state"])
        self.assertEqual("Operation", result["contribution"]["section"])
        self.assertEqual("Action", result["term"])

    def test_fenced_example_does_not_admit_definition(self) -> None:
        result = self.assess(
            "```md\nExample **means** a false definition.\n```\n\nNo definition here.",
            "Example",
        )

        self.assertEqual("not_definition", result["state"])
        self.assertIsNone(result["term"])

    def test_wrong_terminal_target_is_reported_without_new_terms(self) -> None:
        result = self.assess(
            "Action **means** a reusable operation.",
            "Atom/Content Role: Operations/Type: Workflow",
        )

        self.assertEqual("target_mismatch", result["state"])
        self.assertEqual("Action", result["term"])
        self.assertEqual("Atom/Content Role: Operations/Type: Workflow", result["subject_path"])
        self.assertIn(
            "definition-terminal-term-mismatch",
            {item["code"] for item in result["diagnostics"]},
        )

    def test_duplicate_primary_sections_are_unsupported(self) -> None:
        body = (
            "## Claim\n\nEntity **means** the first value.\n\n"
            "## Claim\n\nEntity **means** the second value.\n"
        )
        result = definition_claims.assess_definition(
            Carrier(body, "Requirement"), (Relation("GOVERNS", "Entity"),)
        )

        self.assertEqual("unsupported_candidate", result["state"])
        self.assertIn(
            "definition-primary-section-cardinality",
            {item["code"] for item in result["diagnostics"]},
        )

    def test_empty_definition_text_is_unsupported(self) -> None:
        result = self.assess("Term **means** .", "Term")

        self.assertEqual("unsupported_candidate", result["state"])
        self.assertIn("definition-text-empty", {item["code"] for item in result["diagnostics"]})

    def test_qualified_path_uses_only_the_terminal_term(self) -> None:
        result = self.assess(
            "the Term Action **means** an Operation Type value.",
            "Atom/Content Role: Operations/Type: Action",
        )

        self.assertEqual("recognized", result["state"])
        self.assertEqual("Action", result["term"])
        self.assertEqual(
            "Atom/Content Role: Operations/Type: Action",
            result["evidence"]["governs"]["subject_path"],
        )

    def test_unsupported_unbold_means_is_diagnosed(self) -> None:
        result = self.assess("Term means a legacy-looking statement.", "Term")

        self.assertEqual("unsupported_candidate", result["state"])
        self.assertIn("definition-means-not-bold", {item["code"] for item in result["diagnostics"]})

    def test_inactive_definition_cannot_be_recognized(self) -> None:
        result = self.assess("Term **means** a value.", "Term", status="Draft")

        self.assertEqual("unsupported_candidate", result["state"])
        self.assertIn("definition-authority-inactive", {item["code"] for item in result["diagnostics"]})

    def test_duplicate_governs_is_unsupported(self) -> None:
        result = self.assess(
            "Term **means** a value.",
            "Term",
            relations=(Relation("GOVERNS", "Term"), Relation("GOVERNS", "Other Term")),
        )

        self.assertEqual("unsupported_candidate", result["state"])
        self.assertIn("definition-governs-cardinality", {item["code"] for item in result["diagnostics"]})


class RawPrimaryContentEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.root.mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_carrier(
        self,
        body: str,
        *,
        content_role: str = "Requirement",
        status: str = "Active",
        atom_id: str = "CA-R-900",
        version: int = 7,
        relative: str = "sources/CA-R-900.md",
        eol: str = "\n",
    ) -> RawCarrier:
        frontmatter = eol.join((
            f'atom_id: "{atom_id}"',
            f"version: {version}",
            f"content_role: {content_role}",
            f"status: {status}",
        ))
        data = (f"---{eol}{frontmatter}{eol}---{eol}{body}").encode("utf-8")
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return RawCarrier(
            atom_id=atom_id,
            version=version,
            carrier_path=relative,
            sha256=hashlib.sha256(data).hexdigest(),
            frontmatter=frontmatter,
            body=body,
            content_role=content_role,
            status=status,
        )

    def diagnostic_codes(self, result: dict[str, object]) -> set[str]:
        return {item["code"] for item in result["diagnostics"]}

    def test_uses_raw_crlf_bytes_and_absolute_inclusive_primary_span(self) -> None:
        eol = "\r\n"
        body = (
            f"# Summary{eol}"
            f"> ## Claim{eol}"
            f"```md{eol}## Claim{eol}Example **means** nothing.{eol}```{eol}"
            f"## Claim{eol}"
            f"{eol}"
            f"Café **means** the current value.{eol}"
            f"{eol}"
            f"> ## Details{eol}"
            f"Still primary.{eol}"
            f"## Details{eol}"
            f"Ignored.{eol}"
        )
        carrier = self.write_carrier(body, eol=eol)

        result = definition_claims.raw_primary_content_evidence(self.root, carrier)

        self.assertEqual([], result["diagnostics"])
        evidence = result["evidence"]
        self.assertEqual("primary_content", evidence["contribution"]["kind"])
        self.assertEqual("Claim", evidence["contribution"]["section"])
        source_bytes = (self.root / carrier.carrier_path).read_bytes()
        lines = source_bytes.splitlines(keepends=True)
        heading_index = [
            index for index, line in enumerate(lines) if line == b"## Claim\r\n"
        ][-1]
        details_index = lines.index(b"## Details\r\n")
        span = b"".join(lines[heading_index + 1 : details_index])
        self.assertEqual(heading_index + 2, evidence["contribution"]["start_line"])
        self.assertEqual(details_index, evidence["contribution"]["end_line"])
        self.assertEqual(hashlib.sha256(span).hexdigest(), evidence["contribution"]["text_sha256"])
        self.assertIn(b"\r\n", span)
        # The legacy body-relative reader is intentionally a separate API.
        self.assertEqual("Claim", definition_claims.primary_contribution(carrier)["section"])

    def test_rejects_body_line_ending_drift_after_hash_verified_reread(self) -> None:
        carrier = self.write_carrier("## Claim\r\n\r\nTerm **means** a value.\r\n", eol="\r\n")
        drifted = replace(carrier, body=carrier.body.replace("\r\n", "\n"))

        result = definition_claims.raw_primary_content_evidence(self.root, drifted)

        self.assertIsNone(result["evidence"])
        self.assertIn("raw-carrier-body-drift", self.diagnostic_codes(result))

    def test_rejects_hash_identity_and_revision_mismatches(self) -> None:
        carrier = self.write_carrier("## Claim\n\nTerm **means** a value.\n")

        wrong_hash = definition_claims.raw_primary_content_evidence(
            self.root, replace(carrier, sha256="0" * 64)
        )
        wrong_identity = definition_claims.raw_primary_content_evidence(
            self.root, replace(carrier, atom_id="CA-R-901")
        )
        wrong_revision = definition_claims.raw_primary_content_evidence(
            self.root, replace(carrier, version=8)
        )

        self.assertIn("raw-carrier-hash-mismatch", self.diagnostic_codes(wrong_hash))
        self.assertIn("raw-carrier-identity-mismatch", self.diagnostic_codes(wrong_identity))
        self.assertIn("raw-carrier-identity-mismatch", self.diagnostic_codes(wrong_revision))

    def test_rejects_missing_duplicate_and_unsupported_primary_sections(self) -> None:
        missing = self.write_carrier("## Details\n\nNo primary section.\n")
        duplicate = self.write_carrier(
            "## Claim\n\nFirst.\n\n## Claim\n\nSecond.\n",
            relative="sources/duplicate.md",
        )
        unsupported = self.write_carrier(
            "## Claim\n\nOther role.\n",
            content_role="Concern",
            atom_id="CA-C-900",
            relative="sources/concern.md",
        )

        self.assertIn(
            "raw-primary-section-missing",
            self.diagnostic_codes(definition_claims.raw_primary_content_evidence(self.root, missing)),
        )
        self.assertIn(
            "raw-primary-section-cardinality",
            self.diagnostic_codes(definition_claims.raw_primary_content_evidence(self.root, duplicate)),
        )
        self.assertIn(
            "raw-primary-section-unsupported-role",
            self.diagnostic_codes(definition_claims.raw_primary_content_evidence(self.root, unsupported)),
        )

    def test_four_backtick_fence_does_not_close_at_three_backticks(self) -> None:
        carrier = self.write_carrier(
            "# Example\n\n"
            "````md\n"
            "```\n"
            "## Claim\n\n"
            "Term **means** an example only.\n"
            "````\n"
            "\n## Details\n\nNo role-primary source section exists.\n",
        )

        result = definition_claims.raw_primary_content_evidence(self.root, carrier)

        self.assertIsNone(result["evidence"])
        self.assertIn("raw-primary-section-missing", self.diagnostic_codes(result))

    def test_rejects_path_escape_and_symlink_carriers(self) -> None:
        carrier = self.write_carrier("## Claim\n\nTerm **means** a value.\n")
        escaped = replace(carrier, carrier_path="../outside.md")
        outside = Path(self.temporary.name) / "outside.md"
        outside.write_bytes((self.root / carrier.carrier_path).read_bytes())
        link = self.root / "sources" / "link.md"
        link.symlink_to(outside)
        symlinked = replace(carrier, carrier_path="sources/link.md")

        self.assertIn(
            "raw-carrier-path-invalid",
            self.diagnostic_codes(definition_claims.raw_primary_content_evidence(self.root, escaped)),
        )
        self.assertIn(
            "raw-carrier-symlink-rejected",
            self.diagnostic_codes(definition_claims.raw_primary_content_evidence(self.root, symlinked)),
        )

    def test_rejects_backslash_carrier_path_before_path_resolution(self) -> None:
        carrier = self.write_carrier("## Claim\n\nTerm **means** a value.\n")

        result = definition_claims.raw_primary_content_evidence(
            self.root, replace(carrier, carrier_path="sources\\CA-R-900.md")
        )

        self.assertIsNone(result["evidence"])
        self.assertIn("raw-carrier-path-invalid", self.diagnostic_codes(result))
