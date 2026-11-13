---
atom_id: CA-D-633
ref_id: CA-D-633
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
tier: 5
relations:
  delivery_for:
  - CA-M-332
status: active
version: 16
updated_at: '2026-11-12T17:10:00.904758+00:00'
carrier_destination:
  file:
    name: CA-D-633-FRAMEWORK_DELIVERY-DECISION--deliver-the-complete-project-local-ca-skill-without-hooks.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Deliver the complete project-local ca Skill without hooks

## Claim scope

The canonical ca Skill payload and its project-local Codex target in direct Release Version delivery.

## Claim

### Prose Claim

Direct Release Version delivery **must** install the complete canonical `LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_SKILLS/ca/` directory at the selected Project's `.agents/skills/ca/`, including `SKILL.md`, `agents/openai.yaml`, and every declared resource, while retaining its `caprmedio` Project-MCP dependency and changing no host hooks or global configuration.

## Details

Prepare and verify the complete Skill payload with the local runtime package before clearing any installed target; install those same prepared bytes and check that the copy succeeds. A failed or uncertain copy retains its truthful source-effect result and does not permit automatic replay. The installed Skill belongs to the same local release delivery as the installed Project runtime. Release Version does not register MCP, change Codex permissions, change Codex or Git Hook carriers or hook configuration, or alter unrelated Skills or user directories. Engine runtime `--without-hooks` does not substitute for complete Skill delivery. This Delivery defines neither a candidate-snapshot carrier nor a full-suite gate or N+1 Skill-selection protocol. Plain Journal append/read records supplied actual observations without baseline, prior-history, chain, validation, receipt, deduplication, retry or recovery prerequisites; neither a log entry nor logging failure certifies or changes the observed Skill installation outcome.
