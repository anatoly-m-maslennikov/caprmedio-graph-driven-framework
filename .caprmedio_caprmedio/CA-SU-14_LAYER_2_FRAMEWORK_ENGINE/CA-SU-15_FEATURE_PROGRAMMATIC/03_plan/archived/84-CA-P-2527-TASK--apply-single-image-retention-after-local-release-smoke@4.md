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
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 4
updated_at: "2026-10-21T10:42:00Z"
---
# Summary

Apply single-image retention after Local release smoke

## Objective

Apply single-image retention after Local release smoke.

## Details

After P2526 contract/scope acceptance, reuse canonical ImageManager naming during post-green candidate preparation. Implement candidate-only image retention in the existing cleanup owner after verified installed MCP smoke. Other digests sharing its fingerprint do not earn another retention slot. Use immutable identity and positive CAPRMEDIO classification, never names alone. Preserve container-referenced images, unknown classification and failed inspection; no force, prune or uncertain retry. Container cleanup retains its selected-Project ownership boundary. At most 15 minutes own work; split before extending. No release execution or production port.

### Bounded activation before retention-scope resolution

The existing D564/R1878 safety rule already requires positive verification before image retirement. Correct the current empty-prior-image guard so every image-cleanup call requires the launched immutable image to equal the admitted candidate, even when cleanup.images starts empty. Failed verification skips image removal and reports pending under the existing disposition. This correction and independent ordering tests may proceed now; host-wide versus selected-Project retention semantics remain held until P2526 resolves the Operator's scope choice and aligns the contract. No actual release or Docker effects.

### Current reviewed checkpoint

The empty-prior-image proof gap is fixed: every image-cleanup call now requires current_image == candidate_image; mismatch/None skips discovery/removal and reports pending. Root59/59 focused checks and independent review pass. New one-image retention semantics are NOT yet implemented; C563 scope and P2526 active-contract alignment remain prerequisites. Current fingerprint/ownership preservation is unchanged.

### Project-only implementation activated

C563 is resolved and P2526 source alignment is accepted. Implement in bounded children P2530 (image retention) and P2531 (eligible stopped containers); parent owns exact-prior selected-Project MCP candidate-digest matching and removal of dead fingerprint-only helpers. P2528 already owns accepted ordering/failure tests; refresh synthetic release regression for same-fingerprint/different-digest replacement. Each child has at most15 minutes own work and exclusive files. Preserve runtime validation, exact candidate reuse, no-force/no-prune/no retry and pending reporting. No Docker/release execution.
