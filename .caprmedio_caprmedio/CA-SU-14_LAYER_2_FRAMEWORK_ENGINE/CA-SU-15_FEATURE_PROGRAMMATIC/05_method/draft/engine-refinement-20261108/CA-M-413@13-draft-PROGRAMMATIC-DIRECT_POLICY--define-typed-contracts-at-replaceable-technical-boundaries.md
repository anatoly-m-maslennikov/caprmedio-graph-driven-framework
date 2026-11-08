---
identity:
  atom_id: CA-M-413
  ref_id: CA-M-413@13-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  tier: 4
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-415
state:
  status: Draft
  version: 13
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-M-413@13-draft-PROGRAMMATIC-DIRECT_POLICY--define-typed-contracts-at-replaceable-technical-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/draft/engine-refinement-20261108
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---
# Summary

Define typed contracts at replaceable technical boundaries

declare an explicit typed contract wherever a PROGRAMMATIC component depends on
a replaceable technical implementation, adapter, transport, storage mechanism,
**or** host boundary.

When the boundary carries user-edited or externally applied mutable state, the contract must distinguish a user's requested change, the applied external state and the acknowledged state, including whether a value is unsaved or synced. At a paged or shared-result boundary, it must identify one owner and one snapshot for rows, page counts, complete or source counts, filters, sort order and values, including null, Unicode and hidden values. Delayed or reordered acknowledgements from two clients must not mix snapshots or let one client overwrite the other.

## Details

Candidate source: [CA-M-159@9](archive/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries@9.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component can substitute one
technical implementation for another **or** crosses a host-owned interface.

## Procedure

1. define the accepted inputs, outcomes, failure values, ownership boundary,
   **and** compatibility expectation at the interface. When the boundary carries
   user-edited or externally applied mutable state, state how requested,
   applied and acknowledged changes differ, and whether each value is unsaved
   or synced.
2. keep callers dependent on that contract rather than on implementation-only
   state **or** incidental representation. For paged data, keep rows, counts,
   filters and sort results tied to one owner and snapshot so delayed or
   reordered client acknowledgements cannot combine generations.
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
