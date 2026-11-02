---
atom_id: CA-P-2523
content_role: Plan
type: Plan
label: Task
work_sequence_number: 82
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-21T09:23:16Z"
---
# Summary

Remove the explicitly selected version-unknown images

## Objective

Remove only the eighteen inventory-pinned historical CAPRMEDIO images whose framework version could not be verified, as explicitly directed by the Operator.

## Details

At most15minutes own work; split before extending. Exact target inventory is .caprmedio_tmp/image-tags-20261021-ABiLEA/image_inventory.json rows with verifiedVersion=null; bind all eighteen immutable IDs and fresh schema/labels/Created before effects. The latest Operator answer just remove them supersedes the earlier leave-untagged/unknown-tag options and earlier no-deletion boundary only for those exact images. Use Docker non-force image removal; do not prune, expand by age/name/date, remove known-version/new images, volumes/build cache or containers, stop/restart anything, or touch the current running MCP digest. Preserve any image referenced by a container and report that distinct blocker; container removal needs separate explicit authority. Read back exact per-ID absence and verify current MCP/container identity unchanged. Image deletion is not a recoverable trash operation; retained inventory/metadata is not a backup of image bytes. Normal image naming source/tests and the container queue continue independently; no release or production mutation test is authorized. Manual planning uses the standing fallback after C561 native admission timeout, not a fabricated native success.
