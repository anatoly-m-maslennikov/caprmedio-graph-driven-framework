---
artifact_type: implementation_decision
artifact_id: CAPRMADIO-DECISION-GOV-025
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-DECISION-GOV-023
---

# Decision — Discover project artifacts by identity

Every DSET skill begins at the target repository's `.caprmadio` control root. It
finds the uniquely named settings carrier and searches that bounded tree for
the requested semantic ID, artifact ID, rule ID, document ID, or unique carrier
name. Zero matches and multiple matches stop.

Authored relations, methodology references, evergreen references, settings
registries, and skill wrappers store identities rather than carrier paths. A
tool may hold the resolved path in memory while reading or writing the selected
carrier, but it does not persist that path as the reference.

Implementation files outside `.caprmadio` remain project content and may be located
after an accepted artifact identifies the implementation subject. They are not
alternative owners of DSET settings or project artifacts.

## Rationale

Identity-only discovery makes numbered reorganization and artifact archival
safe, keeps skills independent of repository topology details, and guarantees
that the project-local `.caprmadio` edition—not a global installation, remote copy,
or root framework source—governs every run.

## Primary claim

CAPRMADIO-to-DSET references use unique identities only, and every skill discovers settings, methodology documents, evergreen artifacts, atomic artifacts, and lifecycle events by identity within the target repository's .caprmadio control root without storing their physical carrier paths.
