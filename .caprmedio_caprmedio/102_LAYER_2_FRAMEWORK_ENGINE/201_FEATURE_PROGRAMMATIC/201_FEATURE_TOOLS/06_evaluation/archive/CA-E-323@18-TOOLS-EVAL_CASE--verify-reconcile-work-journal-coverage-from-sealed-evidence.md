---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Storage
  depends_on: []
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-205
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-323@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Verify reconcile work journal coverage from sealed evidence

## Claim checked

CA-M-205 recovers missing Journal coverage **only** **when** sealed evidence supplies **every** required event fact **and** does so idempotently.

## Applicable when

apply whenever Journal coverage recovery logic **or** required event fields change.

## Test case

consider two uncovered governed actions under one active Journal-event schema: one has sealed durable evidence for **every** schema-required event field **and** action binding; the other lacks one schema-required provenance field. reconcile the same frontier twice **without** changing it.

## Acceptance criteria

the first run appends **=1** complete `recovered` event for the fully evidenced action **and** reports the other as blocked; the second run appends nothing; **and** no existing Journal line is edited.

## Failure disposition

reject the realization **and** preserve both action-evidence bundles, the active event schema, coverage decisions, the appended event, blocked field, Journal before-and-after digests, **and** second-run result.
