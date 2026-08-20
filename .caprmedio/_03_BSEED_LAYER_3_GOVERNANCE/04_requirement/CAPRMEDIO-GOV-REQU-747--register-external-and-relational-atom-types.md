---
subject_scopes:
  - artifact-catalog
project_graph_state:
  artifacts:
    enabled_types:
      - concern:external_problem
      - concern:conflict
      - analysis:external_analysis_report
      - analysis:conflict_analysis_report
      - requirement:constraint
      - requirement:contract
      - method:external_implementation_method
      - method:method_binding
      - evaluation:external_evaluation_standard
      - evaluation:review_protocol
      - implementation:external_git_commit
      - implementation:pull_request
      - ops:external_evidence_record
      - ops:verification_record
version: 2
updated_at: 2026-08-21 00:21:06
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-100--preserve-external-and-relational-boundary-obligations
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  replacement_of:
    - CAPRMEDIO-GOV-REQU-734--register-governance-locus-atom-subtypes
---
# Register external and relational Atom Types

GOV registers the following non-internal Atom Types within their owning Content roles:

| Content role | External Type | Relational Type |
|---|---|---|
| `concern` | `external_problem` | `conflict` |
| `analysis` | `external_analysis_report` | `conflict_analysis_report` |
| `plan` | — | — |
| `requirement` | `constraint` | `contract` |
| `method` | `external_implementation_method` | `method_binding` |
| `evaluation` | `external_evaluation_standard` | `review_protocol` |
| `delivery` | — | — |
| `implementation` | `external_git_commit` | `pull_request` |
| `ops` | `external_evidence_record` | `verification_record` |
