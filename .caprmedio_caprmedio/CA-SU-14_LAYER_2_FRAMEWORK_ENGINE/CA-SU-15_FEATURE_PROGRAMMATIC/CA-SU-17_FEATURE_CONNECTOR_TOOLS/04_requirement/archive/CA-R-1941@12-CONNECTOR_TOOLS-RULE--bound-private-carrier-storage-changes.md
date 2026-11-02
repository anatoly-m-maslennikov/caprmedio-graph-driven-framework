---
atom_id: CA-R-1941@12
content_role: Requirement
type: Rule
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Storage
  depends_on:
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/Workflow
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Actor
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
version: 12
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1936
tier: 3
---
# Summary

Bound private carrier storage changes

## Scope

Private file/folder rename, move and non-Atom cleanup mechanics behind the logical connector interface. The required result is one explicitly approved carrier storage change, with independently verified before/after evidence and no widened effect.

## Claim

a private carrier change **must** be bound **to** one logical request under CA-R-1936 **and** CA-D-625's supported `modify` operation. rename, move **and** remove are private adapter variants, **not** new common verbs **or** public physical-path operations. the owning Workflow supplies domain policy, schema, identity, Version/time, lifecycle **and** authorization; the helper performs **only** the exact selected storage change.

the private binding **must** identify the source carrier, file/folder kind, approved source **and** destination roots **where** applicable, expected source state, explicit destination **and** expected absence **where** applicable. paths remain private resolved binding data. the selected root itself, a filesystem/Project root, an ancestor containing either root, an escaping path, symlink **or** substituted source/destination/ancestor **must not** be affected. required source, parent, destination **and** permission evidence **must** be current at the effect boundary.

rename changes **only** the explicitly supplied name within the same parent. move uses the explicitly supplied destination; **any** basename change **must** already be explicit, **not** inferred. both **must** preserve carrier content, declared modes/metadata **and** unrelated entries, except separately supplied Workflow-owned changes outside this helper's location-only contribution. for an actual rename/move, the distinct destination **must** be absent; existing distinct destinations, collisions, overwrite **or** merge requests are rejected. a verified same-binding no-op is **not** an overwrite. a folder rename/move requires a complete finite approved entry inventory; missing, added, substituted **or** unlisted entries fail rather than enlarging the admitted frontier. a folder move destination inside the selected source subtree, **or** **any** other invalid source/destination overlap, is rejected; verified identical-binding no-op remains distinct. no automatic recursive selection is admitted.

remove **must** be separately approved non-Atom storage cleanup of one file **or** one empty folder. a nonempty folder, uncertain classification, Atom/current/historical carrier, required history, protected source **or** unapproved cleanup target is rejected. there is no delete-Atom operation. cleanup neither follows symlinks nor enumerates descendants into a removal set. an existing admitted Atom lifecycle operation **may** use a private carrier move **only** through its exact admitted lifecycle/currentness/history context; the helper cannot substitute for Archive, retire, replacement **or** authority admission.

**before** an actual rename, move **or** cleanup effect, stage **and** review the exact source-bound intended location/absence change **and** its affected source, parents, destination, finite inventory, preservation **and** governing authority frontier. the existing bound authorization **must** resolve a fresh purpose-specific trusted-host record of the Operator's review **and** recorded confirmation that manual editing, maintenance/script writes, Git **and** synchronization are paused for that exact frontier. bind the record **to** the exact logical request, private Action/variant, selected Session/Run **and** affected files. caller-written data, hashes, approval flags **or** arbitrary callbacks cannot mint confirmation; unavailable, missing, stale **or** mismatched confirmation refuses **before** effects.

within that confirmed exclusive window, perform final complete admission/currentness revalidation **before** the exact storage effect **and** retain independent readback **and** verification. unavailable window, changed evidence **or** failed admission stops **before** effects. no project-wide Engine write lock **or** replacement is required; distinct existing resource-specific locks remain unchanged. the model does **not** exclude other Engine writers **or** protect against writers ignoring the confirmed window **and** establishes no crash-atomicity, cleanup restoration, automatic retry **or** replay guarantee.

the result **must** follow CA-D-625's `data/current_state/effects/errors` roles. success requires independent verification of this variant's declared postconditions. unknown effects require `effect_uncertain`; nonempty errors are **not** success, even with known partial effects. empty errors cannot mean merely that no exception occurred. a no-op requires verified requested state already satisfied **and** unchanged; a missing expected-present source is **not** an inferred completed rename/move/remove.

## Details

CA-M-381 supplies binding construction; CA-D-630 binds representation; CA-O-215/216/217 define the three reusable Actions; CA-E-633 supplies falsifiable cases. CA-O-040 is different: its generic Artifact rename includes canonical-reference rewrites. These private helpers never discover or rewrite references, create domain identity or report a logical lifecycle operation completed from a storage effect alone.

retain existing admitted action-local storage safeguards; do **not** invent a transaction, overwrite fallback, rollback promise, retry, resume **or** new lock/concurrent-publication protocol. retain the approved exclusive-window safeguards above; no live cleanup **or** production activation follows from this source amendment. unsupported **or** unprovable safe realization is a blocker, **not** permission **to** weaken the boundary. these are required contracts, **not** implementation **or** independent acceptance.
