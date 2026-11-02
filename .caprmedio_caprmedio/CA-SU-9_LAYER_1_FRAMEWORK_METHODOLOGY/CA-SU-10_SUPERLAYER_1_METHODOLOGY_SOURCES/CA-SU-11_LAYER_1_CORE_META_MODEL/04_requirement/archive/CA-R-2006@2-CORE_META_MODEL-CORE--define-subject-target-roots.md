---
subjects:
  governs: "Subject"
atom_id: "CA-R-2006@2"
content_role: "Requirement"
type: "Rule"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
version: 2
updated_at: "2026-10-22 16:26:09 +0000"
author: "Anatoly Maslennikov"
global_tier: 9
relations: {}
---
# Summary

Define Subject Target Roots

## Scope

canonical Subject paths in this model.

## Claim

a canonical Subject path **must** start at `Subject`. its current branches are `Domain`, `Engineering` and `Graph`. `Graph` includes `Relation` and `Rule` topics that apply within and across branches.

## Details

Domain names what the project means and offers. Engineering names how it is structured, built, stored and operated. Graph names connections and their constraints. these branches do not assign a Content Role and do not replace the kinds described by the graph.

the model can expand. UX and Design are not admitted targets for this migration. a Scope Unit path is not automatically a Subject path.
