---
atom_id: CA-E-341
ref_id: CA-E-341
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  evaluation_for:
  - CA-R-1385
  - CA-R-1491
  - CA-M-182
status: Active
version: 19
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject an undeclared downstream transition

## Claim checked

a worker **or** Scheduler cannot invent downstream work outside the accepted manager-defined graph.

## Test case

return valid worker completion facts together with a requested step identity absent from the persisted declared transitions. inspect the rejected request, persisted stop state, diagnostics **and** attempted effects.

## Acceptance criteria

- completion facts remain inspectable **and** the undeclared transition is rejected; autonomous dispatch stops at the safe declared boundary.
- no undeclared executable work is queued **or** dispatched, **and** no Git **or** governed-content effect is authorized by that request.
- the bounded runtime transition that records blocked state **and** the admitted diagnostic evidence remain permitted under the existing recovery authority. recording the rejection is **not** acceptance of its requested work.
- an intact event about the rejected request remains eligible for Journal storage under CA-R-1491; accepted storage cannot certify the invalid transition **or** grant permission **to** resume.

## Failure disposition

reject invented downstream work, silent loss of the completion **or** stop reason, unauthorized effects, **or** a diagnostic-state update used **to** bypass the dispatch guard. preserve the accepted graph, requested step, completion facts **and** actual stop/effect evidence.
