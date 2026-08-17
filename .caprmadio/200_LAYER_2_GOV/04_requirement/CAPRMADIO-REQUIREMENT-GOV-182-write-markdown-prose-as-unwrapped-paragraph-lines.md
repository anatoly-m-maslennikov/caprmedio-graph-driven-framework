---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-182
scope_path: layer:gov
subject_scopes:
  - carrier-format
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
---

# Write Markdown prose as unwrapped paragraph lines

Each prose paragraph in a governed Markdown carrier occupies one unwrapped source line, distinct paragraphs are separated by a blank line, and prose lines have no configured maximum length; frontmatter, headings, lists, tables, block quotations, code blocks, and other Markdown structures retain their native multiline syntax.
