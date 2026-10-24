---
atom_id: CA-P-2383
content_role: Plan
type: Plan
label: Task
work_sequence_number: 61
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Projection, Plan]
version: 1
updated_at: "2026-10-14 13:07:36 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Avoid repeated identity parsing in Subject preparation

## Objective

Subject preparation reuses parsing of unchanged identity carriers within one invocation while preserving all fresh reads, validation and refusal checks.

## Details

A profiled single-Atom preview on a verified full source copy spent 76.022 of 77.301 seconds in identity audits. Parsing took 46.484 seconds; complete-carrier validation took 1.063 seconds. Profiling overhead and host filesystem differ from the connected Docker runtime. Optimize the measured repeated identity parsing only; do not infer batch performance from this sample.

Share exact-byte parsed identity results between preview checks and the native staging helper's initial/final previews. Keep fresh inventories, no-follow reads, byte and deadline limits, source/layout/grammar currentness, duplicate checks, complete candidate validation, seal equality and manifest readback. Reuse ends with the invocation. Do not change public requests, authority context construction, dependencies or the gateway deadline. Existing preparation rules permit this implementation change.

Add focused reuse-count and drift tests, independent review, and before/after profiling of the same pure preview. Existing real-gateway fixture tests in d2740da53 cover successful scratch staging and uncertain late effects without replay. Estimated implementation work: up to 15 minutes per subagent task.

No live staging, retry, Core repair or publication. Preserve the uncertain CA-D-253 batch. Deployment and connected completion remain separate under CA-P-2382. The 44-owner disposition remains unanswered.

### Definition of Done

Focused and existing affected tests pass; independent review finds no lost freshness/identity checks; identical-input profiling shows reduced repeated parsing with the same preview result. Commit only the reviewed logical change. This does not prove connected performance or complete the parent Epic.
