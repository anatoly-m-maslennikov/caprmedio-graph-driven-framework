---
subject_scopes:
  - carrier-format
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-171-omit-default-frontmatter-values
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-123-plain-scalar-frontmatter-values
    - CAPRMADIO-REQUIREMENT-GOV-162-encode-rmad-applicability-tiers
---

# Resolve registered frontmatter defaults from omission

GOV registers each frontmatter default with its applicability boundary.
Readers resolve an omitted property to that registered default, writers omit
an explicitly supplied default, and validators reject redundant persisted
defaults. Without an applicable registered default, omission means absence.
