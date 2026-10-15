---
subjects:
  governs: "artifact-operations"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: "2026-10-12 23:13:45 +0400"
---
# Summary

Patch artifact metadata

## Scope

Generic Artifact frontmatter patch mechanics and their boundary with logical Atom Modify.

## Claim

the framework **must** provide one deterministic generic Artifact Tool that applies a schema-validated field-level patch **to** one artifact's frontmatter, preserves its body bytes, updates governed revision metadata, **and** rejects unknown fields **or** failed preconditions.

this Tool owns form-agnostic carrier-patch mechanics **only**. it **must not** be exposed **or** applied as a substitute for `ATOM_UPDATE` **to** a CAPRMEDIO Markdown Atom; `ATOM_UPDATE` owns that Atom's target resolution, authority validation, revision transition, one-Atom storage-effect safeguards, **and** MCP-gated effect, **and** **may** use this Tool **only** as an internal helper.

## Details
