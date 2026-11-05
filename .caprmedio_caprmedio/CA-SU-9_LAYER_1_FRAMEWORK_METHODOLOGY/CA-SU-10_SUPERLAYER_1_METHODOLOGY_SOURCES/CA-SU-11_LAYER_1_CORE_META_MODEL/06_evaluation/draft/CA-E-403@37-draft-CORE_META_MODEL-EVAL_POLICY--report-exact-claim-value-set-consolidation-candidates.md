---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL
version: 37
updated_at: 2026-11-05 14:25:52 +0400
relations:
  evaluation_for:
  - CA-R-1358
  - CA-R-1359
atom_id: CA-E-403
ref_id: CA-E-403@37-draft
status: Draft
tier: 4
role: Evaluation
form: Eval Policy
carrier_destination:
  file:
    name: CA-E-403@37-draft-EVAL_POLICY--report-exact-claim-value-set-consolidation-candidates.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Report Exact Claim Value-Set Consolidation Candidates

## Claim

### Prose Claim


Claim Value Set consolidation candidates.


the Evaluation **must** report **`=1`** Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Target Scope Unit, textual Claim Scope, Property, **and** exact qualifiers, has **`=1`** mechanically parseable single-value Claim, **and** differs **only** by **`=1`** unique value proven as allowed by the `:` qualification for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
