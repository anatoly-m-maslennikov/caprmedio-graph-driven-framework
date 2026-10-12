"""Print an apply_patch for bounded Subject-review Plans; never write Plans or mappings."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE = Path(".caprmedio_caprmedio/_projection/core-entity-review/stage2")
PLAN_ROOT = Path(
    ".caprmedio_caprmedio/03_plan/18-CA-P-1959-EPIC--improve-entity-model-stage-2/"
    "08-CA-P-1966-EPIC--map-current-core-subject-origins"
)
PREPARATION_CONTRACT = STAGE / "current-subjects.contract.md"
REVIEW_CONTRACT = STAGE / "current-subjects.review.contract.md"
PREREQUISITES = ("CA-P-1972", "CA-P-1988", "CA-P-1989", "CA-P-1990")
FIRST_PLAN_NUMBER = 1992
LAST_PLAN_NUMBER = 2043
EXPECTED_PLAN_COUNT = LAST_PLAN_NUMBER - FIRST_PLAN_NUMBER + 1
RECEIPTS = {
    "CA-P-1988": STAGE / "task-1988.receipt.json",
    "CA-P-1989": STAGE / "task-1989.receipt.json",
    "CA-P-1990": STAGE / "task-1990.receipt.json",
}

SUPPORT = Path(__file__).resolve().parent
if str(SUPPORT) not in sys.path:
    sys.path.insert(0, str(SUPPORT))
from verify_current_inventory import VerificationError, relative_path, sha, verify_inventory  # noqa: E402

VALIDATOR_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS"
if str(VALIDATOR_ROOT) not in sys.path:
    sys.path.insert(0, str(VALIDATOR_ROOT))
from validate_atoms_workers.parsing import CarrierError, parse_carrier  # noqa: E402


def fail(message: str) -> None:
    raise SystemExit(message)


def safe_file(relative: Path, label: str) -> Path:
    try:
        path = relative_path(ROOT, relative.as_posix(), label)
    except VerificationError as error:
        fail(str(error))
    if not path.is_file() or path.is_symlink():
        fail(f"missing regular {label}: {relative}")
    return path


def read_object(relative: Path, label: str) -> dict[str, Any]:
    path = safe_file(relative, label)
    try:
        value = json.loads(path.read_bytes())
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail(f"invalid {label}: {relative}")
        raise AssertionError("unreachable") from error
    if not isinstance(value, dict):
        fail(f"invalid {label} object: {relative}")
    return value


def header(
    atom_id: str,
    sequence: int,
    timestamp: str,
    blocks: list[str],
    depends_on: list[str],
) -> str:
    return f"""---
atom_id: {atom_id}
content_role: Plan
type: Plan
label: Task
work_sequence_number: {sequence}
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 1
updated_at: "{timestamp}"
relations:
  is_decomposition_of: [CA-P-1966]
  depends_on: {json.dumps(depends_on)}
  blocks: {json.dumps(blocks)}
