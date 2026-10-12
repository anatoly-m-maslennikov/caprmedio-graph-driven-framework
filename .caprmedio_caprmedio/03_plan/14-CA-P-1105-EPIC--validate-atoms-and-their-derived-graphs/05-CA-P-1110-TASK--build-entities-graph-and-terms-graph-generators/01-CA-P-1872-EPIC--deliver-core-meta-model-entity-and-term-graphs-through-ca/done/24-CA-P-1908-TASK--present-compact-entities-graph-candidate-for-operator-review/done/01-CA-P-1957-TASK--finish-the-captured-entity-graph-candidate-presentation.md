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
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 2
updated_at: "2026-10-10 05:18:56 +0400"
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

### Completion receipt

Complete captured-snapshot candidate is persisted and reproduces byte-for-byte through the read-only verification path. All five preparation findings, full ancestor routing, Term-display direction and conditional-rule scopes are repaired. The earlier stale generated outputs were regenerated only within this Task's exclusive scope; accepted inputs were not changed.

- Inventory SHA-256: `f32588f6f9bc97e2180578c051bfbc73f39a7e80b7273bdf6702f9309778ed56`.
- Review SHA-256: `8b0d9c9ff3f940f3bfb4456aabda7b808060424a9910a194ff85a50073bcf975`.
- Manifest SHA-256: `fb9deec859a5f828e648d94da9d7888c50175872a70b9711e6a9f6a734ec81ce`.
- Renderer SHA-256: `3b18039bbfe8292d012b1944d3567d055ae9874dfb64e457fbad15716ede4260`.
- Canonical marked candidate JSON SHA-256: `0b26e7571ab4897f85e2b521255feb9f83e33c4f48ce86f02fd0a8f80c9303b1`; the source-file SHA remains separate.

All 706 primary identities, five explicit target/risk summaries, 117 questions and 123 blocked legacy relation chains remain visible. Ten Term proposals use broader / narrower display order and canonical narrower-to-broader direction. All seven shared rules state their applicability condition. Independent CA-P-1958 acceptance remains pending; this receipt is neither Operator approval nor native admission.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, exact source pins, verification evidence **or** required handoff is missing) **or** (a required prerequisite is **not** Done) **or** (an identity, question, proposal, unresolved reason **or** evidence is omitted **or** changed) **or** (a display relation is passed off as native admission) **or** (the checks fail **or** are unverified) **or** (uncertainty below 90% is silently resolved) **or** (own work exceeds 15 minutes without decomposition) **or** (work exceeds its exclusive scope)).
