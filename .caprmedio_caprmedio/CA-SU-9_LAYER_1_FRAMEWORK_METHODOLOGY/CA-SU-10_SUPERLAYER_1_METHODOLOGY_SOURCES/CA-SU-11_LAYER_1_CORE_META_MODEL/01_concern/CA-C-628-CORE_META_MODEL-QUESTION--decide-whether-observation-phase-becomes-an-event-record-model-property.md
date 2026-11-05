---
atom_id: CA-C-628
ref_id: CA-C-628
container:
  scope_unit: CA-SU-11
role: Concern
form: Question
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File.Main Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Event Record
tier: 3
status: Resolved
version: 3
updated_at: 2026-11-02 18:02:55 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Decide whether Observation Phase becomes an Event Record model Property

## Question

Should execution-observation labels become an Event Record model Property?

## Resolution

Observation Phase is deferred to a future version. Execution-observation labels remain Journal Carrier data, separate from Event Record.Action.
