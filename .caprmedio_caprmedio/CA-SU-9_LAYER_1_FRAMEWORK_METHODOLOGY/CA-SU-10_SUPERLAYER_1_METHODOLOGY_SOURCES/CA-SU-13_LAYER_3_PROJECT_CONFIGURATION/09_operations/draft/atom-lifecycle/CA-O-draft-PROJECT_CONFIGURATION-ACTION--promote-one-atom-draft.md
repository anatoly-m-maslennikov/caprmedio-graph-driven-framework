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

**Preconditions:** Read the exact Draft and validate its complete content/Role, mandatory fields, Draft status, applicable model, explicit Current Status, destination, expected saved-source/currentness, permission, schema, `targetID`, `targetVersion`, collision, and no-overwrite. In a composed Update use the prepared ID/version and original Current Status captured before archival; no archive receipt, history recovery, implicit archive, ID replacement, or second ID is admitted. Never default the Status to `Active`.

**Intended effect:** Publish the exact selected ID with the proposal's content/meaning, explicit Current Status, and publication-time Updated At. Existing-Atom intent uses its exact proposed Version, normally N+1; new-Atom or Summary/Role replacement uses the selected ID at canonical Version 1 even when Draft Version is greater than 1.

**Returned evidence:** Save and read back the Current carrier, destination, identity/version, collision state, and equality to the supplied Status; only then delete the Draft. Return the publication or an explicit error/partial result with actual completed outputs. Do not retry, replay, repair, or perform a rollback. Journal business-event append is independent and nonblocking.
