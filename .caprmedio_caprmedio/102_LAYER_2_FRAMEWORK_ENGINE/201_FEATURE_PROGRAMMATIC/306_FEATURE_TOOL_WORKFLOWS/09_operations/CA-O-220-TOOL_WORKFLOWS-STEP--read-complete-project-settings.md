---
atom_id: CA-O-220
content_role: Operations
type: Step
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:48 +0400
subjects:
  governs: Subject/caprmedio/Workflow//Update Project Settings > Subject/caprmedio/Step//Read complete Project Settings
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
relations: {}
tier: 3
---
# Summary

Read complete Project Settings

## Operation

this Step invokes exactly CA-O-218 for CA-O-206's complete current Project Settings Read.

### Input and parameter binding

bind `operation = "read"`, `target = {kind: "Configuration", identity: "Project Settings"}`, null query/delta **and** the Workflow request's optional exact current-source precondition as expected_state. null expected_state admits an unpinned current Read. bind the Project, current source authority, declared schema version **and** applicable CA-R-1143/CA-E-459 schema through the Workflow's context; bind its complete-source read permission separately from later write permission. no historical source is selected for a current update.

bind remaining required inputs from that admitted request **and** exact Action/Step/Workflow definitions **and** Run context. CA-O-218 resolves storage privately **and** checks supplied bindings; this Step does **not** introduce storage access **or** schema selection into the connector.

return the unaltered Read result. the Workflow proceeds **to** CA-O-210 **only** with complete verified source text/document, matching current_state, no errors **and** no mutation effects. pass that complete document **and** observed state evidence explicitly **to** CA-O-210; do **not** pass an empty, partial **or** guessed source. denied, stale, unsupported, invalid **or** unavailable results stop **without** invoking Modify.

## Details

this is a source contract, **not** runtime admission **or** a completed read. exact realization/definition pins, permission **and** CA-R-1525/CA-R-1720 Run recording remain required. no retry/resume edge is introduced.
