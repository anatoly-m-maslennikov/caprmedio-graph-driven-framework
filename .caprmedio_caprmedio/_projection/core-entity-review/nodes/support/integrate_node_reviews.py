"""CA-P-1937 captured-snapshot node-review integration producer.

The producer is deliberately derived and create-only.  It validates the nine
review packets, joins their rows without changing them, and annotates the
already accepted relation/candidate copies.  It never reads the live Core
frontier and never writes Core, Subjects, plans, or the source ledger.
"""

from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path.cwd().resolve()
D_REL = ".caprmedio_caprmedio/_projection/core-entity-review/nodes"
DESIGN_REL = ".caprmedio_caprmedio/_projection/core-entity-review/design"
BASELINE_REL = ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
BASELINE_SHA256 = "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
BASELINE_INVENTORY_SHA256 = "23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc"
RELATION_LEDGER_REL = f"{DESIGN_REL}/relations.ledger.json"
RELATION_LEDGER_SHA256 = "6ec53f14e64280815e5f57f8d00598913bc26b342102ca3acce5a7f4221d10bd"
CANDIDATE_REL = f"{DESIGN_REL}/candidate.structure.json"
CANDIDATE_SHA256 = "eda055c887706454cfd2d52bee7196a818e8eb0b8e1710d587fcfc4ffa8d9071"
SNAPSHOT_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
PREREQUISITE_RECEIPT_COMMIT = "67d83ebaeeeae6cd2c2e260947c8ffc926d7a329"
OPERATOR_DECISIONS_REL = f"{DESIGN_REL}/operator.decisions.md"
SCOPE_OMISSION_REL = f"{D_REL}/scope.omission.decision.md"
SNAPSHOT_CONTEXT_REL = f"{D_REL}/snapshot.context.md"
EXPECTED_OPERATOR_DECISIONS_SHA256 = "53eeb7a3fdaa002cd05170fe185cfb5baeea72814a1f32567d8eea6f56ac65cb"
EXPECTED_SCOPE_OMISSION_SHA256 = "d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453"
EXPECTED_SNAPSHOT_CONTEXT_SHA256 = "bfd6a7d93745d69432111df37ca139ba727a1ad06e821d94d3c059e44169ee23"
ORIGINAL_PREREQUISITES = tuple(f"CA-P-{number}" for number in range(1928, 1937))
REPAIR_PREREQUISITES = (
    "CA-P-1952",
    "CA-P-1953",
    "CA-P-1954",
    "CA-P-1955",
    "CA-P-1956",
)
PREREQUISITES = ORIGINAL_PREREQUISITES + REPAIR_PREREQUISITES
REVIEW_PLAN_IDS = {
    0: "CA-P-1928",
    1: "CA-P-1929",
    2: "CA-P-1930",
    3: "CA-P-1931",
    4: "CA-P-1932",
    5: "CA-P-1933",
    6: "CA-P-1934",
    7: "CA-P-1935",
    8: "CA-P-1936",
}
REPAIR_REVIEW_PLAN_IDS = {
    0: "CA-P-1956",
    1: "CA-P-1952",
    3: "CA-P-1956",
    4: "CA-P-1953",
    5: "CA-P-1955",
    8: "CA-P-1954",
}
EXPECTED_NODE_COUNT = 706
EXPECTED_SEGMENT_COUNT = 3093
EXPECTED_OCCURRENCE_COUNT = 4534
EXPECTED_CASE_COUNT = 294
EXPECTED_PIN_COUNT = 951


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def serialized(value: Any) -> bytes:
    return canonical(value) + b"\n"


