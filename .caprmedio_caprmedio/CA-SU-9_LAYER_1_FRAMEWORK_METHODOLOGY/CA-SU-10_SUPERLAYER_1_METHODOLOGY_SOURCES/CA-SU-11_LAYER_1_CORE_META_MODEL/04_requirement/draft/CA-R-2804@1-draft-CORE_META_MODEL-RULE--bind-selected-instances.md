---
atom_id: CA-R-2804
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 1
updated_at: 2026-11-05 14:25:52 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2804@1-draft-CORE_META_MODEL-RULE--bind-selected-instances.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Bind selected instances

## Claim

### Prose Claim

`<Kind>` references a declared Model kind. `$x[<Kind>, (conditions)]` binds an existing instance as a named participant, with grouped conditions evaluated against that participant. `$<Kind>` selects anonymously. Repeated anonymous selections use the same domain but do not assert their referents identical or different; use a named participant to express the same selected identity. Selection creates no instance and does not turn a model entity into a data-layer fact. `$container[<Workflow Run> OR <Step Run>]` binds one participant over the union of the specified instance domains. A Relation bound such as `{::1}` applies once over that whole union, not separately to each kind. `$<Journal>{::1}` and `$journal[<Journal>]{::1}` each constrain the selected logical Journal instance population within the Current Project to exactly one. A variable introduced by a standalone typed instance selector remains in scope for following statements in the same CFEL fenced block. A variable introduced in an IF condition is in scope within that condition and its matching THEN group only; it is not in scope in following statements. A new IF binding uses a different name from an already bound outer variable; references to that outer variable retain its identity.
