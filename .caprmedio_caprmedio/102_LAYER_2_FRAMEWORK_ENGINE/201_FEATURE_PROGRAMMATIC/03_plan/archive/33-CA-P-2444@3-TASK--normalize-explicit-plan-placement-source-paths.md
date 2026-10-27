---
atom_id: CA-P-2444@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 33
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 3
updated_at: 2026-10-24 06:04:44 +0400
tier: 3
---
# Summary

Normalize explicit Plan placement source paths

## Objective

Prevent doubled 03_plan path segments after current D461 v14 source alignment.

## Details

Review every consumer of D461 placement bullets. Use one existing canonical parser if available, otherwise one small shared source-path parser. Support the former local folder tokens and current explicit 03_plan/draft and 03_plan/archived paths without accepting traversal, absolute paths or unrelated role directories. Keep the observed six statuses and existing transitions/cascades intact. Freeze exact D461 v14 after Claim review; test scope-root Draft/Archived through the shared placement reader and affected functional callers. Do not invent a concrete nested archive hierarchy, incoming-link policy or edit-draft protocol. Record those separate limits and do not claim nested shared-placement acceptance. At most15minutes ownwork, split before extending. No production MCP/Docker/Git effects.

### Definition of Done

Current explicit paths do not double the role directory, malicious/malformed paths refuse, existing functional cases pass, and the rebuilt candidate includes this bounded compatibility fix.

### Completion checkpoint

Accepted report confirms shared `_plan_folder`/`_plan_mapping` normalize legacy and explicit `03_plan` paths, reject unsafe paths and duplicate labels, and derive mapping completeness from the captured Status domain. Native/contained/reference callers were reused; exact frozen D461 v14 source hash is `270f5d90c4591a9f6d42265d44e5f5c45418ee9981c70b2031e3d8eba3c7bf06`, with real temporary Root Draft/Archived admission tests and 13 intentional legacy fixtures retained. Focused checks passed 126; root FINAL validator passed 535 with 0 skips/errors/failures; peer review passed. The later human flatten policy (D461 v15/E502 v13) affects nested Archived only, leaving root paths unchanged; nested flat implementation is deferred under C539 and C536 is resolved. No nested/runtime acceptance or production pin refresh is claimed.
