---
identity:
  id: CA-P-2791
  ref_id: CA-P-2791@15
context:
  container:
    scope_unit: CA-SU-14
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
  label: Epic
state:
  status: Archived
  version: 15
  updated_at: 2026-11-10 03:36:34 +0400
destination:
  file:
    name: CA-P-2791@15-EPIC--align-engine-implementation-with-the-refined-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2767
---


## Summary

Align Engine implementation with the refined specification

## Objective

Implement and verify the accepted code corrections identified by the Stage 2 specification review.

## Scope

ENGINE and its eligible descendants, including Workbench capabilities. Old non-Workbench Tools, the 500-Atom benchmark sources, the remaining prior Content migration hold (69 MED after the approved six-Atom C707 review), existing Archives/Drafts, standalone chat and actual native Codex rendering remain outside this active queue. C707–C710 source handoffs are resolved. The approved FRAMEWORK_DELIVERY local/public release implementation and test relocation is included only through P2839; other excluded legacy Tools and deferred sources remain excluded.

## Working procedure

Review and fix the next task before starting. RMED → review/fix → applicable M Policy prompt → RED plus non-Policy M → implementation → E2E → review/fix. Use Terra/Luna where efficient, one Scope Unit per agent, exclusive edit ownership and small Work Reports. Check the model, principles and latest Operator input when unsure; record remaining uncertainty as a C / Question and continue independent work. Specifications stay in RMED, not Tasks.

## Inputs

Stage 2 Current adoption, I7–I9, C711, C712 and the thin implementation map in CA-P-2767. Existing catalog and shared-server wiring is present; do not recreate it from an incomplete package-local search.

## Tasks

- [ ] [Confirm the adopted implementation inputs](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2811-TASK--confirm-the-adopted-implementation-inputs.md)
- [ ] [Fix Workbench editor completion](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2812-TASK--fix-workbench-editor-completion.md)
- [ ] [Reconcile Backend implementation and evaluator pins](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2813-TASK--reconcile-backend-implementation-and-evaluator-pins.md)
- [ ] [Verify MCP registration and discovery contracts](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2814-TASK--verify-mcp-registration-and-discovery-contracts.md)
- [ ] [Verify shared Workbench View and transport behavior](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2815-TASK--verify-shared-workbench-view-and-transport-behavior.md)
- [ ] [Review remaining Engine implementation evidence](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2816-TASK--review-remaining-engine-implementation-evidence.md)
- [ ] [Verify Engine performance and resource regressions](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2817-TASK--verify-engine-performance-and-resource-regressions.md)
- [ ] [Review and deliver the accepted Engine changes](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2818-TASK--review-and-deliver-the-accepted-engine-changes.md)
- [ ] [Relocate release implementation and tests](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2839-TASK--relocate-release-implementation-and-tests.md)

- [ ] [Add the query-inaccessible Atom audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2842-TASK--add-the-query-inaccessible-atom-audit-table.md)
- [ ] [Add the declared carrier consistency audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2843-TASK--add-the-declared-carrier-consistency-audit-table.md)
- [ ] [Add the physical carrier consistency audit table](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2844-TASK--add-the-physical-carrier-consistency-audit-table.md)

## Definition of Done

Accepted code corrections match Current RMED and pass their actual acceptance. Latency, throughput, resource use and scope boundaries do not regress. Current module pins describe implemented contracts only. Delivery is independently reported; skipped or deferred native acceptance is never called passed.

## Additional confirmed issue

C712: reproduce and fix stale deleted-Atom rows after a mixed source update/delete batch, with acceptance under E677. Include this in the Backend implementation task before combined regression verification. A full reread is verified recovery, not the incremental-path fix.

## Release implementation ownership

- CA-P-2839 — Relocate release implementation and tests. Backlog; blocked by the reviewed specification move CA-P-2837 and adopted-input confirmation CA-P-2811. The Operator chose specification now, implementation in this Epic.

## Current release source baseline

P2837 is Done. FRAMEWORK_DELIVERY / CA-SU-27 now owns the 80 local/public release specification Atoms. R3012@1 replaces the old RELEASES declaration without changing the Scope Unit ID or order. P2839 must use this Current source baseline. Review the retained pre-existing O184/O186 and archive-only D572 references before choosing any implementation repair; do not restore retired gates or invent replacements. Legacy unreadable D021 remains outside this adopted source frontier.

## Source prerequisite

