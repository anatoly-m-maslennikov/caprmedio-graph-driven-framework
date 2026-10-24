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
version: 4
updated_at: "2026-10-21T21:33:50Z"
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

### Latest approved installer split and source checkpoint

The source implementation is the single
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/INSTALL_TOOLS/install.py`
CLI with separate `runtime` and `project` commands. Runtime owns the
host-global Docker parameters in
`XDG_CONFIG_HOME/caprmedio/runtime.toml` (falling back to
`~/.config/caprmedio/runtime.toml`); `--harness=codex` copies the
standard-library hook and creates an isolated host environment under
`XDG_DATA_HOME/caprmedio/runtime`, registers the global hook and HTTP MCP
connection, and preserves unrelated configuration without granting trust.
Both scopes are dry-runs unless `--apply` is supplied.
An optional immutable image with `--apply` delegates to the existing shared
launcher; without an image it configures only and makes no running-service
claim. Project setup is selected-directory-only, requires an explicit fresh
prefix, seeds minimal settings/control/empty structure, preserves existing
Project carriers, and installs the bundled canonical thin Skill without
Docker/global MCP/hooks/Git initialization/copied Tools. Both scopes refuse
missing, ambiguous, unsafe and conflicting preconditions before effects, and
rollback is limited to exact own writes so concurrent edits are preserved.
Focused checks for this source are pending. This revision claims no test
completion, Docker build, production replacement, hook trust, live activation
or release; keep the Task Active until client/adoption acceptance is verified.
