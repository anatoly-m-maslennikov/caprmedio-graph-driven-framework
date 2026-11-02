from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_contract import ERROR_CODES, validate_request, validate_result


def request(operation="read"):
    return {
        "operation": operation,
        "target": None if operation == "query" else {"kind": "Atom", "identity": "CA-R-863"},
        "query": {"kind": "Atom", "filters": {"scope": "CORE"}} if operation == "query" else None,
        "delta": {"content": "explicit content"} if operation in {"create", "modify"} else None,
        "expected_state": (
            {"absent": True} if operation == "create"
            else {"source_token": "before"} if operation == "modify" else None
        ),
        "authorization": "bound-permission-reference",
        "context": "bound-context-reference",
    }


def check_request(value, operations=("query", "read", "create", "modify"), kinds=("Atom",)):
    return validate_request(value, supported_operations=operations, supported_kinds=kinds)


def result():
    return {
        "data": {"content": "actual content"},
        "current_state": {"identity": "CA-R-863", "version": 7, "source_token": "after"},
        "effects": [], "errors": [],
    }


def effect(value, state="known"):
    return {
        "operation": value["operation"], "target": copy.deepcopy(value["target"]),
        "state": state, "evidence": {"observation": "after-state"},
    }


class ConnectorRequestTests(unittest.TestCase):
    def test_all_operations_and_unpinned_read(self):
        for operation in ("query", "read", "create", "modify"):
            with self.subTest(operation=operation):
                self.assertEqual(check_request(request(operation)), [])

    def test_closed_shape_and_json_values(self):
        for value in (None, [], {**request(), "extra": 1}, {"operation": "read"}):
            with self.subTest(value=value):
                self.assertEqual(check_request(value)[0]["code"], "input_invalid")
        for value in ({1: "non-string-key"}, ("tuple",), object(), float("nan"), float("inf")):
            with self.subTest(value=value):
                self.assertTrue(check_request({**request(), "expected_state": value}))

    def test_cyclic_values_are_rejected_as_non_json(self):
        value = request()
        value["expected_state"] = value
        self.assertEqual(check_request(value)[0]["code"], "input_invalid")
        output = result()
        output["data"] = output
        self.assertEqual(validate_result(output, request=request())[0]["code"], "input_invalid")

    def test_unsupported_operation_and_kind(self):
        for operation in ("delete", [], False):
            self.assertEqual(check_request({**request(), "operation": operation})[0]["code"], "unsupported_operation")
        self.assertEqual(check_request(request("modify"), operations=("read",))[0]["code"], "unsupported_operation")
        self.assertEqual(check_request(request(), kinds=("Scope Unit",))[0]["field"], "target")

    def test_wrong_selectors_and_deltas(self):
        cases = [
            ("read", "target", None), ("read", "target", {"kind": "Atom", "path": "a.md"}),
            ("read", "target", {"kind": "Atom", "identity": None}),
            ("read", "query", {"kind": "Atom", "filters": {}}),
            ("query", "target", {"kind": "Atom", "identity": "CA-R-863"}),
            ("query", "query", None), ("query", "delta", {}), ("read", "delta", {}),
            ("create", "delta", None), ("modify", "delta", None),
            ("create", "expected_state", None), ("modify", "expected_state", None),
        ]
        for operation, field, value in cases:
            with self.subTest(operation=operation, field=field, value=value):
                errors = check_request({**request(operation), field: value})
                self.assertIn(field, [error["field"] for error in errors])

    def test_authority_reference_shape_is_not_authority_resolution(self):
        for field in ("authorization", "context"):
            for invalid in (None, True, False, 1, [], {}, "", " "):
                with self.subTest(field=field, invalid=invalid):
                    self.assertIn(field, [e["field"] for e in check_request({**request(), field: invalid})])
            self.assertEqual(check_request({**request(), field: {"reference": "bound-id"}}), [])

    def test_read_expectation_is_opaque_and_unmodified(self):
        value = {**request(), "expected_state": {"version": 2, "source_token": "historical"}}
        before = copy.deepcopy(value)
        self.assertEqual(check_request(value), [])
        self.assertEqual(value, before)


class ConnectorResultTests(unittest.TestCase):
    def test_verified_read_and_empty_query(self):
        self.assertEqual(validate_result(result(), request=request(), postconditions_verified=True), [])
        value = {**result(), "data": []}
        self.assertEqual(validate_result(value, request=request("query"), postconditions_verified=True), [])

    def test_exception_free_or_truthy_verification_is_insufficient(self):
        for verification in (False, None, 1, "verified"):
            self.assertEqual(validate_result(result(), request=request(), postconditions_verified=verification)[0]["code"], "backend_failure")

    def test_no_op_requires_satisfied_and_unchanged_observation(self):
        value = result()
        before = copy.deepcopy(value)
        self.assertTrue(validate_result(value, request=request("modify"), postconditions_verified=True))
        self.assertEqual(validate_result(value, request=request("modify"), postconditions_verified=True, unchanged_verified=True), [])
        self.assertEqual(value, before)

    def test_known_write_requires_verified_postconditions(self):
        call = request("modify")
        value = {**result(), "effects": [effect(call)]}
        self.assertTrue(validate_result(value, request=call))
        self.assertEqual(validate_result(value, request=call, postconditions_verified=True), [])

    def test_partial_effect_and_every_stable_error_remain_failure(self):
        call = request("modify")
        for code in ERROR_CODES:
            with self.subTest(code=code):
                failure = {"code": code, "message": "Observed failure", "field": "target"}
                value = {**result(), "effects": [effect(call)], "errors": [failure]}
                before = copy.deepcopy(value)
                self.assertEqual(validate_result(value, request=call, postconditions_verified=True), [failure])
                self.assertEqual(value, before)

    def test_unknown_effect_requires_uncertain_error(self):
        call = request("modify")
        value = {**result(), "effects": [effect(call, "unknown")]}
        self.assertEqual(validate_result(value, request=call, postconditions_verified=True)[0]["code"], "effect_uncertain")
        value["errors"] = [{"code": "effect_uncertain", "message": "After-state unavailable", "field": None}]
        self.assertEqual(validate_result(value, request=call), value["errors"])

    def test_read_and_query_cannot_report_mutation_even_with_attestation(self):
        for operation in ("read", "query"):
            call = request(operation)
            value = {**result(), "effects": [effect(call)]}
            self.assertTrue(validate_result(value, request=call, postconditions_verified=True))

    def test_wrong_result_effect_and_error_shapes(self):
        call = request("modify")
        cases = [
            None, {**result(), "success": True}, {"data": None},
            {**result(), "data": object()}, {**result(), "effects": {}},
            {**result(), "effects": [{}]}, {**result(), "errors": {}},
            {**result(), "errors": [{}]},
        ]
        for bad in cases:
            with self.subTest(value=bad):
                self.assertTrue(validate_result(bad, request=call, postconditions_verified=True))
        for overrides in ({"state": "proposed"}, {"evidence": None}, {"operation": "create"}, {"target": {"kind": "Atom", "identity": "CA-R-999"}}):
            self.assertTrue(validate_result({**result(), "effects": [{**effect(call), **overrides}]}, request=call, postconditions_verified=True))
        for overrides in ({"code": "other"}, {"code": []}, {"field": "effects"}, {"field": []}, {"message": ""}):
            failure = {"code": "backend_failure", "message": "Failure", "field": None, **overrides}
            self.assertEqual(validate_result({**result(), "errors": [failure]}, request=call)[0]["code"], "input_invalid")


if __name__ == "__main__":
    unittest.main()
