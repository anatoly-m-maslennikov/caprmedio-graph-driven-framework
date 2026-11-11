---
atom_id: CA-M-262
ref_id: CA-M-262@29-draft
container:
  scope_unit: CA-SU-9
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package/Implementation
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations:
  child_of:
  - CA-M-261
status: Draft
version: 29
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-M-262@29-draft-FRAMEWORK_METHODOLOGY-IMPLEMENTATION_METHOD--preserve-sufficient-authority-for-reconstruction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/05_method/000_draft
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: FRAMEWORK_METHODOLOGY
---
## Summary
Preserve sufficient authority for reconstruction

## Claim

### Prose Claim


**to** rebuild the Implementation, use the current RMED as sufficient authority for reproducing its required behavior **and** passing its applicable Evaluations **without** the previous Implementation **or** additional specification preparation; **if** the implementation language changes, **then** update the affected Method **and** Delivery authority **before** rebuilding against the resulting current RMED. a ready-made alternative Implementation is **not** required.

under unchanged governing RMED, reconstruct runtime behavior that produces the same output for the same complete runtime input, including relevant starting state, configuration, time, randomness, **and** external-service responses. preserve the applicable Method **and** Delivery constraints; identical source code **or** identical source-file bytes are **not** required. judge fresh reconstruction **and** repeated implementation by this runtime equivalence, **not** by a requirement **to** leave already-conforming code untouched. an authorized RMED change establishes a new comparison baseline **and** **must not** be reported as reconstruction against unchanged RMED.
