# Plan blocking — atomic source proposal

The latest decision makes `IS_BLOCKED_BY` Direct from a dependent Plan to a prerequisite Plan and `BLOCKS` its Derived inverse. The proposed pair retains the existing Plan-to-Plan domain and the rule that the prerequisite must be Done before the dependent starts. Both Relation signatures use `Atom/(.Header.Role: Plan)//` and contain no cardinality or alias.

The packet now has five source proposals:

- A new unallocated `IS_BLOCKED_BY` Declaration and same-ID CA-R-1580 revision for Derived `BLOCKS`.
- A same-ID CA-R-2511 revision explicitly allowing zero or more outgoing `IS_BLOCKED_BY` and zero or more outgoing derived `BLOCKS` Relations between Plan instances. This permits multiple prerequisites without requiring any; it does not create facts.
- A same-ID CA-D-471 revision proposing direct encoding on the dependent Plan as a unique sequence of prerequisite Plan IDs under `relations.IS_BLOCKED_BY`. The derived view is not stored. This proposal states the key, value type, uniqueness and reference target; validate its admission and encoding against the dynamic Relation Header and CA-D-657 before use.
- A same-ID CA-M-306 refinement using the admitted Plan Role target and authored direct blocking direction. It retains work/decomposition, applicable Scope and completion rules, containment distinction, source-based confidence handling, and Summary stability. It removes stale Author, Assignee, Claim Target Scope Unit and Plan retry Property enumeration rather than declaring new Properties. Its confidence wording preserves the separately prepared safe WIP intent; the final owner must reconcile any further concurrent CA-M-306 proposal before application.

All four revised Current sources retain their IDs, Versions in preview and Summaries; final versioning and exact predecessor archives belong to the adoption workflow. The new relation ID remains unallocated. `manifest.json` pins all five candidate files, their exact Current sources, the combined method WIP and applicable authority sources. The selected source pins matched when this packet was checked.

CA-E-504, CA-E-404, CA-E-622, CA-M-239 and CA-R-1592 may continue to reason about the logical `BLOCKS` view; audit any actual authoring or stored-fact assumption before changing them. Preserve the separation from Subject DEPENDS_ON. Do not rewrite frozen version-qualified evidence.

**Migration remains a separate CA #3 obligation.** Existing `relations.blocks` facts are stored on prerequisite Plans. The proposed direct facts must be represented on dependent Plans without losing targets, direction, history or collisions. Source adoption alone does not migrate data, code, fixtures or tests. Validate schema admission, the exact carrier encoding, reader/writer behavior, compatibility boundaries and data conversion as part of that separately owned work. No runtime support or actual Plan instance is asserted here.

Recheck source, combined WIP and preview hashes under the authorized lock; allocate the new ID, archive exact predecessors, validate the selected MODEL and apply a single combined successor per source. YAML, pinned bytes, preserved same-ID Summary and full typed Relation selectors were checked. Integrated CFEL validation, migration and runtime tests were not performed. No Current source, code, test, Git state or actual Plan instance changed.
