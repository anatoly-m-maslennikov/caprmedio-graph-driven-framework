---
atom_id: CA-P-2178
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
  governs: Tool
  depends_on: [Atom, Subject, Revision, Plan]
version: 1
updated_at: "2026-10-12 04:16:55 +0400"
relations:
  is_decomposition_of: [CA-P-2173]
  blocks: [CA-P-2179, CA-P-2180, CA-P-2182]
---
# Summary

Define Subject intent and effect materialization

## Objective

Expose the existing planner's exact time-independent Subject intent and pure execution-time byte materialization.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Production prerequisites: CA-P-2170 and its corresponding current packet independently accepted under CA-P-2171. Reopen planner callers first; bind those contracts and implementation pins.

Exclusive edits: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_patch.py` and new `ATOM_UPDATE/tests/test_subject_intent_materialization.py` under that Tools directory. Other workers own native publication, route integration and independent fixtures; do not revert their work. Coordinate any shared helper change through integration.

Reuse no-follow, current eligibility and exact byte-span planning. Provide a deterministic one-target intent/hash that binds Subject replacements, source/grammar/evidence and the allowed effect-time metadata rule, excluding illustrative or actual timestamp values from the approved intended identity. Pure materialization accepts the declared actual Project-time context and computes exact Version +1/updated_at bytes and final after hash; it performs no source/history/Journal writes. No other generated slot, Summary/Type change or standalone apply is admitted.

Check LF/CRLF and all untouched bytes, intended Status, source/grammar/evidence drift, undeclared metadata and invalid time context. Any changed intended effect changes its hash. Deliver the bounded API, exact pins and focused results to CA-P-2179/2180 and independent verification. Split before execution if concrete work exceeds 15 minutes; do not add flexibility or a general migration framework.

### Definition of Done

The Plan is **not** Done if current independent contracts are missing, intention and actual time remain conflated, a declared input is unbound, unrelated bytes/Status/guards regress, focused checks fail, writes occur, or own work exceeds 15 minutes without decomposition.
