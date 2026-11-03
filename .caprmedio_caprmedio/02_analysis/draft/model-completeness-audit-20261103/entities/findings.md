# Current MODEL entity declaration audit

Scope: the 1,167 canonical Current supplier paths in `model-supplier-frontier.json`, including the 13 additional carriers with legacy Subject keys. All 1,167 file hashes matched the frontier at the time of this check. Explicit STRUCTURE subjects, Term registry entries and concrete Atom instances are excluded; unprefixed supplier Subjects are retained as potential MODEL evidence. Broader Engine/Docs sources are not treated as MODEL entities.

The adjacent `entity-declaration-map.json` records exact identities, source IDs, paths, lines, recognized Subject and Formal Claim references, Definition Claim prose, and the per-target identity review. `inventory.py` regenerates the inventory and compares source hashes with the pinned frontier.

## Strict Declaration census

- 177 exact targets have one Requirement / Declaration: 28 Primary Nodes, 82 Properties, 41 Relations, 25 MODEL operator instances, and one other CFEL component. There are no exact-target duplicate Declarations in this bounded inventory. The 82 include `Project.Settings.Authority Modes`, declared by CA-R-2632 through its unprefixed legacy `governs` Subject.
- 47 exact targets have a Requirement / Entity Definition but no same-target Requirement / Declaration: 24 components, 22 Properties, one MODEL instance. Definition Claims are identity and meaning evidence, **not Declaration contract authority**. Exact-target absence does not alone prove that each needs a distinct new Declaration.
- After comparing each target and Definition Claim against declared identities, 45 are high-confidence distinct strict-form gaps: 24 non-Node components and 21 bearer Properties. The `Carrier/File.Format` Definition (CA-R-2346) appears to repeat the format inherited from `Carrier.Format` (CA-R-1950); whether they are one inherited Property identity remains an explicit review question. The distinct identity of the `Format//markdown` modeled instance versus any alternative Format address is also unresolved. These two are not counted as additional distinct missing Declarations.
- Similar leaf names on different bearers do not establish identity. For example, `Carrier.ID` identifies a Carrier, whereas `Atom.Header.ID` belongs to an Atom; `Carrier/File.Path` concerns a File Carrier, whereas `Atom.Header.Carrier Destination.File.Path` is an Atom Header Property. Each reviewed identity, same-leaf Declaration candidate and source Claim is recorded in the machine-readable map. No cross-bearer alias is asserted.
- 63 further exact-target references (32 Primary Nodes and 31 Properties) have no exact Declaration or Entity Definition. They require semantic, placeholder, inheritance and scope review and are not counted as confirmed missing entities.

## Inheritance and limits

Twenty-five additional qualified Property-use paths have an exact unqualified bearer Property Declaration and are recorded as inherited uses, not separate missing Declarations. Forty-eight other conditional selections and 168 complex Subject occurrences remain outside exact-target classification. Namespace root scaffolding is recorded separately.

CFEL, Carrier and Carrier/File have Entity Definition evidence in CA-R-2487, CA-R-1958 and CA-R-1957 respectively, each with its governed Subject at line 7 and its Claim preserved in the map. MODEL's named operator instances and Relation objects are included, while Term vocabulary instances are kept outside this entity census. Property contract detail belongs to the other audit lanes.

The inventory is bounded to selected Subject references and recognized CFEL Property selectors, relation endpoints and Relation-object references. It does not expand unsupported CFEL or prove every possible alternate-path identity, and it does not establish completeness for sources outside the supplier frontier. The 45 high-confidence results are review findings, not permission to invent or promote Declarations.
