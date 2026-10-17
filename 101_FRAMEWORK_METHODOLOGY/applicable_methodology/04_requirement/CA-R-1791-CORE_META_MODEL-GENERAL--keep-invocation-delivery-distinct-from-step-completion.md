---
subjects:
  governs: "Entity/Occurrent/Execution/Step Run"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Occurrent/Execution/Step Run.Execution Context", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal"]
version: 3
updated_at: "2026-10-16 12:08:48 +0000"
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
  source_atom_revision: 3
  source_sha256: 6d558a6d4f6cc84bd823b0bee58c0a8c5411fb7be29670aa3b0d51c079e0d721
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Invocation delivery distinct from Step completion

## Scope

requests for participation **or** prompt delivery for an Agentic Step Invocation.

## Claim

requesting participation **or** returning a prompt **must not** itself complete a Step Run.

## Details
