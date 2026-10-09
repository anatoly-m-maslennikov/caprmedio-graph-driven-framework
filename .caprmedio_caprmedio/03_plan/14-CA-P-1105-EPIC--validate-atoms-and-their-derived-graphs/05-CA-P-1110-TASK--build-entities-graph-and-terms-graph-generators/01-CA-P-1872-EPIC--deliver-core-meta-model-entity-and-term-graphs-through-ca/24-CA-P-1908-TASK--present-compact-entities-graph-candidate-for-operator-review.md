---
atom_id: CA-P-1908
content_role: Plan
type: Plan
label: Task
work_sequence_number: 24
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 6
updated_at: "2026-10-10 03:47:57 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1909]
---
# Summary

Present compact Entities Graph candidate for Operator review

## Objective

Give the Operator the new marked Entities Graph candidate in a compact, indented representation using the latest agreed notation.

## Details

Review context: the Operator chose **Finish against the captured snapshot only**. Use the original CA-P-1905 source pins and immutable Git commit `a971d0e00c33c779f485fc8cad63194894d440fb`; read `nodes/snapshot.context.md` and `nodes/support/snapshot_sources.py`. CA-D-494 revision 2 remains the review input; live revision 3 is outside this snapshot. Preserve originals and label receipts as captured-snapshot checks, not current-Core checks. Any currentness or source-pin requirement below means exact validity against this selected captured snapshot. Do not silently rebind or overwrite live Core.

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1907. Inputs: the pinned current-graph review, grouped/inherited candidate structure, complete occurrence-to-proposed-relation ledger and complete disposition ledger from CA-P-1905 through CA-P-1907.

Use these operators in the candidate display:
- `/`: broader to narrower; its canonical NARROWER_THAN direction is narrower to broader.
- `.`: bearer to dependent qualification, including Properties; canonical IS_BORNE_BY points dependent to bearer.
- `:`: Property to allowed value, never assignment; canonical IS_ALLOWED_VALUE_OF points value to Property.
- `@`: carried Entity to Carrier, using IS_CARRIED_BY; CARRIES is the opposite direction of the same binding.

Use graph concept names such as Version Number, Updated At and Status, not YAML keys such as version_number, updated_at and status. Preserve qualified identities, distinguish generic type constraints from actual instance bindings, and keep Entity/Term graph ownership explicit even in a combined compact display.

Present a plain two-space-indented view without tree connector glyphs, plus compact relation statements where a tree cannot show a cross-link. Show Continuant/Occurrent grouping, inherited shared rules, subtype differences, justified independent roots and visible DROP, CONSOLIDATE and GENERALIZE CANDIDATE marks. Include the Revision and Applicable Methodology proposals from CA-P-1907 with reasons and retained constraints. Marking is not deletion or acceptance of the proposal.

Present both CA-P-1906 views: separate R/M/E/D trees and an Entity-centered view with optional applicable M/E/D links. Distinguish presentation nesting from native Entity relations. Reuse shared source identities and Claims; do not fabricate mandatory M/E/D slots or copy a shared Claim into new authority. Keep R Entity-model notation separate from proposed Method/Evaluation links and D Carrier constraints. No new native graph kind is admitted by displaying these views.

Give a before/candidate comparison, root counts, traceable dispositions and unresolved questions. Preserve the step-1 baseline. A candidate is a proposal, not admitted native facts, Operator acceptance, a source migration or a completed MCP Run.

Output: the accessible candidate graph and review package, handed to the Operator for a decision before any Atom Subject changes. Hand off the full occurrence-to-proposed-relation ledger, node-disposition ledger, exact source pins and canonical hash of the candidate together, so that the decision is reproducible. Preserve every unresolved/not-native reason, check performed and required Operator question; those rows must not acquire an invented native proposal during presentation. Map and evidence every newly authored synthesized candidate Relation separately; do not give it a fake original source occurrence. The @ display operator is not automatically admitted into Subject-path serialization.

Exclusive scope: derived candidate outputs and their handoff evidence only. Do not implement a new graph frontend, modify Core Atoms or Subjects, overwrite the baseline, delete marked entities, rename YAML keys, activate a runtime, push or create a PR.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. These Tasks are created now; their work has not started.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability, source pins, canonical candidate hash, complete occurrence-to-proposed-relation ledger, node-disposition ledger **or** required handoff is missing) **or** (a handed-off relation cannot be traced either to its complete ledger row or to separate evidence as a newly authored candidate Relation) **or** (an unresolved **or** not-native row loses its reason, checks performed **or** required question **or** acquires an invented native proposal) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).
