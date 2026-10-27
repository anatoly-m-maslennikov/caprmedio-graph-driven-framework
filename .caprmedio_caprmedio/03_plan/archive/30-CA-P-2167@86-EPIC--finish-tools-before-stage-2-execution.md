---
atom_id: CA-P-2167@86
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 30
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 86
updated_at: 2026-10-24 07:45:09 +0400
relations: {}
tier: 3
---
# Summary

Finish Tools before Stage 2 execution

## Objective

Maintain the unfinished Tools backlog and its independent evidence. This Plan does not gate Candidate #7 methodology edits or general Stage-2 planning.

## Details

### Current boundary — 2026-10-22

Candidate #7 is an approved, partially applied methodology-only continuation. Its direct source edits are independent of Tool implementation, implementation schemas, tests, MCP, Settings values and runtime. Those Tool concerns remain here as a separate Active backlog; this Plan update does not authorize code, runtime, migration or publication changes.

The obsolete Candidate #3/#4 migration prerequisites CA-P-1967, CA-P-1968, CA-P-1969 and CA-P-1909–CA-P-1912 no longer block this Epic or the approved Candidate #7 methodology work. Their historical decisions remain in their predecessor archives; do not replay or recreate those gates.

### Parent closure boundary

Before CA-P-1959 is marked Done, re-home this unfinished Plan bundle outside that Epic's containment tree, preserving IDs, statuses, child bundles and history and updating its containment/decomposition reference and affected current links. Until then, keep the parent Active: its Done cascade would otherwise cancel this independent backlog. This is a Plan-administration step, not a requirement to complete Tools or a new gate on Candidate #7 source edits.

### Independent Tools backlog

- [CA-P-2174 — Verify remaining Tools on isolated fixtures](30-CA-P-2167@86-EPIC--finish-tools-before-stage-2-execution/07-CA-P-2174-TASK--verify-remaining-tools-on-isolated-fixtures.md) remains an independent fixture-verification item.
- [CA-P-2382 — Verify connected Subject preparation](30-CA-P-2167@86-EPIC--finish-tools-before-stage-2-execution/60-CA-P-2382-TASK--verify-connected-subject-preparation.md) remains a future connected-Tool verification item; its incomplete staging/readback gate is not a methodology prerequisite.
- [CA-P-2256 — Implement TOML item and full-set edits](30-CA-P-2167@86-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits.md) remains Active for receiving work. [CA-P-2297](30-CA-P-2167@86-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/01-CA-P-2297-TASK--bind-toml-modifications-to-receiving-schemas.md) owns that remaining boundary; [CA-P-2307](30-CA-P-2167@86-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/done/02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text.md) is Done for the bounded TOMLKit selection packet.
- Other existing Tool children remain in their current locations and statuses. This repair does not close, cancel or rewrite them.

### Definition of Done

This Epic is Done only when each bounded Tool slice it retains has current accepted contract/source pins, implementation evidence where applicable, independently authored positive/negative/no-op/refusal checks and truthful effect/readback evidence. A fixture result, registry listing, prepared packet or source edit alone is not runtime readiness, migration approval or publication authority. Preserve stale-source refusal, no automatic replay, independent review and incomplete-result visibility.

Candidate #7 methodology application, its unresolved source mapping and its later graph rebuild are outside this Definition of Done and must not be blocked by it. No new code, schema, Settings, MCP, runtime, commit, release or migration result is claimed by this Plan update.
