---
atom_id: CA-C-562
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-R-1901, CA-M-356]
version: 1
updated_at: "2026-10-21T09:20:17Z"
---
# Summary

Route Project MCP image build scratch to Project Temporary State

## Concern

The unchanged ProjectMcpBackend image resolver constructs ImageManager without an explicit Project Temporary State root, permitting a private build attempt under ambient system temporary storage.

## Evidences

Read-only source review found project_mcp_backend.ProjectMcpBackend.resolve_image(source_root, explicit_id) passes only source_root and timeout to ImageManager. Its build_temp_root default is None and _build passes that value to tempfile.mkdtemp. R1473/M289/E467 require configured Project Temporary State, not a host-temp fallback. The development Runtime.build path is fixed separately by P2522. Current canonical tagging acceptance supplies explicit .caprmedio_tmp and does not prove the ProjectMCP default path conforms. No production reproduction or filesystem cleanup was performed.

## Blast radius

This pre-existing caller-plumbing issue is deferred separately from the image display-name fix. Thread the selected Project's validated temporary root through the existing launcher/backend image boundary and consistent fixtures. Do not infer it from source_root: a readable installed package may be read-only and is not the selected Project. Preserve explicit source-root/fingerprint isolation, image SHA admission and Project/runtime safety. Use isolated representative fixtures and actual build-context readback before claiming acceptance. No interface, timeout, source permission or cleanup change is authorized by this Concern alone. Saved under the standing manual fallback after the separate native-admission timeout C561; no native create success is claimed.
