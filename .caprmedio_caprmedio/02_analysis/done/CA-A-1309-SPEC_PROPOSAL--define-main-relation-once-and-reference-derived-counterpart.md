---
atom_id: CA-A-1309
ref_id: CA-A-1309
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Spec Proposal
topics:
  main_subject: Entity
tier: 3
status: Done
version: 4
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
## Summary

Define the main Relation once and reference its derived counterpart

## Proposal

Define only the main direction in full. The derived counterpart has only its name and a short reference to the main direction. The counterpart reuses the main direction's definition through that short reference. Do not duplicate meaning, constraints or a complete second Definition. This is the DRY reason for deriving the counterpart.

## Status

Accepted by the Operator on 2026-10-29 15:24:34 +0400. [P2696](../../03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/02-CA-P-2696-TASK--establish-one-defining-requirement-per-model-entity.md) owns Draft adoption and the remaining Definition ownership corrections. The Epic remains Active.
