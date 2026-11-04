---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 35
updated_at: 2026-11-03 22:25:59 +0400
relations: {}
atom_id: CA-R-807@35-draft
status: Draft
tier: 1
role: Requirement
form: Rule
---
## Summary

Record replacement transitions in the Journal

## Claim

Journal events record actual lifecycle business effects. An archive event names the archived predecessor and no intended successor. A promotion event names a published canonical Atom after readback and may relate it to that predecessor when the Workflow has both actual results. A later failure records the actual completed publication and never reports an uncompleted replacement. Standalone archival has no successor.

The shared lifecycle is create Draft -> archive the selected Current when one exists -> promote the Draft. Draft edits and archive preserve Version and in-place Updated At; promotion reads the Draft marker. A new canonical Atom starts at Version 1, while an existing-Atom publication uses its proposed Version, normally N+1, at publication time. Journal append is independent and nonblocking; its failure is a warning and never an admission gate.

Active Current Atom relations do not carry replacement history. Formal `replaced_by` and `replacement_of` remain deferred; later replacement navigation is derived from immutable Journal and archive history under separately admitted authority.

Failure handling follows CA-R-1432. An independent Journal append failure is a nonblocking warning and does not invalidate completed effects.
