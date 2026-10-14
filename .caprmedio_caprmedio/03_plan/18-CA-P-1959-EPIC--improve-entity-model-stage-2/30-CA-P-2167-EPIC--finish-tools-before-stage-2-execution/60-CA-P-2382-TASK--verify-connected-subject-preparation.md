---
atom_id: CA-P-2382
content_role: Plan
type: Plan
label: Task
work_sequence_number: 60
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Projection, Plan]
version: 2
updated_at: "2026-10-14 11:39:13 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Verify connected Subject preparation

## Objective

Verify the activated, reviewed MCP image through actual discovery, lookup, sealed preview and scratch-only staging for one supported pinned Core Atom.

## Details

Use the actual advertised logical request schemas and MCP transport. Reuse the prepared CA-D-253 request; bind staging to the exact returned preview seal and illustrative timestamp. Do not silently refresh a rejected seal. Preserve the original source bytes and all other Atoms. Reopen the returned scratch manifest and candidate, verify hashes and the permitted Subjects/Version/time delta. Root independently checks the outputs. Estimated work: up to 15 minutes.

This is the Operator-approved connected tool verification, not approval to exclude the 44 structurally refused owners from the batch. No live publication, source repair, content migration, selected manifest refresh or installed-package upgrade is included.

### Current evidence and remaining gate

Actual HTTP discovery/context, exact CA-D-253 lookup and sealed preview passed. The source bytes/mode stayed unchanged; Root independently inspected the responses. Evidence is recorded in connected-preparation-activation.md under the tools-first projection. Preview seal is ba718c8d430ccb7a88c141705019762aa24aa28257171fb37520bcf28e437d06. A fresh no-write request check revalidated all 906 source pins.

Scratch staging was denied by the permission reviewer before process/MCP invocation for lack of explicit trusted approval for that one-Atom mutation. No stage artifacts were created. Request direct approval; do not retry through another route. Stage/readback acceptance remains unproven, so this Task stays Active.

### Definition of Done

Actual lookup, preview and stage succeed without source changes; independent readback confirms the exact sealed scratch result. Save truthful requests, responses and source evidence, including failures or partial artifacts. A registry listing or local fixture alone is insufficient. This Task does not complete the parent Epic or approve the migration packet.
