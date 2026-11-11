---
atom_id: CA-D-497
ref_id: CA-D-497
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom
tier: 3
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-497-PROJECT_CONFIGURATION-DECISION--encode-rmed-review-batch-limits.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-497-PROJECT_CONFIGURATION-ENG_DECISION--encode-rmed-review-batch-limits.md
  source_atom_id: CA-D-497
  source_atom_revision: 18
  source_sha256: fbe8c017e6db7f41efda47520c83902e14da7d1f8f59a6e7143425b55432adb9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Encode RMED review batch limits

## Claim

### Prose Claim


the `rmed_review` parameter group **in** Framework Instance Settings **and** Default Settings.


RMED review batch limits **must** use these TOML parameters:

| Parameter | Encoding |
|---|---|
| `rmed_review.context_headroom_fraction` | finite TOML number strictly between zero **and** one; fraction of each worker's effective context capacity reserved rather than planned for use |
| `rmed_review.max_atoms` | optional positive integer; an explicit cap on selected Atoms, with no default **when** omitted |

resolve **every** parameter independently from explicit Operator Run input, **then** Framework Instance Settings, **then** Default Settings. report the selected value **and** source; do **not** silently coerce invalid values **or** store the same default **in** prompt text as independent authority.

## Details

effective context capacity **and** already-used context are caller-supplied runtime evidence for each worker, **not** reusable default settings. the progress list records their available source under CA-D-496; estimated usage remains labelled as an estimate. the handoff threshold is the effective capacity multiplied by `1 - context_headroom_fraction`. the former `rmed_review.target_minutes` parameter is retired; ETA is informational, **not** an admission limit. settings **must not** raise a worker's actual context capacity. an individually oversized Atom remains explicit deferred work requiring a smaller complete context slice **or** an admitted higher-capacity worker.
