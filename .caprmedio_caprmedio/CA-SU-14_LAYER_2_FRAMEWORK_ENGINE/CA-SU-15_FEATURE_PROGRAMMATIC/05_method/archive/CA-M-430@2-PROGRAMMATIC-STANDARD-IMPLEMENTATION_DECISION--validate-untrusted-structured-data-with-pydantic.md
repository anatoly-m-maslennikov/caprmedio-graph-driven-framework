---
atom_id: CA-M-430@2
content_role: Method
type: Implementation Decision
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
subjects:
  governs: Subject/Engineering/Structured Input Validation
  depends_on:
  - Subject/Engineering/Interface Design
version: 2
updated_at: 2026-10-22 16:26:49 +0000
cce_version: cce_1
cce_form: method
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-415
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Validate untrusted structured data with Pydantic

use Pydantic **when** untrusted structured data crosses an admitted Python
boundary. validate once at the boundary **and** pass accepted typed values into
the deterministic core **without** making Pydantic the universal internal model.

## Details

Candidate source: [CA-M-286@8](archive/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic@8.md)

## Applicable when

apply **to** an admitted CLI payload, Hook event, configuration carrier, Journal
record, protocol message, **or** external adapter whose invalid structure could
hide a contract defect.

## Procedure

1. define the bounded input model with field types **and** constraints **before**
   custom validators.
2. use strict validation **when** coercion could hide a defect; admit lax conversion
   **only** for a declared interoperability need **and** make it observable.
3. reject undeclared extra fields for closed machine contracts.
4. return structured validation diagnostics **and** pass the accepted typed value
   **to** the deterministic core.
5. add Pydantic as a runtime dependency **only** **where** validation **and** schema value
   justify its dependency cost.

## Outcome

untrusted structured inputs become explicit typed values at one boundary while
the internal model remains independent of the validation library.

## Failure or stop

stop admission **when** the boundary is **not** declared, coercion is silent, extra
fields escape a closed contract, **or** the dependency has no bounded benefit.

## Sources

- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/concepts/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
