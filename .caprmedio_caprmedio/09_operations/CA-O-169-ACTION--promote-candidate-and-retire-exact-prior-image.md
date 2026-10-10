---
atom_id: CA-O-169
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Install selected Framework Methodology and refresh Project MCP"
  depends_on: [Action, Version, Methodology, Implementation, Skill, Test, Permission, Journal]
version: 6
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-O-164, CA-O-178, CA-R-1525]
---
# Summary

Promote candidate and retire exact prior image

## Action

Install selected Framework Methodology and refresh Project MCP **means** the final local Action that replaces the installed Framework with the exact verified `101_FRAMEWORK_METHODOLOGY` product, installs the bound `ca` Skill, and restarts or reuses the current Project MCP for a smoke check.

## Scope

The Action requires CA-O-164's frozen inputs, passing full-test preflight, exact compiled product, and the exact staged package, runtime, `ca`, and candidate image prepared by the same Workflow. Under one installation lock it preserves protected settings and Project state, clears only replaceable installed Framework members, and copies `101_FRAMEWORK_METHODOLOGY` as-is into `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`. It then installs that same package/runtime and bound `ca` payload, and restarts or reuses the current Project MCP for the declared smoke check. First installation has no required prior image or installed package; an existing installation is preserved until its replacement is ready.

## Details

Commit the successful installed clear and product copy separately, staging only each transition's owned changes. These checkpoints remain separate within this Action. Other successful state-changing installation steps also retain their own scoped commit; unchanged or read-only steps record results without empty commits. A failed transition or commit stops before the next transition.

The Action never copies from an installed tree as source authority, broadens the active source set, creates another Workflow, pushes, opens a PR, removes unrelated Project state, or retries an uncertain effect. A failed copy, Skill installation, MCP restart/reuse, or smoke check stops with actual evidence and leaves no claim of completed installation.
