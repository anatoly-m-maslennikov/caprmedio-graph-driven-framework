---
atom_id: CA-P-1994
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
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
version: 3
updated_at: "2026-10-11 02:45:32 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
  depends_on: ["CA-P-1972", "CA-P-1988", "CA-P-1989", "CA-P-1990"]
  blocks: ["CA-P-2043"]
---
# Summary

Review current Subject batch 003

## Objective

Account for every assigned current Subject occurrence with live meaning evidence and no guessed replacement.

## Details

Estimated own work: 15 minutes. Required prerequisites: CA-P-1972, CA-P-1988, CA-P-1989, CA-P-1990 Done. Read and pin `.caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.contract.md` SHA-256 `5eb0d90022b68a7d1d2cd27cf60a147deaf4161cb9b2e1c8bdf6c4ef8f2a10bf` and `.caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.review.contract.md` SHA-256 `b7c9c065f997d5bae1409f5c09b4223d08327a523decab6d26c2e4425fd2c28b`. Input: `.caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-003.json`, SHA-256 `04b9a9160f4f5b7a21c18013ff32b858df8488c88513f17d5aaa49897245e8ca`; inventory SHA-256 `e284dbe4943568bc75b7f9ba63ebf583372a60813e62eee3d43b5b75b270220a`. This batch owns 20 sources and 79 occurrences exclusively.

Recheck each source pin, then read its current Main Content. Compare the frozen candidate/review as separate evidence; do not refresh captured files or infer meaning from a label alone. Return one row per occurrence under the review-output contract: unchanged, proposed or unresolved; exact old value, nullable proposed value, confidence, current evidence spans/hashes, preserved distinctions and any concrete question. Below 90%, leave the replacement null. Report quarantined sources and unresolved findings. No deletion, source write, grammar adoption, native admission or schema/key rename.

Own only `stage2/reviews/current-subjects.batch-003.review.json` and an optional same-batch support helper. Root owns integration and Git. Preserve others' edits. If work exceeds 15 minutes, create bounded decomposition before continuing. Creating this Plan does not start or complete review.

Completion: independent structural checks passed for 20 current sources and 79 exact occurrences. Root checked remaining proposal meanings against current defining bodies: explicit Atom Subjects Property, separate historical Revision, and retained Projection Type. Prior review corrected eight unsupported role/Substance/Carrier mappings and the unproved revision qualifier to unresolved. The 9 unresolved rows remain explicit research in the report and required ledger integration. All rows remain non-executable; no original Atom changed. Evidence: stage2/task-1994.receipt.json. Review completion is not mapping completion or migration approval.

Revalidation: Independent revalidation accepted all 22 proposed targets across batches 003, 005 and 006, including the Subjects aggregate Property distinct from the Governed Subject Relation. Five Projection Type or Content Role rows gained precise generic owner/field basis using current defining facts. The high-risk unchanged-row audit found no concrete incorrect mapping decision or qualifier loss. The receipt now pins the repaired report; Git retains the prior evidence revision.

### Definition of Done

Not Done if a pin is stale, coverage overlaps or omits an assigned occurrence/source finding, a proposal lacks current meaning evidence, uncertainty is hidden, Core or captured files change, or own work exceeds 15 minutes without decomposition. A completed proposal is not migration approval.
