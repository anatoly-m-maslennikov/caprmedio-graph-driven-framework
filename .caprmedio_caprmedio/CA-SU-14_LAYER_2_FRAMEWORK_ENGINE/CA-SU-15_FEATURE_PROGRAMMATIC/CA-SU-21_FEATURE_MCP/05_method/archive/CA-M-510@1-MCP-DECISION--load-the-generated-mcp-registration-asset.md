---
atom_id: CA-M-510@1
ref_id: CA-M-510@1
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
tier: 2
relations:
  method_for:
  - CA-R-1106
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-M-168
status: Archived
version: 1
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-510@1-MCP-DECISION--load-the-generated-mcp-registration-asset.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---

## Summary


Load the generated MCP registration asset

## Claim

### Prose Claim

#### Applicable when

MCP starts or explicitly loads a rebuilt installed implementation.

#### Procedure

Read the generated registration asset carried by that installed package. Resolve only its code-owned provider and selected-route entries, then apply the bound Project's configured exclusions. Do not scan native Atoms, Scope Unit graphs or Tool folders for exposure.

#### Outcome

MCP exposes the enabled installed code/configuration surface through its existing backend adapters.

#### Failure or stop

Report missing or malformed registration configuration explicitly. Do not fall back to Atom discovery or expose unlisted helpers.
