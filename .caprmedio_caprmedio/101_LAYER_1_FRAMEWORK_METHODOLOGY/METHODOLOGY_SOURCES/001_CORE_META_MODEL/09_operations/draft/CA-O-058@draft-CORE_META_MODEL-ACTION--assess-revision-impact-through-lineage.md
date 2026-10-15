---
subjects:
  governs: "Assess Lineage Impact"
  depends_on:
    ["Action", "Atom", "Revision/Type: Atom", "Relation", "Lineage Impact Analysis", "Operator", "AI Agent"]
version: 7
updated_at: "2026-10-15 12:09:33 +0000"
relations: {"child_of":["CA-E-002"]}
atom_id: "CA-O-058@draft"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Assess revision impact through lineage

## Operation

Assess Lineage Impact **means** the reusable Action that assesses **every** reachable descendant lineage branch of **`=1`** changed Atom **until** **every** branch has an explicit impact disposition.

apply this Action **when** the Atom:

- receives a new accepted Revision;
- is replaced by a successor; **or**
- moves **to** the archive.

an Operator **or** AI Agent performs this Action within its existing authority. the assessment follows the existing lineage recursively; it does **not** create another cross-Scope Unit dependency graph.

## Details
