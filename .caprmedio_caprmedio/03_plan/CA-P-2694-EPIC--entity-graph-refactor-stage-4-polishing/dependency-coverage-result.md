# P2695 — dependency-only coverage result

Reviewed all 29 original paths / 63 dependency uses. Published 21 source successors with predecessor archives and 3 new Entity Definitions: R2274 Tier Label, R2423 Project Settings Obsolete Names (originally misassigned R2275; see identity correction below), R2277 Extension Sources candidate Selection. No Engine, code, runtime, O, C or A source-content migration was performed.

- Removed invented Relation.Authority and Projection.Authority dependencies; Relation.Source Reference uses the actual Relation model.
- Corrected obsolete UX Entry, Local Scope Unit and Agentic Step Execution Context paths.
- Defined optional Tier Label and its numeric mapping: 0 Principle, 1 Core, 2 General, 3 Standard, 4 Detail. Numeric Tiers continue above 4. D276 registers optional flat tier_label while retaining tier and the distinct Atom label field. No labels were bulk-written to existing Atoms.
- Promoted DERIVED_FROM to Relation Definition authority; formalized already-governed File format values, inherited Atom Active, Plan Done, and Projection Map/Hub values. Defined the Delivery-specified Obsolete Names property without changing Settings values.
- Retained shared R2214 Engineering definitions, R-backed classification/allowed values and declared Selection meanings. Actual named Scope Unit/Action instances retain their Project Structure/O authority; their kind Definitions are not duplicated.

The fresh 1,111-source readback has 20 exact dependency-only paths / 34 uses. They are explicitly covered/registered rather than silently called missing. Exact-Governs absence is not the same as missing definition semantics.

CA-PROJ-014/015/016 were rebuilt from the actual current source ID/Version/hash vector. The coverage audit reports 427 parsed targets, 32 Relation Types, no structural/required-schema gap or stale-source warning, and 23 explicit non-authoritative examples/template diagnostics. This verifies coverage and source fidelity, not unique Definition ownership.

## New stronger Definition ownership requirement

The Operator subsequently required exactly one R/Entity Definition per Entity, with IS_DEFINED_BY derived. That is being handled in P2696, not asserted complete by this Task. Across 337 primary-kind/property paths, 180 have one exact-Governs Definition, 24 have multiple candidates, and 133 use shared/formal declarations without an exact-Governs Definition. The last count is not automatically missing definitions. No candidate has been hidden or arbitrarily selected.

The Definition-family inclusion question and ownership of shared formal declarations remain open. R2278/R2279 are unadopted Rule/Relation Drafts; A1306/A1307 record these decisions. The Epic remains Active.

## Deferred content issue

E477 still contains older conflict-policy examples involving Global Tier and timestamp winners. This Task corrected its Principle dependency only. The Operator previously deferred those Workflow/content corrections; this report does not claim they now implement Operator-only conflict resolution.

## Identity correction — 2026-10-29

The original publication report above records the ID used at that time. That Settings assignment accidentally reused `CA-R-2275`, already validly assigned to the ID Term Definition. The Operator-authorized CA-M-276 repair preserves the original owner and gives Project Settings Obsolete Names the fresh identity `CA-R-2423@1`. Its Claim and all metadata except `atom_id` are byte-preserved. Journal event `0e1853d5-f441-4bc7-9460-bd4db67a0c3c` records the exact preimage and mapping. Current references to this Settings Definition must use CA-R-2423. CA-PROJ-014/015/016 retain historical provenance until regenerated through their original generation path; this repair does not claim a rebuild.
