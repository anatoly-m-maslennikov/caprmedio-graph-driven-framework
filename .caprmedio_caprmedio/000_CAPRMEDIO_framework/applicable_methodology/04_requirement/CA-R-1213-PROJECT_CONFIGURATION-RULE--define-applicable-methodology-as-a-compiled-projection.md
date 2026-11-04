---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection/(.Form := Applicable Methodology)
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Reconciled Projection'
  - CAPRMEDIO_MODEL <+ Atom.Content
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
version: 40
relations: {}
atom_id: CA-R-1213
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
role: Requirement
form: Rule
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1213-PROJECT_CONFIGURATION-RULE--define-applicable-methodology-as-a-compiled-projection.md
  source_atom_id: CA-R-1213
  source_atom_revision: 40
  source_sha256: 78ce37e2a37232355b5dce990ff5ee9853e75eeb4f70295da44e34b7f3294572
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Applicable Methodology as a Compiled Projection

## Claim

### Prose Claim


Compilation of Applicable Methodology from selected Methodology Source Scope Units.


Member identifies a projected Atom member by its source identity and Version; these references identify the members without changing their content or making the Projection authoritative. Each projected member retains the exact source relation required by CA-R-1314.

the Applicable Methodology **must** be a non-authoritative Reconciled Projection compiled by direct, content-preserving derivation from current active Atom Revisions **in** selected Methodology Source Scope Units, preserving the selected source Atoms **and** their final selected Revisions unchanged. Applicable Methodology is **not** a Scope Unit **and** **must not** be the Claim Target Scope Unit of a Goal Atom.

direct **and** content-preserving describe this derivation, **not** a Carrier persistence strategy; its Reconciled Projection classification does **not** select such a strategy. trace metadata **may** be added **to** projected Carriers **only** as governed by applicable Delivery authority, **without** changing the source Atom Revision **or** its Claim authority.

Member carries zero or more string references.

