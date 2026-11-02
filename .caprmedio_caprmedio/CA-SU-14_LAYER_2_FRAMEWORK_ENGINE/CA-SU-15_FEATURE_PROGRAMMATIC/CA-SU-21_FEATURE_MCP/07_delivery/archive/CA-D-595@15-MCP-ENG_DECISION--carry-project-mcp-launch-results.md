---
atom_id: CA-D-595@15
content_role: Delivery
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Engineering/Architecture/Component Structure
  - Subject/Graph Node/Runtime/Container Run
  - Subject/Graph Node/Carrier/Docker Image
  - Subject/Graph Node/Engineering/Architecture/Communication
relations:
  delivery_for:
  - CA-O-235
type: Eng Decision
tier: 3
---
# Summary

carry Project MCP launch results

## Scope

the safe structured result Carrier returned by the bounded Project MCP launcher Action.

## Claim

the launcher **must** carry an attributable structured result that exposes a localhost MCP URL only after loopback Host/Origin-protected host readiness and never carries an HTTP credential.

## Details

- default result fields are the disposition (`started`, `reused`, `refused`, `failed`, or `busy`), exactly one CA-O-235 safe condition code, Project identity, safe selected-root/control-root references, immutable image digest/fingerprint, service identity/state, Docker-observed publication, and readiness disposition. A ready success additionally carries one loopback `/mcp` URL. `--output url` is permitted only for that ready success; a non-success stays structured and has no URL. It carries no Git-repository identity and does not require one.
- the URL is constructed only from the one Docker-observed `127.0.0.1` publication after successful Host/Origin-protected host readiness. No result synthesizes a port, returns a URL before readiness, or redirects through a proxy.
- result and ordinary diagnostics omit password, bearer, Authorization, secret-bearing environment values, credential-file contents, command arguments, and secret URL components. They do not identify a credential source because this transport has none.
- refusal/failure remains a complete structured result with no claimed container replacement, queue/worker/Agent/Workflow start, Tool execution, Release effect, or cross-Project fallback. Bounded wait exhaustion is a readiness failure, not a ready result.
