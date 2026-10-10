"""Deterministic, create-only consolidation of the candidate review receipts.

This module consumes the nine bounded receipts written by the parallel review
workers.  It validates their mechanical bindings and reuses the already
accepted evidence catalogue; it does not perform a new semantic source audit,
admit a native graph, or mutate the captured Core snapshot.

The command is intentionally dry-run by default.  ``--persist`` creates only
missing consolidated outputs, and ``--verify-output`` checks byte identity.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import hashlib
import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCRIPT = Path(__file__).resolve()
REVIEW_BASE = SCRIPT.parents[2]
REPOSITORY_ROOT = SCRIPT.parents[5]
CONSOLIDATED = REVIEW_BASE / "consolidated"

CANDIDATE_REL = "presentation/operator.entity-graph.candidate.json"
BASELINE_REL = "baseline.inventory.json"
PRIOR_REVIEW_REL = "nodes/nodes.dispositions.json"
SNAPSHOT_CONTEXT_REL = "nodes/snapshot.context.md"
NODES_CONTRACT_REL = "nodes/contract.md"
SCOPE_DIRECTION_REL = "nodes/scope.omission.decision.md"
SOURCE_READER_REL = "nodes/support/snapshot_sources.py"
LEGACY_QUESTIONS_REL = "consolidated/legacy-questions.review.json"
CONSOLIDATED_CONTRACT_REL = "consolidated/contract.md"

EXPECTED_CANDIDATE_SHA256 = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
EXPECTED_BASELINE_SHA256 = "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
EXPECTED_PRIOR_REVIEW_SHA256 = "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"
CAPTURED_CORE_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"

ROOT_ENTITIES = (
    "Artifact",
    "Scope Unit",
    "Actor",
    "Relation",
    "Revision",
    "Carrier",
    "Execution",
)
ACTIONS = {
    "retain",
    "rebase",
    "inherit",
    "delivery_policy",
    "operation_or_method",
    "projection_view",
    "syntax_context",
    "drop_candidate",
    "review_required",
    "concrete_conflict",
}
CONTENT_VIEWS = {"R", "M", "E", "D", "O", "P", "C", "A", "mixed", "unclassified"}
QUESTION_KINDS = {"concrete_conflict", "source_gap", "technical_followup"}
UNRESOLVED_ACTIONS = {"review_required", "concrete_conflict", "syntax_context"}


class ConsolidationError(ValueError):
    """A deterministic input or output preflight failure."""


@dataclasses.dataclass(frozen=True)
class ConsolidationConfig:
    """Filesystem and immutable-input pins for one consolidation run.

    The production defaults are deliberately strict.  Tests may use another
    base directory and a smaller batch tuple, but must opt into those values
    explicitly instead of weakening the CLI defaults.
    """

    base_dir: Path = REVIEW_BASE
    reviews_dir: Path | None = None
    batches: tuple[int, ...] = tuple(range(9))
    expected_identity_count: int = 706
    expected_candidate_sha256: str | None = EXPECTED_CANDIDATE_SHA256
    expected_baseline_sha256: str | None = EXPECTED_BASELINE_SHA256
    expected_prior_review_sha256: str | None = EXPECTED_PRIOR_REVIEW_SHA256
    captured_core_commit: str = CAPTURED_CORE_COMMIT

    @property
    def review_dir(self) -> Path:
        return self.reviews_dir or self.base_dir / "consolidated/reviews"


@dataclasses.dataclass
class ConsolidatedInputs:
    config: ConsolidationConfig
    candidate: dict[str, Any]
    candidate_raw: bytes
    baseline: dict[str, Any]
    baseline_raw: bytes
    prior_review: dict[str, Any]
    prior_review_raw: bytes
    legacy_questions: dict[str, Any]
    legacy_questions_raw: bytes
    prior_marks: dict[str, dict[str, Any]]
    evidence_catalogue: dict[str, dict[str, Any]]
    baseline_identities: set[str]
    allowed_source_atom_ids: dict[str, set[str]]
    input_data: list[dict[str, Any]]
    input_raw: list[bytes]
    input_paths: list[Path]
    reviews: list[dict[str, Any]]
    review_raw: list[bytes]
    review_paths: list[Path]
    snapshot_pins: dict[str, dict[str, Any]]
    source_cache: dict[str, bytes]
    snapshot_reader: Any


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_json(value: Any) -> bytes:
    """Stable JSON bytes for partition and manifest hashes."""

    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ConsolidationError(f"cannot canonicalize JSON: {exc}") from exc


def pretty_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ConsolidationError(message)


def _assert_no_symlink(path: Path, label: str) -> None:
    """Reject symlink routes and outputs before any read or write decision."""

    path = Path(path)
    # System temporary directories on macOS commonly pass through /var ->
    # /private/var.  The controlled route/output itself is the security
    # boundary; rejecting unrelated system-parent links would make harmless
    # temporary test roots unusable.
    if path.is_symlink():
        raise ConsolidationError(f"{label} is a symlink: {path}")


def _assert_regular(path: Path, label: str, *, allow_missing: bool = False) -> None:
    _assert_no_symlink(path, label)
    if not path.exists():
        if allow_missing:
            return
        raise ConsolidationError(f"missing {label}: {path}")
    _require(path.is_file(), f"{label} is not a regular file: {path}")


def _read_json(path: Path, label: str) -> tuple[dict[str, Any], bytes]:
    _assert_regular(path, label)
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"), parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise ConsolidationError(f"invalid JSON in {label}: {path}: {exc}") from exc
    _require(isinstance(value, dict), f"{label} must be a JSON object: {path}")
    return value, raw


def _relative_to_repo(path: Path) -> str:
    try:
        return path.relative_to(REPOSITORY_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _load_snapshot_reader(config: ConsolidationConfig) -> Any:
    path = config.base_dir / SOURCE_READER_REL
    _assert_regular(path, "captured snapshot reader")
    spec = importlib.util.spec_from_file_location("core_entity_review_snapshot_sources", path)
    _require(spec is not None and spec.loader is not None, f"cannot load snapshot reader: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _require(getattr(module, "COMMIT", None) == config.captured_core_commit, "captured Core commit pin mismatch")
    return module


def _validate_candidate(candidate: dict[str, Any]) -> None:
    roots = candidate.get("root_entities")
    _require(isinstance(roots, list), "candidate root_entities must be a list")
    names = [item.get("name") for item in roots if isinstance(item, dict)]
    _require(len(names) == len(roots), "candidate root_entities entries must be objects with names")
    _require(len(names) == len(ROOT_ENTITIES), "candidate must contain exactly seven root entities")
    _require(len(set(names)) == len(names), "candidate root entity names must be unique")
    _require(set(names) == set(ROOT_ENTITIES), f"candidate roots differ from allowed seven: {names!r}")
    _require(candidate.get("status") == "Candidate", "candidate status must remain Candidate")


def _load_inputs(config: ConsolidationConfig) -> ConsolidatedInputs:
    base = config.base_dir
    _assert_no_symlink(base, "consolidation route")
    _require(base.is_dir(), f"consolidation base is not a directory: {base}")
    _assert_no_symlink(config.review_dir, "review route")
    _require(config.review_dir.is_dir(), f"review route is not a directory: {config.review_dir}")

    candidate_path = base / CANDIDATE_REL
    candidate, candidate_raw = _read_json(candidate_path, "candidate")
    candidate_hash = sha256(candidate_raw)
    if config.expected_candidate_sha256 is not None:
        _require(candidate_hash == config.expected_candidate_sha256, "candidate SHA-256 mismatch")
    _validate_candidate(candidate)

    baseline_path = base / BASELINE_REL
    baseline, baseline_raw = _read_json(baseline_path, "baseline inventory")
    baseline_hash = sha256(baseline_raw)
    if config.expected_baseline_sha256 is not None:
        _require(baseline_hash == config.expected_baseline_sha256, "baseline file SHA-256 mismatch")
    expected_inventory_hash = sha256(canonical_json({k: v for k, v in baseline.items() if k != "inventory_sha256"}))
    _require(baseline.get("inventory_sha256") == expected_inventory_hash, "baseline canonical inventory hash mismatch")
    baseline_nodes = baseline.get("nodes")
    _require(isinstance(baseline_nodes, list), "baseline nodes must be a list")
    baseline_identities = [node.get("identity") for node in baseline_nodes if isinstance(node, dict)]
    _require(len(baseline_identities) == len(baseline_nodes), "baseline nodes must contain identity objects")
    _require(len(set(baseline_identities)) == len(baseline_identities), "baseline contains duplicate identities")
    _require(len(baseline_identities) == config.expected_identity_count, "baseline identity count mismatch")

    prior_path = base / PRIOR_REVIEW_REL
    prior_review, prior_review_raw = _read_json(prior_path, "accepted disposition ledger")
    prior_hash = sha256(prior_review_raw)
    if config.expected_prior_review_sha256 is not None:
        _require(prior_hash == config.expected_prior_review_sha256, "accepted disposition ledger SHA-256 mismatch")
    marks = prior_review.get("node_disposition_marks")
    _require(isinstance(marks, list), "accepted node disposition marks must be a list")
    _require(len(marks) == config.expected_identity_count, "accepted disposition identity count mismatch")
    prior_marks: dict[str, dict[str, Any]] = {}
    for mark in marks:
        _require(isinstance(mark, dict), "accepted disposition mark must be an object")
        identity = mark.get("identity")
        row = mark.get("review_row")
        _require(isinstance(identity, str) and identity, "accepted disposition mark identity missing")
        _require(identity not in prior_marks, f"duplicate accepted disposition identity: {identity}")
        _require(isinstance(row, dict) and row.get("identity") == identity, f"accepted row identity mismatch: {identity}")
        _require(isinstance(row.get("disposition"), str) and row["disposition"], f"accepted disposition missing: {identity}")
        prior_marks[identity] = mark
    _require(set(prior_marks) == set(baseline_identities), "accepted dispositions do not cover baseline exactly")

    catalogue = prior_review.get("evidence_catalogue")
    _require(isinstance(catalogue, dict), "accepted evidence catalogue must be an object")
    _require(all(isinstance(k, str) and isinstance(v, dict) for k, v in catalogue.items()), "invalid evidence catalogue entry")

    snapshot = _load_snapshot_reader(config)
    try:
        pins = dict(snapshot.source_pins())
    except Exception as exc:  # pragma: no cover - exact exception is reader-owned
        raise ConsolidationError(f"cannot load captured source pins: {exc}") from exc
    _require(pins, "captured source pin catalogue is empty")

    legacy_path = base / LEGACY_QUESTIONS_REL
    legacy_questions, legacy_questions_raw = _read_json(legacy_path, "legacy question review")
    _require(legacy_questions.get("non_authoritative") is True, "legacy question review must be non-authoritative")
    _require(legacy_questions.get("native_admission") == "not_performed", "legacy question review native boundary changed")
    _require(legacy_questions.get("source_migration") == "not_performed", "legacy question review migration boundary changed")
    _require(legacy_questions.get("candidate", {}).get("sha256") == candidate_hash, "legacy question candidate pin mismatch")
    legacy_cases = legacy_questions.get("cases")
    _require(isinstance(legacy_cases, list) and len(legacy_cases) == 47, "legacy question coverage must contain 47 cases")
    _require(legacy_questions.get("legacy_case_count") == 47, "legacy question count declaration mismatch")
    _require(legacy_questions.get("operator_questions_from_legacy_wording") == 0, "legacy question review established an unclassified Operator question")

    input_data: list[dict[str, Any]] = []
    input_raw: list[bytes] = []
    input_paths: list[Path] = []
    input_identity_sets: list[set[str]] = []
    for batch in config.batches:
        path = base / f"nodes/inputs/nodes.batch-{batch}.input.json"
        value, raw = _read_json(path, f"batch {batch} input")
        _require(value.get("batch") == batch, f"batch input number mismatch: {path}")
        nodes = value.get("nodes")
        _require(isinstance(nodes, list), f"batch {batch} input nodes must be a list")
        identities = [node.get("identity") for node in nodes if isinstance(node, dict)]
        _require(len(identities) == len(nodes), f"batch {batch} input contains malformed node")
        _require(len(set(identities)) == len(identities), f"batch {batch} input has duplicate identity")
        _require(set(identities) <= set(baseline_identities), f"batch {batch} input has identity outside baseline")
        partition = value.get("partition_sha256")
        _require(isinstance(partition, str), f"batch {batch} input partition hash missing")
        _require(partition == sha256(canonical_json({k: v for k, v in value.items() if k != "partition_sha256"})), f"batch {batch} partition hash mismatch")
        baseline_ref = value.get("baseline")
        if isinstance(baseline_ref, dict):
            _require(baseline_ref.get("sha256") == baseline_hash, f"batch {batch} baseline file pin mismatch")
            _require(baseline_ref.get("inventory_sha256") == baseline.get("inventory_sha256"), f"batch {batch} baseline inventory pin mismatch")
        input_data.append(value)
        input_raw.append(raw)
        input_paths.append(path)
        input_identity_sets.append(set(identities))

    for left_index, left in enumerate(input_identity_sets):
        for right in input_identity_sets[left_index + 1 :]:
            _require(left.isdisjoint(right), "batch inputs are not disjoint")
    union = set().union(*input_identity_sets) if input_identity_sets else set()
    _require(union == set(baseline_identities), "batch inputs do not cover baseline exactly")

    allowed_source_atom_ids: dict[str, set[str]] = {}
    for value in input_data:
        for node in value["nodes"]:
            identity = node["identity"]
            allowed: set[str] = set()
            for field in ("source_atom_ids", "governing_source_atom_ids"):
                source_ids = node.get(field)
                _require(isinstance(source_ids, list), f"input node {identity} {field} must be a list")
                _require(
                    all(isinstance(atom_id, str) and atom_id for atom_id in source_ids),
                    f"input node {identity} {field} contains an invalid source atom ID",
                )
                allowed.update(source_ids)
            mark = prior_marks[identity]
            for label, accepted in (
                ("source_review", mark.get("source_review")),
                ("review_row", mark["review_row"]),
            ):
                if accepted is None:
                    continue
                _require(isinstance(accepted, dict), f"accepted {label} for {identity} must be an object")
                source_ids = accepted.get("checked_source_atom_ids", [])
                _require(isinstance(source_ids, list), f"accepted {label} for {identity} checked source IDs must be a list")
                _require(
                    all(isinstance(atom_id, str) and atom_id for atom_id in source_ids),
                    f"accepted {label} for {identity} contains an invalid source atom ID",
                )
                allowed.update(source_ids)
            allowed_source_atom_ids[identity] = allowed

    reviews: list[dict[str, Any]] = []
    review_raw: list[bytes] = []
    review_paths: list[Path] = []
    source_cache: dict[str, bytes] = {}
    loaded = ConsolidatedInputs(
        config=config,
        candidate=candidate,
        candidate_raw=candidate_raw,
        baseline=baseline,
        baseline_raw=baseline_raw,
        prior_review=prior_review,
        prior_review_raw=prior_review_raw,
        legacy_questions=legacy_questions,
        legacy_questions_raw=legacy_questions_raw,
        prior_marks=prior_marks,
        evidence_catalogue=catalogue,
        baseline_identities=set(baseline_identities),
        allowed_source_atom_ids=allowed_source_atom_ids,
        input_data=input_data,
        input_raw=input_raw,
        input_paths=input_paths,
        reviews=reviews,
        review_raw=review_raw,
        review_paths=review_paths,
        snapshot_pins=pins,
        source_cache=source_cache,
        snapshot_reader=snapshot,
    )
    for index, batch in enumerate(config.batches):
        path = config.review_dir / f"batch-{batch}.review.json"
        review, raw = _read_json(path, f"batch {batch} review")
        _validate_review_header(review, batch, input_raw[index], loaded)
        _validate_review_rows(review, batch, input_data[index], loaded)
        expected = {node["identity"] for node in input_data[index]["nodes"]}
        actual = [row.get("identity") for row in review.get("nodes", []) if isinstance(row, dict)]
        _require(len(actual) == len(set(actual)), f"batch {batch} review has duplicate identity")
        _require(set(actual) == expected, f"batch {batch} review identity coverage mismatch")
        reviews.append(review)
        review_raw.append(raw)
        review_paths.append(path)
    loaded.reviews = reviews
    loaded.review_raw = review_raw
    loaded.review_paths = review_paths
    all_review_ids = [row.get("identity") for review in reviews for row in review.get("nodes", [])]
    _require(len(all_review_ids) == config.expected_identity_count, "consolidated review identity count mismatch")
    _require(len(set(all_review_ids)) == len(all_review_ids), "consolidated reviews overlap")
    _require(set(all_review_ids) == loaded.baseline_identities, "consolidated reviews do not cover baseline exactly")
    return loaded


def _validate_review_header(review: dict[str, Any], batch: int, input_raw: bytes, loaded: ConsolidatedInputs) -> None:
    required = {
        "schema_version",
        "batch",
        "kind",
        "non_authoritative",
        "native_admission",
        "source_migration",
        "captured_core_commit",
        "candidate_sha256",
        "input_sha256",
        "baseline_sha256",
        "prior_review_sha256",
        "review_method",
        "nodes",
    }
    _require(required <= set(review), f"batch {batch} review is missing receipt fields")
    _require(review["schema_version"] == 1, f"batch {batch} review schema version mismatch")
    _require(review["batch"] == batch, f"batch {batch} review number mismatch")
    _require(review["kind"] == "Captured nodes against Operator candidate", f"batch {batch} review kind mismatch")
    _require(review["non_authoritative"] is True, f"batch {batch} review must be non-authoritative")
    _require(review["native_admission"] == "not_performed", f"batch {batch} review native admission boundary changed")
    _require(review["source_migration"] == "not_performed", f"batch {batch} review source migration boundary changed")
    _require(review["captured_core_commit"] == loaded.config.captured_core_commit, f"batch {batch} captured commit mismatch")
    _require(review["candidate_sha256"] == sha256(loaded.candidate_raw), f"batch {batch} candidate pin mismatch")
    _require(review["input_sha256"] == sha256(input_raw), f"batch {batch} input SHA-256 mismatch")
    _require(review["baseline_sha256"] == sha256(loaded.baseline_raw), f"batch {batch} baseline pin mismatch")
    _require(review["prior_review_sha256"] == sha256(loaded.prior_review_raw), f"batch {batch} prior review pin mismatch")
    method = review["review_method"]
    _require(isinstance(method, str) and method.strip(), f"batch {batch} review method missing")
    method_lower = method.lower()
    _require("captured" in method_lower and "operator" in method_lower, f"batch {batch} review method lacks snapshot/operator boundary")
    def positive_current_core_claim(text: str) -> bool:
        for match in re.finditer(r"\bcurrent[- ]core\b", text):
            prefix = text[max(0, match.start() - 90) : match.start()]
            if re.search(r"\b(?:not|no|without|never|does\s+not|doesn't)\b[^.!?]{0,70}$", prefix):
                continue
            return True
        return False

    _require(not positive_current_core_claim(method_lower), f"batch {batch} review overclaims current Core")

    def positive_audit_claim(text: str) -> bool:
        patterns = (
            r"\bfresh\s+(?:exhaustive|complete|full)\b",
            r"\b(?:exhaustive|complete|full)\s+(?:audit|review)\s+of\s+(?:all\s+)?951",
            r"\ball\s+951\s+sources?\b",
        )
        for pattern in patterns:
            for match in re.finditer(pattern, text):
                prefix = text[max(0, match.start() - 100) : match.start()]
                if re.search(r"\b(?:not|no|without|never|does\s+not|doesn't)\b[^.!?]{0,70}$", prefix):
                    continue
                return True
        return False

    _require(not positive_audit_claim(method_lower), f"batch {batch} review overclaims source audit")
    _require(isinstance(review["nodes"], list), f"batch {batch} review nodes must be a list")


def _source_bytes(atom_id: str, loaded: ConsolidatedInputs) -> bytes:
    if atom_id in loaded.source_cache:
        return loaded.source_cache[atom_id]
    pin = loaded.snapshot_pins.get(atom_id)
    _require(isinstance(pin, dict), f"unknown captured source atom ID: {atom_id}")
    reader = loaded.snapshot_reader
    try:
        raw = reader.read_source(atom_id)
    except Exception as exc:  # pragma: no cover - reader's subprocess error varies
        raise ConsolidationError(f"captured source read failed for {atom_id}: {exc}") from exc
    _require(isinstance(raw, bytes), f"captured source reader returned non-bytes for {atom_id}")
    _require(sha256(raw) == pin.get("carrier_sha256"), f"captured source SHA-256 mismatch: {atom_id}")
    loaded.source_cache[atom_id] = raw
    return raw


def _validate_evidence_ref(ref: str, batch: int, checked_ids: set[str], loaded: ConsolidatedInputs) -> None:
    _require(ref in loaded.evidence_catalogue, f"batch {batch} evidence ref is not in accepted catalogue: {ref}")
    # Old catalogue keys are globally namespaced by the original task/batch.
    _require(f"/batch-{batch}/" in ref, f"batch {batch} evidence ref is owned by another batch: {ref}")
    item = loaded.evidence_catalogue[ref]
    for field in ("atom_id", "atom_revision", "carrier_path", "carrier_sha256", "start_line", "end_line", "quote", "text_sha256"):
        _require(field in item, f"evidence {ref} lacks {field}")
    atom_id = item["atom_id"]
    _require(atom_id in checked_ids, f"evidence {ref} atom is absent from checked_source_atom_ids")
    pin = loaded.snapshot_pins.get(atom_id)
    _require(isinstance(pin, dict), f"evidence {ref} names unknown source atom: {atom_id}")
    for field in ("atom_revision", "carrier_path", "carrier_sha256"):
        _require(item[field] == pin.get(field), f"evidence {ref} source pin mismatch in {field}")
    _require(type(item["start_line"]) is int and type(item["end_line"]) is int, f"evidence {ref} line span must be integer")
    raw = _source_bytes(atom_id, loaded)
    try:
        lines = raw.decode("utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise ConsolidationError(f"evidence source is not UTF-8: {atom_id}") from exc
    start, end = item["start_line"], item["end_line"]
    _require(1 <= start <= end <= len(lines), f"evidence {ref} line span is outside captured source")
    frontmatter_end = next((index for index, line in enumerate(lines[1:], 2) if line == "---"), None)
    _require(frontmatter_end is not None and start > frontmatter_end, f"evidence {ref} points into frontmatter")
    quote = item["quote"]
    _require(isinstance(quote, str) and quote.strip(), f"evidence {ref} quote is empty")
    span = "\n".join(lines[start - 1 : end])
    _require(quote == span, f"evidence {ref} quote does not exactly match captured line span")
    _require(item["text_sha256"] == sha256(quote.encode("utf-8")), f"evidence {ref} quote hash mismatch")
    headings = [line for line in lines[:start] if line.startswith(("# ", "## ", "### "))]
    _require(headings and not headings[-1].startswith("# Summary"), f"evidence {ref} is Summary-only")
    standard_content = any(
        line.startswith(("## Claim", "## Scope", "## Details", "## Operation", "## Procedure", "## Condition", "## Evaluation", "## Definition"))
        for line in headings
    )
    legacy_body = (
        any(line.startswith("# ") and line != "# Summary" for line in headings)
        and "# Summary" not in lines
        and not lines[start - 1].startswith("#")
    )
    _require(standard_content or legacy_body, f"evidence {ref} lacks pertinent Main Content heading")


def _validate_question(question: Any, identity: str) -> dict[str, str] | None:
    if question is None:
        return None
    _require(isinstance(question, dict), f"node {identity} question must be null or object")
    _require(question.get("kind") in QUESTION_KINDS, f"node {identity} question kind is unknown")
    _require(isinstance(question.get("text"), str) and question["text"].strip(), f"node {identity} question text missing")
    return {"kind": question["kind"], "text": question["text"]}


def _validate_candidate_path(root: str | None, path: Any, identity: str) -> None:
    if root is None:
        _require(path is None, f"node {identity} has a candidate_path without candidate_root")
        return
    # A root-only classification is useful for delivery policies and other
    # view/context rows.  A non-null path is only a human display proposal;
    # the contract deliberately does not make it a native root-relative edge.
    if path is None:
        return
    _require(isinstance(path, str) and path.strip(), f"node {identity} candidate_path is empty")


def _validate_review_rows(review: dict[str, Any], batch: int, input_data: dict[str, Any], loaded: ConsolidatedInputs) -> None:
    input_by_identity = {node["identity"]: node for node in input_data["nodes"]}
    for row in review["nodes"]:
        _require(isinstance(row, dict), f"batch {batch} review row must be an object")
        identity = row.get("identity")
        _require(isinstance(identity, str) and identity in input_by_identity, f"batch {batch} row identity is missing or outside input: {identity!r}")
        required = {"identity", "prior_disposition", "action", "candidate_root", "candidate_path", "content_view", "confidence_percent", "reason", "operator_rules", "evidence_refs", "checked_source_atom_ids", "preserved_distinctions", "question"}
        _require(required <= set(row), f"batch {batch} row {identity} is missing fields")
        prior = loaded.prior_marks[identity]["review_row"]["disposition"]
        _require(row["prior_disposition"] == prior, f"batch {batch} row {identity} prior disposition mismatch")
        _require(row["action"] in ACTIONS, f"batch {batch} row {identity} action is unknown: {row['action']!r}")
        root = row["candidate_root"]
        _require(root is None or root in ROOT_ENTITIES, f"batch {batch} row {identity} candidate_root is unknown: {root!r}")
        _require(row["content_view"] in CONTENT_VIEWS, f"batch {batch} row {identity} content_view is unknown: {row['content_view']!r}")
        _require(type(row["confidence_percent"]) in (int, float) and not isinstance(row["confidence_percent"], bool), f"batch {batch} row {identity} confidence must be numeric")
        _require(0 <= row["confidence_percent"] <= 100, f"batch {batch} row {identity} confidence outside 0..100")
        _require(isinstance(row["reason"], str) and row["reason"].strip(), f"batch {batch} row {identity} reason missing")
        reason_lower = row["reason"].lower()
        _require(not any(fragment in reason_lower for fragment in ("all slash paths", "all labels are meaningless", "all old nodes disappear")), f"batch {batch} row {identity} uses a blanket reason")
        rules = row["operator_rules"]
        _require(isinstance(rules, (list, dict)), f"batch {batch} row {identity} operator_rules must be a list or object")
        if isinstance(rules, list):
            _require(all(isinstance(rule, str) and rule.strip() for rule in rules), f"batch {batch} row {identity} operator_rules contains a non-string")
        else:
            _require(all(isinstance(key, str) and key.strip() for key in rules), f"batch {batch} row {identity} operator_rules has an invalid key")
        _validate_candidate_path(root, row["candidate_path"], identity)
        evidence_refs = row["evidence_refs"]
        _require(isinstance(evidence_refs, list), f"batch {batch} row {identity} evidence_refs must be a list")
        _require(len(set(evidence_refs)) == len(evidence_refs), f"batch {batch} row {identity} repeats an evidence ref")
        checked = row["checked_source_atom_ids"]
        _require(isinstance(checked, list) and checked and all(isinstance(atom, str) and atom for atom in checked), f"batch {batch} row {identity} checked_source_atom_ids is empty or malformed")
        _require(len(set(checked)) == len(checked), f"batch {batch} row {identity} repeats a checked source atom")
        checked_set = set(checked)
        for atom_id in checked:
            _require(
                atom_id in loaded.allowed_source_atom_ids[identity],
                f"batch {batch} row {identity} checked source atom is not allowed for this identity: {atom_id}",
            )
            _source_bytes(atom_id, loaded)
        for ref in evidence_refs:
            _require(isinstance(ref, str), f"batch {batch} row {identity} evidence ref is not a string")
            _validate_evidence_ref(ref, batch, checked_set, loaded)
        distinctions = row["preserved_distinctions"]
        _require(isinstance(distinctions, list) and all(isinstance(item, str) and item.strip() for item in distinctions), f"batch {batch} row {identity} preserved_distinctions malformed")
        question = _validate_question(row["question"], identity)
        confidence = row["confidence_percent"]
        action = row["action"]
        if confidence < 90:
            _require(action in {"review_required", "concrete_conflict"}, f"batch {batch} row {identity} low confidence has a committed action")
            _require(root is None and row["candidate_path"] is None, f"batch {batch} row {identity} low confidence has a candidate mapping")
        if action in UNRESOLVED_ACTIONS:
            _require(root is None and row["candidate_path"] is None, f"batch {batch} row {identity} unresolved action has a candidate mapping")
        if action == "concrete_conflict":
            _require(question is not None and question["kind"] == "concrete_conflict", f"batch {batch} row {identity} concrete conflict lacks concrete question")
        if question is not None and question["kind"] == "concrete_conflict":
            _require(root is None and row["candidate_path"] is None, f"batch {batch} row {identity} concrete question has a committed mapping")
        if confidence >= 90 and action not in UNRESOLVED_ACTIONS:
            _require(evidence_refs, f"batch {batch} row {identity} confident action lacks evidence")


def _source_pin(path: Path, kind: str) -> dict[str, Any]:
    _assert_regular(path, kind)
    raw = path.read_bytes()
    return {"kind": kind, "path": _relative_to_repo(path), "bytes": len(raw), "sha256": sha256(raw)}


def _candidate_root_map(candidate: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["name"]: item for item in candidate.get("root_entities", []) if isinstance(item, dict) and isinstance(item.get("name"), str)}


def _text(value: Any, fallback: str = "not specified in candidate") -> str:
    if isinstance(value, str):
        return value.replace("\n", " ").strip() or fallback
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return "; ".join(_text(item, "") for item in value if _text(item, "")) or fallback
    if isinstance(value, dict):
        return "; ".join(f"{key}: {_text(item, '')}" for key, item in value.items() if _text(item, "")) or fallback
    return fallback


def _build_nodes_output(loaded: ConsolidatedInputs) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    node_batches: list[dict[str, Any]] = []
    counts = collections.Counter()
    roots = collections.Counter()
    views = collections.Counter()
    prior = collections.Counter()
    questions = collections.Counter()
    root_classifications = 0
    display_path_proposals = 0
    for batch, review in zip(loaded.config.batches, loaded.reviews):
        identities: list[str] = []
        for row in review["nodes"]:
            rows.append(row)
            identities.append(row["identity"])
            counts[row["action"]] += 1
            roots[row["candidate_root"] or "unmapped"] += 1
            root_classifications += row["candidate_root"] is not None
            display_path_proposals += row["candidate_path"] is not None
            views[row["content_view"]] += 1
            prior[row["prior_disposition"]] += 1
            if row["question"] is not None:
                questions[row["question"]["kind"]] += 1
        node_batches.append({"batch": batch, "identity_count": len(identities), "identities": sorted(identities)})
    rows.sort(key=lambda row: row["identity"])
    input_pins = []
    for batch, path, raw, value in zip(loaded.config.batches, loaded.input_paths, loaded.input_raw, loaded.input_data):
        input_pins.append({
            "batch": batch,
            "path": _relative_to_repo(path),
            "bytes": len(raw),
            "sha256": sha256(raw),
            "partition_sha256": value["partition_sha256"],
            "identity_count": len(value["nodes"]),
        })
    review_pins = []
    for batch, path, raw, review in zip(loaded.config.batches, loaded.review_paths, loaded.review_raw, loaded.reviews):
        review_pins.append({
            "batch": batch,
            "path": _relative_to_repo(path),
            "bytes": len(raw),
            "sha256": sha256(raw),
            "identity_count": len(review["nodes"]),
        })
    source_pins = {
        "candidate": _source_pin(loaded.config.base_dir / CANDIDATE_REL, "operator_candidate"),
        "baseline": _source_pin(loaded.config.base_dir / BASELINE_REL, "captured_baseline_inventory"),
        "prior_review": _source_pin(loaded.config.base_dir / PRIOR_REVIEW_REL, "accepted_disposition_ledger"),
        "snapshot_context": _source_pin(loaded.config.base_dir / SNAPSHOT_CONTEXT_REL, "captured_snapshot_context"),
        "nodes_contract": _source_pin(loaded.config.base_dir / NODES_CONTRACT_REL, "captured_review_contract"),
        "scope_direction": _source_pin(loaded.config.base_dir / SCOPE_DIRECTION_REL, "operator_scope_direction"),
        "source_reader": _source_pin(loaded.config.base_dir / SOURCE_READER_REL, "captured_snapshot_source_reader"),
        "legacy_questions": _source_pin(loaded.config.base_dir / LEGACY_QUESTIONS_REL, "legacy_question_review"),
        "consolidated_contract": _source_pin(loaded.config.base_dir / CONSOLIDATED_CONTRACT_REL, "consolidated_review_contract"),
        "compiler_recipe": _source_pin(SCRIPT, "consolidator_compiler_recipe"),
    }
    return {
        "schema_version": 1,
        "kind": "Consolidated candidate review",
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "mapping_boundary": "candidate_root and candidate_path are reviewer display proposals, not native edges, selectors, or replacement identities",
        "source_context": {
            "kind": "captured_snapshot",
            "git_commit": loaded.config.captured_core_commit,
            "current_core_claimed": False,
            "captured_snapshot_receipt": {"source_pins_checked": 951, "performed_by": "captured snapshot verification"},
            "evidence_source_atoms_checked": len(loaded.source_cache),
            "evidence_catalogue_reused": True,
        },
        "candidate_sha256": sha256(loaded.candidate_raw),
        "baseline_sha256": sha256(loaded.baseline_raw),
        "baseline_inventory_sha256": loaded.baseline["inventory_sha256"],
        "prior_review_sha256": sha256(loaded.prior_review_raw),
        "source_pins": source_pins,
        "input_pins": input_pins,
        "review_pins": review_pins,
        "node_batches": node_batches,
        "nodes": rows,
        "counts": {
            "nodes": len(rows),
            "actions": dict(sorted(counts.items())),
            "candidate_roots": dict(sorted(roots.items())),
            "content_views": dict(sorted(views.items())),
            "prior_dispositions": dict(sorted(prior.items())),
            "questions": dict(sorted(questions.items())),
            "root_classifications": root_classifications,
            "display_path_proposals": display_path_proposals,
        },
        "limits": [
            "Derived comparison only; no Core, Subject, relation, or native graph admission was performed.",
            "The old vetted evidence catalogue is reused; this is not a fresh exhaustive audit of all 951 source pins.",
            "Candidate paths are display proposals, not executable selectors or replacement identities.",
        ],
    }


def _build_graph_text(loaded: ConsolidatedInputs) -> bytes:
    candidate = loaded.candidate
    roots = _candidate_root_map(candidate)
    atom_root = next((item for item in roots["Artifact"].get("narrower_entities", []) if item.get("name") == "Atom"), {})
    examples = atom_root.get("named_dependent_entity_examples") or ["Summary", "Status", "Substance", "Version Number", "Updated At"]
    scope_root = roots["Scope Unit"]
    lines = [
        "# Candidate entity graph display (derived, non-authoritative)",
        "# Captured snapshot comparison only; indentation is display notation, not native admission.",
        "",
        "candidate_graph:",
        "  non_authoritative: true",
        "  roots:",
    ]
    for name in ROOT_ENTITIES:
        lines.append(f"    {name}:")
        lines.append(f"      meaning: {_text(roots[name].get('meaning'))}")
        if name == "Artifact":
            lines.append("      / Atom:")
            lines.append("        kind: Artifact-kind Entity")
            lines.append("        lifecycle: one governed lifecycle; dependent Entities do not have independent lifecycles")
            lines.append("        dependent_entities:")
            lines.extend(f"          .{example}: named dependent Entity example" for example in examples)
            lines.append("        notation_boundary: '/' and '.' are display grouping only, not native relations")
        elif name == "Scope Unit":
            owned = scope_root.get("owned_entity_kinds") or ["Atom", "Scope Unit"]
            lines.append("      owns (candidate descriptive boundary):")
            lines.extend(f"        - {item}" for item in owned)
    dependent = candidate.get("dependent_entities", {})
    identity = candidate.get("entity_identity_model", {})
    content = candidate.get("content_direction", {})
    carrier = candidate.get("carrier_delivery_model", {})
    history = candidate.get("history_model", {})
    atom_versioning = candidate.get("atom_versioning", {})
    methodology = candidate.get("applicable_methodology", {})
    lines.extend(
        [
            "",
            "  selected_confirmed_decisions:",
            f"    inheritance: {_text(dependent.get('meaning'))}",
            f"    identity.scope_unit: {_text(identity.get('scope_unit'))}",
            f"    identity.dependent_entity: {_text(identity.get('dependent_entity', {}).get('operator_example'))}",
            f"    substance: {_text(content.get('umbrella'))}",
            f"    substance_scope_omission: {_text(content.get('scope_omission'))}",
            f"    rmed_views: {_text(content.get('role_labels'))}",
            f"    delivery_policy: {_text(carrier.get('decision'))}",
            f"    atom_versioning: {_text(atom_versioning.get('trigger'))}",
            f"    revision: {_text(history.get('revision_role'))}",
            f"    journal: {_text(history.get('journal_role'))}",
            "  boundary: display grouping and paths are not native relations; adoption and migration remain unperformed.",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def _build_summary_text(loaded: ConsolidatedInputs) -> bytes:
    all_rows = [row for review in loaded.reviews for row in review["nodes"]]
    action_counts = collections.Counter(row["action"] for row in all_rows)
    root_counts = collections.Counter(row["candidate_root"] or "unmapped" for row in all_rows)
    view_counts = collections.Counter(row["content_view"] for row in all_rows)
    root_classifications = sum(row["candidate_root"] is not None for row in all_rows)
    display_path_proposals = sum(row["candidate_path"] is not None for row in all_rows)
    concrete = []
    backlog = []
    for row in sorted(all_rows, key=lambda row: row["identity"]):
        question = row["question"]
        if not question:
            if row["action"] in {"review_required", "concrete_conflict"} or row["confidence_percent"] < 90:
                backlog.append(f"- {row['identity']} [review_required]: {row['reason']}")
            continue
        item = f"- {row['identity']}: {question['text']}"
        if question["kind"] == "concrete_conflict":
            concrete.append(item)
        else:
            backlog.append(f"- {row['identity']} [{question['kind']}]: {question['text']}")
    lines = [
        "CONSOLIDATED CANDIDATE REVIEW",
        "Derived, non-authoritative comparison against the captured snapshot.",
        "",
        f"Coverage: {len(all_rows)} identities across {len(loaded.reviews)} disjoint batches; baseline and old inputs match exactly.",
        f"Candidate SHA-256: {sha256(loaded.candidate_raw)}",
        f"Baseline file SHA-256: {sha256(loaded.baseline_raw)}",
        f"Accepted disposition ledger SHA-256: {sha256(loaded.prior_review_raw)}",
        f"Captured Core commit: {loaded.config.captured_core_commit}",
        f"Legacy question review: {loaded.legacy_questions.get('legacy_case_count', 0)} preserved cases; {loaded.legacy_questions.get('operator_questions_from_legacy_wording', 0)} inherited Operator questions.",
        f"Referenced evidence source atoms mechanically rechecked: {len(loaded.source_cache)} (captured snapshot receipt records 951 pinned sources).",
        f"Candidate root classifications: {root_classifications}; human display-path proposals: {display_path_proposals} (null paths are not counted as mappings).",
        "",
        "Action counts:",
    ]
    lines.extend(f"- {key}: {action_counts[key]}" for key in sorted(action_counts))
    lines.extend(["", "Candidate-root counts:"])
    lines.extend(f"- {key}: {root_counts[key]}" for key in sorted(root_counts))
    lines.extend(["", "Content-view counts:"])
    lines.extend(f"- {key}: {view_counts[key]}" for key in sorted(view_counts))
    lines.extend(
        [
            "",
            "Known candidate policy changes versus the accepted source review:",
            "- The Operator candidate names seven roots and keeps named dependent Entities inside an Artifact lifecycle.",
            "- Revision is a historical Artifact state; Atom version/history and Journal recording remain distinct decisions.",
            "- Substance covers Claim, Objective, Question, Issue and Operation; Substance Scope omission is limited to the whole Subject and whole owning Scope Unit.",
            "- RMED labels are views, M/E remain distinct from Operation definitions and actual Executions, and D uses general policies rather than per-Property Carrier edges.",
            "- These are candidate directions only; no captured Core identity or native relation is changed here.",
            "",
            "Concrete conflicts for Operator:",
        ]
    )
    lines.extend(concrete or ["- none recorded"])
    lines.extend(["", "Source and technical backlog:"])
    lines.extend(backlog or ["- none recorded"])
    lines.extend(
        [
            "",
            "Evidence boundary:",
            "- Evidence references are owned by the accepted catalogue and were checked against captured bytes, exact line spans and quote hashes.",
            "- The old vetted catalogue is reused; this artifact does not claim a fresh exhaustive audit of all 951 sources.",
            "- Operator directions and candidate display mappings remain separate from captured Core evidence.",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def _build_manifest(loaded: ConsolidatedInputs, outputs: Mapping[str, bytes]) -> bytes:
    inputs: list[dict[str, Any]] = []
    for path, raw in zip(loaded.input_paths, loaded.input_raw):
        inputs.append({"kind": "review_input", "path": _relative_to_repo(path), "bytes": len(raw), "sha256": sha256(raw)})
    for path, raw, kind in (
        (loaded.config.base_dir / CANDIDATE_REL, loaded.candidate_raw, "operator_candidate"),
        (loaded.config.base_dir / BASELINE_REL, loaded.baseline_raw, "captured_baseline_inventory"),
        (loaded.config.base_dir / PRIOR_REVIEW_REL, loaded.prior_review_raw, "accepted_disposition_ledger"),
        (loaded.config.base_dir / LEGACY_QUESTIONS_REL, loaded.legacy_questions_raw, "legacy_question_review"),
    ):
        inputs.append({"kind": kind, "path": _relative_to_repo(path), "bytes": len(raw), "sha256": sha256(raw)})
    for path, raw in zip(loaded.review_paths, loaded.review_raw):
        inputs.append({"kind": "review_receipt", "path": _relative_to_repo(path), "bytes": len(raw), "sha256": sha256(raw)})
    # Context pins are included because the distinction between Operator
    # direction and captured source is part of the receipt boundary.
    for rel, kind in ((SNAPSHOT_CONTEXT_REL, "captured_snapshot_context"), (NODES_CONTRACT_REL, "captured_review_contract"), (SCOPE_DIRECTION_REL, "operator_scope_direction"), (SOURCE_READER_REL, "captured_snapshot_source_reader")):
        path = loaded.config.base_dir / rel
        raw = path.read_bytes()
        inputs.append({"kind": kind, "path": _relative_to_repo(path), "bytes": len(raw), "sha256": sha256(raw)})
    contract_path = loaded.config.base_dir / CONSOLIDATED_CONTRACT_REL
    contract_raw = contract_path.read_bytes()
    inputs.append({"kind": "consolidated_review_contract", "path": _relative_to_repo(contract_path), "bytes": len(contract_raw), "sha256": sha256(contract_raw)})
    recipe_raw = SCRIPT.read_bytes()
    inputs.append({"kind": "consolidator_compiler_recipe", "path": _relative_to_repo(SCRIPT), "bytes": len(recipe_raw), "sha256": sha256(recipe_raw)})
    output_entries = {
        name: {"path": _relative_to_repo(loaded.config.base_dir / "consolidated" / name), "bytes": len(raw), "sha256": sha256(raw)}
        for name, raw in outputs.items()
    }
    return pretty_json(
        {
            "schema_version": 1,
            "kind": "Consolidated candidate review manifest",
            "non_authoritative": True,
            "semantic_admission": "not_performed",
            "source_migration": "not_performed",
            "captured_core_commit": loaded.config.captured_core_commit,
            "candidate_sha256": sha256(loaded.candidate_raw),
            "baseline_sha256": sha256(loaded.baseline_raw),
            "baseline_inventory_sha256": loaded.baseline["inventory_sha256"],
            "prior_review_sha256": sha256(loaded.prior_review_raw),
            "identity_count": len(loaded.baseline_identities),
            "batch_count": len(loaded.reviews),
            "inputs": sorted(inputs, key=lambda item: (item["kind"], item["path"])),
            "outputs": output_entries,
            "limits": [
                "Dry-run by default; --persist is create-only and never overwrites mismatched bytes.",
                "No fresh exhaustive audit of all 951 sources is claimed; accepted evidence is reused and mechanically rechecked when referenced.",
                "The manifest excludes its own self-hash to avoid a circular byte dependency.",
            ],
        }
    )


def _build_outputs(loaded: ConsolidatedInputs) -> dict[str, bytes]:
    nodes = _build_nodes_output(loaded)
    graph = _build_graph_text(loaded)
    summary = _build_summary_text(loaded)
    core = {
        "nodes.review.json": pretty_json(nodes),
        "entity-graph.indented.txt": graph,
        "review.summary.txt": summary,
    }
    core["manifest.json"] = _build_manifest(loaded, core)
    return core


def _preflight_outputs(route: Path, outputs: Mapping[str, bytes], *, verify_only: bool) -> dict[str, str]:
    _assert_no_symlink(route, "output route")
    _require(route.is_dir(), f"output route is not a directory: {route}")
    statuses: dict[str, str] = {}
    for name, expected in outputs.items():
        _require(Path(name).name == name and Path(name).suffix in {".json", ".txt"}, f"invalid output name: {name}")
        path = route / name
        _assert_no_symlink(path, f"output {name}")
        if path.exists():
            _require(path.is_file(), f"output is not a regular file: {path}")
            actual = path.read_bytes()
            _require(actual == expected, f"existing output mismatch; refusing overwrite: {path}")
            statuses[name] = "verified"
        else:
            if verify_only:
                raise ConsolidationError(f"missing output during --verify-output: {path}")
            statuses[name] = "create"
    return statuses


def _create_only_write(path: Path, raw: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    fd: int | None = None
    try:
        fd = os.open(path, flags, 0o644)
        view = memoryview(raw)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("short write")
            view = view[written:]
        os.fsync(fd)
    except Exception:
        if fd is not None:
            os.close(fd)
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        raise
    else:
        _require(fd is not None, f"failed to open output for create: {path}")
        os.close(fd)


def consolidate(config: ConsolidationConfig | None = None, *, persist: bool = False, verify_output: bool = False) -> dict[str, Any]:
    """Validate receipts, build deterministic output bytes, and optionally persist.

    No output is written unless ``persist=True``.  Existing outputs must be
    byte-identical in either persistence or verification mode.
    """

    config = config or ConsolidationConfig()
    loaded = _load_inputs(config)
    outputs = _build_outputs(loaded)
    route = config.base_dir / "consolidated"
    statuses = _preflight_outputs(route, outputs, verify_only=verify_output and not persist)
    if persist:
        # Every target was preflighted before the first write, so a mismatch
        # cannot leave a partial set of newly-created artifacts.
        for name, status in statuses.items():
            if status == "create":
                _create_only_write(route / name, outputs[name])
    if verify_output or persist:
        _preflight_outputs(route, outputs, verify_only=True)
    return {
        "status": "persisted" if persist else ("verified" if verify_output else "dry_run"),
        "identity_count": len(loaded.baseline_identities),
        "batch_count": len(loaded.reviews),
        "outputs": {name: {"bytes": len(raw), "sha256": sha256(raw), "status": statuses[name]} for name, raw in outputs.items()},
        "candidate_sha256": sha256(loaded.candidate_raw),
        "baseline_sha256": sha256(loaded.baseline_raw),
        "prior_review_sha256": sha256(loaded.prior_review_raw),
        "captured_core_commit": loaded.config.captured_core_commit,
        "source_context": "captured_snapshot",
        "native_admission": "not_performed",
        "source_migration": "not_performed",
    }


def _parse_batches(raw: str) -> tuple[int, ...]:
    try:
        values = tuple(int(item.strip()) for item in raw.split(",") if item.strip())
    except ValueError as exc:
        raise argparse.ArgumentTypeError("batches must be comma-separated integers") from exc
    if not values or len(set(values)) != len(values):
        raise argparse.ArgumentTypeError("batches must be non-empty and unique")
    return values


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--persist", action="store_true", help="create only missing byte-identical outputs")
    parser.add_argument("--verify-output", action="store_true", help="require existing outputs to match deterministic bytes")
    parser.add_argument("--base-dir", type=Path, default=REVIEW_BASE, help="core-entity-review directory")
    parser.add_argument("--reviews-dir", type=Path, default=None, help="receipt directory (default: consolidated/reviews)")
    parser.add_argument("--batches", type=_parse_batches, default=tuple(range(9)), help="comma-separated batch numbers")
    parser.add_argument("--expected-identity-count", type=int, default=706)
    parser.add_argument("--candidate-sha256", default=EXPECTED_CANDIDATE_SHA256)
    parser.add_argument("--baseline-sha256", default=EXPECTED_BASELINE_SHA256)
    parser.add_argument("--prior-review-sha256", default=EXPECTED_PRIOR_REVIEW_SHA256)
    args = parser.parse_args(argv)
    config = ConsolidationConfig(
        base_dir=args.base_dir,
        reviews_dir=args.reviews_dir,
        batches=tuple(args.batches),
        expected_identity_count=args.expected_identity_count,
        expected_candidate_sha256=args.candidate_sha256,
        expected_baseline_sha256=args.baseline_sha256,
        expected_prior_review_sha256=args.prior_review_sha256,
    )
    try:
        result = consolidate(config, persist=args.persist, verify_output=args.verify_output)
    except (ConsolidationError, OSError) as exc:
        print(f"consolidation failed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover - exercised by CLI checks
    raise SystemExit(main())
