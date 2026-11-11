---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Carrier/File
  - CAPRMEDIO <+ MODEL <+ Carrier/Directory
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-460
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-460-CORE_META_MODEL-ENG_DECISION--serialize-plan-atom-carrier-bundles.md
  source_atom_id: CA-D-460
  source_atom_revision: 25
  source_sha256: 51e94173d93697e404f2812c7ad7e15cbe0fcae2b090b6eb0608c747220f38c6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Plan Atom Carrier Bundles

## Claim scope

Plan Atom Carrier Bundles.

## Claim

a Plan Atom Carrier Bundle **must** consist of **`=1`** Markdown File Carrier **and** **`<=1`** optional matching Directory Carrier using the same canonical stem under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems.

- the Markdown file carries the Plan's own Properties **and** follows CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections, including its mandatory Definition of Done.
- a matching directory organizes related Plan Carriers; it neither creates another Atom **nor** replaces the mandatory Markdown file.
- the file **and** optional directory represent the same identity, Summary, Label, **and** Status, checked under CA-D-480-CORE_META_MODEL-DELIVERY--keep-atom-addresses-consistent-with-carried-properties.
- related Plan files carry independent Atoms; they are **not** additional Carriers of the Hub's Claim.
