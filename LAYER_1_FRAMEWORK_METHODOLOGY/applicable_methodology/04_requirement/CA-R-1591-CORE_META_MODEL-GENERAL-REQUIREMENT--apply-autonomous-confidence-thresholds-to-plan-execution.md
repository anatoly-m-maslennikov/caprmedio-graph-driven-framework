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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1591-CORE_META_MODEL-GENERAL-REQUIREMENT--apply-autonomous-confidence-thresholds-to-plan-execution.md
  source_atom_id: CA-R-1591
  source_atom_revision: 7
  source_sha256: 88f779392b31eb43206ce36ec7b1ddfbaa9be47a836f74a5247ae39d343e9456
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
