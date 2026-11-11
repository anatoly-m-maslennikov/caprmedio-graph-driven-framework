---
identity:
  id: CA-I-6
  ref_id: CA-I-6@1-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Implementation
  form: Code Synopsis
  tier: 8
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit//PROGRAMMATIC
relations:
  DEPENDS_ON:
    atom:
    - CA-R-2008
    - CA-D-640
state:
  status: Draft
  version: 1
  updated_at: 2026-11-09 00:29:04 +0400
destination:
  file:
    name: CA-I-6@1-draft-PROGRAMMATIC-CODE_SYNOPSIS--the-declared-installer-has-no-implementation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/08_implementation/draft/engine-refinement-20261108
author: Anatoly Maslennikov
---

## Summary

The declared installer has no implementation

## Claim

### Prose Claim

The code snapshot has no INSTALL_TOOLS/install.py command. The specification still assigns runtime and project installation commands to that path. Existing bootstrap, shared-launcher and gateway modules implement other parts of host startup and Project binding; their existence does not implement the missing installer.

## Details

The Operator excluded older Tool rebuilding from this Epic. This gap remains in that excluded perimeter; no installer was added or silently substituted during Workbench refinement.

Code snapshot: `b8da4472e53a99370a27fae54f8cde8e08e2ad3d`. The missing Project-relative path is `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/INSTALL_TOOLS/install.py`. The file is absent from both that snapshot and the observed checkout. These observations do not establish runtime behavior or deployment.

| Existing code location | SHA-256 at snapshot |
| --- | --- |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/project_mcp_bootstrap.py` | `725b5eeaf5a924ec1e0dd9b0302f5932bd2e46111dac75f707ef03ae4061a900` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/shared_mcp_launcher.py` | `ff01697d1a269cf66133c14a490b5825c805bc405cd7476b5bc94bf5320ba3ab` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/shared_gateway.py` | `79ed8347de9b346d4d2a36e1438cbafa33c4b8ef4bfe7d4faf0f654594a14f26` |
