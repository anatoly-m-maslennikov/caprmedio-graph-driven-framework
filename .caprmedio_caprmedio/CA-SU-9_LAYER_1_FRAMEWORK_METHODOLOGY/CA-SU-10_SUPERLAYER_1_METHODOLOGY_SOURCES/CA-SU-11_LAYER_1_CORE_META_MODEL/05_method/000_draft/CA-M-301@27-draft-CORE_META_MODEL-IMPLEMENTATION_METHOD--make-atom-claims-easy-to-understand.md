---
atom_id: CA-M-301@27-draft
ref_id: CA-M-301@27-draft
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: Entity/Object/Continuant/Governing Objects/Atom.Content
  dependencies:
  - Entity/Term
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow {1+}<+{1} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Actor
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
tier: 5
relations:
  child_of:
  - CA-M-113
status: Draft
version: 27
updated_at: 2026-10-30 06:13:15 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Make Atom Claims easy to understand

## Claim scope

Atom Claims.

## Claim

**to** make an Atom Claim easy **to** understand, the Author **must** express **and** organize its content so the intended reader can identify what is claimed, what it concerns, **and** how its conditions **and** consequences fit together **without** guessing unstated connections.

## Details

### Meaning and context

- provide the context needed **to** interpret the Claim. reference existing governing definitions **and** authority rather than independently restating them.
- render **every** prose Atom citation as the referenced Atom's complete filename **without** its `.md` extension **or** directory path, preserving **all** filename tokens **and** their exact spelling. direct machine references remain exact Atom IDs rather than citation labels, **and** `CA-R-366-CORE_META_MODEL-REQUIREMENT--reference-exact-atom-revisions-by-version-and-time` continues **to** govern exact-revision metadata.
- choose familiar wording under `CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning` **without** losing precision, necessary distinctions, **or** exact canonical Terms.
- state conditions, alternatives, **and** relationships explicitly. preserve whether **all** conditions apply **or** **any** alternative suffices, including nested logical groups.

### Structure

- use short, direct statements. a simple Claim **may** remain a short paragraph; do **not** compress several points, conditions, **or** steps into one dense sentence.
- use bullets for unordered points, conditions, **or** alternatives.
- use a numbered list for sequential steps **only** **when** the content establishes that sequence. numbering **must not** invent execution order **or** priority.
- use a flow table for a Workflow with Conditional Step definitions. identify **every** Step, its leaf **`=1`** Action reference **or** containing substep structure, its parameter/input bindings **when** applicable, **and** the declared routing condition, selected next Step **or** terminal outcome under `CA-R-1508-CORE_META_MODEL-DEFINITION--define-workflow`.

### Preservation

- preserve the complete Claim **and** its qualifications; easier wording **or** layout **must not** change its meaning.
- retain the Atom boundary under `CA-R-1270-CORE_META_MODEL-RULE--permit-one-composite-claim-as-one-authority-unit`. one Claim does **not** require one sentence; paragraphs, bullets, **and** table rows do **not** determine the number of independently governed Claims.
- express authoritative content once rather than repeating the same Claim **in** prose **and** a list **or** table.
- apply the Term **and** CCE Operator rendering Method under `CA-M-229-CORE_META_MODEL-METHOD--render-governed-terms-and-cce-operators-distinctly` throughout.

readable layout alone is insufficient **when** the Claim still requires the reader **to** reconstruct missing context **or** logical connections.

### Withdrawn preparation — live owner replacement

This obsolete M301 preparation is excluded from the selected adoption set. M301 has no active Current predecessor; it is not restored by this Draft. The coordinated successor is [M444@2](CA-M-444@2-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly.md), prepared from live M444@1 and retaining that owner's identity, Summary and later authoring rules. This carrier is historical preparation only.
