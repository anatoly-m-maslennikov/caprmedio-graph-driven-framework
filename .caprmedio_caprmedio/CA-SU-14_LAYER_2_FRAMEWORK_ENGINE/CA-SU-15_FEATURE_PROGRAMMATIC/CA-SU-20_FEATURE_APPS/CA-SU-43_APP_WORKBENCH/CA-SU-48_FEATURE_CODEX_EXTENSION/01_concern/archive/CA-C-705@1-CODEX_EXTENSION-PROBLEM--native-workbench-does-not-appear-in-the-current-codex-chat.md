---
atom_id: CA-C-705@1
ref_id: CA-C-705@1
container:
  scope_unit: CA-SU-48
role: Concern
form: Problem
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workspace
tier: 5
relations:
  concern_about:
  - CA-R-2902
  - CA-M-476
  - CA-D-681
  - CA-E-684
status: Archived
version: 1
updated_at: 2026-11-07 00:45:56 +0400
carrier_destination:
  file:
    name: CA-C-705@1-CODEX_EXTENSION-PROBLEM--native-workbench-does-not-appear-in-the-current-codex-chat.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/01_concern/archive
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Native Workbench does not appear in the current Codex chat

## Concern

The Operator sees no Workbench interface after `workspace_open` in this Codex chat. The call returns the correct Workspace and declared Project name.

The released MCP advertises `ui://caprmedio/workbench.html` and serves the current self-contained artifact with MIME `text/html;profile=mcp-app`. The application bridge passes disposable-host tests. These checks do not prove that Codex mounts the UI.

## Evidence

The live descriptor and resource check is recorded in the CA-P-2710 release acceptance report. The Operator confirmed that nothing appeared. Computer Use cannot inspect Codex's own window.

Calls in this chat are exposed through `functions.exec`. That call path may explain the missing UI, but this is an inference. Neither a host limitation nor a cache fault has been established. No documented direct rendering action is available in this session.

## Impact

The released backend and browser Workbench work, but native Codex UI delivery does not meet CA-R-2902 yet. Native-host acceptance remains open.
