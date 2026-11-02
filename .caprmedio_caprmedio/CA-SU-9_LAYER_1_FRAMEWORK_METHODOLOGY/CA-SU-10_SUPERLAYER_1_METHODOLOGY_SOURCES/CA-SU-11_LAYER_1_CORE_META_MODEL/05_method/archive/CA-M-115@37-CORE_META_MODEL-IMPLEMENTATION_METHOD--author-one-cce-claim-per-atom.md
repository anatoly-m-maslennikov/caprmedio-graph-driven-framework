---
subjects:
  governs: Subject/Engineering/Methodology
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Graph/Rule/CCE
  - Subject/Domain/Node/Continuant/Actor
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
version: 37
updated_at: 2026-10-24 22:32:06 +0400
relations: {}
atom_id: CA-M-115@37
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Author one CCE Claim per Atom

## Scope

authoring the boundary of **`=1`** independently replaceable prose CCE Atom contribution. Formal Graph Rule Atoms use CA-M-394 instead, retaining one independently replaceable structured rule of exactly one Graph Rule Type. This exception does not apply automatically to every R/Type: Rule Atom.

## Claim

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under CA-D-482-CORE_META_MODEL-DELIVERY--carry-the-resolved-claim-target-scope-unit. express applicability **in** the registered body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; for RMED, use Scope **and** write the Claim within that applicability; those restrictions alone do **not** make the Atom Relational.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.

## Details
