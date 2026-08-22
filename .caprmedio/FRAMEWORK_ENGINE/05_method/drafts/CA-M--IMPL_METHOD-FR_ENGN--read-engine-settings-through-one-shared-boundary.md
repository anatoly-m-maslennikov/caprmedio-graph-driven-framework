---
subject_scopes:
  - framework-engine-software
  - project-settings
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Read Engine settings through one shared boundary

Use one centralized Settings Reader for every applicable Tool, App, and MCP component. It reads only `.caprmedio/caprmedio_project_settings.toml`, validates the complete input with strict Pydantic models, and returns an immutable typed snapshot with source and version provenance. The reader performs no business decision and no write.

Pass the validated snapshot to the consuming manager or application service as explicit input. No Engine component may implement its own project-settings parser, default chain, environment fallback, or semantic override. The control panel must use the same reader; a settings change must go through the governed RMED settings authority and its dedicated Doer rather than edit the generated Project Settings Projection directly.

Keep Python build, formatter, linter, typing, and test-runner configuration separate from project runtime settings.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-003, CA-R-004, CA-R-827.

## Sources

- [Python documentation: `tomllib`](https://docs.python.org/3/library/tomllib.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/api/config/)
- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
