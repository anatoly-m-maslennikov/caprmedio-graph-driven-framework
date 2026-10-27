---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.ID
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Local Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Carrier.Canonical Address
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 24
updated_at: 2026-10-27 06:04:45 +0400
relations:
  method_for:
  - CA-R-728
atom_id: CA-M-276
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
---
# Summary

Repair accidental Atom ID reuse

## Scope

repair of accidental reuse of assigned Project Atom IDs.

## Claim

**to** repair accidental reuse of an assigned Project Atom ID, an AI Agent **must** perform **all** of:

1. identify the distinct source Atoms by exact Carrier address, Revision, **and** recorded history. distinguish accidental reuse from legitimate Revisions of the same Atom **and** derived copies of its Carrier.
2. establish the original valid owner from recorded assignment history. **if** the original owner cannot be established at the effective Confidence Threshold, request an Operator decision for that collision **before** changing its identities **or** references. filename order, discovery order, current filesystem timestamps, **or** the highest Version **must not** select the owner.
3. preserve the original owner's Atom ID. give **every** later accidental reuse the next unreused Project-wide number for its own Content Role under CA-D-450-CORE_META_MODEL-DELIVERY--number-project-owned-atoms-within-each-content-role, using the encoding under CA-D-378-CORE_META_MODEL-DELIVERY--serialize-assigned-atom-identities. this corrects invalid reuse **and** does **not** authorize changing a valid owner's immutable identity.
4. preserve **every** affected Atom's Claim, Content Role, Atom Scope, Claim Target Scope Unit, **and** textual Claim Scope. preserve its immutable prior Revisions **and** recorded history; record the exact predecessor-to-corrected-identity mapping **in** the existing Work Journal **without** rewriting historical Carriers **or** Records.
5. resolve **every** affected current reference against its intended Atom using the reference's context **and** recorded history. update references **only** **when** their intended targets are established; request an Operator decision for unresolved references. do **not** replace the ambiguous ID indiscriminately.
6. verify that the repaired active identities resolve uniquely **and** **every** affected current reference still identifies its intended Claim **before** declaring the collision repaired. keep unrelated Claims **and** identities unchanged.
7. perform repair as an explicitly authorized source change, **not** as an automatic side effect of lookup **or** compilation. preserve CA-D-336-CORE_META_MODEL-DELIVERY--resolve-active-atoms-from-canonical-carrier-identities's failure on ambiguous lookup **until** source repair is complete, **and** regenerate affected Projections from their corrected sources through their existing governed workflows.

## Details
