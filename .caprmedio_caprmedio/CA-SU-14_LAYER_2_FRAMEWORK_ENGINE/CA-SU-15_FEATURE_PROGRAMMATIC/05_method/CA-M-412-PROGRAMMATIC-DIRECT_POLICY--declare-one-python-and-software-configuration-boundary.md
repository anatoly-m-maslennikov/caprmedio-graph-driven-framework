---
identity:
  atom_id: CA-M-412
  ref_id: CA-M-412
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Configuration
    dependencies:
    - MODEL//CAPRMEDIO <+ Asset
  tier: 4
relations:
  child_of:
  - CA-M-415
  DERIVED_FROM:
  - CA-A-053
state:
  status: Active
  version: 13
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-412-PROGRAMMATIC-DIRECT_POLICY--declare-one-python-and-software-configuration-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Declare one Python and software configuration boundary

## Claim



### Prose Claim
select the stable CPython `3.14.*` series **and** require one project-owned
technical configuration boundary for interpreter, formatting, linting, typing,
evaluation, **and** packaging. CA-D-250 owns the current carrier placement **and**
encoding **in** the root `pyproject.toml`; configuration **and** Implementation
materialize this Method's selections there. keep that technical configuration
separate from CAPRMEDIO project settings.

## Details

### Scope

apply **when** Python source **or** a development workflow depends on an interpreter,
dependency, formatter, linter, type checker, evaluator, **or** packager setting.


#### Procedure
1. resolve the current Delivery carrier, **then** materialize the selected
   interpreter series **and** admitted development-tool profiles through that
   boundary.
2. keep one value for **every** setting **and** make local **and** automated workflows read
   that value rather than reproduce it.
3. change the interpreter series **or** a selected tool profile **only** through its
   accepted Method **before** changing configuration.
4. verify the selected stable series **before** using version-specific behavior.
5. keep runtime project settings outside `pyproject.toml` **and** expose them **only**
   through the shared Settings Reader.

#### Outcome

this Method owns one set of Python workflow selections; Delivery owns its
carrier, **and** configuration **and** Implementation reproduce the selections **without**
becoming another methodological authority.

#### Failure or stop

stop **when** two carriers disagree, a moving `latest` label replaces the selected
series, the materialization conflicts with its Delivery, **or** technical **and**
CAPRMEDIO project settings are mixed.

#### Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-A-054 — Validate the Python 3.14 contract upgrade](../02_analysis_and_advisory/CA-A-054-PROGRAMMATIC-ANALYSIS_RPRT--validate-the-python-3-14-contract-upgrade.md)
