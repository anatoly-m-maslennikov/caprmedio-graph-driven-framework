---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Subject", "Subject Path", "Subject Target", "GOVERNS", "DEPENDS_ON", "Entity", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Term", "Entity/Node/Continuant/Projection/Type: Atom Subjects Graph", "Entity/Node/Continuant/Atom/Content Role: Concern", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom/Content Role: Evaluation", "Evaluation For Relation", "Property", "Primary Entity", "Dependent Entity", "Entity/Node/Continuant/Scope Unit", "Atom Scope", "Entity/Node/Continuant/Atom.Target Scope Unit", "Entity/Node/Continuant/Atom.Summary"]
version: 30
updated_at: "2026-10-21 01:47:52 +0400"
relations:
  evaluation_for:
    - CA-R-1275
    - CA-R-1279
    - CA-M-125
    - CA-R-1018
    - CA-R-1248
    - CA-R-1194
    - CA-R-2003
    - CA-R-1193
    - CA-R-1201
    - CA-R-1202
    - CA-R-1452
    - CA-R-1508
    - CA-R-1597
    - CA-R-1014
    - CA-D-269
    - CA-M-301
    - CA-R-1318
    - CA-R-1341
atom_id: "CA-E-246@30"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Archived"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary

Validate Atom Subjects

## Scope

Subject Relations of an Atom evaluated against its complete Markdown Main Content.

## Claim

**every** valid Atom has **`=1`** GOVERNS Subject Target matching its Claim **and** DEPENDS_ON for **every** other Subject Target independently mentioned **in** its complete Markdown Main Content; an Atom citation label is **not** a Subject Target mention **or** Subject target, and the distinct target set **`=`** that mention inventory **without** an intermediate Subject object.

## Details

### Test case

create valid flat Carrier fixtures with **`=1`** scalar GOVERNS target, **`>=0`** distinct scalar DEPENDS_ON targets, Entity targets including an Action Atom **and** a Workflow Atom, a qualified Subject Path, and a definition Claim. reuse the same Entity target, including an Action **or** Workflow Atom, from different Atoms: those Atoms have distinct Subject Relations **to** the same target **without** duplicating its definition **or** identity. distinguish a reusable Action **or** Workflow definition from a particular execution **and** its Journal Records.

add a Method-root fixture `Method/Decomposition` whose exact path is admitted by an accepted source Method Atom's direct GOVERNS relation and whose Substance or Semantics establishes its meaning. a valid Atom may GOVERNS that Method Topic and DEPENDS_ON an Entity target, or the reverse. reject a Method Topic admitted only by a Scope Unit, folder, language name, or carrier path. reject treating it as an Entity Object or requiring a separate Definition Atom for its component Terms.

introduce **in** the source Subjects encoding zero **or** multiple GOVERNS targets, an unresolved **or** ambiguous target, a nested Subject/Entity **or** Subject/Reference wrapper, a repeated source target-kind field, a stored copy of a target definition, a duplicate dependency, a missing mentioned Subject Target, an invalid qualified path, a Term's spelling used **without** its canonical target, and a separate Entity identity invented for an existing Action **or** Workflow Atom. a definition whose GOVERNS reference identifies the wrong target or omits its defined terminal Term **must** fail. add `Atom/Content Role: Requirement/Type: Demand` as **`=1`** target path composed of **`=5`** Term references: `Atom`, `Content Role`, `Requirement`, `Type`, and `Demand`. its source Atom has **`=1`** GOVERNS Subject Relation **to** that target, **not** five Subjects. reject confusing the Relation with its target or treating the referencing Atom as defining **all** five Terms.

add conformance-check Evaluation fixtures whose direct GOVERNS Subject Relations identify the checked targets and whose `evaluation_for` relations separately identify the checked authority under `CA-R-1018-CORE_META_MODEL-CORE--register-evaluation-targets`. reject a generic Evaluation label or check execution substituted for the checked target and a missing or invalid `evaluation_for` target. reject treating an Atom's Subject DEPENDS_ON reference or dependency-list position as Workflow execution order; preserve the separately governed Plan `BLOCKS` completion gate.

accept an unmigrated legacy temporal Carrier only under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`'s migration-limited compatibility and confirm that its decoded direct references preserve the same targets and relation meanings. do **not** require temporal nesting on a migrated flat Carrier. a Projection **may** derive a target's kind from canonical authority **when** its own Spec calls for it; reject independent classification authority or a requirement **to** repeat that kind **in** source Subjects metadata. reject independent reauthoring of either a referenced definition or a projected relation fact.

an Action or Workflow Atom is a valid Entity target under its existing Atom identity. reject excluding it merely because it has Type Action or Workflow. being an Atom and an Entity is **not** duplicate identity.

include a Property borne by a Primary Entity and a Property borne by a Dependent Entity, retaining **`=1`** immediate bearer **in** either case. reference the narrowest exact Entity for both GOVERNS and DEPENDS_ON; a broader bearer is invalid **when** the Claim actually concerns its qualified Dependent Entity. entry or exit criteria use this same target rule. do **not** invent a separate criterion Entity **without** governing authority.

give two Atoms the same Subject target but different owning Scope Units and different permitted explicit Claim Target Scope Units. preserve their independent ownership and targeting; reject deriving either Scope Unit from the Subject Path. preserve RMED applicability **in** its registered Scope body section, read together with Claim and Details, **not** a duplicate frontmatter scope field. this check does **not** remove the Governed Subject contribution **to** contextual Atom Scope under `CA-R-1014-CORE_META_MODEL-CORE-REQUIREMENT--resolve-atom-scope-contextually`.

include Subject Targets mentioned **only** **in** Summary, Scope, Details, a nested heading, a table, or an example. missing **any** such target fails coverage. include a valid citation-only label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension or directory path, for example `CA-R-366-CORE_META_MODEL-REQUIREMENT--reference-exact-atom-revisions-by-version-and-time`; it requires no Subject target for the cited Atom or any Subject Target named only inside that label. **in** a companion fixture, place the same citation label **in** a sentence that independently uses a Subject Target: require the direct Subject target while still excluding the citation label itself. reject an unrelated extra target and a GOVERNS target repeated **in** DEPENDS_ON. an independently mentioned bearer requires its own reference; a bearer occurring only as an implicit qualified-path prefix does **not**. retain an unresolved mention as blocked evidence rather than silently removing it.

include `Term` used **in** its own definition and `Evaluation` used **in** an Evaluation Atom. recognize these as Terms under `CA-R-1318-CORE_META_MODEL-CORE--define-term` and `CA-R-1341-CORE_META_MODEL-CORE--define-evaluation-content-role`; resolve the referenced Subject Target from its definition and usage context. reject omitting a mentioned Subject Target solely because the wording is self-referential, inventing a separate Entity from the Term's spelling, or adding a duplicate DEPENDS_ON target for a target already referenced by GOVERNS. keep unresolved Subject Target meaning blocked; recognizing a Term alone does **not** prove an exact Subject target.

### Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the affected Atom, direct Relation Kind, Subject Path, canonical Subject Target, representation, or cardinality rule. the Atom Subjects Graph reproduces exactly the selected direct references **without** another authoritative relation fact or Subject identity.

### Failure disposition

record a Concern naming **every** affected Atom and direct Subject reference.
