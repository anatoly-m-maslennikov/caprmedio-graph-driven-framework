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
    atom: CA-P-3018
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:47:49.228319+00:00'
destination:
  file:
    name: CA-P-3022-TASK--migrate-cfel-claims-to-readable-python.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-3018-EPIC--adopt-the-workflow-engine-and-migrate-cfel-claims-to-python
---
## Summary

Migrate CFEL Claims to readable Python

## Objective

Migrate CFEL Formal Claims to readable Python declarations and expressions. Preserve Topic and Subject notation. Use descriptive functions, classes and named parameters with minimal boilerplate. Lint syntax and model references.

## Inventory and cutover

The Workbench snapshot found 335 distinct Current references and 132 Draft references with Formal Claims. It also found 970 Current carriers, including installed and historical copies. Pin the authoritative source of each reference before using these counts for migration coverage.

1. Revise the Formal Claim declarations and consumers together. CA-R-2721 currently admits only CFEL fences for RMED. The Workbench compiler also extracts only CFEL fences. Keep existing Claims effective until the Python path supports them.
2. Start with schema definitions, inheritance and overrides. Cover formats, direct and nested cardinalities, Relation declarations and inverses, Role and Form constraints, Status, placement, ordering, and Scope Unit topology. Use a shared declaration representation for generated assets and graph projections.
3. Use the existing Subject resolver for Model references. Keep the Claim linter read-only and check syntax and admitted references before evaluation. Compare readable Python declarations and predicates with a small expression engine on the same real Claims. Record the decision and examples.
4. Run both consumer paths on the same pinned input set. Compare effective inherited and overridden constraints, generated assets, graph facts and diagnostics, and scope topology. Report unsupported Claims with Atom and Version. Switch each consumer after parity, then retire its CFEL Claim handling when its migration inventory is complete.

## Acceptance

Prove coverage on authoritative Current and Draft Claims. Verify that existing Topics and resolved addresses retain their meaning. The linter identifies bad syntax and unresolved references without executing the Claim. Check schema and graph parity for all affected consumers. Record why a separate expression engine is needed or why standard Python and shared helpers suffice.

## Source census

A filesystem check started from the 41 declared Scope Unit paths and scanned their standard Role folders. It recognized the same CFEL Claim fences as the current schema compiler. This found 335 Current references across 471 CFEL carriers and 72 numbered Draft references. For 155 Current references the scan found more than one candidate carrier, including candidates without a CFEL block. Eight declared paths were absent and 31 candidate Markdown carriers did not parse. Resolve those exceptions before treating this as a complete migration inventory. Use exact carrier path, Version and digest for each selected source.

The path check found 328 unqualified Current carriers with CFEL Claims. Of those, 298 matched their declared Scope Unit Container and 30 lacked Container evidence. Six references had only historical carriers, and one unqualified Current carrier had no CFEL Claim. The 31 parse errors included 29 qualified filenames and two unqualified Delivery Atoms, CA-D-487 and CA-D-488. Neither Delivery Atom has a CFEL fence. The working manifest at `.caprmedio_tmp/CA-P-3018/CA-P-3022/cfel-source-frontier.json` records the paths, Versions and digests for this snapshot. Revalidate the manifest before cutover.

## Model Drafts

- CA-R-2721@5-draft admits one Python fence for a Formal Claim whose consumers support Python. It keeps CFEL admitted during migration.
- CA-R-2500@7-draft, CA-R-1417@34-draft, CA-R-2102@18-draft and CA-R-2471@11-draft defer the fence language to the applicable Formal Claim declaration.
- CA-R-3010@8-draft applies the transition to the optional Formal Claim in Code Synopsis.

## First Python example

CA-R-2500 can be expressed as a named declaration with explicit occurrence, value and child constraints.

```python
declare_property(
    address="Atom.Content.Claim",
    roles=RMED,
    occurrences=exactly(1),
    direct_values=exactly(0),
    children=allowed_children(
        names=("Formal Claim", "Prose Claim"),
        occurrences=between(1, 2),
        unique=True,
        order=("Prose Claim", "Formal Claim"),
    ),
)
```

Use the same declared structure for schema compilation, inheritance and graph evidence. Compare this with an expression-engine version of the same rule and with an instance condition that needs a predicate. Keep the comparison provisional until representative Claims from each category pass.


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
