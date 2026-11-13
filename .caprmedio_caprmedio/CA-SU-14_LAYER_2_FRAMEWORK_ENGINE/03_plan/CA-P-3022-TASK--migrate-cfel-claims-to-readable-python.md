---
identity:
  atom_id: CA-P-3022
  ref_id: CA-P-3022
context:
  role: plan
  form: Plan
  label: Task
  tier: 3
  container:
    scope_unit: CA-SU-14
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:47:49.228319+00:00'
destination:
  file:
    name: CA-P-3022-TASK--migrate-cfel-claims-to-readable-python.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan
---
## Summary

Migrate CFEL Claims to readable Python

## Objective

This standalone Task tracks the remaining CFEL migration after the Python pilot in CA-P-3018.

Migrate CFEL Formal Claims to readable Python declarations and expressions. Preserve Topic and Subject notation. Use descriptive functions, classes and named parameters with minimal boilerplate. Lint syntax and model references.

Specification: CA-R-2721, CA-R-3081, CA-R-3082, CA-R-3131.

## Inventory and cutover

The Workbench snapshot found 335 distinct Current references and 132 Draft references with Formal Claims. It also found 970 Current carriers, including installed and historical copies. Pin the authoritative source of each reference before using these counts for migration coverage.

1. Inventory the remaining Current and Draft CFEL Claims. Convert or retire each one under the applicable Model decision.
2. Check syntax and references, then test the complete selected Declaration set. Verify inheritance, overrides, Relation contracts and Scope Unit topology.
3. Use the Model package built and verified in CA-P-3055. Check graph, schema and runtime behavior as consumers migrate.
4. Activate the Python-only revision of CA-R-2721. Retire the CFEL language Atoms and remove CFEL compilation and translation from build and runtime. Keep Topic and Subject notation.

## Acceptance

The selected Declaration set passes validation as a whole. The build and runtime use Python Formal Claims. Graph and schema outputs are derived from those Declarations. Every remaining authoritative CFEL Claim has been converted or retired.

## Source census

A filesystem check started from the 41 declared Scope Unit paths and scanned their standard Role folders. It recognized the same CFEL Claim fences as the current schema compiler. This found 335 Current references across 471 CFEL carriers and 72 numbered Draft references. For 155 Current references the scan found more than one candidate carrier, including candidates without a CFEL block. Eight declared paths were absent and 31 candidate Markdown carriers did not parse. Resolve those exceptions before treating this as a complete migration inventory. Use exact carrier path, Version and digest for each selected source.

The path check found 328 unqualified Current carriers with CFEL Claims. Of those, 298 matched their declared Scope Unit Container and 30 lacked Container evidence. Six references had only historical carriers, and one unqualified Current carrier had no CFEL Claim. The 31 parse errors included 29 qualified filenames and two unqualified Delivery Atoms, CA-D-487 and CA-D-488. Neither Delivery Atom has a CFEL fence. The working manifest at `.caprmedio_tmp/CA-P-3018/CA-P-3022/cfel-source-frontier.json` records the paths, Versions and digests for this snapshot. Revalidate the manifest before cutover.

## Model Drafts

- CA-R-2721@5-draft admits one Python fence for a Formal Claim whose consumers support Python. It keeps CFEL admitted during migration.
- CA-R-2500@7-draft, CA-R-1417@34-draft, CA-R-2102@18-draft and CA-R-2471@11-draft defer the fence language to the applicable Formal Claim declaration.
- CA-R-3010@8-draft applies the transition to the optional Formal Claim in Code Synopsis.

## Python representations

CA-R-2722@5-draft uses the same declaration for a nested Property, its RMED scope, and its direct value and dependent Property cardinalities.

```python
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Requirement, Method, Evaluation, Delivery

declare_entity(
    entity_name="Prose Claim",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Content.Claim",
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
    applies_to_entity_classes=(Requirement, Method, Evaluation, Delivery),
)
```

CA-R-3084@1-draft uses an ordinary Python subclass to give Method / Decision its own identity. CA-R-2554@3-draft uses a named, typed predicate to check the Scope Unit level against its container.

Use ordinary Python for these cases. A separate expression interpreter agreed on the Decision fixtures and needed additional operator dispatch. The typed Scope Unit check runs the exact reviewed function against Model data. Revisit the expression-engine decision for an uncovered Claim that needs it.

A local MODEL override must replace the matching inherited rule while leaving the base MODEL intact under CA-R-2559 and CA-R-2468. The CA-R-2706@2 Tier probe confirmed that sending both incompatible formats to the current Header compiler raises a declaration collision. Selecting the exact local replacement before compilation kept the local source reference and left the base declaration intact. Add acceptance cases for explicit replacement, unrelated rules inherited unchanged, and two competing replacements rejected.

## Baseline

The existing schema, Relation registry, Scope Unit, lifecycle placement, and graph projection tests passed 117 tests and 24 subtests in the checkout. This is the CFEL baseline. Run parity again against the Python path before cutover.

Compiled the exact 328 unqualified CFEL candidate carriers. Of these, 267 feed the declaration compilers. The other 61 include Relation Declarations, Scope Unit Declarations, Scope Delegations, Rules, and Delivery Forms that require their applicable consumers. The normalized baseline at `.caprmedio_tmp/CA-P-3018/CA-P-3022/cfel-consumer-baseline.json` contains records and digests for Workbench Content, Header and Status Groups, and Lifecycle Content, Header and Role/Form. Compare Python output against these records.

The additional baseline at `.caprmedio_tmp/CA-P-3018/CA-P-3022/cfel-graph-placement-baseline.json` records four checked consumer outputs. The Relation registry recognizes 47 names and 12 inverse bindings, the Scope Unit parser derives 41 units, the Core placement compiler produces 31 rules across eight Role folders, and the Contract Graph produces 190 entities and 45 Relations from the pinned candidates. The graph already has 30 coverage gaps. The registry also reports a case collision between the Subject reference `DEPENDS_ON` and Artifact prerequisite `depends_on` declared by CA-R-1200 and CA-R-1026. Preserve and compare these diagnostics explicitly during parity. A green output count alone does not establish source coverage.

## Python representation check

The checkout probe compared hand-authored Python declarations with the records produced by the existing CFEL compilers from the authoritative carriers.

| Claim revisions | Comparison |
|---|---|
| CA-R-2500@6 | Claim heading count, zero direct values and the allowed unique children produced identical lifecycle validation records. |
| CA-R-3005@3 | The Decision Form's four admitted Roles produced identical Role/Form validation records. |
| CA-R-2716@2, CA-R-2717@3 and CA-R-2718@3 | Name and Path inherited the parent's string format. Both the field declaration and the format source retained their own references. |

The two lifecycle comparisons passed 17 accepted and rejected cases. A small expression interpreter and an ordinary Python predicate agreed on 16 Decision Form cases. Five read-only syntax and reference lint checks passed in the probe. The expression interpreter needed its own operator dispatch for these cases. Prefer ordinary declarations and predicates for this first group. Revisit a separate engine if a later Claim needs it.

The current lifecycle validator accepts both orders of Prose Claim and Formal Claim in CA-R-2500. The source requires Prose Claim before Formal Claim. Keep the declared order in the Python representation and test enforcement separately from existing-validator parity.

## Staged migration

The Engine reads CFEL and static Python Formal Claim fences. Python Claims use named parameters and are parsed without executing them. The reader uses the fence language, so the container needs no feature flag. Topics retain their existing syntax.

The pinned conversion produced 299 of 328 Current Claims and 52 of 72 Draft Claims. Converted copies preserve the original Header, Topics and Markdown outside the fence. The 351 converted Claims matched the existing graph extraction after expression whitespace normalization. The mixed source build also matched Workbench schema and Relation registry outputs and Lifecycle Role/Form, Header, Content, Status and placement outputs. Twenty-one converted Scope Unit declarations resolved identically. Two Draft Scope Unit declarations were rejected identically by the Current-only reader.

The focused suites passed 260 tests and 95 subtests. The isolated image returned HTTP 200, served an MCP `query_run` request, loaded a Python Project declaration with a CFEL child declaration, and ran the packaged linter. The build and smoke logs are in `.caprmedio_tmp/CA-P-3018/CA-P-3022/python-claims-final-xxryc6vv`.

Cutover remains open. The conversion inventory lists 29 Current and 20 Draft Claims that need additional work. The reference linter passed 246 staged Claims and reported 105 diagnostics against the captured catalog. Review those diagnostics, reconcile the outstanding source pins and adopt the transition Declarations before replacing live Claims.

## Native Python declaration drafts

The 50 Drafts use `declare_entity` and `declare_relation` to test native class inheritance, nested typed fields, and separate Model and instance Relation rules. [CA-A-1339@1-draft](../02_analysis_and_advisory/000_draft/CA-A-1339@1-draft-FRAMEWORK_ENGINE-ANALYSIS_REPORT--review-the-python-declaration-draft-cohort.md) lists the Draft references, source revisions and review findings. The Drafts keep the migration Task open until the binding and effective rules pass parity checks.

## Formal Model Engine preview

- FORMAL_MODEL_ENGINE is registered as CA-SU-50 under PROGRAMMATIC. CA-R-3090@1 declares its structure. CA-R-3091@1 delegates its responsibilities. CA-R-2654@6 admits the Subject from PROGRAMMATIC. Existing Scope Units keep their declaration arrangement during migration.
- The pinned preview bound all 50 native Python Claims. It derived 13 class contracts, 24 Property contracts and 13 Relation contracts. It verified four distinct Decision branches, two Project-scoped singletons, inherited field formats and the Relation inverse contracts. No Draft diagnostics were reported.
- The graph and parser suites passed 183 tests. The isolated container image built and rendered the formal Model graph from the same pinned Drafts. The preview and its source manifest are in `.caprmedio_tmp/CA-P-3018/CA-P-3022/formal-model-engine`.
- The mixed preview still reports 40 coverage gaps and 347 unsupported legacy clauses. Keep this Task Active until the rest of the migration and Current cutover are verified.

## Mixed consumer verification

- CA-R-2721@5 admits Python Formal Claims where the affected consumers support them. CA-R-2500@7, CA-R-1417@34, CA-R-2102@18, and CA-R-2471@11 now defer the language to that declaration. CFEL remains admitted during migration.
- The shared Workbench and Lifecycle compiler reads the 50 native Python Drafts. The staged schema preserves effective Header, Content, and placement rules. The four Decision Forms keep their Role-qualified identities. The Relation registry still needs inverse-alias compatibility checked before cutover.
- All 50 Drafts pass syntax and reference linting against the mixed Model catalog. The isolated image built and read the 50 Claims and all 42 Scope Units. Evidence is in `.caprmedio_tmp/CA-P-3018/CA-P-3022/native-candidate` and `.caprmedio_tmp/CA-P-3018/CA-P-3022/formal-model-engine/native-lint-verification`.
- Refresh the pinned source inventory after each adoption batch. The legacy bridge and native declarations have different migration coverage. Compare each selected source and the aggregate consumer outputs before switching Current Claims.

## Second native Draft batch

- Published 52 additional native Python Drafts from pinned sources. The batch adds 28 Properties, 21 classes and 3 Relations. Three existing Drafts were also converted in place: CA-R-2530@3-draft, CA-R-2618@4-draft and CA-R-2958@1-draft. All three passed the linter. The remaining held cases are the competing revisions for CA-R-2530 and CA-R-2618, the legacy Draft for CA-R-1021, and the unresolved Step.Content.Claim address in CA-R-2969.
- The combined graph bound all 102 Drafts without native diagnostics. All 102 pass syntax and reference linting. Effective Workbench Header and Content columns, Lifecycle Header and Content constraints, and placement rules match the Current baseline. The four Decision Forms have separate Role-qualified identities.
- The combined Relation registry retains the existing reverse rows through the CFEL inverse declarations. The native compiler also preserves those rows when only the Python Relation declaration is present. The mixed 102-Draft registry no longer reports duplicate inverse aliases. The earlier DEPENDS_ON spelling collision remains.
- CA-R-3081@1 and CA-R-3083@1 are Current. CA-R-3082@1-draft records the derived inverse requirement.
- The isolated candidate image initialized successfully and served MCP query_run. The live Workbench image still needs the mixed compiler before the Claim Drafts are promoted. Coordination with CA #8 is underway.
- The combined preview and verification are in `.caprmedio_tmp/CA-P-3018/CA-P-3022/native-candidate`. The exact new Draft references are in `.caprmedio_tmp/CA-P-3018/CA-P-3022/next-native-publication/published.json`.

