---
atom_id: CA-P-2484@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 60
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 6
updated_at: 2026-10-24 06:04:44 +0400
tier: 3
---
# Summary

Resolve flat Plan archive destinations

## Objective

Use the existing Atom publication owner to resolve owning Scope Unit 03_plan/archived for newly archived Plan Markdown carriers and required new exact predecessor records.

## Details

At most 15 minutes own work; split before extending. CA-D-461@15, CA-E-502@13 and C539 govern. Review P2481 findings and wait for P2478 accepted frozen source. Own atom_operations.py and lifecycle_intents.py only. Reuse one existing-owner resolver, retain @Version suffixes and raw predecessor bytes, refuse destination collisions. Preserve non-Plan and non-Archived placement. No physical migration or rewriting old archive/ trees. Review the dependent bundle-safety Task before execution.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review after P2478 and P2488

Both preceding Tasks are independently accepted on the final production/fixture hashes recorded in the Epic; full bounded portfolio 124/124 passes and final exact-diff review passes. Review D461@15/E502@13 against the existing publication/history owners before any change. Preserve separately admitted descendant actions and collision/refusal semantics. This Task is the next Stage 1 implementation item and remains Backlog; execution has not started. Stage 2 Scope Unit operations and physical legacy archive migration remain excluded.

### Execution checkpoint

Operator requested continuation. Current D461@15, D289@13, E502@13 and R1521@9 were reread with the PROGRAMMATIC M projection and E637/E389. D461 Core flat Plan placement overrides the older General retained-Archived-descendant wording only for Archived Plan Markdown; no broader cascade policy changes. Execute P2484 resolver work only in the existing publication owner modules; P2485 bundle safety waits for reviewed resolver output. Parallel lanes own functional tests, read-only validator and Subject prediction inspection; root owns records and Git. No release, deployment, Scope Unit operation, legacy migration or production-port tests.

### Source checkpoint and bounded follow-up

The publication/status resolver archive_revision_destination(root, atom, version) is implemented on atom_operations e4e3660fea2fb2f27da3345f3564b588451c768fb067d811b2ff50e18aca9733 and lifecycle 4bf3ab19b6079f38cfcff6af664dedc2904929ec54f2c258de9b5fe9f2d9017f. Independent review and integrated acceptance remain pending. Root identified the remaining preserve_atom_revision path still role-local archive/ for Plans; P2490 owns a separate at-most-15-minute completion before extending the parent budget. It also supplies the canonical history API required by P2486 Subject prediction. Non-Plan archive versus preserved-history conventions must remain unchanged; the two are not assumed interchangeable. No bundle-policy changes or success closure are claimed.

### Verified completion and explicit limits

All three bounded implementation children P2490/P2491/P2496 are Done after shared owning-scope destinations, prospective canonical Draft filename and unified Status predecessor paths were implemented and independently accepted. P2485 singleton carrier safety and P2486 validation/Subject predictions are separately verified. Final native71, Subject21, validator544 and CLI11 evidence is bound to frozen inputs; code review APPROVE. This closes the destination/preservation Task, not the missing always-recursive calling Workflow under C551/P2494.
