---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 17
updated_at: 2026-10-24 00:51:05 +0400
atom_id: CA-R-1059@17
content_role: Requirement
status: Archived
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
tier: 3
---
# Summary

Generate active Requirement Subject Catalog

## Scope

TOOLS contribution represented by this existing legacy Atom.

## Claim

the framework **must** provide one deterministic `project` Tool that writes the active-only Subject Requirement Projection as a registered selected-Scope-Unit destination beneath `.caprmedio_caprmedio/_projection/` with basename `stg_requirements_subjects.md`, groups non-orphan Requirements by their single authored Subject, orders **every** Subject by ascending applicable Global Tier, including General where applicable, **and** then numeric Requirement ID, places one Orphans section last, **and** renders exactly the linked `TYPE + ID`, exact authored `Summary` value in the governed Atom carrier format, **and** direct authored `Child of` columns **without** filename fallback **or** inferred ancestry.
