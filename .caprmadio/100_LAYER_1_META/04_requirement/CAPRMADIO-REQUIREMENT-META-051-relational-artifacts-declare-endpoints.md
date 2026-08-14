---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-051
scope_path: layer:meta
subject_scope: artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-014
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-098
---

# Requirement — Make relational endpoints explicit

## Primary claim

An artifact routed to relational governance declares one stable relation kind
and at least two role-bearing endpoints. Each endpoint independently declares
whether its participant is internal or external.

Endpoint origin is not another semantic routing axis. Ordinary citations,
traceability links, and relations among otherwise standalone artifacts do not
change their Governance locus.
