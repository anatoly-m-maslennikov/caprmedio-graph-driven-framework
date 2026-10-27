---
atom_id: CA-P-2189
content_role: Plan
type: Plan
label: Task
work_sequence_number: 26
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject
  depends_on: [Atom, Entity, Projection, Plan, Tool, Operator]
version: 7
updated_at: "2026-10-14 00:51:17 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  blocks: [CA-P-2190]
---
# Summary

Verify the fresh Subject ledger independently

## Objective

Independently accept the persisted fresh ledger and its current-source/model bindings.

## Details

### Current frontier and output binding — 2026-10-14

Independently verify P2188's persisted ledger under `.caprmedio_tmp/stage2-migration-20261014/review/` against P2193's 906-owner/4530-occurrence current frontier. Exact index pin: `.caprmedio_tmp/stage2-migration-20261014/inventory/batches/batches-index.json`, SHA-256 `6e234a12a6ae03d846fc22933b9fd94d8c9b6d169415d24a2217250611895af4`; inventory pin: `.caprmedio_tmp/stage2-migration-20261014/inventory/current-subjects.inventory.json`, SHA-256 `9226df3fcc8b57ca4c15908ed08e61899ea41c6aa32e1bd24c5ff4658efc2344`. Current packet reports are in `.caprmedio_tmp/stage2-migration-20261014/reviews/`; new independent ledger receipts belong in `.caprmedio_tmp/stage2-migration-20261014/verification/`. Inherit P2193's archived-R1433 reconciliation and unchanged other packet ownership. Preserve all `20261012` captures/reports/receipts as historical evidence, while retaining its pinned model decision records as current inputs. Candidate #4, reviewed-meaning, complete-coverage, wrong-output controls and separate independent semantic-acceptance gates are unchanged. No acceptance, staging release or live authority is inferred from refreshed references.

Estimated own work: 15 minutes for one AI Agent independent of integration, assuming separately authored mechanical checks and completed semantic-review receipts. Required inputs: CA-P-2187 and CA-P-2188 Done plus every current source-batch independent receipt. Reopen actual persisted bytes and pins, not only producer output.

Apply inherited CA-P-1959/2193 guidance against [Candidate #4](../../../../../_projection/core-entity-review/presentation/operator.model.candidate-4.md), SHA-256 `6e63d7362514ef20c2551366777073c22300b35a9cef5ad79531ad56b770763d`. Entity is only the umbrella. The three top-level branches are Occurrent, Continuant and Carrier. Continuant explicitly excludes Carrier and contains Object, Actor, History, Projection and Selection. Object is authoritative content about what/how; Actor is who. Actual executions and sessions are Occurrents, not their Journal records. History contains Journals, records and Revisions; Projections are derived content, including Terms Graph. A Selection is a rule/expression; running it is an Occurrent, and a saved/tracked result is a Projection. A Carrier bears a representation without becoming that content. Term annotations preserve source meanings, allowed values and derived vocabulary, not another root. No new native Relation semantics, parser/schema change or Core adoption follows from this candidate. Before execution, inherit CA-P-1959's Candidate #4 review and repair gate, including the completed historical review, Operator dispositions and bounded independent consistency verification of the authorized repairs against the revised target. Affected work waits for that parent check; revised bytes do not inherit the historical analytical PASS. The unchanged full FPF review is not rerun, and no Core adoption or migration is implied. Recheck meanings and obtain current independent acceptance; keep older model/report pins historical and unchanged.

Independently reconcile all source/occurrence/excluded/finding coverage with the inventory, source spans, proposal grammar, Candidate #4/latest decisions and confidence/acceptance evidence. Verify source-specific whole-Subject changes as well as governs/depends_on direction. Use a separately authored current-model ledger/oracle that checks branch/non-root Term distinctions and source/history/projected-view qualifiers; prove deliberate stale-model acceptance, missing, duplicate, stale, wrong-proposal and altered-output cases fail; do not call the producer to establish expected meaning. Deliver the ledger-verification receipt and exact eligible supported tranche inputs. This permits temporary Subject staging only, not final graph acceptance, source mutation or content work. Split a concrete overrun before execution.

Apply the [approved content-conflict exclusions](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc` with the unchanged base decisions and additive [compact scope-reference decision](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/scope-reference-decision.md), SHA-256 `df2303d0128ca9b882e2877f41ebc2f17f2c9fc2ce4a3a7ffefa394000d249c0`. Independently verify complete 906-owner/4530-occurrence reconciliation, every confirmed whole-Atom content conflict's ID/Version/hash, contradictory source/model/Operator evidence, reason and CA-P-1970 queue, and unchanged original bytes plus inventory/graph presence. Verify that eligible tranche inputs contain only fully supported independently accepted whole owners and no excluded owner's rows. Prove deliberate false conflict classification, hidden/partial owner exclusion and selection of an excluded owner fail. Uncertainty or weak evidence is not a conflict exemption, and no unreviewed coverage is admitted.

Bind the [approved unchanged unresolved-owner decision](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/unresolved-owner-decision.md), SHA-256 `d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`, separately from confirmed content conflicts. Independently verify each separate unresolved-owner entry's exact Atom ID, Version, source path/hash, affected occurrences, reason and open question against its complete fresh review. Verify the entire original stays byte-unchanged and visible in inventory and BEFORE/AFTER graph coverage, and none of its rows enter the staged payload. Do not infer a confirmed contradiction or automatic CA-P-1970 queue. Extend the existing negative controls to reject hidden/partial unresolved-owner disposition, mixing that list with confirmed conflicts, and selecting any unresolved owner's supported subset. Accept dispositions as dispositions, not unsupported meanings; complete all 906-owner/4530-occurrence review and ledger checks before releasing only other fully supported whole owners.

### Definition of Done

Not Done if output is self-verified, fresh semantic acceptance/coverage is missing, wrong-output controls fail, a below-90% proposal enters adopted/stageable rows, a content-conflict exclusion is unevidenced/partial/hidden or loses its unchanged original/CA-P-1970 queue, unreviewed coverage is excused as uncertainty or the separate unresolved-owner disposition/preservation is missing, actual pins differ, authority changes or own work exceeds 15 minutes without decomposition.
