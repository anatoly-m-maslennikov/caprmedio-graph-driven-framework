---
atom_id: CA-R-2132
ref_id: CA-R-2132
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
tier: 1
status: Active
version: 13
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-2132-CORE_META_MODEL-RULE--assign-project-goal-tier-minus-one.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2132-CORE_META_MODEL-RULE--assign-project-goal-tier-minus-one.md
  source_atom_id: CA-R-2132
  source_atom_revision: 13
  source_sha256: 6164a776d1f2d5872b2f2157a1098abf712c1b50c5b0108c8f0e975463823752
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Assign Project Goal Tier Minus One

## Claim

### Prose Claim


Atoms of Form Goal whose active Subject resolves to the Project Scope Unit root.


Every Atom of Form Goal whose active Subject resolves to the Project Scope Unit root **must** carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an additional Type-to-Tier restriction.

## Details

Under CA-R-2149, the Project resolved from the active Subject is the ordering context.
