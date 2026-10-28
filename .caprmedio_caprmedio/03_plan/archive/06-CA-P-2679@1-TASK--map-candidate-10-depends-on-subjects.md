---
atom_id: CA-P-2679@1
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

Map Candidate #10 Depends On Subjects

## Objective

Map affected Depends On Subjects after the Governs meanings have been settled.

## Details

Start after P2678. Use a separate Depends On section in the same thin P2675 inventory, with the same four columns. Follow the approved Governs targets and the actual prerequisite meaning of each source; do not infer a new dependency solely from a shared prefix.

Preserve unrelated Atom relations and property values. Retain the existing instance, qualification and property suffixes unless an explicitly reviewed structural correction is necessary; this is not an instance-name, Type or property-schema redesign.

The previously retained Term dependency targets remain explicit mapping questions. Resolve only the target-path choices needed for this migration; Terms Graph implementation and general Term-content work remain deferred. Do not silently remove an unresolved target, invent a new entity, or hide it in the rebuilt view.

Refine the same source Draft used for its Governs correction, where applicable. Do not create competing next versions. Keep each accepted new decision in one Specification Proposal and link it from the work record.

## Definition of Done

Every affected dependency reference has a supported target, an evidenced unchanged disposition or a recorded unresolved question. Governs and Depends On edits for each source are combined in one proposed successor; Current sources remain unchanged.


## References

- [A1218 — Candidate #10](../../../02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [A1219 — Mixed Subject targets](../../../02_analysis/CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md).
- [A1220 — Project as a whole entity](../../../02_analysis/CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md).
- [P2675 — Existing thin Draft/change inventory](../done/02-CA-P-2675-TASK--draft-main-subject-definitions.md).
