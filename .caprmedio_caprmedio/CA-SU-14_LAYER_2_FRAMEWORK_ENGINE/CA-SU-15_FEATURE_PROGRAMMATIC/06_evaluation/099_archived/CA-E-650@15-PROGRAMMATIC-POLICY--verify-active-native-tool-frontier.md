---
atom_id: CA-E-650
ref_id: CA-E-650@15
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 5
relations:
  evaluation_for:
  - CA-M-193
status: Archived
version: 15
updated_at: 2026-11-07 13:19:43 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-650@15-PROGRAMMATIC-POLICY--verify-active-native-tool-frontier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archived
---
# Summary

Verify active native Tool frontier

## Scope

The installed code/configuration callable CAPRMEDIO Tool and Workflow frontier governed by CA-M-193 for a bound Project and shared runtime. Internal CONNECTORS/adapters and PROJECT_TOOLS are excluded.

## Claim

The frontier passes only when every active native Tool is represented with a canonical structural request/result schema and the same decoded payload meaning, while inactive or blocked Tools are excluded. Transport serialization differences are allowed, except for any declared outer Project field such as project_root; no other transport-shape drift is silently introduced. Direct reads remain owned by their canonical Tool without forced workflow routing. Identical structural schemas may be unioned. A partially invalid Project Tool is quarantined and diagnosed without removing healthy Tools, and a failed replacement retains the prior valid frontier explicitly as prior, never as the current frontier.

## Details

- Inventory configured code providers and route names. Verify canonical machine-invocation contracts are exposed and delegated unchanged, with no invented endpoint or hidden composition. Registration and generic call gating must work without an Atom catalog or source-manifest enumeration; operation execution still validates its business prerequisites.
- Verify internal CONNECTORS/adapters and PROJECT_TOOLS never enter this frontier merely because their code or files exist. Preserve direct Tool reads without a mandatory Workflow wrapper.

- Build the frontier from installed code and generated configuration. Compare names, descriptions and code-defined canonical structural schemas, including definitions and required fields; compare decoded request/result meaning rather than transport bytes. Editing or removing unrelated Atoms must not change exposure or trigger a generic registration freshness scan.
- Verify a direct read Tool reaches its canonical owner and preserves the native request/result meaning, with only the declared outer Project field added.
- Present identical same-name schemas and verify one endpoint is possible; present conflicts or a partially invalid Project Tool and verify quarantine and attribution for that Tool while healthy frontier entries remain available.
- Verify inactive, disabled or blocked Tools do not enter the frontier or become callable through stale publication.
- If a replacement frontier is invalid, retain the previous valid frontier with an explicit prior status and do not label it current; mark construction unresolved when native source, Project binding or schema comparison is unavailable.
