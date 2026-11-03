---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Tier
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Atom.Status
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
version: 12
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-2504
  - CA-R-2125
  - CA-R-2428
  - CA-R-2131
  - CA-R-2132
  - CA-R-2149
  - CA-M-438
atom_id: CA-E-654
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Evaluation
form: Eval Case
---
## Summary

Validate Integer Tier Ordering and Scope Constraints

## Claim scope

Current RMEDO source Atoms and their permitted Current Atom targets.

## Claim

this Evaluation **must** cover one coherent numeric graph-ordering case:

- ordinary Project-owned and non-Project Scope Unit-owned Atoms carry integer Tier **>=0**; a verified Project Goal carries exactly Tier **-1**;
- a verified Operator-owned Project Goal retains its Actor owner and uses its Target Project only as ordering context; a same-Project root Atom at Tier 0 may target that Tier -1 Goal, and a descendant-Scope Atom may target it through strict ancestry; unverified Goals or Goals of another Project do not pass;
- the integer Tier is independent of Content Role, Type, semantic abstraction, Claim Scope breadth, filename, structural depth, and any named category;
- for every stored governing Current R/M/E/D relation occurrence selected under CA-R-2148@10, a same-Scope target has a strictly lower Tier than its source, except an admitted typed governing relation from a local Tier 0 Method, Evaluation or Delivery source to a local Tier 0 Requirement target; where an Operations source has an independently admitted typed governing relation to a Requirement, the same narrow exception applies; no new Operations relation is admitted;
- a strict-ancestor target is permitted without Tier comparison; the exact one-way source-Project-Configuration-to-target-Core-Meta-Model logical-role prerequisite declared by CA-R-1218@31 is permitted without Tier comparison when both roles resolve within the same Project; reverse Core-to-Project-Configuration, Project-root-to-Core, Methodology-Sources-root-to-Core, Extension-to-Core, Project-Configuration-to-Extension, cross-Project, and unresolved-role cases do not pass; every other descendant and sibling target is forbidden;
- the CA-R-2148@10 Selection source endpoint is Current R/M/E/D, while the target may be any Current Atom permitted by the registered relation endpoint definition; an independently admitted Operations-source exception is checked separately;
- equal Tier 0 is rejected for R-to-R, R-to-M/E/D/O and M/E/D/O-to-M/E/D/O, and for any relation or endpoints not admitted by its defining declaration; ancestor and declared prerequisite alternatives remain unchanged;
- valid existing integers are preserved, and a source integer may be raised when required by the same-Scope ordering and admitted owner range;
- unknown relation membership or endpoints, missing Tier/scope/parentage, unresolved logical-role identity, unresolved Project correspondence, an unresolved CA-R-1218@31 prerequisite declaration, derived inverse views, and cycles are unresolved failures, not silent passes.

No Content-Role or Type-to-Tier restriction is introduced by this case.
