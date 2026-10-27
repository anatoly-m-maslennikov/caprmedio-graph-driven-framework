---
atom_id: CA-P-2188
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Canceled
subjects:
  governs: Subject
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Node/Engineering/Continuant/Tool
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2045
tier: 3
---
# Summary

Integrate fresh Candidate-3 Subject reviews

## Objective

Persist one fresh occurrence ledger from independently accepted current per-source reviews.

## Details

### Current mapping-disposition checkpoint — 2026-10-14 15:18 +0400

The mapping-disposition gate is complete under CA-P-1959's latest map-first, Subjects-only override. Earlier requirements below for all 48 deep per-owner reviews, separate per-packet semantic receipts, completion of their descendants and the old domain partitions are not prerequisites to this migration slice. Preserve those Plans and reports as historical evidence without claiming them Done or creating a completion cascade. This checkpoint supplies the current process, output and pin binding where older text conflicts; it does not rewrite old receipts or reopen the superseded deep-review gates.

The integrated occurrence map is `.caprmedio_tmp/stage2-migration-20261014/subject-map/subject-map.current.json`, SHA-256 `647f7a91ca166a9cfd08560f1303cfb2cc7d2724848dc50794cd1eee78e062f8`. Its current Candidate #4 pin is `.caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.model.candidate-4.md`, SHA-256 `a23019a1ee6cd3586640d6c3d9e211091f3683ac5f136058d745650570e78ca7`, verified equal to live candidate bytes. All 906 owners and 4,530 occurrences have migration dispositions: 611 mapped-change candidates, 266 unchanged, 17 unchanged deferred-model owners, 10 unchanged uncertain owners and two unchanged pending retirement. Zero occurrences lack a disposition. All 29 excluded owners retain all 155 occurrences, including 44 otherwise-changeable mappings; no supported subset of an excluded owner enters the request. The 34 null targets and 11 open meaning questions remain visible and unadopted. An approved unchanged disposition is not a guessed meaning or completion of the deferred non-Atom revision model.

Independent mapping-disposition check: `.caprmedio_tmp/stage2-migration-20261014/subject-map/mcp-readiness-checkpoint.md`, SHA-256 `83105d77652a6e6735a79496669e8c72ff231b143d4c40cb8606dafe719f7635`, identifies the exact current map and verifies complete owner/occurrence coverage, whole-owner exclusions and zero undisposed occurrences. Its earlier MCP baseline observations remain historical; use P1959/P2167's latest connected checkpoint for Tool/runtime state. For this Subjects-only slice, P2188's persisted integration and P2189's independent migration-disposition verification are satisfied by these current outputs and checks, not by unfinished old deep-review children. No full Atom-content semantic review or new FPF acceptance is claimed.

Keep the captured inventory/map provenance unchanged: `.caprmedio_tmp/stage2-migration-20261014/inventory/current-subjects.inventory.json`, SHA-256 `9226df3fcc8b57ca4c15908ed08e61899ea41c6aa32e1bd24c5ff4658efc2344`. The separate structural repair changed 44 source pins without changing approved Subject intent; do not silently present their older captured paths/Versions/hashes as current. The refreshed current-source binding is `.caprmedio_tmp/stage2-migration-20261014/structural-repair/request-generation/manifest.json`, SHA-256 `4347f853b7f7c88f3b89759621a3aa1cb0fa2f3dd25152f17b23ef7f3dbb67f5`. All its 906 source hashes were rechecked against live files; all 611 public expected ID/Version/hash tuples agree with it. The repaired-source validation receipt is `.caprmedio_tmp/stage2-migration-20261014/structural-repair/repaired-full-validation.json`, SHA-256 `9e981c76434bbce68d7c539ba569093bd3ac6af649c605f11f4473ab346468fe`.

Prepared public request: `.caprmedio_tmp/stage2-migration-20261014/structural-repair/request-generation/preview-subjects.request.json`, SHA-256 `3b931baa1c07fc50fb42668c63407543632c50b05c69540815bd794f54ebdc5c`, containing exactly 611 owners and 848 ordered Subject patches. Metadata/provenance remains outside the closed payload. The captured original conversion's independent receipt, `.caprmedio_tmp/stage2-migration-20261014/public-request/independent-review.md`, SHA-256 `a08be8e25dfeb01e97ce1d800622bded1eb8778482092597b286609521aac481`, stays historical to its exact original pins; the structural-repair generation explicitly records the 44 rebindings and preserved mapping intent, order and exclusions. Request preparation is complete and explicitly non-executable; it is not candidate Atom bytes, whole-request MCP acceptance or staging/publication approval.

Status remains Active in this checkpoint-only packet by explicit instruction, not because superseded deep-review prerequisites still bind. Remaining migration gates concern actual admitted Tool/runtime completion, an explicitly assigned and approved scratch tranche with exact staged-diff/preservation proof, the selected Codex human-confirmation trust decision, current selected-source admission and separate exact live-packet approval. Those responsibilities remain with the applicable preparation/staging/application Plans; they do not keep the completed mapping-disposition gate open. Preserve original sources, ordinary content, history, Journal and both uncertain D253 batches. No new stage, replay, migration, publication, broad connector/catalog/C+A work or content-epic execution is authorized here.

### Current frontier and output binding — 2026-10-14

