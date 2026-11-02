---
atom_id: CA-R-2002
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Relation/Type: INSTANCE_OF'
  depends_on:
  - Entity
  - Entity/Relation
  - 'Entity/Node/Continuant/Projection/Type: Entities Graph'
relations: {}
version: 1
updated_at: "2026-10-20 04:48:02 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-2002-CORE_META_MODEL-CORE--define-instance-of.md
  source_atom_id: CA-R-2002
  source_atom_revision: 1
  source_sha256: a579053a765f6ee71bcca90b5da8441aef1c851707c433d15c140ccec3e357f5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
