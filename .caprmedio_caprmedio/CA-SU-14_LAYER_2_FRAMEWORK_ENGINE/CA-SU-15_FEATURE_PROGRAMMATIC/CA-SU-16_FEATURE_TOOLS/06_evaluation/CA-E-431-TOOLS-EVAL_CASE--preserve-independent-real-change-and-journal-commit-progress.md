---
atom_id: CA-E-431
ref_id: CA-E-431
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
tier: 3
relations:
  evaluation_for:
  - CA-R-802
  - CA-R-812
  - CA-M-087
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Preserve independent real-change and Journal commit progress

## Test case

delay Journal append while a valid real-change action reaches the Git gate, **then** delay the real-change commit while Journal append completes. batch the completed Journal record later, including a batch on the configured periodic interval.

## Acceptance criteria

neither branch gates the other's non-conflicting progress. the real-change commit **contains** **only** its sealed targets; Journal append remains independently durable; the later Journal-only commit **contains** **only** selected Journal Carriers; **and** both commit effects remain serialized by one repository gate **without** losing their common action provenance.
