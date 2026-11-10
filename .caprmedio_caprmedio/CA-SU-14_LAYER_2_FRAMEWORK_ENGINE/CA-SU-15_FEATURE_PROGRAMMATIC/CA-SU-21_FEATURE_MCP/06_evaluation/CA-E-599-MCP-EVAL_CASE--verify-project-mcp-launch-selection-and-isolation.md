---
atom_id: CA-E-599
ref_id: CA-E-599
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: MODEL//CAPRMEDIO <+ Project
  dependencies:
  - MODEL//CAPRMEDIO <+ Project.Settings
  - MODEL//CAPRMEDIO <+ Scope Unit
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Source Selection
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - MODEL//CAPRMEDIO <+ Carrier
tier: 5
relations:
  evaluation_for:
  - CA-R-1900
status: Active
version: 18
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-E-599-MCP-EVAL_CASE--verify-project-mcp-launch-selection-and-isolation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Verify Project MCP launch selection and isolation

## Claim

### Prose Claim

The launcher binds only the selected Project context and refuses malformed or mismatched hook input without an effect or cross-Project state access.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Two roots with the same control-root name | Each valid selection has a different canonical identity, namespace, Gateway context, manifest/registry/query-source read, and reload storage. |
| Two roots below one Git ancestor | Selection resolves only its own local control root; identities cannot observe/reuse the other's lock, cache, receipt, pending launch, or runtime metadata. |
| Single-Project hook omits project_root | Use the fixed bound ProjectSelection. |
| Single-Project hook supplies matching host/container forms | Resolve one identity and remove the envelope before native dispatch. |
| Single-Project hook supplies foreign, malformed, escaping, or symlink-substituted root | Refuse before Docker inspection, Tool dispatch, port allocation, Gateway reload, or state write. |
| Shared hook omits root | Refuse because shared mode requires an explicit Project binding. |
| Shared hook supplies Project A then B | Each request binds only its admitted selection; no process-global root or dynamic switch. |
| Explicit --project-root repo with one direct valid control root | Resolve the declared root only; do not search Git ancestors or historical/default roots. |
| Missing, invalid, or unreadable root | Return attributable selection refusal before Docker inspection or state write. |
| Unsafe control-root selector | Reject traversal, escaping, symlink substitution, zero candidates, and multiple candidates before effects. |
| A-bound manifest/registry/query source supplied from B/foreign binding | Reject the mixed context; construct no substituted or cross-Project selection. |
| Invalid/ambiguous local control-root input | Structured refusal; do not choose sibling, parent, nested, historical, or Git-ancestor roots. |

Do not test source mutation, restart, or release effects.
