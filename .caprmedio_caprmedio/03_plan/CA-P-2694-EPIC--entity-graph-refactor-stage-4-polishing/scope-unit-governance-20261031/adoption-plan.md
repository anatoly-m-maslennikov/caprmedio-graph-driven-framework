# Scope Unit Declaration adoption plan

## Prepared

- 44 instance Drafts have CFEL Claims. Names, Labels, Parents, nine ordering numbers and the retained structural fields are preserved from the original source.
- 43 non-root units have stable IDs. The Project root has none and inherits its ordering constraints from the Project model.
- Frontmatter uses role, form and subjects.active; legacy owner fields and Author are absent. External placement ownership stays in the manifest.
- Folder paths are derived. Authority names include the non-root Scope Unit ID; Delivery names omit it. Project Authority remains `.caprmedio_<project name>`.
- Applicable Methodology remains a Projection, with its hosting Scope Unit planned for retirement.

## Remaining work

1. Review the instance Claims and shared model together against the latest Operator answers. Check fields, IDs, cardinalities, containment and inheritance. Do not claim parser/runtime acceptance from a readback.
2. Retire project_structure.toml completely: governing Atoms, the live file, reader/writer implementations, public bindings that only edit that file, tests and documentation. Declaration Atoms are the sole structural source; no TOML fallback or compatibility output remains.
3. Integrate the changed ordering model with old sources: R1758's Ordered/Unordered Type vocabulary and R2529's Local Order declaration are supersession candidates for ordered and order.number; review their actual consumers before retirement. D440/D441's TOML source conventions and the old native-folder exceptions also need disposition for the source cutover.
4. Review canonical Definition ownership and avoid adopting a second Declaration of an existing model Entity. Apply the shared Project/ID successor Drafts with their related constraints together.
5. Set final external placement, including the Operator-owned root Declaration. Resolve remaining Engine-side Goals in that separate work; do not synthesize them here.
6. Assign canonical Atom IDs to new R Drafts, then promote the reviewed source set with history. Scope Unit IDs are already assigned; these are different identities.
7. Cut over Engine consumers to Current Declaration Atoms, then move Authority and Delivery folders to their derived paths. Delete the live TOML; no fallback or compatibility output remains. Keep Scope Unit workflow definitions unchanged and remove their four TOML-specific executable implementations/bindings. Runtime release remains a separate operation.

[Draft index](instance-drafts.md) · [Source mapping](field-mapping.md). Publication and physical migration are tracked in adoption-execution.json.
