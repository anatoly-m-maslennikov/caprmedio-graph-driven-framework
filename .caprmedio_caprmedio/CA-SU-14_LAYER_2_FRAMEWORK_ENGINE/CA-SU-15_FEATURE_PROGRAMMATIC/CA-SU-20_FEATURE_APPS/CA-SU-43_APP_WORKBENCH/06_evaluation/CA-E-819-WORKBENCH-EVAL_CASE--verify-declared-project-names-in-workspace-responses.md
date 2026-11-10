---
identity:
  atom_id: CA-E-819
  ref_id: CA-E-819
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - MODEL//CAPRMEDIO <+ Workspace
    - MODEL//CAPRMEDIO <+ Project
  tier: 5
relations:
  evaluation_for:
  - CA-R-2902
  - CA-D-673
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 21:18:04 +0400
destination:
  file:
    name: CA-E-819-WORKBENCH-EVAL_CASE--verify-declared-project-names-in-workspace-responses.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Verify declared Project names in Workspace responses

## Claim scope

Shared HTTP and MCP Workspace Open and Get responses.

## Claim

### Prose Claim

HTTP and MCP `workspace_open` and `workspace_get` must return the declared Project name, without storing that name in Workspace documents.

## Details

Use a Project whose declared name differs from its directory basename. Call Open and Get through both interfaces and check that `project_name` equals the declared name. Inspect the resulting Workspace documents and check that they contain no persisted Project-name field.
