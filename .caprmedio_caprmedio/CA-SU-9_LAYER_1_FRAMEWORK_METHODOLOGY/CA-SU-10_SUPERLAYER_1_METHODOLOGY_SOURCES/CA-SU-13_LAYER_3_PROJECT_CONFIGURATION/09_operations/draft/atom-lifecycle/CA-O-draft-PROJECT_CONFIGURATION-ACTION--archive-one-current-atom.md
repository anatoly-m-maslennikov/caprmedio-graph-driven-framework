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

Archive the selected Current Atom using its applicable status model and derived carrier location. Preserve Version and Updated At. Report an explicit error on failure. An actual business observation may be recorded in the Journal independently; a recording failure does not block archival.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedArchivedAtom` a request for additional input, or an explicit failure; any Journal warning is separate.
