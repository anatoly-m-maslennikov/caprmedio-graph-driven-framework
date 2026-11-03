# Read-only Relation audit

Baseline: the selected 1,167 Current MODEL supplier sources pinned by `model-supplier-frontier.json` (the prior 1,154 plus thirteen legacy-governs suppliers). All 1,167 current hashes match the frontier. `inventory.json` carries every source pin, all 41 Relation Declarations, every detected named Formal Claim use, aliases, normalized inverse bindings and carrier relation keys. No canonical source, code, Git state or previous packet was edited.

## Findings for root adjudication

### REL-01 — Declaration active-Subject endpoint restriction excludes the newly admitted non-Node declarations

**High.** R2618 line 28 restricts Requirement/Declaration HAS_ACTIVE_SUBJECT targets to `(Node, Node.**)`; lines 37 and 39 explicitly say that a Declaration addresses a Node. R2487 lines 92–95 separately admit Carrier and CFEL descriptor entities as graph endpoints and state that graph Relations are not limited to Node. The 41 Relation Declarations actually address `Relation//NAME`; the NamedRelationDirection and Alias operator Declarations address `Operator//NAME`. The selected contract supplies no conversion of those CFEL descriptors into Node instances. The generic Atom signature on R2618 line 32 does not remove the more specific Declaration restriction. An implementation intersecting both signatures can reject the catalog it is intended to declare.

This finding does **not** require all objects or Terms to become Nodes. The question is the specific Declaration-only restriction. Root should adjudicate against any explicit inheritance evidence supplied by the graph lane.

### REL-02 — The outgoing-only count sentence contradicts valid right-endpoint cardinalities

**High.** R2588 line 47 says “Every count concerns the active Subject's outgoing Relations.” R2487 lines 67–69 explicitly admits independent forward and reverse slots `Source {:forward}((RELATION)){:reverse} Target`. R2469 line 25 actually places `{:1}` on the right of HAS_ACTIVE_SUBJECT to count authoritative Declaration owners per selected Node; its prose lines 32–39 explains that ownership count. Reading R2588 literally as the universal counting rule changes that valid reverse bound into an outgoing count or makes the contracts conflict.

The right-hand annotation is legal and should **not** be reported as malformed syntax. The contradiction is the unrestricted “Every count” sentence, not the use of reverse cardinality or omission of an unspecified count.

### REL-03 — Minimal inverse policy is stated as a policy for every derived Relation

**Medium.** R2486 line 27 applies reversed endpoints, inherited meaning and a reverse counterpart binding to “Each derived Relation”; R2487 line 89 likewise says a derived Declaration retains the reverse counterpart binding and alias. R2279 lines 28–31 and 36–43 explicitly define IS_DEFINED_BY through IS_DERIVED_RELATION_OF and the R2278 qualified GOVERNS selection, **not** an unconditional HAS_INVERSE pair. R2170's semantics also says that IS_DERIVED_RELATION_OF alone specifies no endpoint transformation.

All eleven declared HAS_INVERSE pairs conform to the minimal inverse policy. IS_DEFINED_BY correctly keeps its qualification; applying the broad wording to it would either require a nonexistent inverse binding or discard the qualifying semantics. R2486 line 33 additionally requires a qualified counterpart's qualification at its direct source, while R1199 lines 35–37 and its prose do not own the R2278 qualification; R2279 does. This is a scope/ownership inconsistency between the general policy and the preserved qualified case, not evidence that IS_DEFINED_BY should become an unconditional inverse.

### REL-04 — Informational: thirteen actual classification uses retain an admitted short alias

**Informational, not a demonstrated grammar violation.** Thirteen classification conditions/conclusions in selected Formal Claims use `>|`. These are actual predicates, not Relation-object references, Subject paths or quoted alias strings. Current R2477 declares `alias(Relation//HAS_CLASSIFICATION) == ">|"`; R2487 explicitly admits the glyph and R2588 line 45 normalizes it. The named-Relation object/predicate distinction does not by itself prohibit an admitted predicate alias. No exact Current grammar prohibition was established, so this is a consistency observation only, not an automatic defect. `inventory.json.formal_classification_alias_uses` gives the exact source lines:

