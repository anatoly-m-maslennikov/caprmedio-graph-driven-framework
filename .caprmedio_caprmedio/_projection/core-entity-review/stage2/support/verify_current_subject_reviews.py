"""One-off read-only evidence checks, not semantic acceptance or a reusable Tool."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
from typing import Any

from verify_current_inventory import ROOT, STAGE2_REL, relative_path, require, sha

CAPTURED_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"


def evidence_bytes(root: Path, pin: dict[str, Any]) -> bytes:
    """Current derived pins may also name their captured-input provenance."""
    require(isinstance(pin, dict) and "path" in pin and "sha256" in pin, "evidence pin shape")
    path = relative_path(root, pin["path"], "evidence pin")
    commit = pin.get("git_commit", pin.get("commit"))
    require(commit is None or commit == CAPTURED_COMMIT, "exact captured evidence commit")
    if path.is_file():
        raw = path.read_bytes()
        if sha(raw) == pin["sha256"]:
            return raw
    require(commit == CAPTURED_COMMIT, "current frozen evidence pin")
    try:
        raw = subprocess.check_output(["git", "show", f"{commit}:{pin['path']}"], cwd=root, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as error:
        raise AssertionError("captured evidence carrier exists") from error
    require(sha(raw) == pin["sha256"], "captured evidence pin")
    return raw


def pinned_json(root: Path, relative: str, digest: str | None = None) -> dict[str, Any]:
    path = relative_path(root, relative, "review evidence")
    require(path.is_file(), "regular evidence file")
    raw = path.read_bytes()
    if digest is not None:
        require(sha(raw) == digest, "exact evidence file pin")
    value = json.loads(raw)
    require(isinstance(value, dict), "evidence JSON object")
    return value


def pointer_value(document: Any, pointer: str) -> Any:
    require(isinstance(pointer, str), "candidate pointer string")
    pointer = pointer.removeprefix("#")
    require(pointer.startswith("/"), "nonempty exact candidate JSON pointer")
    value = document
    for part in pointer[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            require(part.isdigit() and int(part) < len(value), "candidate list pointer")
            value = value[int(part)]
        else:
            require(isinstance(value, dict) and part in value, "candidate object pointer")
            value = value[part]
    return value


def verify_review(root: Path, number: int, report: dict[str, Any] | None = None) -> dict[str, Any]:
    require(type(number) is int and 1 <= number <= 51, "review batch number")
    stage = STAGE2_REL.as_posix()
    manifest = pinned_json(root, stage + "/current-subjects.batches.json")
    descriptor = manifest["batches"][number - 1]
    batch = pinned_json(root, descriptor["path"], descriptor["sha256"])
    inventory_path = relative_path(root, manifest["inventory_path"], "inventory")
    require(sha(inventory_path.read_bytes()) == batch["input_inventory_sha256"], "inventory pin")
    inventory = pinned_json(root, manifest["inventory_path"], batch["input_inventory_sha256"])
    input_pins = inventory.get("input_pins", {})
    require(isinstance(input_pins, dict), "inventory input pin map")
    for pin in input_pins.values():
        evidence_bytes(root, pin)
    if report is None:
        report = pinned_json(root, stage + f"/reviews/current-subjects.batch-{number:03d}.review.json")
    require(report.get("schema_version") == 1 and report.get("non_authoritative") is True, "report form")
    require(report.get("source_migration") == report.get("native_admission") == "not_performed", "no source/native effects")
    require(report.get("task_id") == f"CA-P-{1991 + number}", "review Task ID")
    require(report.get("batch_id") == batch["batch_id"], "review batch ID")
    require(report.get("input_batch_path") == descriptor["path"], "batch path binding")
    require(report.get("input_batch_sha256") == descriptor["sha256"], "batch SHA binding")
    require(report.get("input_inventory_sha256") == batch["input_inventory_sha256"], "inventory binding")

    pins = report.get("evidence_pins")
    if isinstance(pins, dict):
        pins = list(pins.values())
    require(isinstance(pins, list), "evidence pin list")
    pin_paths: set[str] = set()
    for pin in pins:
        require(isinstance(pin, dict) and "path" in pin and "sha256" in pin, "evidence pin shape")
        require(pin["path"] not in pin_paths, "unique evidence pins")
        pin_paths.add(pin["path"])
        if pin["path"] in input_pins:
            require(pin["sha256"] == input_pins[pin["path"]]["sha256"], "report frozen inventory evidence pin")
        evidence_bytes(root, pin)
    candidate_path = ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
    required_pins = {candidate_path, ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json", stage + "/current-subjects.contract.md", stage + "/current-subjects.review.contract.md"}
    require(required_pins <= pin_paths, "required candidate/review/contract pins")
    candidate = pinned_json(root, candidate_path)

    expected_sources = batch["selected_sources"]
    sources = report.get("source_reviews")
    require(isinstance(sources, list) and len(sources) == len(expected_sources), "source coverage")
    require(all(isinstance(s, dict) for s in sources), "source review objects")
    by_source = {s["relative_path"]: s for s in expected_sources}
    require(Counter(s.get("relative_path") for s in sources) == Counter(by_source.keys()), "exact source identities")
    source_lines: dict[str, list[bytes]] = {}
    body_start: dict[str, int] = {}
    for row in sources:
        source = by_source[row["relative_path"]]
        for key in ("relative_path", "full_file_sha256", "atom_id", "version", "quarantined", "findings"):
            require(row.get(key) == source[key], "exact source metadata/finding copy")
        read = row.get("main_content_read")
        require(read is True or isinstance(read, dict), "source content read")
        if isinstance(read, dict):
            require(read.get("read", True) is True, "source content read flag")
        dispositions = row.get("finding_dispositions")
        require(isinstance(dispositions, list), "finding disposition list")
        require(all(isinstance(d, dict) for d in dispositions), "finding disposition objects")
        require(Counter(d.get("finding") for d in dispositions) == Counter(source["findings"]), "exact finding dispositions")
        require(all(isinstance(d.get("reason"), str) and d["reason"].strip() for d in dispositions), "finding reasons")
        require(isinstance(row.get("questions"), list), "source questions explicit")
        path = relative_path(root, source["relative_path"], "current owning source")
        raw = path.read_bytes()
        require(sha(raw) == source["full_file_sha256"], "current owning source pin")
        lines = raw.splitlines(keepends=True)
        require(lines and lines[0].strip() == b"---", "source frontmatter delimiter")
        ending = next((i + 1 for i, line in enumerate(lines[1:], 1) if line.strip() == b"---"), None)
        require(ending is not None, "source body boundary")
        source_lines[source["relative_path"]] = lines
        body_start[source["relative_path"]] = ending + 1
        if isinstance(read, dict):
            require(read.get("path") == source["relative_path"] and read.get("sha256") == source["full_file_sha256"], "read span owning source")
            start, end = read.get("start_line"), read.get("end_line")
            require(type(start) is int and type(end) is int and ending + 1 <= start <= end <= len(lines), "read content span range")
            require(sha(b"".join(lines[start - 1:end])) == read.get("span_sha256"), "read content span digest")

    expected_occurrences = batch["occurrences"]
    rows = report.get("occurrences")
    require(isinstance(rows, list) and len(rows) == len(expected_occurrences), "occurrence coverage")
    require(all(isinstance(r, dict) for r in rows), "occurrence review objects")
    expected_by_id = {r["occurrence_id"]: r for r in expected_occurrences}
    require(Counter(r.get("occurrence_id") for r in rows) == Counter(expected_by_id.keys()), "exact occurrence identities")
    decisions: Counter[str] = Counter()
    for row in rows:
        expected = expected_by_id[row["occurrence_id"]]
        require(all(row.get(k) == v for k, v in expected.items()), "exact occurrence input copy")
        require(row.get("executable") is False, "candidate only")
        decision = row.get("decision")
        require(decision in {"unchanged", "proposed", "unresolved"}, "review decision")
        confidence = row.get("confidence")
        require(type(confidence) in (int, float) and 0 <= confidence <= 1, "numeric confidence")
        proposed = row.get("proposed_value")
        require(isinstance(row.get("reason"), str) and row["reason"].strip(), "meaning reason")
        require(row.get("question") is None or isinstance(row["question"], str), "question shape")
        require(isinstance(row.get("preserved_distinctions"), list) and all(isinstance(v, str) for v in row["preserved_distinctions"]), "preserved distinctions")
        if decision == "unresolved":
            require(proposed is None, "unresolved has no guessed value")
        else:
            require(confidence >= .90 and isinstance(proposed, str) and proposed.strip(), "decided value/confidence")
            require((proposed == expected["old_value"]) == (decision == "unchanged"), "decision value consistency")
        basis = row.get("candidate_basis", [])
        require(isinstance(basis, list), "candidate basis list")
        if decision == "proposed":
            require(bool(basis), "candidate basis required for proposals")
        for item in basis:
            require(isinstance(item, dict) and "pointer" in item, "candidate rule object")
            pointer_value(candidate, item["pointer"])
            require(isinstance(item.get("reason"), str) and item["reason"].strip(), "candidate rule reason")
        evidence = row.get("evidence")
        require(isinstance(evidence, list) and evidence, "current evidence for every occurrence")
        source = by_source[expected["source_path"]]
        own_spans = 0
        for span in evidence:
            require(isinstance(span, dict), "evidence span object")
            raw = evidence_bytes(root, span)
            lines = raw.splitlines(keepends=True)
            start, end = span["start_line"], span["end_line"]
            require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), "span line range")
            require(sha(b"".join(lines[start - 1:end])) == span["span_sha256"], "exact span byte digest")
            require(isinstance(span.get("reason"), str) and span["reason"].strip(), "span meaning reason")
            if span["path"] == source["relative_path"] and span["sha256"] == source["full_file_sha256"]:
                require(start >= body_start[span["path"]], "owning span is content, not metadata")
                own_spans += 1
        require(own_spans > 0, "owning current content evidence")
        decisions[decision] += 1
    return {"outcome": "PASS", "batch": number, "sources": len(sources), "occurrences": len(rows), "decisions": dict(decisions), "scope": "structural evidence only; meaning requires independent review"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=int, required=True)
    args = parser.parse_args()
    try:
        result = verify_review(ROOT, args.batch)
    except (AssertionError, OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}))
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
