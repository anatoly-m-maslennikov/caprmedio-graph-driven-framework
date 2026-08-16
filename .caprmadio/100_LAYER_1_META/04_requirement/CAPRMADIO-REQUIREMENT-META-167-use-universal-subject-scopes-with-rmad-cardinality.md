---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-167
scope_path: layer:meta
subject_scopes:
  - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-126-require-one-subject-scope-on-every-atom
  child_of:
    - CAPRMADIO-REQUIREMENT-META-100-scope-path-does-not-change-semantic-coordinates
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
---

# Use universal Subject scopes with RMAD cardinality

Every Atom must declare a non-empty `subject_scopes` list selected from the
vocabulary governed for its structural owner. Requirement, Method, Assurance,
and Delivery Atoms must declare exactly one Subject scope because each owns one
independently replaceable specification claim. Every other Content role may
declare one or more Subject scopes when its role-specific atomic unit genuinely
spans them.

Subject scopes classify semantic subjects for discovery and review. They do
not change structural ownership, Applicability, authority, priority,
lifecycle, or relations. Duplicate, unknown, fallback, and semantically
irrelevant values are invalid.
