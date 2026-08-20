---
subject_scopes:
  - settings
version: 4
updated_at: 2026-08-20 18:32:49
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-619--classify-framework-settings-as-an-implementation-atom
---
# Encode framework settings as a native TOML Atom

`caprmedio_framework_settings.toml` must contain only executable framework-engine
settings and human-readable configuration comments in native TOML. It must not
embed YAML frontmatter, `atom_id`, Revision metadata, relations, rationale, or
provenance. A governed external Atom binding carries those properties for this
native Atom.
