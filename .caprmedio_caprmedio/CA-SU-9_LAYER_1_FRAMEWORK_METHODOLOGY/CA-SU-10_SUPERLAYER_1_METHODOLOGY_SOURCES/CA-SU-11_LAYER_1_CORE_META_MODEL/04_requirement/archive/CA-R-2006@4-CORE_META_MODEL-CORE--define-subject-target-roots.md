---
subjects:
  governs: Subject
atom_id: CA-R-2006@4
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 4
updated_at: 2026-10-24 00:38:25 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
# Summary

Define Subject Target Roots

## Scope

canonical Subject paths in this model.

## Claim

A canonical Subject path **must** start at `Subject`. `Domain` and `Engineering` are the current product-topic branches. `Graph` is a global topic namespace with `Relation` and `Rule` topics that apply within and across branches.

## Details

Domain names what the project means and offers. Engineering names how it is structured, built, stored and operated. Graph names connections and their constraints. these branches do not assign a Content Role and do not replace the kinds described by the graph.

the model can expand. UX and Design are not admitted targets for this migration. a Scope Unit path is not automatically a Subject path.
