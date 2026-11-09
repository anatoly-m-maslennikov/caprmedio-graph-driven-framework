---
atom_id: CA-R-1109@20
ref_id: CA-R-1109@20
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output
    Publication
tier: 1
status: Archived
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1109@20-MCP-RULE--reconcile-disabled-and-removed-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---
## Summary

Reconcile disabled and removed Tools

## Claim

### Prose Claim

MCP regeneration **must** add **every** newly active valid Tool, exclude **every** explicitly disabled Tool, **and** remove **every** projection whose source Tool is no longer active **or** present. MCP **must not** maintain a second independent allowlist **or** lifecycle registry that can disagree with current project authority **and** Configuration.
