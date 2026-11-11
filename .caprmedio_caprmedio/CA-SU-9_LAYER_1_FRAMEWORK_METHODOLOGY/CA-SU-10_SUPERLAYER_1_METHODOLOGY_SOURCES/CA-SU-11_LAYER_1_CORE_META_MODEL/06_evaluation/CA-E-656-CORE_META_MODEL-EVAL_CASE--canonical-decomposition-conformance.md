---
atom_id: CA-E-656
ref_id: CA-E-656
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
tier: 2
relations:
  evaluation_for:
  - CA-R-642
  child_of:
  - CA-R-642
status: Active
version: 22
updated_at: 2026-11-11 15:57:52 +0400
carrier_destination:
  file:
    name: CA-E-656-CORE_META_MODEL-EVAL_CASE--canonical-decomposition-conformance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Canonical decomposition conformance

## Claim

### Prose Claim


**every** canonical decomposition satisfies CA-R-642.

## Check

for **every** declared axis:

- enumerate the bounded universe; **and**
- classify **every** admissible member.

report **any**:

- missing universe **or** axis declaration;
- an axis without exactly one discriminating question;
- parts at different abstraction levels;
- any assignment of a member outside the declared universe;
- unclassified member;
- multiple same-axis assignments; **or**
- forced near match.

the check **must not** change the governed decomposition.

## Acceptance

pass **only** **when** no conformance issue is found.

## Failure

record **every** issue as a Concern against the narrowest owning scope.
