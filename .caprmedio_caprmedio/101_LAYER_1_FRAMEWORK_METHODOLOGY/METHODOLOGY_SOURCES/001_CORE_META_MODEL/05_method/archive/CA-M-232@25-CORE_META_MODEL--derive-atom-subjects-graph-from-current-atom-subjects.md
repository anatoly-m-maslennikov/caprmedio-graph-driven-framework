---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Subject Graph'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Atom Subjects Graph'
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
  - Subject
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Relation/Type: GOVERNS'
  - 'Subject/Graph Relation/Type: DEPENDS_ON'
version: 25
updated_at: 2026-10-26 05:29:36 +0400
relations: {}
atom_id: CA-M-232@25
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Implementation Method
---
# Summary

Derive Atom Subjects Graph from Current Atom Subjects

## Scope

Atom Subjects Graph derivation from current Atom Subjects.

## Claim

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Subject as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical Subject Target, Subject Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Subject object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. an Atom Subjects Graph may include Entity-root and Method-root Subject Targets. an Entities Graph view must include only Entity-root targets unless its own Spec explicitly admits a distinguishable external reference. an unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details

For the readable Subject Graph hierarchy under CA-R-2150:

1. Compose the selected Current source Subject paths mechanically. Preserve source spelling and provenance; do not invent Subjects from filenames, module names or Scope Unit names.
2. Render primary kinds first. Omit INSTANCE_OF paths and all their descendants from this first section. Dependent properties and their values appear in the second section, not the first tree.
3. In primary-tree order, render each primary with direct or inherited properties. Follow broader-to-narrower kind ancestry only for this inheritance; containment and Depends On do not imply it. Show inherited origins explicitly. Combine source-backed allowed-value additions without removing inherited values. Preserve equal-name origins and report conflicts rather than choosing an override.
4. Render named instances separately. Reuse selected named Subject instances, selected source-backed Relation Type declarations, and Current Requirement/Type Graph Rule declarations with their actual YAML `claim.*` mappings. Defining schemas and examples are not concrete Graph Rules. Do not substitute actual Atom-to-Atom Relation tuples for the requested Relation Type instances.
5. Use tabs for tree depth and local labels without repeated full paths. Preserve declared sibling order, otherwise use alphabetical order. Keep source limitations visible and retain the complete Current Atom ID/Version provenance.
