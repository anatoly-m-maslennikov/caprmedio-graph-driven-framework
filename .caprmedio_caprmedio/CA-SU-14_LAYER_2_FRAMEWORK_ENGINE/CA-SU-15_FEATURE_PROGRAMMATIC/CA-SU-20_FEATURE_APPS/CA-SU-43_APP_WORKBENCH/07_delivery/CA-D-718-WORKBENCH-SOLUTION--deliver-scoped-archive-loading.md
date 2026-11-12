---
identity:
  atom_id: CA-D-718
  ref_id: CA-D-718
context:
  role: delivery
  form: solution
  tier: 5
  container:
    scope_unit: CA-SU-43
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
relations:
  delivery_for:
  - CA-R-2723
  - CA-M-465
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:43:22.100271+00:00'
destination:
  file:
    name: CA-D-718-WORKBENCH-SOLUTION--deliver-scoped-archive-loading.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
---
## Summary

Deliver scoped Archive loading

## Claim scope

The shared Workbench Archive loading contract in HTTP and MCP.

## Claim

### Prose Claim

`workbench_archive_load` takes `scopes`, a nonempty array of `{scope_unit, role}` pairs. The Workbench web interface calls `POST /api/archive-load` beneath its existing Project route. Both adapters use the same selected Project owner and return `loaded_archive_scopes`, the complete array of pairs already loaded by that owner. Workbench status exposes the same coverage.

The load completes when selected `atoms` rows are published. Audit results can follow independently. Ordinary SQL reads the existing `atoms` table.