---
atom_id: CA-R-1843@13
content_role: Requirement
type: Rule
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Authoring/Prompt Authoring
  depends_on:
  - Subject/Graph Node/Engineering/Prompt
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
relations: {}
tier: 3
---
# Summary

Bind implementation prompts to current Workflow sources

## Scope

the PROMPTS implementation of the admitted CA-O-016 Implementation Workflow.

## Claim

the Implementation **must** dispatch a Step prompt only with current, fully read Workflow, Step, and Action source bindings for its actually admitted graph. Context, required inputs, result labels, candidate/evidence freshness, and retry state must match those definitions. A staged shared-context definition is not executable route admission.

## Details

`source_bindings.json` is derived review evidence, not authority. Keep staged definition frontiers separate from the admitted runtime manifest and its frozen test corpus; do not relabel the old executable graph as current or enable an unsupported Step by changing a pin. A changed, absent, mismatched, or partially read source blocks the affected prompt until independent PROMPTS RMED review refreshes its binding; changing a pin only to satisfy a check is forbidden.
