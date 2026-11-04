# CFEL operator and format review

Reviewed all 26 pinned Current native operator-owner Atoms and the relevant CFEL catalog/default rules. Individual verdicts and source pins are in `review.json`. Candidate hashes and dependencies are in `manifest.json` and `successor-format-manifest.json`.

Source-only candidates cover the `//` declared-kind wording, R2487’s clarified Subject-selection `:=` scope, approved parentheses for mixed AND/OR, and the missing AND/OR declarations. R2550/R2598 are fresh-ID successor drafts because their Summaries change; the old carriers and frozen references remain untouched. The bounded incoming-reference inventory found CA-A-1315 as the only other-Atom reference to R2550 and none to R2598, excluding Workflow/Workbench.

The approved `[int, 0..100]` form has two minimal Format declaration previews: closed numeric range endpoints, then comma-combination by intersection. Existing curly-brace cardinality range meanings remain unchanged. R2564 retains required occurrence and one-value cardinality, with `?== 90`; no Carrier or file write is implied.

Relation direction, endpoint signatures, aliases, and delivery/exclusion semantics remain cross-lane. No Current carrier, code, tests, or Git state changed.
