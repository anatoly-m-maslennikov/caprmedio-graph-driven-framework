---
atom_id: CA-M-270
ref_id: CA-M-270@31-draft
container:
  scope_unit: CA-SU-9
role: Method
form: Implementation Method
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design"
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design"
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations:
  child_of:
  - CA-M-261
status: Draft
version: 31
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-M-270@31-draft-FRAMEWORK_METHODOLOGY-IMPLEMENTATION_METHOD--prepare-verification-before-refactoring.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/05_method/000_draft
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: FRAMEWORK_METHODOLOGY
---
## Summary
Prepare verification before refactoring

## Claim

### Prose Claim


**to** refactor existing Implementation, prepare the applicable verification **before** changing the target Implementation:

1. derive regression checks, end-to-end checks, acceptance gates, **and** canary criteria from the applicable Evaluations; select techniques by applicability rather than requiring **every** technique for **every** change. apply the governing Methods within Delivery boundaries while implementing these checks.
2. evaluate the existing Implementation using controlled complete inputs **and** record its outputs **and** existing failures as baseline evidence. expected correctness remains governed by RMED; an existing defect **must not** become a Requirement merely because it appears **in** the baseline.
3. evaluate the refactored candidate against current RMED **and** the recorded baseline under CA-M-262, using the implementation loop **and** retry policy. preserve the applicable checks across the comparison **unless** an authorized RMED change establishes a new baseline under CA-R-1559.
4. apply the required release gates **before** full rollout. **when** canary testing applies, prepare its criteria **before** refactoring **and** execute it on the candidate **after** that Implementation exists during the authorized controlled rollout.

this existing-Implementation baseline is comparison evidence, **not** missing specification recovered from old code, **and** is **not** a prerequisite for a fresh reconstruction with no existing Implementation.
