---
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/Atom.Status
version: 17
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1520@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Return Workflow handoffs through terminal results

## Scope

Workflow handoffs to another Workflow.

## Claim

**when** a Workflow declares a handoff **to** another Workflow, its Run **must** end with a terminal result sufficient for the executor **to** evaluate **and** start the continuation separately.

## Details

### Handoff result

- identify the completed Run, the reason for handoff, **and** the continuation Workflow **or** the methodology rule that selects it.
- provide the target identities **and** observed Revisions, required inputs **and** parameters, proposed changes, completed checks **and** their applicability, **and** a complete account of effects already performed, **if** **any**.
- distinguish a requested continuation from an authorized, started, **or** completed continuation. an incomplete result **must not** trigger guessed execution.

### Run boundary

- the ending Run does **not** call the continuation Workflow, wait for it, **or** resume its own normal Steps afterward.
- the executor retains the original request **and** the association between predecessor **and** successor Runs; it rechecks applicable authority **and** input freshness **before** starting the successor.
- ending the predecessor **must not** report the requested work as complete **when** a required continuation is still pending, blocked, **or** failed.
- the handoff outcome does **not** itself add a Status value. a chain of handoffs **must not** bypass approval, refresh an exhausted retry allowance, **or** create an unbounded loop.

the handoff is a result between distinct Runs, **not** an ON_RESULT edge between Steps of different Workflows.
