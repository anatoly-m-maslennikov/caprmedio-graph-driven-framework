---
atom_id: CA-D-534@4
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 23:34:06 +0400
subjects:
  governs: Subject/Engineering/Project Structure/Authority and Cutover Carriers
  depends_on:
  - Subject/Engineering/Project Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Engineering/Carrier
  - Subject/Engineering/Carrier/Journal Serialization
relations:
  relates_to:
  - CA-R-1830
  - CA-R-1831
---
# Summary

Bind PROJECT_STRUCTURE authority and cutover carriers

## Scope

Carrier placement and mutation boundaries for the reviewed structural Tool.

## Claim

Delivery **must** bind project structure declarations to the authoritative TOML and treat declared authority/delivery paths and filesystem observations as separate carriers.

## Details

- Only the selected TOML declaration delta and explicitly authorized reference/Carrier repairs are writable at cutover; implementation paths are reported as declared `delivery_path` values, not created or inferred by this Atom.
- The shared Events Journal remains the sole Run evidence source. This Delivery Atom carries references to its receipts, not a duplicate Journal format.
- A partial outcome records actual carrier changes and its authorized recovery boundary; it does not authorize broad deletion or unreported repair.
