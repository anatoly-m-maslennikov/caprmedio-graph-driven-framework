---
atom_id: CA-O-228
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 11
updated_at: 2026-10-27 19:59:48 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-228-PROJECT_CONFIGURATION-STEP--diagnose-failed-evaluations-before-semantic-review.md
  source_atom_id: CA-O-228
  source_atom_revision: 11
  source_sha256: c83cf8d42419c118986f68951a6d7f7c442e80ccc40c9861fd460f4a8e340188
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Diagnose failed Evaluations before semantic review

## Operation

This Step invokes CA-O-089 in Isolated context with the exact candidate, failed output, selected existing Plan or actual admitted in-session P/task including instruction/Definition of Done/source context, complete prepared tests/checks, phase, R/E/D and M bindings, relevant inputs, confidence/permission gates, and report/run bindings. CA-O-089's input and semantics remain unchanged.

Retain and pass its six possible results unchanged: `expected_initial_failure`, `implementation_defect`, `test_implementation_defect`, `authority_change_required`, `environment_blocker`, and `unresolved`. Do not edit code, tests, expected behavior, Atoms, or status.

## Details

No hidden retry or repair route and no unsupported subagent promise. The Workflow's semantic Step applies the explicit result mapping and retains failed checks, findings, blockers, and uncertainty.
