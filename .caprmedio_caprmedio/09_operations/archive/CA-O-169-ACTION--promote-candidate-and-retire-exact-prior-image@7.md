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
version: 7
updated_at: "2026-10-11 17:34:07 +0000"
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

Only after installed-package verification and successful Project-MCP startup/smoke, this same Action removes all verified superseded CAPRMEDIO release-owned images for the current Project, including the exact prior image when eligible. It derives each exact immutable image identity and Project-root ownership from retained actual release, build, launcher or start evidence and matching Docker inspection. A tag prefix alone is not ownership proof. It preserves the promoted candidate, unrelated images, other-Project or otherwise protected images, and images retained by containers or required protected references. It never force-deletes containers or prunes globally. Record each image's ownership evidence, use/protection check and actual removal or retention outcome through the shared Run/Action Journal evidence. In-use and unproven cleanup targets remain preserved and are reported as blockers; successful installation is not falsely reported as complete image cleanup.

The Action never copies from an installed tree as source authority, broadens the active source set, creates another Workflow, pushes, opens a PR, removes unrelated Project state, or retries an uncertain effect. A failed copy, Skill installation, MCP restart/reuse, or smoke check stops with actual evidence and leaves no claim of completed installation.
