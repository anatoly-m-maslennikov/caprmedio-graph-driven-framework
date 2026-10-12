---
subjects:
  governs: "artifact-operations"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: "2026-10-12 23:13:45 +0400"
---
# Summary

Rename an artifact carrier

## Scope

Generic Artifact rename mechanics and their boundary with logical Atom relocation.

## Claim

the framework **must** provide one deterministic generic Artifact Tool that renames one artifact carrier under the active filename grammar, rejects collisions, rewrites governed canonical references, records the identity mapping, **and** rolls back the complete rename **when** **any** required rewrite fails.

this Tool owns generic rename mechanics **only**. `ATOM_MOVE` owns CAPRMEDIO Markdown Atom relocation, identity preservation, destination validation, one-Atom storage-effect safeguards, **and** MCP-gated effect semantics; the generic Tool **must not** become a public alternative for moving such Atoms.

## Details
