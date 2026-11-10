---
atom_id: CA-C-490
ref_id: CA-C-490@2
container:
  scope_unit: CA-SU-24
role: Concern
form: Problem
topics:
  main_subject: Implementation Workflow/workspace admission
  dependencies:
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Carrier
relations:
  concern_about:
  - CA-P-1764
status: Archived
version: 2
updated_at: 2026-10-23 03:14:50 +0400
current_scope_unit: PROMPTS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-490@2-PROMPTS-PROBLEM--accept-safe-workspace-ancestor-aliases.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/01_concern/archive
---
# Summary

Accept safe workspace ancestor aliases

## Concern

A valid absolute workspace whose ancestor canonicalizes through a system alias is rejected before the Implementation Action can execute.

## Evidences

At commit c011b68fa, IMPLEMENTATION_WORKFLOW/implementation_actions.py:207 compares resolved and lexical paths. On macOS, /var resolves to /private/var. The focused tests test_selected_project_root_is_used_instead_of_immutable_code_root and test_fixed_test_first_path_performs_real_baseline_candidate_and_assertion reproduce blocked results instead of implemented/evaluation_ready.

## Blast radius

W09 implementation admission and the full release suite.

## Disposition

CA-P-1764 canonicalizes legitimate ancestors while retaining leaf-symlink and protected-authority overlap refusal. Validate with a platform-independent regression before resolving.
