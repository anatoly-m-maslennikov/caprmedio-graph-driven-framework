---
atom_id: CA-R-1802
ref_id: CA-R-1802@16
container:
  scope_unit: CA-SU-24
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation/Traceability
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Coverage
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
tier: 3
status: Archived
version: 16
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1802@16-PROMPTS-RULE--keep-review-completion-separate-from-applied-edits.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement/archive
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
## Summary

Keep review completion separate from applied edits

## Claim scope

completion results produced by the RMED review prompt Implementation for a selected Atom **or** selection.

## Claim

### Prose Claim

the Implementation **must** report completion **only** from complete initial check coverage **and** resolved findings, rather than from the existence of a report **or** an applied edit.

## Details

- an initial failed check is a completed check with a finding; a blocked **or** unperformed check is incomplete coverage.
- confirmed findings are resolved by an authorized correction **or** a recorded rejection supported by the supplied rules. partial correction does **not** resolve remaining findings **or** coverage.
- **every** finding retains its own disposition. a nonempty correction list **or** an empty unresolved list alone does **not** establish that **all** findings were handled. a correction-permission blocker does **not** turn a concluded initial check into an unperformed check.
- a completed selection requires completion evidence for **every** selected Atom. independent completed Atoms remain distinguishable from the unfinished selection.
- completion after fixes records completion of the admitted one-pass work, **not** a claim that saved output passed another Evaluation. this specification adds no recheck Step.
