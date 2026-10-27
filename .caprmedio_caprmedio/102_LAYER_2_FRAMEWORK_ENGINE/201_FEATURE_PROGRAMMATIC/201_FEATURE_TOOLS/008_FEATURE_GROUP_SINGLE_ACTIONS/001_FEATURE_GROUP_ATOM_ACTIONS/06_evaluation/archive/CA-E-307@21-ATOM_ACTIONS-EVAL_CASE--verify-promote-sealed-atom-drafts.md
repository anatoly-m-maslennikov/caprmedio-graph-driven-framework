---
cce_version: cce_1
cce_form: evaluation
atom_id: CA-E-307@21
content_role: Evaluation
current_scope_unit: ATOM_ACTIONS
claim_target_scope_unit: ATOM_ACTIONS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Continuant/Tool//ATOM_PROMOTE
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
version: 21
updated_at: 2026-10-26 00:46:35 +0400
relations:
  evaluation_for:
  - CA-O-066
  - CA-R-869
  - CA-D-450
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 3
type: Eval Case
---
# Verify promote sealed atom drafts

## Claim checked

CA-O-066 admits the complete selected Draft set under CA-R-869 with canonical role-matching identities, exact bytes **and** complete transaction recovery.

## Applicable when

apply **to** **any** realization **before** it can admit Draft authority into the active graph.

## Test cases

1. prepare independent singular **and** frozen bulk fixtures covering an ID-free Draft, `CA-R-draft`, `CA-R-123@4-draft` and legacy `CA-R-123@draft`; retain exact source paths/digests and explicit target/predecessor bindings.
2. verify mutation-free dry runs. Separately test absent apply authority, a non-Draft source, missing/invalid marker, filename-marker mismatch, role mismatch, repeated or historically reused target, missing proposed Version, non-next Version, stale predecessor digest and destination collision. Do not require retained Draft history, lineage or Journal evidence.
3. **after** a valid preview, independently change a Draft digest, target, predecessor Version/digest, marker or destination. Reject apply without silently changing the target, Version, selected set or sealed request.
4. apply valid singular **and** bulk requests through sealed Initiative envelopes. An existing marker must update the same canonical ID at its proposed Version and archive the exact current predecessor; an ID-free/role-draft source must receive its admitted fresh ID. Preserve body/unrelated bytes and remove only selected Draft carriers.
5. exercise both exact existing-marker entry paths for the same pinned Draft: lifecycle `change_status` with `{target: <full Draft descriptor>, status: "Active", canonical_target: <full Current descriptor>, proposed_version: <positive integer>}` and native `ATOM_PROMOTE` with `{selector: <Draft path>, target: <full Draft descriptor>, atom_id: <canonical ID>, canonical_target: <full Current descriptor>, proposed_version: <positive integer>}`. Require every duplicate ID/path/Version, marker, filename, digest and currentness representation to agree. Reject missing, Boolean, zero or negative Versions, marker/filename mismatch, wrong canonical ID/path, stale predecessor or changed digest before writes. Include an admitted current predecessor with a non-Active Status and verify the pinned current descriptor is used without silently substituting Active. A valid declared no-op leaves current/history/digests unchanged; stale or mismatched input is a refusal, not a no-op.
6. verify native new-marker packets contain one Atom Action with an exact Draft pin and no `canonical_target` for a role-only fresh-ID marker. Verify ordered bulk is executed through the existing Workflow one Action at a time, in declared order, with no reordering and no cross-Atom rollback.
7. from independently restored baselines, inject an effect failure **after** a promotion write **and** a failed post-write verification. exercise singular **and** bulk recovery, including failure **after** an earlier bulk member was moved. retain **any** accepted Journal evidence of actual effects.

## Acceptance criteria

**every** rejected preflight leaves its mutable before-state unchanged. Both existing-marker entry paths preserve exact selector/target/canonical-target identity, Version, digest and currentness pins. Successful admission preserves complete membership, canonical filenames/placement, body and unrelated metadata, and unique canonical identity. Existing-marker promotion archives exact predecessor bytes at the prior Version and writes the carried/requested Version; no Journal append or retained Draft history is a gate. A valid no-op has no current/history effect, while stale or mismatched input is refused. **Every** post-effect failure restores **all** selected mutable sources and destinations **to** their exact before-state, preserves unrelated Carriers and accepted Journal evidence, and reports failure rather than promotion success. Incomplete **or** unverified restoration **must** fail this Evaluation. Preflight rejection alone does **not** prove rollback.

## Failure disposition

reject the realization **and** preserve source digests, Draft identities, assigned IDs, historical admission evidence, promotion maps, authorization result, injected failure point, final lifecycle locations **and** **any** partial **or** duplicate active identity. these cases do **not** establish the separate external Project Goal operation boundary.
