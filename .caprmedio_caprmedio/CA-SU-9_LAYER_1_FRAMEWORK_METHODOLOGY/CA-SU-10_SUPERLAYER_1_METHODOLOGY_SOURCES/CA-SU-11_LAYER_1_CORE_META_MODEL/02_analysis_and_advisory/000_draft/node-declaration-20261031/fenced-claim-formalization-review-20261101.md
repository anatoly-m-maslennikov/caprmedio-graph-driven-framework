# Fenced Claim formalization — 2026-11-01

Status: reviewed Draft change. No adoption or runtime deployment.

The Operator restricted fenced code blocks only. Indented code is outside this rule. The Claim Declaration now has only formal expressions. One general FENCED_LABELS selector applies the finite literal Format [in (CFEL)] with occurrence count0..1. All selected labels must match; duplicate labels still count separately. Required Markdown value and zero-dependent constraints are preserved.

The original five-helper candidate is superseded. Independent review caught that a bare allowed-value case did not explicitly close the label domain. The finite Format replaces it. Final review passed for the concise Rule and consumer.

The complete Markdown parse and resolved label binding are required inputs. Unlabelled fences contribute an empty label and fail the Format. Unknown parsing or label bindings error rather than pass. No new raw-info-string, metadata or case-normalization policy is introduced. CFEL body syntax remains a separate check.

The packet contains112 Drafts,27 Primary and47 Property Declarations. There are58 formal-only Claims across the packet. Sixteen Node descendant Declaration Claims retain prose:3 Primary and13 Property. All registered metadata, links and source-preservation checks pass;750 pinned Current Requirement sources and Current Epic38 are unchanged. Parser and runtime behavior were not tested.

Evidence: [application](declaration-expansion/fenced-labels-application-20261101.json), [final review](declaration-expansion/fenced-labels-final-review-20261101.json), [latest prose census](remaining-node-claim-prose-20261031.md).
