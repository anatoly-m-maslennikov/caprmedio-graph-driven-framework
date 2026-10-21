---
atom_id: CA-P-2486
content_role: Plan
type: Plan
label: Task
work_sequence_number: 62
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 4
updated_at: "2026-10-20T21:15:29.652Z"
---
# Summary

Align Plan archive validation and predictions

## Objective

Make Plan archive validation and Subject-history predictions match the shared flat archive destination.

## Details

At most 15 minutes own work; split before extending. Depends on accepted P2484 resolver contract; review after P2485. Own check_structure_extended.py, atom_subject_patch.py and subject_batch_frontier.py plus their focused frozen fixture checks only. Validate Archived Plan Markdown directly under owning 03_plan/archived with matching Version suffix. Preserve legacy trees byte-for-byte; no migration, incoming-link repair or non-Archived hierarchy changes. Do not duplicate the publication owner placement rule or infer new policy.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Independent validator lane admission

P2485 history-bearing bundle execution is postponed for C549, not a reason to block the independently settled Archived Plan validator predicate. Activate only the source-bound validator/frozen-fixture lane now; Subject edits wait for P2490 canonical preservation API. Review D461@15, D289@13 and E502@13 as exact authority. The validator owns independent Evaluation enforcement under M316 and does not import effectful publication logic or redefine placement policy; this separate read-only source-bound check is the justified module boundary under M393. Special-case Archived Plans past the decomposition early return, enforce flat scope placement and Version suffix, and retain non-Archived/non-Plan behavior. Refresh exact D461/D289 pins/fixtures only after adapter reconciliation. No parser/address rule fork, live fixture load, legacy carrier migration, Scope Unit operation, runtime change or new policy. Final integrated acceptance remains P2487.

### Subject adapter lane admission after P2490

The preserved_revision_destination(root, atom) API now exists and root reviewed its exact Plan/non-Plan semantics. Activate the independent Subject adapter lane with exclusive atom_subject_patch.py, subject_batch_frontier.py, subject_batch_authorization.py, tests/subject_batch_fixture.py and focused Subject test files only. The pure intent adapts the sealed _plan snapshot without a source reread. Frontier binding receives explicit selected root and reopens only exact digest-pinned source bytes, via the existing bounded FileSource reader, to supply required owning-scope metadata; it never guesses cwd or expands the packet schema. Both use the same preservation helper, current predecessor Version N/digest, and history-free no-op. Validator lane files remain separately owned. Final integrated acceptance waits for all dependent source to freeze.

### Verified completion and explicit limits

Final frozen VALIDATE_ATOMS cohort544 and fresh-child CLI11 passed against D461@16, with identical validator/source/fixture hashes before and after. Subject prediction/root propagation integration passed Draft12, draft contract4 and batch contract5 on final atom_operations537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284. Exact sealed source metadata, owning flat Plan history and non-Plan ordinary-update archive spelling are preserved. This accepts placement/prediction only, not recursive lifecycle composition.
