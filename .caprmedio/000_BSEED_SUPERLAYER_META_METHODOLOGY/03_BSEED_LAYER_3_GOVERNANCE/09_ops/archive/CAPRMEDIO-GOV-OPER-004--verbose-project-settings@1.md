---
artifact_subtype: test_result
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: evidence_for
    targets:
      - CAPRMEDIO-GOV-EVAL-026--verbose-project-settings-test-case
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-395--verbose-project-settings
---

# Test result — Verbose project settings

## Subject and intended use

Implementation commits `ecfc9cd8957439a6a1cee3167f2cc2e5c48ef045` and
`ac5a0b7b4ec5707fcdcc5f75bd984ef88bc44387` for Requirement
`CAPRMEDIO-GOV-REQU-395--verbose-project-settings` and deterministic Test `CAPRMEDIO-GOV-EVAL-026--verbose-project-settings-test-case`.

This record supports the canonical `caprmedio_settings.toml` cut only. It does not
claim that every preserved historical YAML or JSON artifact has been migrated
to TOML, nor does it satisfy qualitative Evaluation
`CAPRMEDIO-GOV-EVAL-014--verbose-project-settings-evaluation-case`.

## Observed result

The repository and generated adopter fixtures emit a documented
`caprmedio_settings.toml`. The runtime reads the legacy `dset.toml` name only as a
migration input, rejects ambiguous dual-file roots, validates unknown settings
fail-closed, and exposes the selected naming, creation, implementation,
workspace, delegation, and priority behavior.

Project identity, topology, runtime risk, durability, external contracts,
release targets, verification commands, and commit-provenance boundaries
remain project-manifest facts. The Change workspace and delegation-budget
defaults now live only in project settings.

## Commands and results

```text
python -m unittest discover -s tests -q
  266 tests passed in 79.244s

ruff check dset_toolchain tests
  passed with Ruff 0.15.21

mypy dset_toolchain tests
  passed with mypy 2.3.0

python -m dset_toolchain check .
  DSET validation passed

git diff --check
  passed
```

The checks used the repository's installed environment with Python 3.14.3.
The locked `uv` wrapper was unavailable because the external package-index
tunnel failed before dependency resolution; no product assertion depends on
that environmental failure.

## Reopen conditions

Reopen this evidence when the settings filename, schema, defaults, accepted
values, compatibility policy, manifest/settings ownership boundary,
bootstrap output, or cited implementation commit changes.
