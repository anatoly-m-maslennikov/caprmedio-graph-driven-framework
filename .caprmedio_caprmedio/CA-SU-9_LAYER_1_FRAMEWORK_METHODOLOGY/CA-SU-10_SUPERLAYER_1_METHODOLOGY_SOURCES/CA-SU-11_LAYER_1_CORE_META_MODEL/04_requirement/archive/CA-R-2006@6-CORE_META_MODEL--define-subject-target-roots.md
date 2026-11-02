---
subjects:
  governs: Subject
atom_id: CA-R-2006@6
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 6
updated_at: 2026-10-24 14:40:49 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
# Summary

Define Subject Target Roots

## Scope

canonical Subject paths in this model.

## Claim

A canonical Subject path **must** start at `Subject`. `Product`, `Domain`,
`Engineering`, `UX`, `Design` and `Documentation` are current topic branches.
`Graph` is the shared topic namespace for Relations and Rules within and
across branches. The set of topic branches is expandable.

## Details

Product names what the project produces. Domain names the concepts and things
the product works with. Engineering names how it is built, stored and operated.
UX, Design and Documentation name their respective topics. Graph names
connections and their constraints.

Subject branch, Content Role and Local Scope Unit are independent. A Requirement
about a product can live at Project scope without making Project its Subject.
A topic need not be an independently carried object. A Scope Unit path is not
automatically a Subject path.
