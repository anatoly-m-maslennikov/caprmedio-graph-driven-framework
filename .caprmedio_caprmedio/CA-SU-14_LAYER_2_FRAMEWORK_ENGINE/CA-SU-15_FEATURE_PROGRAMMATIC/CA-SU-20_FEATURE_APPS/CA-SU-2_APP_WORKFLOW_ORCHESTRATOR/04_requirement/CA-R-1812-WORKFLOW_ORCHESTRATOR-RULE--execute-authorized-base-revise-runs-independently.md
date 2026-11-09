---
atom_id: CA-R-1812
ref_id: CA-R-1812
container:
  scope_unit: CA-SU-2
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect Authorization"
tier: 3
status: Active
version: 12
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1812-WORKFLOW_ORCHESTRATOR-RULE--execute-authorized-base-revise-runs-independently.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/04_requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

Execute authorized Base Revise Runs independently

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** execute an Operator-authorized RMED Atoms Base Revise Run independently of the requesting session.

## Details

- accept a stable Run ID, explicit Atom selection, current rule files, named Author, confidence threshold **and** permissions.
- execute gather, check **and** fix using the existing Action prompts **and** coordination Tool; preserve the initial checks **without** adding a recheck phase.
- return admission promptly. a separately started local worker executes queued Runs after the MCP client disconnects.
- report queued, running, completed, failed **or** interrupted execution honestly; provide saved status, results **and** recovery through existing observation capabilities.
- initial support is the existing RMED Atoms Base Revise Workflow. unknown Workflow definitions are explicit unsupported requests.
