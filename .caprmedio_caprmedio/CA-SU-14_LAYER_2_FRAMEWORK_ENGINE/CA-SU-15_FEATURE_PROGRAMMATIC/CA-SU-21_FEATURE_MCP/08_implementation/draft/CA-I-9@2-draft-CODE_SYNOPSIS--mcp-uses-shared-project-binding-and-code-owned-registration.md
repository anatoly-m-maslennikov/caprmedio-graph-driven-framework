---
identity:
  id: CA-I-9@2-draft
  ref_id: CA-I-9@2-draft
context:
  container:
    scope_unit: CA-SU-21
  role: Implementation
  form: Code Synopsis
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  tier: 3
state:
  status: Draft
  version: 2
  updated_at: 2026-11-09 22:40:16 +0400
destination:
  file:
    name: CA-I-9@2-draft-CODE_SYNOPSIS--mcp-uses-shared-project-binding-and-code-owned-registration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/08_implementation/draft
author: Anatoly Maslennikov
---

## Summary

MCP uses shared Project binding and code-owned registration

## Claim

### Prose Claim

The inspected MCP code validates an explicit Project binding, registers configured code-owned routes and shares Workbench handlers. Hot reload is opt-in. Existing release and entrypoint code already wires catalog generation and the shared HTTP server.

**Code locations and review notes**

[shared_gateway.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/shared_gateway.py) validates the outer Project selection before dispatch.

[selected_route_registration.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/selected_route_registration.py) registers configured selected routes; source admission remains an invocation check.

[direct_gateway.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/direct_gateway.py) serves tools in process while reload is disabled.

[hot_reload.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/hot_reload.py) requires CAPRMEDIO_HOT_RELOAD=1 to enable reload.

[generate_tools_catalog.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tools_catalog.py) pages tools/list without invoking a Tool.

[entrypoint.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/entrypoint.py) already constructs the shared HTTP command. [local_release.py](../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/RELEASE_VERSION/local_release.py) already calls catalog generation after delivery/readiness checks. Absence of a caller inside the MCP package is not missing integration.

Inspection on 9 November 2026, current working tree. This review inspected code only; it did not execute MCP, release or readiness checks.
