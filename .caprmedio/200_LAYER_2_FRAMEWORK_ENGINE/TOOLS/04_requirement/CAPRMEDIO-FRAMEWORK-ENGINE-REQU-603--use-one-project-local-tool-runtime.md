---
subject_scopes:
  - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-21 01:09:53
relations:
  child_of:
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Use one project-local Tool runtime

All Tools in one CAPRMEDIO project must execute through the same project-local managed environment rooted under `.caprmedio_runtime`, with one governed dependency definition and no Tool-specific runtime environments. The installed runtime must contain every executable, non-executable library, machine-readable registry, and declared dependency needed by the installed Tools; an installed Tool must not import or read framework implementation from another project path. A host-required discovery carrier may point into the runtime, but it must contain no executable framework behavior and must not become dependency authority.
