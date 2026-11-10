---
atom_id: CA-R-1814@10
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Workflow Orchestration/Authority-Bounded Proposal Admission
relations:
  relates_to:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  - CA-O-104
type: Rule
tier: 3
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
