---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis'
  depends_on: []
version: 23
updated_at: 2026-10-24 04:38:42 +0400
relations:
  child_of:
  - CA-R-1725
  resolution_of:
  - CAPRMEDIO-GOV-CONC-053--what-external-review-envelope-is-sufficient
atom_id: CA-R-1648@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Use external Analysis Atoms as review envelopes

## Scope

external reviews, their imported External Analysis Report Atoms, and the internal Analyses derived from them.

## Claim

an external review **must** be imported as an External Analysis Report Atom whose governed envelope identifies its source, provenance, reviewed scope, original body, **and** native attachments **without** requiring a provider-specific finding schema. one internal Analysis derives from that Atom, records the project's finding-level interpretation **and** dispositions, **and** becomes the **only** Analysis source from which project-owned Concern, Plan, Requirement, Method, Evaluation, **or** Delivery Atoms are derived. **every** accepted disposition that changes project meaning **or** work is materialized **in** its owning CAPRMEDIO Content Role; rejected **or** non-actionable findings remain **only** **in** the internal Analysis.

## Details
