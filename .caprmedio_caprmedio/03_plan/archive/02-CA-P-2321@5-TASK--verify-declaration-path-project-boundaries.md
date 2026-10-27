---
atom_id: CA-P-2321@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Configuration
  - Workflow
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 06:12:24 +0400
relations:
  is_decomposition_of:
  - CA-P-2272
tier: 3
---
# Summary

Verify declaration path Project boundaries

## Objective

The shared declaration path check rejects proven foreign Project control boundaries with current evidence.

## Details

Estimated own work: up to 15 minutes. Split further work before exceeding this bound. Inherit the parent's accepted source, independent review and execution gates. Root owns Plans and Git; assigned file ownership stays disjoint.

After independent acceptance of P2320, reuse selected Project identity and bounded Settings reads to prove foreign control roots. Directory prefixes alone do not prove identity. Retain exact marker reads and relevant absence observations; refuse ambiguous, contradictory, unsafe or stale evidence. Preserve legitimate owning-root paths, absent ordinary paths and lookalikes. No new public API, second Settings authority, fallback or synthetic revision evidence.

### Definition of Done

The Plan is **not** Done if its stated outcome lacks exact source/code/test evidence and independent verification; required checks fail; a deferred policy is inferred; existing safety checks are bypassed; or source-only/isolated evidence is represented as live runtime or migration acceptance.

### Acceptance — 2026-10-13

The final helper and affected callers passed independent connected-code review and 22 independent boundary tests. Regression results: Graph 36, Structure 23, Scope 12 and full Atom validation 344 passed. Source selection retains original marker/absence evidence; changed markers refuse and reconstructed late handlers cannot reseal missing proof. Exact final pins and scope are in `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/declaration-boundary-consumers-acceptance.md`. Settings logical Revision evidence and installed MCP/runtime acceptance remain separate.
