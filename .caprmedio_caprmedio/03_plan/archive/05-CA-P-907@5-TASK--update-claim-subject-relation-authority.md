---
atom_id: CA-P-907@5
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs: Subject/Graph/Relation
  depends_on: []
version: 5
updated_at: 2026-10-25 00:54:14 +0400
autonomous_confidence_threshold: 99
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Update Claim-Subject Relation Authority

**when** CA-P-916 is Done, **then** the Assignee **must** make the Claim-Subject authority treat Subjects as independent referenced Entities and every relation as doubly classified.

## Scope

`((every CA-P-905 frontier entry assigned to CLAIM_SUBJECT_RELATION) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (Subject is defined as a descendant or bearer-dependent Entity of Atom, Claim, or Artifact **or** a Claim-Subject relation is interpreted as storing or owning its referenced Subject Entity **or** any Claim-Subject relation lacks exactly one Kind in (GOVERNS, DEPENDS_ON) **or** any Claim-Subject relation lacks exactly one Temporal Form in (CONTINUANT, OCCURRENT) **or** Temporal Form classifies Subject, Content Role, CAPO, RMED, or either relation endpoint **or** an Atom has no GOVERNS Subject relation **or** an Atom has more than one CONTINUANT GOVERNS relation or more than one OCCURRENT GOVERNS relation **or** an Atom has more than two GOVERNS Subject relations in total **or** DEPENDS_ON relations are subjected to the GOVERNS cardinality limit **or** a Definition Atom omits its defined Term from a GOVERNS relation **or** an Atom omits a governed prerequisite Subject from a DEPENDS_ON relation **or** the global Subject Projection is manually authoritative instead of mechanically derived from current Claim-Subject relations **or** `Subject/Temporal Form` or `Atom/Content Role/Temporal Form` remains active authority **or** any replaced conflicting authority remains active).

## Details

the referenced Subjects remain independent of the Artifact that declares their relations. make Temporal Form a classification of the relation occurrence only. leave frontmatter keys, nesting, and other Carrier serialization to CA-P-913.
