---
atom_id: CA-O-210@3
content_role: Operations
type: Step
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Step"
  depends_on: ["Project Settings","Step Run","Workflow Run","Tool"]
version: 3
updated_at: "2026-10-13 02:45:51 +0400"
relations:
  relates_to: [CA-O-206, CA-O-220, CA-O-218, CA-D-631, CA-O-204, CA-R-1143, CA-E-459, CA-R-1509, CA-M-305]
---
# Summary

Patch Project Settings TOML

## Operation

This Step invokes exactly CA-O-204 for O206's one explicit Project Settings change.

### Input and parameter binding

bind logical configuration Project Settings, exact explicit patch/current values **and** write permission from CA-O-206's admitted request. receive the complete verified current document **and** observed source-state evidence from CA-O-220; use that evidence as Modify expected_state **and** enforce **any** supplied request pin. missing, erroneous, incomplete **or** mismatched Read output stops **before** proposal validation **or** Modify. derive **and** validate the proposal from that complete document, preserving unrelated values. Privately bind only `.caprmedio_caprmedio/caprmedio_project_settings.toml`, its actual schema declaration (currently string `"2.0"`) and available current applicable schema/authority under CA-R-1143/CA-E-459. Complete source/proposed-result schema, protected/generated-value and effective-diff checks before invoking a write-capable realization; absence, conflict or unsupported authority stops unchanged.

Supply O204 operation `modify` and D625's explicit logical target/delta, expected_state and authorization/context. O206 owns schema/authority/permission selection; O204 only checks the supplied constraints and exact delta. Bind every remaining required O204 input from that checked request/current authority and exact Action/Step/Workflow definition pins and Run context, never a fallback schema or a different config target. Return the unaltered O204 outcome with actual readback/effect/recording evidence; O206 maps it to terminal complete or stopped. No other Action is invoked here.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
