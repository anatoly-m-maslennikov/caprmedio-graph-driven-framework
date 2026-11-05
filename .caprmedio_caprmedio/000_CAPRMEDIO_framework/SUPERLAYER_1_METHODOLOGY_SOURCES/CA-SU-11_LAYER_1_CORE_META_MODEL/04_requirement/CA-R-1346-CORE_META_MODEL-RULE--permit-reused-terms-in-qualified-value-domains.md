---
atom_id: CA-R-1346
ref_id: CA-R-1346
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
  dependencies:
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Term//Property
tier: 2
status: Active
version: 28
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1346-CORE_META_MODEL-RULE--permit-reused-terms-in-qualified-value-domains.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Permit reused Terms **in** qualified value domains

## Claim

### Prose Claim


a reusable Term **in** allowed-value entity names across multiple qualified Property contexts.


a Term **may** occur **in** allowed-value entity names **in** multiple qualified Property contexts **when** it retains the same approved meaning **and** governing authority admits the value separately **in** **every** such context; distinct modeled entities **must** have distinct complete canonical names, **and** admission **in** one context does **not** admit the value **in** another. Within these allowed-value contexts, this permits component reuse and does not make that one Term the complete canonical entity name of another Entity.

## Details

Reusable lexical Terms and complete canonical names have distinct responsibilities. Shared `Package`, `Unit`, or `ID` components and repeated terminal labels do not collide when complete qualified expressions differ. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. `Atom/(.Header.Role: X)/(.Header.Form: X)` is a possible qualified expression: its two `X` components reuse the registered Term `X` in separately qualified value contexts, and governing authority must admit `X` in each context. The expression does not make `X` the complete canonical name of an entity outside `Term`, create an entity, or transfer value admission. Governing authority establishes the qualification and entity identity; path spelling alone does not invent them.

Repeated references to one source-admitted entity retain its complete canonical name and do not grant another value-domain admission. Component reuse does not introduce another entity or alter the approved meaning owned by its dedicated Term Definition. Complete-name uniqueness does not prohibit reusable Terms or require globally unique terminal labels.