---
"""


def validate_receipt_outputs(receipt_id: str, receipt: dict[str, Any]) -> None:
    if receipt.get("task") != receipt_id or not str(receipt.get("result", "")).startswith("PASS"):
        fail(f"invalid prerequisite receipt: {receipt_id}")
    outputs = receipt.get("outputs")
    if not isinstance(outputs, list) or not outputs:
        fail(f"missing output pins in prerequisite receipt: {receipt_id}")
    for index, output in enumerate(outputs, start=1):
        if not isinstance(output, dict) or not isinstance(output.get("path"), str) or not isinstance(
            output.get("sha256"), str
        ):
            fail(f"invalid output pin {index} in prerequisite receipt: {receipt_id}")
        try:
            path = relative_path(ROOT, output["path"], f"{receipt_id} output {index}")
        except VerificationError as error:
            fail(str(error))
        if not path.is_file() or path.is_symlink() or sha(path.read_bytes()) != output["sha256"]:
            fail(f"stale output pin {index} in prerequisite receipt: {receipt_id}")


def validate_prerequisite_receipts(inventory_sha: str, manifest_sha: str) -> None:
    receipts = {receipt_id: read_object(path, f"{receipt_id} receipt") for receipt_id, path in RECEIPTS.items()}
    for receipt_id, receipt in receipts.items():
        validate_receipt_outputs(receipt_id, receipt)

    snapshot_checks = receipts["CA-P-1989"].get("checks")
    if not isinstance(snapshot_checks, dict) or snapshot_checks.get("current_inventory_sha256") != inventory_sha:
        fail("stale current inventory pin in prerequisite receipt: CA-P-1989")
    verifier_pins = receipts["CA-P-1990"].get("input_pins")
    if verifier_pins != {"inventory": inventory_sha, "batches_manifest": manifest_sha}:
        fail("stale inventory or batch pin in prerequisite receipt: CA-P-1990")


def validate_plan_collisions(outputs: list[tuple[Path, str]]) -> None:
    """Reject target-path and frontmatter-ID collisions, including renamed carriers."""

    planned_ids = {
        match.group(1)
        for _, content in outputs
        if (match := re.search(r"^atom_id: (CA-P-\d+)$", content, re.MULTILINE)) is not None
    }
    if len(planned_ids) != len(outputs):
        fail("generated Plan IDs are not unique")
    for path, _ in outputs:
        target = ROOT / path
        if target.exists() or target.is_symlink():
            fail(f"Plan target already exists: {path}")

    atom_id_line = re.compile(rb"(?m)^atom_id:\s*[\"']?(CA-P-\d+)[\"']?(?:\s+#.*)?\s*$")
    carriers_root = ROOT / ".caprmedio_caprmedio"
    for path in sorted(carriers_root.rglob("*.md")):
        relative = path.relative_to(ROOT)
        try:
            checked = relative_path(ROOT, relative.as_posix(), "Plan collision carrier")
        except VerificationError as error:
            fail(str(error))
        if not checked.is_file() or checked.is_symlink():
            fail(f"unsafe Plan collision carrier: {relative}")
        raw = checked.read_bytes()
        raw_ids = {match.group(1).decode("ascii") for match in atom_id_line.finditer(raw)}
        try:
            parsed = parse_carrier(raw, checked)
        except CarrierError as error:
            if planned_ids.intersection(raw_ids) or (
                raw.startswith(b"---") and any(atom_id.encode("ascii") in raw for atom_id in planned_ids)
            ):
                fail(f"malformed carrier could reserve generated Plan ID: {relative} ({error.code})")
            continue
        if parsed.metadata.get("atom_id") in planned_ids:
            fail(f"Plan ID already exists in carrier frontmatter: {parsed.metadata['atom_id']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first-id", type=int, required=True)
    parser.add_argument("--timestamp", required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    args = parser.parse_args()
    if args.first_id != FIRST_PLAN_NUMBER:
        fail(f"expected --first-id {FIRST_PLAN_NUMBER}")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{4}", args.timestamp) is None:
        fail("invalid Project timestamp")

    try:
        verification = verify_inventory(ROOT)
    except (OSError, VerificationError, KeyError, TypeError, ValueError) as error:
        fail(f"inventory verification failed: {error}")
    inventory_path = safe_file(STAGE / "current-subjects.inventory.json", "current inventory")
    manifest_path = safe_file(STAGE / "current-subjects.batches.json", "current batch manifest")
    inventory_sha = sha(inventory_path.read_bytes())
    manifest_sha = sha(manifest_path.read_bytes())
    validate_prerequisite_receipts(inventory_sha, manifest_sha)

    preparation_contract = safe_file(PREPARATION_CONTRACT, "preparation contract")
    review_contract = safe_file(REVIEW_CONTRACT, "review output contract")
    preparation_contract_sha = sha(preparation_contract.read_bytes())
    review_contract_sha = sha(review_contract.read_bytes())
    manifest = read_object(STAGE / "current-subjects.batches.json", "current batch manifest")
    batches = manifest.get("batches")
    if not isinstance(batches, list) or len(batches) != verification["batches"]:
        fail("verified batch manifest changed while preparing Plans")
    if len(batches) + 1 != EXPECTED_PLAN_COUNT:
        fail(f"expected {EXPECTED_PLAN_COUNT - 1} review batches and one integration Plan")

    integration_id = f"CA-P-{args.first_id + len(batches)}"
    if integration_id != f"CA-P-{LAST_PLAN_NUMBER}":
        fail(f"expected integration Plan CA-P-{LAST_PLAN_NUMBER}")
    outputs: list[tuple[Path, str]] = []
    review_ids: list[str] = []
    for index, batch in enumerate(batches):
        if not isinstance(batch, dict):
            fail(f"invalid verified batch descriptor {index + 1}")
        number = f"{index + 1:03d}"
        expected_batch_path = STAGE / "inputs" / f"current-subjects.batch-{number}.json"
        if batch.get("path") != expected_batch_path.as_posix():
            fail(f"verified batch path changed: {number}")
        safe_file(expected_batch_path, f"verified batch {number}")
        if not isinstance(batch.get("sha256"), str) or not isinstance(batch.get("source_count"), int) or not isinstance(
            batch.get("occurrence_count"), int
        ):
            fail(f"invalid verified batch descriptor {number}")
        atom_id = f"CA-P-{args.first_id + index}"
        review_ids.append(atom_id)
        sequence = index + 2
        path = PLAN_ROOT / f"{sequence:02d}-{atom_id}-TASK--review-current-subject-batch-{number}.md"
        text = header(atom_id, sequence, args.timestamp, [integration_id], list(PREREQUISITES)) + f"""# Summary

