---
atom_id: CA-R-863
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool/ATOM_SEARCH"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 14
updated_at: "2026-10-10 23:53:36 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Search CAPRMEDIO Markdown Atoms

## Scope

Search valid CAPRMEDIO Markdown Atom carriers under the configured Project
control root.

## Claim

The `ATOM_SEARCH` Tool is the canonical Finder for CAPRMEDIO Markdown Atom
carriers. It **must** support deterministic search over carrier path, filename,
frontmatter, and content; exact Atom selectors; lifecycle and subtree filters;
singular and bulk results; and metadata-only, content-only, or combined output.
It may use generic artifact-query mechanics but owns Atom eligibility, selector,
and output-view semantics. It **must** never mutate governed project truth.

For direct Subject lookup, the Tool **must** additionally accept the following
conjunctive request fields:

- `--subject VALUE`;
- `--subject-field governs|depends_on|both`;
- `--subject-match exact|prefix`;
- repeatable `--content-role ROLE`; and
- `--scope-unit OWNER`, together with the existing `--under` and `--lifecycle`
  filters.

The lookup reads only direct structured `subjects.governs` and
`subjects.depends_on` values from an already-valid Atom carrier. `exact` is
literal equality. `prefix` is lexical only: it matches the requested value or
the requested value followed by the current `/` or `:` boundary. It does not
infer an ontology relation or adopt a broader Subject grammar.

Each match **must** identify the Atom ID, Version, Status, owner Scope Unit,
repository-relative path, SHA-256, Updated At, matched field, dependency index
when applicable, and exact matched value. The Tool **must** reject an invalid
request and report an invalid selected candidate separately; it must not silently
turn an invalid candidate into an ordinary non-match.

## Details

CA-O-046 defines the read-only Action; CA-E-301 owns the corresponding conformance checks.