## Model rule provenance

- CA-R-2743@3-draft defines the structured Entity view. Show Direct and Derived Relations, and label each Property or Relation rule as declared here, inherited, or overridden here.
- CA-R-3081@2-draft defines the Entity override rule. A local rule for the same Property or Relation overrides the inherited rule. The view preserves both Declaration references.
- The Model graph now renders both Relation kinds and all three rule origins. The staged preview is `.caprmedio_tmp/CA-P-3018/CA-P-3022/native-candidate/model-rule-origins.md`.
- The release candidate passed the mixed-Claim compiler check. The full release suite reported 24 failing modules, including a migration converter import failure that has since passed in isolation. CA #8 owns the release checks and live image replacement. Keep the Claim replacements as Drafts until the live mixed compiler is verified.

## Typed instance checks

- CA-R-3081@2-draft records the approved named, typed Python function passed as `instance_check`. The parser retains the function source and the linter checks its Model type without executing it.
- The separate evaluator binds the exact reviewed Claim digest and an Engine Model type. It checks the typed input and Boolean result. The legacy compiler rejects a Claim with an instance check until validation can apply it.
- The shared static parser reads typed Project and Scope Unit instance Claims. It preserves explicitly authored structural levels. An isolated copy kept all 42 Current Scope Units and their topology after replacing three structural Claims. The CA-R-2554 pilot accepted the authored root and child levels, rejected a wrong child level, and reported the missing parent level for FORMAL_MODEL_ENGINE. The Current Scope Unit carriers are unchanged.
- CA-R-3090@2-draft is the first native Scope Unit Declaration Draft. It preserves the Current Topic and structural fields and declares level 3. Its adoption requires the live reader and a declared level on its containing Scope Unit.
- The Formal Model Engine suite passed 37 tests. The Scope Unit reader suite passed 42 tests. CA #8's release rerun reduced the failing modules from 24 to seven. The live MCP still uses the prior image.

## Third native Draft batch

- MCP created CA-R-796@45-draft and CA-R-2170@13-draft. Both preserve the Current Topics and body outside the Claim fence. The CA-R-796 Topic was restored after the lifecycle writer normalized its address.
- All 104 staged native Claims bind and pass linting. Cutover preflight checked 101 predecessors with zero file or Version issues. Against the 102-Draft baseline, the two additional Claims preserve effective Workbench and Lifecycle rules and the Relation registry. The graph now exposes each authored endpoint separately.
- The source audit found 299 owner-verified Current and 67 owner-verified Draft CFEL carriers before this batch. The 104-Draft overlay covers 99 of those Current identities. The audit also found 30 provisional Current carriers without Container evidence.

## Optional Properties and the Scope Unit batch

- CA-R-2243@15-draft records that an explicit occurrence bound controls presence. A value bound applies to each present occurrence. The graph now applies the same rule to CFEL and Python Claims. All 183 graph tests passed.
- CA-R-2969@2-draft uses the explicit Operations and Step qualifiers with 0..1 occurrences and one Markdown value per occurrence. The combined preview changes the Mermaid Scheme rule only for Operations / Step. The original Topic is preserved. All 105 native Model Drafts bind and lint, and cutover preflight found no file or Version issues across 102 predecessors.
- Twenty additional Scope Unit Declaration Drafts name their direct parent in Header.Container. The parent is resolved from each Current formal topology Claim and pinned Scope Unit declarations. The live MCP created four. The checkout Lifecycle API created the other sixteen after live MCP returned backend errors.
- The existing CA-R-2640@2-draft now uses a typed Project Claim with ID CA-SU-00 and level 0. Its World Container remains CA-SU--1. With CA-R-3090@2-draft, the isolated overlay covers 22 native Scope Unit Declaration Drafts and preserves the topology and admissions of all 42 units. All 43 Current Scope source hashes match.
- Most Scope Unit levels still need explicit declarations. Legacy structural Claims in Scope Delegations remain under the coexistence rule. The five Delivery placement Claims have compatibility-bridge parity in the complete Core and Project Configuration snapshot. Their native Python representation remains open.

## Explicit Scope levels and Projection Forms

- All 22 native Scope Unit Drafts now declare a structural level. The levels are written explicitly from the pinned containment tree. The staged overlay preserves all 42 Scope Units and their admissions.
- CA-R-2554@3-draft expresses the structural-level rule as a named, typed instance check. The evaluator ran the exact Draft Claim against the staged tree. Fifteen units passed. Twenty lacked a declared level and seven lacked a declared Container level. A deliberately incorrect level was rejected. The Current rule remains in force while the remaining levels and the release integration are open.
- Nine Projection Form Drafts preserve the Current Form values, Topic addresses, and ancestry. Eight are new Drafts created through the checkout Lifecycle API after live MCP returned backend errors. CA-R-2743@3-draft retains the existing rule-origin Prose Claim and now uses a native Python Formal Claim.
- The separate 114-Draft preview preserves the effective schemas and Relation registry of the 105-Draft preview. All 114 Claims bind and lint, and preflight found no file or Version issues across 111 predecessors. CA #8 is continuing the live release gate for the 105-Draft batch.

## Cutover rehearsal and next Property Drafts

- The 105-Draft file rehearsal checked all 102 predecessor pins. Isolated Lifecycle promotion archived CA-R-3005@3 once and activated its four Decision replacements. The graph exposed all four Role-qualified Declarations and preserved the Relation registry.
- The same-ID CA-R-2502 rehearsal stopped before any write because the filesystem selector admitted two Plan evidence copies. The local indexed rehearsal requires DuckPGQ. CA #8 received the exact case for isolated image verification. Workbench passed its release gate modules, and the standalone-chat bridge failed. Live MCP still uses the previous image.
- Four later Property Drafts cover base Status and its order numbers, Context Headroom Fraction, Tier, and the legacy Operations Markdown field. MCP created CA-R-3052@3-draft. The checkout prepared and wrote CA-R-2696@4-draft, CA-R-2629@3-draft and CA-R-2706@3-draft using the exact Core source paths and hashes after MCP failed. The 118-Draft preview binds and lints every Claim. It preserves the effective schemas and registry of the 114-Draft preview. Keep the sealed 105-Draft release packet separate.
- Five native Delivery Claims passed all 32 mixed CFEL/Python combinations against the existing placement reducer. The native placement reader is still a rehearsal. The two existing Scope Unit split examples preserve topology. PROGRAMMATIC loses 13 effective Role/Form admissions when its legacy structural Claim is replaced by a prose-only Delegation, so the existing unit remains on its current arrangement.

Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/` in `wave6-properties/aggregate`, `wave6-cutover`, `wave6-delivery` and `wave6-scope-split`.


## Nested RMED Claim and indexed promotion

- CA-R-2722@5-draft preserves the RMED restriction on the nested Prose Claim Property. The checkout prepared and wrote the Draft from the pinned Current revision after live MCP returned a backend error. Live Workbench indexed the Draft. All 119 Model Drafts bind and lint. The effective schema and Relation registry match the 118-Draft preview.
- The retained-image indexed rehearsal selected an installed framework copy of CA-R-2502 and stopped before writes because the canonical Current destination was occupied. Resolve the selector's source authority and repeat the same-ID rehearsal before live promotion.
- The native placement reader matched eight Role folders and 30 placement bindings in 64 isolated cases. Three other Delivery Claims still need a native representation for delivery and field mappings. The placement reader and the sealed 105-Draft cutover use separate verification.
- The refreshed frontier found 299 owner-verified Current and 66 Draft CFEL carriers. It identified 180 Current carriers outside the 118 Model, 22 Scope Unit, and five staged Delivery selections before CA-R-2722 was added. Resolve provisional Container evidence, missing Scope Unit folders, and parse or identity errors before treating the census as complete.

## Scope Unit coexistence and typed Model batch

- The Operator approved temporary coexistence for the 19 existing Scope Units with combined Delegations. CA-R-3006@11-draft records the exception for exactly those units. CA-R-3006@10-draft retains the separate Role/Form proposal. The current promotion workflow requires consecutive revisions, so the v11 Draft needs a verified adoption route from Current v9.
- Created CA-R-3092@1-draft through CA-R-3110@1-draft as separate, parent-owned Scope Unit Declarations. All 19 are visible in live Workbench. The prior MCP allocated eight IDs already present in Git history. Those eight new Drafts were rekeyed with the checkout allocator. The 19 existing Delegations were checked byte-for-byte.
- The 41-Scope-Draft overlay preserves the topology and effective admissions of all 42 units. CA-R-2554's reviewed level check passes for 41 units. WORKBENCH_BURST_500_RENAMED still has no declared level. The wrong-level fixture is rejected.
- Five Model Drafts cover Event Record Action, the Concern and Plan Header groups, Named Selection, and Projection. All 124 Model Drafts bind and lint. Their effective schemas and Relation registry match the 119-Draft preview. The Named Selection and Projection views expose the declared zero-bearer rule.
- CA #8's indexed rehearsal promoted CA-R-2502 in a disposable copy. The canonical carrier became v6 and one v5 archive was created. Installed copies, Plan copies, and live files kept their hashes. The release gate is running on the rehearsed image.
- The prospective CA-R-2708 typed check agrees with SQL DISTINCT on 30 real string-array samples and eight fixtures. It reports malformed and legacy shapes explicitly. The live validator does not yet enforce this check.

The Scope verification is in `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave9-scope-coexistence/real-overlay-verification.json`. The Model preview is in `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave8-properties/aggregate`.

## Placement compiler and first live promotion

- The native placement reader is integrated into the checkout compiler and linter. The full mixed-source comparison preserved eight Role folders and 30 placement rules in 64 source-selection and source-order cases. The checkout compiler rejected five unsupported Python Claims. The five File Layout Drafts preserve the Current Topics and Claim behavior.
- CA-R-1608@24-draft preserves the Concern Status values and Resolved order number. Its compiled Status asset matches Current. The 125-Model-Draft and five-Delivery-Draft preview preserves the effective schemas and registry of the 124-Draft preview.
- CA #8's tested image passed 2,157 tests across 254 modules with four skips. The running container compiled the mixed declarations and exact CA-R-2969 Draft. The first live promotion consumed CA-R-2502@6-draft. The Current v6 and Archived v5 carrier hashes match the sealed preflight.
- The Operator assigned the benchmark Scope Unit to Workbench. CA #8 received the request to migrate only CA-R-930599129 at structural level 6 while preserving the 500 benchmark Atoms.
- Three five-way Role/Form splits have prepared bodies for Solution, Direct Policy and Approach Policy. The isolated graph and all 112 Role/Form admission cases match the existing rules. The candidate files await Draft publication.

The placement receipt is in `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave7-delivery/checkout-test-results.json`. The Role/Form proof is in `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave10-form-splits/proof.json`.

## First live cutover and next release

- All 105 sealed Claims are Current. Live Workbench found 105 canonical Python revisions. Carrier readback verified 102 archived predecessors, including the shared Decision predecessor. The Model graph bound all 105 Claims. Workbench, Role/Form, Header, Content and placement rules and the Relation registry match the sealed preview.
- The Operator approved the exact missing Container repairs on CA-R-2516 and CA-R-2685. Both were repaired and promoted. Their archives retain the previous Claims, Versions, Topics and Updated At values.
- Workbench published CA-R-930599129@3 with benchmark level 6 and archived v2. It verified all 500 corpus hashes. The 41-Scope-Draft overlay on that Current source passes the reviewed structural-level check for all 42 units.
- MCP created CA-R-3111@1-draft through CA-R-3125@1-draft. These give Solution, Direct Policy and Approach Policy one class per admitted Role. Live Workbench indexed all 15 Drafts. They preserve all 112 Role/Form admission results. The compiler records the three sets as qualified Forms.
- The next release packet pins 20 additional Model Drafts, the 15 Form Drafts and five Delivery Drafts. The actual post-cutover preview preserves the effective schemas and Relation registry. All 35 Model Claims bind without diagnostics. CA #8 received the exact release code and Claim pins for full release validation.
- Ordinary Lifecycle refuses to promote bound Scope Unit sources. A disposable Scope-specific rehearsal published all 41 Declarations and retained the existing topology, admissions and all 19 Delegation bytes. The root Project archive destination remains open. CA-R-3006's narrow transition also needs the Operator's selection of its publication route.

Live cutover evidence is in `.caprmedio_tmp/CA-P-3018/CA-P-3022/native-candidate/live-cutover-verification.json`. The next release and Scope publication receipts are in `wave12-next-release` and `wave14-scope-publication`.

## Next native Drafts and release rehearsal

- Created native Drafts CA-R-2559@3 and CA-R-2560@3 for MODEL and PROJECT STRUCTURE. The preview preserved effective schemas, narrowing edges, ancestry, the MODEL namespace, and both Container classifications.
- Created native Drafts CA-R-1654@39, CA-R-1660@38, CA-R-1022@33 and CA-R-2485@8 for four Relations. The combined 46-Draft preview preserved effective schemas, the Relation registry and all 112 Role/Form admissions. All 41 Model Claims bound in the graph without diagnostics. The four Relation entries expose endpoints omitted by the legacy view.
- The ordinary Lifecycle route promoted all 40 release Drafts in a disposable Project. All 28 predecessors kept their Claim, Version and Updated At in their archive carriers. The 40 successors kept their Draft Topics and Relations. Workbench passed the retained-image Claim checks. Both the candidate and the existing image exceeded the 45-second cold-start gate. The candidate became healthy after 69.6 seconds. Workbench is investigating source capture before rollout.
- Removed a unit test that depended on the local manifest for the already-consumed first Draft cohort. All 43 Formal Model Engine tests passed. The exact release Drafts have separate image and Lifecycle checks.
- An isolated Status compiler preserves the Plan Backlog Status Group and admits Analysis Done only for Analysis Report and Rationale. An isolated native format compiler resolves Named Selection from the selected class Declaration. The format catalog still needs standalone Workbench and incremental integration.
- Keep Subject notation and shared Model Relations and Formats during cutover. Retire Formal Claim grammar rules only after their remaining CFEL Claims and consumers have migrated.

Workbench rekeyed the benchmark Declaration to CA-R-3126@1 and preserved its Claim, Scope Unit ID and all 500 benchmark files. The Core Implementation Discrepancy Declaration became CA-R-3127@1, with the same Claim. Its predecessor CA-R-970308651@2 is archived.

Refreshed and verified CA-PROJ-028 and CA-PROJ-029 against Workbench results. The Main Subjects projection contains 931 values. The Dependencies projection contains 620 string values. CA-A-1185@4 and CA-E-672@3 each contain a legacy YAML mapping in the dependency list. The projection omits those two malformed entries. The source Atoms retain their original YAML.

The receipts are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/` in `wave16-model-roots`, `wave17-combined-preview`, `wave16-release-rehearsal`, `wave16-status-integration`, and `wave16-typed-format`. The rekey receipts are under `.caprmedio_tmp/wave12-retained-release.3gqytlhm/`.

