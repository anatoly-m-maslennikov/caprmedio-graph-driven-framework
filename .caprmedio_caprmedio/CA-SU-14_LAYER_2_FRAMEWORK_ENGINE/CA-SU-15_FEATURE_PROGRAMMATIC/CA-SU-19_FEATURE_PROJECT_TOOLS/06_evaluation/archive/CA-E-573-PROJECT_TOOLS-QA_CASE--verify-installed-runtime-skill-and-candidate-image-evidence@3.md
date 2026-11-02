---
atom_id: CA-E-573
content_role: Evaluation
type: QA Case
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-21T10:41:00Z"
subjects:
  governs: "Tool/RELEASE_VERSION/Installed-delivery QA"
  depends_on: [Tool, Runtime, Skill, Image]
relations:
  evaluation_for: [CA-R-1877, CA-R-1878, CA-M-332]
---
# Summary

Verify direct installed delivery

## Scope

The installed project runtime and `ca` Skill after a direct Local release.

## Claim

The QA case verifies the installed package/runtime and project-local `ca` Skill, then runs the intended Docker/MCP smoke behavior. A failed check stops the release and is reported for manual handling.

## Details

This case does not require a sealed manifest, a separate full-suite aggregation protocol or promotion state. Verify the exact admitted immutable candidate, package Version and canonical version/build-date/digest tag using the existing runtime evidence.

Use independent synthetic Projects and Docker observations to check: green full suite precedes canonical candidate preparation; failed suite or preparation causes no startup/image removal; cleanup requires verified exact candidate launch even with no prior image; only that candidate earns release retention. An unused, fully selected-Project-owned older rebuild is removable even with the same fingerprint. A same-fingerprint but different-image exact prior Project MCP is replaced by the existing ownership-checked path, while exact candidate reuse remains allowed. Foreign, unowned, incomplete/conflicting ownership, running containers outside that path, and images referenced by any container are preserved. Cover failed observation/removal, pending reporting, no force/global prune and no uncertain retry. These functional checks do not authorize an actual release or production Docker effects.
