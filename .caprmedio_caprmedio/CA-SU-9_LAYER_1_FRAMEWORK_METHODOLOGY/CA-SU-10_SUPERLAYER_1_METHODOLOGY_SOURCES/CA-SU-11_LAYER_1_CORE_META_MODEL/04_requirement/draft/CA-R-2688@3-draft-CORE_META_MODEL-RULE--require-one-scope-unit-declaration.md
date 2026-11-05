---
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Scope Unit Declaration)
  - CAPRMEDIO_MODEL <+ Project
version: 3
updated_at: 2026-11-05 12:58:42 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-2688
status: Draft
tier: 2
form: Rule
role: Requirement
carrier_destination:
  file:
    name: CA-R-2688@3-draft-CORE_META_MODEL-RULE--require-one-scope-unit-declaration.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Require one Scope Unit Declaration

## Claim

### Prose Claim


Each Scope Unit, including Project.


Every specific Scope Unit, including Project, except the predefined Scope Unit `world`, has exactly one external Requirement Atom with Form `Scope Unit Declaration` and an active Subject naming that Scope Unit. The Declaration is the sole structural authority for its declared values. `world` has ID `CA-SU--1` and has no Scope Unit Declaration.

The Declaration carries the Scope Unit Name, stable ID, ordered state, optional Label, conditional order.number and direct containment. Project has a stable ID, is unordered and has no order.number. Each non-root Scope Unit other than `world` has one direct Parent; Project has none.

Authority and Delivery folder names are derived from the Declaration. `project_structure.toml` is not a governing source.

## Details

The Project Declaration is externally Operator-owned. The Operator is an Actor, not a Scope Unit.
