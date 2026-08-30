---
atom_id: CA-E-386
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Type-Qualified Status Validation
  depends_on:
    continuant:
      - Entity/Type/Status
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-386-MMODEL-CORE-EVALUATION--validate-type-qualified-status.md
---
# Validate Type-Qualified Status

the Evaluation **must** reject an Artifact **if** its Status domain is resolved globally instead of from its complete Entity-Type path, it has zero **or** multiple current Status values, a Spec Content Role Atom lacks a Core Status **in** (Draft, Active, Archived), a Task Atom lacks a Core Status **in** (Draft, Active, Done, Canceled), a prior transition coexists as current Status metadata, **or** a second revision-disposition axis duplicates Status.
