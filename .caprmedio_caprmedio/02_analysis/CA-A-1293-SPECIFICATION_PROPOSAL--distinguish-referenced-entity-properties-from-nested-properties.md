---
atom_id: CA-A-1293
ref_id: CA-A-1293
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1293-CAPRMEDIO-SPECIFICATION_PROPOSAL--distinguish-referenced-entity-properties-from-nested-properties.md
    path: .caprmedio_caprmedio/02_analysis
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Distinguish referenced-entity properties from nested properties

## Proposed notation

Use the explicit reference boundary:

```text
(atom.owning_scope_unit).name
```

atom.owning_scope_unit identifies the Atom's referenced Scope Unit. The parenthesized reference is followed to that entity, and .name reads the Scope Unit's own Name. It is not an Atom-local nested owning_scope_unit.name property and does not require a duplicated nested name field in the Atom carrier.

The refined conditional example is:

```text
atom.tier[int, if (atom.owning_scope_unit).name = 'project' then >=-1 else >=1]
```

This supersedes the direct chained owner-name spelling in A1292. Reference meaning comes from the property definition or relation; parentheses do not turn every arbitrary string into an entity reference. The logical example does not rename an existing YAML property or create another Subject entity.

## Boundary

This remains a reference-traversal and conditional-expression proposal. It does not redefine normal nested-property access such as atom.content.claim.formal_claim. The earlier distinction between required prose and the optional formal child remains unchanged.

The Tier-policy questions and literal project in A1292 remain unresolved by this notation refinement. Keep existing Tier rules until that separate meaning is settled.

## State

Proposal and Epic tracking only. No Current source, Core syntax Definition, main Model constraint, governing configuration, tool or runtime is changed.
