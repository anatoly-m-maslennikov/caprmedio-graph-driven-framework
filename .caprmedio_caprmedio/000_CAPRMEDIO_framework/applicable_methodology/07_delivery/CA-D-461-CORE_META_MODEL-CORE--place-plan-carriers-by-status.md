---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan.Status", "Entity/Node/Continuant/Atom/Content Role: Plan"]
version: 15
updated_at: "2026-10-20 17:33:41 +0400"
relations: {"relates_to": ["CA-R-1539", "CA-D-483", "CA-R-1541"]}
atom_id: "CA-D-461"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-461-CORE_META_MODEL-CORE--place-plan-carriers-by-status.md
  source_atom_id: CA-D-461
  source_atom_revision: 15
  source_sha256: 8b9a6e140b9b7913cf9c055eba4abc4229108d611c30abbf93c07b97ad5f21a0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Plan Carriers by Status

## Scope

Plan Carrier Bundle placement by carried Status.

## Claim

**every** Plan Carrier Bundle **must** represent its carried Status **in** the following locations:

- Draft: **in** the owning Scope Unit's shared `03_plan/draft` area.
- Active: directly **in** its local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** the owning Scope Unit's shared `03_plan/archived` area.

For a contained Current Plan, the local container for its current-Status placement is the matching Directory Carrier of its declared immediate decomposition target. Draft and Archived areas are shared across the owning Scope Unit, rather than replicated under each Plan container. This rule does **not** decide terminal-Status placement for a Plan without an incoming decomposition Relation. reserved Status directories are **not** Plan nodes. validate folder nesting under CA-D-481; placement does **not** declare decomposition.

read Status from the Plan's own Markdown file under CA-D-483 **and** check its local placement; a parent **or** folder name **must not** supply a descendant's Status at read time. **every** admitted parent Status change requires the containment cascade under CA-R-1521: separate single-Atom Actions write the same requested Status to the latest Revision of **every** recursively contained descendant, subject **to** each Atom's own model. references outside the Carrier tree **and** older archived Revisions are excluded. retain Current descendants inside the parent Carrier tree. Archived Plan Markdown Carriers are placed flat in the owning Scope Unit's shared `03_plan/archived` area, not inside an archived parent's directory.

## Details

- for a contained Plan, apply its current-Status placement relative to its immediate containing Plan's Directory Carrier; for example, a Done child is in `<parent-directory>/done/<child>.md`, using its canonical matching stem. This does **not** specify the parent's own root-level terminal-Status location.
- Place each Archived Plan Markdown Carrier directly in the owning Scope Unit's shared `03_plan/archived` area, without a parent/child Plan directory hierarchy. Apply CA-D-289's Version suffixes **to** Archive Carrier basenames. Preserve exact older version bytes **without** rewriting their Version **or** Status; this rule does **not** migrate existing carriers.
