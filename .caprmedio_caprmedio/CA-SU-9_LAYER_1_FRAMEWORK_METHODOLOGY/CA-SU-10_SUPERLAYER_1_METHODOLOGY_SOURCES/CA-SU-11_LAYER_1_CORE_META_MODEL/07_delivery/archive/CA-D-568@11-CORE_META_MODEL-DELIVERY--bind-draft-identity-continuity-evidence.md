---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.ID
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom.Status: Draft'
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Domain/Node/Continuant/Atom
version: 11
updated_at: 2026-10-24 01:50:12 +0400
relations:
  depends_on:
  - CA-D-650
  relates_to:
  - CA-D-378
  - CA-D-446
  - CA-D-507
  - CA-D-508
  - CA-D-569
  - CA-D-570
atom_id: CA-D-568@11
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
type: Eng Decision
author: Anatoly Maslennikov
tier: 3
---
# Summary

Bind Draft Identity Continuity Evidence

## Scope

identity continuity when a Draft Atom is created, updated or admitted to a non-Draft Status.

## Claim

Draft identity continuity **must** follow the exact admitted target and the applicable identity rules; retained Draft history **must not** be a prerequisite for Create, Update, promotion, another admitted Status change or their success.

- do **not** require, reconstruct, register, resolve or validate a `revision_lineage.history_entry_ref`, unique Draft head, origin chain, direct retained-history parent, pending head reservation or consuming successor before an otherwise admitted effect. A manually authored Draft is not refused merely because those records are absent, incomplete, malformed or unavailable.
- Draft `atom_id` presence and marker form follow CA-D-378 and CA-D-446; Draft filename identity-segment serialization follows CA-D-650. Do **not** restore a former assigned Identity from an archive, lineage/origin metadata, Journal, prior tool demotion or another historical record. Preserve real historical identities without releasing them for reuse. Ordinary Content Role, Summary/replacement, identity/collision, expected-target/currentness, permission and Carrier/schema checks remain applicable; absence of retained Draft history is not itself an identity conflict.
- When a Current Atom revision is updated, preserve the predecessor's old numeric Version, Updated At and unrelated content while archiving it with `status: Archived` and the version-qualified identity; exact pre-archive bytes remain in Git history. Do **not** fabricate a Create event, origin, earlier Draft admission, head, parent or successor to make the current operation admissible. A Summary change still follows the admitted replacement rule.
- Journal existence, completeness, continuity, baseline, prior entry or receipt **must not** gate these effects or their success. Attempt to append supplied actual observations independently; report an actual append failure as a diagnostic without invalidating a completed mutation or replaying its effects.

## Details

Existing retained-history records remain actual history, not an admission capability or a required identity registry. Their absence does not require retrospective Operator reauthoring or a manual-Draft exception. The source-pinned Subjects-only proposal below remains a derived edit of its explicitly bound canonical target.

### Subjects-only edit-draft exception

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It carries `atom_id: <canonical-ID>@<proposed-version>-draft`, `status: Draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and archives the predecessor with its prior numeric Version and Updated At under CA-D-565 before the N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry a marker under CA-D-378/CA-D-446; marker and filename rules are governed by CA-D-650. Canonical ID grammar and the normal source, schema, identity/collision, permission and actual-history safeguards are unchanged.
