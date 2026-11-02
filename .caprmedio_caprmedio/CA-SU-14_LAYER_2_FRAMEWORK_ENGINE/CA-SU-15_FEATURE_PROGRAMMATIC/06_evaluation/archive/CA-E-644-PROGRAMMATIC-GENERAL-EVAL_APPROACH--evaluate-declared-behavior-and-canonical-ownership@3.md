---
atom_id: CA-E-644
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-21T23:29:13+00:00"
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Evaluation'
  depends_on:
  - Entity/Node/Continuant/Implementation
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement'
  - 'Entity/Node/Continuant/Atom/Content Role: Method'
  - 'Entity/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Carrier
relations:
  evaluation_for:
    - CA-M-402
    - CA-M-403
    - CA-M-411
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
