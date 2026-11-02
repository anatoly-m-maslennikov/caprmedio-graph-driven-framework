---
subjects:
  governs: Structural Entity Direct Containment
  depends_on:
  - Containment Relation Pair
  - Directory Carrier Nesting
version: 17
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-D-264@17
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Derive Direct Containment from the Nearest Directory Carrier

## Scope

Artifact Revisions whose canonical Carriers are nested below Directory Carriers.

## Claim

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive **`=1`** direct `IS_CONTAINED_BY` connection to the Structural Entity Revision carried by its nearest ancestor Directory Carrier **and** the reverse `CONTAINS` view from that connection.

## Details

For this Carrier-derived view, canonical nesting supplies the fact; the view does not create a second authored relation declaration. IS_CONTAINED_BY is the child-to-parent direction, and CONTAINS is its derived inverse. Reading or refreshing the inverse view does not edit the containing entity's carrier; when that entity is an Atom, it does not create a new Version for it. Physical nesting does not silently replace the logical parent declared by Project Structure under CA-R-1660. Existing Revision/Structural Entity wording is retained for the separate content migration.
