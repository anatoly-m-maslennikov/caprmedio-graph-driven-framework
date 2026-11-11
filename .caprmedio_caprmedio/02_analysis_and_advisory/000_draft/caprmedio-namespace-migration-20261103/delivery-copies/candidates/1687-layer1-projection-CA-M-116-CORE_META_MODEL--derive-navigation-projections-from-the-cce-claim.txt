---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-M-116
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-116-CORE_META_MODEL--derive-navigation-projections-from-the-cce-claim.md
  source_atom_id: CA-M-116
  source_atom_revision: 31
  source_sha256: 974eacf52fff301159835f6e3c52755e69dea5650aa450d2157acfc1ed856a99
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive navigation Projections from the CCE Claim

## Claim scope

navigation values derived from an Atom Claim.

## Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity rather than regenerating it as an independent Projection.
