---
atom_id: CA-O-203@8
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Implementation
version: 8
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-D-441
tier: 3
---
# Summary

Create one Scope Unit

## Operation

Create One Scope Unit **means** the logical Action that adds exactly one explicitly requested Scope Unit to authoritative Project Structure under CA-R-1829. It does not infer a Scope Unit from a folder or invent a new connector or authority root. Scope identity/hierarchy, complete structure schema and admission are workflow-owned decisions; a mechanical connector receives only the checked explicit target/delta/preconditions/permission through D625.

### Action

1. bind the explicit new Scope Unit identity, its declared parent and allowed type and properties, current Project Structure source pin, applicable current schema and authority, and exact permission. Reject duplicate identities, missing or ambiguous parent, invalid hierarchy/root constraints or an unsupported schema before effects.
2. validate the complete proposed authoritative structure under CA-D-441 and the current structure authority. Preserve all unrelated Scope Units and every protected field. The implicit Project root is not a duplicate `scope_units` row.
3. use the same shared TOML realization selected for O204, with the Project Structure target resolved privately; there is no separate TOML connector. Derive and expose this one exact mutation-free proposal before an independently admitted effect.
4. recheck source, authority, schema and permission immediately before the safe one-Scope-Unit effect. Independently read back and schema-check the complete result; report actual identity/effects or truthful failed, partial or unknown evidence. No Atom deletion, automatic reference rewrite or unsupplied structural change follows.

## Details

Its separate governing Workflow and executable realization remain future gated work; this Action does not introduce an additional Workflow or Step now. Current Project Structure dispatch semantics remain applicable. Storage paths and folders are private realization details, not the public Scope Unit selector.

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
