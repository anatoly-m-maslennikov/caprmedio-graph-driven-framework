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
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Discover current immediate Tool units

## Applicable when

Apply **when** MCP **must** refresh the project-local exposed Tool set.

## Procedure

1. Resolve the current project graph **and** its immediate Tool units owned by `TOOLS`.
2. Match each unit **to** its canonical Tool folder **and** current enablement decision.
3. Exclude nested helpers **and** non-Tool folders from the resulting source set.

## Outcome

MCP has one current, authority-derived source set for Tool exposure.

## Failure or stop

Stop discovery **when** the graph, unit identity, enablement decision, **or** canonical Tool folder is unresolved.
