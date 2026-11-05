---
atom_id: CA-P-2540
ref_id: CA-P-2540
container:
  atom: CA-P-2537
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Workflow Execution
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2537
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 3-CA-P-2540-TASK--prepare-functional-regressions-for-docker-network-cleanup.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/90-CA-P-2537-TASK--diagnose-docker-test-network-lifetime-and-address-exhaustion/done
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Prepare functional regressions for Docker network cleanup

## Objective

Resolve the observed isolated Docker network gate failure without affecting the working MCP.

## Details

Read-only existingtests/fixtures mapping for bounded functional regression design: successfulcase cleanup, partialstartupfailure, interrupt, ownership/refusal/protection and realnetwork absence proof. No sourcewrites/tests/Docker/MCP/release/Git. Return smallest disjoint testownership proposal and exactacceptance; root freezes aftersourceevidence. No unit-test scaffolding for unrequestedgenericcleanupframework.

### Actual result and next boundary

Read-only regression design accepted: existing fixture cleanup checks cover normal/partial startup and cleanup failure; runtime stop retention remains protected. No speculative fixture rewrite or generic cleanup owner is needed for this observed historical capacity issue. P2541 will use the existing real three-test Docker module on an isolated current-source image and compare exact network/production baselines after teardown. Additional cancellation/no-container-start reproduction belongs to C567, separate from current release acceptance.
