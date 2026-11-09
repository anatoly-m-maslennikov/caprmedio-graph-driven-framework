---
identity:
  atom_id: CA-E-805
  ref_id: CA-E-805
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface
      Contracts
  tier: 6
relations:
  evaluation_for:
  - CA-M-193
  CONTRIBUTES_TO:
  - CA-E-650
state:
  status: Active
  version: 1
  updated_at: 2026-11-09 07:45:15 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-805-PROGRAMMATIC-DIRECT_POLICY--verify-native-tool-contract-fidelity.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---

## Summary

Verify native Tool contract fidelity

## Claim

### Prose Claim

An active native Tool passes frontier contract fidelity only when its canonical structural request and result schemas, including definitions and required fields, and its decoded request/result payload meaning are preserved. Transport serialization differences are allowed only for a declared outer Project field such as project_root; no other transport-shape drift is introduced.

Verify names and descriptions against the configured code contracts as well as their canonical structural schemas.
