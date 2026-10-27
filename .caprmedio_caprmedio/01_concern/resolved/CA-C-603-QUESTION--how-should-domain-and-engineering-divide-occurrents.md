---
atom_id: CA-C-603
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Resolved
author: Anatoly Maslennikov
tier: 3
version: 2
updated_at: 2026-10-25 17:27:47 +0400
subjects:
  governs: Subject/Graph Node
relations: {}
---
# Summary

How should Domain and Engineering divide Occurrents?

## Question

Should Domain and Engineering have separate Occurrent branches, or should all
Occurrents share one branch? If there is only one branch, where does it belong?
If both exist, what is the boundary between them?

## Scope

The Subject model's Domain and Engineering branches, including modeled work
execution and the technical runtimes that execute it.

## Details

The Operator deferred this classification decision. The approved Graph Node,
Graph Relation and Graph Rule root reshape can proceed independently; it must
not silently move all Occurrents into Engineering or add a second authoritative
representation of the same occurrence.

The Operator then proposed this distinction for review:

- Domain/business: runs of modeled work, such as Action Run, Step Run and
  Workflow Run.
- Engineering: technical runtimes, such as a session, tool process or running
  application/server.

Judge the distinction by what is represented, not by the word "run". A modeled
Workflow Run can use multiple technical runtimes; those are different
occurrences. Review the exact placement of existing Session, Event and
Execution definitions before a later classification migration.

UX concerns the MCP interface and health-page appearance, not their backend
runtime. This clarification does not resolve the Occurrent taxonomy by itself.

No classification migration or decision is claimed by creating this Question.

## Resolution

The Operator approved the distinction: "good, let's do it. so, eng and domain
both now have occurent and continuant". This supersedes the temporary deferral
above.

- Domain/Occurrent includes modeled Action Runs, Step Runs and Workflow Runs.
- Engineering/Occurrent includes technical sessions and actual tool/app
  runtimes. Technical components and carriers belong under Engineering/Continuant.
- Domain also retains Continuant. Classification follows what the Subject
  describes, not the presence of the word "run".
- UX concerns the MCP interface and health-page appearance, not backend code.

Apply this bounded structural placement in Engine Epic P2637's first task,
P2638. Abstract engineering-policy topics need not be invented as independently
carried runtime objects. The remaining Engine migration stays separate.
