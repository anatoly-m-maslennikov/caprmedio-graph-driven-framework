---
atom_id: CA-P-1957
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
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 1
updated_at: "2026-10-10 05:16:00 +0400"
relations:
  is_decomposition_of: [CA-P-1908]
  blocks: [CA-P-1958]
---
# Summary

Finish the captured entity graph candidate presentation

## Objective

Finish a source-pinned candidate handoff without changing its reviewed meaning.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Start only after the parent's CA-P-1907 prerequisite is Done. Resume the unaccepted renderer checkpoint under `.caprmedio_caprmedio/_projection/core-entity-review/presentation/`; the preceding checkpoint is not a completion receipt.

Repair the five independent preparation findings: pin all accepted inputs; distinguish the CA-P-1938 acceptance-record hash from its actual Done Plan Carrier hash; preflight every output and parent path before exclusive creation; show all five actual consolidation/generalization targets and bounded risks; and visibly mark blocked legacy slash chains instead of declaring them narrower-than. RETAIN is a node meaning mark, not a relation clearance.

Produce `support/render_candidate.py`, `candidate.entities.indented.txt`, `candidate.review.md` and `candidate.manifest.json`. Preserve all 706 identities once in primary inventory, 584 retain marks, three consolidation proposals, two generalization proposals and 117 questions. Keep 17 Continuant, three Occurrent and four non-temporal anchors separate from 682 unclassified identities. Preserve the two unresolved drop annotations, seven conditional common rules, ten separate Term proposals and both RMED pointer views.

Validate accepted input hashes, captured commit `a971d0e00c33c779f485fc8cad63194894d440fb`, Done prerequisites at receipt commit `94776a14a368827a758534eb9c5c0109d649f309`, canonical candidate hash and file hashes separately. Dry-run must not write; persistence must never overwrite; verification must reproduce exact bytes. Handoff final hashes to CA-P-1958.

Exclusive scope is the derived presentation and assigned verification files only. No Core, Subjects, baseline, history, native admission, runtime, MCP, FPF, Git, push or PR writes. Inherit the parent's 90% confidence threshold; preserve uncertainty and ask rather than inventing an answer. The latest Substance Scope omission rule is full governed Subject AND full owning Scope Unit; otherwise Scope stays explicit.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, exact source pins, verification evidence **or** required handoff is missing) **or** (a required prerequisite is **not** Done) **or** (an identity, question, proposal, unresolved reason **or** evidence is omitted **or** changed) **or** (a display relation is passed off as native admission) **or** (the checks fail **or** are unverified) **or** (uncertainty below 90% is silently resolved) **or** (own work exceeds 15 minutes without decomposition) **or** (work exceeds its exclusive scope)).
