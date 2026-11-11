---
identity:
  atom_id: CA-R-2508
  ref_id: CA-R-2508
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Active
  version: 12
  updated_at: 2026-11-08 20:06:37 +0400
destination:
  file:
    name: CA-R-2508-CORE_META_MODEL-DECLARATION--declare-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Atom

## Claim

### Prose Claim

Each Atom instance has exactly one outgoing HAS_ACTIVE_SUBJECT link. Its target is the declared entity or instance resolved from Header.Topics.Main Subject. An unresolved Subject is a diagnostic.

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

Atom//$atom {::1}((HAS_ACTIVE_SUBJECT));

Atom//$atom {::0..1}((GOVERNS));

Atom//$atom {::0+}((CONTRIBUTES_TO));

Atom//$atom {::0+}((IS_REPLACEMENT_FOR));

UNIQUE(Atom//$atom, (.Header.Identity.ID, .Header.State.Version));
```

## Semantics

An Atom is the smallest independently governed Object.
