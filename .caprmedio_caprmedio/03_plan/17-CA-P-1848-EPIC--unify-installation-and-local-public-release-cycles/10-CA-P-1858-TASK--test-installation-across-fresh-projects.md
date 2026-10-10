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
status: Active
author: Anatoly Maslennikov
version: 5
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

the AI Agent provides golden **and** end-to-end evidence that the Local release command installs the selected reusable package safely into fresh independent Projects.

## Details

1. Exercise at least two fixture Project roots, separate repositories, a non-Git Project, a relocated package and execution without the development checkout.
2. Assert no cross-Project state, settings, endpoint, image-selection or mutable-authority leakage; fixtures provide their own settings, structure and registry bytes.
3. Cover active-only Methodology, original-source relations, complete support closure, renamed paths, `.DS_Store`, stale/tampered pins, interrupted migration, idempotent reinstall, destructive replacement and honest unavailable state after removal.
4. Preserve customized `.caprmedio_runtime/config.toml` bytes through reinstall, replacement and failure. An incompatible setting requires explicit migration or blocks activation.
5. Run this coverage as the Local release command's complete preflight suite before the first destructive product wipe. Conformance is validated inside that command; no separately commanded review, approval or handover is added.

### Definition of Done

the Plan is **not** Done **if** required golden/e2e evidence is missing, a fresh, relocated or isolated Project scenario fails, recovery loses records, required Docker/host coverage is absent, or a material release-contract divergence remains unresolved.
