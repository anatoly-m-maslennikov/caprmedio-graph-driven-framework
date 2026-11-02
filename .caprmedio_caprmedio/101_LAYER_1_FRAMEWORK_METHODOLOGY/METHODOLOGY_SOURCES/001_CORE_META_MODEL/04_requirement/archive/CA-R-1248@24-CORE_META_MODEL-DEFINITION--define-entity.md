---
atom_id: CA-R-1248@24
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity
  depends_on:
  - Entity/Object
  - Entity/Object/Continuant
  - Entity/Object/Occurrent
  - Entity/Aspect
  - Entity/Graph Syntax
  - Entity/Carrier
  - Entity/Term
  - Entity/Property
  - Entity/Graph Syntax <+ Relation
  - Entity/Graph Syntax <+ Format
  - Entity/Graph Syntax <+ Cardinality
  - Entity/Term//Property
version: 24
relations: {}
tier: 1
updated_at: 2026-10-30 08:57:49 +0400
---
## Summary

Define Entity

## Claim

Entity is the common category for every primary graph node and every Property in the framework. Object is one specialization, alongside Aspect, Graph Syntax, Carrier, Term and Property. Not every Entity is an Object. These categories separate abstract Objects, topics, syntax, storage representation and reusable lexical Terms; no occurrence is identified with its persistent record. Term is a direct specialization of Entity; its named instances initially form a flat set without additional Term groups.

An Entity used as a Subject-graph node must identify the thing or topic
addressed by the graph. Its description and Carrier remain distinct from
what they describe or represent. A native file, folder, database row or other
observed Carrier does not by itself admit an Entity instance or establish a
Carrier binding. Admission and representation follow their applicable
authority; an already admitted instance retains its identity when represented.

### Formal claim

```text
Entity/Object
Entity/Object/Continuant
Entity/Object/Occurrent
Entity/Aspect
Entity/Graph Syntax
Entity/Carrier
Entity/Term
Entity/Property
Entity/Graph Syntax <+ Relation
Entity/Graph Syntax <+ Format
Entity/Graph Syntax <+ Cardinality
```

## Semantics

Subjects can address actual things, descriptions and abstract topics without
making them one uniform kind. A description can itself be a separate Subject;
it is not the thing described. Entity categories remain open, and a topic
does not have to be forced into Continuant or Occurrent classification.

A Carrier represents an Entity or its information. A persistent record about
an occurrence is distinct from the occurrence itself; the Carrier does not
store that actual occurrence. The applicable kind and source/runtime
admission rules govern instances. This boundary introduces no separate
Artifact identity or defining Requirement for every runtime instance.

The lexical Term Artifact is defined by its dedicated Method. The CARRIES
Relation Definition owns the binding's direction and meaning, while Delivery
specifies the concrete representation. Those meanings are not redefined here.

## Details

A1302 records the adopted Entity root. The Operator's later confirmed decision places Terms directly at `Entity/Term`, initially flat, and moves authoritative lexical Term Definitions to Content Role Method. The direct kind is `Entity/Property`. Membership in this kind expresses identity dependence on an immediate bearer through `IS_PROPERTY_OF`; it is distinct from the lexical Term at `Entity/Term//Property`. These branches are not asserted to form a disjoint or exhaustive partition. This structural definition retains the other root branches, Object's Continuant/Occurrent distinction and Graph Syntax's existing parts. It introduces no Term groups and implements no Terms Graph.

### Draft source pin

This is a proposed semantic revision of Current CA-R-1248@23, with Summary, Content Role and Entity Definition Type preserved. Source path: `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1248-CORE_META_MODEL-DEFINITION--define-entity.md`. Source SHA-256: `ace51485e016e84415c0a96cdf1ee23abcb57dfea5882f653aac26ea4fe8b152`.

Source-fingerprint snapshot: `/tmp/cce-term-root-migration-20261029/current-before.json`; snapshot SHA-256: `23c1414c96d6e57cdc9f1bf50569de396ef130a7231b765cd8b4511bcb573ad5`. This Draft changes no Current source, assigns no new numeric identity and performs no promotion.

### Consolidated boundary source pins

The Operator approved preserving these boundary meanings here and the lexical Artifact meaning in its Method before the three redundant Current Rules are retired. This is a Draft-only consolidation; it performs no Current retirement and adds no separate Artifact identity or per-instance Definition requirement.

- `CA-R-1262@22` at `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1262-CORE_META_MODEL-RULE--keep-entity-and-artifact-distinct.md`, SHA-256 `398c6acd55c8b34e20eb1139d72383d9a47b17961a581ea289754118d9aec14a`.
- `CA-R-1747@26` at `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1747-CORE_META_MODEL--distinguish-native-targets-from-governed-artifacts.md`, SHA-256 `5efa75b803aa4aa036e6c0c1209d43b604be491275f7c4684f9e33b75cb038a4`.
- `CA-R-1994@14` at `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md`, SHA-256 `41b8b0ef51a71969db07cec2008a19e3c6372e90ae9cc66727de31287d722ce8`.
