---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Extension
  depends_on:
  - Subject/Engineering/Extension
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis/Type: Analysis Report'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern'
  - Subject/Engineering/Tool
  - Subject/Engineering/MCP
  - Subject/Engineering/Skill
version: 15
updated_at: 2026-10-25 01:28:32 +0400
relations:
  evaluation_for:
  - CA-M-290
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Evaluation
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-E-468@15
type: Eval Case
tier: 3
---
# Verify one CAPRMEDIO-aligned FPF Extension revision

## Claim checked

CA-M-290 produces one immutable project-local FPF Extension revision that is CAPRMEDIO-aligned, directly invokable, correctly persistent, asynchronously safe, **and** separately installable **and** activatable.

## Applicable when

Apply **before** publishing, installing, activating, updating, downgrading, **or** reloading **any** FPF Extension revision.

## Test case

Materialize the same pinned upstream revision **and** ordered overlay twice; install one result **without** activation; **then** activate it separately **and**, **in** fresh Codex sessions, exercise direct `$fpf` routing, one persistent analysis, one explicit Question Concern request, one ordinary non-persistent question, one Hook-triggered deferred action, one hung Tool, one hung MCP request, one hung worker, independent recovery `status`, `stop`, `start`, **and** `reload`, automatic retry-budget exhaustion, restart recovery, **and** rollback **to** the prior selected revision.

## Acceptance criteria

Both builds have identical manifests, inventories, **and** digests. Installation changes no applicable methodology **and** mutates neither upstream nor user-global FPF sources. Activation selects exactly the installed revision. Direct `$fpf` needs no `ca` wrapper. The Analysis Report is a valid `CA-A` Carrier **in** the correct narrowest `02_analysis/`; the explicit Concern is a valid one-Claim `CA-C` Carrier **in** the correct `01_concern/`; the ordinary question persists nothing. Hook acknowledgement returns within its declared bound **without** waiting for worker work. Manual recovery controls remain bounded **and** responsive while the Hook, Tool, MCP request, manager, **or** worker is hung; the automatic supervisor performs no domain effect; accepted work survives stop, reload, **and** restart **without** duplicate effects; **and** exhausted automatic recovery opens a visible circuit. Rollback restores the exact prior selection **and** installed state.

## Failure disposition

Reject the Extension revision **and** preserve the sealed source frontier, manifests, inventories, digests, installation **and** activation receipts, fresh-session discovery evidence, generated Atom diagnostics, Hook latency, queue **and** worker traces, lifecycle actions, circuit state, **and** rollback evidence.
