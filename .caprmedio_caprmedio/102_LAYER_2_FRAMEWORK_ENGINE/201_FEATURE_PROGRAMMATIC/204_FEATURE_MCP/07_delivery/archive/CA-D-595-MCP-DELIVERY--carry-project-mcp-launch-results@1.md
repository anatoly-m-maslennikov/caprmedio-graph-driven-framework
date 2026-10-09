---
atom_id: CA-D-595
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:42:28 +0000"
subjects:
  governs: "MCP/Project launcher/result Carrier"
  depends_on: [Action, Project, MCP, Gateway, Docker Runtime, Image, Credential, HTTP, Carrier]
relations:
  delivery_for: [CA-O-188]
  relates_to: [CA-D-593, CA-D-594, CA-D-578]
---
# Summary

carry Project MCP launch results

## Scope

the safe structured result Carrier returned by the bounded Project MCP launcher Action.

## Claim

the launcher **must** carry an attributable structured result that exposes a localhost MCP URL only after authenticated host readiness and never carries a credential.

## Details

- default result fields are the disposition (`started`, `reused`, `refused`, `failed`, or `busy`), exactly one CA-O-188 safe condition code, Project identity, safe selected-root/control-root references, immutable image digest/fingerprint, service identity/state, Docker-observed publication, and readiness disposition. A ready success additionally carries one loopback `/mcp` URL. `--output url` is permitted only for that ready success; a non-success stays structured and has no URL. It carries no Git-repository identity and does not require one.
- the URL is constructed only from the one Docker-observed `127.0.0.1` publication after successful authenticated host readiness. No result synthesizes a port, returns a URL before readiness, or redirects through a proxy.
- result and ordinary diagnostics omit token bytes, bearer values, secret-bearing environment values, credential-file contents, command arguments, and secret URL components. They may identify the credential-source kind without exposing its value.
- refusal/failure remains a complete structured result with no claimed container replacement, queue/worker/Agent/Workflow start, Tool execution, Release effect, or cross-Project fallback. Bounded wait exhaustion is a readiness failure, not a ready result.
