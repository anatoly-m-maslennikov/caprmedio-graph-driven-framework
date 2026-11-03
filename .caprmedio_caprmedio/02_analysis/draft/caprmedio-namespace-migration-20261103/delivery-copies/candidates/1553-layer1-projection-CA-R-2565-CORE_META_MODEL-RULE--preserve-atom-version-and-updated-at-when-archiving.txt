---
atom_id: CA-R-2565
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)/Workflow
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2565-CORE_META_MODEL-RULE--preserve-atom-version-and-updated-at-when-archiving.md
  source_atom_id: CA-R-2565
  source_atom_revision: 2
  source_sha256: 023d79334c12d4cf831c8cdd6d98fc1adbc59afeceee634fe7f1da0200768d5b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve Atom Version and Updated At When Archiving

## Claim

When a Workflow archives an Atom:

1. Keep Atom.Version unchanged.
2. Keep Atom.Updated At unchanged.
3. Do not create a new Atom Version solely for archiving.
