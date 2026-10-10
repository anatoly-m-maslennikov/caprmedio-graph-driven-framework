---
atom_id: CA-P-1960
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
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 2
updated_at: "2026-10-10 23:24:00 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1961, CA-P-1962, CA-P-1964, CA-P-1976]
---
# Summary

Define safe Subject Tool contracts

## Objective

Define the lookup and preview contracts needed to repair Core RMEDO Subjects without changing authoritative Atoms.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Review the existing ATOM_SEARCH, ATOM_UPDATE, Subject migration planner and their current RMED+O. Produce a derived contract and gap list before implementation. Reuse existing readers, source pins and preview machinery; do not create a second Atom engine.

Specify field-aware lookup for governs, depends_on or both; exact and delimiter-aware prefix matching; explicit source root, owning Scope Unit, lifecycle and content-role filters. Each hit carries Atom ID, Version, relative source path, field/list index, exact value and source hash. Preserve the direction: governs names what this Atom governs; depends_on names what its content relies on. Neither field alone proves a native relation.

Specify explicit occurrence replacements, before/after bytes, current-version +1, a new updated_at, history/Journal implications and stale-source rejection. Ordinary preview changes only Subjects plus required revision metadata; Summary, Substance, Scope, Details and unrelated metadata stay byte-identical.

Select only the five allowed RMEDO roles. Specify exact old ID/Version preconditions, old Version +1, current Active/prior Archived history and actual effect-time metadata. Define an approved materialization contract for generated updated_at: seal its rule/allowed slot and record the final value and hash before writes. It cannot permit Subject/body substitution or let the preview claim an execution time.

Output only a derived contract, pinned audit evidence and acceptance cases. Tool implementation is approved; authoritative RMED/O changes are not approved by this Task. List missing authority separately. Split larger work before execution.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if the lookup or preview boundary is missing, reuse and authority gaps are unrecorded, the contract permits inferred targets or unapproved source writes, or its evidence is stale; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
