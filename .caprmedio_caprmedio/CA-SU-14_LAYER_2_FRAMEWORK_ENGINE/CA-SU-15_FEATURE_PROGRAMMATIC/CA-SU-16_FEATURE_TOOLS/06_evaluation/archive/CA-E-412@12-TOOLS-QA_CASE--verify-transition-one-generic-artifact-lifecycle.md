---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Transition Generic Artifact Lifecycle
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Artifact
  - Subject/Engineering/Carrier
  - Artifact/Revision
  - Subject/Graph/Relation
version: 12
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-R-1134
  - CA-O-041
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-412@12
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify transition one generic Artifact lifecycle

## Claim checked

CA-O-041 applies **=1** registered generic Artifact lifecycle transition **or** fails closed **without** changing the carrier.

## Applicable when

apply whenever a generic lifecycle state model, destination derivation, **or** lifecycle transaction mechanics change.

## Test case

prepare one source Artifact at a registered lifecycle state with one canonical reference. request one valid transition **and** **then** a transition **not** present **in** the state model.

## Acceptance criteria

the valid case creates the permitted destination **if** needed, moves the carrier, records required metadata **and** reference updates, **and** reaches the registered state. the undefined transition changes nothing.

## Failure disposition

reject the realization **and** preserve the state model, source **and** destination states, metadata **and** reference diffs, transaction evidence, **and** undefined-transition finding.

## Post-effect failure coverage

from an independent recorded before-state, inject a failure **after** the selected Carrier move **or** required metadata **or** reference change **and** **before** the complete transition is accepted.

- verify restoration of **every** selected mutable Carrier, metadata value, **and** canonical reference **to** the exact before-state, including the prior existence **or** absence of owned destination paths. unrelated Carriers remain unchanged.
- distinguish failed preflight, failed apply, successful restoration, **and** incomplete restoration. **none** is an accepted successful transition.
- retain evidence that the injected failure followed a real selected effect. preflight rejection alone does **not** prove recovery; incomplete **or** unverified restoration fails the rollback guarantee.
