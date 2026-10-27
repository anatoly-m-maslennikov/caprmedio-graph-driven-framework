---
atom_id: CA-P-1736@10
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 10
updated_at: 2026-10-24 23:49:54 +0400
subjects:
  governs: Subject/Engineering/Release Version
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Evaluation
  - Subject/Engineering/Release Version/Runtime Package Carrier
  - Subject/Engineering/Methodology
  - Subject/Engineering/Image
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Skill
relations:
  is_decomposition_of:
  - CA-P-1714
tier: 3
---
# Summary

Bind first runtime planning to current proof

## Objective

Integrate read-only canonical compilation proof and actual bootstrap image admission into first-runtime planning and installation.

## Details

Own framework_initialization.py and, if required, one private compiler-currentness module. Use exact deterministic output comparison for a complete conflict-free frontier. Recheck proof before package/Skill/selector effects; planning/startup never compile or build. Expected bounded effort: <=15 minutes; decompose further if necessary.

## Definition of Done

The owned source or implementation is independently accepted and its real verification result is saved. Source or mock proof alone does not close actual first-install or Release gates.

## Result

Initializer binds current canonical compilation and complete-package image proof, refuses caller-controlled fresh inspectors and retained test-double authorization, and reopens inputs before package, Skill and selector effects.

Saved implementation: b790a3fd0. This is scoped source and fixture verification, not an actual complete Release or Framework installation. P1739 remains Active.
