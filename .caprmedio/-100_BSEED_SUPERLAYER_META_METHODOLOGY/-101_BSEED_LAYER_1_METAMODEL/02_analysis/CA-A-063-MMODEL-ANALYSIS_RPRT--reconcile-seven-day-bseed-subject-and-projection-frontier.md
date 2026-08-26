---
atom_id: CA-A-063
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    continuant:
      - artifact-model
      - projection-generation
  prerequisite:
    continuant:
      - subject-temporal-form
      - bootstrap-authority
      - provenance
version: 1
updated_at: 2026-08-25 01:53:20 +0400
relations:
  analysis_of:
    - CA-C-106
---
# Reconcile the seven-day BSEED Subject and Projection frontier

## Conclusion

The accepted but unapplied BSEED frontier from the CAPRMEDIO discussion between 2026-08-18 and 2026-08-25 is limited to three connected bodies of work: qualified Subject and Subject Temporal Form authority remains in a connected draft dependency frontier; Realization Graph remains in fifteen draft Requirements; and Molecule remains discussion-only with no carrier. Other reviewed design lines are already represented by active authority, current drafts, or explicit CAP work and do not justify duplicate Atoms.

## Review boundary

This Analysis compares the latest operator decisions in the current task with the current working tree. Later operator input overrides earlier proposals. It distinguishes an accepted decision from an assistant suggestion, a future possibility, and an already governed claim. It does not promote, rewrite, or archive RMED authority.

| Discussion body | Current carrier state | Disposition |
|---|---|---|
| Intent, Principles, Actors, authority, bounded autonomy, and Operator control | Active Project authority and current CAP carriers exist | Do not duplicate |
| Scope Units, structural kinds, ordering, relations, Contracts, filenames, Types, Content Roles, and CCE | Active or draft BSEED carriers and broad reconciliation Tasks exist | Continue through CA-P-036 through CA-P-039 |
| Project Layers, settings, Extensions, Framework Engine, PROGRAMMATIC and AGENTIC boundaries | Active authority, current drafts, or explicit CAP work exists | Do not duplicate |
| Optional context, memory, Graph App, and host-plugin candidates | Current Analyses, Concerns, and Plans record their accepted or open dispositions | Do not duplicate |
| Qualified Subject and Subject Temporal Form | A connected METAMODEL, SEMANTICS, and GOVERNANCE draft dependency frontier exists | Freeze its exact dependency closure, then review and admit, revise, replace, or archive every selected carrier explicitly |
| Realization Graph | Fifteen METAMODEL, SEMANTICS, and GOVERNANCE Requirement drafts exist | Review and admit, revise, replace, or archive explicitly |
| Molecule | No current Atom, Journal, Projection, or CAP carrier defines it | Create atomic BSEED authority before implementation |

## Accepted Molecule model

A Molecule is a coherent subject-centered Projection compiled from multiple Atoms. Molecule is a Projection Type, not a fourth Artifact Form and not a synonym for every Projection.

Subject Temporal Form and source stance are independent axes. A Molecule has CONTINUANT or OCCURRENT Subject Temporal Form according to what its Subject is. Its to-be or as-is stance follows its source Content Roles: PRMED sources state accepted to-be authority, while Implementation and Ops sources represent realized or observed as-is material.

OCCURRENT does not imply historical observation and does not require a Journal. A Journal is a Molecule source only when the Projection explicitly needs governed history or provenance.

For example, a Molecule compiling the rules for authoring Atoms is CONTINUANT because its Subject is the rule structure. A Molecule compiling the prescribed process for creating or updating Atoms is OCCURRENT because its Subject is the process, even when that process is still to-be authority compiled from PRMED.

## Realization Graph boundary

The Realization Graph remains a generated Projection of native Realization rather than a source of project authority. Its recursive carrier or container face and its typed declaration, resource, and dependency face are Projection-internal structures, not Project Scope Units or governed Atom nodes. The graph is Evaluation input; static, pre-runtime-resolved, inferred-possible, and runtime-observed relations retain distinct evidence boundaries.

Legacy Realization may support discovery and draft proposals, but it cannot recover or establish intent without governed acceptance by the Operator. Pre-runtime analysis may resolve reflection, dependency injection, build transformation, configuration, plugin loading, routing, and similar behavior only to the extent that complete evidence permits; otherwise the result remains possible or unknown until runtime evidence exists.

## CAP disposition

CA-P-094 owns the exact materialization frontier identified here. It is a bounded input to CA-P-036, CA-P-037, CA-P-038, and CA-P-039; it does not replace their whole-Layer reconciliation and combined validation responsibilities.

## Reopening conditions

Reopen this Analysis if a later operator decision changes Molecule identity, makes Subject Temporal Form dependent on source stance, requires Journals for all OCCURRENT Projections, changes the Realization Graph authority boundary, or reveals another accepted decision from this seven-day task that lacks both a carrier and an explicit CAP disposition.
