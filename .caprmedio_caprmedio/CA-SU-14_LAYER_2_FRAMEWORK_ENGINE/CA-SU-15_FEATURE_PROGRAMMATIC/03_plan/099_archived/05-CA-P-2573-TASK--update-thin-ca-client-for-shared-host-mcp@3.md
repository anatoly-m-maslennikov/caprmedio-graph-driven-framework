---
atom_id: CA-P-2573
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 3
updated_at: "2026-10-21T20:53:12Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2576]
  depends_on: [CA-P-2570]
  relates_to: [CA-P-2562, CA-M-396, CA-M-397, CA-M-398, CA-M-399, CA-M-400]
---
# Summary

Update thin ca client for shared host MCP

## Objective

Update the canonical ca Skill and required installation/client material to obtain the exact Project root from the Codex session and transmit it through the shared MCP's advertised contract. Keep procedures in MCP; do not add copied Tool implementation to each Project.

## Details

One Task per file; each leaf has at most 15 minutes own work and must be decomposed before extending it. Review and update dependent Tasks after observed predecessor outcomes. Use the selected Project virtual environment, configured Project Temporary State and only broken/related checks. Do not replay uncertain effects, replace production or run the full suite.

### Definition of Done

The Operator's latest decision uses a Codex PreToolUse hook to pass the full session folder as outer `project_root` on every CAPRMEDIO MCP request. Do not discover an ancestor, resolve a prefix or derive the root from the installed Skill. Native arguments remain unchanged; conflicting explicit binding refuses the affected request rather than silently retargeting it. The server retains canonical Project admission and containment checks.

Bounded client-forward checks cover distinct and nested session folders, unchanged native payloads, unrelated tools, invalid input and conflicting binding. Review/trust and shared-MCP adoption remain explicit activation boundaries; the legacy server cannot consume the added field.

### Observed implementation checkpoint

Canonical `204_MCP/codex_project_context_hook.py`, its functional checks and README are prepared. An identical host copy is installed in `~/.codex/hooks/caprmedio_project_context.py`, and a CAPRMEDIO-only definition is appended to global hooks.json using the selected Project virtual environment. Existing hook definitions and trust state are preserved. The configured command passed a local JSON-protocol smoke check without calling MCP. Four functional tests pass, including the bounded-size refusal. No full suite, Docker build, production replacement, hook trust or live activation is claimed. Keep this Task Active until the remaining client/adoption acceptance is verified.
