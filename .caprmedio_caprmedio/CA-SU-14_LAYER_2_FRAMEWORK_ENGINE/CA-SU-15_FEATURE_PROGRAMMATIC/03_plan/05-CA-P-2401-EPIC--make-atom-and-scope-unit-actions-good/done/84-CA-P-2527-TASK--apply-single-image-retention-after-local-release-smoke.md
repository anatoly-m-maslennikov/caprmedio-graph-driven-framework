---
atom_id: CA-P-2527
ref_id: CA-P-2527
container:
  atom: CA-P-2401
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Release Version/Runtime Package Carrier
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2401
status: Done
version: 9
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 84-CA-P-2527-TASK--apply-single-image-retention-after-local-release-smoke.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done
work_sequence_number: 84
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Apply single-image retention after Local release smoke

## Objective

Apply single-image retention after Local release smoke.

## Details

After P2526 contract/scope acceptance, reuse canonical ImageManager naming during post-green candidate preparation. Implement candidate-only image retention in the existing cleanup owner after verified installed MCP smoke. Other digests sharing its fingerprint do not earn another retention slot. Use immutable identity and positive CAPRMEDIO classification, never names alone. Preserve container-referenced images, unknown classification and failed inspection; no force, prune or uncertain retry. Container cleanup retains its selected-Project ownership boundary. At most 15 minutes own work; split before extending. No release execution or production port.

### Bounded activation before retention-scope resolution

The existing D564/R1878 safety rule already requires positive verification before image retirement. Correct the current empty-prior-image guard so every image-cleanup call requires the launched immutable image to equal the admitted candidate, even when cleanup.images starts empty. Failed verification skips image removal and reports pending under the existing disposition. This correction and independent ordering tests may proceed now; host-wide versus selected-Project retention semantics remain held until P2526 resolves the Operator's scope choice and aligns the contract. No actual release or Docker effects.

### Earlier reviewed checkpoint

The empty-prior-image proof gap is fixed: every image-cleanup call now requires current_image == candidate_image; mismatch/None skips discovery/removal and reports pending. Root59/59 focused checks and independent review pass. New one-image retention semantics are NOT yet implemented; C563 scope and P2526 active-contract alignment remain prerequisites. Current fingerprint/ownership preservation is unchanged.

### Project-only implementation activated

C563 is resolved and P2526 source alignment is accepted. Implement in bounded children P2530 (image retention) and P2531 (eligible stopped containers); parent exclusively owns PROJECT_TOOLS/RELEASE_VERSION/local_release.py (exact-prior MCP matching) and release_cleanup_identity.py (helper definitions). P2531 alone removes imports/calls in release_cleanup.py before the parent deletes the now-unused helper definitions. P2528 already owns accepted ordering/failure tests; the regression lane exclusively owns PROJECT_TOOLS/tests/test_simple_local_release.py and test_local_release_cleanup.py for same-fingerprint/different-digest replacement. Each child has at most15 minutes own work and exclusive files. Preserve runtime validation, exact candidate reuse, no-force/no-prune/no retry and pending reporting. No Docker/release execution.

### Functional implementation accepted

P2530/P2531 and parent caller/helper integration are complete. Independent review APPROVE found no new cleanup data-loss/ownership regression; planning ownership review APPROVE. Final frozen10-module synthetic gate102/102 passed9.632s (earlier integrated102/10216.084s is a separate run, not additive). Complete Project image ownership, exact-candidate retention, same-fingerprint older rebuild retirement, all references, exact-prior MCP replacement and suite/smoke failure gates are covered. Other6changed Python files pass pinned Ruff; local_release retains exactly its4HEAD diagnostics, C90159 unchanged. C564 records stale size/exception evidence and test-file size increases; no whole-source E539 acceptance or global lint-clean claim. No actual release/Docker effects, deployment, version bump or push.
