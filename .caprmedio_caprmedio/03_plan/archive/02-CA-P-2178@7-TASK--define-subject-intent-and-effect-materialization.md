---
atom_id: CA-P-2178@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Domain/Node/Continuant/Atom.Updated At
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 7
updated_at: 2026-10-24 11:41:03 +0400
relations:
  is_decomposition_of:
  - CA-P-2173
  blocks:
  - CA-P-2179
  - CA-P-2180
  - CA-P-2182
tier: 3
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

### Completion receipt

[Independent pure-intent verification](../../../../_projection/core-entity-review/stage2/tools-first/intent-and-application-status.md) passed for `atom_subject_patch.py` SHA-256 `0c2c7058470309820002ce9f97db8a2c30be17fe7726675658d4414c3633f218` and focused fixture SHA-256 `66450ddca99d5e2b605d180dd9f4de93939ec2339ae0b75ea0082017439ec03b`. Root's complete UPDATE suite passed 59 tests, including ten intent/materialization cases; SEARCH passed 49 separately. Source/grammar/evidence, old intended metadata, execution-time rule and exact predecessor destination are bound. Pure materialization revalidates inputs and computes proposed bytes without writing; no-op preserves Version/time and unrelated bytes/Status remain intact.

The later complete UPDATE run passed 66 tests after native preview/refusal cases were added; it supersedes the 59-test suite count rather than adding to it. That safe-path coverage does not accept changed-Subject publication.

This closes pure intent/materialization only. Successful concurrent-safe publication, restoration/history ownership, the full application portfolio and live capability remain unaccepted. The Operator deferred the concurrency design; live changed-Subject writes stay blocked pending the later design and actual verification. This receipt grants no publication mechanism or migration approval.

### Definition of Done

The Plan is **not** Done if current independent contracts are missing, intention and actual time remain conflated, a declared input is unbound, unrelated bytes/Status/guards regress, focused checks fail, writes occur, or own work exceeds 15 minutes without decomposition.
