---
identity:
  atom_id: CA-E-675
  ref_id: CA-E-675@10
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Source Retrieval
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2726
  - CA-M-464
  - CA-D-672
state:
  status: Archived
  version: 10
  updated_at: 2026-11-10 22:20:17 +0400
destination:
  file:
    name: CA-E-675@10-WORKBENCH_BACKEND-EVAL_CASE--preserve-nested-header-and-markdown-property-distinction.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Preserve nested Header and Markdown Property distinctions

## Claim scope

Current-model-guided in-memory parsing of governed carriers.

## Claim

### Prose Claim

Parse YAML Header and actual CommonMark headings directly. Private parsed Header/Markdown retain their distinction and complete body; public Mode 1 exposes only model-declared Header/Content paths, while enabled Mode 2 exposes every observed valid Header path and declared Content columns. Names use dotted lowercase snake_case paths, never old `id`/`status`/`role` aliases; do not expose raw Header/Markdown/property/relation buckets or source bytes.

## Details

Verify absence/null/empty/scalar/list/map/false/zero distinctions; LF/CRLF preservation; duplicate-key rejection; nested direct versus subtree Markdown; actual headings versus declared public Content; and Prose Claim/Formal Claim/fenced-heading handling. `Header.Context.Plan` maps to `header.context.plan` without a wrapper; ambiguous flattening fails rather than merging paths. `header.relations` matches native facts once. Mode 2 rebuilds for new/last-removed/type-changed/globally emptied Header paths, keeps observed empty paths and treats false/zero as values; same-schema edits stay incremental and unadmitted presentation headings do not become Content columns.


### Role and Form applicability after image rebuild

- Build an image from Current Declarations and query valid Current and Draft fixtures for each of the eight Roles: Concern, Analysis & Advisory, Plan, Requirement, Method, Evaluation, Delivery and Operations. For each applicable Form, assert that admitted sections are available under their declared Content paths. Include Concern, Objective, Operation and Analysis & Advisory report sections; retain their text and paths without converting them into Claims.
- Add a Role or Form Declaration or change its Content applicability in the fixture source, rebuild the image, and assert that the resulting query model and columns reflect the new or changed declaration. Repeat with another applicable Role or Form to detect a fixed Role/Form list; unchanged declarations and existing query behavior remain intact.
- Exercise Content paths admitted by an applicable wildcard, including nested headings and multiword segments. Assert dotted lowercase snake_case column names and the correct values in both modes. A heading not admitted by an applicable Content rule remains presentation text and creates no Content column. Add and remove a wildcard-admitted Content path in valid sources and verify schema/table refresh in both modes; a value-only edit with unchanged schema remains incremental.
- Where more specific declarations govern Prose Claim or Formal Claim, verify their prescribed parsing and retain internal prose headings as text. Headings inside fenced blocks remain text, including heading-shaped lines; neither a wildcard nor a nested heading converts them into Content properties.
- Run the existing invalid-source, duplicate-key, Header/Markdown distinction and Mode 1/Mode 2 cases alongside these fixtures. Invalid content stays excluded; declaration changes do not weaken the existing rebuild and incremental-update boundaries.
