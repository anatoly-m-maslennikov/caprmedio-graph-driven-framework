---
atom_id: CA-D-564@5
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-21T10:41:00Z"
subjects:
  governs: "Tool/RELEASE_VERSION/Image carrier"
  depends_on: [Tool, Image, Container, Runtime]
relations:
  delivery_for: [CA-M-332, CA-E-573]
---
# Summary

Carry project-owned Docker image cleanup

## Scope

Direct Docker/MCP smoke for the installed project runtime and cleanup of superseded project-owned images.

## Claim

After a green full suite and successful installed Docker/MCP smoke, delivery retains the exact admitted candidate of the current package Version and removes other eligible images only when they are positively identified as owned by the selected Project and unused by any container. It never prunes broadly, removes an unrelated image, or forces container deletion.

## Details

Canonical image names carry the exact framework Version, actual Docker build date in UTC and digest suffix; they never replace immutable admission or establish ownership. Ownership requires matching inspected Project identity, host Project root and control root together with positive runtime schema/fingerprint classification; a container link is insufficient. A noncandidate digest has no additional retention slot merely because its Version or fingerprint matches. Preserve other Projects' images, unknown or conflicting ownership and every container reference, including stopped containers. Report the exact kept candidate, removed IDs and retained reasons with truthful pending failures; never force, prune or retry uncertain effects. Build output alone does not prove a working runtime.
