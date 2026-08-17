---
artifact_type: constraint
artifact_id: CAPRMADIO-CONSTRAINT-GOV-002
scope_path: layer:gov
subject_scopes:
  - external-boundary
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMADIO-REQUIREMENT-META-099-nonduplicative-current-artifact-properties
    - CAPRMADIO-REQUIREMENT-GOV-116-job-based-carrier-policy
---

# Preserve GitHub preview compatibility

Every CAPRMADIO-owned Markdown or TOML artifact must remain legible and navigable in
GitHub's repository file preview.

Markdown artifacts must:

- use valid YAML frontmatter and GitHub Flavored Markdown;
- use repository-relative Markdown links and image paths;
- use only GitHub-supported alerts: `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, and
  `CAUTION`;
- use `<details><summary>` for collapsible sections;
- use fenced `mermaid` blocks for diagrams; and
- avoid Obsidian wiki links, embeds, and Obsidian-only callout syntax.

TOML artifacts must:

- remain valid UTF-8 TOML;
- be understandable in GitHub's source view without a generated renderer;
- use descriptive keys, comments, and section ordering when they materially
  improve readability; and
- avoid encoding required meaning only through editor-specific behavior.

GitHub-preview compatibility does not require GitHub Pages publication or
prevent other consumers from rendering the same portable files.

## Historical frontmatter metadata

```yaml
source_refs:
  - "https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax"
  - "https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams"
  - "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes"
  - "https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files"
  - "https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter"
```
