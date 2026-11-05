---
atom_id: CA-M-200
ref_id: CA-M-200
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
tier: 2
relations:
  method_for:
  - CA-R-1120
  derived_from:
  - CA-A-058
status: Active
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reconcile Git and Journal provenance bidirectionally

## Applicable when

use this Method **when** comparing reachable Git change history with Work Journal coverage for the same governed action frontier.

## Procedure

1. seal a reachable Git frontier **and** the corresponding Journal batch frontier.
2. normalize both sides **to** action, Initiative, commit SHA, event ID, subject path, subject revision, digest, batch SHA, **and** ordering facts.
3. match Git real-change commits **to** Journal events **in** both directions **and** classify missing, duplicate, unreachable, digest-mismatched, revision-mismatched, **and** watermark-lag cases.
4. append a recovered Journal event **only** **when** reachable history **and** sealed durable state prove **every** required field; **otherwise** keep the case blocked.
5. re-run the comparison over the same frontier **and** emit a stable reconciliation report whose second unchanged run produces no new events.

## Outcome

Git **and** Journal provenance are either reconciled idempotently **or** separated into explicit evidence-backed discrepancy classes.

## Failure or stop

do **not** infer missing provenance **or** rewrite Git history; stop recovery whenever required identity, digest, reachability, **or** batch evidence is insufficient.