## Scope transition and optimized release

- Published the Operator-approved 19-unit transition as Current CA-R-3006@12. Archived v9, consumed the narrow v11 Draft, and verified the exact bytes of the separate v10 permissions Draft. The receipt is `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave12-scope-transition/applied.json`.
- The refreshed 41-Draft Scope preview uses the rekeyed benchmark declaration. The topology and effective admissions match across all 42 Scope Units, all 19 Delegations match their source hashes, and all 42 pass the structural-level check. The manual publication and the root archive destination await the Operator's choice.
- The optimized Workbench image became healthy in 40.2 seconds against the 45-second gate. All 40 pinned Claims passed retained-image smoke, and all 46 passed ordinary promotion in a disposable Project. The full release suite and live replacement are still open.

## Published declaration requirements and compatible Relations

- Promoted CA-R-3081@2 and CA-R-3082@1. Both reviewed requirement bodies match their Drafts. Workbench confirms their Current Versions.
- Promoted CA-R-1022@33, CA-R-1654@39, CA-R-1660@38, and CA-R-2485@8. The running image's sealed compiler preserves their effective schemas and Relation registry. The four live Claims, Topics, Relations and predecessor archives match the verified carriers.
- Revalidated all 40 release pins and the effective schema preview after those publications. The full release gate passed cold start but reported two Workbench E2E failures. A 500-file move did not settle to the expected index state. A recently closed View could not load its cached result. Workbench continues diagnosis with the previous image in service.
- The next code preview combines native Status declarations, selected-class format binding, exact Runtime class resolution, and rejection of unknown declaration arguments. It passed 64 focused tests and parsed 208 native Claim blocks. The isolated Runtime overlay includes all four subtype edges and Session ancestry.
- The current authority scan found 195 Current and 66 Draft CFEL carriers with verified ownership, plus 27 provisional Current carriers. These counts include work awaiting adoption and exclude unresolved carrier evidence.

The verification and publication receipts are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/` in `wave18-declaration-requirements`, `wave18-live-runtime-compatibility`, `wave18-release-revalidated`, `wave18-next-integration`, and `wave18-frontier`.

## Scope Unit cutover

- The Operator approved manual publication and the Project-root archive destination. Published 22 replacements and 19 additional Scope Unit Declarations. The archived root Declaration is under the Project's `04_requirement/099_archived`.
- Readback verified all 41 Current carrier hashes and their exact paths in Workbench. The 42-unit tree retained its topology and effective admissions. All 42 declared levels satisfy the reviewed Claim. The 19 existing Delegations match their original hashes.
- CA #8 completed the eight real-project Workbench E2E tests before the Scope writes. The 40 release Claim pins still match. The isolated resource check and live rollout are separate checks.

The Scope publication receipt is `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave18-scope-publication/live-receipt.json`.

## Second live Claim cutover

- CA #8 deployed and verified image `sha256:9aab33310148e5d5d579e6fbe47b1198ef030fe1dd143f1e0190b5d358b06bd1`. The full gate ran 2,168 tests across 255 modules with four skips and zero failed modules.
- Published the 40 pinned Claims through Lifecycle. Workbench confirms all 40 exact Current paths and Versions. Readback verified each Claim body, Topic and Relation field, all 28 predecessor archives, and consumption of all 40 Draft carriers.
- The actual post-cutover compiler retained the effective Workbench, Header, Content and placement schemas, the Relation registry, and all 112 Role/Form admissions. The graph bound all 35 Model Claims without diagnostics.
- Workbench archive access was loaded for CORE_META_MODEL Requirements after the first Solution successor archived the shared predecessor. The remaining 14 Form Drafts then published through Lifecycle.

The live release and publication receipts are under `.caprmedio_tmp/wave12-retained-release.3gqytlhm/`, `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave18-release-readback/` and `wave19-live-release/`.

The two namespace Declarations CA-R-2559@3 and CA-R-2560@3 are Current. Created five additional Python Drafts for Format, Status, and the Named Selection source Property. Their exact Draft bodies match the pinned proposals.

The Operator requested two simple Topic projections. CA-PROJ-028 lists only the distinct Main Subjects. CA-PROJ-029 lists only the distinct Dependencies. Both use Current Workbench data and carry the Named Selection in their metadata. The verified outputs contain 944 Main Subjects and 620 Dependencies.

## Native Status and typed Model references

- Integrated native Status constraints and typed Model references, including exact class resolution in Workbench and the Model graph. The focused Formal Model Engine, graph, Lifecycle, and Workbench suites passed 328 tests.
- Verified seven Drafts against their Current predecessors. The effective schemas, Status rules, Relation registry, and graph edges match. Four format labels display as `str`. The graph also exposes the declared Status qualifications. CA #8 deployed image `sha256:bcb4cc17a3c70a6785b3c383836824d8d21637e812270362787dfcecdd7fc41d`. The full gate reported 2,182 tests across 261 modules, four skips and zero failed modules. Promoted all seven Claims and verified their exact Current paths, predecessor archives and post-cutover compiler and Model graph parity.
- Published all 16 Runtime, Run, and Recording Claims through live Lifecycle. Verified all 16 exact Current carriers, four exact predecessor archives, and all 20 authoritative paths and versions through Workbench. The graph shows three direct and three reverse execution endpoint pairs, and PRODUCES supplies the derived IS_PRODUCED_BY alias. CA #8 deployed image `sha256:0e96ee9abc59fa40cba7909054b4e192f5f32efe8652ff9e32081f4b16da04da` after 2,183 tests across 261 modules, four skips, and zero failed modules. The rerun updated only two test files; all Claim and generated asset pins matched.

The release preflight and input pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave20-next-release/`. The Runtime cohort pins and batch receipt are in `wave23-runtime-release/`.

## Topic projections

CA-PROJ-028 and CA-PROJ-029 were refreshed from the saved Workbench selections as two plain lists with no Atom Versions. Exact readback matches 959 distinct Main Subjects and 622 distinct Dependencies. The Dependency query filtered JSON elements by their original string type and excluded two mapping-shaped YAML entries in CA-A-1185 and CA-E-672. The Topic refresh receipt records them and the six legacy carriers with multiple Main Subjects under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave28-topics-refresh/`.

## Scope Unit operation checks

Hot-reload Current Scope Unit Declarations and Delegations as source data. Run the typed structural-level check only during operations on Scope Units, their Declarations or their Delegations. Use the latest declarations and the packaged, reviewed check. Keep generic Project loading, Workbench refresh and release gates outside this check.

CA-P-2480 owns the future Scope Unit operations. Its acceptance criteria record the fresh-source check and its operation boundary. CA-P-3022 owns the Python Claim, its static declaration and graph binding, and the typed check interface.

## Scope Unit Paths

The Operator chose `Scope Unit.Paths.Authority` and `Scope Unit.Paths.Delivery` for the two physical folder paths relative to the Project root. Workbench query 11ecf0f2b65147448c7c4eef619ce7d9 verified all three Current Declarations and the Current Delivery Policy. Current CA-R-3128, CA-R-3129 and CA-R-3130 declare the group and its two required string children. CA-D-667@5 assigns the existing folder derivations to the two Properties. CA-R-2689@4 derives ancestry from the declared containment Relations. CA-R-1688@41 preserves Atom identity under physical path changes, and CA-R-1730@41 describes the role of Scope Unit Labels.

Verified all seven Current carrier paths and versions through Workbench, four predecessor archives, and the three exact Property contracts in the live Model graph. All 42 Scope Units resolve repository-relative Authority and Delivery paths. The Project root resolves Authority to `.caprmedio_caprmedio` and Delivery to `.`. The folder existence check found nine missing Authority directories and 19 missing Delivery directories. Paths can resolve before the corresponding folders are materialized. CA-D-667@6 is Current and makes the verified Project root paths explicit in the Delivery Policy. Lifecycle archived version 5. Source bytes matched the promotion rehearsal, and Workbench query 1ac9c01ae28e4693aff0af74e3d847d3 verified the Current carrier. Current CA-R-970@33 removes its dependency on the singular Path Declaration and retains the Name uniqueness rule. Current CA-R-2689@5 preserves the rule that every ancestry representation derives from the declared containment chain. CA-R-2530@3-draft proposes a singular name-chain Path and is superseded by the two physical paths. Keep the singular Current Declaration until its remaining references have a disposition. Workbench confirmed CA-R-1661, CA-R-2655, CA-E-090, CA-E-128, the TOOLS root placement and 16 legacy tool placements are Current. Those tool folders have no declared Scope Units in the topology. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave23-scope-paths/`.

The confirmed Model shape is the plural group `Scope Unit.Paths` with `Authority` and `Delivery`. Workbench query 5e8984a7cd444acfae1a05e87a52f412 reverified the three Current Declarations and CA-D-667@6. The checkout resolved both repository-relative paths for all 42 Scope Units. For FRAMEWORK_ENGINE, Authority is `.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE` and Delivery is `LAYER_2_FRAMEWORK_ENGINE`. The Operator confirmed the plural group. Workbench query `44d9178e5bde4997b5bac9171482c02b` reverified the three Current Declarations and CA-D-667@6. The resolver returned both distinct Project-root-relative paths for all 42 Scope Units. Legacy consumers of the singular `Scope Unit.Path` still need to distinguish structural ancestry from physical placement.

