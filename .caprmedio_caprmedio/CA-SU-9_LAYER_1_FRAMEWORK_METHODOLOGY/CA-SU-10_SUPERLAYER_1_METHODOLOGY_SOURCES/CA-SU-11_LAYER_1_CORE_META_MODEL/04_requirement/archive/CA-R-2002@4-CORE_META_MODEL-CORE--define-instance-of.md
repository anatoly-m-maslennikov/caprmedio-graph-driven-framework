---
atom_id: CA-R-2002@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph/Relation/Type: INSTANCE_OF'
  depends_on:
  - Entity
  - Subject/Graph/Relation
  - 'Subject/Domain/Node/Continuant/Projection/Type: Entities Graph'
relations: {}
version: 4
updated_at: 2026-10-24 00:38:25 +0400
tier: 1
---
# Summary

Define INSTANCE_OF

## Scope

The INSTANCE_OF Relation in the Entities Graph.

## Claim

An INSTANCE_OF Relation from Entity I to kind K **means** that I is a particular instance classified by K, not a narrower kind of K.

## Semantics

`K//Name` qualifies an existing named instance of K. The Subject uses the instance's name, not its Atom ID; it retains that instance's existing identity. The Relation points from instance to kind, while readable navigation goes from kind to the named instance. This is distinct from specialization, bearer dependence and allowed-value qualification. A reusable Workflow definition can be an Atom instance of the Workflow kind; it is not that Workflow's actual execution. An instance name is not automatically a Term. Parsing a name does not create or admit an instance or establish its canonical target.

## Details

### relation admission

- Status: the INSTANCE_OF Relation Kind is Active.
- Owning graph kind: Entities Graph.
- Direct direction: instance to kind.

No new name registry, inverse Relation Kind, default, constraint or inference policy is introduced.
