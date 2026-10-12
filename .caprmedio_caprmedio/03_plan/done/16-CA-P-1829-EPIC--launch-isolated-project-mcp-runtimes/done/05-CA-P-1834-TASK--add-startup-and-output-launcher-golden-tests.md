---
atom_id: CA-P-1834
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 03:46:50 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1837
    - CA-P-1840
    - CA-P-1842
---
# Summary

Add startup **and** output launcher golden tests

## Objective

the AI Agent creates the test-first golden corpus for repeat startup, port admission, **and** safe readiness results.

## Details

- input: the reviewed startup/result RMED **and** existing HTTP runtime tests.
- output: mocked tests for healthy reuse, concurrent same-Project launch, identical request IDs across distinct Project reload stores, container/image mismatch, Docker-allocated ports, wrong publishers, failed health, wrong credentials, timeout, **and** URL output with no credential.
- verification: run the bounded tests **before** implementation; require correct non-success results rather than a fabricated ready endpoint.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: the startup suite exercises the 13 O188 condition codes, strict publication, token redaction, authenticated readiness, real lock contention **and** concurrent reuse; direct unittest invocation recorded expected pre-implementation missing-module failure.

- reopened **after** independent final review: current authority also admits explicit ports. add required bounds, exact publication, requested-port reuse/mismatch, **and** occupied-port refusal fixtures **before** the corresponding implementation repair; prior passing corpus remains valid evidence for its covered cases, **not** the missing cases.

the Plan is **not** Done **if** ((a required startup **or** result case is absent) **or** (a failure fixture accepts a success URL) **or** (the pre-implementation test result is missing)).

- final completion evidence: **`=20`** startup tests, **`=5`** CLI tests, **and** **`=8`** proof-harness fixtures pass within the current **`=60`** host-test corpus. the original pre-implementation missing-module receipt is retained. the post-start-absence regression also recorded **`=1`** failure **before** its repair; no executed red receipt is claimed for the initial explicit-port additions. the frozen-source real-Docker proof `launcher-proof-0omrljbe/result.json` completed both Project layouts, including exact dynamic/explicit ports, mismatch, occupied-publication refusal, safe readiness, **and** reuse.
