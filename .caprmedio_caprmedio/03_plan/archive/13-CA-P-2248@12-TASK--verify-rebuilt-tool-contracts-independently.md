---
atom_id: CA-P-2248@12
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Scope Unit
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Governing Configuration
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Engineering/Project Structure Declaration
  - Subject/Engineering/Configuration/Shared TOML Connector
  - Subject/Engineering/Configuration/Project Structure Workflow Realization
  - Subject/Engineering/Configuration/Project Settings Workflow Realization
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/History
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 12
updated_at: 2026-10-24 21:35:21 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2173
  - CA-P-2174
  - CA-P-2251
tier: 3
---
# Summary

Verify rebuilt Tool contracts independently

## Objective

An independent source review accepts or rejects the actual rebuilt Tool RMEDO against the approved connector and Workflow decisions before affected implementation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent independent of all three contract authors. Start from their actual delivered source packets under CA-P-2245–2247, not predicted files, proposed hashes or a worker's completion label. Packet readiness releases read-only review while the authoring Tasks remain Active pending this acceptance; this is not a circular prerequisite requiring those Tasks already be Done. Root owns integration/shared state and Git.

The Operator approved the two FEATURE siblings CONNECTOR_TOOLS and TOOL_WORKFLOWS under PROGRAMMATIC (Level 3, navigation 5/6), with flat role folders and shared Core policies inside each. Root alone updates Project Structure; only rebuilt RMEDO moves to `305_FEATURE_CONNECTOR_TOOLS`/`306_FEATURE_TOOL_WORKFLOWS`. Their future `305_CONNECTOR_TOOLS`/`306_TOOL_WORKFLOWS` delivery roots remain unmaterialized; existing TOOLS, unrelated legacy authority, existing delivery bindings and code paths stay unchanged. This approval supersedes the prior prospective no-new-Scope-Unit restriction for exactly this split.

Connector Core CA-R-1936/CA-M-376/CA-E-628/CA-D-625 must supply a coherent broad logical API across ALL connector Tools: common input/result/precondition/error/effect contracts, not a new transport, database or retry design. Workflow Core policies remain separate. Actual code work must explicitly address hardcoded authority paths, release/admission bindings, selected-execution refresh/seals/pins and the graph generator's incorrect delivery derivation, with legacy Core/content alignment and independent runtime/admission/fixture gates retained. New source ownership or a matching receipt does not make existing code compatible, and successful source authoring grants no live readiness.

Independently check actual Project Structure declares only the two approved FEATURE additions with Level 3/navigation 5/6 and explicit future delivery bindings; preserve every existing declaration/code path. Reopen complete rebuilt source ownership/target/tier/filename/reference bindings and flat role placement. Confirm shared policies are Core within their FEATURE, not extra CORE Scope Units, and the common Connector Core API covers ALL connector Tools without a transport/database/retry design. Source acceptance must explicitly identify the outstanding hardcoded consumer, release/admission, selected-pin, graph-delivery, legacy Core/content and runtime gates; it cannot validate unmodified code by implication.

Read every complete current affected R/M/E/D/O source and its exact predecessor. Own only a separate independent verification receipt; production/authority sources and the authors' expected output are read-only. Bind actual paths, Atom IDs, Versions, hashes, declared scopes and replacement/history evidence. Confirm new CA-R-1933–1936/CA-M-372–376, CA-E-625–628/CA-D-622–625 plus CA-D-425, CA-O-201–210, reused CA-O-047 and all affected existing contracts against the actual delivered manifest. Independently compare meanings, not just producer assertions or matching bytes.

Check logical storage-neutral interfaces; independent Find/Read/Modify and findWorkflow/modifyWorkflow; createAtom/createSU; no Atom deletion; Summary-change fresh-ID archival and same-ID property refusal; truthful target/created/archived reporting without automatic reference retargeting; shared section edits; property-list VALUE or full-set edits with add/remove; Subject field/scope/exact-prefix-suffix-contains matching; shared TOML Action with distinct config Workflows and schema checks.

Check per-Atom stop-first-failure retains earlier successes and leaves remaining targets untouched without cross-Atom all-or-nothing rollback. One-Atom authorization/currentness/safety/history/recording must remain intact. Resume/retry and concurrent-publication choices remain deferred; source acceptance does not choose either mechanism or open a live gate. A deliberate inconsistent source/result example must fail the review check.

Deliver actual accepted/rejected pins, findings and limits independently. Historical Done receipts/source pins remain unchanged, and new source acceptance is not implementation, fixture proof, runtime activation or live capability. This Task's final scope is the delivered current 81-source subset, its exact history/configuration declarations and this expanded Plan packet, not future missing operation-specific contracts or code. Reopen the actual current Tasks, exact predecessor archives, explicit dependency graph and full pending capability coverage. CA-P-2249/2250 obtain their own different-reviewer acceptance; their author packet readiness does not require self-acceptance. CA-P-2251's later explicitly approved FPF review waits for those accepted manifests plus this Task's accepted scope, not a circular requirement that future review already be complete. CA-P-2252–2278 provide actual <=15-minute implementation/compatibility and independent fixture leaves; current source acceptance is not completion of them. This combined Plan/current-subset check has passed independently; its closure does not complete the separate pending work. Split a concrete review overrun before execution.

### Completion checkpoint

The actual [independent combined acceptance](../../../_projection/core-entity-review/stage2/tools-first/logical-connector-contract-acceptance.md) is PASS for the delivered 81-source RMEDO subset, expanded 38-Plan packet, approved configuration declarations and exact history. It independently checked meanings, coverage, current pins, links, dependencies and deliberate wrong examples. This Done revision records that bounded acceptance only. CA-P-2249/2250 missing contracts, CA-P-2251 approved actual FPF review, implementation/fixtures, applicable Core alignment and deferred live publication remain pending; no runtime or migration capability follows.

### Definition of Done

The Plan is **not** Done if any actual affected source or predecessor is missing/stale, declared decisions or cross-role meanings conflict, producer assertions replace independent review, deliberate wrong examples are accepted, old receipts are silently repinned, one-Atom safeguards weaken, deferred policies are inferred, unauthorized surfaces change, source review is claimed as implementation/live readiness, or own work exceeds 15 minutes without decomposition.
