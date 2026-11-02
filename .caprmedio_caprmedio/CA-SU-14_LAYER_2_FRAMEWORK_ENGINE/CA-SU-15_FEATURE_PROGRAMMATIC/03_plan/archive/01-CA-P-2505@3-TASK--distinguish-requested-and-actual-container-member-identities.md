---
atom_id: CA-P-2505@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2501
version: 3
updated_at: 2026-10-24 06:04:41 +0400
tier: 3
---
# Summary

Distinguish requested and actual container member identities

## Objective

Align technical coordinator aggregate observation with actual canonical Run evidence.

## Details

At most 15 minutes own work; split before extending. Own backend.py and its focused container status tests after initial freeze. Use failed mapping or null consistently with composition. Expose parent_requested_run_id separately from nullable actual parent_run_id, and requested member identities separately from evidence-backed actual_run_id. Completed identities require actual evidence; untouched entries are requested identities. No planned ID may be presented as a started Source Run. Validate marked aggregates and preserve truthful partial/uncertain status, ordinary behavior and direct-enqueue scope guard. Coordinate schema with P2503 before final freeze; no hidden currentness bypass or production traffic.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Acceptance receipt

Twelve focused status/guard tests passed; six adjacent selected public-status tests and three entrypoint tests passed during initial freeze. Independent final exact-delta review APPROVE closes coordinator-as-child actual identity conflation. Backend SHA-256 c29ef051e860635d92dd06e928dcabc489b1db477bb603a1092501cca8b5b2af; focused tests 8d5425765dde39646e1fb630d26cfb2bdd8aaa998aafb60ac5114bc4508eafbb. Requested parent/member IDs remain distinct from nullable evidence-backed actual IDs; failed mapping/null schema is aligned. Full native recursive composition remains dependent acceptance, not this status-only proof.
