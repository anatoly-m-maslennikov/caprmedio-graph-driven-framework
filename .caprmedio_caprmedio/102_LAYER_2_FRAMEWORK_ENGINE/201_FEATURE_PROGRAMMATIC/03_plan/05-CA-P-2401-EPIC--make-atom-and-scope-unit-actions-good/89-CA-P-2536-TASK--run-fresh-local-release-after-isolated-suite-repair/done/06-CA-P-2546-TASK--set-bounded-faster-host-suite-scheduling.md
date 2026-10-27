---
atom_id: CA-P-2546
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Workflow Execution
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2536
version: 7
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
---
# Summary

Set bounded faster host suite scheduling

## Objective

Implement the Operator-approved bounded faster full-suite profile without relaxing validation or resource safety.

## Details

Exclusive edit PROJECT_TOOLS/run_full_test_suite.py only, after current full-suite terminal and root activation. Set MODULE_TIMEOUT_SECONDS3600 and ordinary ThreadPoolExecutor4, keep Docker2, critical publication module isolated first and all exact-once/failure/count/skip/output/launcher/cancellation behavior. No new config API, scheduler abstraction, dependency or Docker daemon/production changes. Respect compact M/E/D; report exact size/unit debt instead of claiming waiver. No tests/Atoms/README/Git/Docker/MCP/release edits; cooperate testowner. At most15minutes own work.

### Execution handoff after terminal failed gate

Active, root owns the three-literal runner update and README directly. Source ownership is PROJECT_TOOLS/run_full_test_suite.py only; tests belong P2547. MODULE_TIMEOUT_SECONDS3600, ordinary4/Docker2; isolated-first ordering and launcher1980 remain unchanged. No generic new API/config.

### Latest focused-only validation instruction

Latest Operator instruction: after these fixes, DO NOT rerun the full suite; run only broken and related checks. This supersedes all earlier next-full-gate clauses in this current Task/Epic. Focused acceptance includes stale image-reference tests/related image selection, scheduler regression portfolio and the original11-test plus new1-test W01Docker modules (all29statuses). Use3600second module budget,4host+2Docker capacity, isolated crash-probe scheduling; no unrelated test rerun or production mutation test. Report focused results accurately; do not call the current HEAD full-suite green or invoke the normal Local-release command that automatically reruns it.

### Focused source acceptance and next boundary

Runner now has3600second module cap,4ordinary+2Docker pools and existing publication-module isolation;1980second launcher cap unchanged. README aligns. Related scheduler17/17 pass0.598s; image/context10/10 pass0.160s; pinned Ruff/diff and independent review APPROVE. Host8CPU16GiB/Docker4CPU~2.84GiB justify not expanding VM workers; sampled memory is not a peak/speedup guarantee. Runner245lines unchanged by this literal-only profile change; C564 remains separate.
