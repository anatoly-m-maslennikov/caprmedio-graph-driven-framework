---
identity:
  atom_id: CA-M-526
  ref_id: CA-M-526@1
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
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
  status: archived
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-526@1-PROGRAMMATIC-DIRECT_POLICY--trace-rmed-obligations-to-their-implementation-owners.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/099_archived
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

Each source module that materially realizes an applicable active Requirement, Evaluation, Delivery or non-Policy Method (Solution or Decision) carries one header comment per implemented Atom before its first code. Each comment contains only the current Atom ID and Version. Use the file language's comment syntax, one Atom per line:

```text
# CA-R-123@1
# CA-M-456@2
# CA-D-789@3
```

These are syntax examples. Do not add role labels, prose, headings or an `implementation of` marker. Do not cite a coding Policy merely because it guided implementation, or an Atom merely imported, called, decorated or wrapped by the source. A narrower set may also appear before an identifiable owning unit when useful.

An owner materially implements the cited Claim. A caller, facade, dependency, test invocation, Relation or Projection alone does not establish ownership. A module may implement several Claims and a Claim may have several genuine owners. A test module owns an Evaluation only when it materially implements that check, fixture or verification behavior.

## Details

Resolve current applicable authority and the actual owner before writing a comment. Preserve independent implemented Claims and many-to-many realization; do not invent an owner or citation for a dynamically unresolved implementation. Derive consumer and call-site references mechanically for review instead of maintaining a second authored `applies` graph.

A missing or ambiguous source, unidentifiable owner, stale citation or malformed comment is a traceability gap. Preserve the source and report the gap instead of mass-editing excluded files. Comments identify where to inspect; they do not prove conformance, test success, release readiness or completion.
