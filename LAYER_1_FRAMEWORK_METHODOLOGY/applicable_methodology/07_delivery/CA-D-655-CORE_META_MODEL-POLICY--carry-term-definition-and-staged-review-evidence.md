---
atom_id: CA-D-655
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Method)/(.Header.Form: Term Definition)'
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-655-CORE_META_MODEL-POLICY--carry-term-definition-and-staged-review-evidence.md
  source_atom_id: CA-D-655
  source_atom_revision: 3
  source_sha256: e7ad4330af9abddec4bf26381d529ab6759d6e86c427f160c9f2d68919936d9a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry Term Definition and staged review evidence

## Claim

### Prose Claim


Content of M/Term Definition Atoms and evidence returned by their well-formedness and staged usage checks.


an M/Term Definition **must** carry its Term spelling **and** authoritative meaning **in** its registered Claim section, **and** its applicable meaning boundary **in** Claim scope **when** required by the existing applicability authority. carry supporting distinctions **and** examples **in** Semantics **or** Details **when** applicable under the registered body layout. a review result **must** identify the selected Term Definition Atom **and** revision, checked source boundary **and** coverage, checked stage, affected Atom **and** revision, exact field occurrence **and** relevant context, assessed condition **and** result, **and** any conflict **or** uncertainty. distinct results for definition well-formedness, meaning ownership, occurrence consistency **and** coverage **must not** be collapsed **into** an unqualified pass. this evidence **must not** require a dictionary Projection, lookup index, new storage format **or** synthetic graph entity.

## Details

Term Definition is the dedicated Method Type for lexical meaning; Entity Definition remains a Requirement Type for entity structure. The Method Type requires its own admitted Type declaration; CA-R-2468's Requirement Type declaration does not establish it. CA-M-439 explains how to write its content; Evaluation authority determines how to check well-formedness and usage consistency. Ordinary existing source carriers and ordinary review output carry the necessary content and evidence. This Policy governs their representation; it does not execute an Evaluation, create a Workflow, dispatch a Run, or manufacture validation evidence.

### Body and review representation

CA-D-479@25 supplies the current RMED body layout: sibling `## Summary` and `## Claim`, with optional `## Claim scope` before Claim and optional `## Semantics` and `## Details` afterward. CA-D-495 supplies applicability placement. This Policy does not introduce new mandatory headings, content fields, report carriers, file locations, schemas, generated dictionaries, or runtime publication.

The ordered usage-review stages identify logical fields: entity names, Claim, Claim scope, Semantics, Details, then remaining authored content. Carry the actual reviewed stage and boundary in the result. Where a logical field is absent or inapplicable, record that fact rather than invent content or silently claim full coverage. A later stage remains unreviewed until checked; an earlier pass is not an overall pass. Unknown or incomplete source coverage remains explicit uncertainty.

### Naming and evidence boundaries

`atom.id` and `projection.id` are distinct complete qualified property names with the same reusable Term `ID` and the property operator `.`. The qualification belongs to the complete property reference; the shared component is not a full-name collision. This does not introduce case-folding, a parser rule, duplicate terminal labels as complete unqualified names, or a rule making every composite expression one entity name.

ID means a unique identifier used to find an entity instance, applying to Continuant and Occurrent instances with uniqueness within matching prefix namespaces. Source examples are `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3`. Preserve the full source identifier, including prefix and any suffix. Identifier spelling alone does not decide whether those examples denote one entity, separate revisions, or separate instances; existing lifecycle authority remains separately applicable.

Term meaning comes from the single applicable dedicated Term Definition, not inferred agreement among Entity Definitions or spelling alone. A source-supported lexical Term target, such as `Term//ID`, is distinct from the property entities addressed by `atom.id` and `projection.id`. Its defining Claim can introduce the lexical target under the existing defining-Atom authority; parsing alone does not create or admit it. A review may identify missing or conflicting authority without fabricating a definition or waiving admission rules. Reusable Terms such as `Package` and `Unit` do not automatically create similarly named Subject Graph entities.

Rejecting a mandatory dictionary for these checks does not retire CA-M-114 or existing optional Terms Graph or Catalog capabilities. Representation rules and authoring instructions alone are not proof of runtime behavior, completed review, corrected naming conflicts, or a naming migration. No parser change or automatic code identifier, path, or quoted external source rewrite is authorized by this Policy.
