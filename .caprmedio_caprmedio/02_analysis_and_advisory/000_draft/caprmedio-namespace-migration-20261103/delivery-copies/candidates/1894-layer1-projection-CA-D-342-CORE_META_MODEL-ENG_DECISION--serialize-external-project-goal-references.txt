---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier/File.Filename
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-342
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-342-CORE_META_MODEL-ENG_DECISION--serialize-external-project-goal-references.md
  source_atom_id: CA-D-342
  source_atom_revision: 28
  source_sha256: aa794d102a8cb8d3ecdcf1f61e35bad4f64d243af66fe33c835ae7b421316b59
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize External Project Goal References

## Claim scope

references to Current and historical external Project Goal Atoms.

## Claim

**every** Reference **to** a Current external Project Goal Atom **must** use its canonical Current Atom ID, not its current Carrier filename stem.

A Reference **to** an Archived external Project Goal Atom **must** use its canonical Atom ID qualified once with its unchanged numeric Version when historical identity is required. A Current Project Goal reference **must not** omit the canonical ID or fall back to a filename stem; this Delivery creates no ID-less Current exception.
