---
version: 26
updated_at: 2026-10-29 14:12:43 +0400
relations:
  evaluation_for:
  - CA-M-294
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Term Definition'
  - Entity/Object/Continuant/Actor
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
  - Entity/Object/Continuant/Term
  - Entity/Aspect/Engineering/Authoring/Controlled English
atom_id: CA-E-472
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eval Policy
tier: 4
---
## Summary

Check simple wording without meaning loss

## Claim scope

wording evaluated under CA-M-294 against explicit authoritative Term Definitions **and** source-backed complete canonical entity names.

## Claim

wording evaluated under CA-M-294 fails **if** **any** of the following holds:

- a demonstrated simpler, more familiar alternative preserves the intended meaning, but unnecessary jargon **or** specialized wording is retained.
- a simplification removes **or** changes a necessary participant, obligation, permission, quantity, condition, boundary, **or** logical distinction.
- a simplification adds ambiguity, substitutes a synonymous full name for an entity's complete canonical entity name, changes a component Term's declared meaning, **or** substitutes a synonym for a canonical CCE Operator **or** reference.
- a simplified Summary adds **to**, broadens, narrows, **or** contradicts its source Claim **or** Claim Scope.

## Details

necessary specialized wording **must not** fail merely because it is technical. shorter wording **must not** pass merely because it uses fewer words. uncertain meaning preservation remains unevaluated, **not** passed. Read the dedicated R/Type: Term Definition for a Term before comparing a rewrite; an Entity Definition **or** agreement among Semantics sections does **not** substitute for that meaning authority. Check entity names, Claim, Claim Scope, Semantics, Details **and** other authored fields **in** that order, using actual carried fields **without** inventing optional sections. No dictionary, lookup service **or** generated Projection is required.

### Term and entity-name preservation cases

compare the same complete canonical entity name before **and** after simplification; a different full name registered for the same entity; an unregistered synonymous full name; the same complete name silently rebound to another entity; **and** a rewrite whose entity binding cannot be determined. The unchanged correct name–entity binding passes this check **when** the remaining preservation checks pass. Both synonymous full names **and** a changed target fail. An indeterminate target remains unevaluated, **not** passed. Repeated mentions of one established complete-name binding do **not** create another entity.

reuse of component Term `Package` in `Package`, `Eval Package` **and** `Runtime Package`, **and** component Term `Unit` in `Scope Unit` **and** `Code Unit`, passes **when** the complete entity names remain exact **and** the component meanings remain consistent. Such reuse is **not** a naming collision. Conflicting component meaning fails; uncertain meaning **or** segmentation remains unevaluated. A Term **may** supply one entire full name **without** being restricted to that one entity **in** other compound names. No separate Unit entity **or** synthetic Term node is inferred from the word's occurrence.

### Canonical entity naming in prose

for `Package > Module > Code Unit`, verify that the three entities retain complete canonical names `Package`, `Module` **and** `Code Unit` **in** graph expressions **and** **all** authored mentions. The name strings **must not** become additional graph nodes, **and** the chain **must not** become another entity. Replacing the same Module entity's name with `component` to vary prose fails, even outside a selector. A separately defined Component entity retains its own full name **and** **must not** be merged with Module. Apply the same check to entity names in admitted `/`, `//`, `.`, `:`, **and** `>` constructs, existing-kind references `@(...)`, **and** the exact declared Relation Type name inside `((...))`; an alternate name for the same Relation Type fails naming. The reference marker refers to an existing kind **without** declaring another target; syntax recognition alone grants no target **or** Relation admission. Operators, delimiters **and** selector syntax are **not** Terms. Under CA-R-1325, a complete composite Subject Expression is **not** one lexical Term; parsing alone **does not** establish a complete entity name **or** another entity. Explicitly source-admitted qualified property names such as `atom.id` **and** `projection.id` remain valid complete names. The three-target chain introduces no fourth entity **or** fourth complete name. Repeated references to one entity remain one binding; property, value, bearer **or** context qualification does **not** permit the same complete canonical name to identify a different entity.

### Explicit Term Definition and qualified property cases

use the explicit ID Term Definition for `id` **in** `atom.id` **and** `projection.id`; both complete property names remain distinct while the component meaning stays a unique identifier used to find an entity instance across Continuant **and** Occurrent instances. Do **not** demand `atom.atom_id` **or** `projection.projection_id`. The dot remains syntax; preserve literal code identifiers under the source boundary. Only compare identifier uniqueness within matching prefixes. `CA-P-123`, `CA-P-123@1-draft` **and** `CA-P-123@3` do **not** establish a version-identity rule **or** a case-folding rule by themselves. A contradictory ID use **in** a later authored field remains a failure even **when** earlier fields agree. Preserve source Atom, Revision **and** exact field occurrence; missing meaning authority **or** undeclared identity behavior stays unresolved, **not** passed.

Readability, meaning preservation, local well-formedness, source consistency **and** checked coverage remain separate outcomes. Exactly one active authoritative Term Definition owns each reusable Term's Project-specific meaning.

