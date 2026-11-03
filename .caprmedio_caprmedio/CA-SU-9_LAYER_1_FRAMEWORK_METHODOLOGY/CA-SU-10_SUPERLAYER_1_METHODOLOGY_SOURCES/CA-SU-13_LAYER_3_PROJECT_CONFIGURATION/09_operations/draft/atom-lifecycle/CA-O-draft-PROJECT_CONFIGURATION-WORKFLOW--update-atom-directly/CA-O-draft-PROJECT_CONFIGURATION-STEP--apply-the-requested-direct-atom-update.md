---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Apply the requested Direct Atom Update

## Claim scope

The sole Step of [Update Atom Directly](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-directly.md), for one non-container Atom.

## Claim

This Step belongs to [Update Atom Directly](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-directly.md) and RUNS exactly [Apply one Direct Atom Update](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--apply-one-direct-atom-update.md).

Bind the selected Atom, requested changes, applicable model, Scope Unit, placement and ordinary operation authorization from the enclosing Workflow inputs. The Action determines the case from the resolved Status; bind no separate repair mode, human-answer record or preservation flag.

Return the Action's actual result, no-op, diagnostics, partial outcome or handoff unchanged. Add no other operation, descendant selection, retry or rollback.
