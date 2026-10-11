---
atom_id: CA-P-2045
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 15
updated_at: "2026-10-11 08:47:03 +0400"
relations:
  is_decomposition_of: [CA-P-2043]
  depends_on: ["CA-P-1972","CA-P-2044","CA-P-1992","CA-P-1993","CA-P-1994","CA-P-1995","CA-P-1996","CA-P-1997","CA-P-1998","CA-P-1999","CA-P-2000","CA-P-2001","CA-P-2002","CA-P-2003","CA-P-2004","CA-P-2005","CA-P-2006","CA-P-2007","CA-P-2008","CA-P-2009","CA-P-2010","CA-P-2011","CA-P-2012","CA-P-2013","CA-P-2014","CA-P-2015","CA-P-2016","CA-P-2017","CA-P-2018","CA-P-2019","CA-P-2020","CA-P-2021","CA-P-2022","CA-P-2023","CA-P-2024","CA-P-2025","CA-P-2026","CA-P-2027","CA-P-2028","CA-P-2029","CA-P-2030","CA-P-2031","CA-P-2032","CA-P-2033","CA-P-2034","CA-P-2035","CA-P-2036","CA-P-2037","CA-P-2038","CA-P-2039","CA-P-2040","CA-P-2041","CA-P-2042"]
  blocks: ["CA-P-1967","CA-P-1909"]
---
# Summary

Integrate reviewed current Subject mappings

## Objective

Create the complete current occurrence ledger only after all review and acceptance gates pass.

## Details

Own work: none after initial ledger creation. CA-P-2057 owns the remaining independent persisted-ledger verification and research registration. Execute only after CA-P-2044 and all 51 review Tasks are Done. Missing or uncertain meaning remains explicit research; bounded follow-ups cover it before this group completes. Keep the existing CA-P-1909–1912 accepted-graph/approval/application route unchanged. No candidate acceptance or live migration approval is inferred.

Read and follow current-subjects.contract.md and current-subjects.review.contract.md. No Core, captured review, grammar, native admission, MCP/FPF, runtime or source mutation. Root owns integration and Git. This Plan records work, not completion.

### Decomposing Plans

CA-P-2086–2093 are Done, with one commit per completed Task. The full current working ledger covers 907 sources and 4534 occurrences: 1468 proposed, 1540 unchanged and 1526 unresolved. All 33 current grammar-source rows are independently re-reviewed (15 proposed, 18 null) and included. Eight quarantined sources remain explicit. The strengthened independent live gate and 14 wrong-data/control tests pass; the ordinary lookup/update/graph suites also pass (296 tests). Exact evidence is `_projection/core-entity-review/stage2/checkpoint-working-ledger-2026-10-11.json`. This is a complete progress ledger, not complete semantic mapping or authorized source adoption. Original Core Subjects/content remain unchanged; the selector choice and final 1909–1912/1969 gates remain open.

- [CA-P-2086 — Consolidate reviewed Subject mapping layers](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/04-CA-P-2086-TASK--consolidate-reviewed-subject-mapping-layers.md)
- [CA-P-2088 — Verify the working Subject ledger independently](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/05-CA-P-2088-TASK--verify-the-working-subject-ledger-independently.md)
- [CA-P-2089 — Audit accepted mapping layer provenance](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/06-CA-P-2089-TASK--audit-accepted-mapping-layer-provenance.md)

- [CA-P-2057 — Verify the persisted ledger and track research](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/01-CA-P-2057-TASK--verify-the-persisted-ledger-and-track-research.md)

CA-P-2094–2099 are Done: 180 exact current origins across 134 owning sources, with eighty supported proposals and one hundred justified nulls. Each final report has independent semantic acceptance, current pin/span/coverage checks, a receipt and a separate commit. Their raw reports remain immutable evidence. CA-P-2100–2102 integrate these findings into the current derived ledger; the earlier 1468/1540/1526 counts above are the prior Git-preserved checkpoint, not the forecast integration result.

- [CA-P-2100 — Integrate accepted subject-family research](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/07-CA-P-2100-TASK--integrate-accepted-subject-family-research.md)
- [CA-P-2101 — Verify accepted subject-family layers independently](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/08-CA-P-2101-TASK--verify-accepted-subject-family-layers-independently.md)
- [CA-P-2102 — Rebuild and check the current subject ledger](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/09-CA-P-2102-TASK--rebuild-and-check-the-current-subject-ledger.md)

Current integration checkpoint: CA-P-2094–2102 are Done. The six independently accepted reports cover 180 current origins across 134 owning sources (80 proposals, 100 explicit nulls). Their findings are now included in the live-verified derived ledger: 1548 proposed, 1540 unchanged, 1446 unresolved across 907 sources and4534 occurrences. Eighteen verifier tests and296 ordinary tool tests pass; ten complete-ledger wrong-data controls reject bad variants. Original Core Subjects/content remain unchanged; eight quarantined sources and the unanswered selector choice remain open. Exact evidence is `_projection/core-entity-review/stage2/checkpoint-subject-families-2094-2099.json`. This is progress, not full mapping or migration approval.

CA-P-2103–2108 are independently accepted:183 exact origins,100 supported proposals and83 nulls. CA-P-2109–2111 integrate this continuation without changing authority.

- [CA-P-2109 — Integrate accepted subject-family research](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/done/010-CA-P-2109-TASK--integrate-accepted-subject-family-research.md)
- [CA-P-2110 — Verify accepted subject-family layers independently](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/011-CA-P-2110-TASK--verify-accepted-subject-family-layers-independently.md)
- [CA-P-2111 — Rebuild and check the current subject ledger](02-CA-P-2045-TASK--integrate-reviewed-current-subject-mappings/012-CA-P-2111-TASK--rebuild-and-check-the-current-subject-ledger.md)

### Definition of Done

Completion checkpoint: CA-P-2089 is Done. Accepted layer provenance is verified for 14 final mapping reports/receipts and 647 selected decided rows; current Core evidence matches 374 files and 381 unique spans. Historical Plan context is separate from live Core meaning. CA-P-2087 remains excluded at this checkpoint.

Not Done if the assigned output or required checks are missing/stale, evidence or coverage failures are hidden, source writes occur, completion exceeds actual evidence, or own work exceeds 15 minutes without decomposition.
