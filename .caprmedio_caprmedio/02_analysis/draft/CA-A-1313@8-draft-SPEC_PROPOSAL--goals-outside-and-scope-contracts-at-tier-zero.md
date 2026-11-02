---
atom_id: CA-A-1313@8-draft
content_role: Analysis
current_scope_unit: caprmedio
status: Draft
author: Anatoly Maslennikov
tier: 3
version: 8
updated_at: 2026-10-31 18:43:05 +0400
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
relations: {}
form: Spec Proposal
---
## Summary

Keep Goals outside and define Scope Contracts inside each Scope Unit

## Proposal

For each declared Scope Unit, keep exactly one Declaration and one or more separate Goal Atoms outside it. Keep its Scope Contract Atoms inside it, at Tier 0.

### Declaration outside

One Scope Unit Declaration is one artifact about the whole declared Scope Unit. It may contain multiple statements about its ID, Name, whether it is ordered or unordered, Label, Local Order and connections. Scope Constraints imposed on that Scope Unit are external and may be part of this Declaration. Do not create a separate Atom for each field or nuance.

The Declaration has Role = Requirement and Form = Scope Unit Declaration. This Form uses the Declaration template. Its statements may be prose, GFEL formal expressions or both. They belong to one coherent declaration. Its Form template may allow a topic Summary, such as “Declare Scope Unit”. Formal expressions must use admitted GFEL; this proposal does not invent another grammar.

Do not embed the Goal Claims in the Declaration. It may reference the separate Goal Atoms without maintaining copies of their Claims. Goal is not another field whose value duplicates a separate Goal.

“Outside” means outside the declared Scope Unit's ownership, not outside every Scope Unit or outside the repository. Ordinary external Goals keep their existing parent owner and child Target Scope Unit. The Project Goal keeps its established Operator Actor owner and Project target, at Tier -1. The Project Declaration is also outside the Project, like the Project Goal, following its external Operator ownership. This does not make the Operator a Scope Unit. No filesystem path is assigned by this decision; the earlier suggestion to keep the Declaration in the project root is not adopted.

### Declaration binding

A Scope Unit Declaration Atom has Role = Requirement and Form = Scope Unit Declaration. Its active Subject (`subjects.active`) identifies the specific Scope Unit instance being declared, not merely the generic Scope Unit kind. Count exactly one matching Declaration Atom per declared Scope Unit. Use this Subject binding; do not require a duplicate binding in Claim or Target Scope Unit. “Active” here names the Subject field, not an added Atom.Status predicate.

“Scope Unit Declaration” names the Declaration’s purpose/template here; it does not introduce a new Content Role outside RMEDO. Other requirements governing a Scope Unit do not become its Declaration simply by sharing that Subject.

### Goals outside

Each declared Scope Unit has one or more separate Goal Atoms stating what it should achieve. The latest correction explicitly supersedes including Goals in its Declaration. Do not merge these Goals into one required Goal or into a single Declaration Claim.

### Scope Contracts inside

Scope Contract Atoms are owned inside the governed Scope Unit and have numeric Tier 0. They state the unit's foundational responsibilities and commitments within its external Goal expectations and Scope Constraints. They may use RMEDO as applicable; no unit must populate all five Content Roles. Do not require exactly one Contract Atom or impose a minimum local Contract count. A Scope Unit may have no local Contract Atoms; this decision introduces no additional sufficiency test.

Scope Contract remains the optional readable Tier-0 label and SCOPE_CONTRACT filename token, not a new Form or Atom.Label. Other numeric Tiers are unchanged. A permitted typed same-Scope Tier-0 MEDO-to-R serving relation remains permitted; this amendment does not admit arbitrary equal-Tier or descendant-target governance.

No additional per-Scope-Unit Definition Atom is required. Shared structure and meaning belong once in the reusable Declaration model/template, not copied into every actual unit's Declaration. The structural declaration of the Scope Unit kind is distinct from the external Declaration of a particular Scope Unit; these are not two competing instance declarations.

### Governing source

Scope Unit Declarations are the proposed governing source for the structure currently represented by project_structure.toml. Do not independently maintain both as governing sources. A compatibility TOML representation may be derived if consumers need it.

This is a proposed authority migration, not permission to remove project_structure.toml now. Preserve every needed governed fact, update consumers and check source coverage before retiring its governing role. No TOML values, Current sources, runtime or code are changed by this Draft.

### Claim, Form and Operator wording

The default is one coherent Claim per Atom, with optional Semantics and Details. Summary faithfully condenses the whole Atom; for RMED it is normally a statement. A Form template may explicitly override these defaults. Declaration permits multiple prose/GFEL statements and may permit a topic Summary. Do not apply that exception to every Atom.

Keep the Operator's wording as close as possible. Correct grammar and organize it into coherent statements using the simplest syntax possible. Preserve terms and key concepts, including DRY and MECE. Do not replace clear wording with synonyms or polished paraphrases.

“Form” replaces the former content-template meaning of Type in this proposal. Drafts use the proposed form field; this does not claim that existing schemas or readers already admit it. The technical field migration needs its own adoption check.

## Superseded alternatives

The following earlier alternatives are not part of this amendment:

- Goals included in the Scope Unit Declaration.
- Exactly one Goal outside a Scope Unit.
- Exactly one Scope Contract inside a Scope Unit.
- A third per-unit Definition Atom in addition to its Declaration and Contracts.
- Declarations and project_structure.toml maintained as independent sources of truth.
- Topic-only Summaries allowed for all Forms.

Earlier adopted decisions remain historical until this amendment and its Drafts are reviewed and adopted. The completed content-only restoration of project Principles/Core is not undone by this proposal.

## Navigation Number

Scope Units do not have Navigation Number. Keep their existing Local Order semantics; do not maintain a duplicate navigation position. Navigation Number is retained only for Steps and P (Plan) Atoms. This decision does not add new numbering or Carrier-format rules for those Atoms.

## Adoption checks

Before TOML retirement, establish full coverage of its governed fields, the source-discovery entry point and the technical Form-field migration. These are adoption checks, not invented schema defaults or runtime work in this packet.

## Adoption boundary

This revision and its linked RMED Drafts are preparation only. Current methodology, existing historical Draft packets, governing TOML, Engine code/runtime and Projections are not promoted, rewritten or deleted by this packet. Older Scope Definition / Goal-retirement trial Drafts are superseded for this adoption and must not be promoted unchanged.


## Operator cardinality expression

The Operator supplied this corrected expression verbatim:

```
(Atom//.Role = Requirement & .Form = Scope Unit Declaration & .subjects.active = Scope Unit//){:1}
```

The intended count is one qualifying Declaration Atom per specific declared Scope Unit, not one across all Scope Units together. Role remains Requirement; Scope Unit Declaration is the Form. `subjects.active` is the Subject binding, not a lifecycle-status filter. The expression is recorded as supplied; no parser admission is claimed.

## Applicable Methodology boundary

Applicable Methodology is a special Projection, not a separately retained hosting Scope Unit. Withdraw that instance Declaration Draft and plan retirement of the APPLICABLE_METHODOLOGY Scope Unit during adoption. Do not create a separate Scope Unit Goal for it. Existing delivered Projection content and Carrier places are not deleted by this decision. Current structure remains unchanged in this preparation packet.