- R2462 lines 37, 39: Independence conclusions.
- R2484 lines 24, 25: Container allowed cases.
- R2499 line 34: Summary obligation condition.
- R2523 line 25, R2524 line 25, R2525 line 25, R2536 line 26, R2559 line 26, R2560 line 26: Container conclusions.
- R2701 line 30, R2714 line 30: Current/Archived field conditions.

Their Relation meaning resolves unambiguously to HAS_CLASSIFICATION; they are not undeclared predicates or alias collisions. Any optional conversion to named predicates would be a style/normalization choice unless a separate explicit prohibition is supplied. Ten other `<+` occurrences were excluded here because they are model address/path forms; quoted alias glyphs were protected.

## Checks that passed

- Exactly 41 Active Requirement/Declaration carriers own exact `Relation//NAME` subjects; no duplicate catalog ownership in the frontier.
- Thirty-five distinct concrete named Relation predicates occur in CFEL fences, plus the separate `((*))` wildcard. Every concrete predicate has a catalog declaration. The apparent `RELATION` unknown occurs only inside two quoted CFEL-operator templates, so it is excluded from actual-use counts.
- Five actual carrier keys (`child_of`, `method_for`, `evaluation_for`, `depends_on`, `delivery_for`) all have exact-name declarations. They are not case-folded into DEPENDS_ON. No authored inverse carrier key was found.
- Seven lexical aliases have typed `alias(Relation//NAME)` operands, no empty tokens, no conflicting values and no cross-Relation token collisions. Relation-object metadata uses qualified addresses; no operator-as-object or retired @reference syntax was detected in CFEL fences.
- Eleven inverse pairs each have one direct-owned binding and one equivalent reverse-written view. Normalization yields eleven facts, not twenty-two independently authored facts. No self-pair, multiple direct source, inverse cycle, conflicting classification or unconditional GOVERNS/IS_DEFINED_BY inverse was found.
- Each minimal inverse resolves endpoint meaning and domain to its direct Declaration; its own absence of duplicated prose/signature is intentional. IS_DEFINED_BY retains its separate qualified semantics. Generic endpoint variables remain restricted by R2486 to declared entities/instances; they do not admit literals, and a non-Node entity is not rejected merely for being outside Node.
- No `Object ((NAME)):{...}` form was found. Existing left/right allowed bounds and conditional count operators were kept distinct. R2469's right-side owner bound is valid. Missing counts remain unspecified rather than zero.
- Workflow/Step/Substep/Action and Scope Unit/Package/Journal containment pairs have explicit opposite-direction named entries where the corresponding model constraints state them. Inverse metadata itself is not counted as permission. Conditional Step RUNS/CONTAINS constraints were examined together rather than treating a condition as an unconditional grant. No additional concrete whitelist contradiction is asserted beyond REL-02.

## Limits and held checks

This is a source-level semantic audit, not execution of a complete CFEL evaluator. It does not prove all runtime populations satisfy their domains or cardinalities. Carrier references with `@version` or targets outside this selected frontier require historical/external resolution; they are not called missing entities here. No count was invented for an intentionally unbounded signature. Root still owns false-positive adjudication and any cross-lane inheritance evidence.

## Final supplier-frontier extension

The thirteen additional suppliers (including R2632 AuthorityModes) introduce no named `((Relation))` predicate, no new Relation Declaration and no new carrier Relation key. Their exact pins are included in inventory.json. The final census remains 41 declarations, 35 concrete used predicates plus wildcard, seven aliases and eleven inverse pairs, with zero unknown actual names or source drift. REL-04 is informational only; REL-01–03 remain open semantic findings for root adjudication.
