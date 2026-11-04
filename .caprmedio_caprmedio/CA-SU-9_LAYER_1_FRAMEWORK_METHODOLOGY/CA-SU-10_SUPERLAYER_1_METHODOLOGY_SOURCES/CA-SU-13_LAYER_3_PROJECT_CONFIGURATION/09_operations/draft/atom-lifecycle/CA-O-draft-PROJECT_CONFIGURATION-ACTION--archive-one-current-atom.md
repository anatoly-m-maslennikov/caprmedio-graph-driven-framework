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

Resolve the exact Current source and validate its schema, mandatory fields, applicable `Archived` status, currentness, placement, authorization, collision, and no-overwrite.

For Current Version N, write `ID@N` with status `Archived`, preserving Version, Updated At, content, and unrelated metadata, then read back the saved carrier. Return it, or the explicit error with completed outputs under [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md). Journal append records the archived predecessor only and is nonblocking.
