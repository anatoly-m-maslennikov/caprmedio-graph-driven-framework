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
version: 1
updated_at: "2026-10-20 16:58:30 +0400"
---
# Summary

Align edit-draft markers with no-ID Draft identity

## Concern

The legacy edit-draft staging representation uses an Atom ID-like @draft marker, while the latest human model decision says a Draft has no Atom ID. The Methodology source alignment and the representation change must be settled together; do not publish held drafts as compliant or infer a new identity system from their filenames.

## Evidences

Epic CA-P-1959 v124 retains the latest approved Draft/Current/Archived group decision and the no-ID Draft rule. The Methodology owner confirmed no source effect is running, the five held edit-drafts remain unpublished, and narrowing lifecycle source proposals are scratch-only, not new active authority. Existing held carrier filenames include CA-R-1016@draft, CA-R-1017@draft, CA-R-1019@draft, CA-R-1021@draft and CA-R-1472@draft. Their concrete representation requires reconciliation against active Draft identity/staging contracts before changing implementation.

The three lifecycle groups do not by themselves authorize removing Draft or Archived serialized Status values. Current-only relation targeting likewise does not choose an incoming-link cleanup or archive gate. No such additional policy is inferred.

## Blast radius

Affected edit-draft staging/publication and promotion may misrepresent Draft identity. This is a separate bounded source-and-implementation follow-up, not a parser fix or authority to replay, delete, reset or publish the held drafts. Preserve their captured evidence and the stopped batch. The approved runtime release does not claim this mismatch is repaired.
