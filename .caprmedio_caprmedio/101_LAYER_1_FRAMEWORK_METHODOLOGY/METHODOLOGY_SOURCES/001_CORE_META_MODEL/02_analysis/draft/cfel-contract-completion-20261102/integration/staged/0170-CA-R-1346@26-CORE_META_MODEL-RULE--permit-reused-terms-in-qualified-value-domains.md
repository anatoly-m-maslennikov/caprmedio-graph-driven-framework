---
subjects:
  active: CFEL <+ Relation//IS_ALLOWED_VALUE_OF
  passive:
  - Term
  - Term//Property
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1346@26
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 2
role: Requirement
form: Rule
---
## Summary

Permit reused Terms **in** qualified value domains

## Claim scope

a reusable Term **in** allowed-value entity names across multiple qualified Property contexts.

## Claim

a Term **may** occur **in** allowed-value entity names **in** multiple qualified Property contexts **when** it retains the same approved meaning **and** governing authority admits the value separately **in** **every** such context; distinct modeled entities **must** have distinct complete canonical names, **and** admission **in** one context does **not** admit the value **in** another. Within these allowed-value contexts, this permits component reuse and does not make that one Term the complete canonical entity name of another Entity.

## Details

Reusable lexical Terms and complete canonical names have distinct responsibilities. Shared `Package`, `Unit`, or `ID` components and repeated terminal labels do not collide when complete qualified expressions differ. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. `Atom/(.Content Role: X)/(.Type: X)` is a possible qualified expression: its two `X` components reuse the registered Term `X` in separately qualified value contexts, and governing authority must admit `X` in each context. The expression does not make `X` the complete canonical name of an entity outside `Term`, create an entity, or transfer value admission. Governing authority establishes the qualification and entity identity; path spelling alone does not invent them.

Repeated references to one source-admitted entity retain its complete canonical name and do not grant another value-domain admission. Component reuse does not introduce another entity or alter the approved meaning owned by its dedicated Term Definition. Complete-name uniqueness does not prohibit reusable Terms or require globally unique terminal labels.
