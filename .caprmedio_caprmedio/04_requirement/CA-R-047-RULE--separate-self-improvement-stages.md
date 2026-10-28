---
version: 30
updated_at: 2026-10-27 19:59:49 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1423
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-047
type: Rule
tier: 1
---
# Separate self-improvement stages

a CAPRMEDIO self-improvement cycle **must** keep the following participating contributions distinct **and** traceably related:

- observations recorded **in** the Journal;
- Analysis;
- Tasks;
- changes **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations authority;
- Implementation;
- Delivery;
- follow-up Evaluation.

reusable Operations definitions remain distinct from the Journal Records of their executions **and** observations under CAPRMEDIO-META-REQU-092.
