---
atom_id: CA-C-564
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2527, CA-P-2529, CA-M-332, CA-E-539]
version: 1
updated_at: "2026-10-21T10:50:11Z"
---
# Summary

Refresh Local release source-conformance evidence

## Concern

Current Local release source-size and inherited lint debt lacks an exact current accepted bounded exception under E539. Functional acceptance of Project-only retention does not establish whole-source conformance. Refresh the explicit bounded evidence/acceptance or make a separately scoped cohesive reduction; do not suppress findings or widen this retention change into an unrelated runner rewrite.

## Evidences

Independent review found the historical P2167 exception records703physical lines/C90158, not the current runner. Current local_release.py is771physical lines; run_local_release has264tokenized logical lines. Pinned Ruff against exact HEAD and current source yields the same four diagnostics: _copy_tree C90113, _prepare_package C90113, run_local_release C90159 and inherited E731 lambda. No new/worsened Ruff diagnostic is claimed, but that is not a fresh size waiver.

Changed cleanup.py/identity.py/images.py are120/92/127physical lines and all executable units are at most25logical lines. The modified cleanup test files are225/235physical lines, up from199/192; their executable units are at most25logical lines and their Ruff checks pass. Do not call these file-size increases inherited unchanged debt. Record their applicable bounded exception or perform cohesive test-fixture splitting in separately scoped work. The pinned Mypy target contains VALIDATE_ATOMS, not these release modules; no strict-typing pass is claimed for them.

Independent functional-safety review approves the retention diff. Root frozen10-module synthetic gate102/102 passed9.632s, separately from the earlier102/102 run16.084s. No real Docker, full Local release, deployment, version bump or push was performed. Measurements and functional evidence do not imply runtime adoption or full E539 acceptance.

## Blast radius

Maintainability, source reviewability and accuracy of readiness/conformance claims for Project Local release and its focused tests. This is not evidence of unsafe Docker cleanup, a new production incident or permission to change unrelated functionality. Current retention invariants and all runtime/ownership/refusal guards remain binding.
