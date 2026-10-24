---
subjects:
  governs: provenance
  depends_on: []
version: 19
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-M-135@19
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Exclude generated-only implementation edges

## Scope

provenance validation of recorded changes in the governed selection.

## Claim

provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.

an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.

## Details
