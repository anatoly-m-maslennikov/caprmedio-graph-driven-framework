---
atom_id: CA-P-1845
content_role: Plan
type: Plan
label: Task
work_sequence_number: 16
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 03:46:50 +0400"
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
    - CA-P-1847
---
# Summary

Prove isolation between Projects in one repository

## Objective

the AI Agent runs the bounded real-Docker proof for two selected CAPRMEDIO Framework Instances **in** one disposable repository.

## Details

- input: the integrated launcher, accepted same-repository fixtures, selected-Project reader changes, **and** startup Evaluation cases.
- the fixture contains two distinct Project root folders **in** the same repository; each root directly contains its own `.caprmedio_<project>` folder. a Project root **does not** need its own `.git` directory for HTTP MCP startup.
- output: saved evidence for distinct authority, settings, state, containers, credentials, **and** allocated ports, plus stable repeated/concurrent same-Project launch **and** the selected readiness-failure cases. include simultaneous reload/receipt activity with identical request IDs **and** prove distinct persistent paths.
- verification: perform the admitted MCP read **or** mutation fixture against one selected Project **and** prove the other Project remains unchanged; reject wrong-Project source frontiers **and** shared reload storage; use synthetic fixture data **and** preserve actual terminal receipts.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

the Plan is **not** Done **if** ((a selected runtime resolves another Project's authority **or** state) **or** (repeat/concurrent launch violates the accepted identity contract) **or** (a required same-repository/security case lacks a terminal result)).

- final completion evidence: `launcher-proof-0omrljbe/result.json` exited **`=0`** with `same-repository` completed for two distinct nested Project roots. own-authority reads passed **and** foreign-Atom reads were rejected. credentials, containers, ports, **and** reload paths stayed distinct; identical reload request IDs produced separate Project-local receipts. stable repeated/concurrent reuse, exact requested ports, occupied-publication refusal, wrong-token readiness refusal, **and** endpoint-only `mcp-http` observations passed. Project authority/Journal snapshots **and** retained runtime N are unchanged; **all** fixture containers were cleaned up with no failure.
