---
atom_id: CA-M-333
content_role: Method
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-11 17:34:07 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Gate construction"
  depends_on: [Tool, Manifest, Evaluation, Image, Journal]
relations:
  method_for: [CA-R-1879, CA-R-1880]
---
# Summary

Derive the Release Version gate and retirement decision

## Scope

Construction of the exact promotion, rollback, and old-image-retirement predicates.

## Claim

The Tool derives promotion only from matching sealed candidate evidence in the required order: compilation, declared full suite, separately retained complete runtime package, no-hook Skill delivery, and actual candidate image; it derives post-success cleanup only after verified installation, promotion and Project-MCP startup/smoke, by enumerating exact immutable image identities and selecting all superseded CAPRMEDIO release-owned images proven for the current Project.

## Details

Match Docker inspection to retained actual Project release, build, launcher or start proof with exact immutable image IDs and Project-root identity. Tag prefixes alone do not admit an image. Exclude the promoted candidate, unrelated images, other-Project or otherwise protected images, and images retained by containers or required protected references. For each eligible or blocked target derive its ownership evidence, use/protection checks and proposed exact removal or retention disposition; do not force-delete containers or prune globally. In-use or unproven targets are retained with reported blockers, not an all-removed assertion. Missing, stale, partial, mismatched, or recording-uncertain evidence yields a blocked or pending decision. This construction neither changes a selection nor removes an image.
