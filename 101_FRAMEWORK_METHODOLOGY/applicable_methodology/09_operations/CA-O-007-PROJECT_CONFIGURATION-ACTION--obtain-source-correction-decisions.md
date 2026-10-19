---
subjects:
  governs: "Obtain Source Correction Decision"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Actor/Type: AI Agent", "Artifact", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/History/Journal", "Entity/Continuant/History/Journal.Record"]
version: 9
updated_at: "2026-10-18 16:19:57 +0400"
relations: {}
atom_id: "CA-O-007"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-007-PROJECT_CONFIGURATION-ACTION--obtain-source-correction-decisions.md
  source_atom_id: CA-O-007
  source_atom_revision: 9
  source_sha256: b96fc9fb653213f9ca8f00ac0bfb7c1507158203d02fb570952c7adc46e49c42
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
