---
atom_id: CA-A-1261
ref_id: CA-A-1261
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Formal Model
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Distinguish Relation Type instances from graph connections

## Decision

Relation instances define the real Relation Types used throughout the graph. Relation describes their structure; Relation//RECORDS and Relation//IS_EXECUTION_OF are named instances of that structure. An actual graph connection uses one of those Types and is identified by its source, Relation Type and target.

Keep the existing // selectors for these reusable Type instances. Correct the stale Definition that still describes the same target as one actual connection. Type-level meaning, direction and derived-inverse declarations must stay distinct from a particular connection's concrete endpoints. This clarification adds no new primary entity branch.

## Review disposition

FM-02 is resolved as a design decision: preserve the Type-instance approach. FX-02's alternative Relation.Type: RECORDS selector is not adopted. Aligning the prepared Definitions and properties remains uncompleted repair work. FM-01 and FM-03 remain open repairs under the already established Claim boundary and latest canonical paths.

## State

This file records the Operator's clarification. The historical FPF report is unchanged; no Current Atom, Definition Draft or runtime was modified by this record.
