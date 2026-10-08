---
atom_id: CA-P-1844
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 01:35:54 +0400"
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

Prove launcher behavior across separate repositories

## Objective

the AI Agent runs the bounded real-Docker launcher proof for two disposable Project repositories.

## Details

- input: the integrated launcher, admitted image, accepted E fixtures, **and** available Docker host capability.
- output: saved evidence for image-missing/build **and** compatible reuse, two isolated runtime endpoints, authenticated MCP access, **and** repeat startup preserving healthy container IDs **and** ports.
- verification: run the declared two-repository harness within its accepted time/resource bounds; retain truthful failures **or** incomplete coverage. keep existing live Project runtimes **and** unrelated images unchanged.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

the Plan is **not** Done **if** ((a required real-Docker case lacks a terminal result) **or** (two repository runtimes collide) **or** (the proof changes an unrelated existing runtime)).

- execution evidence: the saved opt-in proof attempt `launcher-proof-4lng87od` failed during missing-image build **before** Project startup; its retained `result.json` contains no completed group.
- corrected diagnosis: the launcher dropped the standard proxy-routing variables required by the Codex session. the Operator's terminal resolves `auth.docker.io`; a session HTTP request through its configured proxy receives HTTP 200. the earlier failed build is retained as failure evidence, **not** a general host-DNS outage.
- repair evidence: commit `961dc2b35` preserves proxy routing for Docker client processes while excluding MCP **and** unrelated credentials; **`=43`** launcher tests **and** independent source review pass. no permission profile, Docker settings, **or** DNS configuration was changed.
- acceptance remains incomplete; the fresh declared harness retry is running. evidence: `.caprmedio_tmp/launcher-epic-1829/live-proof-blocker.md`.
