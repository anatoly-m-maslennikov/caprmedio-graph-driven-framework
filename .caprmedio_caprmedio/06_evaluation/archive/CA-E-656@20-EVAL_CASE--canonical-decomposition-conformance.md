---
version: 20
updated_at: 2026-11-02 00:18:22 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-M-447
  - CA-R-642
  child_of:
  - CA-R-642
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  passive:
  - Project
  - Atom/(.Role := Concern)
cce_version: cce_1
cce_form: evaluation
current_scope_unit: caprmedio
status: Archived
atom_id: CA-E-656@20
tier: 2
role: Evaluation
form: Eval Case
---
## Summary

Canonical decomposition conformance

## Claim

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
