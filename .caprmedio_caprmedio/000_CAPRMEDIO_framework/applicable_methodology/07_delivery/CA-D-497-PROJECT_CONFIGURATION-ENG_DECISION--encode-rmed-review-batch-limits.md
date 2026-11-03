---
atom_id: CA-D-497
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Atom
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-497-PROJECT_CONFIGURATION-ENG_DECISION--encode-rmed-review-batch-limits.md
  source_atom_id: CA-D-497
  source_atom_revision: 18
  source_sha256: 5565d16e2188e6bc4833434a84ab72dd69b27043c34399c4871bfe56a5d74614
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Encode RMED review batch limits

## Claim scope

the `rmed_review` parameter group **in** Framework Instance Settings **and** Default Settings.

## Claim

RMED review batch limits **must** use these TOML parameters:

| Parameter | Encoding |
|---|---|
| `rmed_review.context_headroom_fraction` | finite TOML number strictly between zero **and** one; fraction of each worker's effective context capacity reserved rather than planned for use |
| `rmed_review.max_atoms` | optional positive integer; an explicit cap on selected Atoms, with no default **when** omitted |

resolve **every** parameter independently from explicit Operator Run input, **then** Framework Instance Settings, **then** Default Settings. report the selected value **and** source; do **not** silently coerce invalid values **or** store the same default **in** prompt text as independent authority.

## Details

effective context capacity **and** already-used context are caller-supplied runtime evidence for each worker, **not** reusable default settings. the progress list records their available source under CA-D-496; estimated usage remains labelled as an estimate. the handoff threshold is the effective capacity multiplied by `1 - context_headroom_fraction`. the former `rmed_review.target_minutes` parameter is retired; ETA is informational, **not** an admission limit. settings **must not** raise a worker's actual context capacity. an individually oversized Atom remains explicit deferred work requiring a smaller complete context slice **or** an admitted higher-capacity worker.
