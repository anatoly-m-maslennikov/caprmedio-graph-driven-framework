---
atom_id: CA-R-2118@15
content_role: Requirement
type: Rule
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-26 14:22:14 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Data Validation
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Applicable Methodology Compilation'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Domain/Continuant/Projection
relations: {}
tier: 3
---
# Summary

Gate source correction and conflict-selection dispositions on exact Operator approval, then reassess.

## Scope

The CA-O-154 through CA-O-156 decision and correction boundary; source mutation remains outside the compiler.

## Claim

`COMPILE_APPLICABLE_METHODOLOGY` **must not** edit methodology authority and **must** accept a conflict selection or correction result only with an exact current Operator decision, independently verified admitted Run and effect evidence, and current source/frontier bindings, followed by reselection and reassessment. Journal references are observational and cannot substitute for that authority or evidence.

## Details

For a decision, the Tool requires the exact conflict ID, proposal or candidate selection, source-frontier digest, Operator identity, independently verified admitted Run and effect evidence, and evidence that the decision is current and unambiguous. A Journal reference may be retained as an observation, but a missing, stale, or failed Journal append is not itself blocking. A stale, partial, missing, mismatched, rejected, ambiguous, or revoked decision or independent evidence is `blocked`. A Project Configuration approval file may be a non-authoritative lookup index only when it resolves to the independently verified decision and effect evidence; it cannot independently authorize selection or correction.

When the accepted disposition requires source correction, the Tool returns the source-owner correction request and awaits an independently produced owned-source change receipt. It has no `edit_source` or projected-Claim-fix mode. No compiler-side effect, output change, approval cache, or inferred delegation may alter source authority. A successful external source change, a non-mutating selection decision, a failed correction, or a recovery attempt requires a fresh CA-R-1839 selection and CA-R-1840 assessment before publication. Failed or partial correction preserves the prior projection and reports actual known effects; it never resumes from the former assessment.

The Tool returns `{ outcome: "reassess_required" | "blocked", decision_provenance, correction_request_or_receipt, evidence_refs }`. It does not create a duplicate approval Atom or duplicate shared Run-support behavior.

### Sources

- CA-O-011 v12, CA-O-154 v2, CA-O-155 v2, and CA-O-156 v2.
- CA-O-006 v6, CA-O-007 v6, and CA-O-008 v11.
- CA-P-1442 v1 and CA-A-1142 v2, W13 decision/Journal boundary.
