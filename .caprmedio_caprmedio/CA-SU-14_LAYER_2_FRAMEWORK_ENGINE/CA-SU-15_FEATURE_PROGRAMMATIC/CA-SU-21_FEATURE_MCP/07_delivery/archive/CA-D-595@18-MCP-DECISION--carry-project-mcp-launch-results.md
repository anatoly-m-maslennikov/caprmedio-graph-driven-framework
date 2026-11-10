---
atom_id: CA-D-595
ref_id: CA-D-595@18
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Container Run
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 3
relations:
  delivery_for:
  - CA-O-235
status: Archived
version: 18
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-595@18-MCP-DECISION--carry-project-mcp-launch-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

carry Project MCP launch results

## Claim

### Prose Claim

the launcher **must** carry an attributable structured result that exposes a localhost MCP URL only after loopback Host/Origin-protected host readiness and never carries an HTTP credential.

## Details

### Scope

the safe structured result Carrier returned by the bounded Project MCP launcher Action.

- default result fields are the disposition (`started`, `reused`, `refused`, `failed`, or `busy`), exactly one CA-O-235 safe condition code, Project identity, safe selected-root/control-root references, immutable image digest/fingerprint, service identity/state, Docker-observed publication, and readiness disposition. A ready success additionally carries one loopback `/caprmedio/mcp` URL. `--output url` is permitted only for that ready success; a non-success stays structured and has no URL. It carries no Git-repository identity and does not require one.
- the URL is constructed only from the one Docker-observed `127.0.0.1` publication after successful Host/Origin-protected host readiness. No result synthesizes a port, returns a URL before readiness, or redirects through a proxy.
- result and ordinary diagnostics omit password, bearer, Authorization, secret-bearing environment values, credential-file contents, command arguments, and secret URL components. They do not identify a credential source because this transport has none.
- refusal/failure remains a complete structured result with no claimed container replacement, queue/worker/Agent/Workflow start, Tool execution, Release effect, or cross-Project fallback. Bounded wait exhaustion is a readiness failure, not a ready result.
