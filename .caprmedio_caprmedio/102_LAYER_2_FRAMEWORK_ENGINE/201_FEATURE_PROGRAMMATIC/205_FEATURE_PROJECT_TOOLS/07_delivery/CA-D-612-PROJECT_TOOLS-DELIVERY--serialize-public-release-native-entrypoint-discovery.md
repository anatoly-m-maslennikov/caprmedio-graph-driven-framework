---
atom_id: CA-D-612
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Public Release/Native Entrypoint Discovery
  depends_on:
  - Subject/Engineering/Public Release/Native Entrypoint Discovery
  - Package
  - Capability Discovery
version: 7
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Serialize public-release native entrypoint discovery

## Scope

The native description surface of the public-release Tool.

## Claim

The public-release source **must** expose its stable `PUBLIC_RELEASE` identity and `PROJECT_TOOLS/PUBLIC_RELEASE/public_release.py` entrypoint. The direct `public.release` command uses this Project-bound implementation without a closed release-admission record or whole-registry validation gate.

## Details

Discovery describes the capability; it does not authorize Git or remote effects. Execute only on the Operator's public-release command for the selected Project and remote. Preserve the direct implementation's input, branch, URL and failure checks and its required full test suite, including integration tests.

This Delivery creates no alternate registry, caller-selected executor or standalone MCP adapter. The ordinary selected Workflows keep their own admission rules; removing obsolete release admission does not weaken them.
