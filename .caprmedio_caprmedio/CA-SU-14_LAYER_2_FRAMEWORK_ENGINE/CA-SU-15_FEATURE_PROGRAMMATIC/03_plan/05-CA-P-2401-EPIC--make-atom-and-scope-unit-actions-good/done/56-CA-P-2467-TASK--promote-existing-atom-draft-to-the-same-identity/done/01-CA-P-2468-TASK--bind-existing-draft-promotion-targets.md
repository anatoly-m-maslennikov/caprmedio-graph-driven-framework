---
atom_id: CA-P-2468
ref_id: CA-P-2468
role: Plan
form: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
relations:
  is_decomposition_of:
  - CA-P-2467
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
container:
  atom: CA-P-2467
carrier_destination:
  file:
    name: 1-CA-P-2468-TASK--bind-existing-draft-promotion-targets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/56-CA-P-2467-TASK--promote-existing-atom-draft-to-the-same-identity/done
---
# Summary

Bind existing Draft promotion targets

## Objective

Seal the exact Draft descriptor, canonical predecessor descriptor, and proposed Version. Reuse typed carrier descriptors; require proposed Version=predecessor+1 and refuse stale, missing, ambiguous or colliding targets before effects.

## Details

At most 15 minutes own work; split before extending. Follow PROGRAMMATIC M projection and latest Operator same-ID promotion decision. Preserve exact history; no Journal/retained-Draft-history admission gate. No live test traffic, deployment, Methodology map repin or held-batch replay.

### Definition of Done

Seal the exact Draft descriptor, canonical predecessor descriptor, and proposed Version. Reuse typed carrier descriptors; require proposed Version=predecessor+1 and refuse stale, missing, ambiguous or colliding targets before effects. Observable focused evidence and independent review are required. Review dependent next Task before execution.

### Dependency review checkpoint

P2468 binding/preflight completed. Four frozen checks passed, including existing-marker creation, sealed-target rejection, Done-to-Active Version refusal and strict Boolean Version denial. Current uniqueness uses the shared bounded CurrentAtomLocator. API review accepts exact target and canonical_target descriptors plus explicit proposed_version; IDs/paths/Versions/digests must agree. P2469 was dependency-reviewed against these checks before activation; publication is not yet accepted.
