---
atom_id: CA-O-206
content_role: Operations
type: Workflow
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Configuration/Project Settings Workflow Realization
version: 7
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-O-220
  - CA-O-210
  - CA-O-218
  - CA-D-631
  - CA-O-204
  - CA-R-1143
  - CA-E-459
  - CA-R-1935
  - CA-M-375
  - CA-M-305
tier: 3
---
# Summary

Update Project Settings

## Operation

Update Project Settings **means** the configuration-specific Workflow that reads its complete current source through Step CA-O-220, **then** checks **and** submits one explicit authoritative TOML patch through Step CA-O-210. the Steps use CA-O-218 Read **and** CA-O-204 Modify on the same shared connector.

### Workflow graph

entry: CA-O-220 **after** bound request **and** authority checks. proceed **to** CA-O-210 **only** on complete verified current Read data, matching observed source-state evidence, empty errors **and** no mutation effects. pass the complete document **and** observed state evidence **to** CA-O-210 **before** constructing **or** validating the proposal. **otherwise**, stop **without** Modify. On confirmed verified patch success or truthful validated no-op, terminate complete with exact effects or no-effect evidence. On rejected, stale, unsupported, failed, partial, unknown or incomplete-recording outcome, terminate stopped; no failed-action retry/resume edge exists.

### Authority and request boundary

Resolve the private exact target `.caprmedio_caprmedio/caprmedio_project_settings.toml`. Bind its actual declared `schema_version` (currently string `"2.0"`) and current applicable Project Settings schema/authority under CA-R-1143 and CA-E-459. A declared marker alone is not a substitute for available authoritative validation; missing, ambiguous, unsupported or conflicting schema/authority blocks dispatch before writing.

Validate complete source and result, protected/generated values and the exact effective diff before any write. Preserve unrelated admitted current values; reject unsupported or legacy sections under the complete closed schema of CA-D-366 before dispatch. Refusal does not authorize deleting, repairing or migrating existing Carrier data. Project Settings remains its independently governed non-Atom configuration; this patch does not give it an Atom ID/Role or independently editable Project Structure.

The request supplies exactly one explicit admitted key change with current values, source pin and permission. This Workflow is distinct from O205 but uses the same TOML Action, not a second connector. No runtime activation, generated-value override or staged Subject migration effect follows.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
