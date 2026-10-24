---
atom_id: CA-O-205
content_role: Operations
type: Workflow
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Configuration/Project Structure Workflow Realization
version: 6
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-O-219
  - CA-O-209
  - CA-O-218
  - CA-D-631
  - CA-O-204
  - CA-R-1829
  - CA-D-441
  - CA-R-1935
  - CA-M-375
  - CA-M-305
tier: 3
---
# Summary

Update Project Structure

## Operation

Update Project Structure **means** the configuration-specific Workflow that reads its complete current source through Step CA-O-219, **then** checks **and** submits one explicit authoritative TOML patch through Step CA-O-209. the Steps use CA-O-218 Read **and** CA-O-204 Modify on the same shared connector.

### Workflow graph

entry: CA-O-219 **after** bound request **and** authority checks. proceed **to** CA-O-209 **only** on complete verified current Read data, matching observed source-state evidence, empty errors **and** no mutation effects. pass the complete document **and** observed state evidence **to** CA-O-209 **before** constructing **or** validating the proposal. **otherwise**, stop **without** Modify. On confirmed verified patch success or truthful validated no-op, terminate complete with exact effects or no-effect evidence. On rejected, stale, unsupported, failed, partial, unknown or incomplete-recording outcome, terminate stopped; no failed-action retry/resume edge exists.

### Authority and request boundary

Resolve the private exact target `.caprmedio_caprmedio/project_structure.toml`. Bind its actual declared `schema_version` (currently integer `1`) and current CA-D-441 schema/authority; a missing, unsupported or conflicting declaration blocks dispatch. Validate the complete proposed structure and CA-R-1829 bounded Scope Unit constraints before any write, including unique identities, declared parents, allowed types, hierarchy and the implicit Project root. Never turn folder existence into Scope Unit authority.

The request supplies exactly one explicit admitted configuration change with current values, source pin and permission. Preserve unrelated Scope Units and fields. This Workflow is distinct from O206 but uses the same TOML Action, not a second connector. Scope Unit creation remains the distinct logical O203 Action where selected; no Atom deletion, reference retargeting or migration publication is implicit.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
