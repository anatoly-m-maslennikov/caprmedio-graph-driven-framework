"""Fail-closed admission for the proposed schema2 Subject transition."""

from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from subject_batch import _PacketV1, _PacketV2
from subject_batch_authorization import (
    _INTENT_DELIVERY_CLAUSE, _OPERATIVE_CLAUSE, _PACKET_DELIVERY_CLAUSE,
    require_subject_profile_transition_authority,
)


class SubjectTransitionAuthorityTests(unittest.TestCase):
    def _root(self):
        root = Path(tempfile.mkdtemp(dir="/private/tmp"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        return root

    def test_only_the_exact_positive_operative_clause_admits_all_five_owners(self):
        root = self._root()
        slots = tuple((f"owner-{ordinal}.md", clause) for ordinal, clause in enumerate(
            (_OPERATIVE_CLAUSE, _OPERATIVE_CLAUSE, _OPERATIVE_CLAUSE,
             _INTENT_DELIVERY_CLAUSE, _PACKET_DELIVERY_CLAUSE)
        ))
        for owner, clause in slots:
            (root / owner).write_text("## Details\n\n" + clause)
        with patch("subject_batch_authorization._TRANSITION_AUTHORITY", slots):
            require_subject_profile_transition_authority(root)

    def test_history_or_prohibition_text_cannot_admit_the_transition(self):
        root = self._root()
        slots = tuple((f"owner-{ordinal}.md", clause) for ordinal, clause in enumerate(
            (_OPERATIVE_CLAUSE, _OPERATIVE_CLAUSE, _OPERATIVE_CLAUSE,
             _INTENT_DELIVERY_CLAUSE, _PACKET_DELIVERY_CLAUSE)
        ))
        for owner, _ in slots:
            (root / owner).write_text("History: do not admit source_subject_profile legacy approved batch.")
        with patch("subject_batch_authorization._TRANSITION_AUTHORITY", slots):
            with self.assertRaisesRegex(ValueError, "not active"):
                require_subject_profile_transition_authority(root)

    def test_schema1_rejects_transition_field_and_schema2_requires_exact_pair(self):
        base = {"subject_profile": "approved", "git_checkpoint": "0" * 40, "atoms": [{
            "target": {"atom_id": "CA-R-1", "path": "a.md", "filename": "a.md", "version": 1,
                       "digest": "0" * 64, "lifecycle": "current", "status": "Active",
                       "updated_at": "2026-01-01 00:00:00 +0000", "content_role": "Requirement", "type": "Rule"},
            "subject_patches": [{"field": "governs", "old": "A", "new": "B"}],
        }]}
        with self.assertRaises(Exception):
            _PacketV1.model_validate({**base, "schema_version": 1, "source_subject_profile": "legacy"})
        _PacketV2.model_validate({**base, "schema_version": 2, "source_subject_profile": "legacy"})
        with self.assertRaises(Exception):
            _PacketV2.model_validate({**base, "schema_version": 2, "source_subject_profile": "approved"})


if __name__ == "__main__":
    unittest.main()
