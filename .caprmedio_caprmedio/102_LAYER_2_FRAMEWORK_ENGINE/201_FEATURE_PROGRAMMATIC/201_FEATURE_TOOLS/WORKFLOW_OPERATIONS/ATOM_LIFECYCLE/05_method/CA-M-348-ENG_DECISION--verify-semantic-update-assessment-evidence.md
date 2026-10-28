---
atom_id: CA-M-348
content_role: Method
current_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 12
updated_at: 2026-10-27 19:59:42 +0400
relations:
  method_for:
  - CA-R-1892
type: Eng Decision
tier: 4
---
# Summary

Verify semantic Update assessment evidence

## Scope

One optional `semantic_assessment_report` reference in a sealed lifecycle Update request.

## Claim

To verify substantive Update evidence, resolve its exact `{path, digest}` and read its current Carrier. For a shared JSON review package, select exactly one assessment for the requested Atom; no Analysis Atom is required. For an Analysis Report, verify its Analysis/Analysis Report/Done classification from current authority and parse its sole canonical JSON evidence object. In both cases compare every target, proposal, authority and lineage pin before admitting the class. Reopen and repeat the same verification immediately before O129 effects; do not rely on caller fields, a filename, a previous read, or a report's recommendations as authorization.

## Details

For an Analysis Report, read only the fixed Results subsection and reject duplicate evidence headings. For a shared JSON review package, read the `assessments` list and reject a missing or duplicate target assessment. Both forms reject duplicate JSON keys, extra object keys and non-canonical scalar types. The verified O145 result retains the report descriptor, exact target/proposal comparison, authority-pin observations, normalized admitted class, declared delta, and lineage pins. A change in any observation requires reassessment. This Method never evaluates prose to invent same-primary-Claim identity or lineage impact; the completed assessment states those findings and the Tool only verifies their exact binding.
