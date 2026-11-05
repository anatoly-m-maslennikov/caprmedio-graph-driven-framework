---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Verification
version: 23
updated_at: 2026-11-02 18:35:20 +0400
atom_id: CA-R-1503
ref_id: CA-R-1503
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1503-CORE_META_MODEL-RULE--keep-evaluation-atoms-mechanism-neutral.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Keep Evaluation Atoms mechanism-neutral

## Claim

### Prose Claim


Evaluation Atom check definitions and their implementation mechanisms.


an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.

## Details

automated tests, model-judged evaluations, statistical assessments, rubrics, manual reviews, **and** other implementation mechanisms **may** realize that check. choosing a mechanism does **not** change the governing Evaluation Atom's Claim.
