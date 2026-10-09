---
atom_id: CA-P-1918
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 2
updated_at: "2026-10-10 02:24:11 +0400"
relations:
  is_decomposition_of: [CA-P-1906]
  blocks: [CA-P-1921]
---
# Summary

Review second context and operation relation batch

## Objective

Review the assigned old slash cases and produce an evidenced, candidate-only interpretation for the complete batch.

## Details

Child work only; no separately executable own work. A reviewed 16-case checkpoint is retained as input; the remaining 49 cases are split before further execution.

Required start prerequisite: CA-P-1905. Inputs: the completed pinned baseline and the explicit partition or design contract.

Assigned partition: Bucket 3, sorted cases 67–131. The input is the matching `batch-6.input.json` in `.caprmedio_tmp/planning/core-entity-review/design/`, bound to CA-P-1905's inventory.

For every assigned case, record its case ID, original parent and child, disposition, proposed operator and canonical Relation with graph ownership and direction where evidenced, confidence_percent, reason, checks performed, exact Main Content evidence spans with Atom ID/revision/path/hash, and any question. An unresolved or not-native case has no asserted native proposal or new endpoints. Preserve the case rather than forcing a slash/dot decision. Syntax-only decisions remain explicitly display-only; a Carrier binding needs its independent evidence.

Preserved checkpoint: `relations.batch-6.json` (16 reviewed display-only cases; 49 unreviewed rows). It is not the completed review. CA-P-1923–1926 review disjoint remaining partitions; they explicitly BLOCK CA-P-1927, which joins the final 65-case output in `relations.batch-6.final.json`. Each original case occurs exactly once; no case outside this partition is changed.

Direct child Tasks:
- [CA-P-1923](06-CA-P-1918-TASK--review-second-context-and-operation-relation-batch/01-CA-P-1923-TASK--review-first-remaining-context-relation-batch.md): Review first remaining context relation batch.
- [CA-P-1924](06-CA-P-1918-TASK--review-second-context-and-operation-relation-batch/02-CA-P-1924-TASK--review-second-remaining-context-relation-batch.md): Review second remaining context relation batch.
- [CA-P-1925](06-CA-P-1918-TASK--review-second-context-and-operation-relation-batch/03-CA-P-1925-TASK--review-third-remaining-context-relation-batch.md): Review third remaining context relation batch.
- [CA-P-1926](06-CA-P-1918-TASK--review-second-context-and-operation-relation-batch/04-CA-P-1926-TASK--review-fourth-remaining-context-relation-batch.md): Review fourth remaining context relation batch.
- [CA-P-1927](06-CA-P-1918-TASK--review-second-context-and-operation-relation-batch/05-CA-P-1927-TASK--join-the-reviewed-second-context-relation-batch.md): Join the reviewed second context relation batch.

Read current Core Main Content and verify exact source pins before proposing meaning. Earlier classification caches are preparation only. Below 90% confidence, leave a proposal unresolved, state the missing evidence and put the question to the Operator before deciding. A diagnostic or proposed view is not native admission. Preserve all qualified identities and do not infer Entity facts from source Atom metadata or Subject incidence. Work locally without MCP or FPF; do not change Core Atoms, Subjects, history, baseline outputs, implementation, runtime or unrelated work.

### Definition of Done

the Plan is **not** Done **if** ((the assigned batch is incomplete, duplicated or mixed with another partition **or** an evidenced proposal lacks a current Main Content span **or** an unresolved row silently asserts a native relation) **or** (a required start prerequisite is **not** Done) **or** (the stated output or handoff is missing) **or** (uncertainty below 90% is silently decided or its question is not put to the Operator) **or** (source pins or checks are stale) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
