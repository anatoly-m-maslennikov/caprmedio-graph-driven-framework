---
identity:
  id: CA-P-2817
  ref_id: CA-P-2817
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: Done
  version: 6
  updated_at: 2026-11-11 08:17:35 +0400
destination:
  file:
    name: CA-P-2817-TASK--verify-engine-performance-and-resource-regressions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2812
  - CA-P-2813
  - CA-P-2814
  - CA-P-2815
  - CA-P-2816
  - CA-P-2839
  - CA-P-2842
  - CA-P-2843
  - CA-P-2844
  - CA-P-2852
  - CA-P-2859
  - CA-P-2861
  - CA-P-2866
  - CA-P-2910
---

## Summary

Verify Engine performance and resource regressions

## Objective

Run the existing latency, 500-Atom throughput, cold rebuild and resource/soak acceptance against the final combined code revision after all performance-affecting changes. Record that revision and rerun affected acceptance if it changes before delivery. Preserve current acceptance limits and report CPU peak caveats separately. Do not substitute profiling runs for acceptance.

## Subtasks

- [x] Review and fix the next scoped input batch. (ETA: up to 15 min.)
- [x] Complete one scoped implementation or verification batch; split before exceeding 20 min.
- [x] Review and fix the result; record a small P / Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.

## Candidate acceptance

The nine Docker tests passed on d520960c81eb, including the short resource guard. Its soak stopped after 21 minutes at the frozen memory guard. P2948 records the failure. The accelerated diagnostic reproduced the crossing during a Scope Declaration refresh and measured a 74 MiB jump across projection replacement. Reverify the corrected image against the original limits. Evidence is under `.caprmedio_tmp/CA-P-2791/CA-P-2817/`.

## Final acceptance

P2960 records nine passing Docker tests and the full 30-minute soak on the corrected image. The existing performance and resource limits passed.
