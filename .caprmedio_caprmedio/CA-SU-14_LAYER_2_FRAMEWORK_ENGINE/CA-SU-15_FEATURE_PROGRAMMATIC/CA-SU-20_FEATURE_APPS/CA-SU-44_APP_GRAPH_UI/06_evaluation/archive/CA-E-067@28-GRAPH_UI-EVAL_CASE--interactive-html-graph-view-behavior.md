---
atom_id: CA-E-067@28
ref_id: CA-E-067@28
container:
  scope_unit: CA-SU-44
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
tier: 4
relations:
  evaluation_for:
  - CA-R-1076
  - CA-M-153
  derived_from:
  - CA-A-057
status: Archived
version: 28
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-E-067@28-GRAPH_UI-EVAL_CASE--interactive-html-graph-view-behavior.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/06_evaluation/archive
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: GRAPH_UI
claim_target_scope_unit: GRAPH_UI
author: Anatoly Maslennikov
---

## Summary

Interactive HTML graph view behavior

## Claim

### Prose Claim

the single generated MRT renders current active Requirement Subject **and** lineage-section views from their STG Projections **and** actual Atom sources **without** becoming a second authority surface.

## Details

### Scope

GRAPH_UI contribution represented by this existing legacy Atom.

### Test case

1. Create current `stg_requirements_subjects.md` **and** `stg_requirements_lineage_sections.md` at registered destinations beneath `.caprmedio_caprmedio/_projection/` for multiple selected declared Scope Units, materialize the MRT, **and** require exactly one `.caprmedio_caprmedio/_projection/mrt_atoms.html` with embedded JavaScript **and** presentation assets **and** no sibling script, stylesheet, data, index, view, **or** per-Atom HTML files.
2. Require the MRT source-lineage manifest **to** name **every** consumed STG file **and** **every** underlying active Atom with canonical path **and** digest; require the Subject **and** lineage-section views **to** match the STG structure while node text, body, frontmatter, **and** live digest match the actual Atom.
3. Change registered project scope paths **and** require the structural-unit filter tree **and** discovered STG set **to** change **without** code modification; exercise tier, structural-unit, **and** Requirement-subtype filters **and** require no inactive Requirement **to** become visible.
4. Toggle RMED orphans **and** prove filtering never recomputes orphan status **or** invents an orphan merely because its neighbor is hidden.
5. **in** `short` mode, require `<Atom ID> <Summary>` from the exact authored Summary value in the governed Atom carrier format, body **without** frontmatter **in** a panel above the node on first click, **and** complete raw Atom source including frontmatter on second click.
6. **in** `detailed` mode, require the same label plus the actual full body **without** frontmatter above the node **and** complete raw Atom source including frontmatter on one click.
7. Change one STG file **and** one Atom independently **after** MRT generation; require the embedded JavaScript **to** retrieve the current sources **and** visibly distinguish stale STG, stale MRT, **and** changed-Atom digest states.
8. Preserve filter **and** focused-node state **in** the URL, keep **every** identity linked **to** its canonical Atom path, **and** prove deleting `mrt_atoms.html` changes no Atom, STG Projection, Journal, `WORKBENCH`, Tool, **or** MCP capability.

### Acceptance criteria

**every** selected active Requirement **and** direct edge appears **in** the correct Subject **and** lineage-section view, the one-file MRT declares complete STG-and-Atom lineage, **every** filter **and** display mode behaves deterministically, live interactions expose the required source forms **and** stale states, **and** the HTML remains non-authoritative.

### Failure disposition

Reject the MRT build, identify the first missing, extra, ambiguous, stale, incorrectly linked, **or** incorrectly interactive element, **and** retain the STG Requirement Projections as the preceding current derived views.

### Sources

- [CA-R-1076 — Render interconnected HTML graph views](../04_requirement/CA-R-1076-GRAPH_UI-RULE--render-interconnected-html-graph-views.md)
- [CA-M-153 — Render and navigate active graph HTML](../05_method/CA-M-153-GRAPH_UI-DECISION--render-and-navigate-active-graph-html.md)
