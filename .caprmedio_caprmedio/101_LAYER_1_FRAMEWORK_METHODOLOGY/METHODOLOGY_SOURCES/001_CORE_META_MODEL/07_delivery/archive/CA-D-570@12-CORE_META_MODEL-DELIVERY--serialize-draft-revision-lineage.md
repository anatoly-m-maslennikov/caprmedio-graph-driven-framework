---
subjects:
  governs: "Entity/Node/Continuant/Atom.Status: Draft"
  depends_on:
    ["Entity/Node/Continuant/Atom.ID", "Entity/Node/Continuant/History/Revision.Identity", "Entity/Node/Continuant/Atom.Status: Draft", "Entity/Node/Continuant/History/Revision", "Entity/Node/Continuant/Atom.Version Number", "Entity/Node/Continuant/Atom/Content Role"]
version: 12
updated_at: "2026-10-20 21:18:18 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-507
    - CA-D-508
    - CA-D-568
atom_id: "CA-D-570@12"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Draft Revision Lineage

## Scope

the recorded lineage metadata of a Project-owned Draft Atom Carrier, when it already exists.

## Claim

A Draft Atom **must not** require `revision_lineage`, a retained Draft-history entry or a trusted Draft head for Create, Update, promotion, another admitted Status change or their success. A Draft Carrier may omit or carry an Atom ID under CA-D-446; its filename follows CA-D-288.

Existing `revision_lineage: {history_entry_ref: {history_revision, path}}` metadata and the actual retained records it references may remain as recorded historical data. Their presence, absence, encoding, resolvability, origin, parent chain, head/leaf status or consuming-successor state **must not** become a mutation or completion gate. Do **not** require a caller or writer to register, reconstruct, repair, reserve, append or consume such a record to admit the current operation.

Retain real exact predecessor bytes and actual historical records under their applicable Delivery rules; do **not** fabricate history or reinterpret an observed value as evidence of an event that was not observed. Every ID-free Draft leaving Draft receives a fresh next-unreused Identity under CA-D-508, including a tool-demoted Draft; existing lineage or history never restores a former assigned ID. Preserve the exact admitted target, ordinary Summary/replacement rules, applicable schema, collision/currentness checks and permissions. No new identity registry, history writer, recovery framework or Journal protocol is introduced.

## Details

CA-D-568 binds identity continuity without a retained-history prerequisite. Journal existence, completeness, baseline, chain, prior entry or receipt does not grant permission or gate mutation success. An actual append attempt reports its own I/O result independently and never replays the performed effect.

### Subjects-only edit-draft exception

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry `atom_id: <canonical-ID>@<proposed-version>-draft` (preferred) or the compatible `atom_id: <canonical-ID>@draft`, `status: Draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts may omit or carry an Atom ID under CA-D-446; marker and filename rules remain governed by CA-D-378 and CA-D-288. Canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
