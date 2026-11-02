"""Frozen Concern status and identity admission regressions."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
from typing import Any, ClassVar
import unittest


HERE = Path(__file__).resolve().parent
TOOL = HERE.parent
PROGRAMMATIC_TOOLS = TOOL.parent
sys.path.insert(0, str(TOOL))
sys.path.insert(0, str(PROGRAMMATIC_TOOLS))

from validate_atoms_workers.authority import AuthorityContext, resolve_context  # noqa: E402
from validate_atoms_workers.checks import validate_carrier  # noqa: E402


_SOURCE_SPECS = (
    (
        "CA-D-446",
        "Delivery",
        "Entity/Node/Continuant/History/Revision.Identity",
        "every non-Draft Atom Revision must have one Identifier.",
        14,
    ),
    (
        "CA-R-1947",
        "Requirement",
        "Entity/Node/Continuant/Atom.Status",
        "Atom.Status **must** admit (Draft, Active, Archived).",
        3,
    ),
    (
        "CA-R-1608",
        "Requirement",
        "Entity/Node/Continuant/Atom/Content Role: Concern.Status",
        "the Core Concern Status model **must** inherit the allowed values of "
        "Atom.Status and add (Resolved, Canceled).",
        8,
    ),
)


def _source(spec: tuple[str, str, str, str, int]) -> dict[str, Any]:
    atom_id, content_role, governed, claim, version = spec
    text = (
        f"---\natom_id: {atom_id}\ncontent_role: {content_role}\n"
        f"status: Active\nversion: {version}\nsubjects:\n  governs: \"{governed}\"\n"
        "---\n# Summary\n\nFrozen authority\n\n## Claim\n\n"
        f"{claim}\n"
    )
    metadata = {
        "atom_id": atom_id, "content_role": content_role, "status": "Active",
        "version": version, "subjects": {"governs": governed},
    }
    return {
        "binding": {
            "atom_id": atom_id,
            "version": version,
            "path": f"/fixtures/{atom_id}.md",
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        },
        "text": text,
        "metadata": metadata,
    }


def _context() -> AuthorityContext:
    return resolve_context([_source(spec) for spec in _SOURCE_SPECS])


def _outcome(result: dict[str, Any], code: str) -> dict[str, Any]:
    return next(row for row in result["outcomes"] if row["code"] == code)


def _carrier(status: object, atom_id: str | None = None) -> dict[str, Any]:
    metadata: dict[str, Any] = {"content_role": "Concern", "status": status}
    if atom_id is not None:
        metadata["atom_id"] = atom_id
    return metadata


class ConcernStatusAdmissionTest(unittest.TestCase):
    context: ClassVar[AuthorityContext]

    @classmethod
    def setUpClass(cls) -> None:
        cls.context = _context()

    def test_inherited_model_drives_canonical_draft_and_non_draft_identity(self) -> None:
        self.assertEqual(
            self.context.domains["domain.status.concern"],
            ("Draft", "Active", "Archived", "Resolved", "Canceled"),
        )
        cases = (
            ("Draft", None, "passed"),
            ("Draft", "EX-C-1", "failed"),
            ("Active", "EX-C-1", "passed"),
            ("Resolved", "EX-C-1", "passed"),
            ("Canceled", "EX-C-1", "passed"),
            ("Active", None, "failed"),
        )
        for status, atom_id, expected in cases:
            with self.subTest(status=status, atom_id=atom_id):
                result = validate_carrier(_carrier(status, atom_id), "", self.context)
                self.assertEqual(_outcome(result, "frontmatter.atom_id")["outcome"], expected)

    def test_invalid_or_missing_status_stops_identity_classification(self) -> None:
        invalid = validate_carrier(_carrier("draft"), "", self.context)
        self.assertEqual(_outcome(invalid, "frontmatter.atom_id")["outcome"], "failed")
        self.assertEqual(_outcome(invalid, "domain.status.concern")["outcome"], "failed")

        missing = validate_carrier({"content_role": "Concern"}, "", self.context)
        self.assertEqual(_outcome(missing, "frontmatter.atom_id")["outcome"], "not_checked")
        self.assertEqual(_outcome(missing, "domain.status.concern")["outcome"], "failed")
        self.assertTrue(
            any(
                gap["reason"] == "Identity applicability requires a resolved carried Status."
                for gap in missing["gaps"]
            )
        )


if __name__ == "__main__":
    unittest.main()
