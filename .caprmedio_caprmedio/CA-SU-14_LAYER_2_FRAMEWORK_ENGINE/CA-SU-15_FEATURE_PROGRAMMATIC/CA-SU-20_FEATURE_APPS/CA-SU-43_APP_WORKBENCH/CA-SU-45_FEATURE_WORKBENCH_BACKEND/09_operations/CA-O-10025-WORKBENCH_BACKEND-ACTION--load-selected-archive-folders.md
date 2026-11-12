---
identity:
  atom_id: CA-O-10025
  ref_id: CA-O-10025
context:
  role: operations
  form: Action
  tier: 6
  container:
    scope_unit: CA-SU-45
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Indexing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
relations:
  depends_on:
  - CA-R-2723
  - CA-M-465
  - CA-D-673
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:39:58.202981+00:00'
destination:
  file:
    name: CA-O-10025-WORKBENCH_BACKEND-ACTION--load-selected-archive-folders.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations
---
## Summary

Load selected Archive folders

## Operation

### Claim scope

One explicit Workbench request to load the Archive folders for selected Scope Units and Roles.

### Claim

Resolve each requested Scope Unit and Role to its model-declared Archive folder and admitted aliases. Validate the selection before reading or publishing any Archive rows. Load the selected physical files into the existing `atoms` table, and return the complete set of Archive scopes loaded by this Workbench owner. A load of the same unchanged folders creates no duplicate rows. Queue audits of the loaded files and make their progress observable through Workbench status. Return explicit selection or source errors. This Action leaves the source files untouched.