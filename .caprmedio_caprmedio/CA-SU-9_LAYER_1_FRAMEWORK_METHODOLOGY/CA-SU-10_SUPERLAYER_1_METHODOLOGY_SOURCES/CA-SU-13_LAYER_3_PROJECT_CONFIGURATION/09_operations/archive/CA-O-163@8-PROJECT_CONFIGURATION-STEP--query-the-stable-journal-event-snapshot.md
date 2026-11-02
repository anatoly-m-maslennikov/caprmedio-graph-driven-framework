---
atom_id: CA-O-163@8
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: "2026-10-19 15:57:09 +0400"
subjects:
  governs: "Find and Fetch Journal Events Query Step"
  depends_on: ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/History/Journal", "Entity/Node/Occurrent/Event", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Action Run"]
relations:
  relates_to: [CA-O-161, CA-O-162, CA-R-1861, CA-R-1866, CA-R-1867]
---
# Summary

Query the stable Journal Event snapshot

## Operation

This Step is the query node of CA-O-161 and invokes exactly one Action, CA-O-162, Query Journal Events.

### Inputs and parameters

Before workflow/action-start recording or Action dispatch, the adapter captures the selected Project's canonical Journal byte-prefix and binds one opaque snapshot token containing source-root identity, prefix byte length and hash, ordered member references, member byte hashes and actually supplied string Event IDs without deduplication or a unique-ID requirement. Capture every decoded row, including missing/nonstring IDs, repeated IDs, lists and scalars, without changing the recorded JSON. Query result wrappers use None when a string ID is absent; coverage follows actual rows, not Event-ID uniqueness. The Action consumes exactly that sealed frontier. A standalone Action captures before its own Run evidence. Bind the literal filter expression, requested result mode (`ids`, selected `fields`, or `full_events`), selected fields when applicable, and bounded page request. The token excludes this invocation's later Run/Event records and permits later append only outside the sealed prefix.

## Details

The Step accepts no filename identity, secret-bearing selection, arbitrary SQL/code, mutation parameter, or fallback Journal root. A failed or incomplete Action returns its actual diagnostic and does not fabricate a successful Workflow or Action Run.
