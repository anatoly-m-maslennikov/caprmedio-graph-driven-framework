---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-116
scope_path: layer:gov
subject_scopes:
  - carrier-format
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-110-job-based-carrier-policy
    - CAPRMADIO-DECISION-GOV-014-toml-optional-unset-normalization
    - CAPRMADIO-DECISION-GOV-015-json-schema-boundary
    - CAPRMADIO-ANALYSIS-REPORT-004-artifact-carrier-format-policy
  relates_to:
    - CAPRMADIO-CONSTRAINT-GOV-002-github-preview-compatibility
---
# Select carriers by their governed job

Every governed Markdown artifact starts with valid YAML frontmatter containing
its applicable non-derived properties. Frontmatter is non-empty, does not
duplicate narrative body content, and does not repeat semantic route
coordinates already determined by the registered artifact type.

CAPRMADIO uses these default carrier boundaries:

| Carrier | Governed job |
|---|---|
| Markdown with YAML frontmatter | Human-governed Atoms and Projections with narrative meaning |
| TOML | Human-edited configuration executed directly by tools |
| JSON | External contracts, standardized schemas, wire data, and generated machine data |
| NDJSON | Append-only Journals and ordered record streams under the applicable `.caprmadio` role folder |
| Native format | Source code, Tests, Evaluations, CI workflows, lockfiles, host manifests, and other prescribed implementation files |

Carrier selection follows the artifact's authoring and consumption boundary,
not its layer or implementation language. A binding standard, ecosystem, or
external obligation keeps its prescribed format and does not gain a parallel
writable representation.

Markdown frontmatter uses `---`. YAML is not a standalone CAPRMADIO artifact format.
Embedded source examples are content rather than separate artifacts.
