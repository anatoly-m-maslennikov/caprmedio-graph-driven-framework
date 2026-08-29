---
cce_version: cce_1
cce_form: cardinality
subjects:
  declared:
    continuant:
      - layout
version: 7
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-389--multilevel-architecture-views
  child_of:
    - CA-R-1054
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-297--enabled-one-level-architecture-views.md
---
# Show one structural level when architecture views are enabled

**when** a project enables an architecture-view Projection surface, **every** applicable Project **or** structural-scope view shows **only** its immediate enabled child scopes. **every** scope view shows the functions, capabilities, **or** components directly beneath it.

**every** enabled view explains how its level works **and** how responsibility descends one level. It links active atomic sources for represented claims **and** never claims that navigation creates authority. A disabled surface **or** absent structural level requires no placeholder view.

## Rationale

The successor preserves readable helicopter views while aligning their existence with optional Projection surfaces.
