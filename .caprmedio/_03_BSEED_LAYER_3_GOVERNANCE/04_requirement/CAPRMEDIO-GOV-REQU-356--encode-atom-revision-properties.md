---
subject_scopes:
  - carrier-format
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-18 07:11:22
relations:
  child_of:
    - CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Encode Atom revision properties

Every Atom revision encoding carries `version` as a positive integer and `updated_at` in `YYYY-MM-DD HH:MM:SS` format interpreted in the configured Artifact timestamp timezone. Markdown Atoms encode both properties in YAML frontmatter. A registered native Atom whose executable format excludes governance metadata encodes both properties in its governed external revision binding. Creation writes version one; every committed edit to the Atom carrier contents, including a carrier-only correction, increments `version` by exactly one and updates `updated_at` in the same operation. A path-only lifecycle move changes neither property, while a replacement Atom starts at version one.
