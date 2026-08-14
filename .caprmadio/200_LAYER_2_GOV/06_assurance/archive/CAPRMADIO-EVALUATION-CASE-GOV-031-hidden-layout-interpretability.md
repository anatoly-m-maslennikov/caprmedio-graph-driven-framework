---
artifact_type: evaluation_plan
artifact_id: CAPRMADIO-EVALUATION-CASE-GOV-031
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-042
  - type: replacement_of
    targets:
      - CAPRMADIO-EVALUATION-CASE-GOV-030
---

# Evaluation Case — Interpret the hidden project control layout

Give independent reviewers a repository tree that includes hidden entries and
the DSET artifact filenames. Pass when they consistently:

- recognize `.caprmadio/` as the project control plane rather than product content;
- identify `.caprmadio/caprmadio_settings.toml` as the sole settings/manifest carrier;
- distinguish project-wide records, Version lifecycle artifacts, and direct
  layer-owned truth;
- interpret stored `.caprmadio/...` paths from the repository root;
- allow file-relative Markdown links without treating them as stored control
  paths; and
- identify `.caprmadio/runtime/` as replaceable operational state rather than
  authority.

Record ambiguities rather than resolving them by majority vote. Any materially
different authority or path-base interpretation keeps this Evaluation
inconclusive.

This Evaluation atom is immutable. Later correction requires a successor
Evaluation and append-only lifecycle event.

## Primary claim

A reviewer can identify DSET as a distinct project control plane, find its sole configuration owner, and distinguish repository-root-relative stored paths from file-relative Markdown links.
