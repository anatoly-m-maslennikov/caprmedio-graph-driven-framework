---
subject_scopes:
  - applicability
project_settings:
  authority:
    tiers:
      default: standard
version: 1
updated_at: 2026-08-20 05:09:11
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-R-795-REQUIREMENT-BSEED_SEMANTICS--admit-applicability-tiers-across-rmedo
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-GOV-REQU-299--effective-priority-conflict-selection
---
# Encode RMEDO applicability tiers

GOV encodes Goal as a Requirement Type, Principle as one role-specific Type in every RMEDO Content role, and `principle`, `core`, and `standard` as the ordered applicability-tier catalog. A Principle Type resolves to local tier `principle` and derived global tier `0` without storing `tier`; Goal derives its global tier from its structural position outside the local catalog. Every other active or draft tier-classified RMEDO Markdown Atom resolves `tier` to one registered readable catalog name and omits `priority`.

Project settings register the readable tier catalog, its default, and every global number produced by the recursive parent-Standard to child-Goal handoff. Validators reject unknown names, invalid Type and Structural-scope combinations, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMEDO Atoms.
