---
subjects:
  governs: Entity
  depends_on:
  - Entity
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Term
version: 29
updated_at: 2026-10-29 10:28:51 +0400
relations: {}
atom_id: CA-R-1194@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Subject Path

## Claim scope

A canonical Subject path identifying a governed or dependency target.

## Claim

A Subject Path is a full canonical expression identifying one thing or topic addressed by GOVERNS or DEPENDS_ON. Entity is the canonical expression root. Its four sibling branches are Object, Aspect, Graph Syntax and Carrier under CA-R-1248. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The target is selected by the meaning addressed, not by the Atom's Local Scope Unit, Content Role, folder or Carrier. The path names a target; it is not itself the Subject Relation. A defining Atom may introduce that target, so format checks do not require prior target existence.

## Semantics

A path may address a classification axis without declaring an entity kind. Atom/Content Role addresses the parameter, while Atom/Content Role: Plan addresses a narrower Atom kind inheriting Atom properties. The root and operators follow the adopted Entity syntax under CA-R-1931; no Project-name namespace layer is introduced.
