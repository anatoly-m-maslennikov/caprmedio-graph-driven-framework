---
atom_id: CA-C-602
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Resolved
author: Anatoly Maslennikov
tier: 3
version: 2
updated_at: 2026-10-24 17:00:51 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal
relations: {}
---
# Summary

What does the Projection and Journal inventory Task govern?

## Question

Does CA-P-1087's old Artifact Subject name the selected source set, the
represented artifacts, or their general classification?

## Scope

The one governing Subject in Current CA-P-1087. This is not a new Domain
entity, selector language or general mapping of Artifact to Selection.

## Details

Bounded choice: use the existing Selection Subject. The Task establishes an
inventory of selected source authority about Projections and Journals. Its
Scope supplies the actual source boundary; it does not define Artifact or a
new kind of object. Preserve its body, lifecycle, relations and other Subjects.

This records interpretation uncertainty for the later content review under
CA-P-1970. It does not create a new named Selection, executable predicate,
runtime behavior or proof that the old Task was executed.

## Resolution

Operator answers consolidated on 2026-10-24.

The Operator approved a named Selection for the bounded source inventory:
Selection//Projection and Journal Authority Sources. Named Selection is not a
new Object kind. Current P1087 now governs that named Selection; its exact
membership boundary stays in its existing content. Batch300 records the
Subjects-only update, preserving its Done Status, body and typed relations.

The Operator also confirmed that // names an instance of a primary kind, not
a property instance. A following property remains valid, for example
Selection//Projection and Journal Authority Sources.updated_at. Names are
unique within the same entity kind, not across different kinds. The Core
INSTANCE_OF and Subject Expression definitions are aligned in batch300;
no parser, selector engine or runtime implementation is claimed.
