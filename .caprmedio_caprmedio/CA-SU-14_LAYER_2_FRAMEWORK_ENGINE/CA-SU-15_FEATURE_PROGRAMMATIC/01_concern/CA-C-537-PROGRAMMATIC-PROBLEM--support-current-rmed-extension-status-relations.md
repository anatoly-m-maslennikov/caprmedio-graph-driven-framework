---
atom_id: CA-C-537
ref_id: CA-C-537
container:
  scope_unit: CA-SU-15
role: Concern
form: Problem
topics:
  main_subject: Subject/Domain/Node/Continuant/Atom
relations:
  concern_about: [CA-R-1676, CA-P-2401]
status: Active
version: 2
updated_at: 2026-10-23 03:06:32 +0400
carrier_destination:
  file:
    name: CA-C-537-PROGRAMMATIC-PROBLEM--support-current-rmed-extension-status-relations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
priority: medium
---
# Summary

Support Current RMED extension-status relations

## Concern

R1676v21 changes RMED relation eligibility from Active to Current. Core RMED domains currently contain only Draft/Active/Archived, so current Core behavior is unchanged, but an admitted extension-specific non-Active Current RMED status would encounter the legacy Active-only inventory/graph logic.

## Evidences

Read-only source and caller comparison verified the Core domain equivalence. No current RMED extension-specific Status declaration was found. The latent gap spans _resolve(active_rmed), _rmed_status and ordinary proposed-reference inventory. This is an extension capability gap, not a reproduced Core failure or proof of current production data loss.

## Blast radius

Schedule one source-bound qualified-status implementation covering all three boundaries and frozen extension cases; changing only a string comparison would omit model/reference safeguards. Do not claim general extension Current-status relation acceptance from the present Core proof.
