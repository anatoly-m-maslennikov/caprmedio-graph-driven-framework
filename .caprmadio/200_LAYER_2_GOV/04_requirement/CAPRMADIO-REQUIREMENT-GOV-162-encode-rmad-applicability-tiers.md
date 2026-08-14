---
subject_scopes:
  - applicability
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

Every active or draft RMAD Markdown Atom resolves `tier` to `principle`, `core`,
or `standard` and omits `priority`. `standard` is the registered default and
must be omitted; `principle` and `core` are stored as unquoted plain scalars.
Validators reject explicit `standard`, unknown or duplicated values,
role-ineligible `tier`, and `priority` on RMAD Atoms.
