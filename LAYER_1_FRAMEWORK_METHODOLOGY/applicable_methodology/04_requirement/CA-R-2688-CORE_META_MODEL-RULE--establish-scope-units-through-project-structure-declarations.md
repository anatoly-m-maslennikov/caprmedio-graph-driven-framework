---
subjects:
  active: Scope Unit
  passive:
  - Atom/(.Role := Requirement)/(.Form := Scope Unit Declaration)
  - Project
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
atom_id: CA-R-2688
status: Active
tier: 2
form: Rule
role: Requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2688-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations.md
  source_atom_id: CA-R-2688
  source_atom_revision: 1
  source_sha256: 29265232fef257d51cb7465bdf92a476df61bf8897187495108db7e900799eec
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require one Scope Unit Declaration

## Claim scope

Each Scope Unit, including Project.

## Claim

Every specific Scope Unit, including Project, has exactly one external Requirement Atom with Form `Scope Unit Declaration` and an active Subject naming that Scope Unit. The Declaration is the sole structural authority for its declared values.

The Declaration carries the Scope Unit Name, ordered state, optional Label, conditional order.number and direct containment. A non-root Scope Unit also has a stable ID. Project is unordered and has neither Scope Unit ID nor order.number. A non-root Scope Unit has one direct Parent; Project has none.

Authority and Delivery folder names are derived from the Declaration. `project_structure.toml` is not a governing source.

## Details

The Project Declaration is externally Operator-owned, like the Project Goal. The Operator is an Actor, not a Scope Unit.
