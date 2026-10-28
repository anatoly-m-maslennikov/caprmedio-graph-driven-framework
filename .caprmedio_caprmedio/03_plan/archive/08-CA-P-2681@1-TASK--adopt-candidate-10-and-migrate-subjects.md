---
atom_id: CA-P-2681@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 18:34:34 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2673
tier: 4
---
# Summary

Adopt Candidate #10 and migrate Subjects

## Objective

Apply the reviewed definition Drafts and Subject changes using the existing source-update lifecycle.

## Details

Start only after P2680 accepts the concrete batch. This Task is queued by the Epic expansion; the present planning edit does not execute it.

Adopt only the reviewed prepared definition/anchor Drafts and the accepted mapped source successors. For other sources, change Subjects only. Do not add a general content, role, Type, Tier, ownership, ID-format or governing-configuration migration.

Use the existing Draft → predecessor archive → promotion lifecycle. Check the affected source before writing, increment its Version for the real update, preserve its predecessor history and record actual changes in the Journal. Keep Atom IDs when Summary and Content Role do not change; do not create new IDs for a Subject-path move alone. Existing Archived material and unrelated Drafts remain untouched.

Use the existing supported batch route or already-authorized direct methodology edits; do not build new Tools, runtime services or approval machinery in this Epic. Apply in bounded batches, stop on failure, and record what actually applied so continuation does not replay completed work. Update the thin inventory from Drafted to Applied only after the source change succeeds.

Do not leave an adopted root definition claiming a fully new source structure while silently excluding unresolved selected old roots. Record any explicit transitional/held boundary instead of presenting a partial application as complete.

## Definition of Done

All accepted selected changes are applied with normal version/history records; new definitions are Current; applied sources match the reviewed batch. No silent exclusions, duplicate Current IDs or unreported partial application remain. Code and runtime are unchanged.


## References

- [A1218 — Candidate #10](../../../02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [A1219 — Mixed Subject targets](../../../02_analysis/CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md).
- [A1220 — Project as a whole entity](../../../02_analysis/CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md).
- [P2675 — Existing thin Draft/change inventory](../done/02-CA-P-2675-TASK--draft-main-subject-definitions.md).
