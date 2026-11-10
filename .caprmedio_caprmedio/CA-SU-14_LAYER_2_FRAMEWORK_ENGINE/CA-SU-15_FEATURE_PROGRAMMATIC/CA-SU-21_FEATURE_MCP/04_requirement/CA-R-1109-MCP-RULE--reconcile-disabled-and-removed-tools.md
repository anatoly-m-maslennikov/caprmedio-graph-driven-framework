---
atom_id: CA-R-1109
ref_id: CA-R-1109
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Data Handling <+ Output Publication
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-171
status: Active
version: 22
updated_at: 2026-11-10 20:47:54 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1109-MCP-RULE--reconcile-disabled-and-removed-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Reconcile disabled and removed Tools

## Claim

### Prose Claim

MCP regeneration **must** add **every** newly active valid Tool, exclude **every** explicitly disabled Tool, **and** remove **every** projection whose source Tool is no longer active **or** present. MCP **must not** maintain a second independent allowlist **or** lifecycle registry that can disagree with current project authority **and** Configuration.

## Details

Load the generated registration asset and configured exclusions; publish its complete enabled entry set, remove disabled or removed configured entries, exclude unlisted helpers, and stop on malformed or unresolved registration configuration. Do not scan native Atoms, Scope Unit graphs, or Tool folders for exposure.
