---
atom_id: CA-P-2518
content_role: Plan
type: Plan
label: Task
work_sequence_number: 78
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
updated_at: "2026-10-21 12:52:33 +0400"
---
# Summary

Implement versioned and dated CAPRMEDIO image names

## Objective

Implement versioned and dated CAPRMEDIO image names.

## Details

Reuse the canonical image owner to give newly built CAPRMEDIO images an inspectable repository/name and tag containing the actual framework version and UTC build date; carry matching standard image metadata. Read current runtime/release RMED and reconcile its precise display-tag permission before implementation. Derive version from the exact source/package boundary, never a live checkout fallback. Preserve immutable sha256 selection, fingerprint and Project isolation, no moving an existing tag, no latest alias, and no runtime replacement. Include development and test builders in the affected closure. At most15minutes own work; split before extending. Acceptance is a frozen source change reviewed against caller/build-context closure; tests are P2519.
