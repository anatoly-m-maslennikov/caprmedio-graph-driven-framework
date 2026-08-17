---
subject_scopes:
  - applicability
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-107-effective-priority-conflict-selection
---
# Encode RMAD applicability tiers

When a project enables applicability-tier classification, each active or draft
RMAD Markdown Atom within that model resolves `tier` to `principle`, `core`, or
`standard` and omits `priority`. Within that model, `standard` is the
registered default and must be omitted; `principle` and `core` are stored as
unquoted plain scalars. Outside an enabled tier model, `tier` is omitted.
Validators reject explicit `standard`, unknown or duplicated values,
role-ineligible `tier`, and `priority` on RMAD Atoms within an enabled tier
model.
