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

Set one Current Atom Status

## Claim scope

This Action applies to one exact selected non-container Current Atom under its qualified applicable model and one exact requested Status in that model's Current group. The group includes model-admitted statuses beyond Active when present and excludes Draft and Archived; no container, descendant, cascade, scope or tier target is admitted.

## Claim

Resolve one exact non-container Current Atom. Validate schema, mandatory fields, expected source/currentness, permissions, collision, placement, and the requested Status against the qualified model's Current group; Draft and Archived are invalid and Active is never hardcoded.

Change only Status in place and synchronize its admitted filename/location, preserving identity, Summary, Role, content, Version, and Updated At. Read back the carrier; create no archive, successor, new Version, promotion, descendant effect, or overwrite. Return the saved result or an explicit error with completed partial outputs. Do not retry, replay, or roll back. Journal records business events only and is nonblocking.
