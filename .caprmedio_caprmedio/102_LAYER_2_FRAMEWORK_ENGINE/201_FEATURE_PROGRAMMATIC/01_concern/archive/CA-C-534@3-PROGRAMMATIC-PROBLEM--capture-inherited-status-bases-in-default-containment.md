---
atom_id: CA-C-534@3
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
  concern_about: [CA-P-2443, CA-R-1539, CA-D-461]
version: 3
updated_at: "2026-10-20T16:01:28.000Z"
---
# Summary

Capture inherited Status bases in default containment

## Concern

The default containment/reference binding path omits the Atom.Status base when composing inherited Role Status declarations. A supplied captured index works, but callers such as contained_atom_targets._bindings do not supply one.

## Evidences

The full frozen validator run executed530 tests and failed20 Plan prerequisite cases at _frontier_status_folders: inheritance requires one current Atom.Status declaration. The call chain is contained_atom_targets._bindings -> _frontier_status_folders(context, plans) -> declarations_from_sources(finite frontier rows), which contains inherited R1539 but no base. This is a current code-path defect exposed by frozen fixtures, not a claim that20 separate production requests failed. P2443 reuses canonical captured authority; missing/ambiguous bases must still refuse.

## Blast radius

Default contained Plan operations and prerequisite checks cannot prove their Status mapping. Keep imagefreeze blocked until this path and the complete frozen suite pass. No production endpoint call or historical replay occurred.

### Resolution checkpoint

The approved release proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record the repaired inherited-Status path completing 410 modules and 3680 tests with zero skips/failures. The released candidate is image `a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`. This resolves the deployment-blocked containment Status repair only; no broader containment/topology capability or historical batch replay is claimed.
