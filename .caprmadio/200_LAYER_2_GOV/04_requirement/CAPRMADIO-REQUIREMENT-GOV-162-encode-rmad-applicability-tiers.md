---
subject_scopes:
  - applicability
version: 3
updated_at: 2026-08-17 20:02:25
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-107-effective-priority-conflict-selection
---
# Encode RMAD applicability tiers

GOV encodes the singular external Goal name separately from the ordered project applicability-tier catalog in project settings. Each active or draft tier-classified Project RMAD Markdown Atom resolves `tier` to one registered readable catalog name and omits `priority`; the external Goal uses the registered external-root name and derives depth `-1`. Project tier depth is the zero-based position of its name in the ordered catalog and is never duplicated in an Atom. The registered default tier may be omitted and resolved from settings. Validators reject unknown or duplicated names, duplicate positions, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMAD Atoms.
