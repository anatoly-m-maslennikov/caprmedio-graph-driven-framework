---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: programmatic-mutation
  depends_on: []
version: 11
updated_at: 2026-10-23 03:17:34 +0400
relations:
  evaluation_for:
  - CA-M-205
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-323@11
status: Archived
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
