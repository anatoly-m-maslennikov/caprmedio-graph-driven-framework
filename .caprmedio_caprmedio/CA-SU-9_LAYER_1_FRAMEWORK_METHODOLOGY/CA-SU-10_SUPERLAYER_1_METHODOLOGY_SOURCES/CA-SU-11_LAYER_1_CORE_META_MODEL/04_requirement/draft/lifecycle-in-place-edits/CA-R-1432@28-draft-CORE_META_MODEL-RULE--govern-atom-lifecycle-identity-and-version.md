---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
version: 28
updated_at: 2026-11-03 20:57:46 +0400
relations: {}
atom_id: CA-R-1432@28-draft
status: Draft
tier: 2
role: Requirement
form: Rule
---
## Summary

Govern Atom lifecycle identity and Version

## Claim

### Prose Claim

Draft edits and directly authorized in-place edits preserve the Atom's ID, Version, and Updated At. A Status-only change or archival preserves Version and Updated At; archival preserves the predecessor's unrelated content and uses the Archived Status and version-qualified identity.

Creating a Draft for a new Version of an existing Atom assigns Version N+1 once and initializes its creation timestamp. Promotion retains that planned Version and timestamp when Summary and Content Role are unchanged. A changed Summary or Content Role instead requires a fresh Atom ID and Version 1 at promotion. Lossless serialization that preserves the Summary value is not a Summary change.

A Current Atom update composes creation of a new Draft, archival of its Current predecessor, and promotion of the Draft. Capture the predecessor's Current Status once and use that same Status for promotion. A new Atom is assigned its own ID and initial Version. Moving an ancestor without changing a descendant's own bytes, metadata, direct owner, or placement relative to that owner does not edit that descendant.
