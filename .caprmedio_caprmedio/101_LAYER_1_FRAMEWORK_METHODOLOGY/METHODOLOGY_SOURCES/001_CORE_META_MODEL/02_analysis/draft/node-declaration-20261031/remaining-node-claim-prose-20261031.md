# Remaining Claim prose — latest 2026-11-01

8 Declaration Claims retain prose: 3 Primary and 5 Property. Node root and Journal Claims are formal-only. Semantics are excluded from this count. Moving constraints to their own Subjects preserves them even when the prose-Claim count grows. Excerpts are verbatim; CFEL blocks are omitted.

## Atom.Tier

[Declaration](../../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-tier.md)

> Goals whose active Subject resolves to the Project use Tier -1. Ordinary Scope Unit-owned non-Goal Atoms use Tier 0 or higher.

## Atom.Subjects.Passive

[Declaration](../../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-subjects-passive.md)

> Passive Subjects identify direct contextual dependencies.

Decision: retain direct contextual-dependency meaning in prose.

## Atom/(.Role := Requirement)/(.Form := Relation Definition).Content.notation_for_subject

[Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-relation-definition-notation-for-subject.md)

> When a short subject notation is admitted for the Relation, this Property is required.

Decision: retain this conditional requirement in prose for now.

## Project

[Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-project.md)

> A Project uses CAPRMEDIO's MODEL.

## Scope Unit.Path

[Declaration](../../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-path.md)

> The Path lists Scope Unit identities along the complete declared containment chain from the root to the addressed Scope Unit.

## Projection.Source.Atoms

[Declaration](../../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md)

> Each value is an Atom ID with an explicit Version.

## Event Record

[Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-event-record.md)

> An Event Record is immutable.

Decision: Event Record owns its immutability; Journal owns containment.

## MODEL

[Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-model.md)

> - A local MODEL inherits CAPRMEDIO's MODEL.
> - MODEL inheritance is distinct from Node narrowing.
> - Local overrides replace matching inherited rules in the local MODEL.
> - Local overrides preserve the base MODEL's rules.
> - Unmodified inherited Declarations are reused.

Decision: MODEL owns inheritance and override resolution; inherited-rule reuse is stated once here.
