---
identity:
  atom_id: CA-E-644
  ref_id: CA-E-644@15-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
      Structure
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  tier: 4
relations:
  evaluation_for:
  - CA-M-402
  - CA-M-403
  - CA-M-411
state:
  status: Draft
  version: 15
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-E-644@15-draft-PROGRAMMATIC-DIRECT_POLICY--evaluate-declared-behavior-and-canonical-ownership.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/draft/engine-refinement-20261108
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Evaluate declared behavior and canonical ownership

## Scope

Implementation changes realizing declared PROGRAMMATIC Requirement or Delivery obligations in modules, units, adapters, Tools, Apps, MCP and workflows. Unimplemented obligations outside the admitted change do not require invented realization.

## Claim

Accept implementation only when each implemented, in-scope declared Requirement or Delivery obligation has an identifiable canonical implementation owner, without silently adding business policy. Prefer fewer coherent units and modules, but do not impose an artificial one-to-one cardinality. Shared behavior may be many-to-many when semantic ownership remains unambiguous.

## Details

- Map each applicable Requirement or Delivery obligation to the actual module or unit that owns its behavior; a relation or projection is not proof.
- Exercise representative callers and adapters to verify delegation to the canonical owner rather than divergent reimplementation.
- Reject invented policy, approval, lifecycle or validation behavior not declared by active authority.
- Accept cohesive helpers and shared adapters when they preserve one semantic owner; reject duplicate decisions, unexplained sprawl or boundary leakage.
- Record deliberate splits or cross-unit relations with their reason and evidence; locality is a preference, not a hard file-count rule.
