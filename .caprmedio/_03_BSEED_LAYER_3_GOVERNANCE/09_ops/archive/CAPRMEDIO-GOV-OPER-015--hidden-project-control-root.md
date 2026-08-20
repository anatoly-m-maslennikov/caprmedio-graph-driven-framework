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
      - CAPRMEDIO-GOV-EVAL-035--hidden-project-control-root-test-case
---

# Test result — hidden project-control root

Commit `fa07cd2ecef6b93474a9b7f0909a9e74f8adc56a` implements schema 1.3
with one canonical control root, `.caprmedio/`. Persisted control paths are relative
to the repository root and therefore begin with `.caprmedio/`; Markdown links may
remain relative to their containing file. Machine-local run, session, cache,
readiness, recovery, and backup state is isolated under ignored
`.caprmedio/runtime/`.

The complete deterministic verifier passed:

- 323 unit and integration Tests;
- Ruff format check across 90 files and Ruff lint;
- strict mypy across 89 source files;
- recursive `dset check` with fresh compilation, traceability, health, and
  bootstrap outputs;
- `git diff --check`.

The suite includes current-layout initialization and discovery, schema 1.2 and
legacy compatibility reads, deterministic schema 1.3 migration, carrier
relocation-chain validation, runtime isolation, generated-adopter validation,
and recursive self-hosting. `CAPRMEDIO-GOV-EVAL-017--hidden-layout-interpretability` remains a separate
qualitative Evaluation and is not claimed by this Test result.


## Historical frontmatter metadata

```yaml
schema_version: "1.0"
context:
  - "candidate_commit=fa07cd2ecef6b93474a9b7f0909a9e74f8adc56a"
  - "platform=macos"
  - "python=3.14.6"
  - "tests=323"
  - "ruff_files=90"
  - "mypy_files=89"
  - "schema=1.3"
observed_at: "2026-07-22T07:16:45+04:00"
polarity: "supports"
currentness: "current"
reopen_when: "The .caprmedio layout, repository-root-relative path rule, runtime-state boundary, compatibility reader, migration script, bootstrap bundle, or configured verification commands change."
subject:
  id: "CAPRMEDIO-GOV-EVAL-035--hidden-project-control-root-test-case"
  revision: "fa07cd2ecef6b93474a9b7f0909a9e74f8adc56a"
  intended_use: "Verify the hidden project-control root, canonical persisted-path base, ignored runtime boundary, migration behavior, and compatibility reads at one exact implementation commit."
producer:
  identity: "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
  performed_work: "Migrated current DSET control state to .caprmedio, made persisted control paths repository-root-relative, isolated runtime state under ignored .caprmedio/runtime, retained bounded schema 1.2 and legacy readers, added a schema 1.3 migration, rebuilt the bootstrap bundle, and executed the complete configured local verifier."
method:
  description: "Ran the complete unit suite, Ruff formatting and lint checks, strict mypy, recursive DSET validation, compilation, traceability and health refreshes, and Git diff hygiene against the implementation candidate."
  setup: "Codex Desktop managed workspace on macOS; Python 3.14.6; repository virtual environment; branch dev."
```
