---
atom_id: CA-O-117
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:46 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
relations:
  depends_on:
  - CA-D-517
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-117-PROJECT_CONFIGURATION-ACTION--wait-for-execution-updates.md
  source_atom_id: CA-O-117
  source_atom_revision: 12
  source_sha256: 13d73ea964237d9de982627357626527930f95f1892fcc5c2f22bb7a53f43706
  original_relations_sha256: cbced7be5518be741db2820cf18422d9087a19d48c5944b1a1b01e50c3823531
---
# Summary

Wait for execution updates

## Operation

Execution notifications **means** the Programmatic Action implementing the following responsibility:

- compare snapshots of existing saved evidence; replay confirmed Journal updates after the cursor, await changes asynchronously, and distinguish unconfirmed event recording.
- accept the declared inputs **and** return the declared results under CA-D-517-WATCH_EXECUTION-ENG_DECISION--encode-watch-execution-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
