---
atom_id: CA-P-1965
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 1
updated_at: "2026-10-10 22:32:47 +0400"
relations: 
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1967, CA-P-1968]
---
# Summary

Support the approved Subject grammar in Tools

## Objective

Make lookup, preview, parsing and validation agree on the approved proposed grammar before source cutover.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisite: CA-P-1964.

Use its recorded decision and exact grammar candidate. Update the existing parser/validator/preview implementation with explicitly selected old and proposed profiles; never silently reinterpret old sources. The proposed profile supports / broader-to-narrower, . bearer qualification and : allowed value with the approved direction and character rules.

Exercise mixed operators, malformed paths, reserved-character escaping, collisions and old-profile compatibility. Derive typed relations, not edges inferred from Source Atom metadata. Keep entity and Term namespaces separate.

This Task changes implementation and isolated fixtures only. It does not adopt governing grammar Atoms, activate a runtime, publish graphs or migrate sources. Include exact implementation pins in the subsequent preview. Split larger work before execution.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if parser, validator and preview disagree, old Subjects are silently reinterpreted, approved syntax has no tests, or authority/runtime/source changes are implied, any direct decomposing Plan is not Done, or own work exceeds 15 minutes without decomposition.
