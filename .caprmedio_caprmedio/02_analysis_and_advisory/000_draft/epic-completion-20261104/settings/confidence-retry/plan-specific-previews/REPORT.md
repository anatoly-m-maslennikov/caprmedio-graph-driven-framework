# Plan-specific confidence precedence — preview

Three source-pinned combined previews retain their Current IDs and exact Summaries. CA-R-1428 and CA-E-241 incorporate their existing Project.Settings merge previews; apply one combined preview per source only after review. `manifest.json` records Current frontier, predecessor, base-preview and candidate hashes.

The latest Plan decision was relayed in this task as: “Plan AI Agent Confidence Threshold fallback: Plan local ?= enclosing Plans via IS_CONTAINED_BY recursively ?= required Project.Settings.AI Agent Confidence Threshold.” The same task directs preservation of outside-Plan direct Operator input, its context limit, and applicable default behavior. This wording is a coordinator relay; this bounded review did not locate a separate verbatim human-decision carrier.

- **CA-M-271:** separates Plan execution from outside-Plan resolution; Plan inheritance admits any nearest enclosing Plan, not only a Hub. Outside a Plan, the current applicable direct Operator input precedes the applicable per-threshold default, with its context limit. It preserves independent parameter lookup, invalid/ambiguous/cyclic stops, source tracing, no silent fallthrough or copied override, and no new execution permission.
- **CA-R-1428:** states the same split without asserting a new threshold or Property.
- **CA-E-241:** tests both cases, recursive nearest-Plan selection, per-threshold independence, failure disposition and source tracing while preserving the existing Claim and Projection checks.

No Current source, runtime evaluator, graph node, new ID or physical settings Carrier changed. Current and merged-preview hashes were checked at preparation. These drafts are not applied; physical settings migration, Plan Carrier successor references and full integration validation remain separate. The partial CA-M-306 packet is held for combined Author, Assignee and Claim Target Scope Unit review.
