---
atom_id: CA-P-2462
ref_id: CA-P-2462
role: Plan
form: Plan
label: Task
work_sequence_number: 51
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
relations:
  is_decomposition_of:
  - CA-P-2401
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
container:
  atom: CA-P-2401
carrier_destination:
  file:
    name: 51-CA-P-2462-TASK--implement-draft-marker-create-and-update.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done
---
# Summary

Implement Draft marker Create and Update

## Objective

Implement canonical parser/Create/Update compatibility without broadening canonical ID lookup or allocating numbers for Draft markers. Acceptance: focused parser and lifecycle functional checks, no history or Journal admission gate.

## Details

At most 15 minutes own work; split before extending. Follow the current PROGRAMMATIC M projection and Core07 D276@21, D288@21, D378@16, D446@16, D568@8, D570@12. Preserve unrelated work. Review dependent successors before execution.

### Definition of Done

Implement canonical parser/Create/Update compatibility without broadening canonical ID lookup or allocating numbers for Draft markers. Acceptance: focused parser and lifecycle functional checks, no history or Journal admission gate.

No deployment, live migration/staging, held-batch replay or Methodology map update. Use synthetic golden Projects and nonproduction test instances only.

### Verified execution checkpoint

Published Draft marker forms are parsed and supported through Create/Update and exact filename/path read/search. Canonical ID grammar and Current/Archived semantics remain strict. Independent marker suite 6, parser/Atom cohort 30 and full promotion 22 passed; final review APPROVE. Temporary unsupported-promotion test expectations were removed only after implementation and replaced with actual sealed-input refusal checks.
