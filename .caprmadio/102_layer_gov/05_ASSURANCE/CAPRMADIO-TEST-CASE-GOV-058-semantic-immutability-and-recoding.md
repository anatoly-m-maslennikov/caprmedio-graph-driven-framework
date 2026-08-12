---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CAPRMADIO-TEST-CASE-GOV-058
scope_path: layer:gov
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-TEST-CASE-GOV-051
      - CAPRMADIO-TEST-CASE-GOV-052
  - type: check_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-108
---

# QA Case — Semantic immutability and lossless recoding

## Claim checked

Lossless whole-graph recoding and unchanged archive relocation preserve every
protected semantic claim and relation, while semantic mutation requires a new
governed revision or successor.

## Applicable conditions

1. Snapshot every protected semantic field and relation endpoint.
2. Perform a complete identifier, filename, heading, carrier, and target
   spelling migration.
3. Prove the semantic snapshot and graph connectivity are equal after recoding.
4. Move an inactive atom unchanged into its role-local archive.
5. Attempt to change one protected claim, rationale, provenance, scope,
   priority, relation meaning, or assurance criterion and require rejection.

## Acceptance criteria

Lossless graph-wide recoding and unchanged archive relocation pass; every
semantic mutation fails and requires a successor identity.

## Failure disposition

Reject the migration or mutation, retain the previous graph, and record a
high-priority Concern with the first non-equivalent field or edge.
