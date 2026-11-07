---
atom_id: CA-E-798
ref_id: CA-E-798
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 4
relations:
  evaluation_for:
  - CA-R-1106
  - CA-R-1108
  - CA-M-506
  - CA-D-704
status: Active
version: 1
updated_at: 2026-11-07 13:08:03 +0400
carrier_destination:
  file:
    name: CA-E-798-MCP-EVAL_CASE--verify-code-owned-mcp-registration-without-atom-discovery.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Verify code-owned MCP registration without Atom discovery

## Claim

### Prose Claim

Generate the MCP registration asset from installed provider code and code-owned inventory. Repeat with unchanged inputs and compare bytes. A provider addition, removal or descriptor/code change is reflected after generation; unlisted helper modules do not become exposed tools.

Start MCP against a Project root without a native Atom tree while making Atom catalog and selected-source manifest registration reads fail if called. Tool listing and a code-only test Tool call still work. Editing or removing an unrelated Atom does not change exposure or cause a generic registration freshness scan. Actual operation-level validation still rejects a request whose business prerequisites are missing.

Cover missing/malformed config, duplicate public names, configured exclusions, unavailable/changed provider code, source-only descriptors, typed request/result rejection, Workbench native tools and preserved selected-route protocols. No registration test grants permission to bypass an operation boundary.

Verify local release generates the asset before package identity/image startup, includes its bytes in package verification and stops before startup on generator failure. Verify the Dockerfile regenerates it on rebuild. Keep post-readiness discovery output separate and accurate. Compare unprofiled startup time and process memory with the prior same-source image; do not infer a permanent RSS saving from allocation estimates.

Verify equivalent MCP and web requests delegate to the same existing backend operation and preserve its response/error semantics. The MCP registration wrapper may validate and translate protocol data but must not introduce a second business implementation or extra internal HTTP transport.

Cover single-Project and shared-Project HTTP/MCP backend parity. Shared HTTP Workbench calls must reach the same native backend without constructing MCP request/result envelopes. Missing, foreign, stale or disabled Project/tool bindings remain rejected; cancellation releases its owner lease; normal results, partial-save outcomes, query errors and health observations retain their existing meaning.