def relative_path(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def safe_path(relative: str) -> Path:
    """Resolve a repository-relative path while rejecting symlinks."""

    path = (ROOT / relative).resolve()
    assert path.is_relative_to(ROOT), ("path-outside-repository", relative)
    original = ROOT / relative
    assert not original.is_symlink(), ("symlink-path", relative)
    for parent in original.parents:
        if parent == ROOT:
            break
        assert not parent.is_symlink(), ("symlink-parent", relative)
    return original


def load_json(relative: str, expected_sha256: str) -> tuple[Any, dict[str, Any]]:
    path = safe_path(relative)
    raw = path.read_bytes()
    assert sha(raw) == expected_sha256, ("input-pin-stale", relative)
    return json.loads(raw), {
        "path": relative,
        "sha256": expected_sha256,
        "bytes": len(raw),
    }


def pin_text(relative: str, expected_sha256: str, *, kind: str) -> dict[str, Any]:
    path = safe_path(relative)
    raw = path.read_bytes()
    assert sha(raw) == expected_sha256, ("context-pin-stale", relative)
    return {
        "kind": kind,
        "path": relative,
        "sha256": expected_sha256,
        "bytes": len(raw),
        "not_core_evidence": True,
    }


def git_bytes(commit: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def captured_tree_paths(commit: str = PREREQUISITE_RECEIPT_COMMIT) -> list[str]:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", commit],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.splitlines()


def captured_plan_paths(commit: str = PREREQUISITE_RECEIPT_COMMIT) -> list[str]:
    return [path for path in captured_tree_paths(commit) if path.endswith(".md")]


def captured_plan_path(paths: list[str], atom_id: str) -> str:
    matches = [
        path
        for path in paths
        if f"-{atom_id}-" in Path(path).name and "/archive/" not in f"/{path}"
    ]
    assert len(matches) == 1, ("captured-plan-identity-ambiguous-or-missing", atom_id, matches)
    return matches[0]


def plan_matches_frontmatter(path: Path, atom_id: str, expected_sha256: str) -> bool:
    """Validate a live Plan by identity, status and bytes, never by its path."""

    if path.is_symlink() or "archive" in path.parts:
        return False
    try:
        raw = path.read_bytes()
    except OSError:
        return False
    if sha(raw) != expected_sha256:
        return False
    return (
        frontmatter_scalar(raw, "atom_id") == atom_id
        and frontmatter_scalar(raw, "status") == "Done"
    )


def verify_live_plan(atom_id: str, expected_sha256: str) -> None:
    """Require one current Done Plan with the captured bytes.

    The current carrier location is intentionally not returned or emitted.  A
    later normal move therefore cannot alter canonical output locators.
    """

    plan_root = safe_path(".caprmedio_caprmedio/03_plan")
    matches = []
    for path in plan_root.rglob("*.md"):
        if path.is_symlink() or "archive" in path.parts:
            continue
        raw = path.read_bytes()
        if not raw.startswith(b"---\n"):
            continue
        try:
            candidate_atom_id = frontmatter_scalar(raw, "atom_id")
        except (AssertionError, UnicodeDecodeError):
            # A malformed unrelated Markdown file is not a Plan carrier, but
            # a malformed file that names this target must not be ignored.
            target_line = re.compile(
                rf"^atom_id:\s*(?:['\"])?{re.escape(atom_id)}(?:['\"])?\s*$",
                re.MULTILINE,
            )
            if target_line.search(raw.decode("utf-8", errors="replace")):
                raise AssertionError(("live-plan-frontmatter-malformed", atom_id, relative_path(path)))
            continue
        if candidate_atom_id == atom_id:
            matches.append(path)
    assert len(matches) == 1, ("live-plan-identity-ambiguous-or-missing", atom_id, len(matches))
    assert plan_matches_frontmatter(matches[0], atom_id, expected_sha256), (
        "live-plan-not-done-or-hash-mismatch",
        atom_id,
    )


def frontmatter_scalar(raw: bytes, key: str) -> str | None:
    text = raw.decode("utf-8")
    assert text.startswith("---\n"), ("plan-frontmatter-missing", key)
    end = text.find("\n---", 4)
    assert end >= 0, ("plan-frontmatter-unclosed", key)
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(text[4:end])
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def captured_prerequisite_pins(
    receipt_commit: str = PREREQUISITE_RECEIPT_COMMIT,
) -> list[dict[str, Any]]:
    """Validate prerequisite plans only from their immutable receipt commit."""

    paths = captured_plan_paths(receipt_commit)
    pins: list[dict[str, Any]] = []
    for atom_id in PREREQUISITES:
        captured_path = captured_plan_path(paths, atom_id)
        raw = git_bytes(receipt_commit, captured_path)
        parsed_atom_id = frontmatter_scalar(raw, "atom_id")
        status = frontmatter_scalar(raw, "status")
        version = frontmatter_scalar(raw, "version")
        assert parsed_atom_id == atom_id, ("captured-plan-atom-id-mismatch", atom_id)
        assert status == "Done", ("captured-plan-not-done", atom_id, status)
        assert version is not None and re.fullmatch(r"[1-9][0-9]*", version), (
            "captured-plan-version-invalid",
            atom_id,
        )
        verify_live_plan(atom_id, sha(raw))
        pins.append(
            {
                "atom_id": atom_id,
                "status": status,
                "version": int(version),
                "carrier_sha256": sha(raw),
                "captured_locator": {
                    "git_commit": receipt_commit,
                    "path": captured_path,
                },
                "captured_git_commit": receipt_commit,
                "captured_path": captured_path,
                "live_plan_verified": True,
            }
        )
    return pins


def review_artifact_from_receipt(raw: bytes, batch: int) -> tuple[str, str]:
    """Read one explicit review path/digest pair from a completion receipt."""

    text = raw.decode("utf-8")
    assert "### Completion receipt" in text, ("completion-receipt-missing", batch)
    section = text.split("### Completion receipt", 1)[1]
    if "### Definition of Done" in section:
        section = section.split("### Definition of Done", 1)[0]
    path_pattern = re.compile(
        rf"(?<![A-Za-z0-9_.-])(?:[A-Za-z0-9_.-]+/)*nodes\.batch-{batch}\.review\.json(?![A-Za-z0-9_.-])"
    )
    digest_pattern = re.compile(
        r"\bSHA(?:-256|256)\b\s*[:=]?\s*[`'\"]?([0-9a-f]{64})[`'\"]?",
        flags=re.IGNORECASE,
    )
    legacy_batch_output_pattern = re.compile(
        rf"\b(?:complete|completed|final)\s+batch-{batch}\s+output\b",
        flags=re.IGNORECASE,
    )
    candidates: list[tuple[str, str]] = []
    for line in section.splitlines():
        path_matches = path_pattern.findall(line)
        digest_matches = digest_pattern.findall(line)
        if path_matches and digest_matches:
            assert len(path_matches) == 1 and len(digest_matches) == 1, (
                "review-receipt-artifact-declaration-ambiguous",
                batch,
            )
            candidates.append((path_matches[0], digest_matches[0].lower()))
        elif legacy_batch_output_pattern.search(line) and digest_matches:
            # Two original Done parent Plans use this exact batch-labelled
            # legacy form.  The batch label and SHA-256 label bind the digest
            # to the expected review artifact; arbitrary receipt hashes do not.
            assert len(digest_matches) == 1, (
                "review-receipt-artifact-declaration-ambiguous",
                batch,
            )
            candidates.append((f"nodes.batch-{batch}.review.json", digest_matches[0].lower()))
    assert len(candidates) == 1, ("review-receipt-artifact-declaration-missing-or-ambiguous", batch)
    return candidates[0]


def review_sha_from_receipt(raw: bytes, batch: int) -> str:
    """Read the digest from one explicit review path/digest declaration."""

    _, digest = review_artifact_from_receipt(raw, batch)
    return digest


def committed_review_pins(
    receipt_commit: str = PREREQUISITE_RECEIPT_COMMIT,
) -> dict[int, dict[str, Any]]:
    """Pin each final review to the receipt Plan and bytes in one commit.

    Batches 0, 1, 3, 4, 5 and 8 intentionally use their repair Plans.  This keeps the
    original Done Plan receipts historically intact while letting the repair
    receipts override only the final review digest for those batches.
    """

    tree_paths = captured_tree_paths(receipt_commit)
    plan_paths = [path for path in tree_paths if path.endswith(".md")]
    review_pins: dict[int, dict[str, Any]] = {}
    for batch in range(9):
        plan_id = REPAIR_REVIEW_PLAN_IDS.get(batch, REVIEW_PLAN_IDS[batch])
        plan_path = captured_plan_path(plan_paths, plan_id)
        plan_raw = git_bytes(receipt_commit, plan_path)
        assert frontmatter_scalar(plan_raw, "atom_id") == plan_id
        assert frontmatter_scalar(plan_raw, "status") == "Done"
        declared_path, declared_sha256 = review_artifact_from_receipt(plan_raw, batch)
        review_matches = [
            path
            for path in tree_paths
            if Path(path).name == f"nodes.batch-{batch}.review.json"
        ]
        assert len(review_matches) == 1, ("captured-review-identity-ambiguous-or-missing", batch, review_matches)
        review_path = review_matches[0]
        assert review_path.endswith(declared_path), (
            "receipt-review-path-mismatch",
            batch,
            declared_path,
            review_path,
        )
        review_raw = git_bytes(receipt_commit, review_path)
        actual_sha256 = sha(review_raw)
        assert declared_sha256 == actual_sha256, (
            "receipt-review-sha-mismatch",
            batch,
            declared_sha256,
            actual_sha256,
        )
        review_pins[batch] = {
            "batch": batch,
            "plan_atom_id": plan_id,
            "receipt_commit": receipt_commit,
            "plan_sha256": sha(plan_raw),
            "plan_captured_path": plan_path,
            "review_sha256": actual_sha256,
            "review_captured_path": review_path,
            "review_bytes": len(review_raw),
            "live_review_hash_checked": False,
        }
    return review_pins


def source_context_pins() -> list[dict[str, Any]]:
    return [
        pin_text(
            OPERATOR_DECISIONS_REL,
            EXPECTED_OPERATOR_DECISIONS_SHA256,
            kind="operator_substance_direction",
        ),
        pin_text(
            SCOPE_OMISSION_REL,
            EXPECTED_SCOPE_OMISSION_SHA256,
            kind="operator_scope_omission_direction",
        ),
        pin_text(
            SNAPSHOT_CONTEXT_REL,
            EXPECTED_SNAPSHOT_CONTEXT_SHA256,
            kind="captured_snapshot_context",
        ),
    ]


def import_review_helpers():
    support = safe_path(f"{D_REL}/support")
    if str(support) not in sys.path:
        sys.path.insert(0, str(support))
    import snapshot_sources  # type: ignore[import-not-found]
    import verify_node_reviews  # type: ignore[import-not-found]

    assert snapshot_sources.COMMIT == SNAPSHOT_COMMIT
    return snapshot_sources, verify_node_reviews


def normalize_catalogue(catalogue: Any) -> dict[str, dict[str, Any]]:
    if isinstance(catalogue, list):
        normalized: dict[str, dict[str, Any]] = {}
        for item in catalogue:
            assert isinstance(item, dict) and item.get("evidence_ref") is not None
            local_ref = str(item["evidence_ref"])
            assert local_ref not in normalized, ("duplicate-local-evidence-ref", local_ref)
            normalized[local_ref] = item
        return normalized
    assert isinstance(catalogue, dict)
    return {str(key): value for key, value in catalogue.items()}


def global_evidence_key(source_task: str, batch: int, local_ref: str) -> str:
    return f"{source_task}/batch-{batch}/{local_ref}"


def node_disposition_id(identity: str) -> str:
    return f"node-disposition:{sha(identity.encode('utf-8'))}"


def review_context(
    snapshot_result: dict[str, Any],
    context_pins: list[dict[str, Any]],
    source_reader_pin: dict[str, Any],
) -> dict[str, Any]:
    return {
        "kind": "captured_snapshot",
        "git_commit": SNAPSHOT_COMMIT,
        "current_core_claimed": False,
        "source_pins_checked": snapshot_result["source_pins_checked"],
        "snapshot_verification": snapshot_result["verification"],
        "source_reader": source_reader_pin,
        "operator_context_pins": context_pins,
        "operator_context_is_not_core_evidence": True,
    }


def prepare_reviews(
    baseline: dict[str, Any],
    snapshot_result: dict[str, Any],
    context_pins: list[dict[str, Any]],
    source_reader_pin: dict[str, Any],
    review_pins: dict[int, dict[str, Any]],
    prerequisite_pins: list[dict[str, Any]],
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
    """Verify and join all review batches, retaining every authored row."""

    _, verify_node_reviews = import_review_helpers()
    source_context = review_context(snapshot_result, context_pins, source_reader_pin)
    review_set: list[dict[str, Any]] = []
    marks: list[dict[str, Any]] = []
    global_catalogue: dict[str, dict[str, Any]] = {}
    seen_identities: set[str] = set()
    disposition_counts: collections.Counter[str] = collections.Counter()
    batch_reports: list[dict[str, Any]] = []

    for batch in range(9):
        input_rel = f"{D_REL}/inputs/nodes.batch-{batch}.input.json"
        output_rel = f"{D_REL}/nodes.batch-{batch}.review.json"
        input_path = safe_path(input_rel)
        output_path = safe_path(output_rel)
        input_raw = input_path.read_bytes()
        output_raw = output_path.read_bytes()
        input_packet = json.loads(input_raw)
        review_packet = json.loads(output_raw)
        committed_pin = review_pins[batch]
        assert sha(output_raw) == committed_pin["review_sha256"], (
            "live-review-hash-does-not-match-committed-receipt",
            batch,
            committed_pin["review_sha256"],
            sha(output_raw),
        )
        committed_pin = copy.deepcopy(committed_pin)
        committed_pin["live_review_hash_checked"] = True
        report = verify_node_reviews.verify(
            batch,
            input_path=input_rel,
            output_path=output_rel,
        )
        assert report["mechanical_checks"] == "pass"
        source_task = input_packet["source_task"]
        assert source_task == f"CA-P-{1928 + batch}", ("source-task-mismatch", batch)
        assert review_packet["source_task"] == source_task
        assert review_packet["batch"] == batch
        assert review_packet["partition_sha256"] == input_packet["partition_sha256"]
        assert report["file_sha256"] == sha(output_raw)
        local_catalogue = normalize_catalogue(review_packet["evidence_catalogue"])
        local_to_global: dict[str, str] = {}
        for local_ref, evidence in local_catalogue.items():
            key = global_evidence_key(source_task, batch, local_ref)
            assert key not in global_catalogue
            global_catalogue[key] = evidence
            local_to_global[local_ref] = key

        rows = review_packet["nodes"]
        input_nodes = {node["identity"]: node for node in input_packet["nodes"]}
        for row in rows:
            identity = row["identity"]
            assert identity in input_nodes, ("review-identity-not-in-input", batch, identity)
            assert identity not in seen_identities, ("review-identity-overlap", identity)
            seen_identities.add(identity)
            disposition_counts[row["disposition"]] += 1
            local_refs = [str(ref) for ref in row.get("evidence_refs", [])]
            check_refs = [
                str(ref)
                for check in row["checks"].values()
                for ref in check.get("evidence_refs", [])
            ]
            all_local_refs = list(dict.fromkeys(local_refs + check_refs))
            assert all(ref in local_to_global for ref in all_local_refs), (
                "review-evidence-ref-not-in-catalogue",
                batch,
                identity,
            )
            global_refs = [local_to_global[ref] for ref in all_local_refs]
            mark_id = node_disposition_id(identity)
            exact_row = copy.deepcopy(row)
            scoped_refs = {
                "task": source_task,
                "batch": batch,
                "local_refs": all_local_refs,
                "global_evidence_refs": global_refs,
                "input_occurrence_ids": (
                    list(row["input_occurrence_ids"])
                    if "input_occurrence_ids" in row
                    else list(input_nodes[identity]["occurrence_ids"])
                ),
            }
            if "segment_ids" in row:
                scoped_refs["segment_ids"] = list(row["segment_ids"])
            marks.append(
                {
                    "node_disposition_id": mark_id,
                    "identity": identity,
                    "canonical_row_sha256": sha(canonical(exact_row)),
                    "review_row": exact_row,
                    "source_review": {
                        "source_context": "captured_snapshot",
                        "git_commit": SNAPSHOT_COMMIT,
                        "checked_source_atom_ids": list(row["checked_source_atom_ids"]),
                        "evidence_refs": global_refs,
                    },
                    "scoped_refs": scoped_refs,
                }
            )
        batch_reports.append(
            {
                "task": source_task,
                "batch": batch,
                "input": {
                    "path": input_rel,
                    "sha256": sha(input_raw),
                    "bytes": len(input_raw),
                },
                "output": {
                    "path": output_rel,
                    "sha256": sha(output_raw),
                    "bytes": len(output_raw),
                },
                "receipt": committed_pin,
                "partition_sha256": input_packet["partition_sha256"],
                "identity_count": len(rows),
                "evidence_count": len(local_catalogue),
                "verifier": report,
            }
        )

    assert len(seen_identities) == EXPECTED_NODE_COUNT
    assert len(marks) == EXPECTED_NODE_COUNT
    review_set_payload = {
        "count": len(batch_reports),
        "batches": batch_reports,
        "source_context": "captured_snapshot",
        "git_commit": SNAPSHOT_COMMIT,
    }
    unresolved_drop_annotations = [
        {
            "identity": mark["identity"],
            "node_disposition_id": mark["node_disposition_id"],
            "canonical_row_sha256": mark["canonical_row_sha256"],
            "display_review_mark": mark["review_row"].get("display_review_mark"),
            "question": mark["review_row"].get("question"),
        }
        for mark in marks
        if mark["review_row"]["disposition"] == "question"
        and str(mark["review_row"].get("display_review_mark", "")).startswith("DROP_CANDIDATE_")
    ]
    counts = {
        "nodes": len(marks),
        "dispositions": dict(sorted(disposition_counts.items())),
        "evidence_catalogue": len(global_catalogue),
        "review_batches": len(batch_reports),
        "questions_with_unresolved_drop_annotations": len(unresolved_drop_annotations),
    }
    packet = {
        "schema_version": 1,
        "source_task": "CA-P-1937",
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "Operator_acceptance": "not_performed",
        "baseline_inventory_sha256": baseline["inventory_sha256"],
        "source_context": source_context,
        "source_review": {
            "review_context": source_context,
            "baseline": {
                "path": BASELINE_REL,
                "sha256": BASELINE_SHA256,
                "inventory_sha256": baseline["inventory_sha256"],
            },
            "review_set": review_set_payload,
        },
        "review_set": review_set_payload,
        "review_receipts": review_pins,
        "node_disposition_marks": marks,
        "unresolved_drop_annotations": unresolved_drop_annotations,
        "evidence_catalogue": global_catalogue,
        "counts": counts,
        "disposition_distribution": dict(sorted(disposition_counts.items())),
        "checks_performed": {
            "captured_snapshot_sources": "pass",
            "captured_source_pins_checked": EXPECTED_PIN_COUNT,
            "all_nine_verify_node_reviews": "pass",
            "exact_identity_coverage": "pass",
            "identity_overlap": "none",
            "five_checks_per_node": "delegated_to_verify_node_reviews",
            "original_review_rows": "retained_nested_and_unmodified",
            "semantic_admission": "not_performed",
        },
        "producer": {
            "path": f"{D_REL}/support/integrate_node_reviews.py",
            "sha256": sha(Path(__file__).read_bytes()),
        },
        "prerequisite_completion_pins": prerequisite_pins,
        "source_context_pins": context_pins,
    }
    return packet, marks, global_catalogue, {"counts": counts, "reports": batch_reports}


def annotate_ledger(
    baseline: dict[str, Any],
    relation_ledger: dict[str, Any],
    marks: list[dict[str, Any]],
    node_packet_sha256: str,
    snapshot_context: dict[str, Any],
    context_pins: list[dict[str, Any]],
    prerequisite_pins: list[dict[str, Any]],
) -> dict[str, Any]:
    marked = copy.deepcopy(relation_ledger)
    by_identity = {mark["identity"]: mark for mark in marks}
    assert len(by_identity) == EXPECTED_NODE_COUNT
    original_segments = marked["original_segments"]
    assert len(original_segments) == EXPECTED_SEGMENT_COUNT
    endpoint_count = collections.Counter()
    for segment in original_segments:
        parent = segment["original_qualified_parent"]
        child = segment["original_qualified_child"]
        assert parent in by_identity and child in by_identity
        parent_mark = by_identity[parent]
        child_mark = by_identity[child]
        annotations = [
            {
                "endpoint": "parent",
                "node_identity": parent,
                "node_disposition_id": parent_mark["node_disposition_id"],
                "disposition": parent_mark["review_row"]["disposition"],
                "canonical_row_sha256": parent_mark["canonical_row_sha256"],
                "native_relation_inferred": False,
                "semantic_admission": "not_performed",
            },
            {
                "endpoint": "child",
                "node_identity": child,
                "node_disposition_id": child_mark["node_disposition_id"],
                "disposition": child_mark["review_row"]["disposition"],
                "canonical_row_sha256": child_mark["canonical_row_sha256"],
                "native_relation_inferred": False,
                "semantic_admission": "not_performed",
            },
        ]
        segment["endpoint_annotations"] = annotations
        segment["node_disposition_ids"] = [
            parent_mark["node_disposition_id"],
            child_mark["node_disposition_id"],
        ]
        segment["native_relation_inferred"] = False
        endpoint_count["segments"] += 1
        endpoint_count[parent_mark["review_row"]["disposition"]] += 1
        endpoint_count[child_mark["review_row"]["disposition"]] += 1
    assert endpoint_count["segments"] == EXPECTED_SEGMENT_COUNT
    marked["node_review_integration"] = {
        "source_task": "CA-P-1937",
        "node_dispositions": {
            "path": f"{D_REL}/nodes.dispositions.json",
            "sha256": node_packet_sha256,
            "count": len(marks),
        },
        "endpoint_annotation_policy": {
            "annotations_per_original_segment": 2,
            "endpoint_fields": ["original_qualified_parent", "original_qualified_child"],
            "node_disposition_link_field": "node_disposition_id",
            "native_relation_inferred": False,
            "original_segment_fields_preserved": True,
        },
        "annotated_original_segments": len(original_segments),
    }
    marked["source_review"] = {
        "kind": "captured_snapshot",
        "git_commit": SNAPSHOT_COMMIT,
        "current_core_claimed": False,
        "source_pins_checked": EXPECTED_PIN_COUNT,
        "snapshot_context": snapshot_context,
        "operator_context_pins": context_pins,
        "operator_context_is_not_core_evidence": True,
    }
    marked["node_review_prerequisite_pins"] = prerequisite_pins
    marked["integration_checks"] = {
        "baseline_sha256": BASELINE_SHA256,
        "baseline_inventory_sha256": baseline["inventory_sha256"],
        "original_nodes": len(marked["original_nodes"]) == EXPECTED_NODE_COUNT,
        "original_occurrences": len(marked["original_occurrences"]) == EXPECTED_OCCURRENCE_COUNT,
        "original_segments": len(marked["original_segments"]) == EXPECTED_SEGMENT_COUNT,
        "segment_reviews": len(marked["segment_reviews"]) == EXPECTED_SEGMENT_COUNT,
        "case_reviews": len(marked["case_reviews"]) == EXPECTED_CASE_COUNT,
        "endpoint_annotations": len(original_segments) * 2,
        "original_review_reasons_preserved": True,
        "original_review_proposals_preserved": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "Operator_acceptance": "not_performed",
    }
    marked["native_admission"] = "not_performed"
    return marked


def annotate_candidate(
    candidate: dict[str, Any],
    baseline: dict[str, Any],
    marks: list[dict[str, Any]],
    node_packet_sha256: str,
    marked_ledger_sha256: str,
    snapshot_context: dict[str, Any],
    context_pins: list[dict[str, Any]],
    prerequisite_pins: list[dict[str, Any]],
) -> dict[str, Any]:
    marked = copy.deepcopy(candidate)
    pinned_marks = [
        {
            "identity": mark["identity"],
            "node_disposition_id": mark["node_disposition_id"],
            "canonical_row_sha256": mark["canonical_row_sha256"],
            "disposition": mark["review_row"]["disposition"],
            "confidence_percent": mark["review_row"]["confidence_percent"],
            "native_admission": "not_performed",
        }
        for mark in marks
    ]
    assert len(pinned_marks) == EXPECTED_NODE_COUNT
    marked["pinned_node_marks"] = pinned_marks
    marked["node_dispositions_ref"] = {
        "path": f"{D_REL}/nodes.dispositions.json",
        "sha256": node_packet_sha256,
        "count": len(marks),
    }
    marked["marked_relation_ledger_ref"] = {
        "path": f"{D_REL}/relations.marked.ledger.json",
        "sha256": marked_ledger_sha256,
        "original_source_sha256": RELATION_LEDGER_SHA256,
        "original_counts": {
            "original_nodes": EXPECTED_NODE_COUNT,
            "original_occurrences": EXPECTED_OCCURRENCE_COUNT,
            "original_segments": EXPECTED_SEGMENT_COUNT,
            "segment_reviews": EXPECTED_SEGMENT_COUNT,
            "case_reviews": EXPECTED_CASE_COUNT,
        },
    }
    marked["node_review_prerequisite_pins"] = prerequisite_pins
    marked["source_context"] = snapshot_context
    marked["source_context_pins"] = context_pins
    marked["integration_checks"] = {
        "exact_node_identity_coverage": len(pinned_marks) == EXPECTED_NODE_COUNT,
        "node_identity_overlap": "none",
        "endpoint_annotations": "preserved_in_marked_relation_ledger",
        "original_candidate_fields_preserved": True,
        "pinned_review_rows": "retained_in_nodes.dispositions.json",
        "native_admission": "not_performed",
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "Operator_acceptance": "not_performed",
        "candidate_is_not_accepted_or_serialized_Subjects": True,
    }
    marked["native_admission"] = "not_performed"
    marked["source_migration"] = "not_performed"
    marked["Operator_acceptance"] = "not_performed"
    marked["baseline_inventory_sha256"] = baseline["inventory_sha256"]
    return marked


def build() -> tuple[dict[str, bytes], dict[str, Any]]:
    baseline, baseline_pin = load_json(BASELINE_REL, BASELINE_SHA256)
    assert baseline["inventory_sha256"] == BASELINE_INVENTORY_SHA256
    assert sha(canonical({k: v for k, v in baseline.items() if k != "inventory_sha256"})) == BASELINE_INVENTORY_SHA256
    relation_ledger, relation_pin = load_json(RELATION_LEDGER_REL, RELATION_LEDGER_SHA256)
    candidate, candidate_pin = load_json(CANDIDATE_REL, CANDIDATE_SHA256)
    assert len(relation_ledger["original_nodes"]) == EXPECTED_NODE_COUNT
    assert len(relation_ledger["original_occurrences"]) == EXPECTED_OCCURRENCE_COUNT
    assert len(relation_ledger["original_segments"]) == EXPECTED_SEGMENT_COUNT
    assert len(relation_ledger["segment_reviews"]) == EXPECTED_SEGMENT_COUNT
    assert len(relation_ledger["case_reviews"]) == EXPECTED_CASE_COUNT
    assert len(candidate["preserved_node_ids"]) == EXPECTED_NODE_COUNT

    snapshot_sources, _ = import_review_helpers()
    snapshot_result = snapshot_sources.verify_snapshot()
    assert snapshot_result["source_pins_checked"] == EXPECTED_PIN_COUNT
    assert snapshot_result["current_core_claimed"] is False
    context_pins = source_context_pins()
    source_reader_path = f"{D_REL}/support/snapshot_sources.py"
    source_reader_pin = pin_text(
        source_reader_path,
        sha(safe_path(source_reader_path).read_bytes()),
        kind="captured_snapshot_source_reader",
    )
    prerequisite_pins = captured_prerequisite_pins()
    review_pins = committed_review_pins()
    node_packet, marks, _, review_info = prepare_reviews(
        baseline,
        snapshot_result,
        context_pins,
        source_reader_pin,
        review_pins,
        prerequisite_pins,
    )
    node_bytes = serialized(node_packet)
    node_sha256 = sha(node_bytes)
    marked_ledger = annotate_ledger(
        baseline,
        relation_ledger,
        marks,
        node_sha256,
        node_packet["source_context"],
        context_pins,
        prerequisite_pins,
    )
    marked_ledger_bytes = serialized(marked_ledger)
    marked_ledger_sha256 = sha(marked_ledger_bytes)
    marked_candidate = annotate_candidate(
        candidate,
        baseline,
        marks,
        node_sha256,
        marked_ledger_sha256,
        node_packet["source_context"],
        context_pins,
        prerequisite_pins,
    )
    candidate_bytes = serialized(marked_candidate)
    candidate_sha256 = sha(candidate_bytes)
    outputs = {
        f"{D_REL}/nodes.dispositions.json": node_bytes,
        f"{D_REL}/relations.marked.ledger.json": marked_ledger_bytes,
        f"{D_REL}/candidate.structure.marked.json": candidate_bytes,
    }
    summary = {
        "source_task": "CA-P-1937",
        "source_context": node_packet["source_context"],
        "input_pins": {
            "baseline": baseline_pin,
            "relation_ledger": relation_pin,
            "candidate": candidate_pin,
            "snapshot_source_reader": source_reader_pin,
        },
        "captured_prerequisites": prerequisite_pins,
        "review_receipts": review_pins,
        "checks": {
            "snapshot": snapshot_result,
            "review_batches": review_info["reports"],
            "exact_node_coverage": len(marks) == EXPECTED_NODE_COUNT,
            "distribution": node_packet["disposition_distribution"],
            "relation_arrays": {
                "original_nodes": len(marked_ledger["original_nodes"]),
                "original_occurrences": len(marked_ledger["original_occurrences"]),
                "original_segments": len(marked_ledger["original_segments"]),
                "segment_reviews": len(marked_ledger["segment_reviews"]),
                "case_reviews": len(marked_ledger["case_reviews"]),
            },
            "endpoint_annotations": EXPECTED_SEGMENT_COUNT * 2,
        },
        "outputs": [
            {"path": path, "sha256": sha(raw), "bytes": len(raw)}
            for path, raw in outputs.items()
        ],
        "counts": node_packet["counts"],
        "hashes": {
            "nodes_dispositions": node_sha256,
            "relations_marked_ledger": marked_ledger_sha256,
            "candidate_structure_marked": candidate_sha256,
        },
    }
    return outputs, summary


def persist_or_verify(outputs: dict[str, bytes], *, persist: bool, verify_output: bool) -> None:
    assert not (persist and verify_output)
    for relative, raw in outputs.items():
        path = safe_path(relative)
        if path.exists():
            assert path.is_file() and not path.is_symlink(), ("existing-output-not-regular", relative)
            assert path.read_bytes() == raw, ("existing-artifact-differs-no-overwrite", relative)
        elif verify_output:
            raise AssertionError(("output-missing", relative))
    if persist:
        for relative, raw in outputs.items():
            path = safe_path(relative)
            if not path.exists():
                with path.open("xb") as handle:
                    handle.write(raw)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true")
    parser.add_argument("--verify-output", action="store_true")
    args = parser.parse_args()
    outputs, summary = build()
    persist_or_verify(outputs, persist=args.persist, verify_output=args.verify_output)
    summary["outcome"] = "verified" if args.verify_output else ("persisted_or_existing_identical" if args.persist else "dry_run")
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
