---
atom_id: CA-R-2508
ref_id: CA-R-2508
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 3
status: Active
version: 8
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2508-DECLARATION--declare-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2508-CORE_META_MODEL-DECLARATION--declare-atom.md
  source_atom_id: CA-R-2508
  source_atom_revision: 8
  source_sha256: 0d30d5a01af09777d7cc465b66e15997783f41298d3e85376fa458897031a666
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom

## Claim

### Prose Claim

For each Atom instance, the outgoing HAS_ACTIVE_SUBJECT Relation has cardinality 0..1 and targets only the declared entity or instance resolved from its active Subject field. When the applicable Current-status rule requires that field, its resolved target supplies the one link; an unresolved field remains a diagnostic.

For each Atom instance, the outgoing GOVERNS Relation has cardinality 0..1 and targets only the canonical Subject the Atom governs through its applicable content. These are separate named outgoing permissions and do not grant an inverse or another Relation. The target-omitted bounds count each Atom’s outgoing links within each Relation Declaration’s admissible endpoint domain; they do not create links.

Each Atom instance's outgoing IS_CONTAINED_BY Relation targets the Atom instance or Scope Unit instance selected by its Header.Container.

### Formal Claim

```CFEL
# model
Atom;

Atom.*[string,in(Header,Content)]{::2};

Atom ((NARROWER_THAN)) Continuant;

# instances
Atom//$atom {::1}((IS_CONTAINED_BY));

Atom//$atom {::0..1}((HAS_ACTIVE_SUBJECT));

Atom//$atom {::0..1}((GOVERNS));

UNIQUE(Atom//$atom, (.Header.ID, .Header.Version));
```

## Semantics

An Atom is the smallest independently governed Object.
