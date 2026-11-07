---
atom_id: CA-R-2508
ref_id: CA-R-2508@9-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 3
status: Draft
version: 9
updated_at: "2026-11-07 14:23:30 +0400"
carrier_destination:
  file:
    name: CA-R-2508@9-draft-CORE_META_MODEL-DECLARATION--declare-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
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

Atom//$atom {::0+}((CONTRIBUTES_TO));

UNIQUE(Atom//$atom, (.Header.ID, .Header.Version));
```

## Semantics

An Atom is the smallest independently governed Object.
