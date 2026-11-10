---
identity:
  id: CA-C-722
  ref_id: CA-C-722
context:
  container:
    scope_unit: CA-SU-15
  role: Concern
  form: Problem
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-10 21:28:00 +0400
destination:
  file:
    name: CA-C-722-PROBLEM--legacy-engine-drafts-have-no-atom-identity.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern
relations:
  concern_about:
  - CA-P-2867
  - CA-P-2871
author: Anatoly Maslennikov
---

## Summary

Legacy Engine Drafts have no Atom identity

## Concern

Fifteen existing Engine Drafts have Role and content but no Atom ID. Their filenames use empty ID markers such as CA-D--. The earlier census required an ID and omitted them, so it could not establish complete Current/Draft source coverage or query accessibility.

## Details

The fifteen Drafts include eight Deliveries, three Evaluations, one Method and three Requirements. They are in PROGRAMMATIC, MCP, WORKBENCH, GRAPH_UI, APPS and SKILLS. All are now tracked by file path and hash; those tracking keys are not fabricated Atom IDs.

Review their topics, Claims, Roles and duplicate coverage before adoption. Give each retained new Draft its canonical identity and filename through the source-correction process. If its claim belongs in an existing Atom, use that survivor rather than assigning an ID merely to preserve a duplicate. Preserve the authored content during structure-only repair.

A readable source-file review does not prove query_run admission. Record remaining indexing and declared-content defects separately. No reader code change or source promotion is performed by this Problem.

## Resolution

All fifteen legacy markers have recorded dispositions: ten retained canonical Atoms are Current and five rejected or obsolete trials are preserved as withdrawn history. The Current graph and identity checks pass. The MCP declaration trial is covered by Current D704/R1107/R1110/R1116; Graph Server storage meaning is covered by D675/R1603 and its obsolete bindings are discarded. D712-specific Graph UI URL/filter/focus and standalone placement design is discarded with the obsolete application; useful state separation remains in D673/D675/R1603. No wholesale D712 coverage is claimed.

This closes source correction, not deployed query accessibility. C716 and implementation reader tasks retain runtime follow-up.
