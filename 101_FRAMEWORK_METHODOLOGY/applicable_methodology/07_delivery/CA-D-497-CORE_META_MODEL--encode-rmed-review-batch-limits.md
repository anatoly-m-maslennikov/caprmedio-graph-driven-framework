---
atom_id: CA-D-497
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-15 18:52:25 +0000"
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings"
  depends_on:
    ["Entity/Occurrent/Execution/Workflow Run", "Default Settings", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Atom"]
relations: {}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-497-CORE_META_MODEL--encode-rmed-review-batch-limits.md
  source_atom_id: CA-D-497
  source_atom_revision: 5
  source_sha256: 760a779935c411dfa8d3deb6a57dc31d69fe910b033aecb1181fe9560ed7ef18
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Encode RMED review batch limits

## Scope

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
