---
atom_id: CA-R-2508
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 6
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-04 11:00:07 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2508-CORE_META_MODEL-DECLARATION--declare-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom

## Claim

### Formal Claim

```CFEL
# model
Atom;

Atom.*[string,in(Header,Content)]{:2};

Atom ((NARROWER_THAN)) Continuant;

# instances
Atom//$atom {:1}((IS_CONTAINED_BY));

Atom//$atom {:0..1}((HAS_ACTIVE_SUBJECT));

Atom//$atom {:0..1}((GOVERNS));

UNIQUE(Atom//$atom, (.Header.ID, .Header.Version));
```

### Prose Claim

For each Atom instance, the outgoing HAS_ACTIVE_SUBJECT Relation has cardinality 0..1 and targets only the declared entity or instance resolved from its active Subject field. When the applicable Current-status rule requires that field, its resolved target supplies the one link; an unresolved field remains a diagnostic.

For each Atom instance, the outgoing GOVERNS Relation has cardinality 0..1 and targets only the canonical Subject the Atom governs through its applicable content. These are separate named outgoing permissions and do not grant an inverse or another Relation. The target-omitted bounds count each Atom’s outgoing links within each Relation Declaration’s admissible endpoint domain; they do not create links.

Each Atom instance's outgoing IS_CONTAINED_BY Relation targets the Atom instance or Scope Unit instance selected by its Header.Relations.IS_CONTAINED_BY.

## Semantics

An Atom is the smallest independently governed Object.
