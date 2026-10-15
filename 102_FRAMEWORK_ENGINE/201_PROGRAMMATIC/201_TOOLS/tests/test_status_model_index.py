"""A bounded status snapshot preserves exact per-carrier model selection."""

from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import authoritative_status_models as models  # noqa: E402
import test_authoritative_status_models as fixtures  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402


class StatusModelIndexTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.AuthoritativeStatusModelsTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root.resolve()
        self.general = self.fixture._source("CA-R-9001", "Plan", ["Active", "Done"])
        self.fixture._source("CA-R-9002", "Plan", ["Active", "Backlog"], atom_type="Epic")
        self.reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))

    def test_index_retains_exact_type_specific_fallback_and_supplied_model_checks(self):
        index = models.capture_status_models(self.root, self.reader)
        for atom, status in (
            ({"content_role": "Plan"}, "Done"),
            ({"content_role": "Plan", "type": "Epic"}, "Backlog"),
            ({"content_role": "Plan", "type": "Other"}, "Done"),
        ):
            with self.subTest(atom=atom):
                expected = models.resolve_status_model(self.root, atom, status)
                actual = models.resolve_status_model(self.root, atom, status, _index=index)
                self.assertEqual(expected, actual)
                self.assertEqual(
                    actual,
                    models.resolve_status_model(
                        self.root, atom, status, supplied_model=actual, _index=index
                    ),
                )
                actual["statuses"].append("forged")
                with self.assertRaises(models.StatusModelError):
                    models.resolve_status_model(
                        self.root, atom, status, supplied_model=actual, _index=index
                    )
        with self.assertRaises(models.StatusModelError):
            models.resolve_status_model(self.root, {"content_role": "Plan"}, "active", _index=index)
        with self.assertRaises(models.StatusModelError):
            models.resolve_status_model(
                self.root.parent, {"content_role": "Plan"}, "Active", _index=index
            )
        models.revalidate_status_models(index, self.reader)

    def test_duplicate_domains_and_invalid_declarations_still_refuse(self):
        self.fixture._source("CA-R-9003", "Plan", ["Active", "Done"])
        index = models.capture_status_models(self.root, self.reader)
        with self.assertRaises(models.StatusModelError):
            models.resolve_status_model(self.root, {"content_role": "Plan"}, "Active", _index=index)
        self.general.write_bytes(
            self.general.read_bytes().replace(b"status: Active", b"status: Archived")
        )
        with self.assertRaises(models.StatusModelError):
            models.capture_status_models(self.root, self.reader)

    def test_capture_and_final_reads_share_one_budget_without_broad_currentness_records(self):
        index = models.capture_status_models(self.root, self.reader)
        self.assertEqual({}, self.reader.fingerprints)
        self.assertEqual({}, self.reader.inventories)
        consumed = self.reader.bytes_read
        models.revalidate_status_models(index, self.reader)
        self.assertGreater(self.reader.bytes_read, consumed)
        self.reader.limits["max_total_read_bytes"] = self.reader.bytes_read
        with self.assertRaises(LimitReached):
            models.revalidate_status_models(index, self.reader)


if __name__ == "__main__":
    unittest.main()
