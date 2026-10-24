---
atom_id: CA-E-645
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-21T23:29:13+00:00"
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Evaluation'
  depends_on:
  - Entity/Node/Continuant/Implementation
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement'
  - 'Entity/Node/Continuant/Atom/Content Role: Method'
  - 'Entity/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Carrier
relations:
  evaluation_for:
    - CA-M-405
    - CA-M-398
---
# Summary

Evaluate observed outcomes and partial results

## Scope

PROGRAMMATIC operations that can complete, no-op, partially apply, fail, cancel or become uncertain across Tools, workflows, Apps, MCP and background work.

## Claim

Accept outcome reporting only when it describes observed state truthfully. Complete, no-op, partial, failed, canceled and uncertain outcomes remain distinguishable; a partial result preserves completed data with the error, and a no-op does not claim a fictional write. Do not require replay or weaken atomicity merely to obtain a result.

## Details

- Exercise success, valid no-op, invalid input, mid-operation failure, cancellation and unavailable-observation cases.
- Compare returned records with durable effects and verify completed items, errors and uncertainty are represented without invented success.
- Verify a partial result contains only completed work and remaining work is not silently replayed, retried or remapped.
- Check that an atomic operation remains atomic when its contract requires it; a truthful failure is preferable to an unsafe partial write.
- Mark an outcome unresolved when the observer cannot distinguish state.
