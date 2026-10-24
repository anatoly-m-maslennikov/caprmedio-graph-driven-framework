---
atom_id: CA-E-642
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-21T22:49:16Z"
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
    - CA-M-285
    - CA-M-395
---
# Summary

Evaluate active Method coverage

## Scope

Every Active PROGRAMMATIC Method and the bounded implementation surface to which it applies, including Tools, Apps, MCP, workflows, background work and descendant Scope Units.

## Claim

Accept conformance only when every applicable Active Method has substantive evidence selected for its failure mode. A relation to an Evaluation is routing metadata, not evidence and not proof of coverage. Record each obligation as covered, partial, uncovered or inapplicable, with the evidence or reason. This portfolio mapping does not create an additional release gate.

## Details

- Derive the applicable Method set from current authority and the actual changed or delivered surface.
- Use static checks, functional or integration tests, end-to-end or canary checks, and focused review according to the failure mode.
- Permit one Evaluation to cover many Methods and one Method to be covered by many Evaluations when each link names the substantive predicate; do not count links or projections as evidence.
- Mark missing fixtures, unavailable environments, contradictory authority or insufficient observations unresolved or partial, not passing. Recompute when the Method, implementation surface or Evaluation changes.
