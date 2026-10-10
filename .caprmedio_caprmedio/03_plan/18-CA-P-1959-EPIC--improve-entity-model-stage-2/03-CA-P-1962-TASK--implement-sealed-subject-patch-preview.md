---
atom_id: CA-P-1962
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 1
updated_at: "2026-10-10 22:32:47 +0400"
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

Extend the existing migration preview instead of using whole-frontmatter replacement. Inputs identify the current source hash, Atom ID/Version, field/index, exact old value and explicit new value. Do not infer replacements from candidate display paths or prose. A move between governs and depends_on must be an explicit paired operation, never a guessed consequence.

Validate the selected grammar profile, source spans and complete before/after Subjects shape. Preserve body and unrelated frontmatter bytes, including formatting and line endings. Preview the current Version +1 and new updated_at; include archive/history and Journal effects for the later approved execution. Seal the exact patch set and its before/after pins with a canonical hash.

Reject stale bytes, stale Version, ambiguous occurrences, invalid shape, collisions, overlapping patches, path escapes and symlink targets. Keep proposed grammar distinct from admitted grammar. Default to no writes. Do not add a standalone live apply path or weaken ATOM_UPDATE's existing admission guard. A live applier remains later work after exact preview approval.

Output: preview API/CLI support, focused tests and truthful limits. No authoritative Atom, history or Journal writes. Split work that exceeds 15 minutes.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if the preview is unsealed, stale input is accepted, unrelated bytes change, Version/timestamp/history implications are missing, targets are inferred, tests fail, or a live write boundary is weakened, any direct decomposing Plan is not Done, or own work exceeds 15 minutes without decomposition.
