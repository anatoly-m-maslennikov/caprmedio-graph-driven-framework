---
atom_id: CA-E-303
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_CREATE"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Create Sealed Atom Carriers"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 15
updated_at: "2026-10-12 23:13:13 +0400"
relations: {"evaluation_for":["CA-R-865","CA-O-032","CA-D-508"]}
---
# Summary

Verify create sealed caprmedio atom carriers

## Scope

One logical Atom Create action under CA-R-865 and CA-O-032, and ordered independent Create actions under CA-M-372.

## Claim

Create validates and admits one new Atom before its authorized effect. Several requested Atoms are independent actions, not one cross-Atom transaction.

## Details

### Required test cases

- Create one valid identified Atom with complete role/type metadata and a fresh never-reused ID. Include a valid unassigned Draft case without allocating an ID or promoting it.
- Reject denied permission, missing validation authority, malformed input, occupied destination, duplicate logical identity, historical ID reuse and stale assignment/source evidence before the affected action writes.
- For ordered targets A, B and C, let A succeed and make B fail admission or publication. Retain A and its truthful effect evidence, report B's failure and do not start C. Do not roll back A or invent completion for B/C.
- Inject a post-write validation failure within one Atom action. Prove that action's admitted all-or-nothing boundary and exact restoration where claimed; preserve unrelated Atoms, existing history and accepted recording. Unverified restoration remains a failed or uncertain effect, not a passing rollback.
- Reject a competing identity admission after preview without silently choosing another ID. Verify the Project-wide next-unreused-number rule and initial Version metadata rather than only checking active filenames.

### Acceptance criteria

Dry runs and rejected preflight create nothing for that action. Each completed action creates exactly its admitted Atom with complete observed ID/Version/state evidence. Earlier completed actions remain after a later failure, and remaining actions are untouched. No partial state is reported as a completed Atom. Resume/retry of the new workflow family and stronger concurrency/publication guarantees remain deferred.

### Failure disposition

Retain exact requests, pins, validation/permission decisions, actual effects, retained successes and unperformed targets. These cases require later functional evidence; they record no actual test pass or backend guarantee.
