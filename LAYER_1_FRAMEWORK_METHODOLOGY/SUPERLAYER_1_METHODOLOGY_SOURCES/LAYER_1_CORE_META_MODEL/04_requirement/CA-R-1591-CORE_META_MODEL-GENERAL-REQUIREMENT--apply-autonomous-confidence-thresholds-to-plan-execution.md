---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Autonomous Confidence Threshold", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Actor/Type: AI Agent"]
version: 7
updated_at: "2026-10-19 15:53:38 +0400"
relations: {"relates_to": ["CA-R-1587", "CA-M-271"]}
atom_id: "CA-R-1591"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Apply autonomous confidence thresholds to Plan execution

## Scope

autonomous continuation of Plan work.

## Claim

autonomous continuation of Plan work **must** satisfy its effective Autonomous Confidence Threshold:

- resolve the value under CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.
- **if** confidence **in** correct execution is below it, request Operator disposition **before** continuing.
- **otherwise**, continue **only** within existing authority; meeting the threshold does **not** grant additional authority.

## Details
