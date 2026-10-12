---
atom_id: CA-R-1941
content_role: Requirement
type: Requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Artifact/Carrier","Action","Workflow","Atom","Operator"]
version: 1
updated_at: "2026-10-13 01:46:23 +0400"
relations:
  relates_to: [CA-R-1936, CA-R-1093, CA-M-381, CA-E-633, CA-D-630, CA-O-215, CA-O-216, CA-O-217, CA-O-040]
---
# Summary

Bound private carrier storage changes

## Scope

Private file/folder rename, move and non-Atom cleanup mechanics behind the logical connector interface. The required result is one explicitly approved carrier storage change, with independently verified before/after evidence and no widened effect.

## Claim

A private carrier change **must** be bound to one logical request under CA-R-1936 and CA-D-625's supported `modify` operation. Rename, move and remove are private adapter variants, not new common verbs or public physical-path operations. The owning Workflow supplies domain policy, schema, identity, Version/time, lifecycle and authorization; the helper performs only the exact selected storage change.

The private binding **must** identify the source carrier, file/folder kind, approved source and destination roots where applicable, expected source state, explicit destination and expected absence where applicable. Paths remain private resolved binding data. The selected root itself, a filesystem/Project root, an ancestor containing either root, an escaping path, symlink or substituted source/destination/ancestor **must not** be affected. Required source, parent, destination and permission evidence must be current at the effect boundary.

Rename changes only the explicitly supplied name within the same parent. Move uses the explicitly supplied destination; any basename change must already be explicit, not inferred. Both **must** preserve carrier content, declared modes/metadata and unrelated entries, except separately supplied Workflow-owned changes outside this helper's location-only contribution. For an actual rename/move, the distinct destination must be absent; existing distinct destinations, collisions, overwrite or merge requests are rejected. A verified same-binding no-op is not an overwrite. A folder rename/move requires a complete finite approved entry inventory; missing, added, substituted or unlisted entries fail rather than enlarging the admitted frontier. A folder move destination inside the selected source subtree, or any other invalid source/destination overlap, is rejected; verified identical-binding no-op remains distinct. No automatic recursive selection is admitted.

Remove **must** be separately approved non-Atom storage cleanup of one file or one empty folder. A nonempty folder, uncertain classification, Atom/current/historical carrier, required history, protected source or unapproved cleanup target is rejected. There is no delete-Atom operation. Cleanup neither follows symlinks nor enumerates descendants into a removal set. An existing admitted Atom lifecycle operation may use a private carrier move only through its exact admitted lifecycle/currentness/history context; the helper cannot substitute for Archive, retire, replacement or authority admission.

The result **must** follow CA-D-625's `data/current_state/effects/errors` roles. Success requires independent verification of this variant's declared postconditions. Unknown effects require `effect_uncertain`; nonempty errors are not success, even with known partial effects. Empty errors cannot mean merely that no exception occurred. A no-op requires verified requested state already satisfied and unchanged; a missing expected-present source is not an inferred completed rename/move/remove.

## Details

CA-M-381 supplies binding construction; CA-D-630 binds representation; CA-O-215/216/217 define the three reusable Actions; CA-E-633 supplies falsifiable cases. CA-O-040 is different: its generic Artifact rename includes canonical-reference rewrites. These private helpers never discover or rewrite references, create domain identity or report a logical lifecycle operation completed from a storage effect alone.

Retain existing admitted action-local storage safeguards; do not invent a transaction, overwrite fallback, rollback promise, retry, resume, lock or concurrent-publication protocol. Unsupported or unprovable safe realization is a blocker, not permission to weaken the boundary. These are required contracts, not implementation or independent acceptance.
