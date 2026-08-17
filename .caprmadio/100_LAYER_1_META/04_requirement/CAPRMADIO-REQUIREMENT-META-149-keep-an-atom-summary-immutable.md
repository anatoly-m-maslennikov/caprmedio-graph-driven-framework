---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-149
scope_path: layer:meta
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-128-bind-governed-transactions-to-stable-artifact-revisions
    - CAPRMADIO-REQUIREMENT-META-157-separate-artifact-carrier-and-revision
---
# Keep an Atom summary immutable

An admitted Atom may receive governed revisions while its filename summary
continues to identify the same role-specific atomic unit accurately. Every
committed revision remains immutable and recoverable through governed history.

The filename summary is immutable for the lifetime of the Atom identity. If a
revision would require a different summary to describe its atomic unit
accurately, CAPRMADIO creates a successor Atom with a new identity and archives
the current Atom after the successor is admitted.

An Atom may be revised under an unchanged filename summary, but a required summary change creates a successor Atom and retires the current identity.
