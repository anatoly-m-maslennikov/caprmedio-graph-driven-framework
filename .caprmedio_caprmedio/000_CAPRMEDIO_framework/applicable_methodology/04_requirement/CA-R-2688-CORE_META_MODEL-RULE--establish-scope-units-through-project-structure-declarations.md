---
atom_id: CA-R-2688
ref_id: CA-R-2688
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Scope Unit Declaration)
  - CAPRMEDIO_MODEL <+ Project
tier: 2
status: Active
version: 2
updated_at: 2026-11-04 09:19:08 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2688-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations.md
  source_atom_id: CA-R-2688
  source_atom_revision: 2
  source_sha256: f92fbee89e17dcb340bf94f890f5eab9f2778197a9edaf3b6972be90882ba8ff
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require one Scope Unit Declaration

## Claim

### Prose Claim


Each Scope Unit, including Project.


Every specific Scope Unit, including Project, has exactly one external Requirement Atom with Form `Scope Unit Declaration` and an active Subject naming that Scope Unit. The Declaration is the sole structural authority for its declared values.

The Declaration carries the Scope Unit Name, ordered state, optional Label, conditional order.number and direct containment. A non-root Scope Unit also has a stable ID. Project is unordered and has neither Scope Unit ID nor order.number. A non-root Scope Unit has one direct Parent; Project has none.

Authority and Delivery folder names are derived from the Declaration. `project_structure.toml` is not a governing source.

## Details

The Project Declaration is externally Operator-owned. The Operator is an Actor, not a Scope Unit.
