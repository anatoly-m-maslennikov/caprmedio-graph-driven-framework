---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit.Parent
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - Subject/Graph/Rule
  - Subject/Graph/Rule.Applies To
  - Subject/Graph/Rule.Condition
version: 3
updated_at: 2026-10-24 01:44:12 +0400
relations:
  method_for:
  - CA-R-2124
  - CA-R-2125
  - CA-R-2130
  - CA-R-2131
  - CA-R-2132
  - CA-R-2149
atom_id: CA-M-438@3
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Archived
author: Anatoly Maslennikov
type: Eng Decision
---
# Summary

Derive Current RMED Atom Ordering Tier

## Scope

Current RMEDO Atoms and the stored governing relation occurrences that constrain their integer Tier.

## Claim

to derive one Current R/M/E/D Atom's integer Tier, the Author **must**:

1. resolve the complete Atom Claim, owner Scope Unit, and Scope Unit ancestry;
2. select only stored governing RMED relation occurrences under CA-R-2148. The source endpoint **must** be a Current R/M/E/D Atom, and the target endpoint **may** be any Current Atom permitted by that relation's endpoint definition;
3. preserve a valid existing integer Tier. Ordinary Project-owned Atoms use Tier **>=0**, ordinary non-Project Atoms use Tier **>=1**, and a verified Project Goal uses exactly Tier **-1**;
4. for each selected same-Scope occurrence, require the target Tier to be strictly lower than the source Tier; for a target in a strict ancestor Scope Unit, accept the occurrence without comparing Tiers;
5. treat descendant or sibling targets, unknown relation membership or endpoints, missing Tier/scope/parentage, derived inverse views, and cycles as unresolved failures rather than silently passing them. Where the approved ordering requires it and the owner range permits it, raise the source integer Tier until the same-Scope constraint holds.

Tier is a graph-ordering level only. It does not classify semantic abstraction, importance, Claim Scope breadth, Content Role, Type, Source ownership, filename, structural depth, or any named tier category.

