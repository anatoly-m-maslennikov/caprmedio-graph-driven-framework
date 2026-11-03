---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.ID
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Version Number
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Status: Draft'
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-446
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-446-CORE_META_MODEL-ENG_DECISION--give-every-non-draft-atom-revision-one-identifier.md
  source_atom_id: CA-D-446
  source_atom_revision: 28
  source_sha256: a364257a7ff40d31aa675ec6aeb64191dada692461b95af8207efe057cd7bd3b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Give Every Non-Draft Atom Revision One Identifier

## Claim scope

Current Atom sources, Archived Atom versions and Draft Atom sources.

## Claim

For each canonical Atom ID, at most one Current Atom source **may** exist across all admitted Status values. Every Current or Archived Atom version **must** be identified by exactly one canonical Atom ID and Version Number; Archived versions **may** retain that ID at distinct Version Numbers. Every Draft Atom **must** carry one `atom_id` marker form specified by CA-D-378; a Current source uses the canonical ID. An Archived predecessor is identified by its canonical ID qualified once with its unchanged numeric Version, with `status: Archived` and its prior Updated At retained; Git history preserves exact pre-archive bytes.

- for a Current or Archived Atom version, carry the canonical Atom ID as the top-level String `atom_id` **and** Version Number as `version`; their pair identifies one Atom version **without** another `identifier` field. A Draft carries only the explicit marker allowed by the Claim and CA-D-378.
- a Draft Carrier **must** carry `atom_id` using only the Draft marker forms admitted by CA-D-378. These forms do not change the Current Atom ID uniqueness rule.
- when an identified Atom is changed to Draft, its Draft Carrier carries the corresponding Draft marker admitted by CA-D-378; the marker and filename remain governed by CA-D-378 and CA-D-650. Do **not** create a second concurrent Draft Carrier for that Status edit.
- when a Current Atom changes, create an Archive Carrier for the predecessor with its qualified ID, `status: Archived`, unchanged numeric Version and old Updated At; the Current successor retains the canonical ID, advances Version from N to N+1, and receives actual edit time under CA-R-1432/CA-R-1788. An exact no-op retains Version/time. There is no demotion Version exception.
- a Draft carrying `<canonical-ID>@<proposed-version>-draft` for an existing Atom proposes an update to that same canonical Atom at the marker's proposed Version. For an actual update, that Version must be the current canonical Version plus one under the existing version-advance rule; archive the current canonical predecessor with its old numeric Version, Updated At and unrelated content, and update that Atom, subject to exact-current, identity/collision, Summary/replacement, Type/Status, schema and permission rules. An exact no-op retains the existing Version/time and creates no predecessor archive. This same-canonical rule does not determine promotion behavior for the role-only new-Atom marker.

## Details

### Draft Atom Identity

Draft Atom ID is mandatory. Its marker form is as stated in the Claim and CA-D-378.

New-Atom Drafts and ordinary lifecycle Draft demotion/update/identification carry the marker admitted by CA-D-378; their filenames follow CA-D-650. A Draft marker does not change the existing Current Atom uniqueness rule. For a Draft marked `<canonical-ID>@<proposed-version>-draft`, promotion proposes an update to the same canonical Atom at the proposed Version, subject to the ordinary currentness, schema, identity/collision, permission, Summary/replacement and change-class rules. Draft identity continuity does not require a retained-history entry, lineage/head/origin chain or consuming successor under CA-D-568/CA-D-570.
