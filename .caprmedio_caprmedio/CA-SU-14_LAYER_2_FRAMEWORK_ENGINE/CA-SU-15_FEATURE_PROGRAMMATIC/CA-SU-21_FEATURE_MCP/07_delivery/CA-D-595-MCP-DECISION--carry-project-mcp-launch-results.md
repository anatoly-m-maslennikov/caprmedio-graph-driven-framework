---
atom_id: CA-D-595
ref_id: CA-D-595
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Action
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Carrier
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - MODEL//CAPRMEDIO <+ Runtime/Container Run
  - MODEL//CAPRMEDIO <+ Carrier/Docker Image
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Communication
tier: 3
relations:
  delivery_for:
  - CA-O-235
status: Active
version: 19
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-D-595-MCP-DECISION--carry-project-mcp-launch-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

carry Project MCP launch results

## Claim

### Prose Claim

the launcher **must** carry an attributable structured result that exposes a localhost MCP URL only after loopback Host/Origin-protected host readiness and never carries an HTTP credential.

## Details

### Safe launcher result

- Default result carries disposition (started, reused, refused, failed, or busy), exactly one CA-O-235 safe condition code, Project identity and safe root/control-root references, immutable image digest/fingerprint, service state, Docker-observed publication, and readiness disposition. A ready success alone carries one loopback /caprmedio/mcp URL; --output url is allowed only then. No Git-repository identity is required.
- Construct the URL only from one Docker-observed 127.0.0.1 publication after successful Host/Origin readiness. Never synthesize a port, return before readiness, or redirect through a proxy.
- Results and ordinary diagnostics omit password, bearer, Authorization, secret environment values, credential-file contents, command arguments, and secret URL components; this transport has no credential source.
- Refusal/failure remains complete structured output with no claimed replacement, queue/worker/Agent/Workflow start, Tool execution, Release effect, or cross-Project fallback. Bounded wait exhaustion is readiness failure, not ready.
