# Projection identity packet

The user chose `(Form, Scope Unit)` as Projection identity in both directions. Source.Named Selection remains the source description and is not an identity component. Two selections for the same Form and Scope Unit therefore refer to the same Projection identity; a refresh or reconfiguration updates that Projection rather than allocating a second ID. Source.Atoms retains explicit Atom Versions when populated.

The packet proposes `Projection.Scope Unit` as a required dependent Property with exactly one Scope Unit instance reference. This uses the existing `Projection.Source.Named Selection` reference pattern. It intentionally does not infer a containment or inverse Relation. The reference is to Scope Unit identity, not its mutable name or path. Its Declaration has an unallocated placeholder ID: assign a canonical ID only during approved application.

The seven provisional Form values correspond one-to-one to the current Entity-related views CA-PROJ-020 through CA-PROJ-026. Catalog, Map and Hub plus those seven values each have a separate unallocated Declaration preview; none was found as an individual Current Requirement / Declaration in the pinned frontier. The Projection.Form property carries no duplicate value enumeration. Terms Graph is deferred and no Form is admitted for it. The packet does not claim the seven proposed names have been applied or that any view exists under those Forms.

Before application, independently review the proposed Property, ten value Declarations and seven new names, the source-of-truth dimension removed from CA-R-1943, and all source hashes. Archive/version the four Current sources, allocate the new Declaration through the normal process, and update any remaining Current Claims that treat source selection as an identity component. This packet provides no migration receipt.

Consumers to reconcile after source approval:

- CA-D-635 serialization: persist `form`, the one `scope_unit` reference, `source.named_selection`, and any `source.atoms` versioned references. A selection-derived filename component may change without creating a new ID.
- The seven Projection view definitions and `.caprmedio_caprmedio/02_analysis/draft/subject-projections-20261103/generate_subject_projections.py`: assign each view its admitted Form, include Scope Unit and preserve source selection/version pins. Check current IDs and collisions before updating any instances or output paths.
- Projection identity checks, registries, filename readers, links, downstream generated indexes, and delivery consumers: use `(Form, Scope Unit)` consistently. Inventory each actual consumer before migration; this is not proof that every consumer has been found.
- Tests and projection rebuilding: verify both identity implications, Scope Unit exactly once, stable ID on source-Version and Named Selection changes, and distinct IDs on different Forms or Scope Units. Build and validate only after the source packet and migration plan are approved.
