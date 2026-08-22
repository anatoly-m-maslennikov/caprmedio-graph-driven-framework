---
name: ca-project-settings
description: Check and regenerate the governed CAPRMEDIO Project Settings and Map Projections from active RMED authority through their registered deterministic Tool. Use when the operator asks to build, update, refresh, synchronize, validate, or diagnose project settings or their exact source frontier.
---

# CA Project Settings

Use the registered Tools as the only writers of native input-Atom revision bindings, the Project Settings Map Projection, and the Project Settings Projection. Treat applicable active RMED `project_settings` contributions as the only semantic input to the two generated outputs.

## Workflow

1. Resolve the repository root containing both `.caprmedio/` and `caprmedio_framework_settings.toml`.
2. Treat check, inspect, validate, or currentness requests as read-only. Treat build, update, refresh, regenerate, or synchronize requests as authorization to update both Projections and the required Framework Settings revision binding; semantic value changes still require an approved change to the owning RMED Atom.
3. Run `python3 002_FRAMEWORK_ENGINE/TOOLS/native_atom_revision.py framework-settings` from the repository root.
4. If it reports `changed=true` during an authorized update, repeat it with `--apply --session-id <current-session-id>`. For a read-only request, report the missing or stale binding without mutation.
5. Run `python3 002_FRAMEWORK_ENGINE/TOOLS/generate_project_settings.py`.
6. If it reports `changed=true` during an authorized update, run it again with `--apply --session-id <current-session-id>`. Never edit `.caprmedio/caprmedio_project_settings.toml` or `.caprmedio/08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml` directly.
7. Repeat both read-only commands and require `changed=false`.
8. Report the exact Framework Settings Atom reference, Map and settings currentness, source count, leaf-binding count, changed outputs, and any rejected source.

## Maintain authority and generation

When an effective setting or its ownership changes, update the owning RMED Atom's `project_settings` contribution through the applicable governed-change flow, then rebuild both Projections. When authority changes composition, TOML grammar, Map grammar, precedence, or validation mechanics, update the registered Tool implementation under `002_FRAMEWORK_ENGINE/TOOLS/`, register the changed Framework Settings Atom revision when applicable, and rebuild both Projections through the workflow above.

Keep deterministic code in Tools. Treat the YAML Map as a versionless `map / implementation` Projection, not an Atom, authoring surface, or third settings carrier. Do not copy executable logic into this Skill, synthesize setting values without active authority, or claim currentness after a failed or partial rebuild.
