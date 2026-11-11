---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.State.Updated At
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Carrier.Canonical Address
version: 19
updated_at: 2026-11-03 20:57:46 +0400
relations:
  child_of:
  - CA-R-1416
atom_id: CA-R-1788@19-draft
status: Draft
tier: 3
role: Requirement
form: Rule
---
## Summary

Initialize Version creation timestamp

## Claim

### Prose Claim

Initialize Updated At to the actual Project-time creation instant when a new Atom Version is created. In-place edits, Status-only changes, archival, and promotion preserve the existing Version's Updated At. An ancestor-only move also preserves a descendant's Updated At. Timestamp encoding follows CA-D-270.
