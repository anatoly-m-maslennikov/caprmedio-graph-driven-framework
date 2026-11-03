---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection
version: 31
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1697
  - CA-R-1708
atom_id: CA-R-1706
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1706-CORE_META_MODEL-RULE--requirement-provide-lineage-impact-projections.md
  source_atom_id: CA-R-1706
  source_atom_revision: 31
  source_sha256: 7d5e88d52512069ef8fefd312145828570dd6d9cb41dbabc58a27d5cfe7d8fbb
  original_relations_sha256: ec206373bb2bfa199e89267d9f9e280ebe9b270bcd727dc38c82ef3f579a8f02
---
## Summary

Requirement — Provide lineage-impact Projections

## Claim scope

lineage-impact Projections for changed, replaced, or archived Atom revisions.

## Claim

CAPRMEDIO provides a non-authoritative lineage-impact Projection whenever an upstream Atom revision is changed, replaced, **or** archived. the Projection derives the reachable descendant set **without** modifying **or** retargeting **any** persisted relation.

for **every** affected descendant, the Projection identifies the exact earlier revision **in** its lineage, the upstream event that triggered review, **and** the current disposition: review required, update the existing Atom, create a new Atom, archive the Atom, **or** confirmed compatible **without** change. unresolved descendants remain visible **until** disposition is recorded through governed history.

the Projection **may** group **and** prioritize work, but it **must not** change an Atom, break a historical link, **or** establish compatibility merely by listing it.

## Primary claim

a changed, replaced, **or** archived ancestor produces a derived review surface for **every** affected descendant while historical lineage remains intact.
