---
atom_id: CA-D-497@10
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Default Settings
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Atom
relations: {}
tier: 3
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
