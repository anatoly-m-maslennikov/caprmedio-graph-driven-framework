---
atom_id: CA-M-423
ref_id: CA-M-423
role: Method
form: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Active
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring/Python Code
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring/Python Code
version: 9
updated_at: 2026-10-27 19:59:43 +0400
author: Anatoly Maslennikov
tier: 3
container:
  scope_unit: CA-SU-15
carrier_destination:
  file:
    name: CA-M-423-PROGRAMMATIC-ENG_POLICY--run-project-python-only-in-uv-managed-isolated-environments.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---
# Summary

run Project Python **only** in uv-managed isolated environments

## Scope

the interpreter and library environment used to execute, develop, evaluate, build, package, or otherwise run Project Python source.

## Claim

Project Python **must** execute **only** through a uv-managed isolated environment **and** **must not** use naked **or** system Python, **or** system-installed libraries.

## Details

Candidate source: [CA-M-358@2](archive/CA-M-358-PROGRAMMATIC-GENERAL--run-project-python-only-in-uv-managed-isolated-environments@2.md)

1. resolve the Project interpreter through `uv python` **and** materialize its declared dependencies through the Project `pyproject.toml` **and** `uv.lock`.
2. synchronize the isolated environment with `uv sync --locked` **before** governed execution **and** start Project Python with `uv run --locked` **or** another uv command that selects that same isolated environment. Child processes **may** reuse **only** the selected environment's interpreter.
3. reject unselected `python`, `python3`, `pip`, **or** `pip3` commands, `PYTHONPATH` injection, user-site packages, system site packages, **and** library resolution outside the uv-managed Project environment.
4. apply the same isolated-environment boundary to development, tests, host launchers, **and** installed Project Tools. Non-Python executables **and** installing uv itself do **not** create a system-Python fallback for Project source.
5. stop **when** uv cannot resolve the declared interpreter **or** locked environment. Do **not** substitute a system interpreter, ambient virtual environment, **or** globally installed library.

## Outcome

Project Python execution has one reproducible uv-managed interpreter and dependency boundary.

## Failure or stop

stop before execution when the command would use an ambient interpreter, an unlocked environment, or any system-installed Project library.
