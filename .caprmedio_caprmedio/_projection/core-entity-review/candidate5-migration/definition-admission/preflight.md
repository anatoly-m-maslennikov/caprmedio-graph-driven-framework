# Candidate #6 — native admission preflight

Observed 2026-10-17. Read-only diagnostics; no source mutation, execution authorization, queued workflow or creation is claimed.

## Existing route

MCP returned complete Create Atom / CA-O-127 execution context. Creation can admit a fully identified new Atom; the unavailable Draft-promotion binding is not a blanket creation blocker. Generic content updates additionally require their existing semantic-assessment inputs. These reports do not replace those inputs or manufacture an authorization receipt.

## Diagnostic results

1. The native `create_atom_action(..., execute=False)` accepted an in-memory Actor.Name creation candidate without relations. This only tests carrier structure. Omitting a required parent is not an acceptable execution workaround.
2. A Continuant creation candidate with `child_of: [CA-R-1174]` stopped before parent semantics: `authoritative carrier frontier is unavailable`, caused by `CARRIER_UNSUPPORTED: Atom validation supports YAML frontmatter`.
3. The exact unrelated offender is `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/01_concern/CAPRMEDIO-FRAMEWORK-ENGINE-CONC-076-SKILLS-PROBLEM--problem-core-skill-runtime-is-incomplete.md`. It uses legacy TOML frontmatter. Relation discovery parses every admitted carrier before filtering requested IDs.
4. The existing pure validator's finite `reference_roles` option successfully resolves R1174 with Requirement-only and PRMEDO inventories. Native Create does not forward that option. This result validates reference discovery only, not the complete proposed relation.
5. The separate `_tier_parent` check in `VALIDATE_ATOMS/validate_atoms_workers/check_graph_extended.py` compares owner strings and rejects different owners. It does not inspect permitted ancestry. The proposed parent map relies on existing ancestor topology, so changing R796 wording alone would not repair execution.

## Local fixes — 2026-10-17

- Bounded reference inventory recognizes well-formed TOML carriers with a clear identity unrelated to the requested targets. It does not admit those carriers, alter them or migrate C/A. The final frontier check includes both direct and transitively discovered parent/prerequisite identities, so a skipped legacy carrier cannot hide a duplicate reached later in the chain. Explicitly requested legacy identities, duplicates, inactive references, closure and currentness checks retain their existing validation. Strict containment inventory is unchanged. Ten new regressions cover legacy lookup, including transitive identity and filename collisions; existing reference, evidence and containment tests are checked separately.
- Parent validation now resolves declared Scope Unit ancestry. Same-owner parents require a lower Global Tier; ancestor parents may have an equal or lower Global Tier, preserving E117 v10. Sibling, unrelated, descendant and greater-tier parents remain rejected. Fifteen new regressions plus sixty existing graph/structure tests passed.
- PROGRAMMATIC implementation followed M384, M157, M160, M158, M387, M316, M392, M388 and M390: bounded declared behavior, shared readers, explicit computation and verified effects. No new workflow or configuration switch was added.
- The actual reviewed Continuant definition with proposed parent R1174 now passes native `create_atom_action(..., execute=False)` using the local code. The destination remains absent. This checks both repaired paths together, without publishing an Atom.
- Ruff passes the changed files with the existing C901 complexity warnings excluded. The reference module already exceeded that limit before this change (`_frontier` 23, reference inventory 50); the additional skip condition makes `_frontier` 24. No unrelated complexity refactor was added.
- Independent review passed after correcting the transitive-reference collision case. All 25 new tests passed together. No remaining concrete defect was identified in these two bounded fixes; full-suite, deployment and live-write verification remain separate.
- Final focused reruns passed 114 lookup/reference tests and 75 parent/graph/structure tests. The 21 strict-containment tests passed before the final one-line closure refinement and were not rerun after it.

## Remaining source and execution work

The local code fixes are implemented. The R796 source correction and other prepared source-alignment updates remain pending. The running MCP has not been redeployed with these changes.

The 45 new definitions, five supporting Rs and one D successor remain proposals. After source alignment and deployment, run real previews and authorized execution, then verify source Atoms and regenerate the graph. Focused test results do not constitute a full-suite or live-admission result.
