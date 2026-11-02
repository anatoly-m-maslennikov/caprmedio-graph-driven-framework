---
subjects:
  governs: "Work Journal/Event/Previous Result Event"
  depends_on: []
status: Archived
version: 17
updated_at: "2026-10-14 18:37:38 +0400"
relations:
  evaluation_for:
    - CA-R-812
    - CA-R-1644
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Recover the first prior result without invention

## Claim checked

**when** recovery is explicitly requested for an existing governed subject with no accepted prior result event, it creates a separate evidenced baseline **only** **when** the prior state is sufficiently supported. an actual first recorded Atom `UPDATE`, `MOVE` **or** `MOVE+UPDATE` with no prior canonically confirmed result for that identity **may** instead record **only** the completed change **without** `previous_result_event` **and** **without** automatically creating a baseline; it does **not** claim that earlier state is Journal-replayable.

## Test case

prepare the first schema-version-3 Atom `UPDATE`, `MOVE` **and** `MOVE+UPDATE` with no prior canonically confirmed result for that identity **and** record each actual change **without** a baseline. separately request recovery **and** prove a separate recovered baseline from matching present Carrier readback **without** Git, **then** with genuine Git corroboration. repeat with an actual prior confirmed result, known unmatched **or** unconfirmed predecessor evidence, contradictory **and** insufficient recovery evidence, an ID-less Draft Carrier, a no-op, unconfirmed append receipts **and** a `REMOVE`.

## Acceptance criteria

the permitted first-recorded-change case appends **=1** actual `completed` `governed_project_change` event, omits `previous_result_event` **and** creates no baseline **or** earlier-state replay claim. **when** a prior canonically confirmed result exists, the change retains its exact immediate `previous_result_event`; known unmatched, unresolved **or** unconfirmed predecessor evidence refuses rather than becoming a first-record exception. `REMOVE` retains its existing predecessor requirement. the explicitly requested, supported recovery case appends **=1** `recovered` `governed_project_state` baseline **before** dependent effects **and** makes the subsequent `completed` `governed_project_change` event reference its confirmed prior through `previous_result_event`. the contradictory **and** insufficient cases do **not** mutate the subject; no historical field is guessed. a no-op creates **none** of a baseline **or** change event. unconfirmed baseline recording blocks effects; unconfirmed post-effect recording retains the real effects as partial **and** permits recording retry **only**. accepted legacy schema-version-2 records remain readable, **not** current write examples.

## Failure disposition

reject recovery **if** it embeds the baseline **in** the change event, invents prior state, accepts contradictory evidence, **or** proceeds **without** the required previous-result reference. reject treating known unmatched **or** unconfirmed history as absent, dropping a required link, automatically creating a baseline for the permitted first change, **or** claiming its earlier state is Journal-replayable. stale, cyclic, non-immediate, duplicate **or** digest-mismatched evidence remains a failure.
