---
atom_id: CA-P-2371
content_role: Plan
type: Plan
label: Task
work_sequence_number: 49
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 2
updated_at: "2026-10-14 06:07:19 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Verify minimum Subject Tool increment

## Objective

Independently review the actual D531 amendment, explicit dependency-set implementation and refreshed selected Subject fixtures after their producers finish. Run focused positive and negative tests; verify exact predecessor bytes and unchanged live Core sources. Record lookup exposure separately until its actual binding is implemented.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Definition of Done

Evidence covers actual final source/code/test pins and executed checks. Any failure or missing runtime path remains explicit. Do not close CA-P-2167 or infer live migration, content changes or broad connector completion from this bounded increment.

### Accepted bounded outcome

Independent D531 source review, connected-code review and fixture review passed. The code/source pins recorded by P2367/P2368/P2370 remain exact. Executed checks: 7 dedicated full-set tests, 49 existing preview/intent/by-value/staging regressions, 8 separate independent tests, 39 refreshed selected apply/portfolio/recovery checks and 3 real selected full-set tests all passed. The live Core's 906 source pins were independently rechecked unchanged during P2372's full request audit.

The new selected test uses the real isolated native publisher: LF/CRLF dependency collapse, Version +1, exact predecessor bytes/mode, current/history descriptors, two effects and actual Journal receipts. Tampered intent refuses; a changed reviewed candidate retains the existing interrupted_pending result with zero effects. Selected test SHA-256 `16bcc037a2353e62f442304207fcbf1459f99afb9b72c3f50cf5257f698c639b`.

No installed MCP round trip or host confirmation-provider readiness is established. The production selected manifest, public lookup/staging exposure and exact live migration approval remain open. P2167 stays Active; this closes only the verified local increment.

