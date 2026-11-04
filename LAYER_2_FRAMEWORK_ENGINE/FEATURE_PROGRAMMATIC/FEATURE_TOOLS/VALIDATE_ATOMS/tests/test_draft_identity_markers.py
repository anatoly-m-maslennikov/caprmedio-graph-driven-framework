"""Source-bound Draft identity marker admission cases."""

from __future__ import annotations

from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
TOOL = HERE.parent
sys.path.insert(0, str(TOOL))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TOOL.parent))

from golden_authority import frozen_source  # noqa: E402
from validate_atoms_workers.authority import resolve_context  # noqa: E402
from validate_atoms_workers.checks import validate_carrier  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402


FIXTURES = HERE / "fixtures"


def fixture_source(path: Path) -> dict:
    raw = path.read_bytes()
    parsed = parse_carrier(raw, path)
    return {
        "binding": {
            "atom_id": parsed.metadata["atom_id"],
            "version": parsed.metadata["version"],
            "sha256": hashlib.sha256(raw).hexdigest(),
            "path": str(path),
        },
        "text": parsed.text,
        "metadata": parsed.metadata,
    }


@lru_cache(maxsize=1)
def legacy_sources() -> tuple[dict, ...]:
    return (
        frozen_source("CA-D-276"),
        frozen_source("CA-D-446"),
        fixture_source(FIXTURES / "schema_authority/CA-D-378@16.md"),
    )


@lru_cache(maxsize=1)
def current_sources() -> tuple[dict, ...]:
    encoding = json.loads((FIXTURES / "current_encoding_authority.json").read_text(encoding="utf-8"))
    raw = encoding["text"].encode("utf-8")
    path = FIXTURES / encoding["source_path"]
    parsed = parse_carrier(raw, path)
    return (
        {
            "binding": {
                "atom_id": parsed.metadata["atom_id"],
                "version": parsed.metadata["version"],
                "sha256": hashlib.sha256(raw).hexdigest(),
                "path": str(path),
            },
            "text": parsed.text,
            "metadata": parsed.metadata,
        },
        frozen_source("CA-D-446"),
        frozen_source("CA-D-378"),
    )


@lru_cache(maxsize=1)
def legacy_context():
    return resolve_context(list(legacy_sources()))


@lru_cache(maxsize=1)
def current_context():
    return resolve_context(list(current_sources()))


def run(status: str, value: str | None = None, *, version: int = 4) -> dict:
    metadata = {"content_role": "Requirement", "status": status, "version": version}
    if value is not None:
        metadata["atom_id"] = value
    return validate_carrier(
        metadata,
        "",
        legacy_context(),
        {
            "sources": list(legacy_sources()),
            "_project_identity": {"identity": {"project_prefix": "CA"}},
        },
    )


def current_run(
    value: str | None,
    *,
    version: int = 4,
    project_prefix: str = "CA",
    sources: tuple[dict, ...] | None = None,
) -> dict:
    metadata = {
        "role": "Requirement",
        "form": "Rule",
        "tier": 1,
        "status": "Draft",
        "version": version,
        "subjects": {"active": "Atom", "passive": []},
        "relations": {},
    }
    if value is not None:
        metadata["atom_id"] = value
    return validate_carrier(
        metadata,
        "",
        current_context(),
        {
            "sources": list(current_sources() if sources is None else sources),
            "_project_identity": {"identity": {"project_prefix": project_prefix}},
        },
    )


def outcome(result: dict) -> dict:
    return next(row for row in result["outcomes"] if row["code"] == "frontmatter.atom_id")


def changed_source(source: dict, suffix: str) -> dict:
    changed = {**source, "binding": dict(source["binding"]), "text": source["text"] + suffix}
    changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode("utf-8")).hexdigest()
    return changed


def changed_claim_source(source: dict) -> dict:
    changed = {**source, "binding": dict(source["binding"])}
    changed["text"] = source["text"].replace("## Claim\n", "## Claim\nChanged ", 1)
    changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode("utf-8")).hexdigest()
    return changed


def has_gap(result: dict, phrase: str) -> bool:
    return any(phrase in row["reason"] for row in result["gaps"])


class DraftIdentityMarkerTest(unittest.TestCase):
    def test_id_free_and_all_admitted_draft_markers_pass(self) -> None:
        for value in (None, "CA-R-draft", "CA-R-123@4-draft", "CA-R-123@draft"):
            with self.subTest(value=value):
                self.assertEqual(outcome(run("Draft", value))["outcome"], "passed")

    def test_qualified_marker_must_match_carried_version(self) -> None:
        self.assertEqual(
            outcome(run("Draft", "CA-R-123@5-draft", version=4))["outcome"], "failed"
        )

    def test_draft_marker_must_match_project_role_and_marker_grammar(self) -> None:
        for value in ("EX-R-draft", "CA-M-draft", "CA-R-123", "CA-R-123@oops-draft"):
            with self.subTest(value=value):
                self.assertEqual(outcome(run("Draft", value))["outcome"], "failed")

    def test_markers_are_draft_only_but_canonical_non_draft_identity_remains_admitted(self) -> None:
        self.assertEqual(outcome(run("Active", "CA-R-123"))["outcome"], "passed")
        for status in ("Active", "Archived"):
            with self.subTest(status=status):
                self.assertEqual(
                    outcome(run(status, "CA-R-123@4-draft"))["outcome"], "failed"
                )

    def test_current_draft_requires_a_canonical_header_id(self) -> None:
        self.assertEqual(outcome(current_run("CA-R-123"))["outcome"], "passed")
        self.assertEqual(
            outcome(current_run("EX-R-123", project_prefix="EX"))["outcome"], "passed"
        )
        self.assertEqual(
            outcome(current_run("ca-R-123", project_prefix="ca"))["outcome"], "failed"
        )
        for value in (None, "CA-R-draft", "CA-R-123@4-draft", "CA-M-123"):
            with self.subTest(value=value):
                self.assertEqual(outcome(current_run(value))["outcome"], "failed")

    def test_draft_identity_rejects_missing_mixed_or_unreviewed_encoding_profiles(self) -> None:
        source_rows = current_sources()
        cases = {
            "missing": source_rows[1:],
            "mixed": (*source_rows, frozen_source("CA-D-276")),
            "unreviewed": (changed_claim_source(source_rows[0]), *source_rows[1:]),
        }
        for label, sources in cases.items():
            with self.subTest(label=label):
                result = current_run("CA-R-123", sources=sources)
                self.assertNotEqual(outcome(result)["outcome"], "passed")
                self.assertTrue(has_gap(result, "exactly one reviewed Current or legacy encoding profile"))

    def test_current_draft_requires_the_reviewed_d378_pin(self) -> None:
        source_rows = current_sources()
        result = current_run(
            "CA-R-123",
            sources=(*source_rows[:2], changed_source(source_rows[2], "\nretained markers only\n")),
        )
        self.assertNotEqual(outcome(result)["outcome"], "passed")
        self.assertTrue(has_gap(result, "Missing or changed supporting authority: CA-D-378."))


if __name__ == "__main__":
    unittest.main()
