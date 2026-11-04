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

Replacement or absorption history **must** be recorded only in the authoritative Journal event for the predecessor's actual archive. That event names the explicit predecessor Atom ID and the selected/intended target canonical ID (`targetID`) known before archival. The target binds intent; it does not assert publication or completed replacement. An unchanged-Summary/Content-Role existing-Atom intent keeps its canonical ID; a changed Summary or Content Role, or a new Atom, selects a fresh ID. Promotion uses the selected ID exactly and may publish any Status admitted by the selected Current operation. Only its actual readback confirms the published successor and Status; a failed promotion never reports a completed replacement or fabricates a successor. Standalone archival requires no successor.

The shared lifecycle is create Draft -> select the `targetID` before Archive -> archive the selected Current when present -> promote using that same ID. The `targetID` lives only in operation context/result, not Draft metadata or a separate artifact. Draft edits and archive preserve Version and in-place Updated At; a new canonical Atom starts at Version 1, while an existing-Atom publication uses its intended proposed Version, normally N+1, at publication time. Journal append is independent and nonblocking; its failure is a warning/diagnostic, never an admission gate.

Active Current Atom relations do not carry replacement history. Formal `replaced_by` and `replacement_of` remain deferred; later replacement navigation is derived from immutable Journal and archive history under separately admitted authority.

On a lifecycle or operation failure, stop and return completed outputs and errors without mutation replay. An independent Journal append failure is only a nonblocking warning/diagnostic and does not invalidate completed effects. There are no retries, replays, or rollbacks.
