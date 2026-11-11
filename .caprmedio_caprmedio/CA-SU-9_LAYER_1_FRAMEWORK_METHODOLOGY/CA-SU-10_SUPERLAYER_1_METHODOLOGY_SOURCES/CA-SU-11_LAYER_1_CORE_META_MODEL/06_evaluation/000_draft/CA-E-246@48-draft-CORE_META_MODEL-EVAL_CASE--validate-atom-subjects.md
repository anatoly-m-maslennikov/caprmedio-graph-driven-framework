---
atom_id: CA-E-246
ref_id: CA-E-246@48-draft
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role: Requirement)/(.Header.Context.Form: Demand)'
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role: Operations)/(.Header.Context.Form: Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role: Operations)/(.Header.Context.Form: Workflow)'
  - CAPRMEDIO_MODEL <+ Term
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Atom Subjects Graph)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//evaluation_for
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Node.**
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
tier: 6
relations:
  evaluation_for:
  - CA-R-1275
  - CA-R-1279
  - CA-M-125
  - CA-R-1018
  - CA-R-2462
  - CA-R-1194
  - CA-R-2003
  - CA-R-1193@23
  - CA-R-2100
  - CA-R-1202
  - CA-R-2467
  - CA-R-2464
  - CA-R-1597
  - CA-R-1014
  - CA-D-269
  - CA-M-444
  - CA-R-1318
  - CA-R-2514
status: Draft
version: 48
updated_at: 2026-11-04 18:25:15 +0400
carrier_destination:
  file:
    name: CA-E-246@48-draft-EVAL_CASE--validate-atom-subjects.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/000_draft
---
## Summary

Validate Atom Subjects

## Claim

### Prose Claim


Subject Relations of an Atom evaluated against its complete Markdown Main Content.


**every** valid Atom has zero **or** one GOVERNS Subject Target matching its Claim **and** DEPENDS_ON for **every** other Subject Target independently mentioned **in** its complete Markdown Main Content; an Atom citation label is **not** a Subject Target mention **or** Subject target, and the distinct target set **`=`** that mention inventory **without** an intermediate Subject object.

## Details

### Test case

create valid flat Carrier fixtures with zero **or** one scalar GOVERNS target and **`>=0`** distinct scalar DEPENDS_ON targets, Entity targets including an Action Atom **and** a Workflow Atom, a qualified Subject Path, and a definition Claim. reuse the same Entity target, including an Action **or** Workflow Atom, from different Atoms: those Atoms have distinct Subject Relations **to** the same target **without** duplicating its definition **or** identity. distinguish a reusable Action **or** Workflow definition from a particular execution **and** its Journal Records.

a Method Content Role Atom may GOVERNS a Domain, Engineering or Graph Subject and DEPENDS_ON a Subject in another branch; its Content Role does not select the Subject branch. reject a separate `Method` Subject root or admitting a method topic from its Scope Unit, folder, language name or Carrier path.

introduce **in** the source Subjects encoding multiple GOVERNS targets, an unresolved **or** ambiguous target, a nested Subject/Entity **or** Subject/Reference wrapper, a repeated source target-kind field, a stored copy of a target definition, a duplicate dependency, a missing mentioned Subject Target, an invalid qualified path, a Term's spelling used **without** its canonical target, and a separate Entity identity invented for an existing Action **or** Workflow Atom. a definition whose GOVERNS reference identifies the wrong target or omits its defined terminal Term **must** fail. add `Atom/(.Header.Role: Requirement)/(.Header.Form: Demand)` as **`=1`** complete target path. Its qualified Atom segment reuses **`=5`** Term references: `Atom`, `Content Role`, `Requirement`, `Type`, and `Demand`; the Entity-rooted prefix remains part of the complete expression. its source Atom has **`=1`** GOVERNS Subject Relation **to** that target, **not** one Subject per lexical component. reject confusing the Relation with its target or treating the referencing Atom as defining **all** referenced Terms.

add conformance-check Evaluation fixtures whose direct GOVERNS Subject Relations identify the checked targets and whose `evaluation_for` relations separately identify the checked authority under `CA-R-1018-CORE_META_MODEL--register-evaluation-targets`. reject a generic Evaluation label or check execution substituted for the checked target and a missing or invalid `evaluation_for` target. reject treating an Atom's Subject DEPENDS_ON reference or dependency-list position as Workflow execution order; preserve the separately governed Plan `BLOCKS` completion gate.

accept an unmigrated legacy temporal Carrier only under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`'s migration-limited compatibility and confirm that its decoded direct references preserve the same targets and relation meanings. do **not** require temporal nesting on a migrated flat Carrier. a Projection **may** derive a target's kind from canonical authority **when** its own Spec calls for it; reject independent classification authority or a requirement **to** repeat that kind **in** source Subjects metadata. reject independent reauthoring of either a referenced definition or a projected relation fact.

an Action or Workflow Atom is a valid Entity target under its existing Atom identity. reject excluding it merely because it has Type Action or Workflow. being an Atom and an Entity is **not** duplicate identity.

include a Property borne by a Primary Entity and a Property borne by a Property, retaining **`=1`** immediate bearer **in** either case. reference the narrowest exact Entity for both GOVERNS and DEPENDS_ON; a broader bearer is invalid **when** the Claim actually concerns its qualified Property. entry or exit criteria use this same target rule. do **not** invent a separate criterion Entity **without** governing authority.

give two Atoms the same Subject target but different owning Scope Units and different permitted explicit Claim Target Scope Units. preserve their independent ownership and targeting; reject deriving either Scope Unit from the Subject Path. preserve RMED applicability **in** its registered Scope body section, read together with Claim and Details, **not** a duplicate frontmatter scope field. this check does **not** remove the Governed Subject contribution **to** contextual Atom Scope under `CA-R-1014-CORE_META_MODEL-RULE--resolve-atom-scope-contextually`.

include Subject Targets mentioned **only** **in** Summary, Scope, Details, a nested heading, a table, or an example. missing **any** such target fails coverage. include a valid citation-only label rendered under `CA-M-444-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly` as the referenced Atom's complete filename **without** its `.md` extension or directory path, for example `CA-R-366-CORE_META_MODEL-REQUIREMENT--reference-exact-atom-revisions-by-version-and-time`; it requires no Subject target for the cited Atom or any Subject Target named only inside that label. **in** a companion fixture, place the same citation label **in** a sentence that independently uses a Subject Target: require the direct Subject target while still excluding the citation label itself. reject an unrelated extra target and a GOVERNS target repeated **in** DEPENDS_ON. an independently mentioned bearer requires its own reference; a bearer occurring only as an implicit qualified-path prefix does **not**. retain an unresolved mention as blocked evidence rather than silently removing it.

include `Term` used **in** its own definition and `Evaluation` used **in** an Evaluation Atom. recognize these as Terms under `CA-R-1318-CORE_META_MODEL-CORE--define-term` and `CA-R-2514-CORE_META_MODEL-CORE--define-evaluation-content-role`; resolve the referenced Subject Target from its definition and usage context. reject omitting a mentioned Subject Target solely because the wording is self-referential, inventing a separate Entity from the Term's spelling, or adding a duplicate DEPENDS_ON target for a target already referenced by GOVERNS. keep unresolved Subject Target meaning blocked; recognizing a Term alone does **not** prove an exact Subject target.

### Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the affected Atom, direct Relation Kind, Subject Path, canonical Subject Target, representation, or cardinality rule. the Atom Subjects Graph reproduces exactly the selected direct references **without** another authoritative relation fact or Subject identity.

### Failure disposition

record a Concern naming **every** affected Atom and direct Subject reference.
