---
subject_scopes:
  - applicability
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-139-use-canonical-carrier-address-as-authority
    - CAPRMADIO-REQUIREMENT-META-169-classify-rmad-atoms-by-applicability-tier
    - CAPRMADIO-REQUIREMENT-META-170-route-priority-and-tier-by-content-role
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-107-effective-priority-conflict-selection
---

# Encode RMAD applicability tiers

Every active or draft RMAD Markdown Atom stores exactly one unquoted `tier`
plain scalar with the value `principle`, `core`, or `standard` and omits
`priority`. Validators reject a missing, unknown, duplicated, or role-ineligible
`tier` and reject `priority` on RMAD Atoms.
