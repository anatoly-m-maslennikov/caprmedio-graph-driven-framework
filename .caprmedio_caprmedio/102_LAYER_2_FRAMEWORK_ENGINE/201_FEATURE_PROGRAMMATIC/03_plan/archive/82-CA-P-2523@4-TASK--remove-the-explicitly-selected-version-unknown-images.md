---
atom_id: CA-P-2523@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 82
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 4
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Remove the explicitly selected version-unknown images

## Objective

Remove only the eighteen inventory-pinned historical CAPRMEDIO images whose framework version could not be verified, as explicitly directed by the Operator.

## Details

At most15minutes own work; split before extending. Exact target inventory is .caprmedio_tmp/image-tags-20261021-ABiLEA/image_inventory.json rows with verifiedVersion=null; bind all eighteen immutable IDs and fresh schema/labels/Created before effects. The latest Operator answer just remove them supersedes the earlier leave-untagged/unknown-tag options and earlier no-deletion boundary only for those exact images. Use Docker non-force image removal; do not prune, expand by age/name/date, remove known-version/new images, volumes/build cache or containers, stop/restart anything, or touch the current running MCP digest. Preserve any image referenced by a container and report that distinct blocker; container removal needs separate explicit authority. Read back exact per-ID absence and verify current MCP/container identity unchanged. Image deletion is not a recoverable trash operation; retained inventory/metadata is not a backup of image bytes. Normal image naming source/tests and the container queue continue independently; no release or production mutation test is authorized. Manual planning uses the standing fallback after C561 native admission timeout, not a fabricated native success.

### Exact deletion result and additional Operator authorization

Initial image-only non-force pass removed16of18exactunversionedimages; bfb07ac21a79 and399b668feb3d were retained because6stoppedworker/agenttestcontainersreferencedthem. Receipt .caprmedio_tmp/image-tags-20261021-ABiLEA/unknown-image-removal-receipt.json pins full image/container IDs; current MCP e81250f8ed4c and image08f26a9b8b14 remain unchanged/healthy. The Operator now explicitly approves removal of those6stoppedtestcontainers and then those2images, acknowledging their logs/writable-state deletion. This latest authorization supersedes the earlier no-container-removal bound only for those exact6IDs. Recheck every container is still stopped and bound to the selected2images, use no force and no volume removal, then verify exact absence and unchanged production. No age/glob/prune or other stopped-container cleanup is authorized.

### Verified checkpoint

Fresh exact stopped/image checks passed. Removed16initial unknown-version images, then the separately authorized6stopped worker/agent containers and final2unknown-version images, non-force and without volumes. Exact IDs and receipts retained in .caprmedio_tmp/image-tags-20261021-ABiLEA. Production container/image unchanged and healthy. Container logs/writable state and images have no undo/backup.
