---
subjects:
  governs: "Entity/Node/Continuant/Atom.ID"
  depends_on:
    ["Entity/Node/Continuant/Atom.Version Number", "Entity/Node/Continuant/Atom.Status: Draft"]
version: 15
updated_at: "2026-10-20 17:07:56 +0400"
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
---
# Summary

Give Every Non-Draft Atom Revision One Identifier

## Scope

Current Atom sources, Archived Atom versions and Draft Atom sources.

## Claim

For each canonical Atom ID, at most one Current Atom source **may** exist across all admitted Status values. Every Current or Archived Atom version **must** be identified by exactly one canonical Atom ID and Version Number; Archived versions **may** retain that ID at distinct Version Numbers. Every Draft Atom source **must** have no Atom ID.

- carry the canonical Atom ID as the top-level String `atom_id` **and** Version Number as `version`; their pair identifies one Atom version **without** another `identifier` field.
- a Draft Carrier **must not** carry an assigned or temporary `atom_id`; a filename, path **or** temporary locator **must not** silently allocate one.
- when an identified Atom is changed to Draft, remove `atom_id` from the resulting Draft Carrier's complete frontmatter **and** its assigned filename number under CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number; do **not** create a second concurrent Draft Carrier for that Status edit.
- preserve the exact prior identified Revision as history, including its old Version, Status and Updated At. An actual Status edit, including demotion to Draft, advances the current Version from N to N+1 with actual edit time under CA-R-1432/CA-R-1788; an exact no-op retains Version/time. There is no demotion Version exception.
- every ID-free Draft later leaving Draft receives a fresh next-unreused Atom Identity under CA-D-508, even when a Tool previously demoted it. Historical identity/lineage is retained as fact, not restored as that Draft's assigned ID or released for reuse.

## Details

### Existing temporary-ID exception

Draft identity rules have no temporary-ID exception. Existing source validation, permissions and exact history preservation still apply.

New-Atom Drafts and ordinary lifecycle Draft demotion/update/identification retain their ID-free filename and applicable identity rules, without a retained Draft-history entry, lineage/head/origin chain or consuming-successor prerequisite under CA-D-568/CA-D-570. Removing those prerequisites does not waive schema, identity/collision, expected-target/currentness, permission or exact actual-history safeguards. This exception supplies no general assigned-ID Draft admission and does not change canonical Atom ID grammar.
