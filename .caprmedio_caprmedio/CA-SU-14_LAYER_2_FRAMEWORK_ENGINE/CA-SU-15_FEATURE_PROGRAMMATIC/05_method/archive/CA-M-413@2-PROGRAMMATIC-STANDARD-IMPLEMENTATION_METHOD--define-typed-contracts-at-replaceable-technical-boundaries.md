---
atom_id: CA-M-413@2
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
subjects:
  governs: Subject/Engineering/Interface Design
  depends_on:
  - Subject/Engineering/Behavior Ownership
  - Subject/Engineering/Compatibility Boundary
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

Define typed contracts at replaceable technical boundaries

declare an explicit typed contract wherever a PROGRAMMATIC component depends on
a replaceable technical implementation, adapter, transport, storage mechanism,
**or** host boundary.

## Details

Candidate source: [CA-M-159@9](archive/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries@9.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component can substitute one
technical implementation for another **or** crosses a host-owned interface.

## Procedure

1. define the accepted inputs, outcomes, failure values, ownership boundary,
   **and** compatibility expectation at the interface.
2. keep callers dependent on that contract rather than on implementation-only
   state **or** incidental representation.
3. use a structural `Protocol` **when** consumers need one capability contract
   **without** requiring implementations **to** inherit from a framework base class.
4. keep substrate-specific behavior **in** a small adapter **and** keep deterministic
   semantic decisions outside that adapter.
5. record an exception **in** its bounded owner **when** a required external interface
   cannot meet the contract directly.

## Outcome

the component can replace the bounded technical implementation **without**
silently changing its callers' declared expectations.

## Failure or stop

stop substitution **or** host integration **when** the boundary has no explicit
contract, its failures cannot be represented, **or** compatibility cannot be
identified from current authority.

## Sources

- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
