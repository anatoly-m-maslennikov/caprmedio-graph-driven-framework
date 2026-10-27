---
atom_id: CA-P-1971@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Atom
  - Subject
  - Term
  - Property
  - Carrier
  - Revision
  - Scope Unit
  - Projection
  - Plan
  - Tool
  - Journal
  - Operator
version: 8
updated_at: 2026-10-24 06:04:18 +0400
relations:
  is_decomposition_of:
  - CA-P-1970
tier: 3
---
# Summary

Verify the Stage 2 entity model

## Objective

Verify the final RMEDO sources and their reproducible entity graph after both ordered steps.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. This verifier is retained Active and deferred under the separate CA-P-1970 content Epic. Required inputs are its completed authorized content-effect children and their independent receipts, not the parent Epic's Done status. This Task contributes to that Epic's completion; current staged Subject migration grants no content execution authority.

Independently check final Subjects, Summary, Substance, Scope and Details against the accepted batch decisions and current governing RMED+O. Verify source identities, revisions, history, evidence coverage and affected validation/tests. Confirm the prospective Entity hierarchy (`Entity -> Object | Term | Selection`, Object -> Occurrent | Continuant), Revision/Journal under History, and Carrier under Continuant rather than as a generic root.

Check each ordinary identity-preserving update selected its current original NON-ARCHIVED eligible source, made exactly Version `+1`, and archived the previous original without a second bump; current need not be Active. Check Type changes created an entirely new Atom/new ID and archived the old Atom. Check a changed Summary received a new ID unless governing policy separately changed, without claiming Type is its sole trigger. Verify `Atom.ID`/`Scope Unit.ID` semantic names retain storage keys, `Atom` remains distinct from `atom`, stored IDs are bare, archived originals share IDs at distinct Versions, and Atom filenames in all statuses use `AtomID@Version-SCOPE_NAME--summary.md` with filename-only `@` and Scope NAME rather than label/path; references use ID plus Version. Use a separately authored expected ledger/oracle without calling the producer's graph builder, and prove altered outputs are rejected.

Verify CA-P-2167's complete independent Tool receipt preceded affected Step-1 use. Verify the Step-2 sequence ran RMEDO-first with independent contract verification, then covered D-approved carrier/reference changes, identity consumers, Applicable Methodology compiler consumers and the Terms builder with independent fixture proof before affected content/consumer usage. Derived Terms compilation must remain Step 2. Check no unapproved rename or automatic runtime/release rebuild was performed. For Applicable Methodology, independently prove selected sources were current NON-ARCHIVED eligible versions; source ID, Version and authored content were preserved; only projected Status/provenance differed; Project Configuration authored corrections before selection/projection; and the whole Projection remained a reusable, non-authoritative lifecycle output with no independently versioned member.

Rebuild the graph from authoritative Subjects with pinned implementation and compare the final relation semantics with the accepted model. Report unresolved, excluded and deferred matters explicitly. Terms remain a separate graph; same spelling does not authorize a Term edge.

Verify the Terms Graph adoption results produced under CA-P-1970 against the preserved historical CA-P-1959 decisions and current governing contracts. Require aligned RMEDO and actual evidence from the affected builder, not just updated planning or candidate text. Check definitions derived from multiple source cases, contributing source passages/versions/scopes, reuse without new authority, and rebuilding after source correction. Independently check that different allowed-value sets alone are not meaning conflicts, disjoint scoped meanings remain visible, incompatible overlapping meanings are flagged and missing evidence or uncertain scope is unresolved. Reject invented properties such as `Scope Unit.Status`, unsupported native Relations and silently settled conflicts. Run recorded positive and negative controls for intended non-Active status, bare ID/archive version, Scope NAME, excluded projected Archived versus historical input, lifecycle, source eligibility, projection provenance, scoped-meaning conflict and unapproved rename cases. Consume source-pinned child verification receipts; split additional independent checks into bounded children if necessary.

Deliver one final receipt with exact source, implementation and output hashes, actual check results and remaining work. No automatic installed-copy refresh, runtime activation, release, push, PR or native MCP delivery follows from this pass. Split verification if it exceeds 15 minutes.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if a required check is failed, missing or stale, final graph reproduction diverges, an accepted decision is unaccounted for, source/body meaning is lost, or completion is overstated; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
