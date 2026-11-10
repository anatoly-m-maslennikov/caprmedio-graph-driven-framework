---
atom_id: CA-R-1894
ref_id: CA-R-1894@13
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output
    Publication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier/File
tier: 3
status: Archived
version: 13
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1894@13-MCP-RULE--refresh-only-accepted-selected-source-pins.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Refresh only accepted selected source pins

## Claim scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

### Prose Claim

the selected binding Projection **must** support an explicitly authorized refresh of the exact source revision registered by CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh, while preserving its admitted capability identities and graph.

## Details

- the registered source revision is authority; the refreshed binding is derived evidence, not new authority.
- preserve **all** route identities, order, Steps, Actions, native calls, edges, query admissions and registry identity. **only** the registered version and digest occurrences and resulting derived digests change.
- retain exact current Operator authorization, source-currentness checks, publication intent, readback and Journal completion. a pending recording is not completed publication.
- unknown revisions, changes to topology or capability admission remain outside this refresh.

