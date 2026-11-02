---
atom_id: CA-E-644@12
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Component Structure
  depends_on:
  - Subject/Graph Node/Engineering/Behavior Ownership
  - Subject/Graph Node/Engineering/Implementation Cohesion
relations:
  evaluation_for:
  - CA-M-402
  - CA-M-403
  - CA-M-411
tier: 4
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
