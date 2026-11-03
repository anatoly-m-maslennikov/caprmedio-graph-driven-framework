---
version: 30
updated_at: 2026-11-02 18:35:20 +0400
relations:
  evaluation_for:
  - CA-M-294
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Eval Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Runtime Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package <+ Module
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package <+ Module <+ Code Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Header.Role: Method)/(.Header.Form: Term Definition)'
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
atom_id: CA-E-472
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Policy
---
## Summary

Check simple wording without meaning loss

## Claim

### Prose Claim


wording evaluated under CA-M-294 against explicit authoritative Term Definitions **and** source-backed complete canonical entity names.


wording evaluated under CA-M-294 fails **if** **any** of the following holds:

- a demonstrated simpler, more familiar alternative preserves the intended meaning, but unnecessary jargon **or** specialized wording is retained.
- a simplification removes **or** changes a necessary participant, obligation, permission, quantity, condition, boundary, **or** logical distinction.
- a simplification adds ambiguity, substitutes a synonymous full name for an entity's complete canonical entity name, changes a component Term's declared meaning, **or** substitutes a synonym for a canonical CCE Operator **or** reference.
- a simplified Summary adds **to**, broadens, narrows, **or** contradicts its source Claim including its applicability in Prose Claim.

## Details

necessary specialized wording **must not** fail merely because it is technical. shorter wording **must not** pass merely because it uses fewer words. uncertain meaning preservation remains unevaluated, **not** passed. Read the dedicated Method Atom of Type Term Definition for a Term before comparing a rewrite; an Entity Definition **or** agreement among Semantics sections does **not** substitute for that meaning authority. Check entity names, Claim including applicability in Prose Claim, Semantics, Details **and** other authored fields **in** that order, using actual carried fields **without** inventing optional sections. No dictionary, lookup service **or** generated Projection is required.

### Term and entity-name preservation cases

compare the same complete canonical entity name before **and** after simplification; a different full name registered for the same entity; an unregistered synonymous full name; the same complete name silently rebound to another entity; **and** a rewrite whose entity binding cannot be determined. The unchanged correct name–entity binding passes this check **when** the remaining preservation checks pass. Both synonymous full names **and** a changed target fail. An indeterminate target remains unevaluated, **not** passed. Repeated mentions of one established complete-name binding do **not** create another entity.

reuse of component Term `Package` in `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package/Eval Package` **and** `Entity/Object/Continuant/Package/Runtime Package`, **and** component Term `Unit` in `Entity/Object/Continuant/Structural Unit/Scope Unit` **and** `Entity/Object/Continuant/Package <+ Module <+ Code Unit`, passes **when** the complete Entity expressions remain exact **and** the component meanings remain consistent. Such reuse is **not** a naming collision. Conflicting component meaning fails; uncertain meaning **or** segmentation remains unevaluated. Outside the Term branch, only the Subject root `Entity` may be expressed by one Term alone. A reusable component does not become another Entity or its complete expression merely by occurring in a name.

### Canonical entity naming in prose

for `Entity/Object/Continuant/Package <+ Module <+ Code Unit`, verify that the three entities retain their complete canonical expressions `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package <+ Module` **and** `Entity/Object/Continuant/Package <+ Module <+ Code Unit` **in** graph Subjects **and** **all** authored mentions. The name strings **must not** become additional graph nodes, **and** the chain **must not** become another entity. Replacing the same Module entity's name with `component` to vary prose fails, even outside a selector. A separately defined Component entity retains its own full name **and** **must not** be merged with Module. Apply the same check to entity names in admitted `/`, `//`, `.`, `:`, `+>`, `<+`, `>|` **and** `|<` constructs, qualified references to already declared Entities, **and** registered direct Relation tokens inside `((...))`. Check a token's registry resolution separately from the Relation Type entity's full canonical expression; its bare token is not that complete expression. An alternate token asserted to name the same Relation Type fails naming. A qualified reference refers to an already declared Entity **without** declaring another target; syntax recognition alone grants no target **or** Relation admission. Operators, delimiters **and** selector syntax are **not** Terms. Under CA-R-1325, a complete composite Subject Expression is **not** one lexical Term; parsing alone **does not** establish a complete entity name **or** another entity. The contextual topic/code spellings `atom.id` **and** `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names. Authored Subjects use their full admitted expressions. The three-target chain introduces no fourth entity **or** fourth complete name. Repeated references to one entity remain one binding; property, value, bearer **or** context qualification does **not** permit the same complete canonical name to identify a different entity.

### Explicit Term Definition and qualified property cases

use the explicit ID Term Definition for the ID Properties distinguished by the contextual topic/code spellings `atom.id` **and** `projection.id`; the respective Properties remain distinct while the meaning stays a unique identifier used to find an entity instance across Continuant **and** Occurrent instances. Do **not** demand `atom.atom_id` **or** `projection.projection_id`. The dot remains syntax; preserve literal code identifiers under the source boundary. Only compare identifier uniqueness within matching prefixes. `CA-P-123`, `CA-P-123@1-draft` **and** `CA-P-123@3` do **not** establish a version-identity rule **or** a case-folding rule by themselves. A contradictory ID use **in** a later authored field remains a failure even **when** earlier fields agree. Preserve source Atom, Revision **and** exact field occurrence; missing meaning authority **or** undeclared identity behavior stays unresolved, **not** passed.

Readability, meaning preservation, local well-formedness, source consistency **and** checked coverage remain separate outcomes. Exactly one active authoritative Term Definition owns each reusable Term's Project-specific meaning.

