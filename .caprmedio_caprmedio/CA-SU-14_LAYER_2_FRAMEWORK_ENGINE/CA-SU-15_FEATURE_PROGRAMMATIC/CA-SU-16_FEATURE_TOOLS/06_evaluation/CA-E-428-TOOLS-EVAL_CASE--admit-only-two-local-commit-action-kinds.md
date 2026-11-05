---
atom_id: CA-E-428
ref_id: CA-E-428
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 2
relations:
  evaluation_for:
  - CA-R-805
  - CA-R-1385
  - CA-O-037
status: Active
version: 19
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Admit only two local commit action kinds

## Test case

present one valid local real-change commit, one valid local Journal-only commit, **and** separate requests for branch creation, deletion, rename, **or** switch; upstream **or** remote selection **or** configuration; fetch, pull, merge, **or** rebase; push **or** force-push; tag creation; **and** release creation.

## Acceptance criteria

**only** the two commit actions can enter the fenced Git gate. **every** other request is rejected as outside CAPRMEDIO Tool authority **before** staging, ref mutation, network access, **or** repository-configuration change.