Consume P2193's fresh 48-packet frontier: 906 owners/4530 occurrences, index `.caprmedio_tmp/stage2-migration-20261014/inventory/batches/batches-index.json` SHA-256 `6e234a12a6ae03d846fc22933b9fd94d8c9b6d169415d24a2217250611895af4`, inventory `.caprmedio_tmp/stage2-migration-20261014/inventory/current-subjects.inventory.json`, SHA-256 `9226df3fcc8b57ca4c15908ed08e61899ea41c6aa32e1bd24c5ff4658efc2344`. Apply P2193's precise archived-R1433 membership reconciliation and inherited destination override. Current reports are in `.caprmedio_tmp/stage2-migration-20261014/reviews/` and this integration's ledger is in `.caprmedio_tmp/stage2-migration-20261014/review/`; preserve the old captures/reports/receipts under `20261012` without overwriting them or inheriting semantic acceptance. Existing `.caprmedio_tmp/stage2-migration-20261012/model/` decisions and Candidate #4 pins remain unchanged. All stated fresh-review, full-coverage, whole-owner disposition and independent-acceptance prerequisites remain binding; this reference reconciliation does not complete integration or release staging.

Estimated own work: 15 minutes for one integration AI Agent, assuming existing deterministic ledger mechanics. Required inputs: CA-P-2187 and CA-P-2193 Done, with every current source-packet Plan and its bounded review/assembly descendants complete, independent semantic receipts for reviewed meanings and actual accepted-content/coverage checks for assembly. Pin the current inventory, Candidate #4, [base Operator decisions](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/operator-subject-decisions.md), SHA-256 `ce28c370232ae43829036714eb24957987d11453fd94a76c4794997b088ecfb5`, additive [compact scope-reference decision](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/scope-reference-decision.md), SHA-256 `df2303d0128ca9b882e2877f41ebc2f17f2c9fc2ce4a3a7ffefa394000d249c0` and [approved content-conflict exclusions](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`, with complete disjoint source ownership. Old CA-P-2050–2056 domains or matching historical bytes are not those reviews.

Apply inherited CA-P-1959/2193 guidance against [Candidate #4](../../../../../_projection/core-entity-review/presentation/operator.model.candidate-4.md), SHA-256 `6e63d7362514ef20c2551366777073c22300b35a9cef5ad79531ad56b770763d`. Entity is only the umbrella. The three top-level branches are Occurrent, Continuant and Carrier. Continuant explicitly excludes Carrier and contains Object, Actor, History, Projection and Selection. Object is authoritative content about what/how; Actor is who. Actual executions and sessions are Occurrents, not their Journal records. History contains Journals, records and Revisions; Projections are derived content, including Terms Graph. A Selection is a rule/expression; running it is an Occurrent, and a saved/tracked result is a Projection. A Carrier bears a representation without becoming that content. Term annotations preserve source meanings, allowed values and derived vocabulary, not another root. No new native Relation semantics, parser/schema change or Core adoption follows from this candidate. Before execution, inherit CA-P-1959's Candidate #4 review and repair gate, including the completed historical review, Operator dispositions and bounded independent consistency verification of the authorized repairs against the revised target. Affected work waits for that parent check; revised bytes do not inherit the historical analytical PASS. The unchanged full FPF review is not rerun, and no Core adoption or migration is implied. Recheck meanings and obtain current independent acceptance; keep older model/report pins historical and unchanged.

Root owns the single derived ledger under `.caprmedio_tmp/stage2-migration-20261014/review/`. Cover every source/occurrence once, including supported, unchanged, unresolved and excluded/finding records, with source-specific governs/dependency meaning and preserved qualifiers. Keep below-90% mappings unadopted and unstaged until the Operator answers. Preserve raw reports and source bytes. Deliver the persisted ledger/hash, coverage reconciliation and exact remaining questions to CA-P-2189; do not infer graph acceptance or live approval. Split a concrete overrun before execution.

Reconcile all 906 owners and 4530 occurrences. A confirmed content conflict records a whole-Atom staging exclusion, its ID/Version/source hash, contradictory source and candidate/Operator evidence, reason and explicit CA-P-1970 queue entry. Excluded originals remain byte-unchanged and visible as unmigrated in inventory/graph coverage; do not stage even a supported subset of that owner. Mark eligible only independently accepted, fully supported whole-owner Subject changes. Missing coverage, uncertainty or weak evidence must not be relabeled as content conflicts; their existing investigation/Operator gates remain. No partial unreviewed set completes this ledger.

Bind the [approved unchanged unresolved-owner decision](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/unresolved-owner-decision.md), SHA-256 `d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`, separately from confirmed content conflicts. Persist that separate whole-owner list in the complete ledger with exact Atom ID, Version, source path/hash, affected occurrences, reason and open question. An uncertain required mapping leaves the entire original Atom unchanged and all its rows unstaged, even when some rows are supported. Preserve raw report/model/decision pins rather than rewrite historical receipts; bind this additive answer explicitly in integration. Retain unresolved owners in inventory and BEFORE/AFTER coverage, without automatically queuing CA-P-1970. Reconcile all 906 owners/4530 occurrences and obtain independent acceptance of supported meanings and every disposition before staging only other fully supported whole owners; uncertainty never excuses missing review coverage.

### Definition of Done

Not Done if a fresh batch/independent receipt is missing, a pin or model binding is stale, coverage overlaps/omits an occurrence, uncertainty is silently resolved or mislabeled as a content conflict, a confirmed content-conflict exclusion lacks exact whole-owner evidence/preservation or its CA-P-1970 queue, the separate unresolved-owner disposition/pins/occurrences/reason/open question or unchanged coverage is missing, old approval is reused, source/content bytes change or own work exceeds 15 minutes without decomposition.
