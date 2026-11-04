# Run–definition Relation contract previews

This source-only packet proposes the existing `IS_EXECUTION_OF` / `HAS_EXECUTION` pair for three matching instance pairs: Workflow Run → Workflow, Step Run → Step and Action Run → Action. It does not add a Relation Kind, Property, runtime object or actual Relation fact.

- CA-R-2245 and CA-R-2417 retain their IDs and Summaries. Each preview gives its direct or inverse binding, derivation classification and matching three endpoint patterns in the Formal Claim, with short Semantics. Cardinality and permissions remain in endpoint Declarations; generic direction and cross-Declaration boilerplate is removed.
- Three unallocated Run preview copies each propose exactly one outgoing `IS_EXECUTION_OF` to their matching reusable definition. Archived CA-R-1510@18, CA-R-1511@22 and CA-R-1969@11 describe one Workflow, Step or Action per respective Run. Current CA-R-2245 already places the Workflow Run bound at its endpoint.
- CA-R-2464, CA-R-2465 and CA-R-2467 previews explicitly permit each reusable Workflow, Step or Action zero or more outgoing derived `HAS_EXECUTION` links to matching Runs. Root accepted these `0+` allowances as authored permissions: they require no actual Run and do not infer or store another Relation fact.
- CA-R-2464 additionally combines `Container == yes` with its live Purpose Semantics and existing instance constraints. The live source was re-read and pinned. CA-R-2465 also classifies Step as a Container, as required by its existing Substep containment, while retaining all Step RUNS/decomposition conditions.

Under CA-R-2588, a Relation signature or inverse binding does not grant the other outgoing direction. Both the direct Run bounds and the explicit inverse permissions are needed under the default-zero model. This packet does not generalize the pair to Runtime, a Substep Run or another endpoint.

The Workflow source is also subject to root's concurrent work: compare the actual final Workflow WIP against this preview and combine all authorized changes into one pinned successor. Before adoption, independently review all eight previews and source pins, verify cardinalities and endpoint names in the final selected MODEL, allocate new Run IDs through the governed Draft route, validate the complete atomic source packet, and retain frozen version-qualified references.

Checks: eight preview/source hashes and YAML metadata; unchanged IDs, versions and Summaries; retained Step RUNS/decomposition conditions; six Current and four semantic evidence pins. These are source previews, not integrated CFEL validation, native admission, runtime behavior, graph regeneration or actual instances.
