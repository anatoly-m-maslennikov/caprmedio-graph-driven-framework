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
version: 13
updated_at: "2026-10-10 23:52:06 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Search CAPRMEDIO Markdown Atoms

the `ATOM_SEARCH` Tool is the canonical Finder for CAPRMEDIO Markdown Atom carriers under the configured Project control root. it **must** support deterministic search over carrier path, filename, frontmatter, **and** content; exact Atom selectors; lifecycle **and** subtree filters; singular **and** bulk results; **and** metadata-only, content-only, **or** combined output. it **may** use generic artifact-query mechanics but owns Atom eligibility, selector, **and** output-view semantics. it **must** never mutate governed project truth.

CA-O-046 defines the read-only Action; CA-E-301 owns the corresponding conformance checks.
