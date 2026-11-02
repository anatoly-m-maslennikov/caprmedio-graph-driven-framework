---
atom_id: CA-C-539@2
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-D-461, CA-E-502, CA-P-2401, CA-C-536]
version: 2
updated_at: "2026-10-20T21:16:20.300Z"
---
# Summary

Implement flat shared Plan archival

## Concern

The latest Operator decision requires flattening archived Plans in the owning Scope Unit shared archive area. Existing nested local-archive consumers do not implement this policy. C536 is resolved as a policy decision, not an implementation or migration receipt.

## Evidences

The Operator answered No—flatten archived Plans. The Methodology owner is aligning the conflicting D461/E502 placement clauses; prior retained-hierarchy wording is superseded only for Archived Plans. P2444 normalizes explicit root paths without claiming nested flat placement, and read-only review identified local-container assumptions in proposed_references and lifecycle_intents. Current non-Archived hierarchy remains unchanged.

## Blast radius

Nested Plan archive/status/container operations need a bounded source-bound implementation and functional tests. Plan physical migration separately, preserve immutable older bytes and non-Plan accompanying data, and do not infer incoming-link removal/retargeting or new Status/cascade policy. Existing carriers and held drafts must not be flattened automatically as part of the parser release. Root archived carrier creation is a narrower acceptance case, not proof of nested flattening.

## Current disposition

The bounded source-level mechanics are accepted at atom_operations537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284: root/nested-leaf flat destinations, Draft identity routing, flat exact Plan predecessors, singleton current-child safety, source-bound validator placement and Subject predictions. Independent native71, Subject21, validator544 and CLI11 passed; code review APPROVE. C549 is answered and C550/C552 source defects are resolved. This does not complete a recursive container request: no calling Workflow currently composes the required descendant Runs. Active C551 and Backlog P2494/P2495 own that missing behavior and acceptance. This Problem therefore remains Active for full user-facing nested archival; no live migration, installed-runtime repair or production proof is claimed.
