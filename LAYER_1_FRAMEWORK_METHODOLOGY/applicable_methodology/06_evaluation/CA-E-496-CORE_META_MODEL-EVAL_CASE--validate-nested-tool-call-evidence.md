---
atom_id: CA-E-496
ref_id: CA-E-496
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Step Run
  - CAPRMEDIO_MODEL <+ Workflow Run
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
  - CAPRMEDIO_MODEL <+ Projection
tier: 3
relations:
  evaluation_for:
  - CA-R-1528
  - CA-R-1511@22
status: Active
version: 23
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-E-496-CORE_META_MODEL-EVAL_CASE--validate-nested-tool-call-evidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-496-CORE_META_MODEL-EVAL_CASE--validate-nested-tool-call-evidence.md
  source_atom_id: CA-E-496
  source_atom_revision: 23
  source_sha256: ca718b31271b35bb659037af498a2ed3d73ed7f0351b7089ec3227fcf91e2682
  original_relations_sha256: 2dde8ea9685247f7085155ccd836cc6ed9705f9aa6cd78755d6134dfe5795c12
---
## Summary

Validate nested Tool-call evidence

## Claim

### Prose Claim


serialized Tool-call evidence within a Step Run.


the Main Content of a Journal Carrier that encodes Tool-call evidence within a Step Run **must** undergo an actual Evaluation under CA-R-1528. Available wire evidence alone is **not** a passing result.

## Details

the Evaluation of that Main Content **must** run and report a passing, failed, or unresolved result. It **must**:

- check whether several Tool calls by an Agentic Action inside a leaf Step Run carry their actual parent Step Run, Tool identities, inputs **or** admitted protected references, results **or** errors, **and** distinguishing call evidence; report failure when required wire evidence is absent;
- check whether repeated attempts with the same Tool **and** inputs retain distinct attempt identities without claiming a second effect when its outcome is unknown; report unresolved when the supplied evidence cannot distinguish the effect;
- check whether a failed Tool call or unconfirmed effect is recorded as that outcome rather than successful completion; report failure for a contradicted success claim;
- check whether a rebuilt nested trace derives from the canonical Journal without another source of execution history; report failure when another source is claimed;
- reject an inference that a Tool call automatically creates a Workflow Step, a Conditional Step route, **or** a new Action definition; and
- check whether secret input uses a governed protected representation rather than plaintext duplication; report failure when plaintext is present.

the Evaluation **must not** edit supplied wire evidence. Missing wire evidence **or** an unperformed Evaluation is **not** a passing result.
