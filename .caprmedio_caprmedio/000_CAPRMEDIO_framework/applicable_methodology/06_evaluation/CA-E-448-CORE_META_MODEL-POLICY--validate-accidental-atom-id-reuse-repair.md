---
atom_id: CA-E-448
ref_id: CA-E-448
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.ID
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
  - CAPRMEDIO_MODEL <+ Journal
tier: 5
relations:
  evaluation_for:
  - CA-M-276
status: Active
version: 33
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-E-448-CORE_META_MODEL-EVAL_POLICY--validate-accidental-atom-id-reuse-repair.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-448-CORE_META_MODEL-POLICY--validate-accidental-atom-id-reuse-repair.md
  source_atom_id: CA-E-448
  source_atom_revision: 33
  source_sha256: ed97d1af8a487161d32e123d923f51c43323f7456ad164ca33b199d8fe7e866d
  original_relations_sha256: 7052f3ea7234947e3eed5cdb9e8de3c7b82427e31f0c1cb14ed06bd377cf52c3
---
## Summary

Validate accidental Atom ID reuse repair

## Claim

### Prose Claim


Atom ID collision repairs.


the Evaluation **must** reject completion of an Atom ID collision repair under CA-M-276-CORE_META_MODEL-IMPLEMENTATION_METHOD--repair-accidental-atom-id-reuse **if** **any** of:

- the original owner was selected **without** sufficient recorded assignment evidence **or** the required Operator decision, **or** its valid Atom ID changed.
- a later accidental reuse retains the colliding ID, receives a previously used number, **or** receives an ID outside its Project prefix **and** Content Role sequence.
- an affected Claim, Content Role, Atom Scope, Claim Target Scope Unit, **or** textual Claim Scope changes beyond the approved identity-reference correction, a distinct Claim is lost **or** merged, **or** an unrelated identity changes.
- a prior Revision **or** historical Record is rewritten, history becomes unreachable, **or** the Work Journal lacks the exact mapping between the historical Carrier **and** its corrected identity.
- an affected current reference resolves ambiguously, remains unresolved, **or** resolves **to** a different intended Claim; an uncertain reference is rebound **without** the required Operator decision.
- legitimate same-Atom Revisions **or** derived copies are renumbered as accidental reuse, **or** lookup **or** compilation silently selects an identity winner.

the Evaluation **must** distinguish a paused collision awaiting an Operator decision from a completed repair. its checks **must** cover the verified-original-owner case, reversed Carrier discovery order, an unknown original owner, an ambiguous incoming reference, **and** legitimate same-Atom Revisions **or** derived copies.
