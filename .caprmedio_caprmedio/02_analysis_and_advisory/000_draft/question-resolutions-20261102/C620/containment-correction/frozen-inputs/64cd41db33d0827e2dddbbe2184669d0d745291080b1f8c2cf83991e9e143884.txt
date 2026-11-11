---
subjects:
  active: Atom.Content
  passive:
  - Term
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Operations)/(.Type: Workflow) {1+}<+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Operations)/(.Type: Step)'
  - Atom
  - Actor
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Operations)/(.Type: Action)'
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Operations)/(.Type: Workflow)'
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-113
atom_id: CA-M-444
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Method
form: Implementation Method
---
## Summary

Atom Claims expose their meaning, conditions and consequences clearly.

## Claim scope

Atom Claims.

## Claim

**to** make an Atom Claim easy **to** understand, the Author **must** express **and** organize its content so the intended reader can identify what is claimed, what it concerns, **and** how its conditions **and** consequences fit together **without** guessing unstated connections.

## Details

### Meaning and context

- provide the context needed **to** interpret the Claim. reference existing governing definitions **and** authority rather than independently restating them.
- mention another Atom **in** prose **only when** an appropriate typed relation connects the Atoms. keep necessary execution bindings explicit; remove redundant context rather than invent a relation merely **to** retain a citation.
- render **every** prose Atom citation as the referenced Atom's complete filename **without** its `.md` extension **or** directory path, preserving **all** filename tokens **and** their exact spelling. direct machine references remain exact Atom IDs rather than citation labels, **and** the exact-revision reference rule continues **to** govern exact-revision metadata.
- choose familiar wording under the simpler-wording Method **without** losing precision, necessary distinctions, **or** exact canonical Terms.
- state conditions, alternatives, **and** relationships explicitly. preserve whether **all** conditions apply **or** **any** alternative suffices, including nested logical groups.

### Structure

- use short, direct statements. a simple Claim **may** remain a short paragraph; do **not** compress several points, conditions, **or** steps into one dense sentence.
- **when** several points share a subject **or** predicate, state that shared lead-in once **and** put the points **in** a list. preserve conjunctions, alternatives, conditions, **and** negation.
- use bullets for unordered points, conditions, **or** alternatives.
- use a numbered list for sequential steps **only** **when** the content establishes that sequence. numbering **must not** invent execution order **or** priority.
- use a flow table for a Workflow with Conditional Step definitions. identify **every** Step, its leaf **`=1`** Action reference **or** Workflow call where permitted, **or** its containing substep structure, its parameter/input bindings **when** applicable, **and** the declared routing condition, selected next Step **or** terminal outcome under the Workflow definition.

### Preservation

- preserve the complete Claim **and** its qualifications; easier wording **or** layout **must not** change its meaning.
- retain the Atom boundary under the composite-Claim boundary rule. one Claim does **not** require one sentence; paragraphs, bullets, **and** table rows do **not** determine the number of independently governed Claims.
- express authoritative content once rather than repeating the same Claim **in** prose **and** a list **or** table.
- apply the Term **and** CCE Operator rendering Method under the Term and operator rendering Method throughout.

readable layout alone is insufficient **when** the Claim still requires the reader **to** reconstruct missing context **or** logical connections.
