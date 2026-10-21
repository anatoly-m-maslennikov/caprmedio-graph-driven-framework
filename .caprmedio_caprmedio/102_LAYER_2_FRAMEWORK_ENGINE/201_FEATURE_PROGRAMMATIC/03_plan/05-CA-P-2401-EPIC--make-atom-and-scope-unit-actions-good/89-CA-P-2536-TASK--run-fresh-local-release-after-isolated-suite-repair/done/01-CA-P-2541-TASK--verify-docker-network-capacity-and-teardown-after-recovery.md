---
atom_id: CA-P-2541
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
version: 2
updated_at: "2026-10-21T12:09:01Z"
---
# Summary

Verify Docker network capacity and teardown after recovery

## Objective

Verify the previously failing real Docker cases after approved bounded network cleanup, before another full Local release.

## Details

Root alone runs the existing test_docker_e2e.py module with current_code_test_image and run_module in the Project3.14 virtualenv. Disposable Projects, dynamic ports, no production mutation tests. All three cases must execute with zero skips. Compare exact network-ID baseline before/after and original production container/image/network health; scoped test teardown must leave no new networks. Keep existing deadlines and fixture guards. Canonical owner cleans only unused attempt image. No new cleanup implementation, production stop semantics, generic collector, daemon settings, push or failed-Run replay. At most15minutes own work excluding passive tests; save actual outcomes, then update parent before fresh full release.

### Recovery verification

Actual current-source Docker functional module passed all three tests with zero skips in94.378s (module96.201s). Test image d6e6898fd510f004e321909fb15fc16146ac0600d849ff6e2462f04ba1fa3f8b was used only for disposable Projects and removed by its canonical unused-attempt owner afterward. Exact network-ID set equals the five-network baseline; original production container/image/network metadata remains identical and healthy. This confirms current teardown on these cases and restored capacity, not every forced-interruption/launcher-startup boundary. Full Local release still pending.
