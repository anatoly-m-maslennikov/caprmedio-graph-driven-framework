---
subjects:
  governs: "Entity/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Continuant/Object/Atom.Author", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Actor/Type: AI Agent", "AI Agent Confidence", "Entity/Continuant/Object/Atom/Content Role: Plan.Autonomous Confidence Threshold", "Spec", "Entity/Continuant/Object/Atom", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Project", "Implementation Workflow"]
version: 7
updated_at: "2026-10-15 18:44:23 +0000"
relations: {"child_of":["CA-M-261"],"relates_to":["CA-R-1591","CA-R-1552","CA-R-1080","CA-M-262"]}
atom_id: "CA-R-1559"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1559-CORE_META_MODEL-GENERAL-REQUIREMENT--gate-governing-atom-changes-during-implementation.md
  source_atom_id: CA-R-1559
  source_atom_revision: 7
  source_sha256: 9e971e9c736d9697cceac5df15dc0dcc6550565fe68e4c18814551c87bf83380
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Gate governing Atom changes during implementation

## Scope

changes to governing RMED Atoms during implementation.

## Claim

authorization **to** change a governing RMED Atom during implementation **must** satisfy the following Actor policy:

- resolve the Atom's effective Author **before** the proposed change, its governing permissions, the effective Plan Autonomous Confidence Threshold under CA-R-1591, **and** **all** additional Operator rules.
- obtain Operator approval **before** changing an Operator-authored Atom.
- request Operator disposition **before** changing an AI-authored Atom **when** confidence is below the threshold **or** an additional rule requires approval.
- an AI-authored Atom **may** change autonomously **only** **when** confidence is at **or** above the threshold **and** **all** applicable permissions **and** Operator rules allow it.
- a prohibition remains a prohibition; authorship **or** confidence **must not** create permission.
- a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080.
- an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.

## Details
