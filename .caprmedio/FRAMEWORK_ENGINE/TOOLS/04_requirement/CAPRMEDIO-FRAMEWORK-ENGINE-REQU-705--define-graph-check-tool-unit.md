---
subject_scopes:
  - feature-boundary
version: 5
updated_at: 2026-08-22 03:09:20
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
  relates_to:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-534--validate-one-artifact-carrier
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-535--validate-project-integrity
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-604--register-extensible-tool-capability-classes
---
# Define the GRAPH_CHECK Tool unit

`GRAPH_CHECK` must be one Checker Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `3`, addressed by `FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK`, and realized under `FRAMEWORK_ENGINE/TOOLS/GRAPH_CHECK/`; it applies selected registered Evaluation criteria to one resolved target set and returns stable issues, evidence, and verdicts without changing governed Atoms, Journals, native Implementation, or derived outputs.
