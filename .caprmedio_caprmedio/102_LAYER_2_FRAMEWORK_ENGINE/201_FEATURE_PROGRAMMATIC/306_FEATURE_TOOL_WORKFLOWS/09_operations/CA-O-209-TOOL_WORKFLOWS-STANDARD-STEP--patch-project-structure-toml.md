---
atom_id: CA-O-209
content_role: Operations
type: Step
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Step"
  depends_on: ["Project Structure","Step Run","Workflow Run","Tool"]
version: 2
updated_at: "2026-10-12 23:49:24 +0400"
relations:
  relates_to: [CA-O-205, CA-O-204, CA-R-1829, CA-D-441, CA-R-1509, CA-M-305]
---
# Summary

Patch Project Structure TOML

## Operation

This Step invokes exactly CA-O-204 for O205's one explicit Project Structure change.

### Input and parameter binding

Bind logical configuration Project Structure, exact explicit patch/current values, source pin and permission from O205's admitted request. Privately bind only `.caprmedio_caprmedio/project_structure.toml`, its actual integer schema declaration and complete current CA-D-441/CA-R-1829 schema, structure and authority checks. Complete those checks against the source and proposed result before invoking a write-capable realization; absence, conflict or unsupported schema stops unchanged.

Supply O204 operation `modify` and D625's explicit logical target/delta, expected_state and authorization/context. O205 owns schema/authority/permission selection; O204 only checks the supplied constraints and exact delta. Bind every remaining required O204 input from that checked request/current authority and exact Action/Step/Workflow definition pins and Run context, never a fallback schema or a different config target. Return the unaltered O204 outcome with actual readback/effect/recording evidence; O205 maps it to terminal complete or stopped. No other Action is invoked here.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
