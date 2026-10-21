---
atom_id: CA-C-556
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2512, CA-P-2513]
version: 1
updated_at: "2026-10-21 04:36:13 +0400"
---
# Summary

Prepare the locked launcher environment before release

## Concern

A Python-version-only release preflight did not prove that the selected launcher virtualenv contained the locked groups. The no-sync release entered the full suite with missing mcp/anyio dependencies; isolated health checks had used the separately populated .venv.

## Evidences

Run local-20261021-mcp-health-0434 committed eligible changes at01ec043df and passed input validation, then module imports failed at tests. Root interrupted only the verified release process; its report/log are retained and owned suite parents exited. No image/install/startup phase ran and production MCP remained unchanged. Initial environment sync exposed a broken inherited /tmp/codex-uv-cache entry; selecting the existing project-local .caprmedio_tmp/cache/uv repaired it without deleting shared cache data.

The selected launcher virtualenv was synchronized from the unchanged uv.lock using uv sync --locked --all-groups, managed Python3.14 and the project-local cache. A fresh exact no-sync launcher invocation imports anyio, mcp, dbos, pydantic, yaml, jsonschema and tomlkit successfully and reports the selected launcher interpreter. Locked versions include mcp2.3.0, dbos2.31.1, pydantic2.13.5, PyYAML6.0.3, jsonschema4.26.0 and tomlkit0.15.1. This resolves environment preparation, not the full release gate.

## Blast radius

P2513 must use a fresh release Run ID and rerun every normal gate; no failed test is waived or counted as acceptance. Bind both UV_PROJECT_ENVIRONMENT and UV_CACHE_DIR to the verified project-local paths. Future release preparation must smoke-import the actual selected test dependencies, not just check Python version. The production container is unchanged; no live mutation test or held/uncertain Run replay occurred.
