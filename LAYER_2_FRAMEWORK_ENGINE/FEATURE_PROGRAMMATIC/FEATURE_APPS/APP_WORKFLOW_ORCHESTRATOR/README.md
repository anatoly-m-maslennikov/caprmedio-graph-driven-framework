# Workbench runtime packaging

The workflow orchestrator, worker queues, selected handlers and AI Agent service
are retired. This legacy directory name remains only because the retained host
release and bootstrap use its [Docker runtime](docker/README.md) paths.

`docker/` contains the MCP/HTTP/shared-MCP container entry point, host launchers,
image selection and health support. The runtime exposes native Workbench tools.
There is no worker mode, DBOS dependency or Workflow execution interface.

Local/public release run through `FEATURE_PROJECT_TOOLS/release.py` on the host.
Subject/Topics views use the standalone renderers under
`FEATURE_TOOLS/GENERATE_ENTITY_GRAPH`.

Technical diagnostics use stdout/stderr and the configured Docker retention.
Workbench saved-query changes and host release events retain their internal
business Journal recording. No public Journal-appender Tool is exposed.

See [the retirement boundary](../../../../.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/CA-P-2849-WORK_REPORT--2848.md) for retained dependencies,
verification and deployment limits.
