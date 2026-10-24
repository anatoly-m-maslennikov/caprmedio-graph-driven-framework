---
atom_id: CA-C-541@2
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2450]
version: 2
updated_at: "2026-10-20T14:29:47.000Z"
---
# Summary

Repair the shared legacy Subject status fixture

## Concern

The shared legacy Subject fixture omits the inherited Atom.Status base R1947 after R1539 snapshot inheritance. The broad full suite fails with `complete-carrier-invalid`; this is a fixture-authority diagnosis, not a reproduced production failure.

## Evidences

The exact failing log is `.caprmedio_tmp/simple_local_release/local-20261020-current-target-parser-repair-1412-tests-v6q0b3c7.log`. The release report is `runtime/...sameRunid.md`; exit 130 is `KeyboardInterrupt` because the root intentionally stopped the known-failing attempt. The disposable pre-complete-carrier check failed on the missing base; adding static R1947 SHA `ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f` makes complete preflight and preview pass.

## Scope and owner

Shared owner: `201_TOOLS/tests/test_selected_atom_lifecycle.py`; the worker copied one CA-R-1947 source line with SHA `ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f` after the R1539 snapshot inheritance. Preserve the inheritance and do not weaken validation. No production change or product-cause claim is made.

### Resolution checkpoint

The bounded fixture correction is complete. The seven affected host-test counts `1, 4, 12, 10, 22, 10, 7` total 66/66 passed. This resolves the confirmed shared-fixture cause only; broad full-suite verification remains pending P2440. No production change, product-cause finding, Docker/deployment acceptance, or release completion is claimed.
