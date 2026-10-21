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
version: 9
updated_at: "2026-10-15 01:12:14 +0000"
relations:
  relates_to: [CA-O-164, CA-O-178, CA-R-1525]
---
# Summary

Promote candidate and retire exact prior image

## Action

Install selected Framework Methodology and refresh Project MCP **means** the final local Action that replaces the installed Framework with the exact verified `101_FRAMEWORK_METHODOLOGY` product, installs the bound `ca` Skill, and restarts or reuses the current Project MCP for a smoke check.

## Scope

The Action requires CA-O-164's current validated active sources, passing intended local-release tool tests, exact compiled product, and the exact verified package, runtime, `ca`, and candidate image prepared by the same Workflow. Under one installation lock it preserves protected settings and Project state, clears only replaceable installed Framework members, and copies `101_FRAMEWORK_METHODOLOGY` as-is into `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`. It then installs that same package/runtime and bound `ca` payload, and restarts or reuses the current Project MCP for the declared smoke check. First installation has no required prior image or installed package; an existing installation is preserved until its replacement is ready.

## Details

Commit the successful installed clear and product copy separately, staging only each transition's owned changes. These checkpoints remain separate within this Action. Other successful state-changing installation steps also retain their own scoped commit; unchanged or read-only steps record results without empty commits. A failed transition or commit stops before the next transition.

This Action considers all accumulated obsolete release-owned containers and images for the current Project, not only the immediate predecessor. Before Project-MCP startup, it may remove exactly identified stopped obsolete containers so retained old containers do not prevent startup. The existing exact-prior Project-MCP replacement path may stop and remove that prior container through its ownership checks; accumulated cleanup does not stop other running containers. After installed-package verification and successful Project-MCP startup/smoke, repeat eligible stopped-container cleanup and remove the now-unused obsolete images.

Derive each exact immutable image/container identity, Project-root ownership and obsolete-code status from actual release, build, launcher or start evidence and matching Docker inspection. A tag prefix or version age alone proves neither ownership nor obsolete code. Preserve the promoted candidate and all images/containers carrying the verified current code, running containers outside the existing exact-prior replacement path, unrelated or other-Project resources, required protected references, and images retained by any container. Unknown ownership, unknown code identity or unavailable inspection means retain and report, including unproven orphan images. Never force-delete containers or prune globally. Record each target's ownership and code evidence, use/protection check and actual removal or retention outcome through the shared Run/Action Journal evidence. Blocked or failed cleanup is reported as pending; successful installation does not imply complete cleanup.

The Action never copies from an installed tree as source authority, broadens the active source set, creates another Workflow, pushes, opens a PR, removes unrelated Project state, or retries an uncertain effect. A failed copy, Skill installation, MCP restart/reuse, or smoke check stops with actual evidence and leaves no claim of completed installation.
