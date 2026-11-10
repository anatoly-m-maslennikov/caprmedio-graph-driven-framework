---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Create one Atom Draft

## Claim scope

One non-container Draft materialization under its applicable model.

## Claim

Create a Draft from `newAtom` properties or from a selected existing Atom and supplied property changes. For an existing Atom read its full properties and content, merge supplied properties, and carry all others forward. Derive Draft metadata, filename and path from the resulting properties and model; the caller does not provide a filename or path. For a Current source with unchanged Summary and Content Role, assign the same-ID Draft Version N+1 once; promotion retains it without another increment. If Summary or Content Role changes, the result is a new identity promoted at Version 1. Editing an existing Draft in place preserves its Version and Updated At. Check formats and allowed values without a semantic gate. On missing or invalid input provide a short explanation and request an additional input dictionary; wait for it. Report an effect failure explicitly. Journal business observations are independent and nonblocking.

### Outputs

`savedDraft`, a request for additional input, or an explicit failure; any Journal warning is separate.
