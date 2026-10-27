---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit.Parent
  - Subject/Domain/Node/Continuant/Atom.Status
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - Subject/Graph/Rule
  - Subject/Graph/Rule.Applies To
  - Subject/Graph/Rule.Condition
version: 5
updated_at: 2026-10-25 14:32:49 +0400
relations:
  evaluation_for:
  - CA-R-2124
  - CA-R-2125
  - CA-R-2130
  - CA-R-2131
  - CA-R-2132
  - CA-R-2149
  - CA-M-438
atom_id: CA-E-654@5
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 5
---
# Summary

Validate Integer Tier Ordering and Scope Constraints

## Scope

Current RMEDO source Atoms and their permitted Current Atom targets.

## Claim

this Evaluation **must** cover one coherent numeric graph-ordering case:

- ordinary Project-owned Atoms carry integer Tier **>=0**; ordinary non-Project Atoms carry integer Tier **>=1**; a verified Project Goal carries exactly Tier **-1**;
- a verified Operator-owned Project Goal retains its Actor owner and uses its Target Project only as ordering context; a same-Project root Atom at Tier 0 may target that Tier -1 Goal, and a descendant-Scope Atom may target it through strict ancestry; unverified Goals or Goals of another Project do not pass;
- the integer Tier is independent of Content Role, Type, semantic abstraction, Claim Scope breadth, filename, structural depth, and any named category;
- for every stored governing Current R/M/E/D relation occurrence selected under CA-R-2148, a same-Scope target has a strictly lower Tier than its source;
- a strict-ancestor target is permitted without Tier comparison; the exact one-way source-Project-Configuration-to-target-Core-Meta-Model logical-role prerequisite declared by CA-R-1218 is permitted without Tier comparison when both roles resolve within the same Project; reverse Core-to-Project-Configuration, Project-root-to-Core, Methodology-Sources-root-to-Core, Extension-to-Core, Project-Configuration-to-Extension, cross-Project, and unresolved-role cases do not pass; every other descendant and sibling target is forbidden;
- the source endpoint is Current R/M/E/D, while the target may be any Current Atom permitted by the registered relation endpoint definition;
- valid existing integers are preserved, and a source integer may be raised when required by the same-Scope ordering and admitted owner range;
- unknown relation membership or endpoints, missing Tier/scope/parentage, unresolved logical-role identity, unresolved Project correspondence, an unresolved CA-R-1218 prerequisite declaration, derived inverse views, and cycles are unresolved failures, not silent passes.

No Content-Role or Type-to-Tier restriction is introduced by this case.
