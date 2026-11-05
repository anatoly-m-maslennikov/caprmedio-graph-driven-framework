---
atom_id: CA-E-654
ref_id: CA-E-654
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
tier: 5
relations:
  evaluation_for:
  - CA-R-2706
  - CA-R-2125
  - CA-R-2428
  - CA-R-2131
  - CA-R-2132
  - CA-R-2149
  - CA-M-438
status: Active
version: 13
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-E-654-CORE_META_MODEL-EVAL_CASE--validate-integer-tier-ordering-and-scope-constraints.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Integer Tier Ordering and Scope Constraints

## Claim

### Prose Claim


Current RMEDO source Atoms and their permitted Current Atom targets.


this Evaluation **must** cover one coherent numeric graph-ordering case:

- ordinary Project-owned and non-Project Scope Unit-owned Atoms carry integer Tier **>=0**, except any Atom of Form Goal whose active Subject resolves to the Project Scope Unit root; that exact predicate carries Tier -1 regardless of Container or owner;
- the Project-root Goal uses that Project as its ordering context under CA-R-2132; a same-Project root Atom at Tier 0 may target that Tier -1 Goal, and a descendant-Scope Atom may target it through strict ancestry; a Form Goal resolving to another Scope Unit or an unresolved active Subject does not satisfy the Project-root Goal predicate, and a non-Goal Form with a Project-root active Subject remains in the ordinary range;
- the integer Tier is independent of Content Role, Type, semantic abstraction, Claim Scope breadth, filename, structural depth, and any named category;
- for every stored governing Current R/M/E/D relation occurrence selected under CA-R-2148@10, a same-Scope target has a strictly lower Tier than its source, except an admitted typed governing relation from a local Tier 0 Method, Evaluation or Delivery source to a local Tier 0 Requirement target; where an Operations source has an independently admitted typed governing relation to a Requirement, the same narrow exception applies; no new Operations relation is admitted;
- a strict-ancestor target is permitted without Tier comparison; the exact one-way source-Project-Configuration-to-target-Core-Meta-Model logical-role prerequisite declared by CA-R-1218@31 is permitted without Tier comparison when both roles resolve within the same Project; reverse Core-to-Project-Configuration, Project-root-to-Core, Methodology-Sources-root-to-Core, Extension-to-Core, Project-Configuration-to-Extension, cross-Project, and unresolved-role cases do not pass; every other descendant and sibling target is forbidden;
- the CA-R-2148@10 Selection source endpoint is Current R/M/E/D, while the target may be any Current Atom permitted by the registered relation endpoint definition; an independently admitted Operations-source exception is checked separately;
- equal Tier 0 is rejected for R-to-R, R-to-M/E/D/O and M/E/D/O-to-M/E/D/O, and for any relation or endpoints not admitted by its defining declaration; ancestor and declared prerequisite alternatives remain unchanged;
- valid existing integers are preserved; an ordinary Scope Unit-scoped source Tier may be raised only when its applicable range permits it; a Project-root Goal remains fixed at Tier -1 under CA-R-2132 and cannot be raised to satisfy an ordering edge;
- unknown relation membership or endpoints, missing Tier/scope/parentage, unresolved logical-role identity, unresolved Project correspondence, an unresolved CA-R-1218@31 prerequisite declaration, derived inverse views, and cycles are unresolved failures, not silent passes.

No Content-Role or Type-to-Tier restriction is introduced by this case.
