---
atom_id: CA-P-2321
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Backlog
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Configuration, Workflow, Plan]
version: 1
updated_at: "2026-10-13 19:01:00 +0400"
relations:
  is_decomposition_of: [CA-P-2272]
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
