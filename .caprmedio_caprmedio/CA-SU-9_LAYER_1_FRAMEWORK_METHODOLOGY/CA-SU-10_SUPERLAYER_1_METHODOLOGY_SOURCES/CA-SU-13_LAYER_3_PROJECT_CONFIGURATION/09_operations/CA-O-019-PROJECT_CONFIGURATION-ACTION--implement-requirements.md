---
atom_id: CA-O-019
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
version: 18
updated_at: 2026-10-27 19:59:44 +0400
relations: {}
tier: 3
---
# Summary

Implement Requirements

## Operation

Requirement Implementation **means** the Agentic Action that realizes the selected P/Plan item's applicable Requirements after their tests are prepared, applying **all** governing Methods within Delivery boundaries.

- inputs: the assigned bounded Plan item, direct full `methods` rows, selected R/E/D, current candidate, prepared tests **and** available baseline results, admitted prerequisites, **and** owned files/work boundary. An optional legacy `method_projection` may accompany those rows but is not required.
- implement **only** the selected ready work. preserve unrelated edits; do **not** alter expected test behavior **or** governing Atoms merely **to** obtain a pass.
- preparation of tests precedes the behavior they check; runnable baseline tests precede that behavior. an explicitly necessary test-execution prerequisite is limited **to** that prerequisite **and** remains traceable.
- return `implemented` with actual changes, fulfilled work, candidate identity **and** pending checks, **or** `blocked` with the exact cause. an unresolved Method conflict requires authority disposition; Atom ID **must not** select the winning Method. implementation is **not** proof of passing Evaluations.

- a changed candidate invalidates affected previous review/check evidence. Return exact changed paths and candidate binding so preparation can select preliminary review, final checks, and final review; implemented is not acceptance.

## Details
