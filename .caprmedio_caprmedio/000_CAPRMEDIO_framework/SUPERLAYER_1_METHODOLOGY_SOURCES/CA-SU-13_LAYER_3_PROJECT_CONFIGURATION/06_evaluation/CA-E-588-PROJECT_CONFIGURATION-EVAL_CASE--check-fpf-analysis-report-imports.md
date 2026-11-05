---
atom_id: CA-E-588
ref_id: CA-E-588
container:
  scope_unit: CA-SU-13
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := FPF Analysis Report)
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  evaluation_for:
  - CA-R-1889
status: Active
version: 20
updated_at: 2026-11-02 19:33:47 +0400
carrier_destination:
  file:
    name: CA-E-588-PROJECT_CONFIGURATION-EVAL_CASE--check-fpf-analysis-report-imports.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Check FPF Analysis Report Imports

## Claim

### Prose Claim


content-preserving migration of existing reports into FPF Analysis Report Carriers.


an FPF Analysis Report import **must** pass all of the following checks before the original Carrier is retired:

- the exact Form and filename token are admitted, the carried Atom ID is unique, and the declared Role, owning Scope Unit, tier, Status and Version metadata match the selected authority;
- exactly one Summary and the ordered Question, Scope, Approach, Results and TLDR sections occur outside the quoted source content, with nonempty values;
- removing only the quotation wrapper recovers every original source byte, including Unicode, line endings, nested headings, code fences and terminal-newline state; its SHA-256 and byte length match the frozen source;
- every selected source has exactly one destination, no existing destination is overwritten, stale inputs and destination collisions stop the batch, and a failed batch does not retire an unverified source;
- rewritten current navigation/source links resolve to the intended new Carriers; historical Journals, archived Revisions, frozen receipts and the quoted report's own historical text remain unchanged.

## Details

These checks verify the import and Carrier structure, not the truth of external findings, FPF execution success, acceptance of recommendations or full framework/runtime conformance. Report unsupported validation coverage explicitly rather than treating an incomplete checker result as a pass.

