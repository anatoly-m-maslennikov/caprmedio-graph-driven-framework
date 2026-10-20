---
atom_id: CA-C-536
content_role: Concern
type: Question
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-D-461, CA-E-502, CA-P-2444]
version: 2
updated_at: "2026-10-20T12:50:48.772Z"
---
# Summary

Settle shared nested Plan archive hierarchy

## Concern

The Operator explicitly answered No—flatten archived Plans. This latest decision overrides D461v14/E502v12 clauses retaining the archived child-folder hierarchy. Current non-archived Plan hierarchy is unchanged; Archived Plan carriers use the owning Scope Unit shared archive area without retaining the Plan hierarchy.

## Evidences

Read-only intersecting contract review found nested local-folder consumers in proposed_references and lifecycle_intents differ from the new shared placement. P2444 fixes only explicit root path parsing. The Methodology owner was asked to align only the conflicting archive-placement source clauses through the canonical workflow. No physical Plan migration, incoming-link cleanup, Status removal or new cascade policy was performed.

## Blast radius

The policy question is resolved, not its implementation. Problem C539 separately tracks flat shared archival implementation and safe migration. Scope-root parser compatibility and the approved release do not claim nested flattening acceptance.
