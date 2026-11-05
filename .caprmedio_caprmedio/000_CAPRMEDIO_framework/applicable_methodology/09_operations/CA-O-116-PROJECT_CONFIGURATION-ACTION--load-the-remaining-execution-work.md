---
atom_id: CA-O-116
ref_id: CA-O-116
container:
  scope_unit: CA-SU-13
role: Operations
form: Action
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  depends_on:
  - CA-D-516
status: Active
version: 13
updated_at: 2026-10-27 19:59:46 +0400
carrier_destination:
  file:
    name: CA-O-116-PROJECT_CONFIGURATION-ACTION--load-the-remaining-execution-work.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-116-PROJECT_CONFIGURATION-ACTION--load-the-remaining-execution-work.md
  source_atom_id: CA-O-116
  source_atom_revision: 13
  source_sha256: 5694f8792ab5d08419cb2e293b1029ca3bb37e00a62845801e6ebcbac87a21ea
  original_relations_sha256: 0ee7c21d931110e5c2b7cd518d732303ee4cf6a02c08a0e81e3396f950117269
---
# Summary

Load the remaining execution work

## Operation

Execution continuation context **means** the Programmatic Action implementing the following responsibility:

- derive remaining work from the saved initial checks and correction dispositions; compare source and criteria fingerprints and report drift before continuation.
- accept the declared inputs **and** return the declared results under CA-D-516-RESUME_EXECUTION_CONTEXT-ENG_DECISION--encode-resume-execution-context-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
