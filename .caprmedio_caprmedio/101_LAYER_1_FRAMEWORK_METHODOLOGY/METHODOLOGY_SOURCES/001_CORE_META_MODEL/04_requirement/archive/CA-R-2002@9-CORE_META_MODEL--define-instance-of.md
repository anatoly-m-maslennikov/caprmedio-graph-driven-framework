---
atom_id: CA-R-2002@9
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Relation/Type: INSTANCE_OF'
  depends_on:
  - Subject/Graph Node
  - Subject/Graph Relation
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Entities Graph'
relations: {}
version: 9
updated_at: 2026-10-25 17:32:27 +0400
tier: 1
type: Definition
---
# Summary

Define INSTANCE_OF

## Scope

The INSTANCE_OF Relation in the Entities Graph.

## Claim

An INSTANCE_OF Relation from Entity I to kind K **means** that I is a particular instance classified by K, not a narrower kind of K.

## Semantics

`K//Name` qualifies an existing named instance of a primary kind K. It does not instantiate a dependent property. The Subject uses the instance's name, not its Atom ID; it retains that instance's existing identity. The Relation points from instance to kind, while readable navigation goes from kind to the named instance. This is distinct from specialization, bearer dependence and allowed-value qualification. A reusable Workflow definition can be an Atom instance of the Workflow kind; it is not that Workflow's actual execution. An instance name is not automatically a Term. Parsing a name does not create or admit an instance or establish its canonical target.

A property can follow a named primary instance using `.`: for example,
`Selection//Projection and Journal Authority Sources.updated_at` names that
Selection instance's property. It does not make the property a primary
instance or give it another independent identity.

Names must be unique within the same entity kind in the project's Current
source view, across owning Scope Units. Two Workflows cannot share a name;
a Workflow and a Scope Unit may share a name because their kinds differ.
This does not prescribe case folding, a name registry or new mandatory names.

## Details

### relation admission

- Status: the INSTANCE_OF Relation Kind is Active.
- Owning graph kind: Entities Graph.
- Direct direction: instance to kind.

No new name registry, inverse Relation Kind, default, constraint or inference policy is introduced.
