---
atom_id: CA-M-415@9
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Authoring/Code Authoring/Python Code
  depends_on:
  - Subject/Graph Node/Engineering/Technical Configuration Boundary
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
version: 9
updated_at: 2026-10-26 00:46:35 +0400
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-261
tier: 3
---
# Summary

Implement PROGRAMMATIC components in Python

## Scope

apply **when** a Tool, App backend service, **or** MCP component is added **or** materially
changed, **or** **when** its Python realization, runtime dependency, **or** non-Python
exception is proposed.

## Claim

use Python for applicable PROGRAMMATIC Tools, App backend services, **and** MCP
components. this Method owns the Python technology selection for that bounded
scope. Configuration **and** Implementation materialize the selected runtime,
dependencies, **and** exceptions; Delivery governs their carrier placement **and**
encoding; Operations defines reusable workflow behavior, **and** Journal Records carry execution evidence. this Method
does **not** govern Skills **or** make Python a discipline-independent CAPRMEDIO
meaning.

## Details

Candidate source: [CA-M-110@21](archive/CA-M-110-PROGRAMMATIC-GENERAL-IMPLEMENTATION_METHOD--implement-programmatic-components-in-python@21.md)

### Procedure
1. apply the Python selection established by this Method **and** read its current
   materialization **before** realizing a component.
2. use the standard library **when** it provides the required behavior with
   comparable clarity **and** reliability.
3. add **or** change a runtime, library, workflow tool, **or** non-Python exception
   **only** through an accepted Method that selects it for a bounded scope.
4. materialize **every** accepted selection **in** canonical configuration **and**
   Implementation **without** making either carrier a second authority.
5. place **and** encode **every** materialization through its Delivery, **and** preserve
   evidence of actual execution results **in** Journal Records.

### Outcome

**every** applicable component follows one Method-owned technology selection.
Configuration **and** Implementation reproduce it, Delivery locates its carriers,
**and** the Journal records execution evidence **without** taking over selection authority.

### Failure or stop

stop admission **or** release **when** no accepted Method owns a required selection,
its materialization disagrees with that Method, **or** the Delivery **or** Operations boundary
is absent. do **not** infer a platform-support claim from local execution.

### Sources

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
