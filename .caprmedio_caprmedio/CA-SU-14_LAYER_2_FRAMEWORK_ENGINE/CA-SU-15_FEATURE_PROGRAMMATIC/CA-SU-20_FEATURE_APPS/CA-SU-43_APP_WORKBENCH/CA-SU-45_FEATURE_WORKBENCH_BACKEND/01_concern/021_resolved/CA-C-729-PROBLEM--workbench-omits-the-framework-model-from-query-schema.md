---
identity:
  atom_id: CA-C-729
  ref_id: CA-C-729
context:
  container:
    scope_unit: CA-SU-45
  role: Concern
  form: Problem
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-11 08:51:05 +0400
destination:
  file:
    name: CA-C-729-PROBLEM--workbench-omits-the-framework-model-from-query-schema.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern/021_resolved
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-R-2726
  - CA-M-500
  - CA-D-672
---

## Summary

Workbench omits the Framework model from query schema

## Concern

The live image exposes 68 atoms columns with no content.* columns. Its generated canonical Relation registry is empty too. R2726 and M500 require Current-model-declared Content and regenerated Role/Form applicability; a successful count(*) query does not satisfy that contract.

SourceReader selects only role directories reached through Current Project Scope Unit Declarations. The current reader returns 36 units and no CORE_META_MODEL or METHODOLOGY_SOURCES because R2648 FRAMEWORK_METHODOLOGY is archived. The Framework declarations remain on disk outside that selected Project tree, so neither schema compiler receives them. A live audit query for R2498/R2499/R2478 returns no rows because these files are outside its inventory; it is not proof they are queryable.

## Details

P2866 must bind the authoritative Current Framework-model input independently of the Project instance inventory, then verify declared Content, Role/Form applicability, relations and affected-source refresh through query_run. Confirm the established source/configuration with the Model owner; do not restore retired Scope declarations, infer authority from arbitrary copied directories or count copied/staged documents as Current sources. The running Header-only queries remain available.

Evidence: .caprmedio_tmp/CA-P-2791/CA-P-2811/query_schema.json and .caprmedio_tmp/CA-P-2791/CA-P-2866/declaration-content-issues.json.

## Resolution

Local Release installed Workbench 0.4.4.43. Workbench HTTP and MCP query_run returned seven declared Content columns, native Formal Claims and matching direct and derived containment. The shared Scope Unit reader also admits the current Framework Methodology declaration and its four descendants. See CA-P-2964 for installed evidence.
