---
atom_id: CA-O-019
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Requirement Implementation"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Implementation"]
version: 6
updated_at: "2026-10-15 18:52:52 +0000"
relations:
  relates_to:
    - CA-O-017
    - CA-O-018
    - CA-R-1559
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-019-CORE_META_MODEL-ACTION--implement-requirements.md
  source_atom_id: CA-O-019
  source_atom_revision: 6
  source_sha256: 4e559bdef07eb5bb682bce066512e4fcc9985cedb2a94438338709fcbdc8352d
  original_relations_sha256: f32f02a87f378bf1c5f8847914dbb7f72760d6fa62b0a6b252dcf643fdd8422d
---
# Summary

Implement Requirements

## Operation

Requirement Implementation **means** the Agentic Action that realizes the selected P/Plan item's applicable Requirements after their tests are prepared, applying **all** governing Methods within Delivery boundaries.

- inputs: the assigned bounded Plan item, active Method Projection, selected R/E/D, current candidate, prepared tests **and** available baseline results, admitted prerequisites, **and** owned files/work boundary.
- implement **only** the selected ready work. preserve unrelated edits; do **not** alter expected test behavior **or** governing Atoms merely **to** obtain a pass.
- preparation of tests precedes the behavior they check; runnable baseline tests precede that behavior. an explicitly necessary test-execution prerequisite is limited **to** that prerequisite **and** remains traceable.
- return `implemented` with actual changes, fulfilled work, candidate identity **and** pending checks, **or** `blocked` with the exact cause. an unresolved Method conflict requires authority disposition; Atom ID **must not** select the winning Method. implementation is **not** proof of passing Evaluations.

## Details
