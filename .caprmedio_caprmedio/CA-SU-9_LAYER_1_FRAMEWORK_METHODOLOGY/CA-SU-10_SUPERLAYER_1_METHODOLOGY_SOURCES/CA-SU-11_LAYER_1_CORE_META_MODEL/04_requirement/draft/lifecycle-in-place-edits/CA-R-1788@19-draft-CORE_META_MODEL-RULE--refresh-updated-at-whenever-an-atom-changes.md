---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Updated At
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
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

Refresh Updated At whenever an Atom changes

## Claim

### Prose Claim

A newly created Draft initializes `updated_at` to its actual creation instant. Only successful initial canonical publication or publication of a new Version assigns the published Atom's actual Project-time publication instant. Every other admitted operation retains the existing `updated_at`, including Draft edits, technical Current/Archived edits, Current-status-only edits, archival (standalone or preceding publication), and filename, ownership, or placement changes.

## Details

Timestamp encoding follows `CA-D-270`. Relocation is defined by [CA-R-1432](CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md); prior-byte retention follows [CA-R-1521](CA-R-1521@33-draft-CORE_META_MODEL-RULE--resolve-lifecycle-changes-from-applicable-status-models.md).
