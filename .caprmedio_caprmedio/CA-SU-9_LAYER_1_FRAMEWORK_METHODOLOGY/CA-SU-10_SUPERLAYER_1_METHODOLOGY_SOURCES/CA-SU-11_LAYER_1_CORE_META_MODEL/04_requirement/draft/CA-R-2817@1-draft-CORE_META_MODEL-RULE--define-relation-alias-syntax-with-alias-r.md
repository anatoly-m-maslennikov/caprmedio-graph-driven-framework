---
atom_id: CA-R-2817
ref_id: CA-R-2817@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
version: 1
updated_at: 2026-11-05 14:25:52 +0400
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2817@1-draft-RULE--define-relation-alias-syntax-with-alias-r.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Define Relation alias syntax with `alias($r)`

## Claim

### Prose Claim

`alias(Relation//NAME) == "notation token"` binds one nonempty lexical notation token to a canonical Relation model name or its inverse alias model name. Resolve the name exactly; do not infer case folding or undeclared synonyms. Each written name has at most one authored short notation token. Reject unknown names, conflicting alias values and ambiguous token bindings. Without a short token, use the full named Relation notation.

A token follows its written name's directional reading. This notation is metadata, not a graph Relation fact; it grants no endpoint permission or cardinality and creates no second Relation fact or Alias entity. Fixed names are written `Relation//NAME`; `((NAME))` invokes the corresponding Relation writing between endpoints.
