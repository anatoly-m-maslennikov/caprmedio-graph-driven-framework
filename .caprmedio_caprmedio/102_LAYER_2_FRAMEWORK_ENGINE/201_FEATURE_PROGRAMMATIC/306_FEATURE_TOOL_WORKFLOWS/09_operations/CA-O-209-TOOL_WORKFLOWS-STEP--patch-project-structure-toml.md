---
atom_id: CA-O-209
content_role: Operations
type: Step
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Update Project Structure > Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Patch Project Structure TOML'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
version: 10
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
---
# Summary

Patch Project Structure TOML

## Operation

This Step invokes exactly CA-O-204 for O205's one explicit Project Structure change.

### Input and parameter binding

bind logical configuration Project Structure, exact explicit patch/current values **and** write permission from CA-O-205's admitted request. receive the complete verified current document **and** observed source-state evidence from CA-O-219; use that evidence as Modify expected_state **and** enforce **any** supplied request pin. missing, erroneous, incomplete **or** mismatched Read output stops **before** proposal validation **or** Modify. derive **and** validate the proposal from that complete document, preserving unrelated values. Privately bind only `.caprmedio_caprmedio/project_structure.toml`, its actual integer schema declaration and complete current CA-D-441/CA-R-1829 schema, structure and authority checks. Complete those checks against the source and proposed result before invoking a write-capable realization; absence, conflict or unsupported schema stops unchanged.

Supply O204 operation `modify` and D625's explicit logical target/delta, expected_state and authorization/context. O205 owns schema/authority/permission selection; O204 only checks the supplied constraints and exact delta. Bind every remaining required O204 input from that checked request/current authority and exact Action/Step/Workflow definition pins and Run context, never a fallback schema or a different config target. Return the unaltered O204 outcome with actual readback/effect/recording evidence; O205 maps it to terminal complete or stopped. No other Action is invoked here.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
