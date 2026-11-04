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

Archive one Current Atom

## Claim scope

This Action operates on one exact selected non-container Current Atom. Archived inputs, containers, descendants, inferred replacements, and overwrites are invalid.

## Claim

**Preconditions:** Resolve the exact Current source and validate required fields, applicable model/status for `Archived`, currentness, placement, permissions, collision, and no-overwrite. An optional known `targetID` is business-observation context only and does not change the archive target or assert publication. Wrong input returns an explicit error before writing.

**Intended effect:** For Current version N, write `ID@N` with status `Archived`, preserving Version, Updated At, content, and unrelated metadata, and synchronize the required filename/location.

**Returned evidence:** Save/read back the Archived carrier and location before returning `archived`; include `targetID` only as business observation. Return explicit error or partial results with actual completed outputs on failure. Create no successor/N+1, promotion, reference retarget, deletion/reactivation, or descendant cascade. Do not retry, replay, repair, or perform a rollback. Journal append is independent and nonblocking.
