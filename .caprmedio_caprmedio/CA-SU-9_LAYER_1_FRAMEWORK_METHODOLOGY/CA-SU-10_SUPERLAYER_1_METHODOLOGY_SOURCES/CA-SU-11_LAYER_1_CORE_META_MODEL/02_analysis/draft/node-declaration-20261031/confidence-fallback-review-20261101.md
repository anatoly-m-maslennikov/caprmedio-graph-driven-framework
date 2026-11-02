# AI Agent Confidence Threshold fallback — 2026-11-01

Status: reviewed Draft changes. No adoption, runtime deployment or configuration value assignment.

The Operator chose an optional P value with recursive IS_CONTAINED_BY fallback and a required Project Settings default. The name is AI Agent Confidence Threshold on both bearers. Project.Settings admits exactly Name, Prefix and this default.

The fallback Rule reuses ?= as one ordered non-writing chain. One LOOKUP operation returns the nearest applicable authored value along existing directed links. It does not create Properties on intervening kinds or confuse unrelated same-named Properties. Absence can continue the chain; invalid present values error. Evaluated fallback-expression cycles and traversal cycles error separately. Later unused branches are not evaluated; independent required Property constraints still apply.

The terminal Project is selected in the current Project evaluation context. No new containment route to Project is required. No actual threshold number is invented. The original same-bearer Atom.Label fallback example remains.

Independent review passed after restoring the general fallback-expression-cycle safeguard. The packet has112 Drafts,27 Primary and47 Property Declarations. Sixty Claims across the packet are formal-only. Fourteen Node descendant Declaration Claims retain prose:3 Primary and11 Property. Registered hashes, metadata and links pass. The750 pinned Current Requirement sources and Current Epic38 remain unchanged.

The old confidence name survives only in historical evidence and Current sources. Retry Limit stays withdrawn. Parser, graph/reference bindings, actual Project default value and runtime consumer migration remain separate work.

Evidence: [decision](declaration-expansion/ai-agent-confidence-fallback-decision-20261101.json), [application](declaration-expansion/confidence-fallback-application-20261101.json), [final review](declaration-expansion/confidence-fallback-final-review-20261101.json).

The [reference inventory](declaration-expansion/confidence-fallback-reference-inventory-20261101.json) covers12 registered Drafts. It flags the [typed-relation adapter binding](declaration-expansion/confidence-fallback-relation-binding-gate-20261101.json): contained_by.atom/scope_unit must resolve as outgoing IS_CONTAINED_BY facts before runtime LOOKUP can operate. This mapping is an implementation gate, not a claim of deployed behavior.
