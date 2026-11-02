---
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Artifact"
    - "Artifact/Carrier"
    - "Atom/Content Role"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: "2026-10-12 23:13:45 +0400"
---
# Summary

Create an artifact carrier

## Scope

Generic Artifact construction mechanics and their boundary with logical CreateAtom.

## Claim

the framework **must** provide one deterministic generic Artifact Tool that allocates the canonical identity **and** filename required by the admitted Artifact Carrier schema **and** creates one Carrier from its structural owner **and** the inputs required by that schema, **without** silently overwriting an existing Carrier.

this Tool owns generic carrier-construction mechanics **only**. `ATOM_CREATE` owns CAPRMEDIO Markdown Atom admission, filename, stable-identity, revision, per-Atom preflight, **and** MCP-gated effect semantics; the generic Tool **must not** become a public alternative for creating such Atoms.

## Details
