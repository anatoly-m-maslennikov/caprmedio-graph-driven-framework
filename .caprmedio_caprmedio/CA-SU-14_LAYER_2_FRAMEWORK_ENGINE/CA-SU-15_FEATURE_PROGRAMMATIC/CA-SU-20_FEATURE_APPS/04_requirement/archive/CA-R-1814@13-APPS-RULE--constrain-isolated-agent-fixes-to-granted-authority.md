---
atom_id: CA-R-1814
ref_id: CA-R-1814
container:
  scope_unit: CA-SU-20
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
status: Archived
version: 13
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1814@13-APPS-RULE--constrain-isolated-agent-fixes-to-granted-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
---
# Summary

Constrain isolated Agent fixes to granted authority

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** admit Agent-proposed changes **only** within the Operator-granted selection **and** permissions.

## Details

- initial automated fixes preserve Version; a Version-changing proposal pauses for a governed Revision history transition rather than overwriting previous authority.

- checks use read-only isolated Codex CLI sessions.
- fix Agents return proposed content; the orchestrator applies admitted content, rather than granting Agents unrestricted access **to** the Project.
- ordinary automated fixes retain the Atom ID **and** Summary. `allow_replacements=true` **with** fix permission authorizes a Summary-changing replacement of a selected Atom: allocate an unreused successor ID, publish Version **`=1`**, archive the predecessor, **and** retain confirmed Journal **and** report evidence.
- replacement permission defaults **to** false. undelegated replacement, retirement, missing authority **or** confidence below the requested threshold require an interrupted Run with explicit blockers. replacement permission does **not** expand the selection **or** authorize changes **to** other Atoms.
- completion requires the existing report admission **and** progress criteria; a worker exit code **alone** proves no semantic completion.
- credentials remain outside requests, prompts, reports **and** source authority.
