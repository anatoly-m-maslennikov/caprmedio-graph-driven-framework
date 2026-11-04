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

Classify admitted Atom changes by semantic effect

## Claim

### Prose Claim

the semantic effect of an admitted Atom change is determined by whether its identity-defining Summary **and** Content Role are preserved or changed, together with the authorized operation that applies it.

The lifecycle is:

- create the requested Draft, for a Current Atom or for a new Atom;
- during preparation, select the target canonical ID before archiving the Current. An existing intent with unchanged Summary **and** Content Role keeps its canonical ID; a new Atom or a Summary/Content Role change selects a fresh ID. Keep this target only in ordinary operation context/result data. The Draft remains its marker until publication; no registry, reservation, **or** receipt is needed;
- archive the Current when one exists. Archival sets the predecessor representation to `status: Archived` while preserving its Version, Updated At, and unrelated content; it does not bump Version;
- promote using the selected ID unchanged. Draft edits **and** identity selection preserve Draft Version **and** Updated At, including when Draft Version is greater than 1. Technical Current/Archived in-place edits and Current-to-Current status-only edits likewise preserve Version **and** Updated At; the latter has no archive **or** successor. A separately published existing identity uses its already proposed Version `N+1`; a fresh canonical ID publishes Version 1. Only successful publication receives its publication time.

Ordinary authorization/security, expected source/currentness, applicable Status model, mandatory-field/schema, collision, and Carrier validation remain required. Scope **and** Tier do not change implicitly. An ancestor-only move that does not change a descendant's own bytes, identity, direct owner, **or** relative placement is not a descendant edit and retains its Version **and** Updated At. Journal records business lifecycle history under CA-R-807; its append is nonblocking and never a history-receipt or admission gate. Lifecycle mutation/operation failures stop and return completed partial outputs **and** errors; there are no retries, replays, **or** rollbacks.
