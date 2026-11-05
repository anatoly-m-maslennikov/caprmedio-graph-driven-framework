---
atom_id: CA-E-599
ref_id: CA-E-599
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Carrier
tier: 5
relations:
  evaluation_for:
  - CA-R-1900
  - CA-M-355
status: Active
version: 15
updated_at: 2026-11-05 13:48:40 +0400
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

The launcher binds only the selected Project context and refuses malformed or mismatched hook input without an effect or cross-Project state access.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Two Project roots with the same control-root name | Each valid selection has a different canonical identity, namespace, Gateway context, manifest/registry/query-source read and reload storage. |
| Two valid Project roots below one Git-repository ancestor | An explicitly selected Project root resolves only its own local control root; each selection has a different identity and cannot observe or reuse the other's lock, cache, receipt, pending-launch record or runtime metadata. |
| Single-Project hook omits project_root | The fixed bound ProjectSelection is used. |
| Single-Project hook supplies matching host and container project_root forms | The mapping resolves to the same identity and native dispatch receives no project_root envelope field. |
| Single-Project hook supplies a foreign, malformed, escaping or symlink-substituted project_root | Refuse before Docker image inspection, native Tool dispatch, port allocation, Gateway reload or state write. |
| Shared hook omits project_root | Refuse because shared mode requires an explicit Project binding. |
| Shared hook supplies a valid Project root for Project A, then Project B | Each request binds only its admitted ProjectSelection; no process-global root or dynamic switch is used. |
| Explicit --project-root repo with one valid direct control root | Resolve the declared Project root only; do not search a Git ancestor or choose a historical/default control root. |
| Missing, invalid or unreadable Project root | Return the attributable selection refusal before Docker image inspection or state write. |
| Unsafe control-root selector | Reject traversal, escaping, symlink-substituted, zero-candidate and multiple-candidate selectors before effect. |
| Selected manifest, registry and query source bound to Project A, then supplied from Project B or a foreign binding | Reject the mixed context rather than constructing a substituted or cross-Project selection. |
| Invalid or ambiguous local control-root input | Return structured selection refusal without choosing a sibling, parent, nested Project, historical default or Git ancestor. |

The Evaluation does not test source mutation, restart or release effects.
