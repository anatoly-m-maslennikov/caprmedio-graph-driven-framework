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

This Action operates on one exact selected non-container Atom under its applicable model. It does not select a container, semantic containment, descendants, or an inferred historical replacement.

## Claim

The Archive one Current Atom Action **means** the following reusable archive behavior:

- resolve the exact selected version and validate its admitted fields, placement and non-container boundary; an explicitly selected Archived version may return the no-op result below. An effect requires a Current source whose qualified Role/Form model admits Archived. Reject other statuses, ambiguity, missing or invalid artifacts, and any write that would overwrite another target with attributable diagnostics;
- for Current version N, materialize the same canonical identity at ID@N with status Archived, preserving Version N, Updated At, the content body and unrelated metadata exactly. Use the applicable Status Delivery mapping; without a more-specific mapping, place it at the owning role's `archive/<canonical-ID>@<version>[-<remaining-filename-components>].md`;
- create no new Version N+1 and do not alter inbound references, delete the Atom, promote a Draft, or cascade to descendants;
- when the explicitly selected version is already Archived, return a truthful `already_archived` no-op and never reactivate it;
- return the actual `archived`, `already_archived`, or diagnostic result, preserve completed results on partial work, and perform no automatic retry or rollback. Journal only the actual business event rather than using it as a permission, completeness, or success gate.
