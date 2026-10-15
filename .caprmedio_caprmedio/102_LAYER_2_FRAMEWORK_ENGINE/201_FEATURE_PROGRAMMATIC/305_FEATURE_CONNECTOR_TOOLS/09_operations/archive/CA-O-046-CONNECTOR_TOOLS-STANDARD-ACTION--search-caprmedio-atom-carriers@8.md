---
atom_id: CA-O-046
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Search Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_SEARCH"
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 8
updated_at: "2026-10-12 23:49:24 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to: [CA-R-1936, CA-M-376, CA-D-625, CA-O-201]
---
# Summary

Search CAPRMEDIO Atom carriers

## Operation

Search Atom Carriers **means** the read-only query Action that returns every and only logical Atom matching the explicit caller criteria through the common connector interface in CA-D-625, CA-R-1936 and CA-M-376. Operation is `query`; it does not choose meaning, identity, lifecycle policy or a subsequent Workflow.

Use D625's closed inner request keys `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` and `context`. Exactly one of target or query is non-null; target is `{kind, identity}`, query is `{kind, filters}`. Query/read use null delta; modify receives explicit supplied edits. Modify requires expected current state; Create requires expected absence. An ordinary explicit-ID Read returns its actual exact Version/state token without requiring a pre-known Version; optional pinned/historical Read Version and expected_state must match exactly. Do not invent a Scope Unit Version. Authorization/context reference already bound permission, source and schema evidence, never a new outer protocol or flags. Return only the common result keys `data`, `current_state`, `effects` and `errors`, with precise code/message/field errors and truthful known or unknown effects.

### Request and checks

1. accept the common explicit query, expected_state and authorization/context bindings. The caller supplies the declared Scope Unit frontier, lifecycle inclusion, logical predicates, requested result fields and any Subject profile/grammar evidence. Require the complete supplied criteria; do not select a default profile, lifecycle filter, currentness policy or omitted frontier.
2. mechanically resolve that supplied frontier and check request shape, current source/precondition evidence, permission and supported supplied validation authority. Public criteria use logical Atom/Scope Unit identity and values; paths, filenames, physical locators and list indexes are private and never public selectors.
3. apply all supplied predicates conjunctively. Subject fields are `governs`, `depends_on` or both; exact matches the complete scalar, prefix uses the explicitly supplied profile's lexical delimiter boundaries, suffix matches the literal end of the complete scalar without a delimiter-boundary requirement, and contains is literal containment. No mode infers ontology, relation, alias or semantic conformance.
4. check sources against the supplied syntax/eligibility criteria without repairing them. Preserve Atom/atom case distinction and explicit malformed, unreadable, ambiguous or incomplete-source diagnostics. Private occurrence evidence is not a public dependency-index contract.
5. return D625's data/current_state/effects/errors result: the exact complete empty, singular or multiple match set with logical Atom IDs, observed Versions, owning Scope Units and requested values, supplied-source attribution and truthful completeness. Effects are none. Do not hide an incomplete frontier as a successful complete match set.

## Details

Find Workflow O201 owns caller-level defaults, semantic criteria and result use. A Find-reference receiving request supplies explicit reference criteria; this connector only returns matching owners and never modifies references, substitutes successors, reads complete Atoms implicitly or invokes Modify.

D625 is the shared logical inner contract, not a new transport; D527's outer envelope remains unchanged. A current independently verified realization, exact definition/source pins and applicable Run recording remain prerequisites to an actual Run. No new MCP binding, runtime admission, Core adoption, retry/resume or Subject migration/publication is asserted.
