"""Observe a Current Plan's standalone Archive boundary."""
import json
import unittest

import yaml
import test_flat_plan_archive


class CurrentStandaloneArchiveDestinationTest(unittest.TestCase):
    def test_standalone_archive_destination_and_history(self):
        fixture = test_flat_plan_archive.FlatPlanArchiveTests("runTest")
        fixture.setUp()
        try:
            source = fixture._plan("CA-P-796", "destination", version=3)
            source_name = source.name
            source_parent = source.parent.relative_to(fixture.root).as_posix()
            text = source.read_text().replace("subjects:\n", f"carrier_destination:\n  file:\n    name: {source_name}\n    path: {source_parent}\nsubjects:\n", 1)
            source.write_text(text)
            before = source.read_bytes()
            before_front, before_body = before.decode().split("---", 2)[1:]
            result = fixture._archive(source)
            archived = fixture.root / result["observed"]["path"]
            archived_front, archived_body = archived.read_text().split("---", 2)[1:]
            initial, observed = yaml.safe_load(before_front), yaml.safe_load(archived_front)
            prior = fixture.root / result["history"]["prior_revision"]["path"]
            self.assertEqual(before, prior.read_bytes())
            self.assertEqual(before_body, archived_body)
            self.assertEqual(observed["status"], "Archived")
            self.assertEqual(observed["version"], initial["version"] + 1)
            self.assertNotEqual(str(observed["updated_at"]), str(initial["updated_at"]))
            self.assertEqual(observed["carrier_destination"]["file"]["name"], archived.name)
            self.assertEqual(observed["carrier_destination"]["file"]["path"], archived.parent.relative_to(fixture.root).as_posix())
            print("ARCHIVE_OBSERVATION " + json.dumps({
                "before_version": initial["version"], "archive_version": observed["version"],
                "before_updated_at": str(initial["updated_at"]), "archive_updated_at": str(observed["updated_at"]),
                "stored_destination": observed["carrier_destination"]["file"],
                "actual_name": archived.name, "actual_path": archived.parent.relative_to(fixture.root).as_posix(),
                "history_exact": before == prior.read_bytes(), "body_exact": before_body == archived_body,
            }))
        finally:
            fixture.doCleanups()

    def test_absent_destination_is_not_backfilled(self):
        fixture = test_flat_plan_archive.FlatPlanArchiveTests("runTest")
        fixture.setUp()
        try:
            source = fixture._plan("CA-P-797", "no-destination", version=3)
            result = fixture._archive(source)
            archived = fixture.root / result["observed"]["path"]
            self.assertNotIn("carrier_destination", yaml.safe_load(archived.read_text().split("---", 2)[1]))
        finally:
            fixture.doCleanups()


if __name__ == "__main__":
    unittest.main()
