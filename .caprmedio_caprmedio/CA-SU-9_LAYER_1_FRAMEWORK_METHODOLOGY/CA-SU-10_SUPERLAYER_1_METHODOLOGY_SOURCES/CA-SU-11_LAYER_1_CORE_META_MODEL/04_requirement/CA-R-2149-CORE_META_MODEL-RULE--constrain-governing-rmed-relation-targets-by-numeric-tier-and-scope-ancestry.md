---
atom_id: CA-R-2149
ref_id: CA-R-2149
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Active
version: 15
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-2149-CORE_META_MODEL-RULE--constrain-governing-rmed-relation-targets-by-numeric-tier-and-scope-ancestry.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

## Claim

### Prose Claim


Stored governing Requirement, Method, Evaluation and Delivery relation occurrences selected under CA-R-2148@10, and any independently admitted Operations-source relation within the narrow Tier 0 exception.


Each stored governing RMED relation must target an Atom in the same ordering Scope Unit at a strictly lower numeric Tier or satisfy the narrow Tier 0 exception below, an Atom in a strict ancestor ordering Scope Unit, or the Core Meta-model prerequisite of Project Configuration explicitly declared by CA-R-1218@31. The prerequisite exception is one-way and non-transitive. Other descendant and sibling targets are forbidden. Unresolved membership, endpoint, Tier or Scope evidence does not pass. An Atom of Form Goal whose active Subject resolves to the Project Scope Unit root uses that Project as its ordering context for this check under CA-R-2132.

As a narrow exception, within the same Local Scope Unit, a Tier `0` Method, Evaluation, Delivery or Operations source may target a Tier `0` Requirement only through a stored typed governing relation already admitted for those endpoints by its defining declaration. Equal Tier `0` does not otherwise pass: it does not admit Requirement-to-Requirement, Requirement-to-M/E/D/O, or M/E/D/O-to-M/E/D/O links. This exception creates no Relation Kind or Operations relation admission and does not establish an automatic conflict winner.

These constraints apply to the source-declared Selection “Stored Governing RMED Relation Occurrences”, not to arbitrary context or history links. There is no automatic conflict winner based on Tier, timestamp or these ordering rules.

## Semantics

An Atom of Form Goal whose active Subject resolves to the Project Scope Unit root uses that Project as its ordering context; ordinary endpoints use their Local Scope Unit. Apart from the explicitly stated equal-Tier-0 exception, the numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218@31; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.
