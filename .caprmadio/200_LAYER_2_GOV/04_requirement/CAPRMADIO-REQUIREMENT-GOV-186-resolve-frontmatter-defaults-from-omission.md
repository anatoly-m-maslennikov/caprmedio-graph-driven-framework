---
subject_scopes:
  - carrier-format
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-171-omit-default-frontmatter-values
    - CAPRMADIO-REQUIREMENT-GOV-163-resolve-registered-frontmatter-defaults-from-omission
---
# Resolve frontmatter defaults from omission

GOV registers every frontmatter default with its applicability boundary. Writers omit a property when its resolved value equals the applicable default, readers resolve that omission from the same authority, validators reject redundant persisted defaults, and omission means absence when no applicable default exists.
