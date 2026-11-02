---
subjects:
  governs: "Plan Blocking Relations"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Plan Graph", "Entity/Node/Continuant/Atom/Content Role: Plan.Status: Done", "Hub Atom", "Subject Relation Kind: DEPENDS_ON"]
version: 7
updated_at: "2026-10-19 15:53:35 +0400"
relations: {"relates_to": ["CA-R-1583", "CA-D-471", "CA-R-1200"]}
atom_id: "CA-R-1580"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1580-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-blocking.md
  source_atom_id: CA-R-1580
  source_atom_revision: 7
  source_sha256: 699820b2af9a396180702e330f3c9af69543ac15a29c64a0edecb688536811c9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Plan blocking

## Scope

Plan-blocking Relations in the Plan Graph.

## Claim

**in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` **may** start **only** **after** Plan `A` is Done.

- a Plan **may** block **>=0** other Plans **and** have **>=0** blockers.
- **all** blockers **must** be Done **before** the blocked work starts.
- navigation order, a shared Hub, **and** `DECOMPOSES_INTO` do **not** establish `BLOCKS`.
- an inverse lookup is derived from the same explicit fact, **not** separately authored; Subject DEPENDS_ON remains a different Relation Kind.

## Details

### relation admission

- owning graph kind: Plan Graph under CA-R-1593; endpoints are Plan Atom references **in** that graph, **not** native nodes of a different graph.
- Status: the Relation Kind is Active; endpoint Plan Revisions use the admitted Plan Status model, **without** requiring every historical **or** pending endpoint **to** be Active.
- authority effect: retain the existing endpoint identities, Claims, Scope Units, **and** tiers; this Relation does **not** transfer authority.
- cardinality: **>=0** distinct direct targets **and** **>=0** distinct incoming blockers; inverse direction is blocked Plan **to** blocker.
- transitivity: retain **only** explicit direct edges; prerequisite reachability **may** be derived for readiness **and** cycle checks **without** creating authored transitive edges.
