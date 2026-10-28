---
atom_id: CA-R-1827@14
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Carrier
  - Subject/Graph Relation
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
version: 14
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Validate one sealed lifecycle target

## Scope

Single-target/predecessor validation and Relation diagnostics before a selected lifecycle operation is delegated.

## Claim

The dispatcher **must** accept exactly one resolved target and, for Replace, exactly one resolved active predecessor and the complete native successor Carrier set. It seals identity, path, filename, expected Version/digest, requested operation/result, and applicable status-model revision before delegation. It preserves the native Create/Update/Replace Carrier and successor-set guards. It checks active inbound and outgoing Relations whose targets would become invalid, unresolved, or semantically inconsistent after the proposed result; it returns every detected broken active inbound/outgoing reference as a diagnostic and does not silently retarget or repair it.

Preview is the default and writes no Carrier, history, or effect. Mutation requires an explicitly authorized Project-local MCP request with the sealed target and delegation envelope; a stale seal, missing authorization, invalid target/predecessor, or failed structural/currentness check prevents mutation. A model-admitted authorized Change Status, including Archive, remains dispatchable when its resulting active references are broken: it performs the admitted status transition and reports those broken references and active referrers for the separate authorized repair Workflow; diagnostics are not automatic retargeting or a blanket lifecycle veto.

## Details

Bulk targeting, generalized relation repair, and arbitrary destructive changes are outside this one-target slice.
