---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Apply one Direct Atom Update

## Claim scope

One exactly selected non-container Atom and its requested changes.

## Claim

Resolve the exact non-container target once. Validate requested fields against the applicable model/schema, mandatory fields, expected source/currentness, permissions, identity, collision, and placement; never overwrite another target; read back the saved carrier.

- **Draft:** edit content in place, preserve Version and Updated At, and leave Current untouched. Unchanged Summary/Role retains the canonical intent marker and proposed Version. A Summary/Role change switches to a role-only marker and filename, keeps Draft Version/time, assigns no stable canonical ID, and publishes the canonical Atom at Version 1.
- **Current:** allow only technical in-place edits preserving meaning, identity, Summary, Role, Status, Version, and Updated At; synchronize filename/location. A semantic request is an explicit error; the caller may separately select Update. Create no archive or successor.
- **Archived:** allow only technical in-place edits preserving identity, meaning, Status, Version, and Updated At; synchronize filename/location. Do not publish Current or promote a Draft; semantic or identity changes are explicit errors.

Return the saved result or an explicit error with completed partial outputs. Do not retry, replay, or roll back. Journal records business events only and is nonblocking. Reject containers, descendants, and cascades; Workflow flow and Step bindings remain outside this Action.
