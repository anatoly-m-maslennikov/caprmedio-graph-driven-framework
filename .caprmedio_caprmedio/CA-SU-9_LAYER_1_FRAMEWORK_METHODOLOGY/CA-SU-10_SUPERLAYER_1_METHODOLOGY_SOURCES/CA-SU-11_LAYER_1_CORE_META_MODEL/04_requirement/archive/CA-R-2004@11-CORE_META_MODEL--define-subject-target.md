---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity
atom_id: CA-R-2004@11
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 11
updated_at: 2026-10-29 10:28:51 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
## Summary

Define Subject Target

## Claim scope

a direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.

## Claim

a Subject Target **means** the topic addressed by a canonical Subject expression. its full path starts at Entity and retains its declared qualification and operators. a Subject can identify a kind, a classification axis, a dependent property, an allowed value or a named instance; it need not identify an independently carried object.

## Details

Subject says what an Atom concerns. Content Role says what its content does. They are independent by definition. An Atom of any RMED Role can govern a topic in any declared Subject branch. A topic about how work is performed does not require a separate Method root.

Entity is the canonical expression root. Its four sibling branches are Object, Aspect, Graph Syntax and Carrier under CA-R-1248. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.

Within the shared Atom branch, `Atom/Content Role` names the classification axis. `Atom/Content Role: Requirement` names a narrower Atom kind that inherits Atom properties. Naming the axis does not create a Content Role entity or assign a role value to an Atom instance.
