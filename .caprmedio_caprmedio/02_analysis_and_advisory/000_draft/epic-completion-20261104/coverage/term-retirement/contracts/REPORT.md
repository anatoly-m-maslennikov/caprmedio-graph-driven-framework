# Term registry removal: source-contract impact

**State:** proposal previews only; held pending the human confirmation. No Current source, archive, frozen reference, runtime, code, tests, or Git state changed. Exact source versions and SHA-256 pins are in `manifest.json`; each proposed disposition has its own pinned preview.

## Smallest safe contract set

- Retain CCE path/operator grammar and Declaration semantics. Revise CA-R-1321, CA-R-1324, and CA-R-1931 only to remove registered-Term scope or obsolete Term-rooted addresses. Keep target resolution, source admission, direct Relation registry, containment, cardinality, and Property rules.
- Retain one-to-one canonical entity naming in a fresh-ID successor to CA-R-2276. Entity identity remains source-established and uses the complete qualified name; literal word reuse does not confer identity or admission.
- Retain separately admitted qualified value contexts in a fresh-ID successor to CA-R-1346; same spelling across contexts does not transfer admission or identity.
- Retain the general NARROWER_THAN acyclicity constraint in CA-R-1345. Remove only its obsolete Terms Graph passive Subject. NARROWER_THAN remains defined for model kinds by CA-R-2475 and has non-Term uses.
- Replace the dual Entity-and-Term projection contract/method with Entity-only successors for CA-R-1387 and CA-M-259. Preserve all generic parsing, evidence, admission, lineage, deterministic projection, output safety, and Run/Journal guarantees. Keep generic CA-E-433 and remap its two `evaluation_for` targets after IDs are allocated.
- Retire Term Definition and Terms Graph-specific contracts only after confirmation: CA-R-1318, R-1319, R-1279, R-1347, R-1244, R-1325, R-1454, E-382, E-659, M-439, M-449–M-455, M-458. Preserve each archived revision and frozen reference.

## Held issues

- CA-R-1284 and CA-R-1348 use `Term//Type`; a replacement target is not established. Preserve Type's single-valued Property and qualified allowed-value semantics; do not invent a new Type Entity.
- CA-R-1455's source-evidence and uncertainty guarantees remain useful, but its current Project-specific Term/missing-definition judgments and parent links depend on the branch being removed. Hold for a fresh-ID, lexical-evidence-only successor decision; do not retire its generic non-authoritative diagnostic value automatically.
- CA-M-125's Term Definition lookup is part of Subject assignment. Keep its assignment responsibility; review only its lookup step after confirmation.
- CA-R-1405, R-1747, R-1558, and R-1765 have Artifact/Type Term-rooted paths and are explicitly deferred to the overlapping artifact/type contract inventory owner.

## Scope boundaries

Ordinary English words, CFEL operator grammar, path labels, and exact literal strings are not by themselves registered-Term dependencies. No broad rewrite of those usages is proposed. EntityGraph, Scope Unit, declaration, relation, and source-authority behavior remains intact. Fresh IDs are required where a Summary changes; this packet allocates none.
