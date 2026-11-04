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

Set one Current Atom Status

## Claim scope

One exact non-container Current Atom and one requested Status in its qualified model's Current group.

## Claim

Validate schema and mandatory fields, exact source currentness, authorization, the requested Status in the model's Current group, collision/no-overwrite, and placement.

Change only Status in place, synchronize filename/location, and read back the saved carrier. Return it or the explicit error with completed outputs.
