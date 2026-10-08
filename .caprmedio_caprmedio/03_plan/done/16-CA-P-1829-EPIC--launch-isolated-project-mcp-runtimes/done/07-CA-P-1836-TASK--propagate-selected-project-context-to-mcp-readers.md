---
atom_id: CA-P-1836
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:53:47 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1837
    - CA-P-1843
---
# Summary

Propagate selected Project context to MCP readers

## Objective

the AI Agent makes the required MCP readers consume the accepted selected-Project context.

## Details

- input: the shared selector, selection RMED, **and** current readers **in** `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/capability_discovery/service.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/authoritative_status_models.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py`, **and** `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py`. include `204_MCP/hot_reload.py` **and** `implementation_server.py` at the Gateway-to-implementation binding boundary.
- output: a bounded context-propagation change using the shared selector, with explicit settings/control-root binding rather than independent hardcoded discovery. carry the selected context through Gateway spawn **and** its admitted argument/environment boundary. preserve existing source-currentness **and** mutation-admission checks; bind manifest, registry, **and** query-source admission **to** the selected Project.
- verification: use two selected Project fixtures **in** one repository; each reader **and** the spawned implementation resolve the requested authority **and** reject an ambiguous **or** mismatched context. a second Project **must not** borrow the first Project's otherwise valid manifest/registry/query-source frontier.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: 7 selected-context, 22 HTTP/hot-reload, 26 Atom-operation, 19 discovery **and** 11 status-model tests passed; the legacy selected-Run fixture was reconciled **to** the canonical builder **and** its focused test passed. contexts propagate through entrypoint, Gateway **and** child while transport credentials remain filtered.

the Plan is **not** Done **if** ((a required reader still selects the fixed caprmedio instance) **or** (a reader falls back **to** another Project) **or** (the targeted reader regressions fail)).
