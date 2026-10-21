---
atom_id: CA-P-2522
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2518]
version: 2
updated_at: "2026-10-21T09:32:38Z"
---
# Summary

Preserve development image handoff and display-tag safety

## Objective

Close bounded caller and metadata-boundary gaps found during independent P2518 review before image naming acceptance.

## Details

At most15minutes own work; split before extending. Preserve the existing build-to-start development journey without recreating a moving local alias: retain/print the canonical immutable digest and resolve a compatible existing image at explicit launch boundaries when no explicit digest is supplied. Do not introduce automatic builds or hidden Docker I/O in pure environment/command construction. Keep build scratch under the Project Temporary State using existing safe path checks. Treat inconsistent successful tag inspection as refusal, never absent; preserve another digest's occupied tag. Enforce Docker's tag-component length, preserve exact version and normalize only actual inspected Created UTC. Own only the canonical production image/build/launch seams; tests remain P2519-owned. Reuse R1901@4/M356@4/D594@6/E600@5 and the PROGRAMMATIC M/E/D view. Independent review plus real disposable Docker readback and unchanged immutable admission are required evidence. No production restart, new release, tag movement, historical version guess or held/uncertain replay. This child splits the follow-up before extending P2518's own-work bound; C560 remains open. Native authoring timeout C561 is not waived or treated as admission success; this planning record uses the standing manual fallback.

### Verified checkpoint

Reviewed canonical-owner follow-up accepted. Development build/start now hands off immutable IDs; explicit Project temporary root, ambiguous tag inspection and tag-component length boundaries are covered. Independent review APPROVE; included in root109/109 checks and isolated actual Docker build. No runtime adoption.
