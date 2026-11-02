---
atom_id: CA-O-205
content_role: Operations
type: Workflow
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow"
  depends_on: ["Project Structure","Scope Unit","Step","Workflow Run","Tool"]
version: 1
updated_at: "2026-10-12 23:17:22 +0400"
relations:
  relates_to: [CA-O-209, CA-O-204, CA-R-1829, CA-D-441, CA-R-1935, CA-M-375, CA-M-305]
---
# Summary

Update Project Structure

## Operation

Update Project Structure **means** the configuration-specific Workflow that checks and submits one explicit authoritative Project Structure TOML patch through Step CA-O-209 using the shared O204 Action.

### Workflow graph

Entry: CA-O-209 after its bound structure request and authority checks. On confirmed verified patch success or truthful validated no-op, terminate complete with exact effects or no-effect evidence. On rejected, stale, unsupported, failed, partial, unknown or incomplete-recording outcome, terminate stopped; no failed-action retry/resume edge exists.

### Authority and request boundary

Resolve the private exact target `.caprmedio_caprmedio/project_structure.toml`. Bind its actual declared `schema_version` (currently integer `1`) and current CA-D-441 schema/authority; a missing, unsupported or conflicting declaration blocks dispatch. Validate the complete proposed structure and CA-R-1829 bounded Scope Unit constraints before any write, including unique identities, declared parents, allowed types, hierarchy and the implicit Project root. Never turn folder existence into Scope Unit authority.

The request supplies exactly one explicit admitted configuration change with current values, source pin and permission. Preserve unrelated Scope Units and fields. This Workflow is distinct from O206 but uses the same TOML Action, not a second connector. Scope Unit creation remains the distinct logical O203 Action where selected; no Atom deletion, reference retargeting or migration publication is implicit.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
