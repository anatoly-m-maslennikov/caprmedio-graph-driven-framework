---
atom_id: CA-R-1801
ref_id: CA-R-1801
container:
  scope_unit: CA-SU-24
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Prompt Authoring
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom
  - MODEL//CAPRMEDIO <+ Term//Property
  - MODEL//CAPRMEDIO <+ Atom.Content
  - MODEL//CAPRMEDIO <+ Atom.Content.Details
  - MODEL//CAPRMEDIO <+ Atom.Content.Summary
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
    <+ Controlled English
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Action
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Step
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Workflow
tier: 3
status: Active
version: 18
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-R-1801-PROMPTS-RULE--provide-complete-local-rmed-review-capability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
## Summary

Provide complete local RMED review capability

## Claim scope

the prompt Implementation of RMED Atoms Base Revise delivered by PROMPTS.

## Claim


### Prose Claim
the prompt Implementation **must** provide complete local RMED review capability under the admitted methodology checklist **and** Action definitions, including assessment of readable content whose Carrier layout is defective.

## Details

- the supported checklist is defined by CA-E-520-CORE_META_MODEL-POLICY--check-rmed-atom-coherence; the Implementation preserves its **`=6`** local check boundaries.
- malformed headings remain Properties defects. readable applicability, contribution, supporting text, **and** Summary remain assessable using their actual source passages.
- this is implementation authority for the capability, **not** another definition of the Workflow. CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch owns the Workflow; its referenced Actions own selection, checking, **and** correction.
- the capability preserves the admitted local-review boundary. it does **not** require cross-Atom comparison **or** an Entity-graph audit.
