---
atom_id: CA-R-1906
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Target admission"
  depends_on: [Tool, Project, Project Structure, Settings, Registry, Operator]
relations:
  relates_to: [CA-D-600, CA-M-361]
---
# Summary

Require explicit target-Project bootstrap or adoption inputs

## Scope

the input boundary that identifies an installation target.

## Claim

the INSTALL_TOOLS facade **must** receive explicit target root, control child, bootstrap-or-adopt mode, settings, Project Structure and registry, and **must not** invent an Operator or missing target input.

## Details

Bootstrap admits a declared Project with an empty runtime boundary; adoption admits pre-existing Project metadata but still requires an empty active runtime boundary for CA-R-1881. Every input is reopened and digested into CA-D-600 before state is written. Ambiguous roots, absent controls, changed settings or inferred Operator identity refuse without effects.
