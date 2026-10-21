---
atom_id: CA-C-539
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-D-461, CA-E-502, CA-P-2401, CA-C-536]
version: 1
updated_at: "2026-10-20 17:32:00 +0400"
---
# Summary

Implement flat shared Plan archival

## Concern

The latest Operator decision requires flattening archived Plans in the owning Scope Unit shared archive area. Existing nested local-archive consumers do not implement this policy. C536 is resolved as a policy decision, not an implementation or migration receipt.

## Evidences

The Operator answered No—flatten archived Plans. The Methodology owner is aligning the conflicting D461/E502 placement clauses; prior retained-hierarchy wording is superseded only for Archived Plans. P2444 normalizes explicit root paths without claiming nested flat placement, and read-only review identified local-container assumptions in proposed_references and lifecycle_intents. Current non-Archived hierarchy remains unchanged.

## Blast radius

Nested Plan archive/status/container operations need a bounded source-bound implementation and functional tests. Plan physical migration separately, preserve immutable older bytes and non-Plan accompanying data, and do not infer incoming-link removal/retargeting or new Status/cascade policy. Existing carriers and held drafts must not be flattened automatically as part of the parser release. Root archived carrier creation is a narrower acceptance case, not proof of nested flattening.
