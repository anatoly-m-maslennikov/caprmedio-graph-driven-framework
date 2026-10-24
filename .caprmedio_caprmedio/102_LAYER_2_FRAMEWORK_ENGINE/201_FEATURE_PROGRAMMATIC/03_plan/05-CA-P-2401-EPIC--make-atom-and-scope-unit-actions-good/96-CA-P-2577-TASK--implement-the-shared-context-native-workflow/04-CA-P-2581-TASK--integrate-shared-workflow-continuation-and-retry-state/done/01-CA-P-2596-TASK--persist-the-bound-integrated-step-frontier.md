---
atom_id: CA-P-2596
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
version: 4
updated_at: "2026-10-22T16:28:06Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2581]
  depends_on: [CA-P-2579, CA-P-2595]
  relates_to: [CA-R-1527, CA-R-1843, CA-R-1845, CA-M-328, CA-D-544, CA-O-016]
---
# Summary

Persist the bound Integrated Step frontier

## Objective

Retain the exact Project, frozen Workflow/Step/Action, current source/candidate/packet digests, actual Run receipts and one-use continuation identity in the existing selected Run directory. Journal delivery is not a state/admission gate.

## Details

At most 15 minutes of own work per leaf; split before expanding. One Task per file. Review and update dependent Tasks after actual predecessor acceptance and before execution. Current source R1527@7 defines Integrated as the current participating session; a separate ephemeral CLI is not an Integrated implementation. Preserve existing native packet fields and current M/E/D guidance, explicit Project binding, source freshness, actual evidence and business-only Journal semantics. Use locked uv and configured Project Temporary State. Create a Concern for a real unresolved decision or blocker. No feature work before CA-P-2595 acceptance; no release, deployment, production MCP calls, full-suite run, uncertain replay or Git publication.

### Definition of Done

Retain exact changed paths/source bindings, focused functional and source-conformance evidence, observed limitations and the reviewed next dependent Task. Count fixture integrity, implementation, pending/current-session execution and runtime admission separately.

### Reviewed parallel storage boundary — 22 October 2026

Independent storage execution is Active after CA-P-2579 and CA-P-2595 acceptance. The store uses opaque bound-frontier data and does not import or weaken the Action validator. Implement CAS/one-use receipts, Project/Run isolation, bounded safe persistence, Project Temporary State atomic staging and concurrent/crash coverage. Coordinate a run-lock transaction so admit/resume/publish cannot deadlock on nested flock. Preserve consumed A receipts when B becomes pending; exact retry returns its retained receipt without advancing B. Use the existing selected Run directory owner. Journal completeness is not a state gate. Current Action result semantics and graph/MCP integration remain separately held.

### Storage and checkpoint decomposition — 22 October 2026

This Task is now a zero-own-work container. Split the expanded persistence responsibility before further execution: CA-P-2603 stores one-use frontier/receipts (Done after independent PASS and root 14 focused checks); CA-P-2604 checkpoints canonical Run-session mutations (Active, at most 15 minutes); CA-P-2605 restores verified session/output state without provider replay (Backlog, at most 15 minutes, after CA-P-2604 acceptance). Root ownership includes canonical atomic evidence staging and its two focused regressions; shared project_runtime safety has ten focused checks. All new persistence uses the existing selected Run directory and canonical Project Temporary State; no Journal completeness gate.

CA-P-2597 stays gated on acceptance of this complete container and CA-P-2580; graph integration may prepare against the stated APIs but is not admitted or complete from store-only success. The Method input universe question remains open, so no production selector or inventory is inferred from the caller packet.

### Complete persistence container accepted — 22 October 2026

Done after CA-P-2603, CA-P-2604 and CA-P-2605 acceptance. Root independently ran 14 frontier tests, five checkpoint checks and six evidence IO regressions; independent targeted reviews passed the store and checkpoint surfaces. Canonical temporary staging has separate focused checks. This closes persistence only, not graph continuation or public MCP admission. Review/admit CA-P-2597 against the accepted APIs before its execution; current Method sources may be refreshed by the separately coordinated Methodology Subjects batch, so never repin a live moving frontier or rewrite frozen tests.
