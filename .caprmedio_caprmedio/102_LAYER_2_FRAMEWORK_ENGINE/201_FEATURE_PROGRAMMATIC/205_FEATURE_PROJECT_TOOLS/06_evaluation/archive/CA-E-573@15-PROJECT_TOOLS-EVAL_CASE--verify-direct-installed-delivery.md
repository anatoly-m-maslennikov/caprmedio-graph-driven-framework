---
atom_id: CA-E-573@15
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Implementation
  depends_on:
  - Subject/Graph Node/Runtime
  - Subject/Graph Node/Engineering/Delivery
  - Subject/Graph Node/Carrier/Docker Image
relations:
  evaluation_for:
  - CA-R-1877
  - CA-R-1878
  - CA-M-332
tier: 5
---
# Summary

Verify direct installed delivery

## Scope

The installed project runtime and `ca` Skill after a direct Local release.

## Claim

The QA case verifies the installed package/runtime and project-local `ca` Skill, then runs the intended Docker/MCP smoke behavior. A failed check stops the release and is reported for manual handling.

## Details

This case does not require a sealed manifest, a separate full-suite aggregation protocol or promotion state. Verify the exact admitted immutable candidate, package Version and canonical version/build-date/digest tag using the existing runtime evidence.

Use independent synthetic Projects and Docker observations to check: for the default Local route, green full suite precedes canonical candidate preparation; failed suite or preparation causes no startup/image removal; cleanup requires verified exact candidate launch even with no prior image; only that candidate earns release retention. An unused, fully selected-Project-owned older rebuild is removable even with the same fingerprint. A same-fingerprint but different-image exact prior Project MCP is replaced by the existing ownership-checked path, while exact candidate reuse remains allowed. Foreign, unowned, incomplete/conflicting ownership, running containers outside that path, and images referenced by any container are preserved. Cover failed observation/removal, pending reporting, no force/global prune and no uncertain retry. These functional checks do not authorize an actual release or production Docker effects.

Fresh focused tests are required for the explicit Local `--test-module` route: validate discovery-bound relative selection and rejection of empty, duplicate, malformed, foreign, and symlink paths; prove selected-only execution and truthful focused scope/module reporting; and prove a selected failure or required skip blocks downstream Local delivery. Selected scope may include any discovered source module, including Docker modules, using the existing shared image and launcher handling. Retain prior unchanged-source evidence separately with its exact source binding; it is not folded into focused selection and does not support a full-suite or Public Full Gate claim. Omitting `--test-module` remains the full Local default, and public release still requires its separate complete Public Full Gate.
