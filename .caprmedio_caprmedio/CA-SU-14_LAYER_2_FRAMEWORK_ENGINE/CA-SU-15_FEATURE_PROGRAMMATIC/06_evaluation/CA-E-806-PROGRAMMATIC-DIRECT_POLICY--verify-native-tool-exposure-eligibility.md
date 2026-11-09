---
identity:
  atom_id: CA-E-806
  ref_id: CA-E-806
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
    name: CA-E-806-PROGRAMMATIC-DIRECT_POLICY--verify-native-tool-exposure-eligibility.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---

## Summary

Verify native Tool exposure eligibility

## Claim

### Prose Claim

A Tool passes frontier exposure eligibility only when it is active native code configured for the bound Project. Inactive, disabled or blocked Tools, internal CONNECTORS/adapters, and PROJECT_TOOLS are excluded and cannot become callable through stale publication.

Verify that editing or removing unrelated Atoms does not change exposure or trigger a generic registration freshness scan.
