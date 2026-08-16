---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-173
scope_path: layer:gov
subject_scopes:
  - runtime
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-146-keep-governed-journals-in-role-folders
  child_of:
    - CAPRMADIO-REQUIREMENT-META-188-preserve-governed-action-history-in-journals
    - CAPRMADIO-REQUIREMENT-GOV-116-job-based-carrier-policy
---

# Register the project Work Journal

GOV must register `.caprmadio/010_journals/` as the canonical home of one project-wide logical Work Journal composed of collision-resistant append-only NDJSON segments. Accepted records and sealed segments must never be edited, reordered, or deleted; segmentation must preserve deterministic total replay order.
