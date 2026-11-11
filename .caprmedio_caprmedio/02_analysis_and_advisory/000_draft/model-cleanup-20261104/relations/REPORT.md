# Relation Declaration review — Current snapshot

41 declarations reviewed below, including CA-R-2732; CA-R-2279 is now archived. The prior audit inventory is a locator only: all rows and source hashes in manifest.json refer to the live source at this review. Current sources changed during review; recheck every pin before use. This is a semantic source review, not proof of graph population, parser enforcement, runtime behavior or migration. Candidate files are complete source previews; they preserve the original Summary, identity and metadata and are not adopted.

| Declaration | Relation | Classification | Effective domain and verdict |
|---|---|---|---|
| CA-R-1016 | `rationale_for` | Direct | Rationale Atom → explained Atom |
| CA-R-1017 | `method_for` | Direct | Method Atom → Requirement Atom |
| CA-R-1018 | `evaluation_for` | Direct | Evaluation Atom → evaluated Atom |
| CA-R-1019 | `delivery_for` | Direct | Delivery Atom → realized Atom |
| CA-R-1020 | `implementation_of` | Direct | governed Implementation Carrier → specification Atom |
| CA-R-1021 | `evidence_for` | Direct | Evidence Carrier → Evaluation or Implementation Carrier |
| CA-R-1022 | `concern_about` | Direct | Concern Atom → governed entity |
| CA-R-1026 | `depends_on` | Direct | dependent Artifact → prerequisite Artifact; excludes Plan scheduling |
| CA-R-1199 | `GOVERNS` | Direct | Atom → governed Subject; stale Node wording: see candidate |
| CA-R-1200 | `DEPENDS_ON` | Direct | Atom → referenced Subject other than governed target; stale Node wording: see candidate |
| CA-R-1580 | `BLOCKS` | Direct | Plan → Plan; prerequisite for starting |
| CA-R-1639 | `DERIVED_FROM` | Direct | derived → source represented-content version; unresolved population requires source binding |
| CA-R-1654 | `feature_realization` | Direct | SPEC Feature Scope Unit → native realization target; target population needs governing source |
| CA-R-1660 | `structural_parent` | Direct | child → immediate structural parent; Project Structure owns declarations |
| CA-R-1993 | `CARRIES` | Direct | Carrier → non-ephemeral represented Entity |
| CA-R-2170 | `IS_DERIVED_RELATION_OF` | Direct | derived Relation descriptor → source Relation descriptor; no reversal implied |
| CA-R-2245 | `IS_EXECUTION_OF` | Direct | Workflow Run → Workflow; other chat owns execution semantics |
| CA-R-2246 | `RECORDS` | Direct | Event Record → recorded event or execution; other chat owns execution semantics |
| CA-R-2255 | `EXECUTES` | Direct | Runtime → Workflow Run; other chat owns execution semantics |
| CA-R-2417 | `HAS_EXECUTION` | Derived inverse | reverse of IS_EXECUTION_OF; inherits its endpoint domain and conditions |
| CA-R-2418 | `IS_CARRIED_BY` | Derived inverse | reverse of CARRIES; inherits its endpoint domain and conditions |
| CA-R-2420 | `IS_EXECUTED_BY` | Derived inverse | reverse of EXECUTES; inherits its endpoint domain and conditions |
| CA-R-2421 | `IS_RECORDED_BY` | Derived inverse | reverse of RECORDS; inherits its endpoint domain and conditions |
| CA-R-2422 | `required_by` | Derived inverse | reverse of depends_on; inherits its endpoint domain and conditions |
| CA-R-2473 | `IS_PROPERTY_OF` | Direct | Property → bearer |
| CA-R-2475 | `NARROWER_THAN` | Direct | narrower → broader MODEL kind |
| CA-R-2476 | `INSTANCE_OF` | Direct | instance → kind |
| CA-R-2477 | `HAS_CLASSIFICATION` | Direct | classified entity → axis, with value qualification |
| CA-R-2478 | `IS_CONTAINED_BY` | Direct | part → immediate Container; +> alias; Container classification required |
| CA-R-2485 | `HAS_INVERSE` | Direct | direct Relation descriptor → derived inverse descriptor; no permission |
| CA-R-2583 | `HAS_EVENT_AUTHOR` | Direct | Event Record → Actor |
| CA-R-2617 | `CONTAINS` | Derived inverse | reverse of IS_CONTAINED_BY; inherits its endpoint domain and conditions |
| CA-R-2618 | `HAS_ACTIVE_SUBJECT` | Direct | Atom → entity/instance from active Subject, including Carrier and CFEL |
| CA-R-2619 | `HAS_INSTANCE` | Derived inverse | reverse of INSTANCE_OF; inherits its endpoint domain and conditions |
| CA-R-2620 | `HAS_NARROWER` | Derived inverse | reverse of NARROWER_THAN; inherits its endpoint domain and conditions |
| CA-R-2621 | `HAS_PROPERTY` | Derived inverse | reverse of IS_PROPERTY_OF; inherits its endpoint domain and conditions |
| CA-R-2622 | `IS_EVENT_AUTHOR_OF` | Derived inverse | reverse of HAS_EVENT_AUTHOR; inherits its endpoint domain and conditions |
| CA-R-2623 | `IS_RUN_BY` | Derived inverse | reverse of RUNS; inherits its endpoint domain and conditions |
| CA-R-2638 | `RUNS` | Direct | Step → Action or Workflow; Substep → Action; count and conditional rules are separate |
| CA-R-796 | `child_of` | Direct | child Atom → governing parent Atom; planned replacement distinct |
| CA-R-2732 | `IS_DECLARED_BY` | Qualified derived | qualified GOVERNS subset reversed; Requirement/Declaration owner under R2278; no HAS_INVERSE |

