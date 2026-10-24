# Candidate #7 — bounded Tool-Atom cleanup

Status: applied and verified, 2026-10-23. This is a non-authoritative change report, not a complete migration or runtime acceptance.

## Actual changes

Reviewed the 207 source Atoms contributing 210 unresolved exact `Tool` Subject occurrences. Applied 205 same-ID updates, preserved 206 predecessors and retired one duplicate, R1870. Removed its three current inbound links from D555, D558 and O162; D555/D558 retain both delivery decisions.

The 205 updated governing Subjects resolve to 91 existing Domain bearers and 114 Engineering topics. No new Domain entity, Atom ID, Summary or Substance was introduced. Corrected 153 Types under the approved classification-only migration exception. No Local Tier change was justified.

Use the governed thing, not its Content Role or a Tool name: Selection for artifact query results; Governing Configuration for Settings/Structure reads; Projection for graph outputs; Journal.Record for recorded events; Execution for actual calls and runs. Keep Action.Execution Kind dependent, and Projection/Type classifiers distinct from dependent properties. Derived Action instruction construction is an Engineering prompt topic, not the Method Atom kind.

## Ownership corrections

- O159: concrete query Action moved from Core to Project Configuration, beside its project procedures. Summary, ID and content remain unchanged.
- C455, C459, C460, C462 and D569: replaced undeclared `ATOM_LIFECYCLE` ownership with declared `TOOLS` and moved current carriers into its role folders. D569's old target-scope mirror was corrected too.
- O160: concrete Step ownership remains a separate follow-up; it was not in this 207-owner frontier. Its stable O159 reference remains intact.

## Hold and remaining work

E567 is unchanged at Version 7 and remains owned by the PROGRAMMATIC reconciliation. Its metadata proposal was sent for combination with that work; no approval or runtime repair is inferred.

389 other legacy dependency literals remain for the wider mapping. This increment does not complete the Subject migration, defining-rule coverage, property/ID work, filename alignment or graph rebuild. Refresh affected source pins before reusing the earlier prepared mapping; those older snapshots remain history.

## Verification

All 205 current headers exactly match reviewed deltas with one Version increment and the actual edit timestamp; all current bodies and intended Status values are unchanged. All 206 archives carry qualified IDs and Archived Status while preserving old Version, timestamp and unrelated content. Current affected IDs resolve uniquely. All six source moves, duplicate retirement and link removals were checked. E567's hash is unchanged. Scoped `git diff --check` and independent post-write review passed.

No production code, Tools, schemas, Settings values, MCP/runtime or release was changed. No runtime suite, commit or push ran.

The [machine-readable change record](candidate-7.tool-atom-cleanup-2026-10-23.json) lists exact source/archive paths, Versions, hashes, deltas and the hold.
