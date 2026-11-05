---
atom_id: CA-C-629
ref_id: CA-C-629
role: Concern
form: Question
status: Resolved
version: 3
updated_at: 2026-11-02 16:49:59 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
priority: medium
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
container:
  scope_unit: CA-SU-11
---
## Summary

How should CFEL test and set cardinalities?

## Question

How does CFEL distinguish allowed cardinalities, count tests and count conclusions?

## Resolution

CA-R-2243 and CA-R-2487 already define `{:n}` as an allowed cardinality, `{=n}` as a count test, and `{==n}` as a required or derived count conclusion.
