---
atom_id: CA-C-535
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2442, CA-R-1022]
version: 3
updated_at: "2026-10-20T16:01:28.000Z"
---
# Summary

Validate resolved Concern target qualified Types

## Concern

Concern target admission checks carried identity, Role, Version and admitted Status, but a generic Role Status fallback alone does not prove the target qualified Type is admitted.

## Evidences

Independent review found check_graph_extended target admission did not call the existing shared source-bound schema Role/Type validator. A role-bearing target with an unknown Type can therefore pass that mechanical slice. The literal Type label Revision is not itself a standalone entity; no arbitrary string ban is warranted. P2442 reuses the existing qualified Type schema and preserves extension uncertainty and ordinary RMED Type omission.

## Blast radius

Only valid Current Atom targets are eligible under R1022v17. Invalid/unresolved Type declarations must remain failures/gaps rather than being admitted by generic Status membership. Do not invent missing Type contributions or semantic validation; retain explicit unsupported schema cases.

### Resolution checkpoint

The approved release proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record the repaired qualified-Type path completing 410 modules and 3680 tests with zero skips/failures. The released candidate is image `a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`. This resolves the deployment-blocked qualified-Type repair; the existing unsupported IType boundary, historical batch behavior and broader capability remain unchanged.
