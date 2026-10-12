---
atom_id: CA-P-1961
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 4
updated_at: "2026-10-11 00:28:49 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1963]
---
# Summary

Implement field-aware Subject lookup

## Objective

Find the exact governs and depends_on occurrences for selected authoritative Core RMEDO Atoms.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisite: CA-P-1960.

Extend the existing search surface or provide a narrow reusable adapter using existing source readers. Query Subjects fields, not full-file text. Support governs, depends_on and both, exact values and delimiter-aware prefixes, explicit source root and RMEDO/lifecycle/owner filters. Return exact occurrences with ID, Version, path, field/index, value and SHA-256 source pin.

Use the declared authoring Core root; do not silently select a delivered or Applicable Methodology copy. Include the source root and updated_at in each result. Default to Active original Atoms. Report malformed or duplicate sources as findings, not silent exclusions. Canonical Core Subjects are flat; legacy forms elsewhere require an explicit compatibility finding, not an implicit rewrite.

Tests cover field direction, body-text false positives, prefix boundaries, repeated dependency values, role/owner/lifecycle filters and deterministic results. Output is read-only. Do not edit authoritative Atoms. Split work that exceeds 15 minutes.

Allowed roles are Requirement, Method, Evaluation, Delivery and Operations, including O. Exclude and report C/A/P/other roles. Verify `Artifact/Atom` does not match `Artifact/Atomology`; use the selected grammar profile's delimiters, not guessed relation meaning. Test path/owner disagreement and require a diagnostic.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if field-specific lookup is missing, body text creates hits, selection or pins are ambiguous, malformed sources are silently omitted, tests fail, or any authoritative Atom changes; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.

### Completion evidence

Implemented the local ATOM_SEARCH Subject mode in atom_subject_lookup.py and its existing wrapper. Explicit Core RMEDO/owner selection stays a caller filter; the reusable Tool also supports other valid content roles. Subject prefix boundaries remain the currently admitted `/` and `:`. No dot semantics or MCP binding was added.

Passed 34 focused lookup and existing Atom-operation tests. The real Core CLI query returned three independently hash-checked occurrences and reported two existing invalid Updated At values (CA-R-1873 and CA-D-559); coverage was correctly limited. Core source hashes before and after were identical. Invalid sources were not repaired. Exact implementation pins and limits are in [_projection/core-entity-review/stage2/task-1961.receipt.json](../../../_projection/core-entity-review/stage2/task-1961.receipt.json).
