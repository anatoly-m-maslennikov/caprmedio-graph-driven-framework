---
atom_id: CA-A-1231@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 23:44:40 +0400
relations: {}
tier: 3
---
# Summary

Split Subject Graph into four Projection Types

## Operator decision

Create separate Projection Types for:

1. Primary Subject entities/topics only.
2. A flat list of primary Subjects with at least one direct or inherited property, with their properties and inheritance marks.
3. Primary Subjects and all named instances, including Relation Type and Graph Rule declarations.
4. Subjects referenced by subjects.depends_on with no subjects.governs reference.

Every Type uses the same selection mechanism: declared Scope Units or Subject branches. Source Scope Unit selection and Subject branch selection remain distinct from the Projection Type.

## Proposed Type names

- Subject Graph Primary Subjects.
- Subject Graph Properties.
- Subject Graph Instances.
- Subject Graph Dependency-only Subjects.

Each Type has its own stable Projection ID under the existing identity policy. Sources retain versions in YAML; displayed definition references use bare Atom IDs. Reuse the same source-backed graph data rather than rebuilding four independent semantic models.

## Work

Prepare four R Definition Atoms, one shared selection Rule, and update the shared Subject Graph/Delivery contracts. The existing combined graph is a separate legacy Type, not one of the four focused Types. No Source remapping, new Scope Unit, Terms Graph, production Tool or runtime change is included.
