---
atom_id: CA-P-2441
content_role: Plan
type: Plan
label: Task
work_sequence_number: 30
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
---
# Summary

Complete Current Concern target admission

## Objective

Bound the independent-review and later Current-only decision follow-up from P2432 before extending its ownwork budget.

## Details

R1022v17 governs anyContentRole target eligibility within Current (notDraft/notArchived; includes admittedDone/Canceled/etc). Fix only Concern-specific inventory and directadapter behavior; preserve other relation policies and qualified extensionstatus/type authority. Reuse existing source-bound targetType/schema checks rather than literalbans or duplicate registries; preserve identity/role/version/uniqueness/canonicalcarrier checks. Add frozen positiveCurrentstatuses and negativeDraft/Archived/malformedtarget cases. Independentreview and finalfullvalidatorcheck precede P2438 imagefreeze. This Task is at most15minutes ownwork; split before extending. NoDocker/MCP/Git effects.

### Definition of Done

Narrow follow-up passes focused and fullfrozen checks plus read-onlyreview, with explicit source/runtime limitations.

### Completion checkpoint

Accepted report confirms positive Current target admission, including Done/Canceled and other allowed statuses, with Draft/Archived negative cases. Foreign prefixes were retained, ASCII encoding was enforced, and the other relation-specific Active policy remained intact. The focused set covered111 checks. No Docker/MCP/deployed acceptance is claimed.
