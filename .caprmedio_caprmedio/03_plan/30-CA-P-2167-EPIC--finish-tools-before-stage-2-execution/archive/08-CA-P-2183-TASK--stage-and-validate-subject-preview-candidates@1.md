---
atom_id: CA-P-2183
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Carrier, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-12 05:40:17 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-1966]
---
# Summary

Stage and validate Subject preview candidates

## Objective

Produce independently checked temporary candidate Atoms without writing authoritative sources.

## Details

Own work: none. Complete the three bounded children. Use opt-in local `ATOM_UPDATE run --stage-preview`, the existing `proposed_carrier` and a fresh generated `.caprmedio_tmp/subject-preview/<id>/`; re-read and validate every staged file. Operate valid inputs under existing eligibility/profile/source-pin checks.

No original, archive/history, Journal or publication write occurs. Staged candidates are non-authoritative and excluded from current-original selection. Preserve source pins/provenance and proposed bytes; never treat preview time as a source effect-time receipt. Live changed-Subject publication and effect-time execution remain deferred.

The Operator requires migration candidates to stay staged; Tool RMEDO and Plans are updated normally. Implementation requires independent verification of updated, accepted governing RMEDO; candidate review alone is insufficient.

CA-P-1963 plus CA-P-2186's actual independent receipt release read-only current-source adaptation/re-pinning/mapping solely to create and review staged candidates, without waiting for CA-P-2167's publication receipt. This does not complete CA-P-2167 or supersede its full source-implementation gate or CA-P-1909–1912's sole final accepted graph, sealed live packet, exact approval and application/reproduction route. Step 2 stays after CA-P-1969.

### Decomposing Plans

- [CA-P-2184 — Review and align staged-preview contracts](08-CA-P-2183-TASK--stage-and-validate-subject-preview-candidates/01-CA-P-2184-TASK--review-and-align-staged-preview-contracts.md)
- [CA-P-2185 — Implement opt-in Subject preview staging](08-CA-P-2183-TASK--stage-and-validate-subject-preview-candidates/02-CA-P-2185-TASK--implement-opt-in-subject-preview-staging.md)
- [CA-P-2186 — Verify staged Subject candidates independently](08-CA-P-2183-TASK--stage-and-validate-subject-preview-candidates/03-CA-P-2186-TASK--verify-staged-subject-candidates-independently.md)

### Definition of Done

The Plan is **not** Done if a child is not Done, actual updated contracts or independent candidate-file validation is missing/stale, source/history/Journal/publication changes, staged outputs gain authority, or its receipt is treated as the full mapping/sealing/application or Tool gate.
