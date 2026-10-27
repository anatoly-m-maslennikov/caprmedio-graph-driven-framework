---
atom_id: CA-P-2369@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 47
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Define minimal Subject lookup MCP exposure

## Objective

Specify the smallest existing-style MCP descriptor/provider on ATOM_SEARCH, reusing field-aware matching and existing admission. Resolve the concrete request/result and source bindings, PRMEDO role frontier, and D424/E301 changes. Do not write code or amend authority until the bounded interface proposal is independently checked; no new general connector framework.

## Details

### Operator decision — 2026-10-14

The Operator approved direct read-only Subject lookup without a Workflow Session or Journal records. Return matching Atoms and their source hashes through the existing ATOM_SEARCH MCP binding. Keep root/source validation and all mutation safeguards unchanged. This does not decide staging, live publication or selected-manifest repair. Revise and independently check the minimal interface proposal before the affected source or code implementation.

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Acceptance — 2026-10-14

The corrected proposal passed independent review: SHA-256 `e1323bcf38b3cef83aa08d4897ff430f249482ace46edf8a4252169cebf5c0c1`. It binds direct lookup to explicit logical criteria and actual source hashes, with no Session, Run or Journal. Identity checks concern possible selected-ID claims; unrelated malformed C/A cannot become a global gate. The Operator decision is recorded above. CA-P-2374–2377 own rules, reader, MCP provider and independent transport verification. This completes only interface definition, not installed readiness.

### Definition of Done

A concrete narrow proposal identifies exact existing seams, source contracts, request/result, admission and fixtures. Independent review confirms feasibility and any genuine Operator decision is recorded rather than guessed. Proposal acceptance alone is not MCP readiness.
