---
atom_id: CA-P-2680@2
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-27 19:56:47 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2673
tier: 4
---
# Summary

Review Candidate #10 adoption batch

## Objective

Review the concrete definitions and Subject-change batch before applying it.

## Details

Start after P2678 and P2679. Read the actual selected Current sources, their proposed Drafts and the thin inventory together. Use A1218, A1219 and A1220 as the accepted proposal and decision records.

Review the prepared 42-Draft definition/anchor set plus the additional Subject-update Drafts supported by the map. Detect stale or competing successors and preserve unrelated older Drafts. Do not promote every file found in a Draft folder.

Check that Node admits the intended mix of things, descriptions and topics; Project means the whole project entity; Implementation remains directly editable and distinct from Projection; Content Role is a valid classification-axis Subject and role-qualified Atom kinds inherit Atom properties. Ordinary Subject moves do not change role, Type, Tier, Summary, owner or other content.

Keep the review bounded to adoption and Subject mapping. Do not reopen the completed FPF challenge, review instances or property inventories, introduce a new grammar/identity system, or add runtime validation requirements. Resolve concrete unmapped targets or definition conflicts with the Operator before applying the corresponding change. Record the exact reviewed batch and its accepted/excluded/held dispositions.

## Definition of Done

One concrete batch is reviewed with explicit dispositions, supported target definitions and no competing source successors. Necessary target-path questions are resolved or explicitly held; no claim of complete adoption is allowed while an in-scope gap remains.


## References

- [A1218 — Candidate #10](../../02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [A1219 — Mixed Subject targets](../../02_analysis/CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md).
- [A1220 — Project as a whole entity](../../02_analysis/CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md).
- [P2675 — Existing thin Draft/change inventory](done/02-CA-P-2675-TASK--draft-main-subject-definitions.md).

## Review evidence

The exact-diff packet checks 2,258 unchanged Current sources and 2,267 staged Drafts. Bodies differ only in ten of the originally prepared sources. Non-Subject metadata stays unchanged except revision fields and the three approved formal Claim paths. Independent source/difference and primary-view format reviews pass; namespace dependency review is completing. No promotion has run.
