---
atom_id: CA-P-1974@9
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Tool
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 9
updated_at: 2026-10-24 06:12:21 +0400
relations:
  is_decomposition_of:
  - CA-P-1970
tier: 3
---
# Summary

Prepare post-Subject content update Tasks

## Objective

Define bounded RMEDO content review/update Tasks only after the complete Subject gate passes.

## Details

Retained Active and deferred under the separate CA-P-1970 content Epic. Current staged Subject migration grants no content-preparation or execution authority. Separate authorization and the existing relevant gates are required before this Task starts.

Estimated own work: 15 minutes. Assignee: AI Agent.

Required prerequisite: CA-P-1969. Verify its complete current receipt, then inventory current NON-ARCHIVED eligible Summary/Substance/applicability Scope/Details source versions and assign disjoint R, M, E, D and O batches. Create review/proposal, authorized update and independent verification children under CA-P-1970 with exact source pins and at-most-15-minute leaf work. Preserve the accepted Subjects and meaningful type/role constraints. Use the whole Subject AND whole owner Scope Unit omission rule. Record concrete unresolved decisions, not guessed replacements. This preparation Task creates Plans only; it does not draft content replacements before the gate or approve/apply them.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

Classify every proposed identity-preserving update as exactly Version `+1` from its current original NON-ARCHIVED Atom, with the prior original archived without a second bump; current does not mean Active. Classify a Type change as a new Atom/new ID and archive of the old Atom. A changed Summary requires a new ID unless governing policy separately changes; Type is not its sole replacement trigger. Preserve bare stored IDs, distinct archived versions of the same ID, `Atom.ID`/`Scope Unit.ID` semantic names without storage-key changes, and the `Atom`/`atom` distinction. Plan Atom filenames in all statuses as `AtomID@Version-SCOPE_NAME--summary.md` (`@` filename-only), with Scope NAME rather than a label or path; references use ID plus Version. Preserve the Substance/Scope/Details change classes. Finishing preparation does not finish CA-P-1970; its generated review/effect/verification children must complete.

After the gate, put a distinct Step-2 Tool sequence first: RMEDO review/update, independent verification of the actual contracts, exact D-approved carrier/reference and identity-consumer alignment, Applicable Methodology compiler and Terms-builder alignment, then independent isolated fixture verification. Affected content/consumer usage waits for those receipts. Do not perform renames during preparation or this current Epic edit; do not plan an automatic runtime/release rebuild. For Applicable Methodology, assign a lifecycle child that selects current NON-ARCHIVED eligible source versions, preserves source ID/Version/authored content, changes only projected Status/provenance, has Project Configuration author corrections before selection/projection, and treats the whole Projection as reusable non-authority with no independently versioned member.

Include the Terms Graph work retained under CA-P-1970, with CA-P-1959 v54 as historical planning context. Cover current RMEDO review/update and independent contract verification, existing builder/extractor/diagnostic alignment, independent fixture acceptance, then affected content/consumer usage in that order. Derived Terms compilation remains this separate Epic's work; no ordinary Core content is pulled into Subject migration. Give each leaf an exact source or file scope, a deliverable, prerequisites and an acceptance check; split it until own work fits 15 minutes. Map existing CA-P-1872 work before adding overlapping graph Tasks.

Include the prospective Entity hierarchy (`Entity -> Object | Term | Selection`, Object -> Occurrent | Continuant), Revision/Journal under History, and Carrier under Continuant in the review inventory. Include the rejected single-definition-owner assumptions and their dependent authoring/validation contracts. Include optional Semantics only under the accepted content rules. Carry the parent's positive and negative acceptance cases into the child checks: intended non-Active status, bare ID with archived version, Scope NAME rather than label/path, excluded projected Archived versus historical input, shared meaning with different allowed-value sets, disjoint scoped meanings, incompatible overlapping uses, unresolved scope, source-linked reuse, invalid lifecycle transition, stale/non-eligible source, and a prohibited storage-key or unapproved filename rename. Do not turn `*.Status` into a new property or silently create `Scope Unit.Status`.

### Definition of Done

The Plan is **not** Done if the Step-1 gate is missing or stale, a role/source batch is unowned or overlapping, review/update authority is unspecified, content replacements are prepared before the gate or applied, or Terms Graph RMEDO/consumer/verification responsibilities are missing or duplicate existing work; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