CA-R-1677@36-draft checks ordered locations against the Scope Unit Declarations, their declared containment and order, and the folder derivation. CA-R-2655@4-draft updates the TOOLS Scope Delegation's reference from the singular Path to `Scope Unit.Paths`. Workbench query `cace4e7d3cc0417890f7ff3735cd3404` verified both Drafts. The 56 focused derivation and placement tests passed. A disposable rehearsal checked CA-R-1677 promotion and the archival of CA-R-1661@32 and CA-R-2530@2. The checked CA-R-2655 publication preserved effective structure for all 42 units, including the physical paths and admitted Role/Form pairs. Generic Lifecycle refused promotion of that bound Scope Delegation and archival of CA-R-2530@3-draft. The old Tool Delivery Atoms and the two Evaluations still need individual dispositions before the singular Path is retired. The receipt is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/scope-path-retirement/`.

Lifecycle published CA-R-1677@36 and archived CA-R-1661@32. Workbench query `7bed54421fe542cd8eefebe91ed99d82` verified both results, the CA-R-1677@35 archive, the three Current `Paths` Declarations, and the remaining CA-R-2530 Current and CA-R-2655 Draft.

## Next Scope and Step Claims

- Current CA-R-2523@4 declares the Scope Unit class in Python and retains the CFEL containment constraints, including the predefined world exception. Current CA-R-2736@2 uses the resulting Scope Unit class for Projection.Scope Unit. The seven compared consumer views retained their effective output.
- CA-R-3061 through CA-R-3064 are Current at version 3. Their Python declarations resolve the qualified Operations Step bearer while preserving the written Topics.
- Current CA-R-1021@34 declares the existing evidence_for Relation between Carrier instances. The Relation registry retained its effective output. The Model graph shows both declared Carrier endpoints.
- CA-R-2554@3 is Current. The selected callback is packaged in the live image and pinned in the checkout for explicit Scope Unit operations.

Workbench verified the three Current revisions and their three predecessor archives by exact path and Version. Current CA-R-2526@7 preserves one required string ID with zero dependents on Scope Unit and Project. The graph exposes the effective occurrence on each Entity through the Model declaration. The integrated graph and compiler changes passed 194 graph tests, 51 Formal Model Engine tests and seven callback checks. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/` in `wave23-frontier`, `wave22-step-properties`, `wave24-next-relations`, and `wave21-scope-callback/real-activation`.

## Step and Scope release rehearsal

The exact five-Claim Lifecycle rehearsal preserved bodies, Topics, five predecessor archives, Scope topology, generated schemas and the Relation registry. The isolated image graph bound all four Step Properties to Operations Step. Its packaged CA-R-2554@3 check passed for 42 Scope Units, rejected a changed ACTION_ENGINE level, and ran only at the explicit check boundary. CA #8 deployed image `sha256:0291bb20f981ea9beee0b8801f6a02d1bc2ea5da75fa9d39e1905e42e7b50cd4`. The unchanged full rerun passed 2,186 tests across 261 modules with four skips and zero failed modules after the first attempt missed a Docker bind-mount delete event. Workbench confirmed all five Current carriers and archives. The packet is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave24-step-scope-release/`.

Current CA-R-3082@2 defines paired Relation endpoint declarations. CA-R-2536@3, CA-R-2521@4, CA-R-2721@6 and CA-R-2710@3 are Current. Workbench verified their exact paths and four predecessor archives. The Model graph shows Journal, the qualified Action Execution Kind and Concern Priority, and the optional Markdown Formal Claim Property. CA-R-2733@3-draft is ready for a predecessor Container repair. Its Current carrier lacks that Header field.

## Scope Delegation Drafts

CA-R-3006@13-draft and CA-R-3008@9-draft align Model Role/Form admission with Scope Delegation Main Subject boundaries and retain the approved transition for 19 Scope Units. Workbench verified both Drafts.

A disposable 19-Delegation comparison removed only structure already stated by the separate Python Declarations. All 42 Scope Units retained their identity, containment, order, structural level and projected data. All 84 local Role/Form admissions remained. Seven Delegations can become prose-only. Generic Lifecycle promotion rejected bound Scope Unit sources, and the older CA-R-3034 Header needs a Topic mapping. Keep this group in the Scope migration until its publication path is verified. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave34-scope-delegation/`.

## Remaining CFEL boundary

The post-Wave-25 physical authority scan found 143 Current carriers and 49 Drafts with authored CFEL Formal Claim blocks. Of the Current carriers, 136 have matching Container evidence and seven remain provisional. The scan found no duplicate references. A byte-pinned follow-up checked all 43 parse or identity exceptions: 41 are supporting reports without frontmatter, and CA-D-487 and CA-D-488 have conflicting Topic aliases. None contains a CFEL fence. Nine declared Scope Unit directories are absent, with no alternate directory bearing those IDs. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave26-census/`.

The post-Wave-28 scan found 134 Current CFEL carriers and 49 CFEL Drafts. The Main Subject Relation and the four retired inverse Declarations account for the five Current carriers removed from the prior census. Seven Current carriers still lack Container evidence. The scan found no duplicate references. The updated manifest and exact source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave28-post-publication-frontier/`.

The post-Wave-29 scan found 133 Current CFEL carriers and 49 CFEL Drafts. Topic Dependencies left the Current CFEL inventory. The Python Plan blocking Draft and new CFEL Lookup Draft offset each other in the Draft count. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave29-post-publication-frontier/`.

Preserve the existing Topic grammar. CA-R-2487, CA-R-2471 and the Subject address Rules govern shared notation. Retire Claim-only syntax after its consumers migrate. Keep Model Format, cardinality, Relation and Property meanings as Model authority. Workbench and Lifecycle still use an internal statement adapter even when the authored Claim is Python.

CA-R-2721 keeps CFEL and supported Python admitted during migration. Current CA-R-2468@3 uses the language admitted by the Formal Claim Property for the Declaration Form. Its Current Python declaration preserves the fence requirement in prose and compiles the same optional field cardinality. The existing shared Content validator accepts unsupported fence labels. CA #8 has the separate enforcement finding.

The Current inverse declarations for NARROWER_THAN and INSTANCE_OF still supply Workbench reverse rows. The native compiler classifies their aliases differently. Keep the standalone declarations until a native cutover preserves reverse rows. The recursive Step and RUNS declarations need one coordinated migration. Historical and population rules require their existing typed Model inputs before native evaluation can be verified.

## Python Topic Dependencies

CA-R-2708@2-draft preserves the Main Subject, optional occurrence, string values and distinctness rule. The named typed Python predicate uses ordinary set equality by count. The Model graph projects the predicate and its declaring Atom. Candidate Schema compilation selects the Current Requirement Declaration by its canonical Main Subject and binds the reviewed Claim to the packaged predicate. It rejects conflicting declarations and verifies the selected source fingerprint. Lifecycle applies it to authored candidates and preserves the existing archive and Status-change behavior.

Workbench verified the Current and Draft rows. A 919-carrier rehearsal passed lint, preserved five effective static schema sections, and rejected duplicate Dependencies. The disposable Lifecycle promotion preserved the exact Claim and its predecessor archive. The Formal Model Engine, graph and focused Lifecycle suites passed 264 tests. Wave 29 passed 2,201 tests across 263 modules, with four skips and zero failed modules. The packaged Lifecycle check rejected duplicate Topic Dependencies on Create, Update and Promote and preserved prior values on Status change and Archive. CA-R-2708@2 is Current. The exact Current and predecessor archive hashes, consumed Draft and Model callback all matched. Workbench query 40a854850dbe434f99b1b486fc52fe11 verified both canonical rows and 42 Scope Units. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave29-topics-uniqueness/`.

## Python Plan blocking

CA-R-2762@3-draft preserves the existing Draft prose and declares a single directed instance pair from dependent Plan to prerequisite Plan, with BLOCKS as its derived reverse name. CA-R-1580@29 remains Current and retains its readiness semantics. Workbench verified both Current declarations and the Python Draft.

The disposable Lifecycle promotion preserved exact source and archive bytes. A 915-carrier compile preserved five effective static schema sections and the Relation registry. The graph projects the paired Plan endpoints with no new cardinality. Full and incremental Relation projections agree on the staged direct and reverse facts. Wave 30 passed 2,201 tests across 263 modules with four skips and zero failed modules. CA-R-2762@3 is Current and @2 is Archived. Exact source hashes matched the release packet. Workbench verified both revisions, the consumed Draft, CA-R-1580@29 and all 42 Scope Units. The live graph retained 1,057 direct facts and 1,057 matching reverse facts. Evidence is under `.caprmedio_tmp/wave30-retained-release/`.

## Python fallback rules

CA-R-2768@3-draft and CA-R-2770@3-draft record the Operator's later decision. Fallback returns an effective value and preserves the authored Property. Omission, null, and an empty string advance to the next source. Zero and false remain values subject to the declared Format. The contextual lookup keeps nearest-first containment and its ambiguity and cycle checks. These are Drafts. The shared Lifecycle and Workbench filename derivation now falls back to Form for omitted, null or empty Label. The explicit Label is preserved for nonempty values. The 16 Lifecycle placement and four Workbench placement audit tests passed. Workbench query 7b8cbf0d69764bc6a223a13f86e1b8b2 found zero empty Label rows in the queried data. CA-R-2705@5-draft expresses the same-bearer Label fallback. Workbench verified the Draft and a disposable promotion preserved its Topics and archive. The isolated combined graph with CA-R-2484 retained 842 nodes and 1,276 edges across 1,585 carriers, with the Label fallback replacing the unsupported-expression diagnostic. The Project and Plan threshold Claims remain in preparation.

## Canonical Relations and reverse aliases

CA-R-2485@9-draft and CA-R-2486@7-draft align HAS_INVERSE and the endpoint Rule with Current CA-R-2247 and CA-R-2951. One canonical Declaration supplies a reverse alias. A qualified derived Relation keeps its own Declaration. Endpoint permissions and bounds remain separately declared for each direction. Workbench verified both Drafts.

The four candidate predecessor inverse Declarations are CA-R-2418 (IS_CARRIED_BY), CA-R-2621 (HAS_PROPERTY), CA-R-2417 (HAS_EXECUTION), and CA-R-2421 (IS_RECORDED_BY). The disposable Lifecycle run promoted both policy Drafts and archived the four predecessors. It retained the five effective schema sections, all 42 Scope Units, the Relation registry, and four synthetic direct and four reverse tuples. The Model graph derives all four aliases from their canonical Declarations. CA #8 released the sealed Wave 28 image after 2,196 tests across 262 modules, four skips and zero failed modules. Lifecycle promoted CA-R-2485@9 and CA-R-2486@7 and archived the four standalone inverse Declarations. The source-byte check verified all seven Wave 28 archives and the Model graph still exposes all four derived aliases. Live Workbench query dc2b429e2fad40cab4ea4565e172f59e matched all 17 expected source rows and absences across 42 Scope Units. Workbench reverse-row parity used four staged pairs. The live data contained zero authored facts for those Relations. The next ordinary rebuild still needs to exclude the superseded installed and historical copies from compiler selection. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave28-inverses/`.

## Python Main Subject Relation

CA-R-2618@4-draft preserves the Current prose, including CFEL operator descriptors as admissible Subject targets. Its native declaration records a direct Relation from an Atom instance to a declared Model entity or instance. The exact Draft passed lint and a disposable Lifecycle promotion. An isolated rebuild reproduced all five Wave 27 baseline assets byte-for-byte. The candidate preserves their effective outputs and updates the source Version, fingerprint and dependent digests in the three assets that record this Relation. The rehearsal preserved the Relation registry, five effective schema sections, Scope Unit topology and the predecessor's body, Version and Updated At. CA-R-2618@4 is Current and its predecessor is Archived. Source-byte, Model graph and Workbench readbacks match the sealed Wave 28 packet. Evidence is under `.caprmedio_tmp/wave28-retained-release/clean-candidate/`.

