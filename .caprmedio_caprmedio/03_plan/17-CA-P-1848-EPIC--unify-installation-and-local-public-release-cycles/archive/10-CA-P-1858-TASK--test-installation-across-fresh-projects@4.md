---
atom_id: CA-P-1858
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Evaluation"
    - "Framework Package"
    - "Atom"
    - "Tool"
    - "Workflow"
    - "Workflow Run"
    - "Journal"
    - "Carrier"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1859
---
# Summary

Test installation across fresh Projects

## Objective

the AI Agent provides golden **and** end-to-end evidence that the new installation boundaries work for fresh independent Projects.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: reviewed RMED/Operations **and** the implemented exporters, compiler, package, state migration, installer **and** launchers.
- write golden/e2e tests first **and** retain fixtures under the owning Tool's `tests` directory. cover active-only Methodology, original-source relations, complete support closure, renamed paths **and** `.DS_Store` handling.
- exercise at least two explicit fixture Project-input roots **in** one repository, separate repositories, a non-Git Project, a relocated package, **and** execution **without** the development checkout. assert no cross-Project state, settings, endpoint, image-selection **or** mutable authority leakage; fixtures provide their own settings, structure **and** registry bytes **and** never receive fabricated adoption metadata.
- cover installation/release failure, stale/tampered pins, interrupted migration, idempotent reinstall, destructive replacement, pending terminal recording and preserved history. After the old installed package is removed, assert unavailable state, no stale selector success and preserved configuration/Project-owned evidence; no fixture result may stand in for a missing real-Docker proof.
- verify `.caprmedio_runtime/config.toml` receives defaults only if absent. Customized values, comments and bytes remain unchanged during same-version reinstall, replacement and failed installation; incompatible settings produce an explicit migration requirement or blocked activation. Test two Projects with different runtime configurations and no leakage.
- perform an independent code/RMED/O review **before** the local gate: trace each implemented package/install/release/discovery path to its current definition, record divergences **and** resolve **or** explicitly block them. record coverage/results **and** correct implementation against RMED/Operations. inherited confidence/retry/permission gates apply; test execution cannot justify suppressing a failure.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** required golden/e2e cases lack evidence, the independent code/RMED/O review is incomplete **or** finds an unresolved material divergence, a fresh/relocated/isolated Project scenario fails, recovery loses records, **or** a required Docker/host path remains unverified.
