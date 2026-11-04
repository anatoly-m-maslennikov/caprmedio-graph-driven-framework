---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Create one Atom Draft

## Claim scope

One non-container Draft materialization under its applicable model.

## Claim

This Action creates one validated `status: Draft` carrier from either `newAtom` properties or one exact `sourceCurrent` selector with changed properties. For a Current, read its full Header and Content, apply only supplied properties, preserve omitted properties, and evaluate Summary and Role after the merge; `newAtom` uses its supplied properties. Copied content is ordinary proposed content.

Validate permissions, model, mandatory fields, exact currentness, non-container Draft name/location, collision and no-overwrite. Derive Draft Status, marker and Version, and initialize Updated At to its creation time. Same Summary/Role keeps the Current ID and proposes Version N+1. A new Atom or Summary/Role change becomes a role-only Draft with fresh `targetID` and `targetVersion` 1. Select that operation context before any later Archive or publication; it is not a carrier field.

Save and validate the Draft by readback, then return it with `targetID`, `targetVersion` and completed outputs. On failure return an explicit error with completed outputs and stop; no retry, repair, rollback or replay. Journal append is an independent, nonblocking business observation.

