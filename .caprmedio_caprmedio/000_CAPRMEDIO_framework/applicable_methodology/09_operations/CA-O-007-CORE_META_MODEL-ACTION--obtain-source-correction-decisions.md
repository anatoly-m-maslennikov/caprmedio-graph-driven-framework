---
subjects:
  governs: "Obtain Source Correction Decision"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Actor/Type: AI Agent", "Artifact", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/History/Journal", "Entity/Continuant/History/Journal.Record"]
version: 8
updated_at: "2026-10-15 18:52:41 +0000"
relations: {}
atom_id: "CA-O-007"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-007-CORE_META_MODEL-ACTION--obtain-source-correction-decisions.md
  source_atom_id: CA-O-007
  source_atom_revision: 8
  source_sha256: d8521f7fb8af02fd3dd4e07cf2aa53bf2dae10a067b1aab3cc01ec170a44a09d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Obtain source correction decisions

## Operation

Obtain Source Correction Decision **means** the reusable Action that obtains the Operator's explicit decision about an exact conflict-resolution proposal.

1. present the proposal, the conflict it addresses, **and** the selected source frontier **to** the Operator.
2. request an explicit decision. distinguish approval, rejection, requested revision, **and** absence of a decision; confidence, inferred intent, **or** an LLM judgment is **not** approval.
3. record the actual decision **in** the Journal with its proposal, conflict, exact source-frontier binding, **and** provenance. record a missing decision as missing, **not** as an approval **or** rejection.
4. return the recorded decision for the applicable authorization checks. a changed proposal **or** source frontier requires the decision's applicability **to** be checked again **before** reliance.

this Action **must not** apply the correction, record approval the Operator did **not** give, **or** create a duplicate approval Atom **in** Project Configuration. the Journal records the decision; it does **not** independently redefine the governing source Claims.

## Details
