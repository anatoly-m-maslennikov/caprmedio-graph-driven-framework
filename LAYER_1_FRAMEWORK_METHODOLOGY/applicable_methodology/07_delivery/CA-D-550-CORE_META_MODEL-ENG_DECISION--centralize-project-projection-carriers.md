---
atom_id: CA-D-550
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Directory
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Carrier
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Project.Settings
version: 20
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-550-CORE_META_MODEL-ENG_DECISION--centralize-project-projection-carriers.md
  source_atom_id: CA-D-550
  source_atom_revision: 20
  source_sha256: 269c09c682181356a6e1476473af8754b554ba3e69f62bf27df3f24f44ba40ac
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Centralize Project Projection Carriers

## Claim

### Prose Claim


persistent non-authoritative view Projection Carriers belonging to a Project.


**all** persistent view Projection Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_projection/`, **except** Applicable Methodology, whose Carrier Root **must** remain `.caprmedio_<project_name>/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`.

## Details

- Graphs **and** derived Journal views use `_projection/` **or** named subdirectories beneath it.
- Applicable Methodology uses its separate Carrier Root; its Methodology Sources retain the `000_APPLICABLE_MTHD_sources/` subdirectory.
- Authoritative Atoms, Methodology Sources, Project Settings, and Project Structure retain their own authoritative locations.
- Temporary build stages **and** intermediate reports remain ephemeral; publication places the delivered view Projection under its declared Carrier Root.
- The derivation RMED → using O → I does not relocate native Implementation into _projection: native I uses its governed Delivery place and may supply actual-state source facts. Views subsequently generated from I use _projection.
