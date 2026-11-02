---
atom_id: CA-O-100@14
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Method Lesson Drafting'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Engineering/Implementation Reconstructability
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
version: 14
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
tier: 3
---
# Summary

Draft Methods from verified implementation issues

## Operation

Method Lesson Drafting **means** the Agentic Action that derives a bounded Standard Method Draft from a verified implementation issue **in** a separately admitted learning Run.

- inputs: an explicit learning request, bounded P/Plan work, retained admitted Evaluation-portfolio results, relevant focused-regression results, reproducible failure, diagnosis, actual fix, passing regression evidence, current governing Method/RED authority, existing related Drafts, **and** confidence/permission gates.
- require sufficient evidence that the proposed correction explains the defect **and** that relevant checks pass on the fixed candidate. an initial test failing because behavior is not implemented yet is **not** a Method lesson; uncertain **or** stale evidence returns `blocked`.
- check existing Methods **and** pending Drafts before writing. return `already_covered` with their references **when** no distinct Method is needed; repeated failures **must not** create duplicate lessons.
- **when** a missing Method is justified **and** authoring is admitted, create **or** refine the applicable Standard Draft with **=1** Claim, its precise governed Entity, correct Scope Unit, actual Author, structured content, **and** linked evidence. preserve Summary identity rules **and** keep Drafts without assigned Atom IDs.
- return `drafted` with the Draft references **and** evidence for separate acceptance by CA-O-090, **or** `blocked` with the unmet gate. this Action does **not** promote Methods **or** generalize them into broader policies.

## Details
