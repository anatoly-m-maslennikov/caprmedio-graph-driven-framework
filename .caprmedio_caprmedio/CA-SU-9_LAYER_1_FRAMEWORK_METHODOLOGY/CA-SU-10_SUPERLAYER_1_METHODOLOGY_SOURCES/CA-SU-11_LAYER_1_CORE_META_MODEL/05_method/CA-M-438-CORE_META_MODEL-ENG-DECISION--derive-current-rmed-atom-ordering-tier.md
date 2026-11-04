---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
version: 18
updated_at: 2026-11-04 09:19:08 +0400
relations:
  method_for:
  - CA-R-2706
  - CA-R-2125
  - CA-R-2428
  - CA-R-2131
  - CA-R-2132
  - CA-R-2149
atom_id: CA-M-438
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 4
status: Active
role: Method
form: Eng Decision
---
## Summary

Derive Current RMED Atom Ordering Tier

## Claim

### Prose Claim


Current RMEDO Atoms and the stored governing relation occurrences that constrain their integer Tier.


to derive one Current R/M/E/D Atom's integer Tier, the Author **must**:

1. resolve the complete Atom Claim and applicable ordering context. For an ordinary endpoint resolve its Local Scope Unit; for an Atom of Form Goal whose active Subject resolves to the Project Scope Unit root, resolve that Project as the ordering context under CA-R-2149. Resolve declared ancestry for these contexts;
2. select only stored governing RMED relation occurrences under CA-R-2148@10. The source endpoint **must** be a Current R/M/E/D Atom, and the target endpoint **may** be any Current Atom permitted by that relation's endpoint definition;
3. preserve a valid existing integer Tier. Ordinary Scope Unit-owned Atoms use Tier **>=0** except any Atom of Form Goal whose active Subject resolves to the Project Scope Unit root; that exact predicate uses Tier **-1** regardless of Container or owner;
4. for each selected same-Scope occurrence, require the target Tier to be strictly lower than the source Tier, except that an admitted typed governing relation from a same-Scope Tier 0 Method, Evaluation, Delivery, or Operations Atom to a Tier 0 Requirement is allowed; for a target in a strict ancestor Scope Unit, accept the occurrence without comparing Tiers; for a source and target that resolve within the same Project to the Project Configuration source role and its Core Meta-Model prerequisite role declared by CA-R-1218@31, accept the occurrence without comparing Tiers;
5. treat every other descendant or sibling target, unknown relation membership or endpoints, missing Tier/scope/parentage, unresolved logical-role identity, unresolved Project correspondence, an unresolved CA-R-1218@31 prerequisite declaration, derived inverse views, and cycles as unresolved failures rather than silently passing them. Raise an ordinary Scope Unit-scoped source integer only when its applicable range permits it. A Project-root Goal is fixed at Tier -1 under CA-R-2132 and is not raised to satisfy an ordering edge.

Tier is a graph-ordering level only. It does not classify semantic abstraction, importance, Claim Scope breadth, Content Role, Type, Source ownership, filename, structural depth, or any named tier category.
