---
atom_id: CA-R-1880
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-11 17:34:07 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Failure and recovery"
  depends_on: [Tool, Workflow Run, Action Run, Journal, Artifact, Image]
relations:
  relates_to: [CA-R-1878, CA-R-1879]
---
# Summary

Preserve the prior release and truthful failure recording

## Scope

Release failure, recording uncertainty, rollback, and delayed old-image retirement.

## Claim

On a failed, blocked, or uncertain release effect or recording before verified promotion, Release Version **must** preserve the prior selected N and actual effect evidence, report the shared Run/Action result truthfully, and never replay an uncertain effect; after successful N+1 installation, promotion and Project-MCP startup/smoke, it **must** retire all verified superseded CAPRMEDIO release-owned images for the current Project whose exact immutable identities and ownership are proven and which have no retaining container or required protected reference.

## Details

Preserve the promoted candidate and unrelated, other-Project or otherwise protected images. Current-Project ownership is derived from retained actual release, build, launcher or start evidence containing exact immutable image identity and Project-root identity, checked against Docker inspection; a tag prefix alone is insufficient. Cleanup includes the exact prior image when eligible, records each removed, protected, in-use or unproven disposition, and reports image-in-use or unproven-ownership blockers without force-deleting containers or claiming all images were removed. This cleanup adds no automatic rollback or effect replay. Existing rollback handling restores only the retained prior selection and affected derived carriers. A request, dry run, candidate manifest, or queued Run is not success, and no failure path authorizes source mutation or broad image pruning.
