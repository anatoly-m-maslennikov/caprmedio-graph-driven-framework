---
atom_id: CA-R-2778
ref_id: CA-R-2778@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Draft
version: 1
updated_at: "2026-11-06 19:26:25 +0400"
carrier_destination:
  file:
    name: CA-R-2778@1-draft-RULE--declare-cfel-universal-quantification.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare CFEL universal quantification

## Claim

### Prose Claim

A `FOR EACH` construct has a typed participant selector of the form `$name[<Kind>]`, `$name[<Kind>, simple-condition]`, or `$name[<Kind>, (conditions)]`, followed by `:` and a parenthesized body. The paired `<Kind>` denotes the selected Model kind. It states that every selected instance satisfying the selector conditions satisfies each complete body expression. The header colon is a block delimiter, not the `:=` allowed-value or `::` value-constraint notation.

The Claim explicitly declares its participant and scope; its active Subject identifies the governed focus and does not implicitly bind a participant. The participant is a logical binding available in its selector conditions and matching body. Each reference to that participant denotes the same selected instance. Within that scope, `$name.property` and `name.property` both read the participant's Property; the bare form does not bind or rebind a participant. A new binding must use a name different from an already bound outer variable. The participant introduced by the `FOR EACH` construct is not in scope after its matching body. Existing IF binding rules remain applicable.

An unparenthesized selector filter is permitted only when it is one simple condition, such as `.context.role = Plan`. Multi-condition filters remain parenthesized; parenthesize mixed `AND` and `OR` conditions to make their grouping explicit. Separate complete body expressions with semicolons. The expression is declarative: it does not create or modify an instance, perform I/O, or prescribe an execution loop.

`FOR EACH` is the only keyword of this construct; its header does not use `with` or `in`.

Universal quantification constrains each matching participant without requiring that the selection contain an instance.
