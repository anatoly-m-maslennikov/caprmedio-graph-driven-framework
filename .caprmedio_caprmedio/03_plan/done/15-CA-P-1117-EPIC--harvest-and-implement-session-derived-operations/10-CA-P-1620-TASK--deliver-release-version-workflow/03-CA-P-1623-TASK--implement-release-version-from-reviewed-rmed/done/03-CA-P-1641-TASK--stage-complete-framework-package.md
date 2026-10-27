---
atom_id: CA-P-1641
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Framework Package
  depends_on:
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Manifest
  - Subject/Graph Node/Engineering/Methodology
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/CAPRMEDIO Main Skill
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 11
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1623
  blocks:
  - CA-P-1643
tier: 3
---
# Summary

Stage complete Framework package

## Objective

Within <=15 minutes, stage complete Framework package.

## Details

Own new RELEASE_VERSION/release_packaging.py and its dedicated tests only: candidate non-active full Framework package under D562 content-addressed release root, complete Engine/Methodology/ca resources, manifest verification, collision/idempotency and source/selector preservation. Explicit staging only; no current.toml promotion, public Skill change, image/test gate manufacture or actual release invocation.

Inputs are P1622 accepted source/RMED pins: O164–179@1, R1876–1880@1, M331–333@1, E571–574@1, D560–564@1. D561/E572 are the repaired accepted pins, not their rejected predecessors. Preserve external dirt and designated C447/C449 boundaries; existing development worker tests are not fresh-image proof.

## Definition of Done

Save exact bounded output and test/remaining-coverage evidence. Pure preparation, staging or source review never establishes release promotion, complete P1623, P1624 or Epic closure.

## Result

The initial staging boundary was independently rejected by P1651 and repaired in P1658, now Done. Current release_packaging.py SHA-256 eea888c353fbf3d850d26be49762a39755f225d8b2aad8c4a63ee5c2d7b85464 and dedicated test_release_packaging.py d30b5160b2a9498ba1febd6fa8ef4d52f9c808d030aea2b37b5cf88f5709d94d require a trusted SealedCandidateCompilation, recheck full rows/bytes/modes/currentness, and implement safe retained-package staging/idempotency/collision behavior. Five focused package tests passed. No public Skill, selector, image or actual repository Release effect is claimed.
