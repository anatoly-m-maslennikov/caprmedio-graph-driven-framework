---
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: "Draft"
subjects:
  governs: "Method/Source Unit Responsibility"
  depends_on:
    - "Method/Function Purity"
    - "Method/Source Check Adoption"
version: 1
updated_at: "2026-10-21 01:47:52 +0400"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Ratchet hand-authored Python source boundaries

**to** construct bounded hand-authored PROGRAMMATIC Python source, decompose code
by responsibility under CA-M-157, CA-M-158, **and** CA-M-160; choose smaller coherent
units **and** external data Carriers; **and** use measurements **to** guide the next
construction choice. CA-E-539 owns source-size, complexity, exception, **and**
ratchet acceptance policy.

## Details

Candidate source: [CA-M-162](../CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)

## Applicable when

apply **to** **every** new **or** materially changed hand-authored Python file **in** Tools, App
backend services, **or** MCP components. generated Runtime **and** Delivery outputs
are outside this source rule.

## Procedure

1. read the applicable Evaluation policy **and** changed-source measurements.
2. separate independently reusable responsibilities **and** move deterministic
   transformations outside effect **and** lifecycle owners.
3. extract related units into specifically named modules **when** that keeps
   dependencies **and** responsibility visible.
4. externalize large static mappings. use TOML by default, JSON for schemas
   **or** machine interchange, **and** YAML **only when** its distinct features are required.
5. submit the resulting source **and** any bounded exception rationale **to** the
   applicable Evaluation. use its result **to** choose the next decomposition.

## Outcome

changed source ratchets toward readable, bounded units **and** externalized static
data. construction choices remain traceable **to** responsibility boundaries
**and** the measurements supplied **to** CA-E-539.

## Failure or stop

return unresolved construction choices **when** the applicable Evaluation policy
**or** required measurement is unavailable. retain a separate responsibility **and**
needed recovery boundary **when** a proposed decomposition would obscure either.
acceptance **and** rejection follow CA-E-539.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
