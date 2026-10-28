---
atom_id: CA-A-1230
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-28 00:02:21 +0400
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

## Applied result

The source successors were promoted with predecessor archives, and the full combined CA-PROJ-009 was rebuilt from Current RMEDO. Definition references are bare R Atom IDs; source versions remain in YAML. A1231 subsequently defines four focused Projection Types without removing the existing combined Type.
