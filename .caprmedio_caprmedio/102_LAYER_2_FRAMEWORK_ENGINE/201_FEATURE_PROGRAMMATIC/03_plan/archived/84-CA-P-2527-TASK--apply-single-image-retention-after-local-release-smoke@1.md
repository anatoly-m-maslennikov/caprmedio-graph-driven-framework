---
atom_id: CA-P-2527
content_role: Plan
type: Plan
label: Task
work_sequence_number: 84
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-21T10:06:31Z"
---
# Summary

Apply single-image retention after Local release smoke

## Objective

Apply single-image retention after Local release smoke.

## Details

After P2526 contract/scope acceptance, reuse canonical ImageManager naming during post-green candidate preparation. Implement candidate-only image retention in the existing cleanup owner after verified installed MCP smoke. Other digests sharing its fingerprint do not earn another retention slot. Use immutable identity and positive CAPRMEDIO classification, never names alone. Preserve container-referenced images, unknown classification and failed inspection; no force, prune or uncertain retry. Container cleanup retains its selected-Project ownership boundary. At most 15 minutes own work; split before extending. No release execution or production port.
