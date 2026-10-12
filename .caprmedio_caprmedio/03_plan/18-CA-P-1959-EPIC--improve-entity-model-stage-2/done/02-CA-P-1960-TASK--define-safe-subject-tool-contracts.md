---
atom_id: CA-P-1960
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
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 4
updated_at: "2026-10-11 00:12:22 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1961, CA-P-1962, CA-P-1964, CA-P-1976]
---
# Summary

Define safe Subject Tool contracts

## Objective

Compile the reviewed, source-pinned lookup and preview contracts needed to repair Core RMEDO Subjects without changing authoritative Atoms.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisite: CA-P-1978.

Use CA-P-1978's actually repaired and independently verified Tool RMEDO, exact pins and acceptance receipt. Compile a derived contract before implementation; do not create competing authority or re-decide its rules. Reuse the existing ATOM_SEARCH, ATOM_UPDATE, Subject migration planner, readers and source-pin machinery. A newly found authority gap returns to CA-P-1978's repair owner before code work.

Specify field-aware lookup for governs, depends_on or both; exact and delimiter-aware prefix matching; explicit source root, owning Scope Unit, lifecycle and content-role filters. Each hit carries Atom ID, Version, relative source path, field/list index, exact value and source hash. Preserve the direction: governs names what this Atom governs; depends_on names what its content relies on. Neither field alone proves a native relation.

Specify explicit occurrence replacements, before/after bytes, current-version +1, a new updated_at, history/Journal implications and stale-source rejection. Ordinary preview changes only Subjects plus required revision metadata; Summary, Substance, Scope, Details and unrelated metadata stay byte-identical.

Select only the five allowed RMEDO roles. Specify exact old ID/Version preconditions, old Version +1, current Active/prior Archived history and actual effect-time metadata. Define an approved materialization contract for generated updated_at: seal its rule/allowed slot and record the final value and hash before writes. It cannot permit Subject/body substitution or let the preview claim an execution time.

Output only the derived contract, current reviewed RMEDO pins and acceptance cases. This Task does not write authoritative Tool RMEDO; CA-P-1978 owns those repairs. Implementation stays blocked on the verified packet. Split larger work before execution.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Local execution receipt

Compiled the accepted source-pinned packet as `.caprmedio_caprmedio/_projection/core-entity-review/stage2/subject-tools.contract.md`: small valid-file lookup and exclusive pinned no-write patch preview, existing wrappers/parsing/complete-carrier validation and guards, actual migrations/history/Journal effects as separately approved ad-hoc scripts. All twelve accepted source pins and Project Structure remained current. No Tool authority, feature code or Core source changed. CA-P-1961/1962 implementation and CA-P-1976 question preparation may proceed.

### Definition of Done

The Plan is **not** Done if the lookup or preview boundary is missing, reuse and authority gaps are unrecorded, the contract permits inferred targets or unapproved source writes, or its evidence is stale; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
