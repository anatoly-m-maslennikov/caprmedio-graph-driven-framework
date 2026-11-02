---
atom_id: CA-R-1843@4
content_role: Requirement
type: Requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Implementation Workflow prompt source currentness
  depends_on:
  - Prompt
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
relations:
  relates_to:
  - CA-O-016
  - CA-O-231
  - CA-O-232
  - CA-O-233
  - CA-O-094
  - CA-O-234
  - CA-O-096
  - CA-O-099
---
# Summary

Bind implementation prompts to current Workflow sources

## Scope

the PROMPTS implementation of the admitted CA-O-016 Implementation Workflow.

## Claim

the Implementation **must** dispatch a Step prompt only with current, fully read Workflow, Step, and Action source bindings for its actually admitted graph. Context, required inputs, result labels, candidate/evidence freshness, and retry state must match those definitions. A staged shared-context definition is not executable route admission.

## Details

`source_bindings.json` is derived review evidence, not authority. Keep staged definition frontiers separate from the admitted runtime manifest and its frozen test corpus; do not relabel the old executable graph as current or enable an unsupported Step by changing a pin. A changed, absent, mismatched, or partially read source blocks the affected prompt until independent PROMPTS RMED review refreshes its binding; changing a pin only to satisfy a check is forbidden.
