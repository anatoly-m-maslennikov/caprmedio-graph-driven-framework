---
atom_id: CA-C-594
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-24 07:20:16 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/Selection
relations: {}
---
# Summary

Can existing topics resolve the remaining multi-topic Plan Subjects?

## Question

Can the remaining twelve legacy Plans use existing topics and source-defined
Selections without treating their old objectives as new methodology decisions?

## Scope

P083, P108, P109, P112, P113, P908, P922, P939, P942, P943, P946 and P950.
Only Subjects change. Old objectives, completion claims and execution evidence
remain unchanged for the separate content review.

## Details

Use the following bounded interpretation and continue:

- Multi-component work does not by itself need a new Domain entity. Existing
  Engineering topics cover Commit Automation, Carriers, Skill and MCP.
- A frozen consumer set, source frontier, reported conflict set or findings set
  is a named Selection when the owning Plan defines its membership.
- P108's migration map is a Projection. Use that general kind rather than
  introduce or assume a newly registered Projection Type named Map.
- P112 reconciles Operator-owned project purpose and parent-owned scope purpose
  Atoms. These are the latest model's Project Goal and ordinary Goal cases.
  Use the named Selection Scope Unit Goals, with both existing Requirement
  Types and Scope Unit context. Do not restore a separate Job entity or Type.
- P908's completed historical task is about the Artifact concept. Use the
  existing Term//Artifact plus Relation/Rule context. This does not restore an
  Artifact object branch or approve its obsolete taxonomy as a current R rule.
- P943 explicitly creates consumer-owned Demand Atoms. Their existing
  Requirement Type is the governed thing; MCP is supporting context.
- Where a historical source-scope alias names LOCAL_CONFIGURATION, use the
  already-registered PROJECT_CONFIGURATION Scope Unit in the new Subject.
  Preserve the old spelling in task bodies until their content migration.

Keep unclassified activity labels and predecessor IDs literal in DEPENDS_ON
for later mapping; do not make them fictitious Occurrent instances, new Domain
properties or generic Terms merely to produce a canonical-looking graph.

The source-specific proofs record each body anchor, proposed target and
unchanged-source pin. These are the Operator-authorized low-blast best choices
after Candidate #7, the plan, latest input and principles were checked. No
implementation, deployment, live approval or old Task execution is performed.
