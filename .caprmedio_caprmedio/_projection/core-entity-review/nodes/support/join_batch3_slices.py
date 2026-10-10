#!/usr/bin/env python3
"""Join the six completed batch-3 slice reviews without semantic alteration."""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from functools import lru_cache

ROOT = pathlib.Path.cwd()
NODES = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes"
PLAN_ROOT = ROOT / ".caprmedio_caprmedio/03_plan"
PARENT_INPUT = NODES / "inputs/nodes.batch-3.input.json"
OUTPUT = NODES / "nodes.batch-3.review.json"
sys.path.insert(0, str(NODES / "support"))
from snapshot_sources import COMMIT, verify_snapshot  # noqa: E402
from verify_node_reviews import verify  # noqa: E402

CHILD_TASKS = (
    "CA-P-1939", "CA-P-1940", "CA-P-1941",
    "CA-P-1942", "CA-P-1943", "CA-P-1944",
)
CAPTURED_TASK_RECEIPT_PREFIX = "bdc700939"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def file_sha(path):
    return sha(path.read_bytes())


def require_regular(path):
    assert path.is_file() and not path.is_symlink(), path


def require_output_scope():
    assert NODES.is_dir() and not NODES.is_symlink(), NODES
    assert OUTPUT.parent == NODES and OUTPUT.name == "nodes.batch-3.review.json", OUTPUT
    assert OUTPUT.parent.resolve() == NODES.resolve(), OUTPUT
    if OUTPUT.exists():
        require_regular(OUTPUT)