## Python Header Container and Relations

CA-R-2779@2 is Current and preserves one Container occurrence with one child named atom or scope_unit. The effective Model rule covers the occurrence that the old Claim repeated in its instance clauses. CA-R-2709@6 is Current and preserves the optional Relations group, one or more child names when present, and one or more string values per child. The native declaration keeps these counts distinct. Current CA-R-3081@3 records the two parameters and their separate meanings. Workbench verified it and the archived @2 predecessor. The older CA-R-2709@2-draft remains historical Draft work.

Workbench verified both Draft carriers. Both passed a disposable Lifecycle promotion, exact archive checks, lint, and effective comparisons for five schema sections, the Relation registry, graph constraints and diagnostics, and all 42 Scope Units. The Formal Model Engine and graph suites passed 248 tests. CA #8 released the pinned image after 2,189 tests across 261 modules with four skips and zero failed modules. Both Claims were then promoted. Workbench and source readback verified both exact Current carriers, both predecessor archives and their effective Model graph contracts. CA #8 is also implementing the existing CA-R-2779 default for an omitted Container on the Project root Declaration. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave26-header-release/`.

## Python Atom Content and Header

CA-R-2498@7-draft preserves the recursive Markdown format and open child names for Atom.Content. Its three ordering relations apply only to Requirement, Method, Evaluation and Delivery. CA-R-2719@5-draft preserves the five Header child names and their four ordering relations. The graph recognizes both written directions of immediate sibling order and applies its Role scope to ordering contracts. Other Roles retain the same Content Property and inherited Markdown format.

Workbench verified both Drafts. Both passed lint and disposable Lifecycle promotion, preserving Topics, exact predecessor archives, five effective schema sections, the Relation registry and all 42 Scope Units. The Formal Model Engine and graph suites passed 250 tests. The pinned packet is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave27-content/`. The candidate image passed 2,196 tests across 262 modules, with four skips and zero failed modules. Staged Workbench and Lifecycle checks verified the root Container default for an omitted value. CA #8 verified the candidate image and live Workbench recovery. Lifecycle promoted CA-R-2498@7 and CA-R-2719@5 in one batch. Workbench query ebcdf706dd2048f6913fd47c3bc36afd verified the two canonical Current rows and their predecessor archives. Source-byte readback matched all four pinned hashes and the live Model graph preserved all seven scoped ordering pairs.

## Python Property ordering

Native declarations use `ordered_dependent_property_pairs` for immediate sibling adjacency. The Model graph retains the governing Atom and any Role selector on each pair. CA-R-3070@2, CA-R-3071@2 and CA-R-3072@2 are Current and preserve Header group order. CA-R-2500@8 is Current and preserves Prose Claim immediately before Formal Claim for RMED only. The live Model graph returns all nine expected pairs. Workbench and source-byte readback verified all four Current Claims and their predecessor archives. CA-R-3083@2 is Current and records the ordering interface. CA #8 released the image after 2,187 tests across 261 modules, with four skips, zero failed modules and all eight E2E checks passing. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave25-ordered-release/`.

The recursive Step audit found no Current Substep carriers in this Project. Existing placement only admits Step under Workflow or Substep under Step. The Model drafts, placement and Workflow consumer changes need one coordinated cutover before retiring Substep.

CA-R-2632@5 and CA-R-2687@2 are Current. The native Claims preserve both Authority Mode string children and both Scope Unit Order children. The Authority Modes patch preserved all 93 effective Property formats. CA #8 released the sealed Wave 31 image after 2,203 tests across 263 modules, with four skips and zero failed modules. The two Current predecessors received the rehearsed CA-SU-11 Container repair before Lifecycle promotion. Both Current and Archived source hashes matched the packet, both Drafts were consumed, and Workbench query aaf56f9974d748dc930569989645706a matched both Current and Archived paths, both consumed Drafts, and all 42 Scope Units. The Model graph readback passed. Evidence is under `.caprmedio_tmp/wave31-retained-release/`.

## Python Aspect declarations

CA-R-3056 through CA-R-3059 have Python Drafts for four concrete Aspects. The exact disposable promotions retained all 842 graph nodes and 1,276 semantic edges across 1,585 Current Requirement carriers. Each explicit INSTANCE_OF record points to its promoted source. A 956-carrier asset comparison preserved five effective schema sections, the Status model and the Relation registry. The Formal Model Engine and graph suites passed 260 tests. The release packet and both receipts are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave31-aspect-proof/`. CA #8 released the verified Wave 32 image after 2,207 tests across 263 modules, with four skips and zero failed modules. Lifecycle published all four Claims as Current version 4. Exact Current and archive hashes, consumed Drafts and Aspect graph provenance passed live readback. Workbench query 0f46cba1a5b9401fb389765751e86b80 independently matched all twelve rows and absences across 42 Scope Units.

The Wave 33 census found 123 Current and 49 Draft CFEL carriers. Five of the Current carriers have provisional Container evidence.

## Python Workflow Claim contract

CA-R-2961@2-draft preserves the required Claim, its zero direct values, the three allowed child names and the two ordering constraints. The prose Semantics still requires at least one of Prose Claim and Formal Claim. The linter verified the base against the inherited Atom.Content Declaration. The 1,585-carrier graph comparison preserved all four effective Claim constraints. A release-model overlay preserved all five effective schema sections. Workbench verified the Draft and its Current predecessor. A disposable Lifecycle promotion preserved the body and Topics and produced the expected archive. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave33-workflow-claim/`.

## Python Container classification

CA-R-2484@3-draft preserves the two admitted Container values, yes and no, and the existing prose. An isolated parser and graph patch projects both as allowed values and removes the two existing unsupported-expression diagnostics for this Claim. The 1,585-carrier comparison retained the other diagnostics, graph nodes and edges, the Relation registry, and the compared Workbench and Lifecycle schemas. Workbench verified the Current and Draft carriers. A disposable Lifecycle promotion preserved Topics and the predecessor archive. The code patch and pinned publication packet are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave33-structure/classification/`. The patch is integrated in the checkout with the Label fallback and linter changes. The combined Wave 33 packet holds all three exact promoted carriers, the reviewed code and the regression tests. The combined overlay preserved all five effective schema sections, the Status model and Relation registry. The checkout passed 283 focused tests across Formal Model Engine, graph, Lifecycle placement and Workbench placement audits. CA #8 released Wave 33 after 2,211 tests across 264 modules, with four skips and zero failed modules. CA-R-2961@2, CA-R-2484@3 and CA-R-2705@5 are Current. Live source and Model graph readback matched all three exact promoted carriers and predecessor archives. All three Drafts were consumed. Workbench query 8876290bb1cb4475a5dd2d34cf049655 independently matched all three Current carriers, three archives, the consumed Drafts and 42 Scope Units.

## Workflow Purpose and Engine Aspect hierarchy

The Workflow Purpose group has three Python Drafts. CA-R-2733@3-draft retains one string value. CA-R-2734@4-draft and CA-R-2735@4-draft retain Runtime and Project as the admitted values and preserve the Current prose. Both older v2 Drafts were left intact. Workbench verified the three Drafts. The graph comparison preserved 842 nodes and 1,276 edges, and the schema and Relation registry checks passed. The previous extractor did not recognize CA-R-2733’s qualified value-format expression. Its Python Claim supplies the corresponding Property contract. Three exact Container repairs and promotions passed in a disposable project. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave34-workflow-purpose/`.

CA-R-3022@4-draft preserves 47 authored structure paths and 71 explicit Aspect memberships as separate collections. Workbench verified the Draft. The disposable graph comparison retained all 71 formal source occurrences and the same graph facts and diagnostics across 1,585 Requirement carriers. The promotion preserved Topics and produced the expected predecessor archive. The isolated code patch and release pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave34-aspect-hierarchy/`. The combined exact four-carrier overlay retained 42 Scope Units, 842 nodes, 1,276 edges, the five effective schema sections, the Status model and the Relation registry. The final checkout passed 59 Formal Model Engine tests and 205 graph tests. CA #8 received both packets and the integrated code pins for Wave 34. CA #8 released Wave 34 after 2,212 tests across 265 modules, with four skips and zero failed modules. Lifecycle promoted all four Drafts after the three rehearsed Container repairs. The live verifier matched four Current sources, four predecessor archives, the four consumed Drafts and the Model graph. Workbench query cc134a86c9e445e090b50c7ad84c2900 independently matched all four Current carriers, their predecessor archives, the consumed Drafts and 42 Scope Units. The post-publication census found 119 Current and 49 Draft CFEL Claims.

## Python Projection ID dependencies

CA-R-2537@4-draft retains the Projection ID format, its cardinalities and both dependencies between ID and the pair of Form and Scope Unit. The isolated Python patch lints each referenced Property and projects two source-bound rules. Workbench and Lifecycle schema outputs, the Relation registry and unrelated graph contracts matched. A disposable promotion preserved the Draft body, Topics and predecessor archive. The patch represents the constraints for linting and projection. Historical population evaluation is outside this patch.

The MCP create request timed out behind an archive refresh, then finished. Its retry produced an identical v5 Draft. The original v4 was retained and the duplicate v5 carrier removed under the Lifecycle write lock, with exact bytes retained in scratch. After the Wave 34 restart, Workbench query 7aa01d0e311e4d8fb5dcf6a1b9613ff7 confirmed v4 and the absence of v5. Evidence and pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave35-population-rule/`.

CA-R-2499@7-draft preserves the existing Atom ID to Summary dependency across Current, Backlog and Archived Status Groups. CA-R-2564@5-draft retains the Project confidence threshold’s mandatory integer occurrence, inclusive bounds of 0 and 100, and effective fallback of 90. Workbench verified both Drafts, and disposable promotions preserved the Claims, Topics and predecessor archives.

The combined Wave 35 rehearsal used the exact three promoted carriers against the retained Wave 34 Model. The Relation registry and five effective schema sections matched. The complete Lifecycle candidate asset differed only in source provenance and derived digests. All eight code files match their reviewed hashes. The checkout passed 306 focused tests across the Formal Model Engine, graph, Lifecycle placement and Workbench placement audits. CA #8 received the packet for the sealed image and full release gate. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave35-summary-cohort/`.

The first Wave 35 full gate found a missing standalone test import path. The isolated threshold module passed both tests with PYTHONPATH unset after the fix. The eight updated file pins and test-only patch went to CA #8 for the full rerun. The initial sealed image passed the staged Model graph and Workbench readback.

## Python View and Workspace declarations

CA-R-2793@5-draft declares the View fields as a Python dataclass with explicit Property occurrence and value cardinalities. Workbench query c8124f35a3444e909043bbd7ed48652d confirmed Current version 4 and Draft version 5. An isolated compiler and graph comparison matched effective graph output and checked schemas across 1,585 Requirement carriers. All 69 Formal Model Engine and 205 graph tests passed. Disposable Lifecycle promotion retained both bodies, Topics and timestamps, produced the expected archive, and consumed only the staged Draft. Exact pins and source previews are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave36-view/`.

The Workspace rehearsal found that the graph extractor treated double-colon Relation cardinalities as endpoint text. The separate parser fix correctly extracts 14 authored Model Relation constraints, including Workspace containment, and 24 authored instance Relation constraints. The expanded audit pinned all 38 expressions to their exact source bytes and found only changes to endpoint selectors and cardinalities. The corrected graph retained nodes, edges, registry, diagnostics and checked schema sections. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave36-workspace/`.

Workbench query 0665bb5522234933bcb00d3e455b1482 confirmed both version 5 Drafts. Both exact disposable promotions preserved the new Claims and archived the exact predecessor bodies with unchanged timestamps. The 1,585-carrier comparison used the actual promoted preview bytes and preserved the six normalized constraints, carrying their new version and source digest. The integrated checkout passed 71 Formal Model Engine and 206 graph tests. All six new focused tests passed without PYTHONPATH. CA #8 received the pinned two-Claim packet for the next release.

