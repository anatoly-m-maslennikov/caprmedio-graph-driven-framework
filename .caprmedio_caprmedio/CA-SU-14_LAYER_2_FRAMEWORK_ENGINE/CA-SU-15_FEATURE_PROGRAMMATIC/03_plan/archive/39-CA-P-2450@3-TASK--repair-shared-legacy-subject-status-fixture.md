---
atom_id: CA-P-2450@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 39
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 3
updated_at: '2026-10-20T14:32:38.000Z'
---
# Summary

Repair the shared legacy Subject status fixture

## Objective

Apply the bounded fixture correction for inherited Atom.Status authority and run the focused dependent modules.

## Details

Current owner: `201_TOOLS/tests/test_selected_atom_lifecycle.py`. Add the static R1947 source with SHA `ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f` after R1539 snapshot inheritance, preserving the shared legacy Subject fixture contract. Run only the focused dependent checks; do not broaden into a full-suite release attempt. No production change, validation weakening, deployment, or Git effect.

At most15minutes ownwork, split before extending. Preserve exact diagnostic evidence and concurrent edits.

### Definition of Done

The shared fixture contains the inherited R1947 Atom.Status authority and the focused dependent modules pass with the complete-carrier preflight/preview boundary recorded. This narrow Task does not claim a broad full-suite pass, production acceptance, or release completion.

### Completion checkpoint

The worker copied one CA-R-1947 source line with SHA `ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f` into `201_TOOLS/tests/test_selected_atom_lifecycle.py` after R1539 snapshot inheritance. Seven affected host-test counts `1, 4, 12, 10, 22, 10, 7` total 66/66 passed. No Docker validation or broad full-release claim is made.

Follow-up host proof adds 48 base checks and 14 stage checks. Combined affected host proof is 128 checks (`66 + 48 + 14`); no Docker validation or broad full-release claim is made.