def plan_metadata(raw, path):
    text = raw.decode("utf-8")
    if not text.startswith("---\n"):
        return None
    frontmatter = text.split("---\n", 2)[1]
    atom_id = re.search(r"^atom_id:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
    status = re.search(r"^status:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
    version = re.search(r"^version:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
    updated_at = re.search(r'^updated_at:\s*"?([^"\n]+)"?\s*$', frontmatter, re.MULTILINE)
    if not atom_id or not status:
        return None
    return {
        "atom_id": atom_id.group(1),
        "status": status.group(1),
        "path": str(path),
        "sha256": sha(raw),
        "version": version.group(1) if version else None,
        "updated_at": updated_at.group(1) if updated_at else None,
    }


@lru_cache(maxsize=1)
def captured_task_receipt_commit():
    completed = subprocess.run(
        ["git", "rev-parse", f"{CAPTURED_TASK_RECEIPT_PREFIX}^{{commit}}"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout.decode().strip()
    assert re.fullmatch(r"[0-9a-f]{40}", completed), completed
    return completed


@lru_cache(maxsize=1)
def captured_done_plans():
    commit = captured_task_receipt_commit()
    plan_root = str(PLAN_ROOT.relative_to(ROOT))
    found = {}
    for atom_id in CHILD_TASKS:
        candidates = subprocess.run(
            ["git", "grep", "-l", "-z", "-F", f"atom_id: {atom_id}", commit, "--", plan_root],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout.split(b"\0")
        candidates = [candidate.decode().split(":", 1)[1] for candidate in candidates if candidate]
        assert len(candidates) == 1, (atom_id, candidates)
        relative_path = candidates[0]
        raw = subprocess.run(
            ["git", "show", f"{commit}:{relative_path}"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
        record = plan_metadata(raw, relative_path)
        assert record and record["atom_id"] == atom_id and record["status"] == "Done", record
        found[atom_id] = record
    assert set(found) == set(CHILD_TASKS), sorted(found)
    return found


def locate_live_done_plan(atom_id, expected_sha):
    matches = []
    for path in PLAN_ROOT.rglob("*.md"):
        record = plan_metadata(path.read_bytes(), path.relative_to(ROOT))
        if record and record["atom_id"] == atom_id:
            matches.append(record)
    assert len(matches) == 1, (atom_id, [record["path"] for record in matches])
    live = matches[0]
    assert live["status"] == "Done" and live["sha256"] == expected_sha, live


def captured_done_plan(atom_id):
    record = captured_done_plans()[atom_id]
    locate_live_done_plan(atom_id, record["sha256"])
    return record


def remap_evidence_refs(value, names):
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if key == "evidence_refs":
                assert isinstance(item, list), item
                assert all(ref in names for ref in item), item
                result[key] = [names[ref] for ref in item]
            else:
                result[key] = remap_evidence_refs(item, names)
        return result
    if isinstance(value, list):
        return [remap_evidence_refs(item, names) for item in value]
    return value


def all_evidence_refs(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "evidence_refs":
                yield from item
            else:
                yield from all_evidence_refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from all_evidence_refs(item)


def child_paths(task):
    return (
        NODES / "inputs/slices" / f"{task}.input.json",
        NODES / "slices" / f"{task}.review.json",
    )


def compose():
    require_regular(PARENT_INPUT)
    parent_raw = PARENT_INPUT.read_bytes()
    parent = json.loads(parent_raw)
    assert parent["source_task"] == "CA-P-1931" and parent["batch"] == 3
    assert len(parent["nodes"]) == 80
    parent_identities = [node["identity"] for node in parent["nodes"]]
    assert len(set(parent_identities)) == 80
    snapshot = verify_snapshot()
    assert snapshot["git_commit"] == COMMIT and snapshot["source_pins_checked"] == 951

    evidence_catalogue = {}
    rows_by_identity = {}
    child_provenance = {}
    child_verifications = []
    all_child_identities = []
    for task in CHILD_TASKS:
        input_path, output_path = child_paths(task)
        require_regular(input_path)
        require_regular(output_path)
        child_input_raw = input_path.read_bytes()
        child_output_raw = output_path.read_bytes()
        child_input = json.loads(child_input_raw)
        child_review = json.loads(child_output_raw)
        assert child_input["source_task"] == task == child_review["source_task"]
        assert child_input["batch"] == child_review["batch"] == 3
        assert child_input["parent_source_task"] == "CA-P-1931"
        assert child_input["parent_input"] == {
            "path": str(PARENT_INPUT.relative_to(ROOT)),
            "sha256": file_sha(PARENT_INPUT),
            "partition_sha256": parent["partition_sha256"],
        }
        indexes = child_input["subset_indexes"]
        assert child_input["nodes"] == [parent["nodes"][index] for index in indexes]
        assert child_review["input_file_sha256"] == sha(child_input_raw)
        assert child_review["partition_sha256"] == child_input["partition_sha256"]
        assert child_review["baseline_inventory_sha256"] == parent["baseline"]["inventory_sha256"]
        verification = verify(3, input_path=input_path, output_path=output_path)
        child_verifications.append({"source_task": task, **verification})
        plan = captured_done_plan(task)

        raw_catalogue = child_review["evidence_catalogue"]
        if isinstance(raw_catalogue, list):
            assert all(isinstance(item, dict) and item.get("evidence_ref") for item in raw_catalogue)
            assert len({item["evidence_ref"] for item in raw_catalogue}) == len(raw_catalogue)
            local_catalogue = {item["evidence_ref"]: item for item in raw_catalogue}
        else:
            assert isinstance(raw_catalogue, dict)
            local_catalogue = raw_catalogue
        ref_names = {local_ref: f"{task}::{local_ref}" for local_ref in local_catalogue}
        assert len(set(ref_names.values())) == len(ref_names)
        for local_ref, evidence in local_catalogue.items():
            global_ref = ref_names[local_ref]
            copied = copy.deepcopy(evidence)
            assert copied.get("evidence_ref", local_ref) == local_ref
            copied["evidence_ref"] = global_ref
            assert copied["quote"] == evidence["quote"]
            assert copied["text_sha256"] == evidence["text_sha256"]
            assert global_ref not in evidence_catalogue
            evidence_catalogue[global_ref] = copied

        provenance_rows = []
        for row in child_review["nodes"]:
            identity = row["identity"]
            assert identity not in rows_by_identity, identity
            remapped = remap_evidence_refs(copy.deepcopy(row), ref_names)
            assert remapped["reason"] == row["reason"]
            assert remapped["disposition"] == row["disposition"]
            assert remapped["confidence_percent"] == row["confidence_percent"]
            assert remapped["proposal"] == remap_evidence_refs(row["proposal"], ref_names)
            assert set(all_evidence_refs(remapped)) <= set(evidence_catalogue)
            rows_by_identity[identity] = remapped
            all_child_identities.append(identity)
            provenance_rows.append({
                "identity": identity,
                "row_canonical_sha256": sha(canonical(row)),
                "row": copy.deepcopy(row),
            })
        child_provenance[task] = {
            "plan": plan,
            "input": {
                "path": str(input_path.relative_to(ROOT)),
                "sha256": sha(child_input_raw),
                "partition_sha256": child_input["partition_sha256"],
                "subset_indexes": indexes,
            },
            "output": {
                "path": str(output_path.relative_to(ROOT)),
                "sha256": sha(child_output_raw),
                "evidence_ref_namespace": f"{task}::",
            },
            "source_context": {
                key: copy.deepcopy(child_review[key])
                for key in ("source_context", "captured_git_commit", "review_context", "snapshot_verification", "current_core_claimed")
                if key in child_review
            },
            "rows": provenance_rows,
        }

    assert len(all_child_identities) == 80 and len(set(all_child_identities)) == 80
    assert set(all_child_identities) == set(parent_identities)
    output_rows = [rows_by_identity[identity] for identity in parent_identities]
    assert len(output_rows) == 80
    for row in output_rows:
        assert set(all_evidence_refs(row)) <= set(evidence_catalogue)
    return {
        "source_task": "CA-P-1931",
        "batch": 3,
        "baseline_inventory_sha256": parent["baseline"]["inventory_sha256"],
        "input_file_sha256": sha(parent_raw),
        "partition_sha256": parent["partition_sha256"],
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "source_context": {
            "kind": "captured_snapshot",
            "git_commit": COMMIT,
            "baseline_inventory_path": parent["baseline"]["path"],
            "baseline_inventory_file_sha256": parent["baseline"]["sha256"],
            "current_core_claimed": False,
            "snapshot_verification": snapshot,
        },
        "parent_input": {
            "path": str(PARENT_INPUT.relative_to(ROOT)),
            "sha256": sha(parent_raw),
            "partition_sha256": parent["partition_sha256"],
        },
        "child_review_provenance": child_provenance,
        "child_verifications": child_verifications,
        "evidence_catalogue": evidence_catalogue,
        "nodes": output_rows,
    }


def report(review, output_sha, outcome):
    counts = {}
    for row in review["nodes"]:
        counts[row["disposition"]] = counts.get(row["disposition"], 0) + 1
    return {
        "outcome": outcome,
        "batch": 3,
        "identities": len(review["nodes"]),
        "child_tasks": list(CHILD_TASKS),
        "evidence_spans": len(review["evidence_catalogue"]),
        "dispositions": counts,
        "file_sha256": output_sha,
        "source_context": "captured_snapshot",
        "git_commit": COMMIT,
        "semantic_admission": "not_performed",
    }


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--persist", action="store_true")
    mode.add_argument("--verify-output", action="store_true")
    args = parser.parse_args()
    require_output_scope()
    review = compose()
    raw = (json.dumps(review, ensure_ascii=False, indent=2) + "\n").encode()
    output_sha = sha(raw)
    if args.verify_output:
        require_regular(OUTPUT)
        assert OUTPUT.read_bytes() == raw, "joined output differs from reproducible slice join"
        verification = verify(3, input_path=PARENT_INPUT, output_path=OUTPUT)
        print(json.dumps({**report(review, output_sha, "verified"), "parent_verification": verification}, sort_keys=True))
        return
    if args.persist:
        if OUTPUT.exists():
            require_regular(OUTPUT)
            assert OUTPUT.read_bytes() == raw, "refusing to overwrite mismatched joined output"
            outcome = "already_matching"
        else:
            with OUTPUT.open("xb") as handle:
                handle.write(raw)
            outcome = "created"
        print(json.dumps(report(review, output_sha, outcome), sort_keys=True))
        return
    print(json.dumps(report(review, output_sha, "dry_run"), sort_keys=True))


if __name__ == "__main__":
    main()
