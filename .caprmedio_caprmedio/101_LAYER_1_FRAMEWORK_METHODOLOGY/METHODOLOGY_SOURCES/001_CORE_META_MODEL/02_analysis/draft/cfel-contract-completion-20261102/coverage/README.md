# CFEL contract coverage

This folder is read-only migration evidence. It does not alter Current Atoms,
source carriers, projections, runtime code or Git state.

## Baseline

`baseline.json` is pinned to:

- the 1,101-source Current frontier;
- 30 Primary Node and 60 Property Declarations;
- retained `CFEL`, `Carrier` and `Term` root source clauses;
- all 38 Current `Relation Definition` candidates;
- labelled CFEL Claim blocks and every fenced Claim block, including legacy
  unlabelled and unrecognized blocks;
- Claim prose records and source hashes;
- relation-name usage separated from placeholders, predicates, literals and
  wildcards.

Each expected source records its Atom ID, Version, status, repository path and
SHA-256. The checker does not infer a Relation from `>`, `+>`, `:`, `=`,
wildcards or generic placeholders.

`candidate-clause-matrix.json` is the source-to-draft matrix for Current
Relation owners, derived Declaration candidates and retained legacy CFEL
candidates. `property-contract-review.md` records the bounded Property
contract review and remaining notation/closed-world questions.

## Invocation

From the repository root:

```bash
python3 \
  .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/coverage/check_contract_coverage.py \
  --output \
  .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/coverage/baseline.json
```

When the generated contract graph is ready, add `--graph PATH`. The graph
check fails on a missing expected entity, missing exact source clause, missing
Relation Declaration or unrecognized Relation clause. For every named
Relation it checks the applicable contract:

```text
Semantics;
((REL)) >| Derivation == Direct|Derived;
((DERIVED_REL)) ((IS_DERIVED_RELATION_OF)) ((SOURCE_REL));
((REL)) ((HAS_INVERSE)) ((COUNTERPART))
```

The short-notation line is checked only when an existing alias is admitted.
Relations without an alias keep their full named notation. `HAS_INVERSE` is
checked only for explicitly confirmed endpoint-reversing pairs; inverse
permission and cardinality are never inferred. Graph Relations and other CFEL
operators are distinct. Existing parser path aliases are `/` →
`NARROWER_THAN`, `//` → `INSTANCE_OF` and `.` → `IS_PROPERTY_OF`; a possible
canonical-mapping change remains a review item.

`--strict-diagnostics` verifies the retained CFEL candidate manifest and the
legacy-entity/event-record packet. The expected tree issue count is 31:
16 CFEL, 14 legacy Entity, and 1 Event Record. This is separate from the
current parser diagnostic count.
