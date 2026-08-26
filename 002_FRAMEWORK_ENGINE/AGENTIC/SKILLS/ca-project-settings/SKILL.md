---
name: ca-project-settings
description: Check and regenerate the governed CAPRMEDIO Project Scope Unit Graph and Sources Projections from Project Configuration, admitted graph contributions, current graph structure, and Journal inputs. Use when the operator asks to build, update, refresh, synchronize, validate, or diagnose the current Scope Unit Graph or its exact sources.
---

# CA Project Scope Unit Graph

Use the registered Tools as the only writers of native Project Configuration revision bindings and the two Project Scope Unit Graph Projections. Treat `caprmedio_framework_settings.toml` as the sole carrier of current operator-selected values. Treat applicable active RMED `project_scope_unit_graph` and `project_graph_state` contributions, current graph structure, and applicable Journal inputs as the only other admitted inputs.

## Workflow

1. Resolve the repository root containing both `.caprmedio/` and `caprmedio_framework_settings.toml`.
2. Treat check, inspect, validate, or currentness requests as read-only. Treat build, update, refresh, regenerate, or synchronize requests as authorization to update both Projections and the required Project Configuration revision binding; semantic value changes still require an approved Configuration change.
3. Run `python3 002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/native_atom_revision.py framework-settings` from the repository root.
4. If it reports `changed=true` during an authorized update, repeat it with `--apply --session-id <current-session-id>`. For a read-only request, report the missing or stale binding without mutation.
5. Run the selected installed `GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py` Tool without `--apply`.
6. If it reports `changed=true` during an authorized update, repeat it with `--apply`. Never edit `.caprmedio/project_scope_unit_graph.projection.toml` or `.caprmedio/project_scope_unit_graph_sources.projection.toml` directly.
7. Repeat both read-only commands and require `changed=false`.
8. Report the exact Project Configuration Atom reference, Scope Unit Graph currentness, admitted-source count, changed outputs, and any rejected source.

## Maintain authority and generation

When an effective current operator-selected value changes, update `caprmedio_framework_settings.toml` through the applicable governed-change flow, then rebuild both Projections. When registered graph facts, defaults, or structural context change, update the applicable active RMED `project_scope_unit_graph` or `project_graph_state` contribution. When authority changes composition, TOML grammar, Map grammar, precedence, or validation mechanics, update the registered Tool implementation under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/`, register the changed Project Configuration revision when applicable, and rebuild both Projections through the workflow above.

Keep deterministic code in Tools. Treat the TOML Sources Projection as a versionless `map / implementation` Projection, not an Atom, authoring surface, or second Configuration carrier. Do not copy executable logic into this Skill, synthesize values without admitted authority, read a prior Projection as an input, or claim currentness after a failed or partial rebuild.
