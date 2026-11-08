---
atom_id: CA-M-432
ref_id: CA-M-432@8
container:
  scope_unit: CA-SU-15
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
tier: 1
status: Archived
version: 8
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-432@8-PROGRAMMATIC-ENG_POLICY--use-a-modular-monolith.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archived
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Use a modular monolith

## Scope

New or changed PROGRAMMATIC runtime implementation, including all descendant
Scope Units that contribute to that runtime.

## Claim

Implement the PROGRAMMATIC runtime as one modular application with shared queue
and run state. Keep clear module boundaries aligned with Scope Unit
responsibilities. Do not introduce separate services or internal network APIs
merely to separate Scope Units.

## Details

Adapters, Single Actions, schedulers, Workflows, the Action Engine and MCP retain
distinct responsibilities within the shared runtime. Scope Units define
responsibility and ownership, not deployment boundaries.
