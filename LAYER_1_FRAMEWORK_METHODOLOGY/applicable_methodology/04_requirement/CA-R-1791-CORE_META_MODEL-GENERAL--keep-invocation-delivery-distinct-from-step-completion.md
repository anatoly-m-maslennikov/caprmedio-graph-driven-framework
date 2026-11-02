---
subjects:
  governs: "Entity/Node/Occurrent/Execution/Step Run"
  depends_on:
    ["Entity/Node/Occurrent/Execution/Step Run", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Node/Occurrent/Execution/Step Run.Execution Context", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/History/Journal"]
version: 5
updated_at: "2026-10-19 15:54:06 +0400"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1791"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1791-CORE_META_MODEL-GENERAL--keep-invocation-delivery-distinct-from-step-completion.md
  source_atom_id: CA-R-1791
  source_atom_revision: 5
  source_sha256: b05e3da36f71dd6a0ee521b21547794021bebf9c84df22c3c4656c8f1241c077
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Invocation delivery distinct from Step completion

## Scope

requests for participation **or** prompt delivery for an Agentic Step Invocation.

## Claim

requesting participation **or** returning a prompt **must not** itself complete a Step Run.

## Details
