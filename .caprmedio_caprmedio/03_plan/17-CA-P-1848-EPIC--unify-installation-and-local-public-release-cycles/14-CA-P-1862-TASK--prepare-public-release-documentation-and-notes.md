---
atom_id: CA-P-1862
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 15:41:25 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Version"
    - "Framework Package"
    - "Workflow Run"
    - "Evaluation"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1863
---
# Summary

Prepare public release documentation **and** notes

## Objective

the AI Agent prepares accurate public release documentation **and** a full PR description for the validated release.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the actual source changes, validated local release result, existing README, canonical Version **and** `VERSION_HISTORY.md`.
- update README install/start/upgrade instructions to the new `methodology`, `.caprmedio_install` beta-package **and** per-Project `.caprmedio_runtime` boundaries, uv-only execution, ca installation **and** password-free loopback MCP. remove stale path/command claims.
- select/update the canonical Version **once** under Operator input **and** current version policy; keep package, local receipt **and** public files consistent. if this changes the local validated closure, refresh the local release/gate rather than publishing mismatched identities.
- write a full PR description from actual changes: purpose, delivery/install migration, corrected defects, compatibility/rollback, complete tests/evidence **and** honest limitations. keep **only** its concise bullet-point release summary **in** Version History; retain the bullet structure for 0.4, 0.4.1 **and** subsequent entries.
- store a reviewable description for the later GitHub PR; documentation preparation **must not** claim a push, PR, merge **or** release that has not occurred.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** README is stale, Version files/package identity disagree, the PR description lacks meaningful evidence/migration context, **or** Version History duplicates the full description rather than its short bullet summary.
