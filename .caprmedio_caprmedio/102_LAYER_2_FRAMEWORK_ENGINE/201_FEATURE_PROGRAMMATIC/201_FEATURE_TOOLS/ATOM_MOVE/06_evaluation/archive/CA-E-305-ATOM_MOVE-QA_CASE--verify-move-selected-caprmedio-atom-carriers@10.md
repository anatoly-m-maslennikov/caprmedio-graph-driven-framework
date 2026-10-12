---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 10
updated_at: "2026-10-12 23:13:13 +0400"
relations:
  evaluation_for:
    - CA-M-187
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify move selected caprmedio atom carriers

## Claim checked

CA-M-187 moves one sealed Atom while preserving its complete bytes, filename and stable ID. A subtree selection is an ordered set of independent Atom actions under CA-M-372.

## Applicable when

Apply before relying on an Atom Move realization. These cases specify required future checks, not an observed pass.

## Test case

Prepare one exact Atom and a two-level subtree with three Atoms and one non-Atom file. Freeze the explicit ordered Atom selection and expected source states. Verify default shape preservation and explicitly requested flattening maps without mutation. Each move needs its own permission/currentness and collision checks.

## Failure cases

For ordered A, B and C, complete A and inject a destination collision or post-write failure for B. Retain A at its observed destination, report B's failure and leave C and the non-Atom untouched. Do not restore A merely because B failed.

Within one Move action, inject a failure after destination publication or during verification. Require that action's admitted all-or-nothing boundary and exact restoration where claimed; unverified restoration fails the check. Preserve unrelated files and accepted history. Preflight refusal is not post-effect rollback evidence, and this revision does not settle CA-C-119's separate owner/filename issue.

## Acceptance criteria

Each completed action preserves its Atom's filename, ID and byte digest and removes only its admitted source. Maps and effects remain attributable per Atom. Dry runs and rejected preflight have no effect; earlier completed actions survive a later failure and the remainder is untouched. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.

## Failure disposition

Retain ordered selection, exact pins, mappings, permission decisions, observed source/destination states, successes, failure and unperformed remainder.
