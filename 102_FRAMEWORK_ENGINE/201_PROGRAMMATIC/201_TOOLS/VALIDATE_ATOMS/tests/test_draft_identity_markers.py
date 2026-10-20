"""Source-bound Draft identity marker admission cases."""

from __future__ import annotations

from functools import lru_cache
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


@lru_cache(maxsize=1)
def context():
    return resolve_context([frozen_source("CA-D-446"), frozen_source("CA-D-378")])


def run(status: str, value: str | None = None, *, version: int = 4) -> dict:
    metadata = {"content_role": "Requirement", "status": status, "version": version}
    if value is not None:
        metadata["atom_id"] = value
    return validate_carrier(
        metadata,
        "",
        context(),
        {
            "sources": [frozen_source("CA-D-446"), frozen_source("CA-D-378")],
            "_project_identity": {"identity": {"project_prefix": "CA"}},
        },
    )


def outcome(result: dict) -> dict:
    return next(row for row in result["outcomes"] if row["code"] == "frontmatter.atom_id")


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


if __name__ == "__main__":
    unittest.main()
