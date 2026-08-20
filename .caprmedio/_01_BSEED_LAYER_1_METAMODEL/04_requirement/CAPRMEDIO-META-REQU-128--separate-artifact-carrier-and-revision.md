---
subject_scopes:
  - artifact-model
tier: core
version: 5
updated_at: 2026-08-20 20:03:45
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--use-the-graph-to-organize-project-work
---
# Separate artifact carrier and revision

CAPRMEDIO distinguishes an Artifact from its Carrier and Revisions. An Artifact is a governed semantic object. `atom_id`, when present, is a property of an Atom Artifact rather than of its Carrier or any one Revision. A Carrier is the Artifact's mutable physical representation in a native format at a governed project-relative address. A Revision is one exact recoverable Carrier state. Carrier address, filename, and content may change without replacing the Atom or changing its assigned `atom_id`.
