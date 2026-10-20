---
atom_id: CA-C-537
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-R-1676, CA-P-2401]
version: 1
updated_at: "2026-10-20T13:21:50.935Z"
---
# Summary

Support Current RMED extension-status relations

## Concern

R1676v21 changes RMED relation eligibility from Active to Current. Core RMED domains currently contain only Draft/Active/Archived, so current Core behavior is unchanged, but an admitted extension-specific non-Active Current RMED status would encounter the legacy Active-only inventory/graph logic.

## Evidences

Read-only source and caller comparison verified the Core domain equivalence. No current RMED extension-specific Status declaration was found. The latent gap spans _resolve(active_rmed), _rmed_status and ordinary proposed-reference inventory. This is an extension capability gap, not a reproduced Core failure or proof of current production data loss.

## Blast radius

Schedule one source-bound qualified-status implementation covering all three boundaries and frozen extension cases; changing only a string comparison would omit model/reference safeguards. Do not claim general extension Current-status relation acceptance from the present Core proof.
