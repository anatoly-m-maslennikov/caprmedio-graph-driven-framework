---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan.Status", "Entity/Node/Continuant/Atom/Content Role: Plan"]
version: 13
updated_at: "2026-10-19 15:55:51 +0400"
relations: {"relates_to": ["CA-R-1539", "CA-D-483", "CA-R-1541"]}
atom_id: "CA-D-461"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Place Plan Carriers by Status

## Scope

Plan Carrier Bundle placement by carried Status.

## Claim

**every** Plan Carrier Bundle **must** represent its carried Status **in** its local Plan container under the following mapping:

- Draft: **in** its `draft` subdirectory.
- Active: directly **in** that local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** its `archived` subdirectory.

the local container is the matching Directory Carrier of its declared immediate decomposition target **when** that folder is used, **or** the owning Scope Unit's `03_plan`. reserved Status directories are **not** Plan nodes. validate folder nesting under CA-D-481; placement does **not** declare decomposition.

read Status from the Plan's own Markdown file under CA-D-483 **and** check its local placement; a parent **or** folder name **must not** supply a descendant's Status at read time. **every** admitted parent Status change requires the containment cascade under CA-R-1521: separate single-Atom Actions write the same requested Status to the latest Revision of **every** recursively contained descendant, subject **to** each Atom's own model. references outside the Carrier tree **and** older archived Revisions are excluded. retain descendants inside the parent Carrier tree, including **when** Archived.

## Details

- apply the Status mapping in each Plan's local container; for example, a Done parent at `03_plan/done/<parent>.md` **may** retain its Done child at `03_plan/done/<parent>/done/<child>.md`, using their canonical matching stems.
- for Archived placement, keep the same containment **and** apply CA-D-289's Version suffixes **to** Archive Carrier basenames. preserve exact older Revision bytes **without** rewriting their Version **or** Status; this rule does **not** migrate noncanonical legacy `archive/` trees.
