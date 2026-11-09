---
atom_id: CA-M-153@27
ref_id: CA-M-153@27
container:
  scope_unit: CA-SU-44
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
tier: 3
relations:
  method_for:
  - CA-R-1076
  derived_from:
  - CA-A-057
status: Archived
version: 27
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-153@27-GRAPH_UI-DECISION--render-and-navigate-active-graph-html.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/05_method/archive
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: GRAPH_UI
claim_target_scope_unit: GRAPH_UI
author: Anatoly Maslennikov
---

## Summary

Render and navigate active graph HTML

## Claim

### Prose Claim

Render **and** use the active graph views through this procedure:

1. Select the applicable declared Scope Units from authoritative Project Structure **and** resolve their registered current `stg_requirements_subjects.md` **and** `stg_requirements_lineage_sections.md` Projection destinations beneath `.caprmedio_caprmedio/_projection/`. Directory observations do not declare Scope Units, and persistent views do not reside beside Scope Unit Atoms.
2. Use the Subject STG files for Subject, tier, **and** orphan placement; use the lineage-section STG files for Principle-root sections **and** direct Requirement relations; **and** read the actual active Atom Markdown for canonical identity, authored Summary value, body, frontmatter, path, **and** current digest. Reject a missing STG, inconsistent STG pair, unresolved Atom, **or** STG-to-Atom digest mismatch.
3. Materialize exactly one `.caprmedio_caprmedio/_projection/mrt_atoms.html` file by atomic replacement. Embed **all** JavaScript **and** presentation assets **in** that file, generate no sibling JavaScript, CSS, data, index, view, **or** per-Atom HTML files, **and** keep service state **only** under `.caprmedio_runtime`.
4. Embed a machine-readable source-lineage manifest covering **every** consumed STG file, **every** underlying Atom, their source-frontier relation, canonical paths, **and** digests. The embedded JavaScript **must** use `WORKBENCH` **to** retrieve current STG **and** Atom content rather than treating embedded HTML text as authority.
5. Derive the structural-unit filter tree from current registered scope paths **and** expose tier, structural-unit, **and** Requirement-subtype filters plus a show-or-hide control for RMED orphans. Preserve complete-graph orphan classification **when** a display filter hides a neighbor.
6. Let the HTML setting select `short` **or** `detailed` initial node display. A short node shows `<Atom ID> <Summary>` from the exact authored Summary value in the governed Atom carrier format; its first click shows the actual current body **without** frontmatter **in** a panel above the node **and** its second click shows complete raw Markdown including frontmatter. A detailed node initially shows that body above the label **and** one click shows complete raw Markdown.
7. Compare **every** live STG **and** Atom digest with the lineage manifest, visibly identify stale STG, stale MRT, **and** unavailable-source states, preserve filters **and** focused-node state **in** the URL, **and** keep each identity linked **to** its canonical source path. Treat the UI as optional: removing it leaves `WORKBENCH`, Tools, **and** MCP operable.

## Details

### Scope

GRAPH_UI contribution represented by this existing legacy Atom.
