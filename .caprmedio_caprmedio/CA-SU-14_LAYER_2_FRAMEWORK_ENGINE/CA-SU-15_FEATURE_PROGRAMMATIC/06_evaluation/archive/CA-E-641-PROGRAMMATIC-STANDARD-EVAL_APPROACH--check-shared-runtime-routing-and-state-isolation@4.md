---
atom_id: CA-E-641
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-21T22:49:16Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  evaluation_for: [CA-R-2008, CA-M-401]
---
# Summary

Check shared-runtime routing and Project state isolation

## Scope

The shared Docker/MCP binding, bounded Project pool, public Tool frontier and
same-listener health view governed by CA-R-2008.

## Claim

Accept the shared-runtime increment only when a reproducible two-Project
verification world demonstrates explicit routing, concurrent state isolation,
truthful frontier conflicts and bounded resource behavior through one container
and one external HTTP MCP endpoint. This source defines required evidence; it
does not claim that active tests, deployment or installed adoption have
occurred.

## Details

- Build two disposable valid Projects under one configured host
  `projects_root`, with authoritative prefixes, distinct declarations,
  settings/model generations and identical local Run, receipt and result IDs.
  Exercise concurrent and interleaved Tool calls, asynchronous continuations,
  nested calls and reload boundaries. Verify each operation keeps its own
  source frontier, caches, locks, DBOS/Git/Journal records, outputs and
  results, including exact native payload preservation.
- Exercise missing, outside-root, symlink-substituted, mismatched
  prefix/control-root/full-identity, overlapping/ambiguous and
  global-working-directory-only selectors. Verify attributable refusal with no
  sibling fallback or effect. Cross-Project lookup of identical local IDs must
  refuse or resolve only under the qualified full identity.
- Set the pool bound to the default `max_loaded_projects = 2` and exercise a
  third accessible Project, idle eviction and busy admission. Verify bounded
  memory/context counts, deterministic idle-only eviction, busy refusal and no
  automatic retry, replay or remapping.
- Build the public frontier from valid native Project Tool contracts. Verify
  identical same-name input/output schemas share one endpoint, while a schema
  conflict quarantines and diagnoses only the affected Project Tool. Verify
  disabled/inactive Tools refuse, the outer `project_root` is added only at
  the native schema root with `$defs` preserved, native requests/results remain
  unchanged, and new names require explicit restart/client reconnect.
- Verify the health snapshot through the same configured listener: default,
  JSON and wildcard requests retain the ready boolean and `200/503` semantics;
  explicit HTML is escaped and contains no absolute paths, payloads, secrets or
  provider exception text. Host/Origin guards remain unchanged. Host readiness
  means initialized published frontier, not every Project job/cache; known
  contexts expose prefix and opaque identity separately, while unloaded/unknown
  contexts stay unknown. Health GETs perform no Tool, Workflow, DBOS, Docker,
  reload, mutation or replay.
- Verify host startup and other unbound service events do not invent a Project
  prefix, while request logs and results retain the actual bound prefix and
  opaque identity. Record that a read/write mount of all Projects provides
  application-level routing only, not OS-level hostile-workload isolation.
- Verify the single `INSTALL_TOOLS/install.py` CLI keeps `runtime` and
  `project` scopes separate and defaults both to dry-run. For `runtime`,
  check host-global Docker parameters, the outside-Project XDG data runtime,
  Codex hook and HTTP MCP registration, preservation of unrelated config,
  refusal of a conflicting CAPRMEDIO connection before effects, and the
  immutable-image/`--apply` handoff to the existing launcher. Without an
  image, verify configuration-only output does not claim a running service.
  For `project`, check selected-directory-only setup, explicit fresh prefix,
  minimal fresh settings/control/empty structure, preservation of existing
  Project carriers, canonical bundled thin Skill installation, refusal of
  missing/ambiguous/unsafe/conflicting inputs, and rollback that preserves
  concurrent edits. These source checks remain evidence to collect; the
  source record does not claim tests or runtime activation.

## Acceptance and failure disposition

Use an isolated nonproduction listener/state and frozen disposable fixture
inputs; do not mutate the production MCP port, home configuration or live
Project Atoms. Keep pass, fail, partial and unavailable evidence distinct.
Missing fixture, environment or live-gate evidence is unresolved, not a
successful behavioral result. A source projection, local test report or
written configuration does not prove deployment.
