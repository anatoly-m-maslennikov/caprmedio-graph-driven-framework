# Header, Content and CFEL migration

The selected migration is applied and checked. P2694 remains Active for its existing P2707 verification and the remaining MODEL audit queue.

| Result | Verified scope |
| --- | --- |
| Root prefixes | 1,178 files; 3,685 active/passive Subject values |
| Manual source adoption | 87 Current outputs; 27 fresh IDs CA-R-2696–CA-R-2722 |
| Preserved history | 86 exact-byte predecessor archives |
| Retired sources | R2501 Claim Scope; R2595 reference operator; D482 stored target |
| Remote pre-migration checkpoint | db837f08ec3f29eeb6010e4bce09bfc64f2332d1 on amm/dev |
| In-place migration | 1,158 selected files; 1,071 changed; zero held |
| Postcheck repairs | 5 current consumers; zero remaining live references to retired/replaced IDs |
| Preservation | IDs, Summaries, versions, statuses and Updated At retained |
| Repeat application | Zero changes |
| Focused tests | 160 passed |
| Live readback | 44 Scope Unit Declarations; three status domains |
| Projections | Seven rebuilt from 1,154 exact Current sources |
| Relations | 41 Declarations; 11 inverse views; seven symbolic aliases |
| Detail contracts | All 110 provenance sources are Requirement / Declaration |

Markdown titles alone declare no Properties. Declared paths identify Properties. Wildcards constrain declared Properties. Formal Claim and Prose Claim are the declared Claim children; other prose headings remain Markdown.

Relation objects use `Relation//NAME`; actual links use `{:count}((NAME))` where bounded. Valid opposite endpoint bounds retain their meaning. The `@` reference marker is removed; version citations and quoted CFEL literals are preserved.

## Remaining MODEL audit queue

12 selected sources still have unresolved model bindings. These were recorded rather than mapped to invented Properties.

| Atom | Subject |
| --- | --- |
| CA-R-2559 | `CAPRMEDIO_MODEL` |
| CA-R-1014 | `CAPRMEDIO_MODEL <+ Atom.Local Scope Unit` |
| CA-R-1489 | `CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan).Implementation Retry Limit` |
| CA-R-1596 | `CAPRMEDIO_MODEL <+ Atom.Target Scope Unit` |
| CA-R-1690 | `CAPRMEDIO_MODEL <+ Atom.Governance Origin` |
| CA-R-1732 | `CAPRMEDIO_MODEL <+ Atom.Target Scope Unit` |
| CA-R-718 | `CAPRMEDIO_MODEL <+ Atom.Target Scope Unit` |
| CA-R-886 | `CAPRMEDIO_MODEL <+ Atom.Local Scope Unit` |
| CA-R-920 | `CAPRMEDIO_MODEL <+ Atom.Local Scope Unit` |
| CA-R-947 | `CAPRMEDIO_MODEL <+ Atom.Target Scope Unit` |
| CA-D-291 | `CAPRMEDIO_MODEL <+ Atom.Local Scope Unit` |
| CA-R-1645 | `CAPRMEDIO_MODEL <+ Atom.Governance Origin` |

The projection check also reports 251 sources outside its declared scope and 320 unsupported CFEL diagnostics. These counts were not compared with a pre-migration baseline. Unsupported expressions remain visible. The qualified IS_DEFINED_BY derivation remains prose evidence; its endpoint transformation is structurally uninterpreted.

The Event Record hierarchy retains an explicit root diagnostic. The older Engine/native-workflow/release checks were outside this focused run. Manual source application did not create a native Run or append a Journal record.

## Evidence

[Application and verification receipts](../../../03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/)

## Projections

- [CA-PROJ-020-CAPRMEDIO--Map--Primary-Entities-Tree](../../../_projection/CA-PROJ-020-CAPRMEDIO--Map--Primary-Entities-Tree.md)
- [CA-PROJ-021-CAPRMEDIO--Map--Primary-Entities-with-Direct-Properties](../../../_projection/CA-PROJ-021-CAPRMEDIO--Map--Primary-Entities-with-Direct-Properties.md)
- [CA-PROJ-022-CAPRMEDIO--Map--Primary-Entities-with-Inherited-Property-Contracts](../../../_projection/CA-PROJ-022-CAPRMEDIO--Map--Primary-Entities-with-Inherited-Property-Contracts.md)
- [CA-PROJ-023-CAPRMEDIO--Map--Primary-Entities-with-Inherited-Formal-Claims](../../../_projection/CA-PROJ-023-CAPRMEDIO--Map--Primary-Entities-with-Inherited-Formal-Claims.md)
- [CA-PROJ-024-CAPRMEDIO--Map--Passive-Only-Subjects](../../../_projection/CA-PROJ-024-CAPRMEDIO--Map--Passive-Only-Subjects.md)
- [CA-PROJ-025-CAPRMEDIO--Map--Subjects-without-Requirement-Declarations](../../../_projection/CA-PROJ-025-CAPRMEDIO--Map--Subjects-without-Requirement-Declarations.md)
- [CA-PROJ-026-CAPRMEDIO--Map--Entity-Definition-and-Active-Subject-Coverage](../../../_projection/CA-PROJ-026-CAPRMEDIO--Map--Entity-Definition-and-Active-Subject-Coverage.md)
