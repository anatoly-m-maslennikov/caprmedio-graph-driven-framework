---
atom_id: CA-P-912@4
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Status
  depends_on:
  - Subject/Graph/Rule
  - Status Authority Update
version: 4
updated_at: 2026-10-24 22:06:39 +0400
autonomous_confidence_threshold: 99
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Update Type-Qualified Status Authority

**when** CA-P-911 is Done, **then** the Assignee **must** make every governed Status Property resolve from the complete Entity-Type context.

## Scope

`((every CA-P-905 frontier entry assigned to TYPE_QUALIFIED_STATUS) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (one global Atom Status value domain overrides Type-qualified Status domains **or** Requirement Status does not resolve as `Atom/Content Role: Requirement/Status` **or** Method, Evaluation, or Delivery Status does not resolve under its own Content Role-qualified path **or** Task Status does not resolve as `Atom/Content Role: Plan/Type: Task/Status` **or** any RMED Status lacks the Core values (Draft, Active, Archived) **or** Task Status lacks the Core values (Draft, Active, Done, Canceled) **or** Requirement and Task Status cannot have different allowed values **or** more than one current Status is assigned to one governed Artifact **or** prior Status transitions are required to coexist in current metadata instead of the Journal **or** any replaced conflicting authority remains active).

## Details

keep allowed Status values open to each qualified Entity Type. do not introduce a second revision-disposition axis. leave the shared Carrier key and status-folder materialization to CA-P-913.
