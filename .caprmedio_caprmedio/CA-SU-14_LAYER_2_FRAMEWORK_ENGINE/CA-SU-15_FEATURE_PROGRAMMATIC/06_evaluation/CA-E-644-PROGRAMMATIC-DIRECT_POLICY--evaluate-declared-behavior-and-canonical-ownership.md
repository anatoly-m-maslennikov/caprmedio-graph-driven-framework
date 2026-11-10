---
identity:
  atom_id: CA-E-644
  ref_id: CA-E-644
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Component Structure
    dependencies:
    - MODEL//CAPRMEDIO <+ Package/Project Package
  tier: 4
relations:
  evaluation_for:
  - CA-M-402
  - CA-M-403
state:
  status: Active
  version: 18
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-644-PROGRAMMATIC-DIRECT_POLICY--evaluate-declared-behavior-and-canonical-ownership.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Evaluate declared behavior and canonical ownership

## Claim

### Prose Claim

Each implemented in-scope Requirement/Delivery obligation has identifiable canonical behavior owner, verified through callers/adapters. Allow coherent shared many-to-many ownership but reject invented policy, duplicate decisions and leakage; record deliberate splits with evidence.
