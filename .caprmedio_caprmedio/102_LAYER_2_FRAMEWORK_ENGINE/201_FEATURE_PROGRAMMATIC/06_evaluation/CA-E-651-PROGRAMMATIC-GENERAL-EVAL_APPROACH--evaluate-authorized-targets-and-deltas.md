---
atom_id: CA-E-651
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 01:50:12 +0400
subjects:
  governs: Subject/Engineering/Effect Authorization
  depends_on: []
relations:
  evaluation_for:
  - CA-M-404
tier: 2
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
