---
atom_id: CA-C-533@4
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-1959, CA-D-446]
version: 4
updated_at: "2026-10-20T19:10:44.040Z"
---
# Summary

Align edit-draft markers with no-ID Draft identity

## Concern

The source correction is implemented and verified, but installed runtime adoption remains outside this increment. The published Draft forms are: optional `atom_id` and ID-free empty-number Drafts, `CA-R-draft`/role-draft markers for new Atoms, version-qualified `<canonical-ID>@<proposed-version>-draft` edit markers, and legacy `<canonical-ID>@draft` compatibility. A marker is Draft-only proposal metadata, not a canonical identity. Existing-marker promotion must update the same canonical Atom at the explicit carried/requested Version, archive the exact current predecessor, and refuse stale target/version/digest bindings.

## Evidences

The six original Core deliveries and Engine RMEDO now agree on Draft-only markers and no retained-history/Journal admission gate. Independent frozen checks passed validator 542, CLI E2E 28, native promotion 8, marker formats 6, model lifecycle 20, exact pins 1 and full promotion 22. Staging passed focused 16, contract 5 and workflow 10. Same-path concurrent-edit preservation, exact predecessor bytes, Done-to-Active child bundles, strict Version bindings and mutation-free no-op were independently reviewed. The older parser cohort was corrected as a fixture/obsolete expectation issue and passed all 30; no production guard was weakened.

These are source/host proofs only. No release, deployment, installed mirror refresh, migration or held-Draft publication occurred. The installed 0.4.4.8 runtime has not been activated with this increment, so this Problem remains Active for separately authorized runtime adoption and reconciliation of held carriers CA-R-1016@draft, CA-R-1017@draft, CA-R-1019@draft, CA-R-1021@draft and CA-R-1472@draft. Preserve their captured evidence and the stopped batch; do not replay or reset it.

## Blast radius

Affected edit-draft staging/publication and promotion may misrepresent Draft identity or overwrite a stale canonical predecessor. This is a separate bounded source-and-implementation follow-up, not authority to replay, delete, reset or publish the held drafts. Preserve their captured evidence and the stopped batch. The approved runtime release does not claim this Problem is repaired.
