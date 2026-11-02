---
atom_id: CA-E-303@24
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool//ATOM_CREATE
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.ID
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 24
updated_at: 2026-10-24 01:50:12 +0400
relations:
  evaluation_for:
  - CA-R-865
  - CA-O-032
  - CA-D-508
tier: 3
---
# Summary

Verify create sealed caprmedio atom carriers

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

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
- Create an Atom in each requested Status admitted by its applicable Role/Type model, including a case where Journal append fails or has no Event ID; verify the actual created Atom/Run outcome without replay.
- Create a new Draft with no `atom_id` and the ID-free empty-number filename, and a role-draft marker such as `CA-R-draft`; validate marker/filename agreement without allocating a canonical number. Journal absence or append failure does not reject an otherwise admitted create.
- Create an existing-Atom Draft carrier `CA-R-123@4-draft` with carried `version: 4` as a proposal for canonical `CA-R-123` Version 4; preserve Version 4 and do not allocate a canonical ID during Draft creation. Repeat the case with legacy `CA-R-123@draft` and an explicit proposed Version 4. Reject marker/filename/Version mismatches before writes. This is Draft-carrier staging, not new Atom creation; the fresh-ID and initial-Version cases above remain unchanged.

### Acceptance criteria

Dry runs and rejected preflight create nothing for that action. Each completed action creates exactly its admitted Atom with complete observed ID/Version/state evidence. Earlier completed actions remain after a later failure, and remaining actions are untouched. No partial state is reported as a completed Atom. Resume/retry of the new workflow family and stronger concurrency/publication guarantees remain deferred.

### Failure disposition

Retain exact requests, pins, validation/permission decisions, actual effects, retained successes and unperformed targets. These cases require later functional evidence; they record no actual test pass or backend guarantee.
