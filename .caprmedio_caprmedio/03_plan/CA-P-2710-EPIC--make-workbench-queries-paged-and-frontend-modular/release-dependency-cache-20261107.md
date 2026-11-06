# Local-release dependency cache miss

The release passed 252 tests in 35 selected modules and launcher integration, then failed before deployment at prepare_candidate_image. The running MCP was not replaced.

Dockerfile copies version.toml before uv sync. Every release-version change invalidates the dependency layer. The r2 BuildKit record 8t4jqazq58irzofrvw8pm6460 shows repeated downloads of 53 packages and cancellation after 9 minutes in that step. Current-code test image838569baed56ab1d96fd974b52d5c129fb42087636765f641be729ed4b413db5 reused the dependency layer.

A prepared two-file patch moves version.toml COPY after dependency installation and keeps version delivery tested. It is not applied: Dockerfile/tests belong to WORKFLOW_ORCHESTRATOR, outside the Operator's Workbench-only code scope. Cross-thread handoff to CA #3 was rejected by automatic approval review because destination permission was not confirmed; no message was delivered.
