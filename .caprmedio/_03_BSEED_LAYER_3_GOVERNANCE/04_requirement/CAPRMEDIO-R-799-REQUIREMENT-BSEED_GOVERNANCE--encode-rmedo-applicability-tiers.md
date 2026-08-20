---
subject_scopes:
  - applicability
version: 3
updated_at: 2026-08-21 00:21:06
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

GOV encodes `principle`, `core`, and `standard` as the ordered local applicability-tier catalog. A tier-classified RMEDO Atom at derived global tier `0` resolves to local tier `principle` without storing `tier`; every other active or draft tier-classified RMEDO Markdown Atom resolves `tier` to one registered readable catalog name and omits `priority`. Intent is outside RMEDO and the local tier catalog while occupying global tier `-1`.

Applicable Atoms register the readable tier catalog and default. Project Graph State Projections expose the enabled local tiers and every global number produced by recursive Structural-level derivation for each current level and Scope Unit without becoming authority for them. Validators reject unknown names, invalid Type and Structural-scope combinations, role-ineligible tiers, numeric tier values in Atoms, and `priority` on tier-classified RMEDO Atoms.
