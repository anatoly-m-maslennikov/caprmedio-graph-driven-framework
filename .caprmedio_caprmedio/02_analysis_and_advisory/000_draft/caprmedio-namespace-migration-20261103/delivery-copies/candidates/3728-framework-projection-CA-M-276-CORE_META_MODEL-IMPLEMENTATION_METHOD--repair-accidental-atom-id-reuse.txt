---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.ID
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.ID
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Version Number
  - CAPRMEDIO <+ MODEL <+ Carrier.Canonical Address
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO <+ MODEL <+ Journal
version: 31
updated_at: 2026-11-02 18:35:20 +0400
relations:
  method_for:
  - CA-R-2493
atom_id: CA-M-276
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-276-CORE_META_MODEL-IMPLEMENTATION_METHOD--repair-accidental-atom-id-reuse.md
  source_atom_id: CA-M-276
  source_atom_revision: 31
  source_sha256: 0f39bfc102c76f8a92a2fd4a63b8cfd2f265785401ad1e354d265e25a1e2705a
  original_relations_sha256: e34eb399209772e69c9e83607058eeacd9f02b5fab47517d59060b76f37de2af
---
## Summary

Repair accidental Atom ID reuse

## Claim scope

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
