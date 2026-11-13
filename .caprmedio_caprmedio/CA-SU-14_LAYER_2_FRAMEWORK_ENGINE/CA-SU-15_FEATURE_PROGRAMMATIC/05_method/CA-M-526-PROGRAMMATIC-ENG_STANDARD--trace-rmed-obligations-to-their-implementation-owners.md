---
identity:
  atom_id: CA-M-526
  ref_id: CA-M-526
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Eng Standard
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Authoring <+ Code Authoring
    dependencies:
    - MODEL//CAPRMEDIO <+ Atom
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Requirement)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Method)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Evaluation)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Delivery)
  tier: 2
state:
  status: active
  version: 3
  updated_at: '2026-11-13T12:16:59.633843+00:00'
destination:
  file:
    name: CA-M-526-PROGRAMMATIC-ENG_STANDARD--trace-rmed-obligations-to-their-implementation-owners.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-2117
---
## Summary

Trace RMED obligations to their implementation owners

## Claim scope

The admitted PROGRAMMATIC implementation boundary, including descendant Tools, Apps, MCP components, workflows and their owning modules or units. Vendor code, generated output, frozen fixtures and legacy history are outside automatic editing unless explicitly admitted.

## Claim

### Prose Claim

Record implementation ownership with exact, versioned RMEDO Atom IDs. An owner materially implements the cited Claim in the existing implementation. Calling, importing, re-exporting, or applying a Claim as guidance does not make a module its implementation owner. A test module owns an Evaluation when it implements the check or its verification behavior.

Use one record per owner:

- Put Decisions, individual Requirements, and Test or Evaluation Cases in the spec reference of the Module that implements them.
- Record a directly implemented Solution in its owning Package’s spec reference. For other Claims that several Modules jointly implement, record the pin once in their smallest common owning Package. Distinct owners may each cite an Atom when each materially implements it. In the Workbench pilot, review Requirement-to-Module links for one-to-one, many-to-one and one-to-many ownership. Flag many-to-many groups for discussion.
- Record an Engineering Standard once at the Package where it is in use as a package-wide practice. Keep applicability separate from implementation ownership.

## Details

Resolve the actual Atom version and owner before recording a pin. Keep each pin in the form `CA-R-123@4`. Include RMEDO Atoms that have actual implementation owners. Report missing or ambiguous ownership and unresolved pins without guessing. Trace links identify where to inspect and do not establish conformance.

Use the Markdown spec reference format defined by the PROGRAMMATIC trace policy. During migration, a source header pin remains valid until its owning sidecar replaces it. Keep each migrated pin in one place.
