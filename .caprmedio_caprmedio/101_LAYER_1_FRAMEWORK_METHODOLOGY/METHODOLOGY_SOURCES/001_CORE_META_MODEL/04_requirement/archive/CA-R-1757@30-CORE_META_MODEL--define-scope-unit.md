---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
  depends_on:
  - Entity/Object/Continuant
  - Entity/Object/Continuant/Governing Objects/Atom
version: 30
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-R-1757@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Scope Unit

## Claim scope

Scope Units.

## Claim

A Scope Unit means a Continuant Node that provides an ownership boundary for Atoms and may structurally contain child Scope Units, Atoms and Projections. Project is the parentless root Scope Unit. Recursive kind containment does not permit a Scope Unit instance to structurally contain itself.

### Formal claim

```text
Scope Unit/Project
Scope Unit > @(Scope Unit)
Scope Unit > @(Atom)
Scope Unit > @(Projection)
```

## Details

The contained Scope Units, Atoms and Projections are parts, not vocabulary registrations. In abbreviated schema notation use Scope Unit >@(Scope Unit), Scope Unit >@(Atom), and Scope Unit >@(Projection). These references reuse existing kinds and do not imply subtype inheritance. This declaration permits the listed endpoint kinds; it does not add an unlimited Carrier containment rule or replace separate parent-cardinality, local Scope assignment or Project Goal Operator-ownership rules. The direct IS_CONTAINED_BY / derived CONTAINS direction remains unchanged.

CA-A-1258 records the Project-root decision.
