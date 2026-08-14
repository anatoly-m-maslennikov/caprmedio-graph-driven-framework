---
artifact_type: method
artifact_subtype: technical_decision
artifact_id: CAPRMADIO-DECISION-GOV-029
scope_path: layer:gov
subject_scopes:
  - layout
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-IMPL-GOV-008
---

# Keep legal files outside the control plane

The repository license remains the root `LICENSE` carrier. Retained third-party
licenses and no-license notices live in the root `LICENSES` directory.

These legal carriers are distribution inputs, not CAPRMADIO methodology, applied
artifacts, settings, runtime state, or historical CAPRMADIO data. They therefore do
not live inside `.caprmadio` and are not visible to skill discovery or semantic
compilation.

Source provenance stores each legal carrier's globally unique filename.
Provenance validation resolves that filename only within `LICENSES`; it does
not perform a repository-wide search or treat the legal file as CAPRMADIO authority.

## Rationale

Legal notices must ship with the repository but answer a different governance
question from project-local CAPRMADIO truth. A separate conventional distribution
surface keeps both responsibilities clear.

## Rationale

Licenses govern repository distribution, while .caprmadio governs current project development state. Keeping legal carriers outside the control plane preserves that boundary and gives standard repository readers a predictable location.
