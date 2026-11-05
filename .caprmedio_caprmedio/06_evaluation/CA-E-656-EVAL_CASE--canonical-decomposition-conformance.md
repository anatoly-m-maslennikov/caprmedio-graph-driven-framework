---
version: 21
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-M-447
  - CA-R-642
  child_of:
  - CA-R-642
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
cce_version: cce_1
cce_form: evaluation
current_scope_unit: caprmedio
status: Active
atom_id: CA-E-656
ref_id: CA-E-656
tier: 2
role: Evaluation
form: Eval Case
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-E-656-CAPRMEDIO-EVAL_CASE--canonical-decomposition-conformance.md
    path: .caprmedio_caprmedio/06_evaluation
---
## Summary

Canonical decomposition conformance

## Claim

### Prose Claim


**every** canonical decomposition satisfies CA-M-447 **and** CA-R-642.

## Check

for **every** declared axis:

- enumerate the bounded universe; **and**
- classify **every** admissible member.

report **any**:

- missing universe **or** axis declaration;
- unclassified member;
- multiple same-axis assignments; **or**
- forced near match.

the check **must not** change the governed decomposition.

## Acceptance

pass **only** **when** no conformance issue is found.

## Failure

record **every** issue as a Concern against the narrowest owning scope.
