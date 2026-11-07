---
atom_id: CA-M-168
ref_id: CA-M-168
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
tier: 2
relations:
  method_for:
  - CA-R-1106
  derived_from:
  - CA-A-057
status: Active
version: 19
updated_at: 2026-11-07 13:19:43 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Discover current immediate Tool units

## Applicable when

MCP starts or explicitly loads a rebuilt installed implementation.

## Procedure

Read the generated registration asset carried by that installed package. Resolve only its code-owned provider and selected-route entries, then apply the bound Project's configured exclusions. Do not scan native Atoms, Scope Unit graphs or Tool folders for exposure.

## Outcome

MCP exposes the enabled installed code/configuration surface through its existing backend adapters.

## Failure or stop

Report missing or malformed registration configuration explicitly. Do not fall back to Atom discovery or expose unlisted helpers.
