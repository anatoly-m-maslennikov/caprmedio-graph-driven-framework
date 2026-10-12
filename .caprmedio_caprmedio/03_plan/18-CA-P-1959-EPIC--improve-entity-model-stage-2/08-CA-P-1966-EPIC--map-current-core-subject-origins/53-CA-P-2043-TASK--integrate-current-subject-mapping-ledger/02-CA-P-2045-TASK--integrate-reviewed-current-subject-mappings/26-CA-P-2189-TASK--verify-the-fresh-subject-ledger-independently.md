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
version: 2
updated_at: "2026-10-12 16:31:39 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  blocks: [CA-P-2190]
---
# Summary

Verify the fresh Subject ledger independently

## Objective

Independently accept the persisted fresh ledger and its current-source/model bindings.

## Details

Estimated own work: 15 minutes for one AI Agent independent of integration, assuming separately authored mechanical checks and completed semantic-review receipts. Required inputs: CA-P-2187 and CA-P-2188 Done plus every current source-batch independent receipt. Reopen actual persisted bytes and pins, not only producer output.

Independently reconcile all source/occurrence/excluded/finding coverage with the inventory, source spans, proposal grammar, Candidate #3/latest decisions and confidence/acceptance evidence. Verify source-specific whole-Subject changes as well as governs/depends_on direction. Use a separately authored expected ledger/oracle and prove deliberate missing, duplicate, stale, wrong-proposal and altered-output cases fail; do not call the producer to establish expected meaning. Deliver the ledger-verification receipt and exact eligible supported tranche inputs. This permits temporary Subject staging only, not final graph acceptance, source mutation or content work. Split a concrete overrun before execution.

Apply the [approved content-conflict exclusions](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc` with the unchanged base decisions and additive [compact scope-reference decision](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/scope-reference-decision.md), SHA-256 `df2303d0128ca9b882e2877f41ebc2f17f2c9fc2ce4a3a7ffefa394000d249c0`. Independently verify complete 907-owner/4534-occurrence reconciliation, every confirmed whole-Atom content conflict's ID/Version/hash, contradictory source/model/Operator evidence, reason and CA-P-1970 queue, and unchanged original bytes plus inventory/graph presence. Verify that eligible tranche inputs contain only fully supported independently accepted whole owners and no excluded owner's rows. Prove deliberate false conflict classification, hidden/partial owner exclusion and selection of an excluded owner fail. Uncertainty or weak evidence is not a conflict exemption, and no unreviewed coverage is admitted.

### Definition of Done

Not Done if output is self-verified, fresh semantic acceptance/coverage is missing, wrong-output controls fail, a below-90% proposal enters adopted/stageable rows, a content-conflict exclusion is unevidenced/partial/hidden or loses its unchanged original/CA-P-1970 queue, uncertainty is used as an exemption, actual pins differ, authority changes or own work exceeds 15 minutes without decomposition.
