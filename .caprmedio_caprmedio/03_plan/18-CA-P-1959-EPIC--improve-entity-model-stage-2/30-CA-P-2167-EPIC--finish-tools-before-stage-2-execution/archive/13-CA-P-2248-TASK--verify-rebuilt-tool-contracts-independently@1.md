---
atom_id: CA-P-2248
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 1
updated_at: "2026-10-12 23:10:03 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2173, CA-P-2174]
---
# Summary

Verify rebuilt Tool contracts independently

## Objective

An independent source review accepts or rejects the actual rebuilt Tool RMEDO against the approved connector and Workflow decisions before affected implementation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent independent of all three contract authors. Start from their actual delivered source packets under CA-P-2245–2247, not predicted files, proposed hashes or a worker's completion label. Packet readiness releases read-only review while the authoring Tasks remain Active pending this acceptance; this is not a circular prerequisite requiring those Tasks already be Done. Root owns integration/shared state and Git.

Read every complete current affected R/M/E/D/O source and its exact predecessor. Own only a separate independent verification receipt; production/authority sources and the authors' expected output are read-only. Bind actual paths, Atom IDs, Versions, hashes, declared scopes and replacement/history evidence. Confirm new CA-R-1933–1935/CA-M-372–375, CA-E-625–627/CA-D-622–624 plus CA-D-425, CA-O-201–210, reused CA-O-047 and all affected existing contracts against the actual delivered manifest. Independently compare meanings, not just producer assertions or matching bytes.

Check logical storage-neutral interfaces; independent Find/Read/Modify and findWorkflow/modifyWorkflow; createAtom/createSU; no Atom deletion; Summary-change fresh-ID archival and same-ID property refusal; truthful target/created/archived reporting without automatic reference retargeting; shared section edits; property-list VALUE or full-set edits with add/remove; Subject field/scope/exact-prefix-suffix-contains matching; shared TOML Action with distinct config Workflows and schema checks.

Check per-Atom stop-first-failure retains earlier successes and leaves remaining targets untouched without cross-Atom all-or-nothing rollback. One-Atom authorization/currentness/safety/history/recording must remain intact. Resume/retry and concurrent-publication choices remain deferred; source acceptance does not choose either mechanism or open a live gate. A deliberate inconsistent source/result example must fail the review check.

Deliver actual accepted/rejected pins, findings and limits independently. Historical Done receipts/source pins remain unchanged, and new source acceptance is not implementation, fixture proof, runtime activation or live capability. After contracts pass, additional connector/configuration/section implementation requires actual <=15-minute work leaves and fresh independent fixture acceptance before use; CA-P-2173 alone does not cover the new Tool set. No broad implementation hierarchy is created here. Split a concrete review overrun before execution.

### Definition of Done

The Plan is **not** Done if any actual affected source or predecessor is missing/stale, declared decisions or cross-role meanings conflict, producer assertions replace independent review, deliberate wrong examples are accepted, old receipts are silently repinned, one-Atom safeguards weaken, deferred policies are inferred, unauthorized surfaces change, source review is claimed as implementation/live readiness, or own work exceeds 15 minutes without decomposition.
