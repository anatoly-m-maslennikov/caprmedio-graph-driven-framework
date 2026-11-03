---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Create Atom Draft

## Claim scope

PROJECT_CONFIGURATION

## Claim

This reusable Workflow creates a Draft for exactly one non-container Atom under its applicable model, either as a new proposal or from one explicitly selected source. It owns the entry, the single-step order, transitions, terminals, inputs, outputs, and single-target boundary; it does not duplicate the Action algorithm or bind an implementation provider.

### Entry, transition, and terminals

The entry accepts one source selection (missing/null, exact Current, explicit Draft, or explicit Archived), one Draft destination, and the caller's complete proposed content/changes, Summary, Role, placement, applicable model, permissions, and expected preconditions. It dispatches exactly one Step, [Create the requested Atom Draft](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--create-atom-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-requested-atom-draft.md), once.

On a verified Draft carrier the Workflow ends `complete` with the exact path, marker, status, proposed Version, and any replacementSummaryRole mapping. An invalid, ambiguous, colliding, container, or otherwise refused request ends `blocked` with attributable diagnostics and no unadmitted write. A failed or partial effect ends with the actual completed and incomplete outputs; no automatic retry or cross-target rollback is admitted. Journal recording is an observation of an actual event, never a permission, completeness, or success gate.

### Boundary and outputs

The selected target is one non-container Atom only. Semantic containment is a container boundary even when no containing folder exists: reject the request and do not select descendants or run a cascade. Exact source resolution occurs once; the Workflow does not search history or infer a source. Missing/null source is the valid new role-only case, while invalid source data returns diagnostics and ambiguity returns choices without a write. The separate Step passes the Action result and its evidence through unchanged.

