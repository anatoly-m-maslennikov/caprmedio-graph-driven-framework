---
atom_id: CA-P-1958
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
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 1
updated_at: "2026-10-10 05:16:00 +0400"
relations:
  is_decomposition_of: [CA-P-1908]
---
# Summary

Verify the captured entity graph candidate presentation

## Objective

Independently verify the complete candidate handoff before Operator review.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1957. Check its Done receipt and exact output hashes before final verification.

Independently verify the final presentation against the fixed accepted node/ledger/structure/design/RMED/context inputs, captured Core commit `a971d0e00c33c779f485fc8cad63194894d440fb` and Done prerequisite receipt commit `94776a14a368827a758534eb9c5c0109d649f309`. Do not refresh Core or replay accepted producer writes.

Check all 706 exact original identities appear once in primary inventory; counts and five actual proposal targets match the marked review; 117 questions and two unresolved drop annotations remain questions; 17/3/4/682 display buckets do not silently classify other nodes. Inspect blocked legacy paths and the notation legend, both RMED references, seven inherited conditional rules and ten separately evidenced Term proposals. Distinguish acceptance-record versus Plan Carrier pins, canonical versus file hashes, and display roots versus ontology roots.

Exercise no-write reproduction and negative persistence guards in an isolated scratch area: late mismatch before any creation, symlink targets/parents, exclusive creation race, missing verification output and identical existing output. Preserve all accepted inputs and outputs. Write only `presentation/presentation.acceptance.md` and optionally `presentation/support/verify_candidate_presentation.py`, with exact hashes, checks and explicit limits. Any failed check goes back to the presentation owner; do not repair its outputs.

Exclusive scope is the derived presentation and assigned verification files only. No Core, Subjects, baseline, history, native admission, runtime, MCP, FPF, Git, push or PR writes. Inherit the parent's 90% confidence threshold; preserve uncertainty and ask rather than inventing an answer. The latest Substance Scope omission rule is full governed Subject AND full owning Scope Unit; otherwise Scope stays explicit.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, exact source pins, verification evidence **or** required handoff is missing) **or** (a required prerequisite is **not** Done) **or** (an identity, question, proposal, unresolved reason **or** evidence is omitted **or** changed) **or** (a display relation is passed off as native admission) **or** (the checks fail **or** are unverified) **or** (uncertainty below 90% is silently resolved) **or** (own work exceeds 15 minutes without decomposition) **or** (work exceeds its exclusive scope)).
