---
subjects:
  active: Journal
  passive:
  - Scope Unit//CORE_META_MODEL
  - Scope Unit
  - 'Entity/Object/Continuant/Projection/Type: Artifact Change Log'
  - 'Entity/Object/Continuant/Projection/Type: Process Log'
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1466
  - CA-R-1720
  - CA-R-1463
  - CA-R-1467@19
  - CA-R-1468@20
atom_id: CA-E-464
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-464-CORE_META_MODEL-POLICY--validate-journal-independence-from-git.md
  source_atom_id: CA-E-464
  source_atom_revision: 24
  source_sha256: a4ad4d2cb4d357093910d75f65e3ce9464d9fec5b39112b3c3cae578f39debda
  original_relations_sha256: 9df3c2ead8f13c90ef6760757de1f2b5279c95b90ff24ea559bbfb7ab2082444
---
## Summary

Validate Journal independence from Git

## Claim scope

Core Meta-Model rules concerning Journal recording, replacement evidence, and canonical log Projections.

## Claim

the Evaluation **must** reject a Core Meta-Model rule that makes Journal recording, replacement evidence, **or** either canonical log Projection depend on Git installation, commit topology, hooks, **or** commit messages.

with no Git Extension selected, admitted Journal records **and** their Artifact Change Log **and** Process Log Projections **must** remain valid under their applicable authority. with the Git Extension selected, its commit references **may** add provenance but **must not** create a second authoritative event history. changing **or** removing secondary Git history **must not** destroy the recorded identity **and** evidence needed **to** rebuild the two logs. a missing **or** invalid authoritative Journal remains a failure **in** either case.
