---
atom_id: CA-R-1879
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-11 16:46:21 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Currentness"
  depends_on: [Tool, Workflow Run, Artifact, Revision, Digest, Methodology]
relations:
  relates_to: [CA-R-1876, CA-R-1877]
---
# Summary

Freeze the executing release and pin candidate currentness

## Scope

The N-to-N+1 boundary during candidate construction, testing, installation, and rollback.

## Claim

Release Version **must** keep the executing Framework, active runtime pointer, and project-local `ca` Skill at frozen N while constructing and testing a separately pinned N+1; the full suite must pass before separately staging/installing N+1, and promotion may select N+1 only after installed-package and actual candidate-image gates also pass.

## Details

Candidate N+1 may be retained separately after its suite gate, but N remains the runnable rollback point and active public selection until promotion. The executing Run never silently substitutes candidate definitions, and first-cut verification never invokes another release. Changed N, retained snapshot bytes, candidate output digest, captured test environment, or image identity blocks the affected promotion rather than being refreshed in place. Current definitions and active sources are discovered and captured internally at Run start; later authoring edits do not replace the retained release payload or require a manually maintained revision refresh. Exact executing definition evidence, current authorization, target-state checks, and applicable definition revalidation remain required.
