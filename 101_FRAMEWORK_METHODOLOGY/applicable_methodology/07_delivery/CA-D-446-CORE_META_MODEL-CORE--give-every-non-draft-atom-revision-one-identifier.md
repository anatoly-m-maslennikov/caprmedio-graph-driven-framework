---
subjects:
  governs: "Entity/Continuant/History/Revision.Identity"
  depends_on:
    ["Entity/Continuant/Object/Atom.ID", "Entity/Continuant/Object/Atom.Version Number", "Entity/Continuant/Object/Atom.Status: Draft"]
version: 12
updated_at: "2026-10-16 12:09:30 +0000"
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
  source_atom_revision: 12
  source_sha256: fcdd312b99767d7652faedba51a1e1e6612bf65855e56fe224bb53f24b27e667
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
- when an identified Atom is changed to Draft, remove `atom_id` from the resulting Draft Carrier's complete frontmatter **and** its assigned filename number under CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number; do **not** create a second concurrent Draft Carrier for that Status edit.
- preserve the exact prior identified Revision as history, including its old Version, Status and Updated At. An actual Status edit, including demotion to Draft, advances the current Version from N to N+1 with actual edit time under CA-R-1432/CA-R-1788; an exact no-op retains Version/time. There is no demotion Version exception.
- every ID-free Draft later leaving Draft receives a fresh next-unreused Atom Identity under CA-D-508, even when a Tool previously demoted it. Historical identity/lineage is retained as fact, not restored as that Draft's assigned ID or released for reuse.

## Details

### Subjects-only edit draft of an existing Atom

A Subjects-only edit draft of an existing identified Atom is a derived proposal for that Atom's next Revision, not another canonical original, a new Atom Draft, or a demotion of the current Revision. It is admitted only with an explicit canonical target and exact current ID/Version/SHA-256 source pin retained by the reviewed batch packet. The canonical current Carrier remains untouched during staging. This narrowly scoped proposal carries `atom_id` equal to the canonical ID plus the exact suffix `@draft` and `status: Draft`; that temporary proposal ID is not an assigned canonical Atom Identity, a new Type, or a globally valid canonical ID/reference syntax.

Its filename replaces the source's canonical ID once with that temporary proposal ID in the owning role's `draft/` folder. Bind the complete proposed bytes and safe path/digest to the reviewed packet. Apart from the declared Subjects, temporary ID/Status and proposed Version/time, preserve the source's complete metadata and body bytes. A changed proposal shows N+1 and illustrative Updated At; a true no-op retains the source Version/time behind its temporary proposal markers.

Approval rechecks the exact canonical source-before and reviewed draft bytes. Normalize only the temporary ID and Draft marker back to the pinned canonical ID and original Status, and materialize actual Updated At for a changed update. Require equality with independently validated fresh Subjects-only canonical materialization before the existing updater archives the exact current predecessor and publishes N+1. Preserve original Status and every other unrelated byte; do not allocate identity, perform a lifecycle Status transition, infer identity from a suffix alone, or bypass current source validation. A changed source or proposal refuses rather than silently rebinding approval. Existing low-level effect/restoration handling remains.

New-Atom Drafts and ordinary lifecycle Draft demotion/update/identification retain their ID-free filename and applicable identity rules, without a retained Draft-history entry, lineage/head/origin chain or consuming-successor prerequisite under CA-D-568/CA-D-570. Removing those prerequisites does not waive schema, identity/collision, expected-target/currentness, permission or exact actual-history safeguards. This exception supplies no general assigned-ID Draft admission and does not change canonical Atom ID grammar.
