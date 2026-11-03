---
atom_id: CA-M-345
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: Atom/(.Role := "Analysis & Advisory")/(.Form := FPF Analysis Report)
  passive:
  - Atom.Content.Summary
  - Aspects <+ Engineering <+ Traceability
version: 20
updated_at: 2026-11-02 19:33:47 +0400
relations:
  method_for:
  - CA-R-1889
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-345-PROJECT_CONFIGURATION--author-fpf-analysis-reports.md
  source_atom_id: CA-M-345
  source_atom_revision: 20
  source_sha256: c9642014641c640079c26d022c9dae7f14f184101970ebaed522f4bc43450645
  original_relations_sha256: b70967c5352152ca9b72848a50e82082d932847305b9d8a76594bf66fcb60243
---
## Summary

Author FPF Analysis Reports

## Claim scope

authoring and content-preserving import of FPF Analysis Report Atoms.

## Claim

**to** author an FPF Analysis Report, use the common Analysis & Advisory structure under CA-D-479 and retain the report's bounded question, scope, approach, results, provenance and evidence limits without treating its recommendations as accepted specification.

- carry `role: "Analysis & Advisory"` and `form: FPF Analysis Report`, the actual owning Scope Unit, applicable tier, Status and Version Properties. Summary describes the Question; TLDR summarizes the retained analytical record without replacing Results.
- **when** importing an existing report, preserve its complete original UTF-8 text as quoted Markdown in Results. Quotation is a carrier wrapper, not an edit to the original text. Record its original path, SHA-256 and byte length in Approach so the original bytes can be recovered and checked.
- identify the original inquiry from its explicit task or question where available; otherwise identify the bounded historical report without inventing a missing execution contract. Preserve all native findings, alternatives, citations, limitations and time-relative statements in the quoted record.
- distinguish import metadata and its current Revision timestamp from the original report's provenance. Do not infer an original execution timestamp or completed FPF Run merely from a filename or physical file existence.
- place the Carrier by the applicable Analysis & Advisory Delivery rules. Resolve real destination links to the new Carrier while retaining historical Journal, archive and frozen-evidence references unchanged.

## Details

Importing a report does not rerun FPF, adopt a candidate, change project policy or close an issue. Completion of the bounded imported reporting product is distinct from those outcomes.

