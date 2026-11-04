---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.ID
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom.Header.Status: Draft'
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
  - CAPRMEDIO_MODEL <+ Atom
version: 20
updated_at: 2026-11-03 22:28:39 +0400
relations:
  depends_on:
  - CA-D-650
  - CA-D-378
  - CA-D-446
atom_id: CA-D-568@20-draft
status: Draft
tier: 4
role: Delivery
form: Decision
---
## Summary

Bind Draft Identity Continuity Evidence

## Claim

Draft identity continuity **must** follow the exact admitted target and applicable identity rules. Retained Draft history or additional paperwork is not a prerequisite for creation, editing, promotion, Status change, or success.

- Draft `atom_id` and marker encoding follow CA-D-378 and CA-D-446; filename identity-segment serialization follows CA-D-650. Do not restore an old ID from archive or other history, and do not release historical IDs for reuse. Ordinary model, carrier, source, permission, identity/collision, currentness, and schema checks remain applicable.
- A new Draft starts at Version 1. In-place Draft edits preserve Version and Updated At, including a Summary/Role change that turns an existing-Atom Draft into a new-Atom role-only proposal; that retained Version, even when greater than 1, is not a reason to reject the Draft. Promotion reads the Draft marker: an existing-Atom marker retains its canonical ID and proposed Version, while a role-only Draft receives a fresh canonical ID and publishes Version 1.
- Use the shared flow: create Draft -> archive the selected Current when one exists -> promote the Draft. Archive does not receive, allocate, or report an intended successor. Do not search history, restore an old ID, or make a canonical ID a Draft property or separate artifact.
- Publishing a new Version archives the exact predecessor with its Version, Updated At, and unrelated content unchanged, then publishes the intended replacement at N+1 at publication time. In-place technical Draft, Current, Archived, and Current-status-only edits preserve Version and Updated At and create no predecessor archive or successor. Do not fabricate events or lineage to admit an operation.
- A proposed new Version of an existing Atom, including a Subjects-only edit, uses the canonical target and the normal `@<proposed-version>-draft` marker until promotion; publication follows the predecessor-archive/N+1 rule. Journal or history receipts are not admission gates. Independent Journal append failures are nonblocking warnings and do not invalidate completed effects. Failure handling follows CA-R-1432.
