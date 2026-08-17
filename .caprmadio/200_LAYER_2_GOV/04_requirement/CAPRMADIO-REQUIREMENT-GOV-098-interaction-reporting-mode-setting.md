---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-098
scope_path: layer:gov
subject_scopes:
  - interaction
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMADIO-REQUIREMENT-META-058
---
# Configure interaction reporting mode

`caprmadio_settings.toml` provides one project-owned interaction reporting setting:

```toml
[interaction]
reporting_mode = "silent" # silent | verbose
```

The allowed values are exactly `silent` and `verbose`. The default is
`silent`.

In `silent` mode, CAPRMADIO does not announce ordinary mode selection, workflow
routing, skill chaining, or gate transitions. It answers exploratory input
normally and reports only durable artifacts or project state that it created,
updated, archived, committed, or otherwise changed.

In `verbose` mode, CAPRMADIO explicitly reports relevant workflow modes, mode
transitions, selected skill chains, entry and exit gates, and planned or
completed artifact operations.

Reporting mode changes presentation only. It never changes authorization,
artifact creation, workflow routing, validation, or safety behavior. Both
values must still report:

- blockers and failed operations;
- ambiguity that requires operator input;
- permission or approval requests;
- safety-critical information;
- material deviations from the requested outcome.

Skills and tools read this setting from the current project's governance
configuration. They do not maintain independent reporting defaults.

## Rationale

Silent reporting keeps ordinary CAPRMADIO use natural and concise, while verbose
reporting makes orchestration inspectable during adoption, debugging, audits,
and methodology development. Keeping both behaviors behind one project-owned
setting prevents individual skills from drifting into inconsistent interaction
styles.
