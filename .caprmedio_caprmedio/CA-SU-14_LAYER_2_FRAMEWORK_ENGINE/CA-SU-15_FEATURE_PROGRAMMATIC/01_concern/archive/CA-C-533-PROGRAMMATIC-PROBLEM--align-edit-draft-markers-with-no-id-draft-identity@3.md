---
atom_id: CA-C-533
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-1959, CA-D-446]
version: 3
updated_at: "2026-10-20T18:47:15.122Z"
---
# Summary

Resolve Draft marker and same-identity promotion contracts

## Concern

The initial mismatch is narrowed, but the Engine contracts must consistently implement the published Draft forms: optional `atom_id` and ID-free empty-number Drafts, `CA-R-draft`/role-draft markers for new Atoms, version-qualified `<canonical-ID>@<proposed-version>-draft` edit markers, and legacy `<canonical-ID>@draft` compatibility. A marker is Draft-only proposal metadata, not a canonical identity. Existing-marker promotion must update the same canonical Atom at the explicit carried/requested Version, archive the exact current predecessor, and refuse stale target/version/digest bindings.

## Evidences

Current implementation review has confirmed two bounded remaining defects: same-path failed-promotion recovery must refuse to overwrite an intervening canonical edit (P2475), and legacy/ID-free reviewed Drafts must reject carried Version drift before normalization (P2476). P2474 fresh native Status normalization passed 8 native cases and 20 owner promotion golden checks; P2472 Done-to-Active placement and ordinary recovery checks passed. P2473 qualified-marker Version mismatch is fixed. These focused results do not close the remaining review findings or prove deployed support. Keep this Problem Active pending the bounded fixes, independent matrix and review; no held carrier or failed Run is replayed.

Epic CA-P-2401 v18 and the current Core delivery rules retain the Draft/Current/Archived distinction, with no retained Draft-history or Journal gate. Existing held carrier filenames include CA-R-1016@draft, CA-R-1017@draft, CA-R-1019@draft, CA-R-1021@draft and CA-R-1472@draft. Their concrete representation still requires reconciliation against the active marker and same-identity promotion contracts before changing implementation; this Problem remains Active until the focused Engine tests establish it.

The three lifecycle groups do not by themselves authorize removing Draft or Archived serialized Status values. Current-only relation targeting likewise does not choose an incoming-link cleanup or archive gate. No such additional policy is inferred.

## Blast radius

Affected edit-draft staging/publication and promotion may misrepresent Draft identity or overwrite a stale canonical predecessor. This is a separate bounded source-and-implementation follow-up, not authority to replay, delete, reset or publish the held drafts. Preserve their captured evidence and the stopped batch. The approved runtime release does not claim this Problem is repaired.
