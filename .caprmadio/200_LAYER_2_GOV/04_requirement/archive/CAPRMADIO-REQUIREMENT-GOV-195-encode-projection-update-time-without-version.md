---
subject_scopes:
  - carrier-format
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-206-keep-projections-versionless
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
---
# Encode Projection update time without version

Every Projection frontmatter carries `updated_at` as the RFC 3339 UTC time of its latest completed rebuild and omits `version`. A rebuild updates `updated_at`; currentness remains derived from the declared source frontier, generator, and configuration rather than from that timestamp.