Wave 36 passed 2,225 tests across 271 modules with four skips and zero failed modules. CA #8 verified the running image and the exact Current and Draft paths with Workbench query d38e4b16e9a14ca791049a112485df23. Lifecycle published CA-R-2792@5 and CA-R-2793@5 as Active. The live source verifier matched the Current and Archived bytes, both consumed Drafts and the Model graph. Evidence is under `.caprmedio_tmp/wave36-retained-release/`. Workbench query 656c3f6e9ef14a50b686c149fae74890 independently verified both version 5 Current carriers, both version 4 archives, the consumed Drafts and all 42 Scope Units. The refreshed authority scan found 114 Current CFEL Claims, including two provisional sources, and 46 Draft Claims. Its source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave36-post-publication-frontier/`.

## Plan Work Sequence Number

CA-R-2712@6-draft keeps the optional positive integer and the two direct-Container uniqueness rules for Active Plans. CA-R-997@35-draft aligns the old prose rule with the same scope. Workbench query 71be449e242b4c3d8a811cc88c32e1a5 confirmed both Drafts and the retained earlier CA-R-2712@3-draft. The isolated graph records preserve both key sets, the Active condition and the single-value checks. Both Drafts passed disposable Lifecycle promotion without errors or warnings. The archived bodies and the promoted Claims, Topics and timestamps match their pinned inputs. Runtime uniqueness evaluation was outside this proof. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave37-plan-sequence/`.

## Plan confidence fallback and Event Record ID

Workbench query 95e99f2164564df893d5171c51097af3 confirmed the Plan threshold Python Draft CA-R-2711@8 and the two existing authority Drafts CA-R-2768@3 and CA-R-2770@3. Together they retain nearest-first lookup, the Project fallback, the declared integer bounds and an effective value without a Carrier write. Undefined, null and empty string advance to the next source. Zero is retained. Nonempty values are validated against the declared Format. All three passed disposable Lifecycle promotion. The exact five-Claim overlay also includes CA-R-2712@6 and CA-R-997@35. Its linter, Relation registry, effective schema and inheritance checks passed. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave37-plan-sequence/rebased/`. Runtime Plan threshold resolution remains unverified.

Workbench query 140b07d0e91f462ca0db2106765bf889 confirmed CA-R-2558@3-draft. It preserves one required string ID and uniqueness across the Event Record population without Plan-specific filters. Its disposable Lifecycle promotion preserved the Claim, Topics, and exact predecessor body. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave37-event-id/`.

The combined six-Claim rehearsal used exact promoted bytes for the Event Record ID and the five Plan and fallback revisions. All five checked schema sections, the Relation registry, and inheritance diagnostics matched. The checkout passed 77 Formal Model Engine tests and 206 graph tests, including six new standalone cases. CA #8 received the pinned packet for release after the Workspace and View batch.

The corrected Wave 35 image passed the full gate with 2,219 tests across 268 modules, four skips and zero failed modules. The staged Model graph and staged Workbench readback passed on the same image. CA #8 deployed the image and verified live Workbench query 0520baea519f46ceafc6d3b0b3158f11 across all three Current and Draft paths and 42 Scope Units. Lifecycle promoted CA-R-2499@7, CA-R-2537@4 and CA-R-2564@5 with no warnings. All three Current and archive hashes matched, all three Drafts were consumed, and the pinned live Model graph verifier passed. Workbench query 1c29fb32861b498bba5f95f2044142e2 independently matched the three Current and three Archived revisions, all three consumed Drafts, and all 42 Scope Units. The authority census now has 116 Current and 49 Draft CFEL Claims, with two Current entries provisional. Evidence is in `.caprmedio_tmp/wave35-retained-release/` and `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave35-post-publication-frontier/`.

## Projection delivery Claim

CA-D-665@3-draft replaces the undeclared Markdown Carrier address with the declared `Carrier/File/Markdown` kind from CA-R-2456. CA-D-635 already binds Projection delivery to a Markdown File Carrier. The Python Claim passes the Model linter using the Current Delivery operator authority. Workbench query 0baac5a8c1254ec5ab626ca16542132c matched the exact Current and Draft paths, and a disposable promotion preserved the Claim, Topics and predecessor body. The graph extractor still reports the Delivery expression as unsupported. This proves the static declaration and source transition. The release and delivery behavior comparison remain open. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-delivery/`.

## CFEL Draft Form migration

MCP edited the existing CA-R-2954@1-draft, CA-R-2956@1-draft and CA-R-3023@1-draft in place. Each Python Claim reproduces both authored Role-qualified expressions and passes lint. The exact body and Draft Version checks passed. The existing graph diagnostics for those expressions remain. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-form-compat/`.

## Requirement Form identity

CA-R-2999@4-draft declares Requirement under the Requirement Role. It removes the legacy global constraint on the Form name so that a separate Role can declare its own Form with the same name. Workbench query 372fa04eb8104c48bcc4412077160211 verified the Draft. The graph resolved the qualified Form and its parent without a self-edge. Disposable Lifecycle promotion preserved the Draft body and Topics and archived the exact predecessor body. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-mechanical/requirement-form-correction/`.

CA-R-3075@2-draft declares Scope Unit Declaration under the Requirement Role and preserves its Scope Unit Main Subject target. The Python Claim exposes this instance Relation with source provenance. It uses the Role-qualified Topic and adds no Relation cardinality. Workbench query de8e1d87bf4e4512ab7675f9eb9c6ec0 verified the exact Draft. Disposable promotion retained the CA-R-3007 predecessor reference and preserved the version 1 Claim and Topic in its archive. A 1,585-Requirement graph rehearsal resolved the target to the qualified Form. The same-Form fixture for CA-R-2999 retains the Requirement pair, rejects an undeclared Method pair and admits it only when separately declared. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-scope-form/` and `wave38-mechanical/requirement-form-release/`.

The exact two-Form packet passed on the frozen Wave 37 overlay. The 1,585 Current Requirement carriers and 42 Scope Units retained the Relation registry and the Workbench and Lifecycle Header and Content compiler outputs. The Role/Form changes are limited to the two Requirement-qualified Forms. CA #8 received the source and archive pins together with the pilot response fix. Staged Workbench query 29110bf371c840028efb6083b44cc8f1 verified both exact candidate revisions and 42 Scope Units on the sealed Wave 38 image. The same image passed all five disposable MCP pilot scenarios, including recursive activation, partial and final failure, changed-definition rejection and Journal append failure. The full release gate passed 2,232 tests across 274 modules, with four skips and zero failed modules. CA #8 verified the running image and all 42 Scope Units through Workbench query 558c1aede5d341deb9032566198918ca. Workbench query fb58a5a5a5514292a23bd582ec3e1b9d verified the exact retained CA-R-3007@3 archive. Lifecycle promoted CA-R-2999@4 and CA-R-3075@2 to Active without warnings. The live source verifier matched both Current and archive hashes, the consumed Drafts and the Model graph. Workbench query 3db81ceba7c94373abbed9bcd9806801 independently verified the two Current paths, both archives, zero remaining Draft rows and all 42 Scope Units. The refreshed authority scan found 109 Current CFEL Claims, including two provisional sources, and 44 Draft Claims. Source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-post-publication-frontier/`. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-form-packet/`.

The disposable Scope Delegation check preserved all 42 Scope Units with seven prose-only candidate Claims. Generic Lifecycle blocked six bound-source promotions and rejected the older CA-R-3034 Header. Two negative controls showed that the reader accepts a missing Delegation and ignores an unresolved prose Main Subject endpoint. The transition must preserve the existing Main Subject boundaries and verify one or more Delegations per non-Project Scope Unit before the temporary coexistence rule can be retired. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-scope-split/`.

The Tier Label proof verified the four mappings and omitted labels with typed fixture data. Current YAML carries Tier as an integer and cannot encode a nested Label at that same key. A Model binding decision is pending. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-tier-label/`.

## Python Format Claims

Workbench query 9649c95e5a8041aa94e28d1be85fdf27 verified the eight Python Drafts: CA-R-2249 through CA-R-2254 at version 8, CA-R-2257 at version 7 and CA-R-2547 at version 5. They preserve the Topics, prose and grouped Claim statements. The 745-carrier Model comparison matched the narrowing graph, Relation registry and five effective schema sections. All eight disposable promotions preserved the Draft Claim and Topic and archived the exact predecessor body. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave39-formats/`. CA-R-2248 retains its competing Draft and its unresolved Markdown Format wording.

## Python named instance references

Workbench query 82022318d7a24f06b7bf0b9559efd129 verified CA-R-2277@5-draft for Extension Sources and CA-R-2775@4-draft for Visual Design. The existing Python helpers reproduce the exact grouped statements and preserve both Topics, prose, graph facts and diagnostics. The linter resolved the named instances using the source-bound Subject graph as well as the Model contract catalogue. Extension Sources retains its existing unsupported-expression diagnostic. Both disposable promotions preserved the Draft Claims and predecessor archives. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-named-instances/`.

## Wave 37 live publication

The retained image passed 2,231 tests across 274 modules, with four skips and zero failed modules. Live Workbench query ff50206ca7bb4028b80d33dd0e8a0b44 confirmed the exact six Current and Draft sources and all 42 Scope Units. Lifecycle published the six revisions with zero errors and warnings. The frozen-source verifier matched all six Current and Archived hashes, confirmed all six Drafts were consumed, and reran the Model graph proof. Workbench query 691c5789c81045c791d858d53ff32ef2 independently matched all six Current paths, six exact predecessor Archives, the consumed Drafts and all 42 Scope Units. The Plan threshold and population Claims were verified for linter and projection behavior. Autonomous Plan execution remains outside this static verification. Evidence is under `.caprmedio_tmp/wave37-retained-release/`. The refreshed authority scan found 111 Current CFEL Claims, including two provisional sources, and 44 Draft Claims. Exact source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave37-post-publication-frontier/`.

## Operator symbol extraction

The Model graph recognizes a symbol assignment when the Formal Claim names the same CFEL Operator as the Atom's Main Subject. The check handles escaped text and rejects malformed literals and mismatched Topics. All 28 pinned Current sources yielded the same symbol through the CFEL and Python paths. The graph suite passed 207 tests. CA #8 received the two-file patch and exact hashes for the next release after Wave 38. The linter still takes a supplied operator catalogue. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave39-operators/`.

Workbench query 29d83a88d927424287a3f1edd7bb2116 verified 22 Python Operator Drafts. Each preserved the written Topic, exact compiled statement, decoded symbol, Semantics and other Claim content. All 22 passed disposable Lifecycle promotion and exact archive checks. Publication pins are in `wave39-operators/publication-pins.json`. Delivery, Instance Binding, Narrowing, Alias, Lookup and Allowed Value remain outside this packet while their Draft, consumer or authority issues are resolved. The post-release graph comparison pinned exactly 28 newly recognized symbols across 1,585 Current Requirement carriers.

## Term, inverse and language Claims

Workbench query 6cc3b38b467a4f6ea8e059772b9d613b verified CA-R-1318@38, CA-R-2483@7, CA-R-2616@3, CA-R-2619@3, CA-R-2620@3, CA-R-2771@3 and CA-R-2772@3 as Drafts. The first five use Python helpers and retain the exact compiled statements, including both reverse Relation views. The other two already state their full range and intersection rules in prose. Their CFEL grammar examples use placeholder names and counts, so they now appear as text in Details. The graph retains the same constraints and drops the two unsupported-example diagnostics. All seven Drafts passed disposable promotion, including exact Topics, predecessor bodies and archive hashes. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave41-language/`. The two direct Relation Claims and their competing Drafts remain open.

CA-R-2581@3-draft retains the required Event Record Relations group and immediate Relation-name constraint. Workbench query f1df04da501a4745be41da559aabc10c verified it. The Claim lints, reproduces both grouped statements, and matches the checked graph and schema consumers. Disposable promotion preserved its Topic and predecessor body. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave41-event-relations/`.

## Summary invariant in Direct Update

