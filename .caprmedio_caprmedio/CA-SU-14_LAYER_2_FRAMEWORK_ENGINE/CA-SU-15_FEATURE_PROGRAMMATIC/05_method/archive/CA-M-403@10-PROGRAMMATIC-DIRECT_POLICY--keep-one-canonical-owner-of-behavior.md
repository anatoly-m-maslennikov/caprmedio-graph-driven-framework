---
identity:
  atom_id: CA-M-403@10
  ref_id: CA-M-403@10
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
      Structure
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
      Structure
  tier: 1
state:
  status: Archived
  version: 10
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-M-403@10-PROGRAMMATIC-DIRECT_POLICY--keep-one-canonical-owner-of-behavior.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Keep one canonical owner of behavior

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** expose a declared capability through different transports, adapters or storage backends, reuse its canonical behavioral owner rather than independently redefining its meaning.

## Details

Candidate source: [CA-M-387@2](archive/CA-M-387-PROGRAMMATIC-CORE--keep-one-canonical-owner-of-behavior@2.md)

- Adapters translate supported requests and results; they do not invent domain decisions or hidden Workflow composition.
- Keep identity, lifecycle, semantic admission and sequencing with their declared owner.
- Replacing a transport or backend must not silently change the declared capability.

Source basis: CA-M-341, CA-M-376.
