---
identity:
  atom_id: CA-M-432
  ref_id: CA-M-432
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
      Structure
  tier: 1
state:
  status: Active
  version: 10
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-M-432-PROGRAMMATIC-SOLUTION--use-a-modular-monolith.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Use a modular monolith

## Claim

### Prose Claim

Implement the PROGRAMMATIC runtime as one modular application with shared queue and run state. Keep clear module boundaries aligned with Scope Unit responsibilities. Scope ownership does not require a one-to-one mapping to modules or deployments. Do not introduce separate services or internal network APIs merely to separate Scope Units.

## Details

### Scope

New or changed PROGRAMMATIC runtime implementation, including all descendant
Scope Units that contribute to that runtime.

Adapters, Single Actions, schedulers, Workflows, the Action Engine and MCP retain
distinct responsibilities within the shared runtime. Scope Units define
responsibility and ownership, not deployment boundaries.
