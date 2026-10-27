---
atom_id: CA-O-105@13
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-24 17:18:27 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Select RMED Review Batch'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
relations:
  relates_to:
  - CA-D-496
  - CA-D-497
tier: 3
---
# Summary

Select a bounded RMED review batch

## Operation

Select RMED Review Batch **means** the read-only Action that resolves a requested selection into a bounded, reproducible local-review queue.

1. resolve the requested Scope Unit locally **or** with descendants, Global **or** Local Tiers, **or** explicit Carrier list from carried Properties **and** authoritative selection data; select active RMED source Atoms.
2. gather the relevant `atom_local` rules once: CCE, local Property encoding **and** domains, body structure, **and** Scope/Claim/Details/Summary coherence. supply their actual content **and** the vocabulary needed for case checks.
3. record the original selection **in** the CA-D-496 progress list, ordered by Atom ID, Revision, **then** path. retain malformed **or** missing identifiers as inspectable candidates sorted by path.
4. return the full selected queue **and** shared rules **to** the caller: `ready`, `empty` for a genuinely empty selection, **or** `blocked` for unresolved selection.

## Details

the caller handles reviewer dispatch **after** gathering finishes, resolves context headroom under CA-D-497, **and** supplies **`=1`** Atom per fresh reviewer with its full text **and** relevant rules. the caller **must** keep the configured headroom unused **and** distinguish observed runtime usage from estimated workload. the batch is a scheduling unit, **not** a multi-Atom reviewer context. keep shared rules once **without** copying the full methodology into **every** report. the caller supplies permissions **and** a temporary output directory. unavailable data blocks **only** an in-scope selection **or** check; excluded graph checks do **not** become coverage gaps.
