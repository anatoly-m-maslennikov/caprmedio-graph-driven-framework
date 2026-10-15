---
atom_id: CA-P-2340
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Configuration, Workflow, Plan]
version: 2
updated_at: "2026-10-13 22:13:02 +0400"
relations:
  is_decomposition_of: [CA-P-2295]
---
# Summary

Bind selected Scope Read receiver

## Objective

A private production O212 receiver binds the existing Scope Read adapter to an actual selected Action and RunExecutionSession.

## Details

### Current continuation checkpoint — 2026-10-13 22:13:02 +0400

The private O212 receiver now binds a genuine recorded Action/Session, independent sealed context, retained Settings/Structure pins and the existing reader. Author and independent tests passed; all 264 connector checks passed. Evidence is selected-read-receivers-checkpoint.md under the tools-first projection. No route was registered. Production complete Settings-schema validation is still an explicit dependency, not a fixture callback claimed as current policy. The Operator selected new-reader-only work with no legacy compatibility; existing Settings and callers must stay unchanged. This Task remains Active. Decompose remaining schema/production binding work into a new bounded child before further own implementation work.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; workers own disjoint implementation/test files and preserve other workers' edits. Inherit accepted parent RMEDO and independent review gates.

Reuse D625/D627/D527 and O212/M378 with current D441/D442 and applicable complete Settings/schema/read-permission authority. Fix logical request/context extraction privately from sealed route-owned D527 parameters; do not invent a public envelope. Retain ProjectSelection provenance for Settings then Structure without resealing drift. Require genuine Session and started Action, not a caller boolean. Invoke execute_scope_request and return its native result through the same Session; no second Run, live registration, guessed Workflow or Artifact/Journal Query alias. Read parsing/writing/CLI stay separate. Implement the smallest actual receiver with isolated genuine admission tests, complete output, missing/ambiguous/denied/stale/wrong-action cases and no source effects. Further O211/O047/O046 wiring remains separately bounded.

### Definition of Done

The outcome has exact current source/code/test evidence, actual positive/refusal checks and independent acceptance. Preparation, isolated helpers or source acceptance do not establish live/runtime completion. No unapproved policy, weakened guard, live Core migration or deferred capability is included.
