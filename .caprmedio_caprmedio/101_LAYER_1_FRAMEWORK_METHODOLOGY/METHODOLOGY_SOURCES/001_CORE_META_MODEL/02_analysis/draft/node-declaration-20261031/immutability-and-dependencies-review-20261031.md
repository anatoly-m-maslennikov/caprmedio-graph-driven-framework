# Immutability and dependency patterns — 2026-10-31

The user settled Atom.ID immutability at first promotion to Current or Archived, with direct Draft to Archived permitted. The ID remains fixed across the same Atom's later versions, including Drafts.

IMMUTABLE(p) binds the first applicable scalar value and keeps the constraint active across later versions and false guards. Removing an optional Property after activation fails. Same-bearer lineage is explicit and independent of the mutable value, Version or Carrier. Atom.ID and admitted Event Record.ID are the first consumers. The existing field and uniqueness contracts remain intact.

DETERMINES expresses a dependency between key and dependent tuples over complete relevant historical states within one Project. ID determines Summary. Projection's Form/Named Selection/Source Of Truth tuple and its ID determine each other. Repeated equal states are allowed. References compare declared target identities, not physical addresses. Latest Projection.Form naming is retained; older Current Type names remain unchanged source evidence.

Both patterns and their consumers passed independent Terra review. Eleven immutability cases and the dependency truth table/reference-migration case were reviewed as model examples, not executable parser tests. Source snapshots preserve the edited consumer Drafts before conversion.

[Immutability review](declaration-expansion/immutability-review-20261031.json) · [Lifecycle examples](declaration-expansion/immutability-examples-20261031.json) · [Dependency review](declaration-expansion/functional-dependency-review-20261031.json) · [Dependency evidence](declaration-expansion/functional-dependency-evidence-20261031.json)

Prose count:23 to21. Atom.ID and Projection.ID are now formal-only. Summary retains its qualitative coverage requirement pending the authoring-Method decision. Primary Semantics remain unchanged.

Structural metadata, hashes and links pass for110 Drafts. The750 snapshotted Current Core Requirements and Current Epic38 remain unchanged. No allocation, promotion, parser, runtime, history provider or Workflow-instance implementation was performed. Historical lineage and semantic reference bindings remain adoption gates; a single current snapshot does not prove these invariants.
