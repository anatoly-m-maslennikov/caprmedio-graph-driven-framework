"""Canonical Journal durability, not a cached receipt, proves append success."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_work_journal_schema_v5 as fixtures  # noqa: E402
import work_journal  # noqa: E402


class WorkJournalReceiptIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.WorkJournalSchemaV5Test(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root, self.event = self.fixture.root, self.fixture.event
        self.partition = {"author": "test-user", "local_date": "2026-10-04", "timezone": "Asia/Tbilisi"}

    def append(self, event=None):
        return work_journal.append_sealed_events(self.root, [self.event if event is None else event], **self.partition)[0]

    def predict(self, event=None):
        return work_journal.predict_sealed_event_receipts(self.root, [self.event if event is None else event], **self.partition)[0]

    def cache(self):
        return work_journal._receipt_path(self.root, self.event["event_id"])

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                for path in self.root.rglob("*") if path.is_file()}

    def assert_refusal_without_writes(self, action, code):
        before = self.snapshot()
        with self.assertRaises(work_journal.WorkJournalError) as caught:
            action()
        self.assertEqual(code, caught.exception.code)
        self.assertEqual(before, self.snapshot())

    def other_event(self):
        event = copy.deepcopy(self.event)
        event["event_id"] = "independent-unrelated-event"
        return work_journal.with_event_digest(event)

    def test_real_append_then_idempotence_uses_exact_canonical_line_prefix(self):
        receipt = self.append()
        payload = work_journal.canonical_json_bytes(self.event) + b"\n"
        self.assertEqual(payload, (self.root / receipt["carrier"]).read_bytes())
        self.assertEqual({
            "event_id": self.event["event_id"], "action_id": self.event["action_id"],
            "event_digest": self.event["event_digest"], "carrier": receipt["carrier"], "line": 1,
            "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
            "appended_carrier_digest": hashlib.sha256(payload).hexdigest(),
        }, receipt)
        unrelated = self.append(self.other_event())
        self.assertEqual(2, unrelated["line"])
        before = self.snapshot()
        self.assertEqual(receipt, self.append())
        self.assertEqual({**receipt, "disposition": "reused"}, self.predict())
        self.assertEqual(before, self.snapshot())

    def test_deleted_canonical_carrier_cannot_return_cached_success_or_reappend(self):
        receipt = self.append()
        carrier = self.root / receipt["carrier"]
        cached_bytes = self.cache().read_bytes()
        carrier.unlink()
        self.assert_refusal_without_writes(self.append, "invalid-receipt")
        self.assert_refusal_without_writes(self.predict, "invalid-receipt")
        self.assertFalse(carrier.exists())
        self.assertEqual(cached_bytes, self.cache().read_bytes())

    def test_missing_canonical_event_and_malformed_or_mismatched_cache_refuse(self):
        receipt = self.append()
        (self.root / receipt["carrier"]).unlink()
        cases = [
            (b"not JSON", "invalid-receipt"),
            (b"[]", "invalid-receipt"),
            (json.dumps({**receipt, "event_id": "other-event"}).encode(), "invalid-receipt"),
            (json.dumps({**receipt, "event_digest": "0" * 64}).encode(), "identity-collision"),
            (json.dumps({**receipt, "action_id": "other-action"}).encode(), "invalid-receipt"),
            (json.dumps({**receipt, "carrier": "unrelated.ndjson"}).encode(), "invalid-receipt"),
            (json.dumps({**receipt, "line": 99}).encode(), "invalid-receipt"),
            (json.dumps({"event_id": receipt["event_id"], "event_digest": receipt["event_digest"]}).encode(), "invalid-receipt"),
        ]
        for cached, code in cases:
            with self.subTest(cached=cached):
                self.cache().write_bytes(cached)
                self.assert_refusal_without_writes(self.append, code)
                self.assert_refusal_without_writes(self.predict, code)

    def test_canonical_present_cache_absent_reconstructs_receipt_without_rewriting(self):
        receipt = self.append()
        self.cache().unlink()
        before = self.snapshot()
        self.assertEqual(receipt, self.append())
        self.assertEqual({**receipt, "disposition": "reused"}, self.predict())
        self.assertFalse(self.cache().exists())
        self.assertEqual(before, self.snapshot())

    def test_canonical_present_is_authority_even_when_cache_is_forged_or_unreadable_json(self):
        receipt = self.append()
        for cached in (b"not JSON", json.dumps({**receipt, "event_id": "other-event", "event_digest": "0" * 64,
                                                "action_id": "other-action", "carrier": "unrelated.ndjson", "line": 99}).encode()):
            with self.subTest(cached=cached):
                self.cache().write_bytes(cached)
                before = self.snapshot()
                self.assertEqual(receipt, self.append())
                self.assertEqual({**receipt, "disposition": "reused"}, self.predict())
                self.assertEqual(before, self.snapshot())

    def test_unrelated_canonical_event_cannot_back_the_deleted_targets_cached_receipt(self):
        target_receipt = self.append()
        (self.root / target_receipt["carrier"]).unlink()
        unrelated_event = self.other_event()
        unrelated = self.append(unrelated_event)
        carrier = self.root / unrelated["carrier"]
        self.assertEqual(work_journal.canonical_json_bytes(unrelated_event) + b"\n", carrier.read_bytes())
        self.assert_refusal_without_writes(self.append, "invalid-receipt")
        self.assert_refusal_without_writes(self.predict, "invalid-receipt")
        self.assertEqual(unrelated, self.append(unrelated_event))

    def test_same_event_identity_with_different_valid_sealed_bytes_refuses_before_mutation(self):
        self.append()
        changed = copy.deepcopy(self.event)
        changed.update(event="failed", outcome="failed")
        changed = work_journal.with_event_digest(changed)
        self.assertNotEqual(self.event["event_digest"], changed["event_digest"])
        self.assert_refusal_without_writes(lambda: self.append(changed), "identity-collision")
        self.assert_refusal_without_writes(lambda: self.predict(changed), "identity-collision")

    def test_changed_canonical_result_with_retained_declared_digest_cannot_prove_success(self):
        receipt = self.append()
        carrier = self.root / receipt["carrier"]
        changed = copy.deepcopy(self.event)
        changed["result_ref"] = "results/altered-result.json"
        self.assertEqual(self.event["event_digest"], changed["event_digest"])
        self.assertNotEqual(self.event["event_digest"], work_journal.event_digest(changed))
        carrier.write_bytes(work_journal.canonical_json_bytes(changed) + b"\n")
        self.assert_refusal_without_writes(self.append, "identity-collision")
        self.assert_refusal_without_writes(self.predict, "identity-collision")

    def test_physical_json_spacing_and_key_order_do_not_change_the_existing_event_digest_contract(self):
        receipt = self.append()
        carrier = self.root / receipt["carrier"]
        differently_formatted = json.dumps(self.event, sort_keys=False, separators=(", ", ": ")).encode() + b"\n"
        self.assertNotEqual(carrier.read_bytes(), differently_formatted)
        self.assertEqual(self.event["event_digest"], work_journal.event_digest(json.loads(differently_formatted)))
        carrier.write_bytes(differently_formatted)
        before = self.snapshot()
        actual_receipt = {**receipt, "appended_carrier_digest": hashlib.sha256(differently_formatted).hexdigest()}
        self.assertEqual(actual_receipt, self.append())
        self.assertEqual({**actual_receipt, "disposition": "reused"}, self.predict())
        self.assertEqual(before, self.snapshot())


if __name__ == "__main__":
    unittest.main()
