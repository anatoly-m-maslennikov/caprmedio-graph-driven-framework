---
atom_id: CA-P-1962
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 5
updated_at: "2026-10-11 00:36:36 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1963]
---
# Summary

Implement sealed Subject patch previews

## Objective

Preview explicit Subject replacements with stale-source checks and exact preservation of unrelated content.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisite: CA-P-1960.

Add a small Subject-only preview mode to the existing Atom update surface for already-correct files. Inputs identify the current source hash, Atom ID/Version, field/index, exact old value and explicit new value. Do not use whole-frontmatter replacement, infer mappings or repair legacy files. Migration decisions and application remain in a later ad-hoc script, not this reusable Tool.

Validate the admitted flat Subjects shape, exact source spans and complete resulting file. Preserve body and unrelated frontmatter bytes, including formatting and line endings. Preview the current Version +1 and illustrative updated_at. Return the exact patch set, before/after pins and a canonical preview digest. Do not execute or fabricate archive/history/Journal effects; the later ad-hoc migration packet specifies them separately.

Check ID preservation and exact old Version +1. Bind actual effect-time updated_at using only the sealed metadata materialization rule; mark dry-run timestamps illustrative. Record both the sealed template and actual materialized after hash. All non-Subjects bytes remain unchanged except the specifically admitted Version/updated_at effects; history/Journal effects are separate named effects, not unspecified frontmatter changes.

Reject stale bytes, stale Version, ambiguous occurrences, invalid shape, collisions, overlapping patches, path escapes and symlink targets. Keep proposed grammar distinct from admitted grammar. Default to no writes. Do not add a standalone live apply path or weaken ATOM_UPDATE's existing admission guard. A live applier remains later work after exact preview approval.

Output: preview API/CLI support, focused tests and truthful limits. No authoritative Atom, history or Journal writes. Split work that exceeds 15 minutes.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if the preview is unsealed, stale input is accepted, unrelated bytes change, Version/timestamp/history implications are missing, targets are inferred, tests fail, or a live write boundary is weakened; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.

### Completion evidence

Implemented local Subjects-only preview in atom_subject_patch.py and the existing ATOM_UPDATE wrapper. Exact input pins and replacements bind one no-follow descriptor snapshot. Both the original and proposed complete carrier are validated; all batch sources are rechecked before returning. The existing apply guard remains intact. Preview has no source, history or Journal writer, and no MCP binding.

The ten focused tests passed, including injected source replacement, stale snapshots, full byte preservation and validator refusal. Independent code review passed after the source-read race was repaired. Root independently ran real no-op and non-no-op CLI previews against CA-R-866 with the complete validator, checked the canonical digest and default timezone-bearing timestamp, and confirmed unchanged Tool/Core sources and apply refusal. Exact pins and limits are in [_projection/core-entity-review/stage2/task-1962.receipt.json](../../../_projection/core-entity-review/stage2/task-1962.receipt.json). Later migration still needs grammar resolution, exact approval and an admitted application route.
