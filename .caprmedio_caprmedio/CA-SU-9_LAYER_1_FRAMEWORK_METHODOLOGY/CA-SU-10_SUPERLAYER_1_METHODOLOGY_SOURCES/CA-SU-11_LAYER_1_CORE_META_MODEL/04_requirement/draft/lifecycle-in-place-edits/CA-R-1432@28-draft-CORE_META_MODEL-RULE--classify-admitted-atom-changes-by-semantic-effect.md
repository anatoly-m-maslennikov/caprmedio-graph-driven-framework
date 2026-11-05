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

For the operation's semantic outcome:

- Creating a Draft for a Current Atom whose Summary and Content Role are unchanged, including a Subjects-only edit, retains that canonical ID in the Draft marker and proposes Version `N+1`. A new Atom, or a Summary or Content Role change, uses a role-only Draft marker.
- Archiving a Current Atom sets its representation to `status: Archived`, preserves its Version and unrelated content.
- Promotion reads the Draft marker: an existing-Atom marker publishes the same canonical ID at its proposed Version, while a role-only Draft receives a fresh canonical ID only at publication and publishes Version 1.

Draft edits preserve Draft Version, including when it is greater than 1. Technical Current or Archived in-place edits and Current-to-Current status-only edits likewise preserve Version; the latter has no archive or successor. [CA-R-1788](./CA-R-1788@19-draft-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md) owns `updated_at` initialization, retention, and publication time.

At every write boundary, security/authorization, expected source/currentness, applicable model/schema and admitted field values, identity/collision and no-overwrite, and Carrier/filesystem safety remain required. Scope and Tier do not change implicitly. For a selected source, internal `expectedSource` is the original read's full Header and Content together with its identity and source selection; the source must match it exactly at the write boundary. This context is tool-internal, not a caller-required field, Atom property, saved proof, receipt, or Journal gate.

An ancestor-only move that does not change a descendant's own bytes, identity, direct owner, or relative placement is not a descendant edit and retains its Version. [CA-R-1788](./CA-R-1788@19-draft-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md) governs its `updated_at`; [CA-R-807](./CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md) governs Journal observations.

An actual mutation, binding/runtime, or write-boundary failure stops later Steps and returns the explicit error and actual completed outputs. Do not retry, replay, recover, or roll back a mutation; completed effects remain.
