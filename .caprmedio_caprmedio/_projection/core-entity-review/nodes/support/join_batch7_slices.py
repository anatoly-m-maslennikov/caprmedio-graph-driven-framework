"""Join the five CA-P-1935 batch-7 node-review slices.

The producer is deliberately create-only.  Without ``--persist`` it performs
all checks and prints the deterministic output digest without writing.  Child
rows and evidence are copied verbatim except that evidence references are
namespaced by child task ID; the original row hashes and source paths are
kept in a separate provenance receipt.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path.cwd()
NODES = ROOT / ".caprmedio_caprmedio" / "_projection" / "core-entity-review" / "nodes"
SUPPORT = NODES / "support"
PARENT_INPUT = NODES / "inputs" / "nodes.batch-7.input.json"
OUTPUT = NODES / "nodes.batch-7.review.json"
CHILD_TASKS = (1945, 1946, 1947, 1948, 1949)
PLAN_SNAPSHOT_COMMIT = "bdc700939"
SNAPSHOT_CONTEXT = NODES / "snapshot.context.md"
SCOPE_DECISION = NODES / "scope.omission.decision.md"
sys.path.insert(0, str(SUPPORT))
from snapshot_sources import COMMIT, verify_snapshot  # noqa: E402
import verify_node_reviews  # noqa: E402


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def load_json(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    return json.loads(raw), raw


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def assert_pin(path: Path, expected_sha: str, label: str) -> bytes:
    raw = path.read_bytes()
    if sha(raw) != expected_sha:
        raise AssertionError(f"{label} pin mismatch")
    return raw


def plan_receipt(task_id: int) -> dict[str, Any]:
    matches = sorted(ROOT.glob(f".caprmedio_caprmedio/03_plan/**/*CA-P-{task_id}-TASK--*.md"))
    expected_id = f"CA-P-{task_id}"
    current_matches: list[tuple[Path, bytes, str]] = []
    for candidate in matches:
        raw = candidate.read_bytes()
        text = raw.decode("utf-8")
        atom_id_match = re.search(r"^atom_id:\s*(\S+)\s*$", text, re.MULTILINE)
        if atom_id_match is not None and atom_id_match.group(1) == expected_id:
            current_matches.append((candidate, raw, text))
    if len(current_matches) != 1:
        raise AssertionError(f"expected exactly one current {expected_id} Plan by frontmatter, found {len(current_matches)}")
    current_path, current_raw, current_text = current_matches[0]
    tree = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", PLAN_SNAPSHOT_COMMIT, "--", ".caprmedio_caprmedio/03_plan"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    captured_matches: list[tuple[str, bytes, str]] = []
    marker = f"CA-P-{task_id}-TASK--"
    for path in tree:
        if marker not in path or not path.endswith(".md"):
            continue
        captured_raw = subprocess.run(
            ["git", "show", f"{PLAN_SNAPSHOT_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        captured_text = captured_raw.decode("utf-8")
        atom_id_match = re.search(r"^atom_id:\s*(\S+)\s*$", captured_text, re.MULTILINE)
        if atom_id_match is not None and atom_id_match.group(1) == expected_id:
            captured_matches.append((path, captured_raw, captured_text))
    if len(captured_matches) != 1:
        raise AssertionError(f"expected exactly one captured {expected_id} Plan by frontmatter, found {len(captured_matches)}")
    captured_path, captured_raw, captured_text = captured_matches[0]
    captured_sha = sha(captured_raw)
    if sha(current_raw) != captured_sha:
        raise AssertionError(f"current CA-P-{task_id} Plan differs from captured snapshot")
    current_id_match = re.search(r"^atom_id:\s*(\S+)\s*$", current_text, re.MULTILINE)
    captured_id_match = re.search(r"^atom_id:\s*(\S+)\s*$", captured_text, re.MULTILINE)
    if current_id_match is None or current_id_match.group(1) != expected_id:
        raise AssertionError(f"current Plan frontmatter identity mismatch for {expected_id}")
    if captured_id_match is None or captured_id_match.group(1) != expected_id:
        raise AssertionError(f"captured Plan frontmatter identity mismatch for {expected_id}")
    status_match = re.search(r"^status:\s*(\S+)\s*$", current_text, re.MULTILINE)
    if status_match is None or status_match.group(1) != "Done":
        raise AssertionError(f"CA-P-{task_id} prerequisite is not Done")
    captured_status_match = re.search(r"^status:\s*(\S+)\s*$", captured_text, re.MULTILINE)
    if captured_status_match is None or captured_status_match.group(1) != "Done":
        raise AssertionError(f"captured CA-P-{task_id} prerequisite is not Done")
    version_match = re.search(r"^version:\s*(\S+)\s*$", captured_text, re.MULTILINE)
    updated_match = re.search(r"^updated_at:\s*(.+?)\s*$", captured_text, re.MULTILINE)
    return {
        "task": f"CA-P-{task_id}",
        "captured_commit": PLAN_SNAPSHOT_COMMIT,
        "captured_path": captured_path,
        "captured_sha256": captured_sha,
        "current_status": status_match.group(1),
        "current_sha256": sha(current_raw),
        "version": version_match.group(1) if version_match else None,
        "updated_at": updated_match.group(1) if updated_match else None,
    }


def verify_child_input(
    task_id: int,
    child_input: dict[str, Any],
    child_input_raw: bytes,
    parent: dict[str, Any],
    parent_raw: bytes,
    baseline: dict[str, Any],
    operator_decision: dict[str, Any],
    scope_pin: dict[str, Any],
) -> None:
    expected_task = f"CA-P-{task_id}"
    if child_input["source_task"] != expected_task or child_input["batch"] != 7:
        raise AssertionError(f"{expected_task} input task/batch mismatch")
    expected_partition = sha(canonical({k: v for k, v in child_input.items() if k != "partition_sha256"}))
    if expected_partition != child_input["partition_sha256"]:
        raise AssertionError(f"{expected_task} input partition digest mismatch")
    if child_input.get("parent_source_task") != parent["source_task"]:
        raise AssertionError(f"{expected_task} parent source task mismatch")
    parent_pin = child_input.get("parent_input")
    expected_parent_pin = {
        "path": rel(PARENT_INPUT),
        "sha256": sha(parent_raw),
        "partition_sha256": parent["partition_sha256"],
    }
    if parent_pin != expected_parent_pin:
        raise AssertionError(f"{expected_task} parent input pin mismatch")
    if child_input["baseline"] != parent["baseline"]:
        raise AssertionError(f"{expected_task} baseline pin mismatch")
    if child_input.get("operator_decision") != operator_decision:
        raise AssertionError(f"{expected_task} Operator decision pin mismatch")
    if child_input.get("scope_omission_pin") != scope_pin:
        raise AssertionError(f"{expected_task} scope decision pin mismatch")
    if child_input.get("non_authoritative") is not True:
        raise AssertionError(f"{expected_task} input is authoritative")
    if not child_input.get("nodes"):
        raise AssertionError(f"{expected_task} has no assigned nodes")
    if sha(child_input_raw) == "":
        raise AssertionError("unreachable input digest guard")


def child_catalogue(output: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    catalogue = output.get("evidence_catalogue")
    if isinstance(catalogue, list):
        items = [(item.get("evidence_ref"), item) for item in catalogue]
    elif isinstance(catalogue, dict):
        items = list(catalogue.items())
    else:
        raise AssertionError("child evidence catalogue is neither list nor object")
    refs = [ref for ref, _ in items]
    if any(not isinstance(ref, str) or not ref for ref in refs) or len(set(refs)) != len(refs):
        raise AssertionError("child evidence references are not unique")
    return items


def remap_refs(value: Any, mapping: dict[str, str]) -> Any:
    """Copy a row while remapping only fields named evidence_refs."""

    if isinstance(value, dict):
        copied: dict[str, Any] = {}
        for key, item in value.items():
            if key == "evidence_refs":
                if not isinstance(item, list):
                    raise AssertionError("evidence_refs is not a list")
                copied[key] = [mapping[ref] for ref in item]
            else:
                copied[key] = remap_refs(item, mapping)
        return copied
    if isinstance(value, list):
        return [remap_refs(item, mapping) for item in value]
    return value


def build_join() -> tuple[dict[str, Any], dict[str, Any]]:
    parent, parent_raw = load_json(PARENT_INPUT)
    if parent["source_task"] != "CA-P-1935" or parent["batch"] != 7 or parent["identity_count"] != 80:
        raise AssertionError("unexpected CA-P-1935 batch-7 parent input")
    if sha(canonical({k: v for k, v in parent.items() if k != "partition_sha256"})) != parent["partition_sha256"]:
        raise AssertionError("parent partition digest mismatch")

    baseline_path = ROOT / parent["baseline"]["path"]
    baseline_raw = assert_pin(baseline_path, parent["baseline"]["sha256"], "baseline")
    baseline = json.loads(baseline_raw)
    if baseline["inventory_sha256"] != parent["baseline"]["inventory_sha256"]:
        raise AssertionError("baseline inventory digest mismatch")
    operator_decision = parent["operator_decision"]
    operator_path = ROOT / operator_decision["path"]
    assert_pin(operator_path, operator_decision["sha256"], "Operator decision")
    scope_pin = {
        "path": rel(SCOPE_DECISION),
        "sha256": sha(SCOPE_DECISION.read_bytes()),
    }
    snapshot = verify_snapshot()
    if snapshot["git_commit"] != COMMIT or snapshot["source_context"] != "captured_snapshot":
        raise AssertionError("captured snapshot verification did not return the selected context")
    if not SNAPSHOT_CONTEXT.is_file():
        raise AssertionError("snapshot context record is missing")

    parent_identities = [node["identity"] for node in parent["nodes"]]
    if len(parent_identities) != 80 or len(set(parent_identities)) != 80:
        raise AssertionError("parent identity coverage is not exact")
    parent_identity_set = set(parent_identities)

    joined_rows_by_identity: dict[str, dict[str, Any]] = {}
    joined_evidence: list[dict[str, Any]] = []
    child_receipts: list[dict[str, Any]] = []
    all_original_rows: list[dict[str, Any]] = []
    child_input_paths: list[str] = []

    for task_id in CHILD_TASKS:
        task = f"CA-P-{task_id}"
        input_path = NODES / "inputs" / "slices" / f"CA-P-{task_id}.input.json"
        output_path = NODES / "slices" / f"CA-P-{task_id}.review.json"
        child_input, child_input_raw = load_json(input_path)
        child_output, child_output_raw = load_json(output_path)
        child_input_paths.append(rel(input_path))
        verify_child_input(task_id, child_input, child_input_raw, parent, parent_raw, baseline, operator_decision, scope_pin)
        verification = verify_node_reviews.verify(7, str(input_path), str(output_path))
        if verification["source_context"] != "captured_snapshot" or verification["git_commit"] != COMMIT:
            raise AssertionError(f"{task} did not verify against the captured snapshot")
        if child_output["source_task"] != task or child_output["batch"] != 7:
            raise AssertionError(f"{task} output task/batch mismatch")

        input_identities = [node["identity"] for node in child_input["nodes"]]
        output_rows = child_output["nodes"]
        if len(input_identities) != len(output_rows) or set(input_identities) != {row["identity"] for row in output_rows}:
            raise AssertionError(f"{task} input/output identity coverage mismatch")
        if not set(input_identities).issubset(parent_identity_set):
            raise AssertionError(f"{task} contains identity outside the parent partition")
        overlap = set(input_identities) & set(joined_rows_by_identity)
        if overlap:
            raise AssertionError(f"child identity overlap: {sorted(overlap)}")

        original_catalogue = child_catalogue(child_output)
        refs: dict[str, str] = {}
        namespaced_catalogue: list[dict[str, Any]] = []
        for old_ref, item in original_catalogue:
            new_ref = f"{task}/{old_ref}"
            if new_ref in refs.values():
                raise AssertionError(f"evidence reference collision: {new_ref}")
            refs[old_ref] = new_ref
            item_copy = copy.deepcopy(item)
            item_copy["evidence_ref"] = new_ref
            namespaced_catalogue.append(item_copy)
        joined_evidence.extend(namespaced_catalogue)

        row_provenance: list[dict[str, Any]] = []
        for original_row in output_rows:
            identity = original_row["identity"]
            if identity not in input_identities:
                raise AssertionError(f"{task} output has an unexpected identity")
            all_original_rows.append(original_row)
            row_provenance.append(
                {
                    "identity": identity,
                    "source_path": rel(output_path),
                    "row_canonical_sha256": sha(canonical(original_row)),
                }
            )
            joined_rows_by_identity[identity] = remap_refs(original_row, refs)

        child_receipts.append(
            {
                "source_task": task,
                "plan": plan_receipt(task_id),
                "input": {
                    "path": rel(input_path),
                    "sha256": sha(child_input_raw),
                    "partition_sha256": child_input["partition_sha256"],
                    "parent_input": child_input["parent_input"],
                },
                "output": {
                    "path": rel(output_path),
                    "sha256": sha(child_output_raw),
                    "row_count": len(output_rows),
                },
                "source_context": verification["source_context"],
                "git_commit": verification["git_commit"],
                "evidence_ref_map": refs,
                "row_provenance": row_provenance,
            }
        )

    if set(joined_rows_by_identity) != parent_identity_set or len(joined_rows_by_identity) != 80:
        raise AssertionError("child union does not exactly cover the parent 80 identities")
    if len(all_original_rows) != 80:
        raise AssertionError("child row count is not exactly 80")

    joined_rows = [joined_rows_by_identity[identity] for identity in parent_identities]
    output = {
        "source_task": parent["source_task"],
        "batch": parent["batch"],
        "baseline_inventory_sha256": parent["baseline"]["inventory_sha256"],
        "input_file_sha256": sha(parent_raw),
        "partition_sha256": parent["partition_sha256"],
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "source_context": "captured_snapshot",
        "git_commit": COMMIT,
        "operator_decision": copy.deepcopy(operator_decision),
        "scope_omission_decision": {**scope_pin, "applied_to_batch": False},
        "parent_input": {
            "path": rel(PARENT_INPUT),
            "sha256": sha(parent_raw),
            "partition_sha256": parent["partition_sha256"],
        },
        "child_tasks": [f"CA-P-{task_id}" for task_id in CHILD_TASKS],
        "child_receipts": child_receipts,
        "evidence_catalogue": joined_evidence,
        "nodes": joined_rows,
        "coverage": {
            "parent_identity_count": 80,
            "joined_identity_count": len(joined_rows),
            "child_count": len(CHILD_TASKS),
            "child_row_count": len(all_original_rows),
            "evidence_span_count": len(joined_evidence),
            "disposition_counts": dict(sorted(Counter(row["disposition"] for row in joined_rows).items())),
            "evidence_namespace": "<child source_task>/<original evidence_ref>",
            "original_rows_preserved_by": "child_receipts.row_provenance.row_canonical_sha256",
        },
    }
    provenance = {
        "parent_input_paths": child_input_paths,
        "child_output_paths": [receipt["output"]["path"] for receipt in child_receipts],
        "child_row_canonical_sha256_records": sum((receipt["row_provenance"] for receipt in child_receipts), []),
    }
    output["provenance"] = provenance
    return output, provenance


def output_bytes(output: dict[str, Any]) -> bytes:
    return (json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def assert_output_scope() -> None:
    """Keep the create-only output inside the owned projection directory."""

    if OUTPUT.is_symlink():
        raise AssertionError("joined output must not be a symlink")
    try:
        OUTPUT.resolve(strict=False).relative_to(NODES.resolve())
    except ValueError as exc:
        raise AssertionError("joined output escapes the owned nodes directory") from exc
    if OUTPUT.exists() and not OUTPUT.is_file():
        raise AssertionError("joined output exists but is not a regular file")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true", help="create the joined output, refusing mismatched existing content")
    parser.add_argument("--verify-output", action="store_true", help="verify existing output without writing")
    args = parser.parse_args()
    if args.persist and args.verify_output:
        parser.error("--persist and --verify-output are mutually exclusive")

    assert_output_scope()
    output, _ = build_join()
    generated = output_bytes(output)
    generated_sha = sha(generated)
    exists = OUTPUT.exists()
    existing_matches = exists and OUTPUT.read_bytes() == generated

    if args.verify_output:
        if not exists:
            raise FileNotFoundError(f"joined output does not exist: {OUTPUT}")
        if not existing_matches:
            raise AssertionError("existing joined output differs from the deterministic rebuild")
        verified = verify_node_reviews.verify(7, str(PARENT_INPUT), str(OUTPUT))
        print(json.dumps({"mode": "verify-output", "output": rel(OUTPUT), "sha256": generated_sha, "verification": verified}, sort_keys=True))
        return

    if args.persist:
        if exists:
            if not existing_matches:
                raise FileExistsError("refusing to overwrite mismatched existing joined output")
            outcome = "already_persisted"
        else:
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            with OUTPUT.open("xb") as handle:
                handle.write(generated)
            outcome = "persisted"
        print(json.dumps({"mode": "persist", "outcome": outcome, "output": rel(OUTPUT), "sha256": generated_sha}, sort_keys=True))
        return

    print(
        json.dumps(
            {
                "mode": "dryrun",
                "would_write": not exists,
                "existing_matches": existing_matches if exists else None,
                "output": rel(OUTPUT),
                "sha256": generated_sha,
                "identities": len(output["nodes"]),
                "evidence_spans": len(output["evidence_catalogue"]),
                "dispositions": output["coverage"]["disposition_counts"],
                "child_tasks": output["child_tasks"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
