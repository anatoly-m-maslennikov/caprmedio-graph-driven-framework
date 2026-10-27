---
subjects:
  governs: Work Journal/Append
  depends_on: []
version: 23
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-R-804
  - CA-R-805
  - CA-R-812
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-195@23
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Retry without duplicating Journal records

## Claim checked

interrupted Journal append, real-change gate, **and** Journal-batch work recover from one sealed action **without** duplicating **or** redefining evidence.

## Test case

use one sealed action. interrupt a Journal append **after** a proper subset of an action-owned partition is written, retry it with changed process time, **then** separately interrupt the real-change gate **after** an uncertain Git effect. reconcile the gate against Git **and** outbox state **before** retrying. finally batch the completed Journal record.

## Acceptance criteria

the Journal **contains** one canonical record for the action; an identical append retry reuses its identity **and** writes **only** missing bytes. a divergent record payload fails **before** append. the uncertain Git effect is reconciled **before** **any** retry **and** produces **<=1** real-change commit. Journal append **and** batch state remain independent of the gate lease; a later Journal-only batch commits **only** Journal carrier changes. recovery state retains durable action, receipt, **and** reconciliation references **without** copied mutable provenance.

## Failure disposition

reject the flow **if** recovery duplicates **or** redefines an event, retries an uncertain Git effect blindly, mixes a Journal batch into a real-change commit, **or** loses the sealed action binding.
