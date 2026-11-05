---
atom_id: CA-R-2263
ref_id: CA-R-2263
role: Requirement
form: Rule
current_scope_unit: FRAMEWORK_METHODOLOGY
status: Active
author: Anatoly Maslennikov
tier: 1
topics:
  main_subject: 'Entity/Aspect/Product: CAPRMEDIO Framework'
version: 1
updated_at: 2026-10-29 09:32:49 +0400
container:
  scope_unit: CA-SU-9
carrier_destination:
  file:
    name: CA-R-2263-FRAMEWORK_METHODOLOGY-RULE--automatically-initialize-the-session-engine.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement
---
## Summary

Automatically initialize the session engine

## Claim

CAPRMEDIO **must** initialize its session engine at session start **and** **after** context compaction **without** requiring an operator command.

The session engine here means the Runtime responsible for the current Session and context, not a separately introduced model kind. C610 tracks its concrete Engine owner for later implementation.

## Details

Preserves the meaning of the legacy methodology Requirement CAPRMEDIO-METHODOLOGY-REQU-507-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--automatically-initialize-the-session-engine. Its archived carrier retains the original header and provenance.
