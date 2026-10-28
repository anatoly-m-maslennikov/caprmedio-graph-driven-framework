---
atom_id: CA-P-2678@4
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 4
updated_at: 2026-10-27 19:45:11 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2673
tier: 4
---
# Summary

Map Candidate #10 Governs Subjects

## Objective

Map the selected Current RMEDO Atoms’ Governs Subjects to the accepted Candidate #10 structure before mapping dependencies.

## Details

Start with a fresh inventory of the Current Requirement, Method, Evaluation, Delivery and Operations source set used by the Subject Graph. Record the actual source boundary and counts; do not assume the earlier snapshot count remains current. Treat the prepared 42 Drafts as a separate proposed input, not Current sources.

Continue the existing thin change table in P2675 as the single live inventory. Keep four columns: Atom ID | old Subject | new Subject | status. Use a Governs section first; link real Drafts from the Atom IDs. Do not create a second map with copied Claims, hashes or extended analyses.

Map by meaning, using A1218 and the accepted A1219/A1220 decisions. Shared concepts use the CAPRMEDIO namespace; project-specific concepts use the project namespace. Owning Scope Unit does not select the Subject namespace. Do not copy Tool or Scope Unit names into topic branches.

Create or refine only the necessary source-update Drafts as mappings become supported. Reuse the prepared next-version Draft instead of creating another successor for the same source. Keep unrelated content unchanged. Mark unsupported mappings explicitly; ask the Operator one concrete question at a time below 90% confidence and save each accepted decision in its own Specification Proposal.

## Definition of Done

Every selected Current Governs Subject has an evidenced proposed target, unchanged disposition or explicit unresolved question. The thin inventory and actual Drafts agree; no source promotion or migration has run.


## References

- [A1218 — Candidate #10](../../02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [A1219 — Mixed Subject targets](../../02_analysis/CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md).
- [A1220 — Project as a whole entity](../../02_analysis/CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md).
- [P2675 — Existing thin Draft/change inventory](done/02-CA-P-2675-TASK--draft-main-subject-definitions.md).

## Progress

Fresh inventory: 2,258 Current RMEDO Atoms. The first 803 Engineering, UX and Documentation Governs changes are Drafted; Current sources remain unchanged. Remaining source groups are being resolved before dependency mapping.


### Retained temporal classifications

Decision: [A1221](../../02_analysis/CA-A-1221-SPECIFICATION_PROPOSAL--retain-continuant-and-occurrent-subjects.md). R1967 and R1972 are Subject-mapping Drafts; their meanings are unchanged.

### Formal references and generic Type rules

- [CA-A-1222](../../02_analysis/CA-A-1222-SPECIFICATION_PROPOSAL--update-formal-subject-references.md).
- [CA-A-1223](../../02_analysis/CA-A-1223-SPECIFICATION_PROPOSAL--govern-nodes-with-generic-type-rules.md).
