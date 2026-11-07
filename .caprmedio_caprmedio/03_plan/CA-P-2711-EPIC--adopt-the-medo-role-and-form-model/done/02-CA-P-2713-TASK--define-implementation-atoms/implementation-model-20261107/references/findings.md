# CA-P-2713 — reference and lifecycle findings

Status: proposal-only. This lane makes no native-model, code, runtime, Journal, or Git change.

## Smallest defensible binding

Use a `Code references` subheading in the ordinary Claim text of an admitted I / Code Synopsis. It contains one or more unambiguous Project-context Markdown links to actual code, optionally narrowed by an anchor or accompanied by an observed digest. A declared Code-Root Locator applies when present. This is ordinary Markdown, not a registered Property, new Atom, or Relation. It does not demand one-to-one coverage, a specification, a commit SHA, Git metadata, a snapshot status, or a locator grammar.

The actual code Carrier remains authoritative for actual behavior and structure. A synopsis is an authored observation of it. A difference from an optional specification or from synopsis text is neutral until an assessment establishes a Concern.

## Existing relation fit

| Need | Existing fit | Boundary |
| --- | --- | --- |
| Optional contribution to specification, analysis, or Task | `CONTRIBUTES_TO` (CA-R-3001), I -> related Atom | Contribution is not verified satisfaction and is never required. |
| Rationale for an I description | `rationale_for` (CA-R-1016), Rationale -> I | Use only when the Rationale actually explains the synopsis. |
| Assessed matter | `concern_about` (CA-R-1022), Concern -> governed entity | A neutral difference does not create a Concern. |
| Actual carrier implements a specification | `implementation_of` (CA-R-1020), Carrier -> specification Atom | Do not repurpose it for Code Synopsis references. |
| Evidence Carrier support | `evidence_for` (CA-R-1021), Carrier -> Carrier | Do not repurpose it for Code Synopsis references. |

## Identity and lifecycle

I / Code Synopsis reuses ordinary Atom identity, Status, Version, Updated At, and archival rules (CA-R-1412, CA-R-1415, CA-R-1788, CA-R-2565). A code edit does not automatically revise the synopsis, advance its Version, or change its Status. An accepted synopsis edit follows the normal Atom lifecycle; archival preserves Version and Updated At.

CA-R-2173 supports separating logical artifacts from their Carriers while treating actual implementation as authoritative. CA-R-1873 supports existing code as a source for adoption and reconciliation without automatically changing governing RMED. However, its Current production sentence still requires native I to derive from current applicable RMED; the pending successor in `impact/rule-candidates.json` is needed before the no-specification case can be adopted as Current.

## Integration handoffs, not blockers

1. Refresh process, Task Run, and any automatic synchronization remain Engine-workflow concerns; this Form invariant adds none.
2. Root integrates the scoped CA-R-1873 successor before asserting the approved no-specification boundary in a native Current source.

Pinned source paths and hashes, plus promotion-ready candidate text, are in `drafts.json`; the compact integration contract is in `integration-contract.json`.
