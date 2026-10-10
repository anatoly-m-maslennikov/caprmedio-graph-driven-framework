---
atom_id: CA-P-2000
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 2
updated_at: "2026-10-11 01:54:51 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
  depends_on: ["CA-P-1972", "CA-P-1988", "CA-P-1989", "CA-P-1990"]
  blocks: ["CA-P-2043"]
---
# Summary

Review current Subject batch 009

## Objective

Account for every assigned current Subject occurrence with live meaning evidence and no guessed replacement.

## Details

Estimated own work: 15 minutes. Required prerequisites: CA-P-1972, CA-P-1988, CA-P-1989, CA-P-1990 Done. Read and pin `.caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.contract.md` SHA-256 `5eb0d90022b68a7d1d2cd27cf60a147deaf4161cb9b2e1c8bdf6c4ef8f2a10bf` and `.caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.review.contract.md` SHA-256 `b7c9c065f997d5bae1409f5c09b4223d08327a523decab6d26c2e4425fd2c28b`. Input: `.caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-009.json`, SHA-256 `f23bbf6dd98a3aabf2f8a6d84109acd27da6db782595af02b076dedec1b1cf64`; inventory SHA-256 `e284dbe4943568bc75b7f9ba63ebf583372a60813e62eee3d43b5b75b270220a`. This batch owns 20 sources and 88 occurrences exclusively.

Recheck each source pin, then read its current Main Content. Compare the frozen candidate/review as separate evidence; do not refresh captured files or infer meaning from a label alone. Return one row per occurrence under the review-output contract: unchanged, proposed or unresolved; exact old value, nullable proposed value, confidence, current evidence spans/hashes, preserved distinctions and any concrete question. Below 90%, leave the replacement null. Report quarantined sources and unresolved findings. No deletion, source write, grammar adoption, native admission or schema/key rename.

Own only `stage2/reviews/current-subjects.batch-009.review.json` and an optional same-batch support helper. Root owns integration and Git. Preserve others' edits. If work exceeds 15 minutes, create bounded decomposition before continuing. Creating this Plan does not start or complete review.

Completion: root independently verified all 20 current source pins and all 88 occurrences, then read the owning Main Content for the 1 proposed and 28 unchanged decisions. The Summary mapping preserves its Atom bearer. The 59 unresolved rows remain explicit research in the report and required ledger integration; no replacement is guessed. All rows remain non-executable. Evidence: stage2/task-2000.receipt.json. This completed review is not completed mapping or migration approval.

### Definition of Done

Not Done if a pin is stale, coverage overlaps or omits an assigned occurrence/source finding, a proposal lacks current meaning evidence, uncertainty is hidden, Core or captured files change, or own work exceeds 15 minutes without decomposition. A completed proposal is not migration approval.
