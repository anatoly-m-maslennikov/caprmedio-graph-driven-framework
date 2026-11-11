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
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Goal)
tier: 4
relations:
  evaluation_for:
  - CA-R-3034
  - CA-R-2650
  - CA-R-718
  - CA-D-325
status: Active
version: 31
updated_at: "2026-11-11 18:11:33 +0400"
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: caprmedio
carrier_destination:
  file:
    name: CA-E-445-PROJECT_CONFIGURATION-EVAL_CASE--validate-methodology-membership-in-the-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation
---

## Summary

Validate Methodology membership in the Project

## Claim

### Prose Claim

The Methodology Scope Units belong to the caprmedio Project Scope Unit tree and remain governed by its applicable Project-owned Tier 0 Atoms.

## Test case

Resolve the current Project Scope Unit tree from authoritative ownership declarations and locate FRAMEWORK_METHODOLOGY, METHODOLOGY_SOURCES, and its source Scope Units. Verify their ancestry to caprmedio and their authority Directory Carriers. Include their active Atoms in applicable Project Tier 0 alignment checks. Then place a Methodology Scope Unit outside that tree, author or persist a Structural Level property for a current caprmedio Scope Unit, register an unauthorized Bootstrap Scope Unit as part of the current caprmedio structure, exempt Methodology from an applicable Project-owned Tier 0 Atom, or represent an Atom's different Claim Target Scope Unit as an additional Scope Unit edge.

## Acceptance criteria

Every current Methodology Scope Unit has a parent chain to caprmedio. Any displayed ancestry depth or path is derived from that parent chain only and does not establish another authored source of ancestry. Its source Carrier placement does not exempt it from Project authority. Applicable Project Tier 0 checks include its active Atoms. All invalid fixtures fail. The predefined world Scope Unit is not an additional Scope Unit in the caprmedio Project structure. The external Project Goal's Tier `-1` remains valid and does not create or imply a Scope Unit depth. Archived Bootstrap records remain historical evidence without becoming current Scope Units.

## Failure disposition

Record a Concern identifying the incorrect owner, authored or persisted Structural Level property, Carrier binding, applicable Project Tier 0 exemption, or invented Scope Unit edge.
