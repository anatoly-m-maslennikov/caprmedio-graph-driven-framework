---
identity:
  atom_id: CA-E-644
  ref_id: CA-E-644@17
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
      Structure
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  tier: 4
relations:
  evaluation_for:
  - CA-M-402
  - CA-M-403
state:
  status: Archived
  version: 17
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-E-644@17-PROGRAMMATIC-DIRECT_POLICY--evaluate-declared-behavior-and-canonical-ownership.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Evaluate declared behavior and canonical ownership

## Claim

### Prose Claim

Accept implementation only when each implemented, in-scope declared Requirement or Delivery obligation has an identifiable canonical implementation owner, without silently adding business policy. Prefer fewer coherent units and modules, but do not impose an artificial one-to-one cardinality. Shared behavior may be many-to-many when semantic ownership remains unambiguous.

## Details

### Scope

Implementation changes realizing declared PROGRAMMATIC Requirement or Delivery obligations in modules, units, adapters, Tools, Apps, MCP and workflows. Unimplemented obligations outside the admitted change do not require invented realization.

- Map each applicable Requirement or Delivery obligation to the actual module or unit that owns its behavior; a relation or projection is not proof.
- Exercise representative callers and adapters to verify delegation to the canonical owner rather than divergent reimplementation.
- Reject invented policy, approval, lifecycle or validation behavior not declared by active authority.
- Accept cohesive helpers and shared adapters when they preserve one semantic owner; reject duplicate decisions, unexplained sprawl or boundary leakage.
- Record deliberate splits or cross-unit relations with their reason and evidence; locality is a preference, not a hard file-count rule.
