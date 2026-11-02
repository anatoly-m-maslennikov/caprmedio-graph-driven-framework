"""Focused acceptance tests for the closed CA-D-539 fact-context validator."""

from __future__ import annotations

import copy
import hashlib
import sys
import unittest
from pathlib import Path


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))

import fact_context_contract as contract  # noqa: E402
from graph_fact_context import canonical_bytes  # noqa: E402


SHA_A = "a" * 64
SHA_B = "b" * 64
SHA_C = "c" * 64


def digest(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def source_ref() -> dict[str, object]:
    return {
        "atom_id": "CA-R-001",
        "atom_revision": 1,
        "carrier_path": "sources/CA-R-001.md",
        "carrier_sha256": SHA_A,
        "contribution": {
            "kind": "primary_content",
            "section": "Claim",
            "start_line": 1,
            "end_line": 2,
            "text_sha256": SHA_B,
        },
    }


def evaluator() -> dict[str, str]:
    return {"id": "reviewed-profile", "version": "1", "profile_sha256": SHA_C}


def check(*, disposition: str = "pass", refs: list[dict[str, object]] | None = None) -> dict[str, object]:
    return {"code": "reviewed", "disposition": disposition, "source_refs": [] if refs is None else refs}


def empty_context(graph_kind: str = "entities") -> dict[str, object]:
    required = ("entity_admission", "entity_property", "relation") if graph_kind == "entities" else ("definition", "relation")
    context: dict[str, object] = {
        "schema_version": 1,
        "context_kind": "caprmedio.derived_fact_context",
        "graph_kind": graph_kind,
        "source_binding": {
            "source_frontier_sha256": SHA_A,
            "selection_sha256": SHA_B,
            "authority_frontier_sha256": digest([]),
        },
        "provider": {"id": "test-provider", "version": "1", "profile_sha256": SHA_A},
        "authority_sources": [],
        "relation_registry": [],
        "coverage": [
            {
                "fact_class": fact_class,
                "disposition": "complete",
                "selected_result": "empty",
                "candidate_count": 0,
                "admitted_count": 0,
                "source_refs": [],
            }
            for fact_class in sorted(required)
        ],
        "candidates": [],
        "admission_decisions": [],
        "admitted_facts": [],
        "derivations": [],
        "diagnostics": [],
    }
    context["context_sha256"] = digest(context)
    return context


def positive_entity_context() -> dict[str, object]:
    source = source_ref()
    context = empty_context()
    context["authority_sources"] = [source]
    context["source_binding"]["authority_frontier_sha256"] = digest([source])
    candidate: dict[str, object] = {
        "candidate_id": "candidate:entity",
        "fact_class": "entity_admission",
        "payload": {"entity_identity": "Entity"},
        "recognizer": evaluator(),
        "source_ref": source,
    }
    context["candidates"] = [candidate]
    decision: dict[str, object] = {
        "candidate_id": candidate["candidate_id"],
        "disposition": "admitted",
        "evaluator": evaluator(),
        "authority_inputs": [source],
        "checks": [check(refs=[source])],
    }
    decision["decision_sha256"] = digest(decision)
    context["admission_decisions"] = [decision]
    context["admitted_facts"] = [{
        "fact_id": "fact:entity",
        "candidate_id": candidate["candidate_id"],
        "fact_class": "entity_admission",
        "payload": {"entity_identity": "Entity"},
        "decision_sha256": decision["decision_sha256"],
    }]
    coverage = context["coverage"]
    assert isinstance(coverage, list)
    for row in coverage:
        if row["fact_class"] == "entity_admission":
            row.update(disposition="complete", selected_result="nonempty", candidate_count=1, admitted_count=1)
    context["context_sha256"] = digest({key: value for key, value in context.items() if key != "context_sha256"})
    return context


def relation_registry(source: dict[str, object]) -> dict[str, object]:
    row: dict[str, object] = {
        "kind": {"graph_kind": "entities", "canonical_name": "IS_BORNE_BY"},
        "metadata": {
            "meaning": "one bearer relation",
            "direction": "source-to-target",
            "inverse": {"kind": "declared", "graph_kind": "entities", "canonical_name": "BEARS"},
            "source_class": "Entity",
            "target_class": "Entity",
            "source_graph_context": "entities",
            "target_graph_context": "entities",
            "cardinality": "many-to-one",
            "authority_effect": "derived",
            "transitivity": "none",
            "applicability": "entities",
            "status": "Active",
            "exclusive_purpose": "bearing",
        },
        "authority_inputs": [source],
        "evaluator": evaluator(),
        "checks": [check(refs=[source])],
    }
    row["registry_record_sha256"] = digest(row)
    return row


class FactContextContractTests(unittest.TestCase):
    def assert_rejected(self, context: dict[str, object], code: str | None = None) -> None:
        with self.assertRaises(contract.ContractError) as raised:
            contract.validate_fact_context(context)
        if code is not None:
            self.assertEqual(code, raised.exception.code)
        self.assertNotIn("Entity", str(raised.exception))
        self.assertNotIn("forged-secret", str(raised.exception))

    def test_minimal_explicit_empty_context_is_valid(self) -> None:
        context = empty_context()
        self.assertIsNone(contract.validate_fact_context(context))

    def test_positive_admitted_entity_fact_is_valid(self) -> None:
        self.assertIsNone(contract.validate_fact_context(positive_entity_context()))

    def test_unknown_top_field_is_rejected_without_value_leak(self) -> None:
        context = empty_context()
        context["forged-secret"] = "forged-secret"
        self.assert_rejected(context, "context-schema-invalid")

    def test_duplicate_candidate_identity_is_rejected(self) -> None:
        context = positive_entity_context()
        candidates = context["candidates"]
        assert isinstance(candidates, list)
        candidates.append(copy.deepcopy(candidates[0]))
        self.assert_rejected(context, "candidate-duplicate")

    def test_orphan_decision_is_rejected(self) -> None:
        context = empty_context()
        context["admission_decisions"] = [{
            "candidate_id": "missing",
            "disposition": "rejected",
            "evaluator": evaluator(),
            "authority_inputs": [],
            "checks": [check()],
            "decision_sha256": SHA_A,
        }]
        self.assert_rejected(context, "decision-reference-invalid")

    def test_changed_fact_payload_is_rejected(self) -> None:
        context = positive_entity_context()
        facts = context["admitted_facts"]
        assert isinstance(facts, list)
        facts[0]["payload"] = {"entity_identity": "Changed"}
        self.assert_rejected(context, "fact-payload-mismatch")

    def test_admitted_decision_with_failed_check_is_rejected(self) -> None:
        context = positive_entity_context()
        decisions = context["admission_decisions"]
        assert isinstance(decisions, list)
        decision = decisions[0]
        decision["checks"] = [check(disposition="fail")]
        decision["decision_sha256"] = digest({key: value for key, value in decision.items() if key != "decision_sha256"})
        context["context_sha256"] = digest({key: value for key, value in context.items() if key != "context_sha256"})
        self.assert_rejected(context, "decision-check-failed")

    def test_forged_nested_digest_is_rejected(self) -> None:
        context = positive_entity_context()
        context["context_sha256"] = SHA_A
        self.assert_rejected(context, "context-digest-mismatch")

    def test_forged_authority_frontier_is_rejected_after_context_rehash(self) -> None:
        context = empty_context()
        context["source_binding"]["authority_frontier_sha256"] = SHA_A
        context["context_sha256"] = digest({key: value for key, value in context.items() if key != "context_sha256"})
        self.assert_rejected(context, "source-binding-authority-frontier-mismatch")

    def test_wrong_candidate_sort_is_rejected(self) -> None:
        context = positive_entity_context()
        candidate = copy.deepcopy(context["candidates"][0])
        candidate["candidate_id"] = "candidate:zzz"
        context["candidates"].append(candidate)
        # Keep the record set otherwise coherent; ordering itself is the fault.
        context["candidates"] = list(reversed(context["candidates"]))
        self.assert_rejected(context, "candidate-order-invalid")

    def test_direct_bears_fact_is_rejected_even_with_owner_registry(self) -> None:
        context = positive_entity_context()
        source = context["authority_sources"][0]
        registry = relation_registry(source)
        context["relation_registry"] = [registry]
        payload = {
            "kind": {"graph_kind": "entities", "canonical_name": "BEARS"},
            "registry_record_sha256": registry["registry_record_sha256"],
            "source": {"identity": "Entity", "graph_kind": "entities", "node_class": "Entity"},
            "target": {"identity": "Bearer", "graph_kind": "entities", "node_class": "Entity"},
            "representation": "external_reference",
        }
        candidate = {
            "candidate_id": "candidate:bears",
            "fact_class": "relation",
            "payload": payload,
            "recognizer": evaluator(),
            "source_ref": source,
        }
        context["candidates"].append(candidate)
        decision = {
            "candidate_id": "candidate:bears", "disposition": "admitted", "evaluator": evaluator(),
            "authority_inputs": [source], "checks": [check(refs=[source])],
        }
        decision["decision_sha256"] = digest(decision)
        context["admission_decisions"].append(decision)
        context["admitted_facts"].append({
            "fact_id": "fact:bears", "candidate_id": "candidate:bears", "fact_class": "relation",
            "payload": payload, "decision_sha256": decision["decision_sha256"],
        })
        context["coverage"][-1].update(candidate_count=1, admitted_count=1, selected_result="nonempty", disposition="complete")
        self.assert_rejected(context, "candidate-inverse-direct")

    def test_derivation_cycle_is_rejected(self) -> None:
        context = empty_context()
        source = source_ref()
        context["authority_sources"] = [source]
        context["source_binding"]["authority_frontier_sha256"] = digest([source])
        registry = relation_registry(source)
        context["relation_registry"] = [registry]
        payload = {
            "kind": {"graph_kind": "entities", "canonical_name": "IS_BORNE_BY"},
            "registry_record_sha256": registry["registry_record_sha256"],
            "source": {"identity": "Entity", "graph_kind": "entities", "node_class": "Entity"},
            "target": {"identity": "Bearer", "graph_kind": "entities", "node_class": "Entity"},
            "representation": "external_reference",
        }
        first = {
            "derivation_id": "derivation:a", "fact_class": "relation", "payload": payload,
            "input_fact_ids": ["derivation:b"], "authority_inputs": [source], "evaluator": evaluator(),
            "checks": [check(refs=[source])], "disposition": "admitted",
        }
        second = {
            "derivation_id": "derivation:b", "fact_class": "relation", "payload": payload,
            "input_fact_ids": ["derivation:a"], "authority_inputs": [source], "evaluator": evaluator(),
            "checks": [check(refs=[source])], "disposition": "admitted",
        }
        first["derivation_sha256"] = digest(first)
        second["derivation_sha256"] = digest(second)
        context["derivations"] = [first, second]
        context["coverage"][-1].update(candidate_count=2, admitted_count=2, selected_result="nonempty", disposition="complete")
        context["context_sha256"] = digest({key: value for key, value in context.items() if key != "context_sha256"})
        self.assert_rejected(context, "derivation-cycle")

    def test_diagnostic_details_redaction_boundary_is_recursive(self) -> None:
        for key in ("raw_source", "api_key", "token", "password", "access_token"):
            with self.subTest(key=key):
                context = empty_context()
                secret = "forged-secret-value"
                context["diagnostics"] = [{
                    "code": "provider-detail",
                    "severity": "warning",
                    "source_refs": [],
                    "details": {"nested": {key: secret}},
                }]
                context["context_sha256"] = digest({
                    name: value for name, value in context.items() if name != "context_sha256"
                })
                with self.assertRaises(contract.ContractError) as raised:
                    contract.validate_fact_context(context)
                self.assertEqual("diagnostic-details-redacted", raised.exception.code)
                self.assertNotIn(secret, str(raised.exception))

    def test_diagnostic_details_allow_atom_ids_paths_hashes_and_semantic_names(self) -> None:
        context = empty_context()
        context["diagnostics"] = [{
            "code": "provider-detail",
            "severity": "info",
            "source_refs": [],
            "details": {
                "atom_id": "CA-R-001",
                "carrier_path": "sources/CA-R-001.md",
                "carrier_sha256": SHA_A,
                "semantic_name": "Token",
            },
        }]
        context["context_sha256"] = digest({
            name: value for name, value in context.items() if name != "context_sha256"
        })
        self.assertIsNone(contract.validate_fact_context(context))


if __name__ == "__main__":
    unittest.main()
