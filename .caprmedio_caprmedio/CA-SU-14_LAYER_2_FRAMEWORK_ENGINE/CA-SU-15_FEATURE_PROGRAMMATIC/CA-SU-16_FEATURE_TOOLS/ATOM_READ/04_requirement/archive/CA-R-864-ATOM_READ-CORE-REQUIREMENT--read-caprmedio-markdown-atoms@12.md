---
subjects:
  governs: "Tool/ATOM_READ"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 12
updated_at: "2026-10-12 23:13:45 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
---
# Summary

Read CAPRMEDIO Markdown Atoms

## Scope

Independent reads of explicitly selected CAPRMEDIO Markdown Atom sources.

## Claim

the `ATOM_READ` Tool is the canonical Finder for resolving one **or** many CAPRMEDIO Markdown Atoms from an exact repository-relative path, full filename, filename stem, **or** Atom ID. Read **must** be independently invocable for an explicit Atom identity without a preceding Find. Its complete-source result **must** carry the exact Atom ID, Version and source pin with the full selected source; explicitly requested content-only or metadata-only views remain permitted. metadata **must** include the raw frontmatter **and** identity, placement, **and** lifecycle facts derived from the carrier filename **and** location. it **may** use generic metadata retrieval but owns Atom resolution **and** output-view semantics. missing **or** ambiguous selectors **must** fail explicitly, **and** the Tool **must** never mutate governed project truth.

CA-O-047 defines the read-only Action; CA-E-302 owns the corresponding conformance checks.

## Details
