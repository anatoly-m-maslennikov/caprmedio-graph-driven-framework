---
atom_id: CA-E-651
ref_id: CA-E-651
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 2
relations:
  evaluation_for:
  - CA-M-404
status: Active
version: 13
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-E-651-PROGRAMMATIC-POLICY--evaluate-authorized-targets-and-deltas.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Evaluate authorized targets and deltas

## Scope

PROGRAMMATIC mutations and delegated effects, including independent members of a batch and concurrent requests crossing file, process, persistence or transport boundaries.

## Claim

Accept effect conformance only when the observed effects stay within the actually authorized target and delta under the required expected state. Reading additional state, finding a convenient replacement target or receiving a successful adapter response does not authorize an extra effect. Ambiguous, stale, unsupported or unauthorized bindings stop the affected change while unrelated authorized work remains independently reportable.

## Details

- Bind the actual instruction, explicit target, allowed delta and required preconditions; compare observed changed paths, resources and values with that boundary, not merely the final success flag.
- Exercise an authorized exact change and wrong-Project, wrong-target, extra-delta, target-substitution, stale-source, ambiguous and unsupported cases. Rejected cases have no unauthorized effect.
- Observe adapters and asynchronous continuations as well as the canonical owner. A secondary read or discovered artifact must not silently become a write target.
- For concurrent or bulk work, retain verified independent completed effects and refuse the affected stale or unauthorized member without widening scope, replaying completed work or inventing cross-target rollback.
- Distinguish a safety refusal from unhealthy runtime. This Evaluation does not add an approval mechanism, mandatory new Plan artifact, Journal-completeness gate or automatic retry.
