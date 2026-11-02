---
subjects:
  governs: "Entity/Node/Continuant/Atom.ID"
  depends_on:
    ["Entity/Node/Continuant/Atom.Version Number", "Entity/Node/Continuant/Atom.Status: Draft"]
version: 16
updated_at: "2026-10-20 21:17:32 +0400"
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

For each canonical Atom ID, at most one Current Atom source **may** exist across all admitted Status values. Every Current or Archived Atom version **must** be identified by exactly one canonical Atom ID and Version Number; Archived versions **may** retain that ID at distinct Version Numbers. A Draft Atom **may** omit or carry an `atom_id`. A carried Draft source may use only the marker forms specified by CA-D-378; a Current source uses the canonical ID. Exact archived predecessor bytes remain governed by actual-history preservation and are not normalized by this rule.

- for a Current or Archived Atom version, carry the canonical Atom ID as the top-level String `atom_id` **and** Version Number as `version`; their pair identifies one Atom version **without** another `identifier` field. Draft `atom_id` presence and marker form follow the Claim and CA-D-378.
- a Draft Carrier may omit or carry `atom_id` using only the Draft marker forms admitted by CA-D-378. These forms do not change the Current Atom ID uniqueness rule.
- when an identified Atom is changed to Draft, its Draft Carrier may omit `atom_id` or carry a Draft marker admitted by CA-D-378; any carried marker and filename remain governed by CA-D-378 and CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number. Do **not** create a second concurrent Draft Carrier for that Status edit.
- preserve the exact prior identified Revision as history, including its old Version, Status and Updated At. An actual Status edit, including demotion to Draft, advances the current Version from N to N+1 with actual edit time under CA-R-1432/CA-R-1788; an exact no-op retains Version/time. There is no demotion Version exception.
- every ID-free Draft later leaving Draft receives a fresh next-unreused Atom Identity under CA-D-508, even when a Tool previously demoted it. Historical identity/lineage is retained as fact, not restored as that Draft's assigned ID or released for reuse.

## Details

### Draft Atom Identity

Draft Atom ID presence and permitted marker forms are as stated in the Claim and CA-D-378.

New-Atom Drafts and ordinary lifecycle Draft demotion/update/identification may omit or carry an Atom ID under this rule, using only marker forms admitted by CA-D-378; their filenames follow CA-D-288. A Draft marker does not change the existing Current Atom uniqueness rule. These rules do not prescribe a new ID restoration or allocation default when a Draft leaves Draft. The absence of retained Draft-history entry, lineage/head/origin chain or consuming-successor prerequisite under CA-D-568/CA-D-570 does not waive schema, identity/collision, expected-target/currentness, permission or exact actual-history safeguards.
