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

canonical Atom publication timestamps.

A newly created Draft initializes `updated_at` to its actual creation instant. Successful initial canonical publication or publication of a new Version **must** initialize or refresh the published Atom's `updated_at` to the actual Project-time publication instant. Draft edits, technical Current/Archived in-place edits, Current-to-Current status-only edits, and standalone archival retain their existing Updated At; these operations do not refresh `updated_at`.

When publication archives its predecessor, the Archive Carrier **must** retain the predecessor's prior Updated At and unrelated content; Git history preserves the exact pre-archive bytes. Publication time is assigned only when the canonical Atom is successfully published.

## Details

an ancestor-only move that changes an Atom's repository locator **without** changing its own bytes, identity, direct owner **or** placement relative **to** that owner is **not** an edit **to** that Atom and retains its Updated At under CA-R-1432. A direct Status, filename, ownership, or local-placement change is handled by its authorized operation; it refreshes Updated At only when that operation successfully performs an initial publication or publishes a new Version. timestamp encoding follows `CA-D-270`.
