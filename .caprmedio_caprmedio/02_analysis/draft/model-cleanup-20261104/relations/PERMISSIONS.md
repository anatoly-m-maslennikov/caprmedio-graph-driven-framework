# Effective relation permission review

Scope: native active role-directory Markdown under `.caprmedio_caprmedio`, excluding 000_CAPRMEDIO_framework, draft, archive/archived, analysis and plans. The evidence index `permission-occurrences.json` pins the scanned paths and every non-own named-CFEL occurrence. It is a lexical candidate index: conditions, inverse metadata, right slots, source declarations, layer, inherited selectors and false positives must be interpreted, not counted as permissions. It does not prove exhaustive effective-MODEL closure, semantic prose extraction or runtime conformance. The reviewed catalog is the 41 declarations pinned in `manifest.json`; R2279 is archived and R2732 is Current.

## Confirmed source conflicts

1. **HAS_ACTIVE_SUBJECT**: R2462's instance default covers Atom instances via R2508 Atom → Continuant and R2589 Node/Continuant. R2618 makes the active-Subject field the source of a canonical link; R2469 requires the Declaration → Node links and puts `{:1}` on the *right* (number of declaring owners for each selected Node). That is not an outgoing Atom allowance under R2588. No outgoing named exception was found in the native Active CFEL scan. Thus the wildcard default rejects the same Declaration links required by R2469. It is not repaired by changing the owner count.
2. **GOVERNS**: R2278 states that each logical model entity has a declaring Requirement/Form Declaration and that its governed Subject identifies it; R2732 requires a qualified GOVERNS source fact. The declaring Atom is a Node instance, so its GOVERNS link is subject to the outgoing wildcard. No outgoing named exception was found in the scan. R1199 is the Relation domain signature and does not override that default.
3. **IS_DECLARED_BY**, when its qualified view is exposed for a Node host: R2732 derives the qualified reverse view and R2278 identifies it as the declaring Atom, but no Node-host outgoing exception for that direction was found. Under R2588 its direct source's allowance cannot grant the derived direction. This concerns the view's admissibility and adds no second authored fact; the result depends on the selected model including the relevant qualified source fact.

These findings are grounded in Required Node/Atom cases; absence of a named allowance for other relations is not by itself a defect. Broad blanket permissions and inverse exact-one counts have not been invented. The appropriate intended ranges of GOVERNS and IS_DECLARED_BY need governing decisions before a complete repair can be safely drafted. HAS_ACTIVE_SUBJECT needs a matching outgoing exception, but the exact Atom/target selection and bounds should be reconciled with its field and applicable ownership rules first.

## Per-relation permission assessment

Named general descriptors define domains, not grants. An inherited Node wildcard applies only where Host is in its selected Node population; a Carrier, CFEL descriptor or unresolved generic endpoint is not assumed to be a Node. The table records positive, conditional evidence or a remaining coverage gap; absence does not prove that a link exists or that its host is a Node. Inverse directions are assessed independently.

| Declaration | Relation | Effective permission evidence or gap |
|---|---|---|
| CA-R-1016 | `rationale_for` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1017 | `method_for` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1018 | `evaluation_for` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1019 | `delivery_for` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1020 | `implementation_of` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1021 | `evidence_for` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1022 | `concern_about` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1026 | `depends_on` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1199 | `GOVERNS` | CONFLICT: R2278 requires declaring Atom GOVERNS entity; Node Atom outgoing grant not found |
| CA-R-1200 | `DEPENDS_ON` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1580 | `BLOCKS` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1639 | `DERIVED_FROM` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1654 | `feature_realization` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1660 | `structural_parent` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-1993 | `CARRIES` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2170 | `IS_DERIVED_RELATION_OF` | Other CFEL occurrences in CA-R-2732; inspect matches individually: condition, metadata or right-slot alone is not outgoing permission. |
| CA-R-2245 | `IS_EXECUTION_OF` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2246 | `RECORDS` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2255 | `EXECUTES` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2417 | `HAS_EXECUTION` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2418 | `IS_CARRIED_BY` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2420 | `IS_EXECUTED_BY` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2421 | `IS_RECORDED_BY` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2422 | `required_by` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2473 | `IS_PROPERTY_OF` | R2462 model 0..1, instance Property exactly 1; root Node zero |
| CA-R-2475 | `NARROWER_THAN` | R2462 model Node → Node 0+ |
| CA-R-2476 | `INSTANCE_OF` | R2462 Node instance → Node model 0+ |
| CA-R-2477 | `HAS_CLASSIFICATION` | R2588 admits matching asserted/conditional axis and value only; >|/|< aliases normalized |
| CA-R-2478 | `IS_CONTAINED_BY` | R2465/R2466 Step/Substep; R2523 Scope Unit; R2525 Package; R2557 Event Record; evaluate host/layer separately |
| CA-R-2485 | `HAS_INVERSE` | Other CFEL occurrences in CA-R-1026, CA-R-1993, CA-R-2245, CA-R-2246, CA-R-2255, CA-R-2417, CA-R-2418, CA-R-2420, CA-R-2421, CA-R-2422, CA-R-2473, CA-R-2475, CA-R-2476, CA-R-2478, CA-R-2583, CA-R-2617, CA-R-2619, CA-R-2620, CA-R-2621, CA-R-2622, CA-R-2623, CA-R-2638; inspect matches individually: condition, metadata or right-slot alone is not outgoing permission. |
| CA-R-2583 | `HAS_EVENT_AUTHOR` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2617 | `CONTAINS` | R2464 Workflow; R2465 conditional Step; R2523 Scope Unit; R2525 Package; R2536 Journal |
| CA-R-2618 | `HAS_ACTIVE_SUBJECT` | CONFLICT: required Declaration → Node link has right-slot owner count only; no outgoing grant found |
| CA-R-2619 | `HAS_INSTANCE` | R2462 Node model → Node instance 0+ |
| CA-R-2620 | `HAS_NARROWER` | R2462 model Node → Node 0+ |
| CA-R-2621 | `HAS_PROPERTY` | R2462 model and instance Node/Property → Property 0+ |
| CA-R-2622 | `IS_EVENT_AUTHOR_OF` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2623 | `IS_RUN_BY` | R2464 Workflow → Step 0+; R2467 Action → Step/Substep 0+ |
| CA-R-2638 | `RUNS` | R2465 conditional Step → Action/Workflow exactly 1; R2466 Substep → Action exactly 1 |
| CA-R-796 | `child_of` | No non-declaration CFEL use found in scan; endpoint signature does not grant Node outgoing permission. |
| CA-R-2732 | `IS_DECLARED_BY` | CONFLICT for Node hosts if required qualified view is exposed: R2278/R2732 derive it but no Node outgoing grant found |

R2462 and R2588 supply the inherited default and precedence; R2462 also supplies the separate Node structural allowances above. R2465's Step RUNS and CONTAINS permissions are conditional, not additive unconditional grants. R2469's right-slot count cannot be treated as a left-slot grant. R2278's exact-one rule concerns logical model entity declaring owners, not every runtime instance. Cardinalities apply per selected endpoint, not to the Cartesian product; an inverse is not automatically exact-one. The source-level permission check does not establish that any particular population exists, that a generic endpoint resolves, or that an implementation evaluates these rules.
