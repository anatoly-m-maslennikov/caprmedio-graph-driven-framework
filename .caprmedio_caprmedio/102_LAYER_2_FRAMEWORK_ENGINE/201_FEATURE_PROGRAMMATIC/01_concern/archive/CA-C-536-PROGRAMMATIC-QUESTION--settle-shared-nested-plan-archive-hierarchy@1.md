---
atom_id: CA-C-536
content_role: Concern
type: Question
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-D-461, CA-E-502, CA-P-2444]
version: 1
updated_at: "2026-10-20T13:21:50.935Z"
---
# Summary

Settle shared nested Plan archive hierarchy

## Concern

Current D461v14/E502v12 require Scope Unit-shared Draft/Archived areas but do not settle the concrete nested archive path preserving child hierarchy. The Operator has been asked whether archived parents retain complete child-folder hierarchy; no answer or automatic flattening is assumed.

## Evidences

Read-only intersecting contract review found nested local-folder consumers in proposed_references and lifecycle_intents differ from the new shared placement. P2444 fixes only explicit root path parsing. No physical Plan migration, incoming-link cleanup, Status removal or new cascade policy was performed.

## Blast radius

Keep ambiguous nested shared-placement changes postponed and preserve existing carriers/bundles. Scope-root path compatibility and parser release do not establish nested shared archival acceptance.
