---
atom_id: CA-M-229
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - python-technical-configuration
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 01:50:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Declare one Python and software configuration boundary

Select the stable CPython `3.14.*` series and one project-owned
`pyproject.toml` surface for interpreter, formatting, linting, typing,
evaluation, and packaging configuration. Keep this technical configuration
separate from CAPRMEDIO project settings.

## Applicable when

Apply when Python source or a development workflow depends on an interpreter,
dependency, formatter, linter, type checker, evaluator, or packager setting.

## Procedure

1. Materialize the selected interpreter series and admitted development-tool
   profiles in the root `pyproject.toml`.
2. Keep one value for each setting and make local and automated workflows read
   that value rather than reproduce it.
3. Change the interpreter series or a selected tool profile only through its
   accepted Method before changing configuration.
4. Verify the selected stable series before using version-specific behavior.
5. Keep runtime project settings outside `pyproject.toml` and expose them only
   through the shared Settings Reader.

## Outcome

One technical control surface materializes every accepted Python workflow
selection without becoming a second source of methodological authority.

## Failure or stop

Stop when two carriers disagree, a moving `latest` label replaces the selected
series, or technical and CAPRMEDIO project settings are mixed.

## Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-A-054 — Validate the Python 3.14 contract upgrade](../02_analysis/CA-A-054-PROGRAMMATIC-ANALYSIS_RPRT--validate-python-3-14-contract-upgrade.md)
