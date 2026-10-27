---
atom_id: CA-R-1892@13
content_role: Requirement
current_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis/Type: Analysis Report'
version: 13
updated_at: 2026-10-26 00:46:35 +0400
relations:
  relates_to:
  - CA-R-1825
  - CA-R-1826
  - CA-R-1827
tier: 3
type: Rule
---
# Summary

Bind semantic Update assessment evidence

## Scope

Tool realization of one substantive Atom Update through the existing O067/O145/O129 lifecycle boundary.

## Claim

Outside CA-R-866's explicitly instructed Subjects-only batch branch, a Tool **must** treat a substantive Update as unresolved unless current, completed assessment evidence from an existing shared JSON review package or a Done Analysis Report supplies exact, read-only-verifiable semantic assessment evidence. A separate Analysis Atom for each changed Atom is not required. The evidence **must** establish unchanged Summary and same primary-Claim identity, one admitted R1432 class, a declared delta, and completed lineage-impact review. It is evidence only: it does not grant Operator permission, effect admission, or any other authorization.

## Details

When an Analysis Report is supplied, its current source-derived Analysis status must be `Done`. A shared review package selects exactly one assessment for the requested target and may cover multiple independent updates. In either form, the evidence binds the exact target, complete proposal, current CA-R-1432 and CA-R-1464 authority, admitted class, preserved primary Claim identity, declared delta and completed lineage review. CA-D-585 defines the request and report representation.

O145 and O129 independently reopen the selected evidence and every declared pin. They compare it to the current target, complete proposal and current R1432/R1464 bytes. Source-derived Analysis classification and Done status are checked only for an Analysis Report. Missing, stale, malformed, ambiguous, mismatched or unverifiable evidence returns `unresolved` before mutation; an Analysis Report with an unadmitted type or non-Done status also returns `unresolved`. A report with `replacement` produces the existing Replace handoff; no report may make a same-ID Update eligible when its Summary changes.

The Tool seals only the normalized verified evidence from a completed O145 Step together with its exact request binding. O129 revalidates that seal immediately before effects. Mechanical lossless normalization remains separately provable without this optional report.

CA-R-866's branch substitutes the exact ordered packet and actual instructed-operation Initiative/Operator authorization for per-Atom semantic Analysis Reports/O067/O145. It requires no additional form, review/pause response, content-review/confirmation round or fabricated receipt. Keep normal exact source/draft/patch/layout, identity/Summary, archive, Version/time and readback checks, not a separate full-candidate validation or initial intent-metadata gate. This exception does not weaken ordinary content-update assessments or admit authority from syntax, hashes or a caller Boolean.
