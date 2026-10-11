---
atom_id: CA-P-2062
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Tool, Plan, Projection]
version: 4
updated_at: "2026-10-11 04:37:07 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1965]
---
# Summary

Align Subject Tool grammar contracts

## Objective

The Search/Update Tool contracts support the approved syntax through a small explicit profile API before code is changed.

## Details

Own work: none. Required prerequisite: CA-P-2061 (Done, d99b21b8e). Its review identifies ten required Engine Tool contract revisions before code. The Engine Tool-RMEDO source scope was already authorized by the Operator's first RMEDO gate; this work does not extend the five-definition Core exception.

Use legacy default or explicitly selected approved profile for ordinary correct-file operations only. Cross-profile migration is ad-hoc and separate. Both profiles reject @. Lookup is lexical, not a semantic-conformance attestation. Preview root keys are exactly atoms and optional subject_profile; items remain closed. Selected profile and immutable reviewed grammar evidence must be echoed/sealed; no silent ignored profile. Syntax/operator direction is not native endpoint admission. No new public graph CLI selector or reusable migration engine.

Use the settled schema and latest Operator correction in `_projection/core-entity-review/stage2/grammar-tools.current-contract.md`: no @ carrier/display operator; D atoms define storage. The frozen CA-P-2061 review remains evidence of that earlier review, not an override of the latest input.

Preserve old byte-exact source versions under role-local archive paths and current +1 versions. Root owns pre-effect observations, Journal, integration and Git. Workers own disjoint source/archive files only. Keep all ordinary Core files, original Core Subjects, captured review/ledger and old Tool packet/acceptance unchanged.

### Decomposing Plans

- [CA-P-2063 — Align Subject Tool Requirements and Methods](17-CA-P-2062-TASK--align-subject-tool-grammar-contracts/done/01-CA-P-2063-TASK--align-subject-tool-requirements-and-methods.md)
- [CA-P-2064 — Align Subject Tool Evaluation and Delivery](17-CA-P-2062-TASK--align-subject-tool-grammar-contracts/02-CA-P-2064-TASK--align-subject-tool-evaluation-and-delivery.md)
- [CA-P-2065 — Align Subject Tool Operations](17-CA-P-2062-TASK--align-subject-tool-grammar-contracts/done/03-CA-P-2065-TASK--align-subject-tool-operations.md)
- [CA-P-2066 — Accept and compile aligned Subject Tool contracts](17-CA-P-2062-TASK--align-subject-tool-grammar-contracts/04-CA-P-2066-TASK--accept-and-compile-aligned-subject-tool-contracts.md)

### Definition of Done

Not Done if any required source/pin/evidence is missing or stale, independent acceptance is absent, unrelated source/body/scope changes occur, required effects are overstated, or own work exceeds 15 minutes without decomposition.
