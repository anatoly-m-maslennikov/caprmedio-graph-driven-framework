---
atom_id: CA-O-047@5
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
cce_version: cce_1
cce_form: definition
subjects:
  governs: Read Atom Carriers
  depends_on:
  - Action
  - Tool/ATOM_READ
  - Subject/Domain/Node/Continuant/Atom
  - Artifact/Carrier
  - Scope Unit
version: 5
updated_at: 2026-10-23 03:06:32 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to: [CA-R-1936, CA-M-376, CA-D-625]
---
# Read selected CAPRMEDIO Atom carriers

Read Atom Carriers **means** the read-only full-read Action through the common connector interface in CA-D-625, CA-R-1936 and CA-M-376. Operation is `read`; the caller supplies one explicit logical Atom ID target and authorization/context fixing its source view. An ordinary Read needs no pre-known Version; optional pinned/historical Version or expected_state is enforced exactly. It is callable independently of Find or Modify.

Use D625's closed inner request keys `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` and `context`. Exactly one of target or query is non-null; target is `{kind, identity}`, query is `{kind, filters}`. Query/read use null delta; modify receives explicit supplied edits. Modify requires expected current state; Create requires expected absence. An ordinary explicit-ID Read returns its actual exact Version/state token without requiring a pre-known Version; optional pinned/historical Read Version and expected_state must match exactly. Do not invent a Scope Unit Version. Authorization/context reference already bound permission, source and schema evidence, never a new outer protocol or flags. Return only the common result keys `data`, `current_state`, `effects` and `errors`, with precise code/message/field errors and truthful known or unknown effects.

## Action

1. mechanically resolve exactly the supplied logical Atom ID against the source view fixed by target/context. Return its actual exact Version and state token. If the caller supplies a pinned/historical Version or expected_state, enforce that exact match. Missing, ambiguous, stale or unavailable evidence returns a structured error; do not choose a guessed latest Version, lifecycle model, replacement successor, hidden query or different target.
2. check the common request, supplied preconditions, permission and current source evidence, then read the complete Atom faithfully. Preserve all Properties, Sections and source values without normalization, repair or identity decisions.
3. return D625's data/current_state/effects/errors result containing the full logical Atom, observed ID/Version and exact state token, owning Scope Unit and supplied source attribution. Effects are none. Optional private Carrier display is diagnostic only; storage paths, filename stems and list indexes are not public targeting fields.
4. a receiving Workflow may independently invoke this Action for each of its explicit targets. This connector neither selects a batch nor decides next-target progression, retry or resume.

## Outcome and stops

Return the exact full Atom or the precise missing, ambiguous, stale, unreadable, unsupported or out-of-scope structured outcome. No Find prerequisite, write, mutation, automatic retargeting or inferred lifecycle transition follows.

D625 is the shared logical inner contract, not a new transport; D527's outer envelope remains unchanged. Actual Run realization, current definition/source pins, permission and shared recording require independent verification. This definition advertises no new runnable binding, MCP activation, Core adoption or migration publication.
