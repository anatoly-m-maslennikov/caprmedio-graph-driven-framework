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

Journal events record actual lifecycle business effects. An archive event names the archived predecessor and no intended successor. A promotion event names a published canonical Atom after readback and may relate it to that predecessor when the Workflow has both actual results. A later failure still records an actual completed publication.

Append observations independently. An append failure is a nonblocking warning and never an admission gate.

Active Current Atom relations do not carry replacement history. Formal `replaced_by` and `replacement_of` remain deferred; later replacement navigation is derived from immutable Journal and archive history under separately admitted authority.