The disposable Lifecycle backend originally permitted a Current or Archived Summary edit that made another published revision of the same ID disagree. The Direct Update path now reads the other published revisions of that ID before changing the Summary. Draft revisions stay outside the check. Current edits with only a Draft sibling and isolated Archived edits still succeed. Missing Archive coverage returns the existing Archive load error before any effects. The indexed route used Workbench for source selection; the unbound route used the declared source inventory. The guard runs under the existing project write lock. All 206 Lifecycle tests passed. The patch and source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave41-summary-runtime/` and were sent to CA #8. Release verification is pending.

## Whole-Carrier Delivery and reverse Relations

Workbench query c6c5dff927544e79af122a77dff740c5 verified CA-D-662@7, CA-D-664@9, CA-R-2469@5 and CA-R-2767@3 as Drafts. The Delivery Claims use whole-Carrier bindings. Their existing YAML, Markdown and destination mappings are stated in prose. The scratch renderer produced the expected YAML destination and Markdown body. The two Requirement Claims reproduce the exact grouped statements. Workbench registry and reverse facts matched on two pinned Current Method sources; the incremental reverse-edge fixture passed. All four disposable promotions preserved Topics and predecessor bodies. The whole-Carrier and Relation packets remain Draft. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave41-delivery/` and `wave41-more-relations/`.

## Existing derived Relation Drafts

CA-R-2761@1-draft and CA-R-2421@6-draft now use Python Formal Claims with the same Derived classification and inverse direction. Workbench query 462c0a41cd5649f1b7a47cb14cb073ca verified both existing Draft references and the Python fences. Their exact bodies match the rehearsed candidates. A disposable comparison preserved the narrowing graph, Relation registry and five effective schema sections. Both revisions remain Draft. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave42-draft-cohort/`.

Workbench query 951b18381ace4ab4b20b1db7b9ce6a26 verified CA-R-2247@14-draft. The Python Claim compiles to the same model and instance constraints as Current v13. The graph, Relation registry and five schema consumers matched in rehearsal. The separate v12 Draft retained its original bytes. Disposable Lifecycle promotion verified the exact v14 Claim and v13 archive. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave42-relation-atom/`.

## Python Claim lint through the internal query API

The Formal Model Engine can lint an exact Atom reference through the internal API behind `query_run`. It pages the Current Declaration inventory, binds each result to a source carrier, and checks Python syntax, Model references, Relations and declared notation without executing the Claim. A disposable Workbench integration verified pagination, syntax diagnostics, declared notation, missing or ambiguous references, exclusion of Drafts and installed copies as authority, and rejection when the indexed Declaration inventory changes during the read. The API is verified in the checkout.

## Wave 39 live publication

The retained image passed 2,233 tests across 274 modules, with four skips and zero failed modules. CA #8 verified the running image and all ten exact Current and Draft paths through Workbench query ab580db2a099493dbfa0360bc88207f6. Lifecycle published all ten Drafts as Active with zero errors or warnings. The frozen verifier matched ten Current carriers and ten predecessor archives by exact bytes, confirmed consumption of all ten Drafts, and checked the Model graph including 28 Operator symbol records. Evidence is under `.caprmedio_tmp/wave39-retained-release/`. The refreshed source census found 99 Current CFEL Claims, including two with provisional ownership evidence, and 42 Draft CFEL Claims. Source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave39-post-publication-frontier/`.

Independent Workbench query e126ede773d247a98ae3a9492d8c93ef matched the Current and Archived carriers, absent consumed Drafts, and all 42 Scope Units after publication.

## Format, Cardinality and derived Relation Claims

Workbench query 24377d468fe34e71bcccbdc935935c18 verified the Python Drafts CA-R-2248@7, CA-R-2327@7, CA-R-1580@30 and CA-R-2623@5. Their compiled expressions, extracted constraints, Relation registry, Model graph and five schema consumers match the Current Claims. The graph records the new Python fences. The older CA-R-2248@6 and CA-R-2327@2 Draft carriers match their original bytes.

Disposable Lifecycle promotion passed for CA-R-2327@7, CA-R-1580@30 and CA-R-2623@5. Their exact outputs join CA-R-2247@14 in the next Claim packet supplied to CA #8. CA-R-2248@7 remains outside that packet because the current Action expects its immediate preceding Version, v6, and Current is v5. The competing v6 Draft proposes a different Form and Topic. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave43-claim-packet/` and `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave43-format-cardinality/`.

CA-R-1432 and CA-O-10005 currently retain the Version assigned to a same-ID Draft. CA-O-10003 assumes the same promotion behavior. This differs from the requested promotion rule to assign one more than the maximum existing Version for the Atom ID. With Current v5 and Drafts v6 and v7, that rule would archive v5 and publish the selected v7 content at v8. Resolve the governing Claims and update the Lifecycle route before applying that rule. Both Format Drafts remain available.

CA-R-1432@31-draft records the promotion Version rule. Workbench query 69ab17a3c85744b58df3d268b1cfef2f verified the new Draft and the retained Current v30 and Draft v28. The Action Clauses and Updated At treatment still need alignment before publication.

The Projection renderer published a Markdown Projection from both the Current CA-D-665 carrier and the rehearsed Python revision in disposable Projects. The output path, filename, YAML identity and exact source reference matched each run's inputs. The renderer does not interpret the Delivery expression. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave38-delivery/renderer-readback.json`.

## Wave 40 live publication

CA #8 deployed the exact image that passed 2,233 tests across 274 modules, with four skips and zero failed modules. Workbench query 822ec13db8a843cf80bdec0e61512e55 matched all 44 Current and Draft rows and 42 Scope Units before publication. Lifecycle promoted all 22 Operator Drafts with zero errors and warnings. The frozen verifier matched the 22 Current and 22 Archived carriers by exact bytes, confirmed consumption of the 22 Drafts, and verified the graph. Evidence is under `.caprmedio_tmp/wave40-retained-release/`. The refreshed census found 77 Current CFEL Claims, including two with provisional ownership evidence, and 42 Draft CFEL Claims. Source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave40-post-publication-frontier/`.

Independent Workbench query c0defe444ba2467988b125121a7ab571 matched all 22 Current carriers, 22 predecessor archives and 42 Scope Units. It found zero rows for the consumed Drafts.

Workbench query c9c727eefd3745ddbe480cce9e89c8df verified the Python Claim in the existing CA-R-2420@6-draft. The converted Claim retains the derived inverse and Execution-to-Runtime signature. Graph extraction differs only in the Python fence and whitespace in the rendered instance expression. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave43-draft-inverse/`.

## Qualified Workflow references

The project-backed Claim linter uses the declared Model graph to resolve qualified paths, unique short names, and inherited Property addresses. A disposable Workbench fixture resolves Operations Workflow and Step, checks an inherited Property, and rejects a Workflow under the wrong Role.

Workbench query 2698d575197f40ad9a58fce6ad810ccb verified CA-R-2464@9-draft and the retained v6 Draft. The Python Claim matches the extracted constraints, diagnostics, Relation registry and five schema consumers. The rendered graph records the new fence and spaces in two Relation expressions. The Current v8 carrier lacks a Container. A disposable rehearsal succeeded after adding only `container.scope_unit: CA-SU-11` to v8. The live v8 carrier remains unmodified.

Workbench query 9fe3ca1fd605471380537caff9baf13c verified the conversion of the existing CA-R-2417@6-draft to Python. Its rendered expressions, extracted constraints, diagnostics, Relation registry and five schema consumers match the previous Draft. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave44-qualified-workflow/`.

The qualifier check requires the named Property to be declared. For inherited Properties, it uses the most specific applicable declaration and rejects unrelated competing origins. The updated checkout passed 78 Formal Model Engine tests and 14 linter tests. CA #8 verified the pinned four-file patch for a release after Wave 43.

## Wave 41 live publication

CA #8 deployed the exact image that passed 2,234 tests across 274 modules with four skips and zero failures. The staged Summary guard fixture rejected conflicting published Summaries and accepted Draft edits. Live Workbench query 1b0262d448ff4108abe338192a4cb494 matched the 16 exact Current and Draft paths and all 42 Scope Units. Lifecycle published eight Python Claims as Active with zero errors or warnings. The frozen verifier matched all eight Current carriers and predecessor archives, Draft consumption and the Model graph. Evidence is under `.caprmedio_tmp/wave41-retained-release/`. The refreshed census found 69 Current CFEL Claims, including two with provisional ownership, and 40 Draft CFEL Claims. Source pins are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave41-post-publication-frontier/`.

Independent Workbench query 40b2eaec8aea4f8dabb8148c4713ae8b matched all eight Current carriers, eight exact archives, both retired paths, zero consumed Draft rows and all 42 Scope Units. CA #8 began Wave 42 from that receipt.

## Remaining Operator Claims

Workbench query bbcc5865435f45bca1053613009d74e1 verified six Python Drafts for Delivery, Instance Binding, Narrowing, Alias, Lookup and Allowed Value. The current symbols, prose, grouped expressions, extracted records, registry and five schema consumers match the converted Claims. The graph records the new fences. Prior CA-R-2604@4 and CA-R-2720@2 Drafts match their original bytes.

Disposable promotion passed for CA-R-2596@2, CA-R-2610@2, CA-R-2720@4, CA-R-2770@4 and CA-R-3069@2. The CA-R-3069 rehearsal preserved its already Archived replacement target CA-R-2592@1. CA-R-2604@5 remains Draft because promotion requires an immediate preceding Current Version and v4 is a competing Draft. CA #8 received the five-Claim packet for a later release. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave44-remaining-operators/`.

## Scope Delegations without admission rules

A disposable Project retained all 42 Scope Units and their effective admissions after removing the duplicate structural Claims from seven Scope Delegations. The separate Python Scope Unit Declarations supply those facts. The Delegation prose remains intact. Twelve other Delegations still carry Role/Form admission policy in their Formal Claims. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave44-prose-delegations/`.

## Atom Declaration

CA-R-2508@13-draft preserves the Current Atom Declaration’s grouped expressions, extracted graph, Relation registry and five compiler assets in Python. Workbench query `658e78c3dda44663aa30c78860619c5c` verified the Draft and the retained v7 Draft. Disposable promotion matched the exact Current and archive output hashes. CA #8 received the candidate for a release after Wave 43. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave44-atom-core/`.

## Wave 42 live publication

The exact live image passed 2,235 tests across 274 modules with four skips and zero failed modules. Workbench query `1831a539718a4740aba9eb6ecad3a61a` matched all eight Current and Draft inputs and all 42 Scope Units. Lifecycle promoted CA-D-662@7, CA-D-664@9, CA-R-2469@5 and CA-R-2767@3 with zero errors and warnings. The frozen verifier matched their four Current and four archive source hashes, consumed Drafts, and the Model graph. Archive-inclusive Workbench query `aab5969a5a7d4aaba2e8852b71b618b1` matched all four Current carriers, four Archives, four consumed Draft absences, and 42 Scope Units. CA #8 began the Wave 43 release. Evidence is under `.caprmedio_tmp/wave42-retained-release/`.

## Post-Wave 42 remaining Claims

The source census found 63 confirmed Current CFEL Claims, two Current Claims with unresolved Container evidence, and 40 CFEL Drafts. It scanned declared Authority paths and matched the Scope Unit source digest. The census and exceptions are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave42-post-publication-frontier/`.

MCP created all seven prose-only Scope Delegation Drafts. Workbench query `9820157ba83844238009542c9ee26d65` matched the exact Draft paths and Versions. Source readback matched each rehearsed prose body and the original Subject and Container. The CA-R-3034 Draft maps its legacy active Subject to Topics with the same address. Standard promotion rejected the seven bound sources. The Scope-specific rehearsal matched all 42 units’ topology, normalized ownership and admissions, all seven archive and Current destinations, and rollback after an injected failure. The bounded contract graph retained its narrowing, Relation and component sections. It dropped the seven CFEL blocks and their unsupported diagnostics. The manual publication is pending approval.

CA-R-1788@21-draft and CA-R-1432@31-draft align Updated At with accepted business updates, including promotion, and retain preservation for archives and Carrier-only changes. Workbench query `bffdf4aa9e0d47818e337eeb784c712c` matched both Drafts and both Current predecessors. Lifecycle Actions and Event Record consumers still need coordinated verification before publication.

## Relation alias syntax

The static Python Claim reader now checks the exact declared Relation name in alias assignments and preserves the rendered alias token. It rejects malformed addresses and missing or empty aliases. Fifteen linter tests, six parser tests and 42 graph tests passed. CA #8 received the pinned patch for a release after Wave 44.

CA-R-2617@4-draft preserves the Current CONTAINS inverse and alias, its extracted constraints, five schema consumers and the Relation registry. Only the Formal Claim fence changes in the graph. Workbench query `c679f992794a40839dc22dd033a8855d` verified the Current and both Drafts. Standard promotion rejected v4 because the separate v3 Draft is not Current. Evidence is under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave45-containment-alias/`.