The earlier Decision reviews in CA-P-2767 are complete. CA-P-2767 and the broader Summary merge pass P2840 are now Done; their reviewed adoption is query-verified and the source prerequisite is satisfied. The 89-Decision frontier was reviewed; 16 Forms were promoted, 73 Decisions retained, seven receiving delegations updated and one Evaluation carrier link repaired. The 24 adopted sources were queried back; no new Atom merge or implementation behavior was introduced. P2811 must select the Current source Versions, including the new shared Engine Method Policies M327/M328, before compiling implementation guidance. Keep the 69 held MED outside this queue. Existing Code Synopses remain factual code observations; reconcile old pins during the already-planned implementation review.

## First Summary merge source baseline

The first P2840 checkpoint adopted five groups; the final baseline below supersedes that partial checkpoint. P2811 must follow Current replacement lineage from R1522 to R1605, M169 to R1107, M178 to R1116, D705 to M509, and D676/D677 to R2782, and include the new M513 Method Decision where applicable. Historical module pins stay factual; reconcile them during the existing implementation map review. Do not restore the six retired contracts as separate Current sources. C712 was reproduced again during this adoption; full reread cleared five stale deleted-source rows, so the incremental-path fix and its E2E acceptance remain required.

## Final adopted source baseline

P2767 and P2840 are Done. Use the 33 applied groups in P2767/summary-merges.tsv: 48 retired contracts now resolve to their Current survivors. Include M513 and the new R3013 registry Requirement, plus the approved D366/D512/E525 reference-only repairs. Do not restore retired Methods/Deliveries as separate Current contracts. Before compiling guidance or reconciling I7–I9 and module pins, select actual Current Versions through the replacement lineage; retained historical pins remain factual evidence, not current implementation claims.

The six unadopted groups and all 69 deferred MED remain held. The 500 benchmark sources stay excluded. C712 still needs its incremental delete-path fix and E2E acceptance; a source reread is recovery only. Preserve the P2839 release relocation and P2842–P2844 audit work already in this queue.

Reconcile query extraction with the latest model-declared named Header values before policy compilation. A concurrent source lane adopted M514@2/M515@2 with lowercase role/form/status; live query exposes their Headers and Summaries but not their Claims. Check this under adopted-input confirmation, Backend extraction and the query-inaccessible audit work. Their source Atoms were not changed by this pass.

## Reopened source-evidence review

P2767 is Active again for P2845, reviewing recently created I7/I8/I9. The final Summary-merge baseline remains adopted. Keep P2811 Backlog until this bounded evidence review is integrated; do not infer that old Synopsis/module pins have already been reconciled with Current contracts.

## Code Synopsis review checkpoint

P2845 reviewed all three recent Synopses. Use Current I7/I8 at Version 2 as source evidence. P2812 must implement Current M468 and verify the two reproduced completion failures; passing workspace/helper tests are insufficient acceptance. P2813 retains the C712 mixed update/delete reproduction and exact pin reconciliation; static code-path presence does not resolve that Concern. Existing M500/D672 already cover the schema-asset distinction, so do not invent a relocation from missing package-local evidence.

MCP I9 adoption is held under C714/P2847 because concurrent code changes removed its selected-route registration file and changed dispatch code during review. Source I9 remains at Version 1. P2814 must use the freshly reviewed source state after that follow-up; do not restore removed code solely to match the old Synopsis. P2767 stays Active and this implementation Epic stays Backlog. No implementation or runtime acceptance was performed by the source review.

## Query delivery follow-up

- [ ] [CA-P-2852 — Implement query result files and Bookmarks](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2852-TASK--implement-query-result-files-and-bookmarks.md)

Use the adopted RMEDO and the small [Work Report](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2853-WORK_REPORT--2852.md). Source adoption does not establish implementation or release.

## New-source implementation follow-up

The generic Codex hook works independently of any plugin. Plugin and native side-panel work remain deferred. Specification changes are tracked in RMEDO Drafts; implementation remains separate.

- [ ] [CA-P-2859 — Fix newly found reader eligibility gaps](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2859-TASK--fix-newly-found-reader-eligibility-gaps.md)
- [ ] [CA-P-2860 — Implement session-bound Workflow Run reads](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2860-TASK--implement-session-bound-workflow-run-reads.md)
- [ ] [CA-P-2861 — Deliver and verify the standalone Codex hook](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2861-TASK--deliver-and-verify-the-standalone-codex-hook.md)

## Newly found content-reader follow-up

- [ ] [CA-P-2866 — Verify content extraction for admitted Engine carriers](CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2866-TASK--verify-content-extraction-for-admitted-engine-carriers.md)
