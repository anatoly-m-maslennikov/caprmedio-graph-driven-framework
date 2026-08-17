---
artifact_type: implementation_decision
artifact_id: CAPRMADIO-DECISION-GOV-022
scope_path: layer:gov
subject_scopes:
  - methodology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-051
      - CAPRMADIO-REQUIREMENT-GOV-046
---

# Decision — Separate methodology from applied project artifacts

The project-local DSET control plane uses three visibly distinct carriers:

```text
.caprmadio/000_caprmadio_methodology/   installed project-local DSET methodology
.caprmadio/100_project/            applied project-wide artifacts
.caprmadio/100_LAYER_1_META/         applied META artifacts
.caprmadio/200_LAYER_2_GOV/          applied GOV artifacts
.caprmadio/103_layer_tool/         applied TOOL artifacts
.caprmadio/104_layer_skill/        applied SKILL artifacts
.caprmadio/105_layer_ops/          applied OPS artifacts
.caprmadio/150_versions/           applied Version artifacts
```

The reusable DSET framework source remains a separate governed product surface
at the repository root:

```text
10_project/
11_layer_meta/
12_layer_gov/
13_layer_tool/
14_layer_skill/
15_layer_ops/
50_versions/
```

`000_caprmadio_methodology` contains governing rules, procedures, schemas,
templates, and workflow definitions. It never owns this project's Decisions,
Questions, Problems, QA atoms, evidence, or applied specifications and plans.

## Rationale

Methodology defines how the project works; applied artifacts record what this
project decides, plans, checks, and observes. Keeping those carriers in
separate numbered namespaces prevents framework rules from being mistaken for
project state while preserving deterministic local rule resolution for thin
skills.

## Primary claim

DSET stores the installed project-local methodology only under .caprmadio/000_caprmadio_methodology, stores applied project artifacts only under .caprmadio/100_project through .caprmadio/150_versions, and keeps the reusable framework source in the repository root's 10_project through 50_versions product structure.
