# CFEL operator and format review

The 26-Atom review and source pins are in `review.json`; candidates and hashes are in `manifest.json` and `successor-format-manifest.json`.

`LOOKUP(R, q)` already occurs in Current R2711 and is listed in R2487, but has no dedicated current operator declaration. Its full existing contract is now attached to a new `Operator//Lookup` Declaration under R2616’s existing Operator kind; no Rule-only generic CFEL scope or new syntax is introduced. The contract was moved out of the focused fallback successor without semantic loss.

The two range candidates are Rules on existing `CFEL <+ Format`; `[int, 0..100]` is defined by inclusive numeric-range and comma-intersection semantics. Existing `{:n..m}` cardinality remains unchanged. The R2550/R2598 Summary changes use fresh-ID successors. The R2705/R2711 candidates bind selected Atom/Plan instances before assigning defaults; R2711 binds the unique Project in the current Project context under R2524/R2552, while preserving its schema-valued LOOKUP argument. The atomic plan includes the CA-A-1315 dependency remap and all-or-none retirement; frozen references and mirrors remain untouched.

These are source-only candidates; pin checks do not establish adoption or runtime behavior. No Current source, mirror, archive, projection, CoreRuntime pin, code, tests, or Git state changed.
