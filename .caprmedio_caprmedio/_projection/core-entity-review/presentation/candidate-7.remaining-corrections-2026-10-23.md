# Candidate #7 — applied remaining-source corrections

Updated: 2026-10-23 03:29:31 +0400. Status: partial, applied and recorded; not full migration completion.

## Actual effects

- 2,219 distinct source Atoms changed, with 3,244 versioned updates and predecessor archives across the stages.
- 5,132 exact Subject corrections, excluding O160's separately recorded ownership/Subject correction.
- 732 previously missing carried IDs added from unambiguous existing filenames. No new identity was allocated.
- O160 moved from Core to Project Configuration. Its Summary and body remain unchanged.
- No new Domain entity, Summary, Substance, Type, relation link or intended Status was introduced by this continuation. The five ordinary batches leave ownership unchanged; only O160 changes ownership.

| Stage | Atom updates | Subject corrections |
| --- | ---: | ---: |
| stage1 | 876 | 1,553 |
| stage2 | 1,204 | 2,630 |
| legacy-identity | 732 | 0 |
| stage3 | 279 | 791 |
| stage4 | 152 | 158 |

Each real update advances Version and Updated At. Its predecessor has an Archived ID/filename qualified by the old Version and keeps that numeric Version and timestamp. Current body content is unchanged; archives qualify their own identity where it occurs. A source can appear in more than one stage; stage totals are not unique-Atom totals.

The [JSON ledger](candidate-7.remaining-corrections-2026-10-23.json) records every changed source path, Version and current/archive hash. The original inventory contains 2,901 C/A/R/M/E/D/O carriers, including legacy sources missing Status. Plans and Implementation are outside this specification frontier. Previously excluded legacy carriers remain visible; malformed data was not guessed.

## Verification

Independent Luna verification is recorded in the JSON ledger. The ordinary Stage 1→2 chain already passed: 1,466 unique current owners, 4,183 endpoint changes and 2,080 archives. The final receipt covers the identity repairs, later aliases and O160 too. Mechanical apply checks also ran after every batch. These checks are source-migration evidence, not runtime or release acceptance.

The PROGRAMMATIC holds E567, R1847, R1848, D547, E568 and A1142 remain untouched. All other unrelated dirty work is preserved.

## Remaining

- 5,224 noncanonical Subject occurrences (1,399 exact strings) still need their own source dispositions. Canonical-looking syntax alone is not semantic acceptance.
- The [unapplied worker proposals](candidate-7.remaining-mapping-proposals-2026-10-23.json) preserve those 5,224 exact occurrence records and their historical source pins outside disposable scratch. They are proposals, not accepted mappings or permission to add Domain entities.
- Incomplete headers and 40 originally malformed/non-string Subject values remain visible. Adding IDs is not proof that every other required property is fixed.
- Obsolete Revision/glossary sources need contextual mapping or retirement. The unapplied glossary candidates are R1193/R1251 (preserve useful dependence meaning in R1260 Semantics) and R1248/R1266/R1267 (preserve Node abstraction in R1994 and bearer distinctions in R1260); verify consumers before any retirement. General Substance migration stays separate.
- CA-O-188 names two distinct sources: a public-release Workflow with an explicit ID and a localhost-MCP launch Action with only the filename identity. The latter was excluded from the 732-ID repair. Neither identity is reassigned or retired here.
- Other Type/property/ID and filename work, Plan-frontier work, graph rebuild, final verification and independent Tools-plan rehoming remain. Keep CA-P-1959 Active.

No production Tools/code, MCP/runtime, Settings values, tests, release, commits or Journal events were changed or claimed. Scratch scripts performed the file mechanics. Worker mapping proposals are not automatically applied or authoritative; this checkpoint is batch evidence, not a newly admitted graph Projection.
