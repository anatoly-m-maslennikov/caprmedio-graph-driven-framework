---
atom_id: CA-M-411@4
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Engineering/Implementation Cohesion
  depends_on:
  - Subject/Engineering/Source Unit Responsibility
  - Subject/Engineering/Behavior Ownership
version: 4
updated_at: 2026-10-24 00:38:25 +0400
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  derived_from:
  - CA-M-403
tier: 3
---
# Summary

Concentrate Requirement and Delivery implementation

## Scope

New or changed PROGRAMMATIC implementation of Requirement (R) and Delivery (D) Atoms, including descendant Scope Units.

## Claim

For each implemented R or D Atom, prefer concentrating its actual claim-specific implementation in one cohesive implementation module and as few code units as practical, ideally one. Preserve complete realization of the Claim and allow justified multi-module exceptions when forced concentration would harm correctness or cohesion. Many-to-many implementation relations remain valid.

## Details

Candidate source: [CA-M-393@1](archive/CA-M-393-PROGRAMMATIC-CORE--concentrate-requirement-and-delivery-implementation@1.md)

- Apply the preference to actual implementation, not merely an owner label, trace link or facade over dispersed logic. Several Atoms may share one module or code unit; several code units within one module may realize one Atom.
- Use code units, such as functions or classes, at the stated implementation granularity; do not confuse them with governed Scope Units.
- For R, concentrate its claim-specific meaning, behavior or enforcement. For D, concentrate its representation, serialization, storage or placement logic. Implementation need not be executable code.
- Distinguish claim-specific realization from callers, dependencies, tests and other evidence. Their presence alone does not add a realizing module; a caller that performs part of the required enforcement does count.
- Preserve complete and truthful implementation relations. Leave unimplemented Atoms without invented implementation targets.
- When multiple modules are necessary, retain the required boundaries and state the concrete reason; do not duplicate logic, inflate a module or omit obligations merely to reduce the count.

This Method is an implementation-organization preference, not an absolute cardinality limit, new approval gate or test policy.

