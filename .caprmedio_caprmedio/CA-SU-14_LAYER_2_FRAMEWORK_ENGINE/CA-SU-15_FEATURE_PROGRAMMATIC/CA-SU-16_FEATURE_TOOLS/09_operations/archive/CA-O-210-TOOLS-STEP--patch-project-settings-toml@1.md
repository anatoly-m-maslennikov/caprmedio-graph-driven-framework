---
atom_id: CA-O-210
content_role: Operations
type: Step
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Step"
  depends_on: ["Project Settings","Step Run","Workflow Run","Tool"]
version: 1
updated_at: "2026-10-12 23:17:22 +0400"
relations:
  relates_to: [CA-O-206, CA-O-204, CA-R-1143, CA-E-459, CA-R-1509, CA-M-305]
---
# Summary

Patch Project Settings TOML

## Operation

This Step invokes exactly CA-O-204 for O206's one explicit Project Settings change.

### Input and parameter binding

Bind logical configuration Project Settings, exact explicit patch/current values, source pin and permission from O206's admitted request. Privately bind only `.caprmedio_caprmedio/caprmedio_project_settings.toml`, its actual schema declaration (currently string `"2.0"`) and available current applicable schema/authority under CA-R-1143/CA-E-459. Complete source/proposed-result schema, protected/generated-value and effective-diff checks before invoking a write-capable realization; absence, conflict or unsupported authority stops unchanged.

Bind every remaining required O204 input from that checked request/current authority and exact Action/Step/Workflow definition pins and Run context, never a fallback schema or a different config target. Return the unaltered O204 outcome with actual readback/effect/recording evidence; O206 maps it to terminal complete or stopped. No other Action is invoked here.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
