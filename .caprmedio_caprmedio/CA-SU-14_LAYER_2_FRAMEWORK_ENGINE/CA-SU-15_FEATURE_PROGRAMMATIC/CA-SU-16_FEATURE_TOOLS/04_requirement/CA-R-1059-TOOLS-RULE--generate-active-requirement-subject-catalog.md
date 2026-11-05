---
atom_id: CA-R-1059
ref_id: CA-R-1059
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 3
status: Active
version: 24
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1059-TOOLS-RULE--generate-active-requirement-subject-catalog.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Generate active Requirement Subject Catalog

## Scope

TOOLS contribution represented by this existing legacy Atom.

## Claim

the framework **must** provide one deterministic `project` Tool that writes the active-only Subject Requirement Projection as a registered selected-Scope-Unit destination beneath `.caprmedio_caprmedio/_projection/` with basename `stg_requirements_subjects.md`, groups non-orphan Requirements by their single authored Subject, orders **every** Subject by ascending applicable Global Tier, including General where applicable, **and** then numeric Requirement ID, places one Orphans section last, **and** renders exactly the linked `TYPE + ID`, exact authored `Summary` value in the governed Atom carrier format, **and** direct authored `Child of` columns **without** filename fallback **or** inferred ancestry.
