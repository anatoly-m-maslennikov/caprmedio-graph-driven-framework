"""Preview-first, one-off aggregation of accepted current-Subject reviews.

This is CA-P-2046 preparation, not a migration or a reusable framework Tool.
It intentionally refuses to aggregate until every review Plan, receipt, report,
and independent verifier is current.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
from typing import Any, Callable

from verify_current_inventory import (
    CarrierError,
    ROOT,
    STAGE2_REL,
    parse_carrier,
    read_json,
    relative_path,
    require,
    sha,
    verify_inventory,
)
from verify_current_subject_reviews import verify_review


OWNERSHIP_REL = STAGE2_REL / "current-subjects.review.ownership.json"
LEDGER_REL = STAGE2_REL / "current-subjects.mapping-ledger.json"
SOURCE_CONTRACT_REL = STAGE2_REL / "current-subjects.contract.md"
REVIEW_CONTRACT_REL = STAGE2_REL / "current-subjects.review.contract.md"
EXPECTED_SOURCE_CONTRACT_SHA = "5eb0d90022b68a7d1d2cd27cf60a147deaf4161cb9b2e1c8bdf6c4ef8f2a10bf"
EXPECTED_REVIEW_CONTRACT_SHA = "b7c9c065f997d5bae1409f5c09b4223d08327a523decab6d26c2e4425fd2c28b"
EXPECTED_SOURCES = 907
EXPECTED_OCCURRENCES = 4534
EXPECTED_QUARANTINED_SOURCES = 8
EXPECTED_REVIEW_TASKS = 51
REQUIRED_PREPARATION_RECEIPTS = ("CA-P-1972", "CA-P-1988", "CA-P-1989", "CA-P-1990")


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _pin(root: Path, relative: str, label: str) -> dict[str, str]:
    path = relative_path(root, relative, label)
    require(path.is_file() and not path.is_symlink(), f"{label} regular file")
    return {"path": relative, "sha256": sha(path.read_bytes())}


def _load(root: Path, relative: str, label: str) -> dict[str, Any]:
    return read_json(relative_path(root, relative, label), label)


def _receipt_relative(task_id: str) -> str:
    return (STAGE2_REL / f"task-{task_id.removeprefix('CA-P-')}.receipt.json").as_posix()


def _plan_relative(root: Path, registered: str) -> str:
    """Resolve a registered active Plan path or its same-name `done/` carrier."""

    candidate = relative_path(root, registered, "review Plan")
    done = candidate.parent / "done" / candidate.name
    existing = [path for path in (candidate, done) if path.exists() or path.is_symlink()]
    require(len(existing) == 1, "one registered review Plan carrier")
    path = existing[0]
    require(path.is_file() and not path.is_symlink(), "review Plan regular file")
    return _relative(root, path)


def _done_plan(root: Path, task: dict[str, Any]) -> dict[str, str]:
    registered = task.get("plan_path")
    require(isinstance(registered, str), "registered review Plan path")
    relative = _plan_relative(root, registered)
    path = relative_path(root, relative, "review Plan")
    try:
        metadata = parse_carrier(path.read_bytes(), path).metadata
    except CarrierError as error:
        raise AssertionError("review Plan parses") from error
    require(metadata.get("atom_id") == task.get("task_id"), "review Plan identity")
    require(metadata.get("status") == "Done", "review Plan Done status")
    relations = metadata.get("relations")
    require(isinstance(relations, dict), "review Plan relations")
    require(relations.get("is_decomposition_of") == ["CA-P-1966"], "review Plan decomposition")
    return _pin(root, relative, "review Plan")


def _receipt(root: Path, task: dict[str, Any], report: dict[str, Any], report_pin: dict[str, str]) -> dict[str, str]:
    task_id = task["task_id"]
    relative = _receipt_relative(task_id)
    receipt = _load(root, relative, "review receipt")
    require(receipt.get("task") == task_id, "review receipt task identity")
    output = receipt.get("output")
    require(isinstance(output, dict), "review receipt output")
    require(output == report_pin, "review receipt current report pin")
    input_batch = receipt.get("input_batch")
    require(
        input_batch == {"path": task.get("input_batch_path"), "sha256": task.get("input_batch_sha256")},
        "review receipt input batch pin",
    )
    checks = receipt.get("checks")
    require(isinstance(checks, dict), "review receipt checks")
    require(checks.get("independent_structural_verifier") == "PASS", "review receipt independent verifier")
    require(checks.get("sources") == task.get("source_count"), "review receipt source count")
    require(checks.get("occurrences") == task.get("occurrence_count"), "review receipt occurrence count")
    require(checks.get("all_executable_false") is True, "review receipt executable boundary")
    decisions = Counter(row.get("decision") for row in report.get("occurrences", []))
    for decision in ("proposed", "unchanged", "unresolved"):
        require(checks.get(decision) == decisions[decision], f"review receipt {decision} count")
    return _pin(root, relative, "review receipt")


def _preparation_receipts(root: Path) -> list[dict[str, str]]:
    pins: list[dict[str, str]] = []
    for task_id in REQUIRED_PREPARATION_RECEIPTS:
        relative = _receipt_relative(task_id)
        receipt = _load(root, relative, "preparation receipt")
        require(receipt.get("task") == task_id, "preparation receipt task identity")
        require(isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS"), "preparation receipt PASS")
        pins.append(_pin(root, relative, "preparation receipt"))
    return pins


def _report(root: Path, task: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    relative = task.get("output_path")
    require(isinstance(relative, str), "registered review report path")
    report = _load(root, relative, "review report")
    pin = _pin(root, relative, "review report")
    require(report.get("task_id") == task.get("task_id"), "review report task identity")
    require(report.get("input_batch_path") == task.get("input_batch_path"), "review report batch path")
    require(report.get("input_batch_sha256") == task.get("input_batch_sha256"), "review report batch SHA")
    return report, pin


def _exact_report_coverage(
    task: dict[str, Any], batch: dict[str, Any], report: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    expected_sources = batch.get("selected_sources")
    expected_occurrences = batch.get("occurrences")
    rows = report.get("source_reviews")
    occurrences = report.get("occurrences")
    require(isinstance(expected_sources, list) and isinstance(rows, list), "report source lists")
    require(isinstance(expected_occurrences, list) and isinstance(occurrences, list), "report occurrence lists")
    require(len(rows) == task.get("source_count") == len(expected_sources), "registered report source count")
    require(len(occurrences) == task.get("occurrence_count") == len(expected_occurrences), "registered report occurrence count")
    expected_by_source = {row["relative_path"]: row for row in expected_sources}
    require(len(expected_by_source) == len(expected_sources), "batch source identities unique")
    require(Counter(row.get("relative_path") for row in rows) == Counter(expected_by_source.keys()), "exact report source coverage")
    for row in rows:
        expected = expected_by_source[row["relative_path"]]
        for key in ("relative_path", "full_file_sha256", "atom_id", "version", "quarantined", "findings"):
            require(row.get(key) == expected.get(key), "integrated source data unchanged")
    expected_by_occurrence = {row["occurrence_id"]: row for row in expected_occurrences}
    require(len(expected_by_occurrence) == len(expected_occurrences), "batch occurrence identities unique")
    require(
        Counter(row.get("occurrence_id") for row in occurrences) == Counter(expected_by_occurrence.keys()),
        "exact report occurrence coverage",
    )
    for row in occurrences:
        expected = expected_by_occurrence[row["occurrence_id"]]
        require(all(row.get(key) == value for key, value in expected.items()), "integrated occurrence data unchanged")
        require(row.get("executable") is False, "integrated executable boundary")
        decision = row.get("decision")
        proposed = row.get("proposed_value")
        confidence = row.get("confidence")
        require(decision in {"unchanged", "proposed", "unresolved"}, "integrated decision")
        require(type(confidence) in (int, float) and 0 <= confidence <= 1, "integrated confidence")
        if decision == "unresolved":
            require(proposed is None, "integrated unresolved null")
        else:
            require(confidence >= 0.90 and isinstance(proposed, str) and proposed.strip(), "integrated decided value")
    return rows, occurrences


def build_ledger(
    root: Path = ROOT,
    *,
    inventory_verifier: Callable[..., dict[str, Any]] = verify_inventory,
    review_verifier: Callable[..., dict[str, Any]] = verify_review,
) -> dict[str, Any]:
    """Build, but do not write, the fully pinned derived ledger."""

    root = Path(root).resolve()
    require(root.is_dir(), "repository root exists")
    inventory_result = inventory_verifier(root)
    require(inventory_result.get("outcome") == "PASS", "independent inventory verifier")
    require(inventory_result.get("selected_sources") == EXPECTED_SOURCES, "expected selected source count")
    require(inventory_result.get("occurrences") == EXPECTED_OCCURRENCES, "expected occurrence count")
    require(inventory_result.get("batches") == EXPECTED_REVIEW_TASKS, "expected batch count")

    inventory_relative = (STAGE2_REL / "current-subjects.inventory.json").as_posix()
    manifest_relative = (STAGE2_REL / "current-subjects.batches.json").as_posix()
    ownership_relative = OWNERSHIP_REL.as_posix()
    inventory = _load(root, inventory_relative, "inventory")
    manifest = _load(root, manifest_relative, "batch manifest")
    ownership = _load(root, ownership_relative, "review ownership")
    inventory_pin = _pin(root, inventory_relative, "inventory")
    manifest_pin = _pin(root, manifest_relative, "batch manifest")
    ownership_pin = _pin(root, ownership_relative, "review ownership")
    require(manifest.get("inventory_path") == inventory_relative, "manifest inventory path")
    require(inventory.get("schema_version") == 1 and inventory.get("non_authoritative") is True, "inventory form")
    sources = inventory.get("selected_sources")
    expected_occurrences = inventory.get("occurrences")
    require(isinstance(sources, list) and len(sources) == EXPECTED_SOURCES, "inventory source count")
    require(isinstance(expected_occurrences, list) and len(expected_occurrences) == EXPECTED_OCCURRENCES, "inventory occurrence count")
    require(sum(row.get("quarantined") is True for row in sources) == EXPECTED_QUARANTINED_SOURCES, "inventory quarantine count")
    require(ownership.get("inventory_sha256") == inventory_pin["sha256"], "ownership inventory pin")
    require(ownership.get("batches_manifest_sha256") == manifest_pin["sha256"], "ownership manifest pin")
    require(ownership.get("counts") == {"sources": EXPECTED_SOURCES, "occurrences": EXPECTED_OCCURRENCES, "review_tasks": EXPECTED_REVIEW_TASKS, "integration_tasks": 1}, "ownership counts")

    source_contract_pin = _pin(root, SOURCE_CONTRACT_REL.as_posix(), "source contract")
    review_contract_pin = _pin(root, REVIEW_CONTRACT_REL.as_posix(), "review contract")
    require(source_contract_pin["sha256"] == EXPECTED_SOURCE_CONTRACT_SHA, "source contract pin")
    require(review_contract_pin["sha256"] == EXPECTED_REVIEW_CONTRACT_SHA, "review contract pin")
    require(ownership.get("review_contract_sha256") == review_contract_pin["sha256"], "ownership review contract pin")

    tasks = ownership.get("review_tasks")
    descriptors = manifest.get("batches")
    require(isinstance(tasks, list) and len(tasks) == EXPECTED_REVIEW_TASKS, "all review Tasks registered")
    require(isinstance(descriptors, list) and len(descriptors) == EXPECTED_REVIEW_TASKS, "all review batches registered")
    expected_task_ids = [f"CA-P-{1992 + index}" for index in range(EXPECTED_REVIEW_TASKS)]
    require([task.get("task_id") for task in tasks] == expected_task_ids, "all review Task identities")
    require(len({task.get("output_path") for task in tasks}) == EXPECTED_REVIEW_TASKS, "unique review report paths")

    preparation_pins = _preparation_receipts(root)
    report_pins: list[dict[str, str]] = []
    receipt_pins: list[dict[str, str]] = []
    plan_pins: list[dict[str, str]] = []
    integrated_sources: list[dict[str, Any]] = []
    integrated_occurrences: list[dict[str, Any]] = []
    all_sources: list[str] = []
    all_occurrences: list[str] = []

    for number, (task, descriptor) in enumerate(zip(tasks, descriptors), start=1):
        require(task.get("input_batch_path") == descriptor.get("path"), "task batch path binding")
        require(task.get("input_batch_sha256") == descriptor.get("sha256"), "task batch SHA binding")
        require(task.get("source_count") == descriptor.get("source_count"), "task source count binding")
        require(task.get("occurrence_count") == descriptor.get("occurrence_count"), "task occurrence count binding")
        plan_pins.append(_done_plan(root, task))
        report, report_pin = _report(root, task)
        review_result = review_verifier(root, number, report)
        require(review_result.get("outcome") == "PASS", "independent review verifier")
        require(review_result.get("sources") == task.get("source_count"), "independent review source count")
        require(review_result.get("occurrences") == task.get("occurrence_count"), "independent review occurrence count")
        batch = _load(root, descriptor["path"], "review input batch")
        require(sha(relative_path(root, descriptor["path"], "review input batch").read_bytes()) == descriptor["sha256"], "review input batch pin")
        source_rows, occurrence_rows = _exact_report_coverage(task, batch, report)
        receipt_pins.append(_receipt(root, task, report, report_pin))
        report_pins.append(report_pin)
        origin = {"originating_review_path": report_pin["path"], "originating_review_sha256": report_pin["sha256"], "task_id": task["task_id"], "batch_id": report["batch_id"]}
        integrated_sources.extend({**row, **origin} for row in source_rows)
        integrated_occurrences.extend({**row, **origin} for row in occurrence_rows)
        all_sources.extend(row["relative_path"] for row in source_rows)
        all_occurrences.extend(row["occurrence_id"] for row in occurrence_rows)

    expected_source_paths = [row["relative_path"] for row in sources]
    expected_occurrence_ids = [row["occurrence_id"] for row in expected_occurrences]
    require(Counter(all_sources) == Counter(expected_source_paths), "aggregate source exact coverage")
    require(len(all_sources) == len(set(all_sources)) == EXPECTED_SOURCES, "aggregate source no overlap")
    require(Counter(all_occurrences) == Counter(expected_occurrence_ids), "aggregate occurrence exact coverage")
    require(len(all_occurrences) == len(set(all_occurrences)) == EXPECTED_OCCURRENCES, "aggregate occurrence no overlap")

    integrated_occurrences.sort(key=lambda row: row["occurrence_id"])
    integrated_sources.sort(key=lambda row: row["relative_path"])
    decisions = Counter(row["decision"] for row in integrated_occurrences)
    unresolved = [
        {
            "occurrence_id": row["occurrence_id"],
            "task_id": row["task_id"],
            "originating_review_path": row["originating_review_path"],
            "originating_review_sha256": row["originating_review_sha256"],
            "question": row["question"],
        }
        for row in integrated_occurrences
        if row["decision"] == "unresolved"
    ]
    return {
        "schema_version": 1,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "scope": "CA-P-2045 gated derived occurrence ledger only; no semantic acceptance or migration authorization.",
        "pin_index": {
            "inventory": inventory_pin,
            "batches_manifest": manifest_pin,
            "ownership": ownership_pin,
            "contracts": [source_contract_pin, review_contract_pin],
            "preparation_receipts": preparation_pins,
            "plans": plan_pins,
            "reports": report_pins,
            "review_receipts": receipt_pins,
        },
        "counts": {
            "sources": len(integrated_sources),
            "occurrences": len(integrated_occurrences),
            "quarantined_sources": sum(row["quarantined"] is True for row in integrated_sources),
            "quarantined_occurrences": sum(row["quarantined"] is True for row in integrated_occurrences),
            "review_tasks": len(tasks),
            "decisions": dict(sorted(decisions.items())),
            "unresolved": len(unresolved),
        },
        "source_reviews": integrated_sources,
        "occurrences": integrated_occurrences,
        "unresolved_occurrence_refs": unresolved,
    }


def persist_ledger(root: Path = ROOT, **kwargs: Any) -> dict[str, Any]:
    """Create the one derived ledger once, after all gates have passed."""

    root = Path(root).resolve()
    ledger = build_ledger(root, **kwargs)
    target = relative_path(root, LEDGER_REL.as_posix(), "derived ledger")
    require(not target.exists() and not target.is_symlink(), "derived ledger create-only")
    require(target.parent.is_dir() and not target.parent.is_symlink(), "derived ledger directory")
    try:
        with target.open("xb") as handle:
            handle.write(json.dumps(ledger, indent=2, sort_keys=True).encode() + b"\n")
    except FileExistsError as error:
        raise AssertionError("derived ledger create-only") from error
    return ledger


def _preview(ledger: dict[str, Any]) -> dict[str, Any]:
    return {
        "outcome": "PREVIEW",
        "scope": ledger["scope"],
        "counts": ledger["counts"],
        "unresolved_occurrence_count": len(ledger["unresolved_occurrence_refs"]),
        "would_create": LEDGER_REL.as_posix(),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--persist", action="store_true", help="create the derived ledger once after every gate passes")
    args = parser.parse_args(argv)
    try:
        ledger = persist_ledger(args.root) if args.persist else build_ledger(args.root)
    except (AssertionError, OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True), file=sys.stderr)
        return 1
    result = {
        "outcome": "CREATED",
        "path": LEDGER_REL.as_posix(),
        "counts": ledger["counts"],
        "scope": ledger["scope"],
    } if args.persist else _preview(ledger)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
