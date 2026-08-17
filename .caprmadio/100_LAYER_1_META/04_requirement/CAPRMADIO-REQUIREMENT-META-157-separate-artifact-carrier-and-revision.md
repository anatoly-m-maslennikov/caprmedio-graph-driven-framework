---
subject_scopes:
  - artifact-model
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-182-the-graph-is-the-operating-model
---
# Separate artifact carrier and revision

An Artifact is a governed semantic object with a stable identity. A carrier is the physical representation that encodes an Artifact in its native format at a canonical project-relative address. A revision is one exact, recoverable state of that Artifact as represented by a committed carrier state.

Artifact identity survives a carrier move or format-preserving migration when the governed meaning and identity remain valid. A carrier path, filename, file extension, content digest, and Git commit may identify or help resolve a revision, but none alone substitutes for Artifact identity. A native project target outside `.caprmadio/` is Implementation rather than a governed Artifact unless CAPRMADIO separately admits an Artifact that represents or binds it.

Relations and governed transactions bind to the exact Artifact revision they consume. Current carriers may move or be replaced without rewriting the historical revision identities on which earlier work relied.

CAPRMADIO treats the semantic Artifact, its physical carrier, and each exact committed revision as distinct identity levels.
