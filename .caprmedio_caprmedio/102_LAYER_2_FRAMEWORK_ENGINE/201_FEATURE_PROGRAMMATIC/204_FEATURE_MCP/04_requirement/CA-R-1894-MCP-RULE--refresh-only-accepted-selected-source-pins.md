---
atom_id: CA-R-1894
content_role: Requirement
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier/File
relations: {}
tier: 3
type: Rule
---
# Summary

Refresh only accepted selected source pins

## Scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

the selected binding Projection **must** support an explicitly authorized refresh of the exact source revision registered by CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh, while preserving its admitted capability identities and graph.

## Details

- the registered source revision is authority; the refreshed binding is derived evidence, not new authority.
- preserve **all** route identities, order, Steps, Actions, native calls, edges, query admissions and registry identity. **only** the registered version and digest occurrences and resulting derived digests change.
- retain exact current Operator authorization, source-currentness checks, publication intent, readback and Journal completion. a pending recording is not completed publication.
- unknown revisions, changes to topology or capability admission remain outside this refresh.