Removing CA-R-2420 from a disposable comparison kept the runtime EXECUTES inverse, reverse links, registry and all five schema outputs. The Contract graph lost the standalone IS_EXECUTED_BY Relation entry and instead listed it as a derived alias of EXECUTES. Keep the Current carrier until the expected graph representation is settled.

## Wave 43 live publication

The exact deployed image passed 2,236 tests across 275 modules with four skips and zero failed modules. Workbench query `07aa90cd0d2247c4847c212c808b8568` matched ten Current and Draft rows, including the two older Drafts, and all 42 Scope Units. Lifecycle promoted CA-R-1580@30, CA-R-2247@14, CA-R-2327@7 and CA-R-2623@5 with zero errors or warnings. The frozen live verifier matched all four Current and Archive source hashes, consumed Drafts and the Model graph. Both older Drafts still match their pinned bytes. The refreshed source census found 59 confirmed Current CFEL Claims, two with unresolved Container evidence, and 40 CFEL Drafts. Archive-inclusive Workbench query `7b67c15fab434e3d85cfcecf7b6649a8` matched all 16 expected Current, Archive, Draft and absence rows across 42 Scope Units. CA #8 began Wave 44. Evidence is under `.caprmedio_tmp/wave43-retained-release/` and `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave43-post-publication-frontier/`.

## Header Draft conversions

CA-R-2709@2-draft and CA-R-2719@2-draft now use Python Formal Claims. The converted Claims preserve the Relations Property and the Header groups and order. Their Topics, Containers, Draft Status and Versions matched the original carriers. Workbench query `380ebd02eaf74408b1cbb6a471f90cbf` verified both Drafts and their Current counterparts. The disposable comparisons matched the normalized graph, Relation registry and five schema consumers. Original Draft bytes and proofs are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/wave46-header-draft-proof/`.

## Promotion Version implementation

A disposable Lifecycle overlay allocates one above the highest Version for the same ID, including competing Drafts and unloaded Archive reservations. The indexed example with Current 7, selected Draft 6 and competing Draft 8 published Version 9. An Archived-only ID at Version 5 resumes at 6 if Summary and Role match. A genuinely new ID starts at Version 1. Exact no-op promotion retains the Current Version. Standalone and composed promotion reject changed archive bytes and report completed effects. The existing 206 Lifecycle tests and ten independent promotion tests passed against the final overlay and its fixture changes. Source-pinned Action body candidates and the overlay are under `.caprmedio_tmp/CA-P-3018/CA-P-3022/promotion-version/`. This version change awaits coordinated Action and runtime release. Event Record and Updated At integration remains separate.

## Relation signatures and narrowing paths

The integrated checkout linter accepts a generic endpoint only in the signature of the registered Relation named by the selected Requirement Declaration. It also resolves a unique, source-bound direct narrowing path to the existing Model identity. Nine focused tests and 22 existing parser and Project lint tests passed. CA-R-1498, CA-R-2475 and CA-R-2476 reproduce their Current graph constraints, schema and registry outputs. CA-R-2732 still needs its qualified target resolved. CA-R-2524@4-draft now uses Python with the graph-derived Scope Unit/Project binding. Lifecycle created CA-R-1498@19-draft, and the disposable promotion matched its predecessor archive, formal body and Topics. Workbench query `5618ec469d7e444c92d1f89c6737a3a0` matched both Drafts and their Current counterparts. CA #8 received the pinned next release.

## Wave 44 live publication

The exact deployed image passed 2,240 tests across 275 modules with four skips and zero failures. Workbench query `91dc23c9e9094193a63f1e0e7bedcd9d` matched all 14 pre-promotion Current and Draft rows. Query `4c01c5a0b24c487193f23eecbfdbc715` matched both required Archive inputs. Lifecycle promoted CA-R-2596@2, CA-R-2610@2, CA-R-2720@4, CA-R-2770@4, CA-R-3069@2 and CA-R-2508@13 without warnings. The exact verifier matched six Current and archive pairs, consumed Drafts and the Model graph. Six retained Drafts and both existing Archive inputs matched their original hashes. Independent Workbench query `c9987647a3214a9fa7d83f7d89c3eca5` matched all 21 publication expectations across 42 Scope Units.

## Wave 46 publication

CA #8 deployed the exact retained image with the two linter changes. The gate ran 2,241 tests in 275 modules, with four skips and zero failures. Workbench query `57c9922f0a5848569d007c79bc0dd293` matched the Current and Draft source pins and all 42 Scope Units before promotion. Lifecycle promoted CA-R-1498@19 and archived @18. The resulting carriers matched their staged bytes. The Model graph and six compiler outputs matched the staged expectations using a disposable copy with original staged bytes for three historical Drafts that were converted independently. The live Drafts were verified separately. Release evidence is under `.caprmedio_tmp/wave46-retained-release/`.

Independent Workbench query `590c0f118f8b49aeb05a41f12e036397` matched the four publication checks across all 42 Scope Units.

Lifecycle created CA-O-10003@2-draft and CA-O-10005@2-draft for the promotion Version change. Workbench query `cace4e7d3cc0417890f7ff3735cd3404` and source readback matched both Drafts and their pinned bodies. The Operator confirmed first publication from Draft @1 uses Version 1 even when another Draft @2 exists for the same unpublished ID. The focused test passed against the existing promotion overlay and verified Draft @2 byte-for-byte.

Lifecycle converted CA-R-2247@12-draft, CA-R-2604@4-draft and CA-R-2720@2-draft to Python. The Drafts keep their individual semantics, including differences from Current. Lifecycle also synchronized their stored destination filenames with the existing carrier filenames. Workbench query `cdb62c7c16464b36916ac2aced52055c` verified the three exact Draft references. The pinned comparison checked strict lint, generated statements, effective graph and five schema outputs.

Lifecycle created CA-R-2475@7-draft and CA-R-2476@8-draft with Python Claims that reproduce the respective Current signatures and constraints. Their earlier competing Drafts remain available. The existing promotion gate requires the consecutive predecessor, so publication awaits the promotion Version cutover or another approved publication route.

## Qualified declaring Relation

Lifecycle created CA-R-2732@3-draft with the existing Requirement Form selection translated to Python. The linter resolves each admitted Form against the Current Model and permits the union as the target of the matching `IS_DECLARED_BY` signature. A bound target can be referenced again. The Current graph, Relation registry and five schema outputs matched the staged Claim. Twenty-two parser and Workbench tests and eight focused selector tests passed. Workbench query `a60f3223ce36492ba218e22b9728e590` verified Current @2 and Draft @3. The promotion rehearsal pinned the successor and its archive. CA #8 received the three code and test pins and the exact Draft packet.

CA-R-2478@7-draft translates the Current containment Relation while retaining its inverse alias and written notation. The registry, five schemas and all 41 declared Scope containment links matched. The earlier CA-R-2478@6-draft and CA-R-2617@3-draft retained their exact bytes.

CA-R-2420@7-draft preserves the Current `IS_EXECUTED_BY` inverse and its written reverse direction. Extracted constraints, diagnostics, the registry and five schema outputs matched. Workbench query `6a21aec335534c8f87098f382f4cd313` and source readback verified the new Draft and the separately preserved CA-R-2420@6-draft.

Lifecycle converted the Formal Claims of CA-R-2734@2-draft, CA-R-2735@2-draft and CA-R-2777@1-draft in place. The three Drafts retained their parsed statements and graph-backed Subject bindings. Workbench query `9858c17d21484b38af27dd764e1356c4` and source readback verified the Drafts. Lifecycle synchronized the stored destination filenames. CA-R-2777 still overlaps the Current AllowedValue Declaration and remains a Draft.

## Promotion Version authority

Lifecycle created CA-R-1432@32-draft with the approved promotion Version rule and preserved the separate CA-R-1432@31-draft and its Updated At work. CA-E-491@27-draft and CA-E-521@23-draft revise the Version expectations. Workbench query `c942144ef0214e7995ab12ef94acc532` and source readback verified the Drafts. CA-O-051@21 still has the old Version rule. Lifecycle refused to create its Draft because the existing Action has a legacy Summary heading. The staged Action body and the open sealed-Draft route audit are tracked separately from the live release.

CA-R-869@25, CA-O-066@15 and CA-O-030@35 still describe sealed admission with predecessor-plus-one or carried Draft Versions. CA-D-425@30 and CA-D-659@3 still describe the corresponding bindings. The live Engine registry exposes the ordinary Lifecycle provider. It has no dispatch for `ATOM_PROMOTE` or the named legacy update route. The older Claims remain Current authority and need disposition before the general Version cutover.

Created CA-O-051@22-draft directly from the disposable Lifecycle output. The rehearsal normalized the legacy Summary heading only in its temporary input. The Current Action retained its exact bytes. Workbench query `2e45cdc1de704228878b9ee5f04411d9` verified the Current and Draft references.

The Version overlay published the exact CA-R-1432@32-draft body as Current @33 in a disposable Project. It retained CA-R-1432@31-draft byte-for-byte and archived Current @30 with its body, Topics, Version and Updated At preserved. The rehearsal used fixture placement and status admission. Source and output hashes are in `promotion-version/rehearsal-r1432/receipt.json` under the Task evidence directory.

A second rehearsal used the project layout, release schemas, and Workbench index. CA-R-1432@32 published as Current @33, archived @30, and preserved the competing Drafts byte-for-byte. The direct filesystem probe rejected a legacy @10 carrier whose header says Active even though its filename identifies an archive. The indexed Lifecycle route passed with that carrier present. Evidence is in `promotion-version/real-layout/r1432-indexed-receipt.json`.

The batched Version rehearsal used the real Workbench index. With Archive coverage loaded, the shortcut probed @7, promotion resolved the actual Archived @10, published @12 from Draft @8, and preserved competing Draft @11. With coverage unloaded, the batch returned `archive_not_loaded` with no effects and preserved both Drafts. The tested shortcut affected refresh grouping only. Evidence is in `promotion-version/batch-predecessor/root-verification.json` under the Task evidence directory.

## Wave 47 staging

CA #8 staged CA-R-2732@3 and the exact linter patch. Staged Workbench query `5a1c28e7439647e08e08c4c6edfafe5c` matched 42 Scope Units, the expected Current carrier and its Version. The staged graph and six compiler outputs matched the rebased baseline. The Operator stopped the release gate. CA #8 verified the test containers were down, retained the staged image, and confirmed the preceding release was live and healthy. The retained candidate was later resumed and published.

An independent audit read the 43 earlier census exceptions. Forty-one are execution-evidence Markdown reports without Atom frontmatter. CA-D-487 and CA-D-488 are Delivery Atoms with conflicting legacy Topic fields and prose-only Claims. None of the 43 contains a CFEL fence.

The pre-publication census found 52 confirmed Current and 32 Draft Claims with CFEL fences, plus two provisional Current sources. The exact selection is in `wave47-pre-publication-frontier/current-frontier-audit.json` under the Task evidence directory.

Six Current Core Model Claims had a mechanical conversion and no Python Draft. Strict lint rejected CA-R-1026 and CA-R-2422 because the registry excludes the case-colliding `depends_on` Relation. The other four cover Substep or Event Author and await their Model disposition. No new Drafts were created for these six Claims.

## Wave 47 publication

CA #8 deployed the retained image after the full gate ran 2,241 tests across 275 modules with four skips and zero failed modules. Lifecycle published CA-R-2732@3 and archived @2. The verifier matched the Current and Archived carrier bytes, Model graph and six compiler outputs. Workbench query `c310019ed3fb445a945e054d5b382201` confirmed the publication across 42 Scope Units. Independent query `394a51db6a9f420d80f60ef188fa3797` confirmed the Current Python Claim and Archived CFEL Claim. Evidence is under `.caprmedio_tmp/wave47-retained-release/`.
