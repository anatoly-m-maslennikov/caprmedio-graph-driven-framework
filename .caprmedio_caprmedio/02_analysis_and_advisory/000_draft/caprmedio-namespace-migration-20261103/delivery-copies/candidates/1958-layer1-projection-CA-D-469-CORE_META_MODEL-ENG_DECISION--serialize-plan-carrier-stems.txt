---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Filename
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ MODEL <+ Atom.ID
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-469
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-469-CORE_META_MODEL-ENG_DECISION--serialize-plan-carrier-stems.md
  source_atom_id: CA-D-469
  source_atom_revision: 24
  source_sha256: 1482b7f93f04dec40751ae8092da9d696393db89bf305025fd7c3484eff92d1a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Plan Carrier stems

## Claim scope

identified Plan Carrier stems.

## Claim

**every** identified Plan Carrier stem **must** use `[<WORK_SEQUENCE_NUMBER>-]<ATOM_ID>[-<LABEL>]--<SUMMARY_SLUG>`, with `.md` **only** on its File Carrier.

- the optional Label is a navigation token, **not** an Atom Type token; normalize it under CA-D-284.
- render the Summary under CA-D-282.
- **by default**, direct Plans decomposing the same Hub use unique leading Work Sequence Numbers **before** their Atom IDs, under CA-D-381 **and** CA-R-997.
- a same-bundle Directory Carrier **and** File Carrier use the same stem; number **or** Label changes preserve Atom identity **and** do **not** declare `BLOCKS`.
