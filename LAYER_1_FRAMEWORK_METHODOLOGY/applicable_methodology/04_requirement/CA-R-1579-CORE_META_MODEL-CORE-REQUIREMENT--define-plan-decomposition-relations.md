---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Plan Graph", "Entity/Node/Continuant/Atom/Content Role: Plan.Label", "Relation Kind", "Entity/Node/Continuant/Atom/Content Role: Plan.Status", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom.Substance"]
version: 8
updated_at: "2026-10-19 15:53:35 +0400"
relations: {"relates_to": ["CA-D-481", "CA-R-1574", "CA-R-1583"]}
atom_id: "CA-R-1579"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1579-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-decomposition-relations.md
  source_atom_id: CA-R-1579
  source_atom_revision: 8
  source_sha256: d1c89fbca0ee38f44308a2a40a61d344cf1f8a5b6bfc748f4720de9491468e53
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Plan decomposition Relations

## Scope

Plan-decomposition Relations in the Plan Graph.

## Claim

**in** the Plan Graph, `A DECOMPOSES_INTO B` **means** that completing Plan `B` contributes required work **to** completing Plan `A`; `B IS_DECOMPOSITION_OF A` is the inverse view of the same fact.

- the source **and** target are distinct Plan Atoms, independently of their Labels.
- decomposition is an all-of relation: **all** decomposed Plans are required for completion under CA-R-1583.
- decomposition concerns planned work, **not** Claim containment, Scope Unit parentage, **or** Type inheritance.
- the decomposing Plan owns the direct `IS_DECOMPOSITION_OF` declaration under CA-D-481; derive `DECOMPOSES_INTO` from that same fact, **not** from folder placement.

## Details

### relation admission

- owning graph kind: Plan Graph under CA-R-1593; endpoints are Plan Atom references **in** that graph, **not** native nodes of a different graph.
- Status: the Relation Kind is Active; endpoint Plan Revisions use the admitted Plan Status model, **without** requiring every historical **or** pending endpoint **to** be Active.
- authority effect: retain the existing endpoint identities, Claims, Scope Units, **and** tiers; this Relation does **not** transfer authority.
- cardinality: **`<=1`** authored `IS_DECOMPOSITION_OF` target **and** **`>=0`** derived `DECOMPOSES_INTO` targets per Plan.
- transitivity: the direct Relation is **not** transitively materialized; recursive reachability is derived under CA-R-1537.
