---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal <+ Event Record
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-359
atom_id: CA-D-360
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-360-CORE_META_MODEL-ENG_DECISION--bind-framework-settings-revisions-to-journal-receipts.md
  source_atom_id: CA-D-360
  source_atom_revision: 27
  source_sha256: f54f12b4b3464ed0572c9976f7d88c1877998cdc5ba2df511e6ded84e4105238
  original_relations_sha256: c8bb85fb8ef619e2f610eea8ab82f269c447e9ea5167b4426122d66f74bb9054
---
## Summary

Bind Framework Settings Revisions to Journal Receipts

## Claim

### Prose Claim


the current `caprmedio_framework_settings` Revision and SHA-256 Digest.


the current caprmedio_framework_settings Revision **and** SHA-256 Digest **must** bind **to** its authoritative TOML Carrier through a canonical completed governed-change Work Journal receipt **or** an explicitly authorized canonical recovered-state Work Journal receipt registering its observed baseline; the receipt **must** match the selected Project, exact Carrier path, logical Artifact Revision, **and** Digest. absence, ambiguity, **or** mismatch **must** leave its currentness unknown.

## Details

- recovered baseline registration **must** use the existing `recovered` event for `governed_project_state`, with the exact positive-integer logical Revision in `result.version` **and** Carrier evidence in `recovery_evidence.carrier`: `path`, `sha256`, `observed_at`, **and** `observer_run_id`. no new Journal event **or** schema is required.
- `observed_at` **must** record the actual observation time; `observer_run_id` **must** identify a real observing Run **or** session supported by evidence. unresolved past Actor, mutation time, intent, **or** history **must** remain explicit uncertainty under CA-R-1644.
- the logical Revision **must** follow the existing Artifact lineage, including Carrier renames **or** movements; a changed path **must not** reset it **or** justify a guessed allocation.
- registration **must not** write the Settings Carrier, fabricate a past Settings change **or** author, **or** rewrite Journal history under CA-D-308. a Carrier changed since observation **must not** be presented as the registered current baseline; its historical observation remains intact.
- baseline registration establishes the observed binding only. under CA-R-1491 it proves neither Settings schema conformance nor correct performance **or** authorization of another operation.