Review current Subject batch {number}

## Objective

Account for every assigned current Subject occurrence with live meaning evidence and no guessed replacement.

## Details

Estimated own work: 15 minutes. Required prerequisites: {", ".join(PREREQUISITES)} Done. Read and pin `{PREPARATION_CONTRACT.as_posix()}` SHA-256 `{preparation_contract_sha}` and `{REVIEW_CONTRACT.as_posix()}` SHA-256 `{review_contract_sha}`. Input: `{batch['path']}`, SHA-256 `{batch['sha256']}`; inventory SHA-256 `{inventory_sha}`. This batch owns {batch['source_count']} sources and {batch['occurrence_count']} occurrences exclusively.

Recheck each source pin, then read its current Main Content. Compare the frozen candidate/review as separate evidence; do not refresh captured files or infer meaning from a label alone. Return one row per occurrence under the review-output contract: unchanged, proposed or unresolved; exact old value, nullable proposed value, confidence, current evidence spans/hashes, preserved distinctions and any concrete question. Below 90%, leave the replacement null. Report quarantined sources and unresolved findings. No deletion, source write, grammar adoption, native admission or schema/key rename.

Own only `stage2/reviews/current-subjects.batch-{number}.review.json` and an optional same-batch support helper. Root owns integration and Git. Preserve others' edits. If work exceeds 15 minutes, create bounded decomposition before continuing. Creating this Plan does not start or complete review.

### Definition of Done

Not Done if a pin is stale, coverage overlaps or omits an assigned occurrence/source finding, a proposal lacks current meaning evidence, uncertainty is hidden, Core or captured files change, or own work exceeds 15 minutes without decomposition. A completed proposal is not migration approval.
"""
        outputs.append((path, text))

    sequence = len(batches) + 2
    integration_path = PLAN_ROOT / f"{sequence:02d}-{integration_id}-TASK--integrate-current-subject-mapping-ledger.md"
    integration_dependencies = [*PREREQUISITES, *review_ids]
    text = header(integration_id, sequence, args.timestamp, ["CA-P-1967", "CA-P-1909"], integration_dependencies) + f"""# Summary

Integrate current Subject mapping ledger

## Objective

Produce one complete, source-pinned occurrence ledger with every unresolved finding visible.

## Details

Estimated own work: 15 minutes. Required prerequisites: {", ".join(PREREQUISITES)} and all {len(batches)} direct review Tasks Done. Read and pin `{PREPARATION_CONTRACT.as_posix()}` SHA-256 `{preparation_contract_sha}` and `{REVIEW_CONTRACT.as_posix()}` SHA-256 `{review_contract_sha}`. Recheck the inventory SHA-256 `{inventory_sha}`, all batch/source/input pins and each receipt. Verify every selected source/finding and occurrence exactly once, no overlap, unchanged/proposed/unresolved states, evidence spans and confidence. An incomplete review cannot count as Done.

Persist only the derived integrated ledger and verification receipt under stage2. Preserve the original candidate/captured review. Ask only about concrete unresolved design conflicts; missing evidence stays research work. Low-confidence mappings must remain null. If research remains, decompose it into bounded Tasks before completing this Plan. No Core write, grammar adoption, native fact admission or migration approval. CA-P-1909 retains accepted-graph ownership; CA-P-1910–1912 retain sealed approval, application and reproduction. Root owns shared integration and Git.

### Definition of Done

Not Done if any prerequisite is incomplete, a pin is stale, coverage or evidence verification fails, a selected source/finding is missing, unresolved mapping work is hidden, or own work exceeds 15 minutes without decomposition. This ledger alone does not finish or authorize migration.
"""
    outputs.append((integration_path, text))

    validate_plan_collisions(outputs)
    stop = len(outputs) if args.stop is None else args.stop
    if not 0 <= args.start <= stop <= len(outputs):
        fail("invalid Plan slice")
    chosen = outputs[args.start:stop]
    print("*** Begin Patch")
    for path, content in chosen:
        print(f"*** Add File: {ROOT / path}")
        print("\n".join("+" + line for line in content.splitlines()))
    print("*** End Patch")


if __name__ == "__main__":
    main()
