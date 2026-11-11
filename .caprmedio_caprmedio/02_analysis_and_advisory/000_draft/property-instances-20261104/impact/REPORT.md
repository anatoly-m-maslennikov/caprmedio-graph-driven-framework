# Property-instance impact recheck

Rechecked all 88 declarations from the model-cleanup Property table against the proposed `rules/` overlays, including the revised CA-R-2243/2471/2472/2474 semantics and declaration previews. The 36-entry manifest's source and candidate hashes all match (`36/36`). These are proposal overlays, not Current adoption. The row-level pins and applicable overlay are in `property-instance-impact.tsv`.

## Result

No actual contradiction remains in the inspected contracts under these previews. The previous containment finding was based on the superseded blanket-mandatory rule and is withdrawn. The recheck has 82 rows with no conflict found and six conditional/structural-use questions; none is established as impossible from the pinned declarations.

- **Containment:** CA-R-2698@1 limits a present `IS_CONTAINED_BY` structural property to one selected endpoint. The CA-R-2699@1 and CA-R-2700@1 previews allow zero or one value for `atom` and `scope_unit`. Thus one endpoint may be present and carry a value; the other is omitted. There is no empty endpoint Property instance and no two-mandatory-child contradiction. The parent itself remains optional (`{:0..1}`).
- **RMED Claim:** CA-R-2500@4 still requires the Claim structural parent and one or two selected child names. CA-R-2721@1 and CA-R-2722@1 previews give each leaf zero or one Markdown value, meaning absent or present with one value. The parent requires nonempty child structure, so at least one child is present; the other may be omitted. The Formal Claim `FENCED_LABELS` constraint is guarded by that Property's presence. No impossible parent/child contract remains.
- **Event input/output:** CA-R-2572@2 and CA-R-2576@2 each allow the parent variant to be absent or present. If present, its selector allows two or three of `id`, `version`, and `updated_at`; `id` and `updated_at` provide two required values, while `version` is optional under the proposed CA-R-2574/2578 value-bound previews. Each present variant can therefore have a nonempty value satisfying the selected-child range. No declaration here requires input and output simultaneously.
- **Nested Settings:** Parent/child counts remain satisfiable. For example, Project Settings allows 3..11 of 11 child names; required Name and Prefix plus at least one other selected value-bearing setting can satisfy the lower bound. Optional zero-child groupings may be omitted; if present, they need a nonempty child value to qualify as present Properties.

## Remaining conditional evidence

Five mandatory or optional zero-direct-value structural parents have a child selector that permits zero: `Atom.Content`, `Atom.Header.Relations`, `Atom.Header.Subjects`, `Project.Settings.Confidence`, and `Project.Settings.RMED Review`. A present instance must have nonempty child structure to have a value; the empty instance is invalid. Their constraints still admit nonempty valid values, and the pinned 88-row declaration set does not establish that an applicable bearer must be empty or lacks a child. The first three therefore need model-instance/applicability evidence before deciding whether the mandatory container requirement is satisfiable for every bearer. The two optional Settings groupings can be omitted; they only need children when present.

`Atom/(.Header.Role:=Operations).Workflow.Purpose` remains conditional on unresolved Workflow variant applicability (CA-R-2464@5, CA-R-2734@1, CA-R-2735@1). If it applies, its positive one-value constraint requires a present value-bearing instance.

## Interpretation applied

The preview rules give a Property at most one occurrence per corresponding bearer. A leaf with a positive value minimum is required; a zero minimum alone allows omission, and a present Property cannot be valueless. Structural parents with zero direct values can still have a value through nonempty child structure. Explicit occurrence and other applicable constraints remain in force. Thus a local optional leaf clause moved from occurrence `{:0..1}` plus value `{:1}` to value `{:0..1}` means “absent, or one present value.” It does not create an empty-field node.

The inventory is the bounded 88-row frontier, not a complete declaration or runtime-instance census. No parser enforcement, data migration, preview adoption, or Current-source change was performed.
