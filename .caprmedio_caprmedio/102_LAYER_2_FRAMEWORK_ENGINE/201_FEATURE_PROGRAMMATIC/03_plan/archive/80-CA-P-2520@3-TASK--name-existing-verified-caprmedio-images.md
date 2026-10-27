---
atom_id: CA-P-2520@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 80
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 3
updated_at: '2026-10-21T09:34:20Z'
---
# Summary

Name existing verified CAPRMEDIO images

## Objective

Name existing verified CAPRMEDIO images.

## Details

After source/test acceptance, add repository/name and version/build-date tags to the exact positively identified existing CAPRMEDIO image IDs. Use Docker Created for original build date and verified embedded/release/Git source evidence for version. Never assign today's version or date to historical images, guess unknown version, touch unrelated images, move a tag owned by another image, delete/prune, rebuild, stop/restart or replace any container. Preserve runtime sha256 identity. At most15minutes own work; split before extending. Read back every changed image's RepoTags and report any unverifiable image as deferred with evidence.

### Verified checkpoint

Dependency review: P2518/P2522 independently accepted; root109tests and isolated canonical real build/reuse pass. Unknown-version cleanup is complete under separate P2523 authority. Proceed only with11source-proven inventory IDs using unchanged exact labels/Created and rechecked Git version proof, shared canonical display-tag helper and full readback. No container operation or moving occupied tag.

### Verified checkpoint

All11pinned source-proven historical/current images are now named caprmedio-runtime with exact verified0.4.4.3/0.4.4.7/0.4.4.9 versions, original DockerCreatedUTC and first12SHA. Fresh labels/Created and gitshow source-head version.toml rechecked before tags; all tags read back to same fullIDs. A preflight initially used the wrong TOML section and stopped before tags; corrected to framework.version. After all11tags succeeded, total-image-count assertion exposed one extra696-byte scratch image27b9017daa69 lacking Created; it is separately inspected, not included in this pinned maintenance or guessed. Existing12runtimeimages (11historical+1new) all named. Production unchanged.
