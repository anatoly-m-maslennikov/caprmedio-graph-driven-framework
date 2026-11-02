# Coverage baseline — 2026-11-02

Status: read-only baseline. No Current source, projection, runtime or Git
state was changed.

## Pinned frontier

- Source: `.../node-declaration-20261031/migration-20261101/current-source-frontier.json`
- Sources: **1,101**
- Frontier SHA-256: `fadf6b7ef86a7f85fc88d63f8b0692c1aef0e3f254166b291d4cdafc4ba17fb7`
- Every loaded source SHA matches its frontier pin: **1,101/1,101**.

## Contract inventory

- Node Declarations: **90**
  - Primary Nodes: 30
  - Properties: 60
  - Missing source pins: 0
  - Version/status/SHA mismatches: 0
- Retained non-Node roots:
  - CFEL: 19 current root-source clauses
  - Carrier: 29
  - Term: 6
- Relation Definition candidates: **38**
  - Named owner relations: 38
  - Referenced relation names: 40

## Raw claim evidence

- Labelled CFEL Claim blocks: **114** across 110 sources.
- Fenced Claim blocks of all labels: **176**.
- Legacy unlabelled (`text`) Claim blocks retained: **71**.
- Unrecognized Claim blocks retained as review evidence: **13**.
- Claim sections with prose: **1,016**.
- Formal-only Claim sections: 84.
- Sources without a `## Claim` heading: 0.

The baseline stores source pins, line ranges, raw block text and hashes for
labelled, legacy and unrecognized Claim blocks, plus prose Claim
hashes/previews. It does not interpret CFEL semantics.

## Relation gaps

The current Relation contract is checked independently for each named Relation:

```text
Semantics;
((REL)) >| Derivation == Direct|Derived;
((DERIVED_REL)) ((IS_DERIVED_RELATION_OF)) ((SOURCE_REL));
((REL)) ((HAS_INVERSE)) ((COUNTERPART))
```

The short-notation line is required only for an existing admitted alias. A
Relation without an alias keeps its full name. `HAS_INVERSE` is required only
for a confirmed endpoint-reversing pair; inverse permission and cardinality
are not inferred.

Current source coverage reports:

- Semantics: 35 current candidates missing
- Existing short-notation bindings: 5 expected; 5 current candidates missing
- Derivation: 38 current candidates missing
- Derived-relation link: 7 current candidates missing
- Confirmed inverse declaration: 16 current candidates missing

The 60-row `candidate-clause-matrix.json` covers 38 Current Relation
Definition owners, 6 derived Declaration candidates and 16 retained CFEL
legacy candidates. It records source pins, draft paths and hashes, Claim
fence coverage, Semantics, Derivation, `IS_DERIVED_RELATION_OF`, existing
notation, confirmed inverse evidence and explicit gaps.

Used names that are not currently owned by a Relation Definition are:

`CONTAINS`, `HAS_INSTANCE`, `HAS_NARROWER`, `HAS_PROPERTY`, `IS_RUN_BY`.

Generic placeholders are kept separate: `R`, `RELATION`, `RELATION_TOKEN`,
`RELATION_TYPE`. Literal-binding markers and wildcard selectors are recorded
but are never promoted to Relations. Graph Relations and other CFEL operators
are distinct. Direct and derived permissions remain separate; inverse
permission and cardinality are never inferred. Unrecognized relation clauses
remain explicit review gaps.

Existing parser path aliases are `/` → `NARROWER_THAN`, `//` → `INSTANCE_OF`
and `.` → `IS_PROPERTY_OF`, using path traversal against the opposite authored
edge. A possible canonical-mapping change is flagged for review; no derived
glyph is adopted automatically.

## Diagnostics

The expected tree-issue packet is **31**:

- 16 CFEL
- 14 legacy Entity
- 1 Event Record

The current graph-diagnostics carrier separately contains 345 parser
diagnostics. The retained manifests confirm 16 CFEL, 14 legacy Entity and 1
Event Record issue: **31/31 verified**.

## Check command

```bash
python3 \
  .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/coverage/check_contract_coverage.py \
  --output \
  .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/coverage/baseline.json
```

When the generated contract graph exists, add `--graph PATH`. The checker
fails on missing entities, missing exact source clauses, missing Relation
Declarations, incomplete applicable Relation fields or unrecognized Relation
clauses.
