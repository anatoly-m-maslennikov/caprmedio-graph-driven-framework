---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1147
  derived_from:
    - CA-A-058
---
# Record one verified release outcome

## Applicable when

Use this Method after one release attempt has a sealed factual outcome and attributable verification evidence.

## Procedure

1. Seal the attempted version, release revision or commit, manifest, verification results, Journal frontier, actor, and completion time.
2. Determine success only from the declared release acceptance criteria and their attributable evidence.
3. For success, create one immutable Ops Release Record binding the version, exact revisions, checks, evidence, Journal, and canonical Git identity.
4. For failure, create non-release Ops evidence that records the failed attempt and preserves the version as unreleased.
5. Reject duplicate or conflicting outcomes for the same release identity.

## Outcome

A successful release has one immutable Release Record; an unsuccessful attempt remains explicit evidence and never becomes a release claim.

## Failure or stop

Do not infer success from intent, partial checks, or an unsealed manifest; stop on missing evidence or conflicting release identity.
