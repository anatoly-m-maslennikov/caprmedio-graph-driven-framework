---
atom_id: CA-A-1230@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 23:19:29 +0400
relations: {}
tier: 3
---
# Summary

Deliver the full Subject Graph with definition IDs

## Operator correction

“1. it's not full subject graph”

“2. definitions should not be citated, only id of atoms with definitions”

## Decision

The Current-RMEDO Subject Graph must render the complete source-backed Subject hierarchy, not a selected main-entity excerpt. Include its four sections: Primary subjects; Properties with direct/inherited values; Instances; and Dependency-only subjects.

Use only bare defining Atom IDs for definition references. Do not duplicate definition text, Claim quotations, citation links or a separate definition table. Keep source Atom versions in the YAML provenance.

## Scope

Update R2150 and D653, preserve their predecessors, and rebuild CA-PROJ-009 from all selected Current RMEDO Governs and Depends On Subjects. Reuse existing parser/rendering logic where possible. No Subject remapping, new entity, construction tree, Terms Graph, production Tool/runtime change or new FPF review.

## Preparation

Two source successors are Drafted. Full-source rendering and coverage checks precede promotion/publication. The previous primary-only excerpt is not evidence that the full graph was rendered.
