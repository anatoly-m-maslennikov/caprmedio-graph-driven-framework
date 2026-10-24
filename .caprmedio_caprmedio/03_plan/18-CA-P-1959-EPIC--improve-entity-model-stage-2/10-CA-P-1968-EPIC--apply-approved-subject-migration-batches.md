---
atom_id: CA-P-1968
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject
  depends_on: [Atom, Subject, Term, Property, Carrier, Scope Unit, Projection, Plan, Operator]
version: 7
updated_at: "2026-10-22 22:05:30 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  depends_on: [CA-P-1966, CA-P-2045]
  blocks: [CA-P-1969]
---
# Summary

Apply approved Subject migration batches

## Objective

Organize and verify approved Candidate #7 methodology source increments before ordinary content updates, preserving predecessor history and truthful applied effects.

## Details

Candidate #7 application is methodology-only: Subjects, defining Requirements/Deliveries, property rules, Type classifications and identity/ID rules. Re-read live source files before any effect and record actual current paths, old/new IDs, Versions, Statuses, timestamps, predecessor archives and changed fields. A classification-only Type correction may keep the ID only when Summary and Substance are unchanged. Preserve unrelated body content and ordinary content migration under CA-P-1970.

Mapping research remains separate from source application. Use the fresh worklist and the integrated ledger from CA-P-2043/CA-P-2045; do not resurrect the old Candidate #3/#4 packet, fixed counts, CA-P-2188–CA-P-2193, the CA-P-2167 Tool gate or the CA-P-1909–CA-P-1912 sealed pipeline as current prerequisites. CA-P-1973 was canceled; its predecessor and cancellation path are history, not a current child-completion requirement.

Each applied update must preserve its Summary unless a separately defined R/D source change requires a new identity; archive the predecessor with qualified ID@oldVersion and Archived Status, leaving archived numeric Version, Updated At and unrelated content unchanged. Stop on a failed or uncertain effect and leave completed effects plus untouched remainder visible. No automatic replay or rollback.

Before claiming the full Candidate #7 migration, maintain a separate current-Plan metadata and Draft-ID worklist. Verify Current Plan required properties, applicable Types, effective Labels, filename tokens, group-qualified Draft IDs and Draft lineage independently from Subject mapping; do not hide these cases inside a Subject-only count or treat a missing Draft field as a source guess.

No code, implementation schemas, MCP, tests, Settings values, runtime activation, Journal fabrication, release or deployment is included. This Plan does not claim a complete Subject migration or a rebuilt graph.

### Definition of Done

Not Done if an effect lacks a current approved mapping and source readback, a predecessor archive is malformed, a Type-only exception violates its Summary/Substance condition, ordinary content changes, a canceled child is treated as required, or actual effects are confused with a plan, scratch record or runtime receipt.
