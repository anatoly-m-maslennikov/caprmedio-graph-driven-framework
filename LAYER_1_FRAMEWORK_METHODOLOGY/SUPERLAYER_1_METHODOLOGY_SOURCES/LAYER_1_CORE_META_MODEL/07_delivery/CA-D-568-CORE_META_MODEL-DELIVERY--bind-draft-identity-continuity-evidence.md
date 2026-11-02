---
subjects:
  governs: "Atom/Revision/Status: Draft/Identity Continuity Evidence"
  depends_on:
    - "Atom/Identity"
    - "Atom/Identifier"
    - "Atom/Revision/Identifier"
    - "Atom/Revision/Status: Draft"
    - "Atom/Revision/Version"
    - "Atom/Revision/History"
    - "Tool/Workflow Operations/Atom Lifecycle/Request Parameters"
version: 8
updated_at: "2026-10-20 21:17:55 +0400"
relations:
  relates_to:
    - CA-D-288
    - CA-D-378
    - CA-D-446
    - CA-D-507
    - CA-D-508
    - CA-D-569
    - CA-D-570
atom_id: "CA-D-568"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Draft Identity Continuity Evidence

## Scope

identity continuity when a Draft Atom is created, updated or admitted to a non-Draft Status.

## Claim

Draft identity continuity **must** follow the exact admitted target and the applicable identity rules; retained Draft history **must not** be a prerequisite for Create, Update, promotion, another admitted Status change or their success.

- do **not** require, reconstruct, register, resolve or validate a `revision_lineage.history_entry_ref`, unique Draft head, origin chain, direct retained-history parent, pending head reservation or consuming successor before an otherwise admitted effect. A manually authored Draft is not refused merely because those records are absent, incomplete, malformed or unavailable.
- **every** ID-free Draft leaving Draft receives a fresh next-unreused Atom Identity under CA-D-508, including a Draft produced by demoting a previously identified Atom. Do **not** restore its former assigned Identity from an archive, lineage/origin metadata, Journal, prior tool demotion or another historical record. Preserve real historical identities without releasing them for reuse. Ordinary Content Role, Summary/replacement, identity/collision, expected-target/currentness, permission and Carrier/schema checks remain applicable; absence of retained Draft history is not itself an identity conflict.
- retain exact actual predecessor bytes and real historical records under their applicable Delivery rules. Do **not** fabricate a Create event, origin, earlier Draft admission, head, parent or successor to make the current operation admissible. A Summary change still follows the admitted replacement rule.
- Journal existence, completeness, continuity, baseline, prior entry or receipt **must not** gate these effects or their success. Attempt to append supplied actual observations independently; report an actual append failure as a diagnostic without invalidating a completed mutation or replaying its effects.

## Details

Existing retained-history records remain actual history, not an admission capability or a required identity registry. Their absence does not require retrospective Operator reauthoring or a manual-Draft exception. The source-pinned Subjects-only proposal below remains a derived edit of its explicitly bound canonical target.

### Subjects-only edit-draft exception

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry `atom_id: <canonical-ID>@<proposed-version>-draft` (preferred) or the compatible `atom_id: <canonical-ID>@draft`, `status: Draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts may omit or carry an Atom ID under CA-D-446; marker and filename rules remain governed by CA-D-378 and CA-D-288. Canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
