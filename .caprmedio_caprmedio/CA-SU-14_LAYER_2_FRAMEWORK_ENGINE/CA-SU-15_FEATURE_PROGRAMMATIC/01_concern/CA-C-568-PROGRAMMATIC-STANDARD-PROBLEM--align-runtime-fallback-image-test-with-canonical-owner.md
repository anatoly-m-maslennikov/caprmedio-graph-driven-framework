---
atom_id: CA-C-568
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2536, CA-P-2542, CA-O-164]
version: 2
updated_at: "2026-10-21T13:14:49Z"
---
# Summary

Align runtime fallback image test with canonical owner

## Concern

The full suite's runtime fallback-image assertion references a no-longer-exported constant, causing AttributeError before it checks actual image behavior. Correct the test's expected value owner without adding a redundant runtime compatibility export or changing image selection.

## Evidences

Run local-20261021-network-recovered-120901 log lines5456-5475: test_image_override.py ran5 tests with1error; runtime.IMAGE absent. Current docker/runtime.py imports IMMUTABLE_IMAGE and image_reference from docker/image_reference.py, whose IMAGE remains caprmedio-runtime:local. Repo search finds only this test uses runtime.IMAGE. The same module's explicit immutable-image, bridge and malformed-override cases pass. Actual publication25/25 and affected Docker3/3 passed in this run. Remaining suite continues under source freeze to collect other failures; no green release is claimed.

## Blast radius

Full Local-release gate and accuracy of fallback-image regression coverage. No demonstrated production image-selection defect. Keep immutable override validation and canonical development fallback unchanged. Correct only the actual stale test dependency after full-suite terminal state, then focused checks/review and a fresh complete release gate.

### Focused source acceptance and next boundary

P2542 fixed only the stale test constant-owner reference; all14related override/metadata checks passed0.280s, with independent approval and pinned Ruff/diff clean. No production fallback or immutable-image behavior changed. The complete old Run remains failed; latest Operator requires only broken/related reruns, not a full green HEAD claim.
