---
atom_id: CA-P-2075@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 62
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Atom
  - Subject
  - Projection
  - Plan
  - Operator
version: 2
updated_at: 2026-10-11 05:28:54 +0400
relations:
  is_decomposition_of:
  - CA-P-1966
---
# Summary

Review relation and Subject mapping candidates

## Objective

Independently review the assigned proposed mappings without changing authoritative Subjects.

## Details

Estimated own work: at most 15 minutes. Review exactly the 23 proposed occurrences in relations_subjects.review.json under Stage 2 supplements. The unresolved input rows are not this Task's completion claim and remain tracked by CA-P-2049 and its existing children.

Read the current supplement/review contracts and exact owning evidence for each proposed occurrence. Confirm current full-file and span pins, source meaning, candidate basis and preservation of qualifiers. A valid hash or a root-list citation alone is not semantic acceptance. Below 90% confidence, do not accept.

Output only `.caprmedio_caprmedio/_projection/core-entity-review/stage2/semantic-reviews/task-2075.review.json`: pin all report inputs and current grammar/decision evidence; give one accepted, rejected, stale or unresolved disposition per assigned proposed occurrence, with concrete evidence/reason. Keep all proposed edits non-executable. Group repeated reasons only when every occurrence remains explicitly accounted for. A stale source is not automatically rebound or repaired.

Latest compact notation has only /, . and :. @ has no carrier/display role; D atoms own storage. The role/type selector-versus-narrower-kind question is unanswered. Do not infer its answer, introduce selectors, silently turn a Type value into a subtype, collapse a specific named workflow/step to a generic definition, attach Revision to Artifact, or create per-property Carrier bindings. Candidate display paths are not native-kind admission.

Workers own only their disjoint review output. They are not alone in the worktree; preserve all other edits. No governing Source, existing supplement, frozen ledger/candidate, code, Plans, Journal, Git, MCP/FPF, runtime or live graph writes. Root owns integration and the completed Task commit. A review receipt does not complete source migration or its parent mapping group.

### Definition of Done

Not Done if any assigned proposal is unaccounted for, stale/unsupported meaning is accepted, old qualifiers or identity are discarded, confidence is guessed, a pending Operator choice is inferred, source/frozen evidence changes, or own work exceeds 15 minutes without decomposition.

### Completion

Reviewed all 23 assigned proposals: 23 accepted. Root verified exact coverage, current source and Main Content span pins, input pins, confidence, approved notation and non-executable outputs.

All 23 selected occurrences have current own source/span evidence. The raw relations_subjects report still has three stale grammar references; this separately pinned review supplies current grammar evidence without rebinding the raw report or treating it as migration-ready.

Done means this bounded review is complete, not that rejected/unresolved mappings, the parent research or source migration are complete. The original research report and captured inputs remain unchanged. The receipt records the Task version-1 input as historical evidence; Task closure changes only this Plan to version 2.