## Cross-cutting assessment

- R2486 and R2487 now distinguish declared model entities/instances, including Carrier and CFEL descriptors, from literals and glyphs. R2618's Declaration-only Node restriction was removed. R2588 now distinguishes the two endpoint count slots and limits the wildcard baseline to outgoing counts. The prior audit REL-01–03 are repaired at the inspected source level; this is not runtime validation.
- A named signature defines endpoint domain, not an independent whitelist permission or a fact. A direct permission does not permit the derived inverse; verify each direction's inherited/local model or instance allowance separately. Normalize reverse writing and written count slots; omitted count is unspecified. Count each selected endpoint's matching neighbors, not a Cartesian product. No inverse exact-one follows from a forward exact-one.
- Minimal inverse Declarations intentionally carry only the reverse HAS_INVERSE view and their own alias if present. They inherit endpoint meaning/domain from the direct counterpart, while each direction's permissions remain separate. IS_DECLARED_BY instead explicitly preserves its qualification and endpoint reversal; it is not an unconditional inverse. Relation//NAME is a descriptor, ((NAME)) an actual relation operator, and <((NAME)) its reverse written view. IS_CONTAINED_BY is direct; CONTAINS is derived, and +>/<+ are directional aliases.
- R2465 gives Step the conditional exclusive choice between containing one or more Substeps and running one Action or Workflow. R2466 gives each Substep exactly one Action; R2638 reflects these endpoint domains, while IS_RUN_BY is its inverse, not an automatic inverse permission or count. Actual workflow-instance implementation is deferred; the declarations' #instances labels alone do not establish realized instance conformance.
- R1199 and R1200 call Subjects graph Nodes, while R2486/R2487 and R2278 admit named Carrier and CFEL entities, and R2732 derives from GOVERNS for those declaring owners. Their generic signatures do not narrow to Node. Two complete pinned previews replace that stale Node wording with entity or instance and retain role, content and other constraints. Before adopting R1200, check that the relevant Subject resolver admits the selected target; the candidate does not assert that every mention resolves.
- R2469 explicitly counts declaring owners for Nodes and their Properties; R2278 separately sets exact-one declaration ownership of logical model Entities including other branches, and explicitly does not create an ownership rule for each runtime instance. Do not extend either bound to all instances or infer an inverse outgoing permission.
- Generic endpoint variables cannot establish a population by themselves. In particular, represented-content versions (DERIVED_FROM), native realization targets (feature_realization), governed entities (concern_about), structural children/parents, and runtime occurrence endpoints need their applicable source declarations. No missing population is asserted empty or resolved merely by this audit. Review actual effective inherited permissions for selected MODEL and layer before admitting links.
- R2638, R2465 and R2466 describe existing Step/Substep domains; none of the candidates changes workflow execution semantics or invents workflow instances. Check the companion Workflow work before any coordinated adoption.

No separate user decision is needed for the two narrow wording previews. Whether remaining generic endpoint populations are fully defined requires their governing source/consumer review; this review does not guess missing kinds or invent declarations.
