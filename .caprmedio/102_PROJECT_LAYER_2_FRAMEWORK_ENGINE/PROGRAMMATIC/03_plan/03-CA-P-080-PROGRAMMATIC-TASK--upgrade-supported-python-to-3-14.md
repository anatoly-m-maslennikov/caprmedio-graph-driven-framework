---
cce_version: cce_1
cce_form: obligation
subjects:
  - python-runtime
  - programmatic-delivery
  - compatibility
version: 1
updated_at: 2026-08-23 16:33:00
autonomous_confidence_threshold: 98
---
# Upgrade supported Python to 3.14

WHEN the Operator accepts CPython 3.14 as the supported stable series, THE Assignee MUST replace the accepted CPython 3.12 technical selection with CPython `3.14.*`, align every current checked-in support carrier, and record exact-revision validation under a stable 3.14 release.

## Scope

`(Atom ID IN (CA-R-1047, CA-M-110, CA-E-250, CA-D-250) OR Path IN (pyproject.toml, .github/workflows/publish-release.yml))`

## Definition of Done

THE Task is NOT DONE IF (`pyproject.toml` does not select `==3.14.*` OR a current checked-in Python support carrier still selects 3.12 OR validation does not record the exact CPython 3.14 patch release, source frontier, commands, and outcomes OR validation writes Python cache files into governed source directories OR the default standard-library-first dependency boundary changes without separate authority OR completed CA-P-071 history is rewritten OR the Task claims that workflow configuration alone proves a successful hosted run).

## Details

Use the stable CPython 3.14 series rather than the moving phrase `latest stable`. Preserve the existing R/M/E/D ownership: `pyproject.toml` owns the selected technical value while CA-R-1047, CA-M-110, CA-E-250, and CA-D-250 govern its meaning, method, evaluation boundary, and delivery.

Update the configured workflow interpreter to 3.14, but distinguish the declared workflow boundary from hosted execution evidence. Validate the current Programmatic Python source and installed read-only Tool interfaces with the local stable 3.14 interpreter. Do not run the repository's suspended test suite as part of this Task.

## Source

- [Python 3.14.7](https://www.python.org/downloads/release/python-3147/), released 2026-08-05.
