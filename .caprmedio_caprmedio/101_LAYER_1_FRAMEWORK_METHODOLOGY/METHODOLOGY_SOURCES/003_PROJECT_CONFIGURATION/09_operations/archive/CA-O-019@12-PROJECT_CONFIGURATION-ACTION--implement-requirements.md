---
atom_id: CA-O-019@12
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Requirement Implementation
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Implementation
version: 12
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-O-017
  - CA-O-018
  - CA-R-1559
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
