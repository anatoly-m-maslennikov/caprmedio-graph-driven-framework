---
atom_id: CA-R-1842@8
content_role: Requirement
type: Rule
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 10:27:10 +0400
subjects:
  governs: Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY
  depends_on:
  - Subject/Engineering/Tool
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow//Applicable Methodology Compilation'
  - Step
  - Action
  - Methodology Source
  - Atom Revision
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1839
  - CA-R-1840
  - CA-R-2118
  - CA-O-011
  - CA-O-157
  - CA-O-009
  - CA-M-226
tier: 3
---
# Summary

Publish only a current resolved frontier atomically while preserving the prior output on failure.

## Scope

The CA-O-157 projection-publication boundary after a current conflict-free reassessment.

## Claim

`COMPILE_APPLICABLE_METHODOLOGY` **must** atomically publish only the complete current resolved frontier and **must** preserve the entire prior Applicable Methodology output when preparation, currentness validation, publication transaction, output-fidelity, or source-currentness validation fails. A Journal append failure after a successful publication is a recording diagnostic, not a reason to roll back the published output.

## Details

Immediately before commit, the Tool revalidates every selected source path, Atom ID, Revision, byte digest, source relation, decision provenance when applicable, and final source-frontier digest. It stages the full replacement output, including all governed RMED role directories, before one recoverable publication transaction. Any changed, newly discovered, missing, malformed, incomplete, stale, unresolved, or unsupported input blocks publication before output mutation. A transaction, filesystem, output-fidelity, or source-currentness failure leaves the prior output byte-for-byte intact and reports whether publication was not started, rolled back, or has an explicitly uncertain recovery state. If the atomic publication succeeds but the business Journal append fails, retain the actual published output, report a `recording_error` diagnostic with the known publication and effect evidence, and do not claim a completed Journal record. Journal append remains a plain explicit business-record operation; repeating it neither establishes identity nor authorizes or blocks the operation.

Each published Carrier retains its original authored frontmatter, body, and Relations unchanged and adds only the non-authoritative projection binding required to identify its original source Carrier, Atom ID, Revision, and digest. The output is a derived Projection, not source authority. Successful publication returns the exact published output digest and independently verified publication/effect evidence, with optional Journal/Run observation references; a failed Journal append is reported without rolling back a successful publication. It neither edits source authority nor substitutes a generated file for a source correction.

### Sources

- CA-O-011 v12 and CA-O-157 v2; CA-O-009 v5.
- CA-M-226 v6; CA-P-1442 v1; CA-A-1142 v2, W13 fidelity boundary.
