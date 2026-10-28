---
atom_id: CA-A-1223
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 19:45:11 +0400
relations: {}
tier: 3
---
# Summary

Govern Nodes with generic Type rules

## Question

Where do generic Type definitions and checks belong when there is no Node/Type Subject?

## Proposal

Use Subject/CAPRMEDIO/Graph/Node for CA-R-1284, CA-R-1285, CA-R-1286, CA-R-1349, CA-R-1350 and CA-E-387. Their existing Content Scope and Claims retain the precise Type-classification, allowed-value and assignment boundaries.

Do not add Node/Type or Node.Type as a shared classification axis or universal property. Type remains optional for a Node unless a specific rule requires it. Map references to these general Type rules' old Graph Node.Type target to Graph/Node as well.

CA-D-393 is different: its Scope and Claim govern external Type names derived from internal Content Role Types. Its Subject is Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type. Do not blanket-map every Type-related Atom to Graph/Node.

## Decision

Operator: “we don't have Node/Type, and we don't need it. so, Graph/Node. Are you sure it's all about Graph/Node?”

The six selected sources were read individually. R1284 explicitly addresses optional Type Properties for Graph Nodes; R1285/R1349/R1350 and E387 constrain such assignments, and R1286 keeps their qualified allowed-value sets expandable. None requires every Node to bear Type. D393 is excluded from this general mapping.

## Adoption

Subjects-only successors; existing Scope, Claim, relations and identity stay unchanged. Stage for review before replacing Current sources.

## References

- [Candidate #10](CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
