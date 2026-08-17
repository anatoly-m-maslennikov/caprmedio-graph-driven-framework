---
subject_scopes:
  - applicability
version: 4
updated_at: 2026-08-17 22:35:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-107-effective-priority-conflict-selection
---
# Encode RMAD applicability tiers

GOV encodes the singular Project Goal Requirement subtype separately from the ordered applicability-tier catalog in project settings. Each active or draft tier-classified RMAD Markdown Atom resolves `tier` to one registered readable catalog name and omits `priority`; the Goal uses its registered subtype name and resolves to global tier `-1`. Applicability-tier position is the zero-based position of its name in the ordered catalog and is never duplicated in an Atom. The registered default tier may be omitted and resolved from settings. Validators reject unknown or duplicated names, duplicate positions, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMAD Atoms.
