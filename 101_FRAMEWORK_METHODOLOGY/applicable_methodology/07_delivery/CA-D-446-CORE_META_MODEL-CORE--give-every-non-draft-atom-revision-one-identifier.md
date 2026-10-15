---
subjects:
  governs: "Atom/Revision/Identifier"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Version"
    - "Atom/Revision/Status: Draft"
version: 8
updated_at: "2026-10-15 10:01:40 +0000"
relations:
  relates_to:
    - CA-D-378
    - CA-D-292
atom_id: "CA-D-446"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-446-CORE_META_MODEL-CORE--give-every-non-draft-atom-revision-one-identifier.md
  source_atom_id: CA-D-446
  source_atom_revision: 8
  source_sha256: a04eb16d411594afb88d8c1925072328bad8c41771b835c02e4903b6d12fb3e9
  original_relations_sha256: b17be253479843ef6dd3db281ba4b0df0d9ef1c54b95463e807c1b4fdfc085bd
---
# Summary

Give Every Non-Draft Atom Revision One Identifier

## Scope

non-Draft Atom Revisions and Draft Carriers.

## Claim

**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version.

- carry the assigned Atom Identity as the top-level String `atom_id` **and** Version as `version`; their pair identifies this Revision **without** another `identifier` field.
- outside the explicit Subjects-only edit-draft exception below, a Draft Carrier **must not** carry an assigned `atom_id`; a filename, path, **or** temporary locator **must not** silently allocate one.
- when an identified Atom is changed to Draft, its Draft Carrier remains a Revision of that same Atom: remove `atom_id` from the Draft Carrier's complete frontmatter **and** its assigned filename number under CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number; do **not** create another Draft Atom **or** represent the change as a replacement.
- preserve that Draft Revision's Summary, meaning, Version, **and** identified predecessor history. this rule does **not** allocate **or** reuse an Atom Identity for a later Revision leaving Draft.

## Details

### Subjects-only edit draft of an existing Atom

A Subjects-only edit draft of an existing identified Atom is a derived proposal for that Atom's next Revision, not another canonical original, a new Atom Draft, or a demotion of the current Revision. It is admitted only with an explicit canonical target and exact current ID/Version/SHA-256 source pin retained by the reviewed batch packet. The canonical current Carrier remains untouched during staging. This narrowly scoped proposal carries `atom_id` equal to the canonical ID plus the exact suffix `@draft` and `status: Draft`; that temporary proposal ID is not an assigned canonical Atom Identity, a new Type, or a globally valid canonical ID/reference syntax.

Its filename replaces the source's canonical ID once with that temporary proposal ID in the owning role's `draft/` folder. Bind the complete proposed bytes and safe path/digest to the reviewed packet. Apart from the declared Subjects, temporary ID/Status and proposed Version/time, preserve the source's complete metadata and body bytes. A changed proposal shows N+1 and illustrative Updated At; a true no-op retains the source Version/time behind its temporary proposal markers.

Approval rechecks the exact canonical source-before and reviewed draft bytes. Normalize only the temporary ID and Draft marker back to the pinned canonical ID and original Status, and materialize actual Updated At for a changed update. Require equality with independently validated fresh Subjects-only canonical materialization before the existing updater archives the exact current predecessor and publishes N+1. Preserve original Status and every other unrelated byte; do not allocate identity, perform a lifecycle Status transition, infer identity from a suffix alone, or bypass current source validation. A changed source or proposal refuses rather than silently rebinding approval. Existing low-level effect/restoration handling remains.

New-Atom Drafts and ordinary lifecycle Draft demotion/update/identification retain their ID-free filename and retained-lineage rules. This exception supplies no general assigned-ID Draft admission and does not change canonical Atom ID grammar.
