---
subjects:
  governs: "Entity/Occurrent/Execution/Step Run"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Occurrent/Execution/Step Run.Execution Context", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/History/Journal"]
version: 4
updated_at: "2026-10-18 03:33:59 +0400"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1792"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1792-CORE_META_MODEL-GENERAL--preserve-terminal-workflow-handoff-approval-boundaries.md
  source_atom_id: CA-R-1792
  source_atom_revision: 4
  source_sha256: 062e36ce01bf1b229cf42623c8f55e19ad6841857a2b5e381f744a3b5a4f2031
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Preserve terminal Workflow handoff approval boundaries

## Scope

a terminal Workflow handoff from an Agentic Step Invocation.

## Claim

a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.

## Details
