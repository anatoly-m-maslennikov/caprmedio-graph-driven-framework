# MODEL Property value-contract audit

The recognized exact-target universe contains 104 Property targets: 82 with Current Requirement/Form Declaration sources and 22 with Entity Definition but no exact Declaration. The declaration table pins each source to `model-supplier-frontier.json` SHA-256 `8deca481ee12c09ac65df272e20c4d15aaffafbafcd344187003011bfe9db71e`; all 82 paths and hashes matched their live sources. The separate no-declaration table pins the 22 Definition sources. These totals cover the recognized Property universe, not all possible MODEL grammar or unresolved identity alternatives.

| Result | Count |
|---|---:|
| Declared format and value count in the declared context | 82 |
| Exact target without Declaration authority | 22 |
| Missing format or value count among the 82 Declaration targets | 0 found |
| Conflicts among examined value clauses | 0 found |
| Unresolved exact-target identity and inherited Declaration coverage among the 22 | 22 |

`[]` with `{:0}` explicitly forbids direct values; no format is required for a nonexistent value. Zero-value groups pass. Definition content is not used to establish an authoritative format or value count. Each no-Declaration target is a coverage finding, not an instruction to create another Declaration: alternate paths need adjudication. `Carrier/File.Format` may inherit from `Carrier.Format`; both currently appear in the Definition-only inventory, so effective Declaration authority remains unproven.

The `value-contracts.tsv` records qualified and conditional contexts and distinguishes occurrence count from value count. The three Scope Unit.order declarations omit occurrence bounds in their own value clauses; other applicable Declaration constraints and the rule requiring occurrence bounds must be resolved before classifying those omissions as violations. `Atom.Content.**` constrains declared descendants and does not introduce arbitrary Property names. The RMED Claim group has zero values, while each present Formal or Prose Claim child has one Markdown value; these are compatible with the inherited descendant rule.

CA-R-2632 specifies the zero-value Authority Modes group; CarrierAlias `read_view` recognizes its legacy `subjects.governs`. Its old Claim layout remains migration debt, not a reason to discard its value contract. CA-R-2532:25 includes Authority Modes in its parent allowlist. No live source was edited.
