---
atom_id: CA-D-570
ref_id: CA-D-570
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Status:Draft
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
  - CAPRMEDIO_MODEL <+ Atom.Header.Status:Draft
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
tier: 3
status: active
version: 26
updated_at: 2026-11-09 00:57:07 +0400
carrier_destination:
  file:
    name: CA-D-570-CORE_META_MODEL-DECISION--serialize-draft-revision-lineage.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize Draft Revision Lineage

## Claim

### Prose Claim


the recorded lineage metadata of a Project-owned Draft Atom Carrier, when it already exists.


A Draft Atom **must not** require `revision_lineage`, a retained Draft-history entry or a trusted Draft head for Create, Update, promotion, another admitted Status change or their success. Every Draft Carrier carries the mandatory Draft `atom_id` marker under CA-D-378/CA-D-446; its filename follows CA-D-650.

Existing `revision_lineage: {history_entry_ref: {history_revision, path}}` metadata and the actual retained records it references may remain as recorded historical data. Their presence, absence, encoding, resolvability, origin, parent chain, head/leaf status or consuming-successor state **must not** become a mutation or completion gate. Do **not** require a caller or writer to register, reconstruct, repair, reserve, append or consume such a record to admit the current operation.

When a Current Atom changes, archive its predecessor with the old numeric Version and Updated At, an Archived status and a version-qualified identity under CA-D-446/CA-D-565; the Current successor follows the normal Version and timestamp rules. Do **not** fabricate history or reinterpret an observed value as evidence of an event that was not observed. Preserve the exact admitted target, ordinary Summary/replacement rules, applicable schema, collision/currentness checks and permissions. No new identity registry, history writer, recovery framework or Journal protocol is introduced.

## Details

CA-D-568 binds identity continuity without a retained-history prerequisite. Journal existence, completeness, baseline, chain, prior entry or receipt does not grant permission or gate mutation success. An actual append attempt reports its own I/O result independently and never replays the performed effect.

### Subjects-only edit-draft exception

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It carries the admitted `<canonical-ID>@<proposed-version>-draft` ID marker at its declared Header path, logical Draft Status encoded as `draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and archives the old predecessor identity/version under the ordinary archive rules before the N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry a marker under CA-D-378/CA-D-446; filename rules are governed by CA-D-650. Canonical ID grammar and the normal source, schema, identity/collision, permission and actual-history safeguards are unchanged.
