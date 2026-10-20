---
atom_id: CA-P-2444
content_role: Plan
type: Plan
label: Task
work_sequence_number: 33
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20 17:21:00 +0400"
---
# Summary

Normalize explicit Plan placement source paths

## Objective

Prevent doubled 03_plan path segments after current D461 v14 source alignment.

## Details

Review every consumer of D461 placement bullets. Use one existing canonical parser if available, otherwise one small shared source-path parser. Support the former local folder tokens and current explicit 03_plan/draft and 03_plan/archived paths without accepting traversal, absolute paths or unrelated role directories. Keep the observed six statuses and existing transitions/cascades intact. Freeze exact D461 v14 after Claim review; test scope-root Draft/Archived through the shared placement reader and affected functional callers. Do not invent a concrete nested archive hierarchy, incoming-link policy or edit-draft protocol. Record those separate limits and do not claim nested shared-placement acceptance. At most15minutes ownwork, split before extending. No production MCP/Docker/Git effects.

### Definition of Done

Current explicit paths do not double the role directory, malicious/malformed paths refuse, existing functional cases pass, and the rebuilt candidate includes this bounded compatibility fix.
