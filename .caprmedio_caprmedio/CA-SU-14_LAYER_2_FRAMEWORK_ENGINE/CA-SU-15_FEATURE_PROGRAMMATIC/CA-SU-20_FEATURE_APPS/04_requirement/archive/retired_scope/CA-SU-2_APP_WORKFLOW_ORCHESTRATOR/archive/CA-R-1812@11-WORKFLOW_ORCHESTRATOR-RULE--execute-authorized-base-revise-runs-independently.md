---
atom_id: CA-R-1812@11
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
relations: {}
type: Rule
tier: 3
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
