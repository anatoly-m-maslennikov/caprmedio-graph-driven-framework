---
atom_id: CA-P-2447@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 36
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 2
updated_at: '2026-10-20T13:57:26.000Z'
---
# Summary

Freeze the Subject grammar fixture and source-readability preflight

## Objective

Prepare one exact frozen Subject grammar fixture and prove its authoritative grammar source can be read before any Docker case is started.

## Details

Current owner: `prepare_validator_acceptance`. Preserve the exact selected grammar fixture, source location, and source fingerprint. Run only the read-only source preflight first; if the selected grammar source cannot be read, stop and record that boundary rather than substituting a fixture or weakening validation. Docker/runtime execution and production state are outside this Task.

At most15minutes ownwork, split before extending. Preserve exact predecessors and concurrent edits. No code, production MCP/Docker, Git, Journal, or report effects.

### Definition of Done

The frozen Subject grammar fixture is explicit and the exact authoritative grammar source is proven readable before Docker invocation, with source identity recorded. This narrow DoD does not claim Docker/runtime passage or production acceptance.

### Completion checkpoint

Accepted host-only preparation confirms the disposable `_capture_grammar(atom_operations,root,get_profile('approved'))` path materializes five approved grammar sources from `frozen_authority_fixture_bytes` at exact frozen profile paths with no live fallback; all pinned hashes match, compile/AST<=25 and diffcheck pass. This is source/fixture preparation only: no Docker or runtime proof, production acceptance, or P2448/C540 conclusion is claimed.
