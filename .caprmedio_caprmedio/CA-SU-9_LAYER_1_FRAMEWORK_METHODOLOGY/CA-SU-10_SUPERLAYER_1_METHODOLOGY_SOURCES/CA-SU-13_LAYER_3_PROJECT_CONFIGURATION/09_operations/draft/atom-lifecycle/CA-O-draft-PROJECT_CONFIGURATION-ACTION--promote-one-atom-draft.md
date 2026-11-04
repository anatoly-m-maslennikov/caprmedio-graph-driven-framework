---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Promote one Atom Draft

## Claim scope

This Action publishes one exact selected Draft for one non-container Atom under the applicable model. It rejects containers, descendants, cascades, implicit archival, and overwrites.

## Claim

Read the selected Draft and validate its unchanged selection, Draft status, marker identity/version, content, applicable model, explicit Current Status, destination, authorization, schema, mandatory fields, collision, and no-overwrite. Do not require a predecessor to remain Current.

For an existing-Atom marker, use its canonical ID and proposed Version. For a role-only Draft, allocate a fresh canonical ID and publish Version 1. Publish the Draft's content with the supplied Status and publication-time Updated At. Save and read back the Current carrier before deleting the Draft.

Return the publication, or the explicit error with completed outputs under [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md). Journal append is independent and nonblocking.
