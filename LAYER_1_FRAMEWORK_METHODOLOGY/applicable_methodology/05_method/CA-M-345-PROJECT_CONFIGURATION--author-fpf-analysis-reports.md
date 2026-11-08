---
atom_id: CA-M-345
ref_id: CA-M-345
container:
  scope_unit: CA-SU-13
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := FPF Analysis Report)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
tier: 3
relations:
  method_for:
  - CA-R-1889
status: Active
version: 20
updated_at: 2026-11-02 19:33:47 +0400
carrier_destination:
  file:
    name: CA-M-345-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--author-fpf-analysis-reports.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-345-PROJECT_CONFIGURATION--author-fpf-analysis-reports.md
  source_atom_id: CA-M-345
  source_atom_revision: 20
  source_sha256: b2b3ca39509e6eed4e56c5724d1b7ad24b771da49f528989dc8875c8a9c49a41
  original_relations_sha256: b70967c5352152ca9b72848a50e82082d932847305b9d8a76594bf66fcb60243
---
## Summary

Author FPF Analysis Reports

## Claim

### Prose Claim


authoring and content-preserving import of FPF Analysis Report Atoms.


**to** author an FPF Analysis Report, use the common Analysis & Advisory structure under CA-D-479 and retain the report's bounded question, scope, approach, results, provenance and evidence limits without treating its recommendations as accepted specification.

- carry `role: "Analysis & Advisory"` and `form: FPF Analysis Report`, the actual owning Scope Unit, applicable tier, Status and Version Properties. Summary describes the Question; TLDR summarizes the retained analytical record without replacing Results.
- **when** importing an existing report, preserve its complete original UTF-8 text as quoted Markdown in Results. Quotation is a carrier wrapper, not an edit to the original text. Record its original path, SHA-256 and byte length in Approach so the original bytes can be recovered and checked.
- identify the original inquiry from its explicit task or question where available; otherwise identify the bounded historical report without inventing a missing execution contract. Preserve all native findings, alternatives, citations, limitations and time-relative statements in the quoted record.
- distinguish import metadata and its current Revision timestamp from the original report's provenance. Do not infer an original execution timestamp or completed FPF Run merely from a filename or physical file existence.
- place the Carrier by the applicable Analysis & Advisory Delivery rules. Resolve real destination links to the new Carrier while retaining historical Journal, archive and frozen-evidence references unchanged.

## Details

Importing a report does not rerun FPF, adopt a candidate, change project policy or close an issue. Completion of the bounded imported reporting product is distinct from those outcomes.

