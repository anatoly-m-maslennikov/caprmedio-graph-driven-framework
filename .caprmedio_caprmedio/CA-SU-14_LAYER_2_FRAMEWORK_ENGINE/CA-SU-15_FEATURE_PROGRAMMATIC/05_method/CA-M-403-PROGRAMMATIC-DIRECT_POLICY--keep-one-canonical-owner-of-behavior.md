---
identity:
  atom_id: CA-M-403
  ref_id: CA-M-403
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Component Structure
    dependencies: []
  tier: 1
state:
  status: Active
  version: 13
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-403-PROGRAMMATIC-DIRECT_POLICY--keep-one-canonical-owner-of-behavior.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-411
---

## Summary

Keep one canonical owner of behavior

## Claim

### Prose Claim

**To** expose a declared capability through different transports, adapters or storage backends, reuse its canonical behavioral owner rather than independently redefining its meaning.

## Details

### Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.


- Adapters translate supported requests and results; they do not invent domain decisions or hidden Workflow composition.
- Keep identity, lifecycle, semantic admission and sequencing with their declared owner.
- Replacing a transport or backend must not silently change the declared capability.


### Retained Requirement and Delivery locality

For each implemented R or D Atom, prefer concentrating its actual claim-specific implementation in one cohesive implementation module and as few code units as practical, ideally one. Preserve complete realization of the Claim and allow justified multi-module exceptions when forced concentration would harm correctness or cohesion. Many-to-many implementation relations remain valid.

#### Details

##### Scope

New or changed PROGRAMMATIC implementation of Requirement (R) and Delivery (D) Atoms, including descendant Scope Units.


- Apply the preference to actual implementation, not merely an owner label, trace link or facade over dispersed logic. Several Atoms may share one module or code unit; several code units within one module may realize one Atom.
- Use code units, such as functions or classes, at the stated implementation granularity; do not confuse them with governed Scope Units.
- For R, concentrate its claim-specific meaning, behavior or enforcement. For D, concentrate its representation, serialization, storage or placement logic. Implementation need not be executable code.
- Distinguish claim-specific realization from callers, dependencies, tests and other evidence. Their presence alone does not add a realizing module; a caller that performs part of the required enforcement does count.
- Preserve complete and truthful implementation relations. Leave unimplemented Atoms without invented implementation targets.
- When multiple modules are necessary, retain the required boundaries and state the concrete reason; do not duplicate logic, inflate a module or omit obligations merely to reduce the count.

This Method is an implementation-organization preference, not an absolute cardinality limit, new approval gate or test policy.
