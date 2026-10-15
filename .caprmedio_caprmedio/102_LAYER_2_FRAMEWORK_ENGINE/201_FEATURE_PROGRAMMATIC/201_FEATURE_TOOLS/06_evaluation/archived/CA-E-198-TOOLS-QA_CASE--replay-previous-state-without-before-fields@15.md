---
subjects:
  governs: "Work Journal/Event/Previous Result Event"
  depends_on: []
status: Archived
version: 15
updated_at: "2026-10-14 18:37:38 +0400"
relations:
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-339
    - CA-M-087
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Replay previous state without before fields

## Claim checked

**when** an actual prior canonically confirmed result for the Atom identity exists, the immediate previous governed file state is recovered through `previous_result_event`, **without** copying before-state fields into the current event. a first recorded actual Atom `UPDATE`, `MOVE` **or** `MOVE+UPDATE` with no such prior result **may** omit the reference **without** a baseline; its earlier state is not thereby Journal-replayable.

## Test case

apply an `ADD`, two consecutive `UPDATE` actions, **and** a `MOVE+UPDATE` for one identity, **then** replay **every** linked transition **only** from **every** current event **and** the event referenced by `previous_result_event`. separately record a first actual Atom `UPDATE`, `MOVE` **and** `MOVE+UPDATE` with no prior canonically confirmed result, **then** a later linked change; repeat with known unmatched **or** unconfirmed history **and** a `REMOVE`.

## Acceptance criteria

the first `ADD` **or** permitted first recorded Atom `UPDATE`, `MOVE` **or** `MOVE+UPDATE` has no previous-result reference; the latter creates no automatic baseline **and** makes no earlier-state Journal-replay claim. **every** change with an actual prior confirmed result references exactly the immediate accepted prior result; replay reconstructs **every** linked transition. known unmatched, unresolved **or** unconfirmed history is **not** the first-record exception; `REMOVE` retains its existing predecessor requirement. no current event stores a copied **before** path, digest, filename, version, **or** message; accepted historical records remain unchanged.

## Failure disposition

reject the event chain at the first missing required, stale, cyclic, non-immediate, **or** duplicated previous state. reject using the first-record exception **when** prior history exists **or** is unresolved **or** unconfirmed, fabricated baselines **or** earlier-state replay claims, **and** altered event/digest bindings.
