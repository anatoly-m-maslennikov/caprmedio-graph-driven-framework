---
atom_id: CA-P-1910
content_role: Plan
type: Plan
label: Task
work_sequence_number: 26
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
version: 2
updated_at: "2026-10-10 23:24:00 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1911, CA-P-1968, CA-P-1973]
---
# Summary

Prepare the accepted Core Subject migration preview

## Objective

Prepare an exact, sealed migration preview for the verified accepted Core graph without changing authoritative sources.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

CA-P-1967 supplies the sole source-pinned candidate packet and must be Done before final preview acceptance. Reuse that packet, current grammar/profile and post-grammar Tool verification; do not create a second independent approval route.

Readiness condition: CA-P-1909 is Done. Inputs: its verified accepted graph, canonical hash, current source pins, recorded Operator decision and complete occurrence and node ledgers. Candidate or graph approval is not migration approval.

Produce an exact file-and-patch preview. Classify every change as Subject-only, a required governed grammar change, or necessary revision/history maintenance. Bind each patch to its current source bytes, authoritative identity and revision, expected after bytes, accepted decision and ledger rows. Keep excluded and unchanged source files pinned. Identify any change beyond these categories as outside scope and request separate authority.

Preview `/`, `.` and `:` using currently admitted Subject serialization or exact proposed grammar-contract revisions needed for the accepted notation. If the current grammar does not admit a required operator, include its precise proposed governed revision in the sealed preview. An isolated dry-run may evaluate that proposed grammar, but must identify it as proposed, claim no admission and write no authority. `@` remains compact graph display notation, not admitted Subject syntax; retain source-backed IS_CARRIED_BY/CARRIES bindings separately. Unsupported Carrier bindings, new ontology Claim meanings or unrelated semantic changes require separate RMED authority, not an invented serializer or automatic grammar admission.

Output: the sealed exact patch preview and its canonical hash, before/expected-after source pins, change classification, expected graph output, read-only dry-run proof, and verification/recovery plan. Reproduce the accepted qualified nodes, relations and ledgers in an isolated preview without writing the authoritative Core or grammar carriers. State how failures will be detected and how approved recovery would preserve exact revisions and history; do not infer rollback permission.

Exclusive scope: preview, isolated derived dry-run outputs and review evidence only. No authoritative Subject, grammar, metadata, history or implementation writes; no baseline overwrite, runtime activation or live MCP execution. Hand the exact sealed preview to the Operator for separate migration authorization. Full native MCP delivery remains separate and pending.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold. Split into bounded direct child Plans before execution if the ready work cannot fit 15 minutes. Creation of this Task does not start, authorize or complete this stage, and implies no MCP Run or Journal receipt.

### Definition of Done

the Plan is **not** Done **if** ((CA-P-1909 is **not** Done) **or** (the exact sealed preview, canonical hash, file/patch classifications, before/after pins, expected graph output, dry-run proof **or** verification/recovery plan is missing) **or** (a patch lacks an accepted decision, ledger mapping **or** current governing authority) **or** (unsupported syntax, Carrier binding **or** semantic changes are silently admitted) **or** (authoritative sources, grammar, history, implementation **or** the baseline were changed) **or** (a required check is failed, stale **or** unverified) **or** (uncertainty below the confidence threshold was silently resolved **or** work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
