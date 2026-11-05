---
atom_id: CA-E-445
ref_id: CA-E-445
container:
  scope_unit: CA-SU-13
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
tier: 4
relations:
  evaluation_for:
  - CA-R-706
  - CA-R-718
  - CA-D-325
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: caprmedio
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-445-PROJECT_CONFIGURATION-EVAL-CASE--validate-methodology-membership-in-the-project.md
  source_atom_id: CA-E-445
  source_atom_revision: 28
  source_sha256: 44dde9a84eff1a42c0331b950a371c2d547aee8a09239eb59b55885e3b02ea54
  original_relations_sha256: b44b20e012b4a11fdeca3e65c5d30f54989f67003fcb6939e46e32716dfd3cfb
---
## Summary

Validate Methodology membership in the Project

## Claim

### Prose Claim


the Methodology Scope Units belong **to** the caprmedio Project Scope Unit tree **and** remain governed by its active Project-owned Tier 0 Atoms.

## Test case

resolve the current Project Scope Unit tree from authoritative ownership declarations **and** locate FRAMEWORK_METHODOLOGY, METHODOLOGY_SOURCES, **and** its source Scope Units. verify their ancestry **to** caprmedio **and** their authority Directory Carriers. include their active Atoms **in** Project Scope Contract-first alignment checks. **then** place a Methodology Scope Unit outside that tree, author or persist a Structural Level property for a current caprmedio Scope Unit, register a Bootstrap Scope Unit as part of the current caprmedio structure, exempt Methodology from a Project-owned Tier 0 Atom, **or** represent an Atom's different Claim Target Scope Unit as an additional Scope Unit edge.

## Acceptance criteria

**every** current Methodology Scope Unit has a parent chain **to** caprmedio. any displayed ancestry depth or path is derived from that parent chain only and does not establish another authored source of ancestry. its source Carrier placement does **not** exempt it from Project authority. the ordinary Project Scope Contract-first checks include its active Atoms. **all** invalid fixtures fail. the Core Meta-Model's optional support for Bootstrap Scope Units does **not** activate them for caprmedio. the external Project Goal's Tier **`-1`** remains valid and does not create or imply a Scope Unit depth. archived Bootstrap records remain historical evidence **without** becoming current Scope Units.

## Failure disposition

record a Concern identifying the incorrect owner, authored or persisted Structural Level property, Carrier binding, Project Scope Contract exemption, **or** invented Scope Unit edge.
