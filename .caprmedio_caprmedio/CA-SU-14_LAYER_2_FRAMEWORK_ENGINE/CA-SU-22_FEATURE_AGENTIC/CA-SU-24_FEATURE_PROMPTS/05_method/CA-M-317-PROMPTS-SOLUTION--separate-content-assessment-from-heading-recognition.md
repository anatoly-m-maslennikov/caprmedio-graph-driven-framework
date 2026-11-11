---
atom_id: CA-M-317
ref_id: CA-M-317
container:
  scope_unit: CA-SU-24
role: Method
form: Solution
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Prompt Authoring
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom
  - MODEL//CAPRMEDIO <+ Term//Property
  - MODEL//CAPRMEDIO <+ Carrier
  - MODEL//CAPRMEDIO <+ Atom.Content
  - MODEL//CAPRMEDIO <+ Atom.Content.Details
  - MODEL//CAPRMEDIO <+ Atom.Content.Summary
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Evaluation)
tier: 3
status: Active
version: 19
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-M-317-PROMPTS-SOLUTION--separate-content-assessment-from-heading-recognition.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/05_method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---

## Summary

Separate content assessment from heading recognition

## Claim

### Prose Claim

**to** implement local content assessment, use semantic reading of the complete carried text for content judgments **and** structural parsing for Property conformance, keeping the two judgments separate.

## Details

- instructions request actual quoted passages **and** an explanation of their semantic function, including applicability, contribution, supporting detail, **or** Summary.
- a missing heading is evidence of a Carrier defect; it is **not** evidence that readable content cannot be assessed. a semantic interpretation does **not** declare a missing Property section present.
- instructions distinguish independently replaceable Claims from clauses, examples, **or** conditions of the same Claim. they preserve useful content **when** proposing a correction.
- unresolved meaning **or** genuinely unavailable evidence is stated precisely for the affected check. a generic layout failure is insufficient justification for skipping readable content.
