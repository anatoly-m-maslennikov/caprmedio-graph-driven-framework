---
identity:
  atom_id: CA-D-721
  ref_id: CA-D-721
context:
  role: delivery
  form: solution
  tier: 5
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
    dependencies: []
  container:
    scope_unit: MCP
state:
  version: 1
  status: active
  updated_at: '2026-11-12T17:01:36.783431+00:00'
destination:
  file:
    name: CA-D-721-MCP-SOLUTION--expose-project-operations-through-the-shared-http-api.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery
---
## Summary

Expose Project operations through the shared HTTP API

## Claim

### Prose Claim

Expose Project HTTP operations at `/caprmedio/{project}/api/{operation}` for any client. Keep `/caprmedio/workbench/{project}` as the Workbench page. The existing Workbench operation URLs remain compatibility aliases to the same handlers.

Keep the existing operation names, request arguments and responses. Both URLs validate the Project name against the same selected Project and apply the same eligibility and dispatch rules. The Workbench frontend calls the shared Project API.
